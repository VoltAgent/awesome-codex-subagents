# Codex Skills

The directories under `skills/` are the canonical, change-controlled definitions of this repository's Codex skills.

For development and use on a machine with a repository checkout, link each skill into the personal Codex skills directory instead of maintaining a copied installation:

```text
repository/skills/<skill-name>  <-- canonical Git source
             |
             `-- symlink or junction --> $CODEX_HOME/skills/<skill-name>
```

When `CODEX_HOME` is unset, Codex uses `~/.codex`.

## macOS and Linux

From the repository root:

```bash
skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_dir"
ln -s "$PWD/skills/llm-wiki" "$skills_dir/llm-wiki"
```

The destination must not already exist. If it contains an older copied installation, preserve or review that directory before replacing it with the link.

## Windows PowerShell

From the repository root, create a directory junction:

```powershell
$CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$SkillsDir = Join-Path $CodexRoot "skills"
$RepoSkill = (Resolve-Path "skills/llm-wiki").Path
New-Item -ItemType Directory -Force $SkillsDir | Out-Null
New-Item -ItemType Junction -Path (Join-Path $SkillsDir "llm-wiki") -Target $RepoSkill
```

## Updating

Pull the repository normally:

```bash
git pull --ff-only
```

The installed skill updates immediately because Codex resolves the link to the repository directory. Start a new Codex turn if the changed skill metadata or instructions are already loaded in the current turn.

## Available skills

- [`llm-wiki`](llm-wiki/) — persistent, compounding Markdown knowledge bases. See its [README](llm-wiki/README.md) for complete installation and usage instructions.
- [`multi-agent-debate`](multi-agent-debate/) — independent expert analysis, adversarial debate, and structured synthesis.
