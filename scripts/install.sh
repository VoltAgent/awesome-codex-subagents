#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)

scope=global
preset=everyday
force=false
dry_run=false

usage() {
    printf '%s\n' \
        "Usage: $0 [--scope global|project] [--preset everyday|all] [--force] [--dry-run]" \
        "" \
        "Defaults to the everyday preset in the global Codex agents directory."
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --scope)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            scope=$2
            shift 2
            ;;
        --preset)
            [ "$#" -ge 2 ] || { usage >&2; exit 2; }
            preset=$2
            shift 2
            ;;
        --force)
            force=true
            shift
            ;;
        --dry-run)
            dry_run=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            printf 'Unknown option: %s\n' "$1" >&2
            usage >&2
            exit 2
            ;;
    esac
done

case "$scope" in
    global)
        codex_root=${CODEX_HOME:-"${HOME}/.codex"}
        destination=$codex_root/agents
        ;;
    project)
        destination=$(pwd)/.codex/agents
        ;;
    *)
        printf 'Invalid scope: %s\n' "$scope" >&2
        exit 2
        ;;
esac

case "$preset" in
    everyday)
        source_list=$repo_root/presets/everyday-development.txt
        ;;
    all)
        source_list=
        ;;
    *)
        printf 'Invalid preset: %s\n' "$preset" >&2
        exit 2
        ;;
esac

if [ "$dry_run" = false ]; then
    mkdir -p "$destination"
fi

installed=0
skipped=0

install_one() {
    relative_path=$1
    source_file=$repo_root/$relative_path
    target_file=$destination/$(basename -- "$relative_path")

    if [ ! -f "$source_file" ]; then
        printf 'Missing source: %s\n' "$relative_path" >&2
        exit 1
    fi

    if [ -e "$target_file" ] && [ "$force" = false ]; then
        printf 'skip     %s (already exists)\n' "$target_file"
        skipped=$((skipped + 1))
        return
    fi

    if [ "$dry_run" = true ]; then
        printf 'would install %s\n' "$target_file"
    else
        cp "$source_file" "$target_file"
        printf 'installed %s\n' "$target_file"
    fi
    installed=$((installed + 1))
}

if [ "$preset" = everyday ]; then
    while IFS= read -r relative_path || [ -n "$relative_path" ]; do
        case "$relative_path" in
            ''|'#'*) continue ;;
        esac
        install_one "$relative_path"
    done < "$source_list"
else
    for source_file in "$repo_root"/categories/*/*.toml; do
        relative_path=${source_file#"$repo_root/"}
        install_one "$relative_path"
    done
fi

printf 'Done: %s selected, %s skipped. Destination: %s\n' "$installed" "$skipped" "$destination"
