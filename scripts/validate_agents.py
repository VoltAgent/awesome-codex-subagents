#!/usr/bin/env python3
"""Validate Codex custom agent TOML files."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
AGENT_FILES = sorted((ROOT / "categories").glob("*/*.toml"))
REQUIRED = {
    "name": str,
    "description": str,
    "developer_instructions": str,
}
ALLOWED_MODELS = {"gpt-5.6-sol", "gpt-5.6-terra"}
ALLOWED_EFFORTS = {"low", "medium", "high", "xhigh", "max", "ultra"}
ALLOWED_SANDBOXES = {"read-only", "workspace-write", "danger-full-access"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        with path.open("rb") as handle:
            data = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return [f"invalid TOML: {exc}"]

    for key, expected_type in REQUIRED.items():
        value = data.get(key)
        if not isinstance(value, expected_type) or not value.strip():
            errors.append(f"{key} must be a non-empty {expected_type.__name__}")

    if data.get("name") != path.stem:
        errors.append(f"name must match filename: expected {path.stem!r}")

    if data.get("model") not in ALLOWED_MODELS:
        errors.append(f"unsupported model: {data.get('model')!r}")

    if data.get("model_reasoning_effort") not in ALLOWED_EFFORTS:
        errors.append(
            f"unsupported model_reasoning_effort: "
            f"{data.get('model_reasoning_effort')!r}"
        )

    if data.get("sandbox_mode") not in ALLOWED_SANDBOXES:
        errors.append(f"unsupported sandbox_mode: {data.get('sandbox_mode')!r}")

    return errors


def main() -> int:
    if not AGENT_FILES:
        print("No agent files found.", file=sys.stderr)
        return 1

    failures = 0
    names: dict[str, Path] = {}

    for path in AGENT_FILES:
        errors = validate(path)
        try:
            with path.open("rb") as handle:
                name = tomllib.load(handle).get("name")
        except (OSError, tomllib.TOMLDecodeError):
            name = None

        if isinstance(name, str) and name in names:
            errors.append(f"duplicate name also used by {names[name].relative_to(ROOT)}")
        elif isinstance(name, str):
            names[name] = path

        if errors:
            failures += 1
            relative = path.relative_to(ROOT)
            for error in errors:
                print(f"{relative}: {error}", file=sys.stderr)

    if failures:
        print(f"Validation failed: {failures}/{len(AGENT_FILES)} files", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    for path in AGENT_FILES:
        with path.open("rb") as handle:
            model = tomllib.load(handle)["model"]
        counts[model] = counts.get(model, 0) + 1

    summary = ", ".join(f"{model}={count}" for model, count in sorted(counts.items()))
    print(f"Validated {len(AGENT_FILES)} agents ({summary}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
