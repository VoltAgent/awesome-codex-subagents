# LLM Wiki Skill

`llm-wiki` is a reusable Codex skill for building and maintaining a persistent, interlinked Markdown knowledge base from curated sources.

Instead of retrieving raw document fragments from scratch for every question, the skill incrementally compiles source material into a maintained wiki. New evidence updates existing entity and topic pages, records contradictions and supersession, preserves provenance, and strengthens the knowledge base over time.

## What it supports

- **Bootstrap:** Create a minimal wiki with immutable raw sources, generated Markdown pages, a content index, an append-only log, and a project-specific schema.
- **Ingest:** Integrate a source into every affected page rather than producing an isolated summary.
- **Query:** Search the compiled wiki, follow relationships, verify important claims against raw sources, and answer with citations.
- **Crystallize:** Turn research, debugging sessions, comparisons, and decisions into durable knowledge.
- **Lint:** Find unsupported claims, contradictions, stale knowledge, broken links, duplicate entities, privacy leaks, and schema drift.
- **Evolve:** Add lifecycle management, typed relationships, scalable search, automation, quality controls, and multi-writer governance when the wiki grows enough to need them.

The default is intentionally small. Pages remain human-readable and authoritative; graph and search indexes are optional, rebuildable aids.

## Package contents

```text
llm-wiki/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- bootstrap-and-schema.md
|   |-- operations.md
|   `-- scaling-and-governance.md
`-- scripts/
    `-- init_wiki.py
```

## Install on another machine

Codex discovers personal skills from `$CODEX_HOME/skills`. When `CODEX_HOME` is not set, the default is `~/.codex/skills`.

The repository copy under `skills/llm-wiki/` is the canonical source. The recommended installation links Codex directly to that directory so every change remains visible to Git and `git pull` updates the installed skill immediately.

### Recommended: clone and link the skill

On macOS or Linux:

```bash
git clone https://github.com/dutycaws/awesome-codex-subagents.git
cd awesome-codex-subagents
skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_dir"
ln -s "$PWD/skills/llm-wiki" "$skills_dir/llm-wiki"
```

On Windows PowerShell, use a directory junction:

```powershell
git clone https://github.com/dutycaws/awesome-codex-subagents.git
Set-Location awesome-codex-subagents
$CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$SkillsDir = Join-Path $CodexRoot "skills"
$RepoSkill = (Resolve-Path "skills/llm-wiki").Path
New-Item -ItemType Directory -Force $SkillsDir | Out-Null
New-Item -ItemType Junction -Path (Join-Path $SkillsDir "llm-wiki") -Target $RepoSkill
```

The link destination must not already exist. If another `llm-wiki` installation is present, review and preserve any unique changes before replacing it. If the skill is on a branch or tag that has not reached the default branch, clone or check out that ref before creating the link.

Start a new Codex turn after linking the skill.

### Alternative: install a snapshot from GitHub

If you do not want to keep a local repository checkout, ask Codex on the other machine:

```text
Use $skill-installer to install skills/llm-wiki from dutycaws/awesome-codex-subagents.
```

The equivalent installer command is:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo dutycaws/awesome-codex-subagents \
  --path skills/llm-wiki
```

The installer uses the repository's `main` branch by default. To install from a different branch or tag, add `--ref <branch-or-tag>`. It stops if `llm-wiki` is already installed rather than overwriting it. This method creates a snapshot rather than a source-controlled link.

### Verify the installation

On macOS or Linux:

```bash
test -L "${CODEX_HOME:-$HOME/.codex}/skills/llm-wiki" && \
  test -f "${CODEX_HOME:-$HOME/.codex}/skills/llm-wiki/SKILL.md" && \
  echo "llm-wiki linked and installed"
```

For a snapshot installation, only the `test -f` check is expected to succeed.

Or ask Codex to use it explicitly:

```text
$llm-wiki Initialize a research wiki for distributed systems in this project.
```

## Update it later

For the recommended linked installation, update only the repository checkout:

```bash
cd awesome-codex-subagents
git pull --ff-only
```

The installed skill now reflects the pulled files automatically. Keep edits in the repository so `git status`, commits, branches, and reviews capture every change.

For snapshot installations, the GitHub installer intentionally refuses to overwrite an existing destination. Preserve any local changes, replace the old snapshot deliberately, and run the installer again.

## Use the skill

Invoke it explicitly with `$llm-wiki`, or describe a persistent-wiki task and let Codex select it automatically.

Examples:

```text
$llm-wiki Initialize a wiki for my machine-learning paper collection.

$llm-wiki Ingest the new sources in raw/ and integrate them with the existing topics.

$llm-wiki Answer how the authentication architecture changed, with source citations.

$llm-wiki Crystallize this debugging session into reusable project knowledge.

$llm-wiki Lint the wiki and report problems without modifying files.
```

## Initialize the default layout directly

The bundled initializer creates missing files without overwriting existing ones:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/llm-wiki/scripts/init_wiki.py" /path/to/project
```

Default output:

```text
project/
|-- raw/
|-- wiki/
|   |-- index.md
|   `-- log.md
`-- .llm-wiki/
    `-- schema.md
```

Preview changes or customize paths:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/llm-wiki/scripts/init_wiki.py" \
  /path/to/project \
  --sources-dir sources \
  --wiki-dir knowledge \
  --schema-file .knowledge/schema.md \
  --dry-run
```

Python 3 is needed only for this initializer. The skill itself has no third-party runtime dependencies.
