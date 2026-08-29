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
skill_name="icm-workflow-architect" # or llm-wiki / multi-agent-debate
skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_dir"
ln -s "$PWD/skills/$skill_name" "$skills_dir/$skill_name"
```

The destination must not already exist. If it contains an older copied installation, preserve or review that directory before replacing it with the link.

## Windows PowerShell

From the repository root, create a directory junction:

```powershell
$SkillName = "icm-workflow-architect" # or llm-wiki / multi-agent-debate
$CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$SkillsDir = Join-Path $CodexRoot "skills"
$RepoSkill = (Resolve-Path (Join-Path "skills" $SkillName)).Path
New-Item -ItemType Directory -Force $SkillsDir | Out-Null
New-Item -ItemType Junction -Path (Join-Path $SkillsDir $SkillName) -Target $RepoSkill
```

## Updating

Pull the repository normally:

```bash
git pull --ff-only
```

The installed skill updates immediately because Codex resolves the link to the repository directory. Start a new Codex turn if the changed skill metadata or instructions are already loaded in the current turn.

## Available skills

- [`icm-workflow-architect`](icm-workflow-architect/) — converts prompts, SOPs, and recurring workflows into repository-controlled ICM structures for Codex.
- [`llm-wiki`](llm-wiki/) — persistent, compounding Markdown knowledge bases. See its [README](llm-wiki/README.md) for complete installation and usage instructions.
- [`multi-agent-debate`](multi-agent-debate/) — a council of independent experts for adversarial debate and structured synthesis. See its [README](multi-agent-debate/README.md) for installation and usage instructions.
