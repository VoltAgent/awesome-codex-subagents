#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEAM="$ROOT/teams/product-engineering"
FORCE=0
TARGET=""
usage(){ echo "Usage: $0 [--force] /path/to/target-repo" >&2; }
while [[ $# -gt 0 ]]; do
  case "$1" in
    --force) FORCE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) [[ -z "$TARGET" ]] || { usage; exit 2; }; TARGET="$1"; shift ;;
  esac
done
[[ -n "$TARGET" ]] || { usage; exit 2; }
TARGET="$(cd "$TARGET" && pwd)"
[[ -d "$TARGET/.git" ]] || { echo "Target is not a git repository root: $TARGET" >&2; exit 1; }
for p in "$TEAM/AGENTS.md" "$TEAM/config.toml" "$TEAM/agents" "$TEAM/contracts" "$TEAM/policies"; do
  [[ -e "$p" ]] || { echo "Missing team source: $p" >&2; exit 1; }
done
conflicts=()
[[ -e "$TARGET/AGENTS.md" ]] && conflicts+=("AGENTS.md")
[[ -e "$TARGET/.codex/config.toml" ]] && conflicts+=(".codex/config.toml")
for src in "$TEAM"/agents/*.toml; do
  dest="$TARGET/.codex/agents/$(basename "$src")"
  [[ -e "$dest" ]] && conflicts+=("${dest#$TARGET/}")
done
if (( ${#conflicts[@]} > 0 && FORCE == 0 )); then
  echo "Refusing to overwrite existing files:" >&2
  printf '  - %s\n' "${conflicts[@]}" >&2
  echo "Merge existing instructions/config manually or rerun with --force when replacement is intentional." >&2
  exit 1
fi
mkdir -p "$TARGET/.codex/agents" "$TARGET/.codex/team/contracts" "$TARGET/.codex/team/policies"
cp "$TEAM/AGENTS.md" "$TARGET/AGENTS.md"
cp "$TEAM/config.toml" "$TARGET/.codex/config.toml"
cp "$TEAM"/agents/*.toml "$TARGET/.codex/agents/"
cp "$TEAM"/contracts/*.md "$TARGET/.codex/team/contracts/"
cp "$TEAM"/policies/*.md "$TARGET/.codex/team/policies/"
echo "Installed autonomous product team into $TARGET"
echo "Open the target repository in a NEW Codex session, then describe the application/feature/bug to deliver."
