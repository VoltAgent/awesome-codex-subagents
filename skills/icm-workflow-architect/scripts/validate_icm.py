#!/usr/bin/env python3
"""Validate deterministic structural invariants of an ICM workspace or skill."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


STAGE_NAME = re.compile(r"^(?P<number>\d{2})[-_][a-z0-9]+(?:[-_][a-z0-9]+)*$")
PLACEHOLDER = re.compile(r"\{\{[?/]?[A-Z][A-Z0-9_]*\}\}")
BACKTICK = re.compile(r"`([^`]+)`")
HEADING = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Issue:
    level: str
    message: str


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)


def section(text: str, name: str) -> str | None:
    match = re.search(
        rf"^##\s+{re.escape(name)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        text,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else None


def headings(text: str) -> set[str]:
    return {match.group(1).strip().casefold() for match in HEADING.finditer(text)}


def validate_contract(path: Path, root: Path, issues: list[Issue]) -> None:
    text = path.read_text(encoding="utf-8")
    names = headings(text)
    for required in ("inputs", "process", "outputs"):
        if required not in names:
            issues.append(Issue("ERROR", f"{relative(path, root)}: missing '## {required.title()}'"))

    if "human check" not in names and "checkpoints" not in names:
        issues.append(
            Issue(
                "ERROR",
                f"{relative(path, root)}: missing '## Human Check' or '## Checkpoints'",
            )
        )

    line_count = len(text.splitlines())
    if line_count > 80:
        issues.append(
            Issue("WARN", f"{relative(path, root)}: {line_count} lines; target is 80 or fewer")
        )

    inputs = section(text, "Inputs")
    if inputs is None:
        return

    for line in inputs.splitlines():
        if "reference" not in line.casefold():
            continue
        for raw in BACKTICK.findall(line):
            candidate = raw.strip()
            if not candidate.endswith(".md"):
                continue
            if any(token in candidate for token in ("{", "}", "*", "<", ">")):
                continue
            target = Path(candidate)
            if not target.is_absolute():
                target = path.parent / target
            if not target.exists():
                issues.append(
                    Issue(
                        "ERROR",
                        f"{relative(path, root)}: stable reference does not exist: {candidate}",
                    )
                )


def find_stage_dirs(root: Path) -> list[Path]:
    stages_root = root / "stages"
    if not stages_root.is_dir():
        return []
    return sorted(path for path in stages_root.iterdir() if path.is_dir())


def validate(root: Path, allow_placeholders: bool) -> list[Issue]:
    issues: list[Issue] = []

    entry_files = [root / name for name in ("SKILL.md", "AGENTS.md", "CLAUDE.md") if (root / name).is_file()]
    if not entry_files:
        issues.append(Issue("ERROR", "missing entry file: expected SKILL.md, AGENTS.md, or CLAUDE.md"))

    route = root / "CONTEXT.md"
    stage_dirs = find_stage_dirs(root)
    if stage_dirs and not route.is_file():
        issues.append(Issue("ERROR", "staged workspace is missing root CONTEXT.md"))

    stage_numbers: list[int] = []
    for stage_dir in stage_dirs:
        match = STAGE_NAME.fullmatch(stage_dir.name)
        if not match:
            issues.append(
                Issue(
                    "ERROR",
                    f"{relative(stage_dir, root)}: stage name must match NN-kebab-name or NN_kebab-name",
                )
            )
            continue
        stage_numbers.append(int(match.group("number")))

        contract = stage_dir / "CONTEXT.md"
        if not contract.is_file():
            issues.append(Issue("ERROR", f"{relative(stage_dir, root)}: missing CONTEXT.md"))
        else:
            validate_contract(contract, root, issues)

        output = stage_dir / "output"
        if not output.is_dir():
            issues.append(Issue("ERROR", f"{relative(stage_dir, root)}: missing output/ directory"))
        elif not any(output.iterdir()):
            issues.append(
                Issue("WARN", f"{relative(output, root)}: empty directory should contain .gitkeep if tracked")
            )

    if not stage_dirs:
        compact_contracts = [
            path
            for path in markdown_files(root)
            if {"inputs", "process", "outputs"}.issubset(headings(path.read_text(encoding="utf-8")))
        ]
        if compact_contracts:
            issues.append(Issue("WARN", "no stages/ directory; validating as a compact single-stage ICM"))
        else:
            issues.append(Issue("ERROR", "no stages/ directory and no compact Inputs/Process/Outputs contract"))

    if stage_numbers:
        if len(stage_numbers) != len(set(stage_numbers)):
            issues.append(Issue("ERROR", "duplicate stage numbers"))
        ordered = sorted(set(stage_numbers))
        if ordered[0] != 1:
            issues.append(Issue("WARN", f"stage numbering starts at {ordered[0]:02d}, not 01"))
        expected = list(range(ordered[0], ordered[-1] + 1))
        if ordered != expected:
            issues.append(Issue("WARN", f"stage numbering has gaps: found {ordered}"))

    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        unresolved = sorted(set(PLACEHOLDER.findall(text)))
        if unresolved and not allow_placeholders:
            sample = ", ".join(unresolved[:4])
            suffix = " ..." if len(unresolved) > 4 else ""
            issues.append(
                Issue(
                    "ERROR",
                    f"{relative(path, root)}: unresolved setup placeholders: {sample}{suffix}",
                )
            )

        if "references" in path.parts or "_shared" in path.parts:
            line_count = len(text.splitlines())
            if line_count > 200:
                issues.append(
                    Issue("WARN", f"{relative(path, root)}: {line_count} lines; split focused references above 200")
                )

    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="ICM workspace or repo-local skill root")
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="permit {{PLACEHOLDER}} tokens in an intentionally unconfigured template",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return a failure status when warnings are present",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    issues = validate(root, args.allow_placeholders)
    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARN"]

    print(f"ICM validation: {root}")
    for issue in issues:
        print(f"{issue.level}: {issue.message}")
    if not issues:
        print("PASS: deterministic structural checks passed")
    print(f"Summary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
