# Autonomous Product Engineering Team

This fork includes an opinionated Codex product-engineering team that can take an application or feature from requirements through implementation, validation, review, and release readiness.

The original `categories/` catalog remains intact. The autonomous team is a curated layer under `teams/product-engineering/`.

## Install into an application repository

From this repository:

```bash
./scripts/install-product-team.sh /path/to/your/application
```

Then open the target application in a new Codex session and describe the product or feature you want built.

The installer deliberately refuses to overwrite an existing `AGENTS.md` or `.codex/config.toml`. Merge existing project rules manually, or use `--force` only when replacement is intentional.

## Model policy

This profile is intentionally constrained to two model configurations:

- `gpt-5.6-sol` + `low` for the primary engineering lead and product/architecture/planning/review/security decisions.
- `gpt-5.6-luna` + `max` for implementation, exploration, UI execution, testing, browser QA, debugging, database work, and deployment preparation.

This keeps orchestration predictable: **Sol decides; Luna executes.**

## Core principles

- The main Codex thread is engineering lead and integration owner.
- Subagents are bounded specialists.
- Read-heavy work can run in parallel; write-heavy work requires disjoint ownership.
- Acceptance criteria are traceable to implementation and validation evidence.
- Testers/reviewers are independent from fixers.
- Repeated failures escalate instead of looping blindly.
- Routine engineering decisions are autonomous; production/destructive/paid/external-impact actions remain human-gated.
