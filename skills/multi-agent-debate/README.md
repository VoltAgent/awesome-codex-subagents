# Council of Subagents Debate Skill

`multi-agent-debate` is a reusable Codex skill for evaluating consequential decisions through a bounded council of independent subagents.

The council does not vote its way to artificial consensus. It frames the decision, assigns experts with materially different mandates, gathers independent positions, cross-examines assumptions, stress-tests the provisional synthesis, preserves credible dissent, and returns a decision record with risks and a validation plan.

## What it supports

- Frames the question, constraints, assumptions, evidence gaps, and decision criteria.
- Selects a diverse panel of three to five experts by default.
- Keeps initial analyses independent so early opinions do not anchor the panel.
- Runs a cross-examination round that requires fair restatement and evidence-based revision.
- Uses an optional adversarial round when consequential uncertainty remains.
- Synthesizes by evidence quality and decision consequences rather than vote count.
- Preserves minority positions, reversal triggers, and the smallest useful validation step.

Use it for architectural, operational, security, product, research, planning, or debugging decisions with real uncertainty and competing trade-offs. Avoid it for routine work, simple factual questions, or reversible low-risk choices where coordination would cost more than it contributes.

## Package contents

```text
multi-agent-debate/
|-- SKILL.md
|-- README.md
`-- agents/
    `-- openai.yaml
```

The repository directory is the canonical, change-controlled definition. The local Codex installation should link to this directory rather than contain a copied skill.

## Install on another machine

Codex discovers personal skills from `$CODEX_HOME/skills`. When `CODEX_HOME` is unset, the default is `~/.codex/skills`.

### Recommended: clone and link the skill

On macOS or Linux:

```bash
git clone https://github.com/dutycaws/awesome-codex-subagents.git
cd awesome-codex-subagents
skills_dir="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skills_dir"
ln -s "$PWD/skills/multi-agent-debate" "$skills_dir/multi-agent-debate"
```

On Windows PowerShell, use a directory junction:

```powershell
git clone https://github.com/dutycaws/awesome-codex-subagents.git
Set-Location awesome-codex-subagents
$CodexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$SkillsDir = Join-Path $CodexRoot "skills"
$RepoSkill = (Resolve-Path "skills/multi-agent-debate").Path
New-Item -ItemType Directory -Force $SkillsDir | Out-Null
New-Item -ItemType Junction -Path (Join-Path $SkillsDir "multi-agent-debate") -Target $RepoSkill
```

The link destination must not already exist. If another installation is present, review and preserve any unique changes before replacing it. If the skill exists only on a branch or tag, clone or check out that ref before creating the link.

Start a new Codex turn after linking the skill.

### Alternative: install a snapshot from GitHub

If you do not want a repository checkout on the other machine, ask Codex:

```text
Use $skill-installer to install skills/multi-agent-debate from dutycaws/awesome-codex-subagents.
```

The equivalent installer command is:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo dutycaws/awesome-codex-subagents \
  --path skills/multi-agent-debate
```

The installer uses `main` by default. Add `--ref <branch-or-tag>` for another ref. It refuses to overwrite an existing destination. This method creates a snapshot rather than a source-controlled link.

## Verify the linked installation

On macOS or Linux:

```bash
test -L "${CODEX_HOME:-$HOME/.codex}/skills/multi-agent-debate" && \
  test -f "${CODEX_HOME:-$HOME/.codex}/skills/multi-agent-debate/SKILL.md" && \
  echo "multi-agent-debate linked and installed"
```

For a snapshot installation, only the `test -f` check is expected to succeed.

## Update it later

For a linked installation, pull the repository checkout:

```bash
cd awesome-codex-subagents
git pull --ff-only
```

The installed skill reflects the pulled files immediately. Keep changes in the repository so `git status`, commits, branches, and reviews capture the complete definition.

## Use the council

Invoke it explicitly with `$multi-agent-debate`, or describe a consequential decision whose assumptions should be challenged.

Examples:

```text
$multi-agent-debate Decide whether we should split this service now or keep the modular monolith for another year.

$multi-agent-debate Evaluate the security, reliability, delivery, and product trade-offs of this authentication migration.

$multi-agent-debate Stress-test this incident remediation plan and preserve any credible dissent.

$multi-agent-debate Compare the two proposed data models and recommend the smallest validation experiment.
```

The workflow requires a Codex environment that can spawn subagents. It adapts the panel and number of rounds to available concurrency and stops when additional debate is unlikely to change the decision.
