#!/usr/bin/env python3
"""Safely initialize the minimal files for an LLM-maintained Markdown wiki."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import sys


SCHEMA_TEMPLATE = """# LLM Wiki Schema

## Purpose

- Domain: Unspecified; define before the first domain-specific ingest.
- Audience: The project owner unless a broader scope is defined.
- Recurring questions: Add them as usage reveals stable needs.

## Layers

- Raw sources: `{sources_dir}/` — human-curated and immutable to the agent.
- Compiled wiki: `{wiki_dir}/` — agent-maintained Markdown.
- Schema: `{schema_file}` — this project contract.

## Paths and identity

- Index: `{wiki_dir}/index.md`
- Log: `{wiki_dir}/log.md`
- Source IDs: source-relative paths until a stronger stable-ID convention is defined
- Page naming and aliases: descriptive lowercase kebab-case filenames with aliases recorded on the canonical page

## Knowledge model

- Entity types: introduce only after observing the domain
- Relationship types: supports, contradicts, supersedes; add domain types only as needed
- Claim states: active, contested, superseded

## Provenance

Every material factual claim cites a stable source ID and the most precise available locator. Mark agent inference explicitly. Do not treat repeated copies of one upstream claim as independent support.

## Page contract

Pages should state their kind, status, created and updated dates, supporting source IDs, current understanding, evidence, relationships, contradictions, and open questions when those fields are relevant.

## Operations

- Ingest: integrate the source into all affected pages, update the index, and append to the log.
- Query: search the wiki first and verify decisive or contested claims against raw sources.
- Crystallize: file reusable work only when requested or explicitly authorized.
- Lint: audit by default; repair only when requested or explicitly authorized.
- Schema changes: log the reason and preserve interpretability of older pages.

## Privacy and governance

Do not propagate credentials, tokens, private material, or unnecessary PII into generated pages. Generated knowledge inherits the most restrictive scope of its sources until a broader scope is explicitly defined. Bulk deletion, merge, or export must be audited and reversible where practical.

## Scale triggers

Start with the index. Add lifecycle rules, graph structure, dedicated search, automation, and writer coordination only when observed usage justifies them.
"""

INDEX_TEMPLATE = """# Wiki Index

This is the content-oriented catalog of the wiki. Keep entries current and organize them by domain-relevant category as the wiki grows.

## Pages

<!-- Add: - [Page title](path.md) — one-line current description. -->
"""

LOG_TEMPLATE = """# Wiki Log

This is the append-only chronological audit trail for ingests, crystallizations, lint repairs, and schema changes.

## [{today}] bootstrap | Initialized LLM Wiki

- Created the minimal source, wiki, schema, index, and log structure.
"""


def relative_path(value: str, option: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise argparse.ArgumentTypeError(
            f"{option} must be a relative path contained by the project root"
        )
    if not path.parts or str(path) in {"", "."}:
        raise argparse.ArgumentTypeError(f"{option} must not be empty")
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a minimal LLM Wiki without overwriting existing files."
    )
    parser.add_argument(
        "root", nargs="?", default=".", help="Project root (default: current directory)"
    )
    parser.add_argument("--sources-dir", default="raw", help="Relative raw-source directory")
    parser.add_argument("--wiki-dir", default="wiki", help="Relative compiled-wiki directory")
    parser.add_argument(
        "--schema-file",
        default=".llm-wiki/schema.md",
        help="Relative schema file path",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print planned actions without writing"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        sources_rel = relative_path(args.sources_dir, "--sources-dir")
        wiki_rel = relative_path(args.wiki_dir, "--wiki-dir")
        schema_rel = relative_path(args.schema_file, "--schema-file")
    except argparse.ArgumentTypeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    root = Path(args.root).expanduser().resolve()
    if sources_rel == wiki_rel or sources_rel in wiki_rel.parents or wiki_rel in sources_rel.parents:
        print("error: source and wiki directories must not overlap", file=sys.stderr)
        return 2
    if schema_rel == sources_rel or sources_rel in schema_rel.parents or schema_rel in sources_rel.parents:
        print("error: the schema must not be inside or overlap the raw-source directory", file=sys.stderr)
        return 2
    if schema_rel in {wiki_rel / "index.md", wiki_rel / "log.md"}:
        print("error: the schema must not replace the wiki index or log", file=sys.stderr)
        return 2

    for relative in (sources_rel, wiki_rel, schema_rel):
        target = (root / relative).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            print(
                f"error: {relative} resolves outside the project root, possibly through a symlink",
                file=sys.stderr,
            )
            return 2

    directories = [root / sources_rel, root / wiki_rel, root / schema_rel.parent]
    files = {
        root / schema_rel: SCHEMA_TEMPLATE.format(
            sources_dir=sources_rel.as_posix(),
            wiki_dir=wiki_rel.as_posix(),
            schema_file=schema_rel.as_posix(),
        ),
        root / wiki_rel / "index.md": INDEX_TEMPLATE,
        root / wiki_rel / "log.md": LOG_TEMPLATE.format(today=date.today().isoformat()),
    }

    for directory in directories:
        action = "exists" if directory.exists() else "create directory"
        print(f"{action}: {directory}")
        if not args.dry_run:
            directory.mkdir(parents=True, exist_ok=True)

    for path, content in files.items():
        if path.exists():
            print(f"skip existing file: {path}")
            continue
        print(f"create file: {path}")
        if not args.dry_run:
            path.write_text(content, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
