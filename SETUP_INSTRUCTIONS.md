# Setup Instructions

This overlay adds the autonomous product-engineering team to the `awesome-codex-subagents` fork while preserving the upstream `categories/` catalog.

## 1. Apply this overlay to the fork

```bash
git clone https://github.com/divyamanand/awesome-codex-subagents.git
cd awesome-codex-subagents
git checkout -b feat/autonomous-product-team

# Extract the ZIP contents into the repository root.
unzip /path/to/autonomous-product-team-sol-luna.zip -d .

chmod +x scripts/install-product-team.sh scripts/validate-product-team.py
python3 scripts/validate-product-team.py

git add .
git commit -m "feat: add autonomous product engineering team"
git push -u origin feat/autonomous-product-team
```

Expected validation output:

```text
Product team validation passed: 16 agents
```

## 2. Install the team into an application repository

From the modified `awesome-codex-subagents` clone:

```bash
./scripts/install-product-team.sh /absolute/path/to/your-application
```

The target application receives:

```text
AGENTS.md
.codex/
├── config.toml
├── agents/
│   └── 16 curated agent TOML files
└── team/
    ├── contracts/
    └── policies/
```

The installer refuses to overwrite an existing root `AGENTS.md`, `.codex/config.toml`, or same-named agent file. Merge existing project instructions manually when those files already exist. Use `--force` only when replacement is intentional.

## 3. Start Codex

Open the target application in a **new Codex session** and trust the project so project-scoped `.codex/config.toml` is loaded.

The installed configuration intentionally uses only two model profiles:

- **Primary lead + decision agents:** `gpt-5.6-sol`, reasoning `low`
- **Execution/evidence agents:** `gpt-5.6-luna`, reasoning `max`

Decision agents are:

- `product-manager`
- `solution-architect`
- `execution-planner`
- `reviewer`
- `security-reviewer`

All other curated subagents use Luna max.

Then give the main Codex thread the product request directly, for example:

```text
Build an expense-management web application. Users can sign in, create expenses,
upload receipts, categorize transactions, and view monthly analytics. Own the work
end-to-end and use the product-engineering subagents according to AGENTS.md.
```

The main thread remains integration owner. It should delegate bounded work, validate the integrated application, route failures through the retry/debug/replan loop, and stop at the configured human gates for destructive or production-impacting actions.

## 4. Verify the installed configuration

In the application repository:

```bash
cat .codex/config.toml
grep -R '^model\|^model_reasoning_effort' .codex/agents | sort
```

You should see only `gpt-5.6-sol` + `low` and `gpt-5.6-luna` + `max`.
