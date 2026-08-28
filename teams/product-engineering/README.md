# Product Engineering Team

A curated Codex multi-agent team for building applications end to end.

This layer keeps the upstream `categories/` catalog intact and adds the missing operating system: a lead constitution, a current multi-agent config, a small core team, shared contracts, quality/autonomy policies, an installer, and validation.

## Lifecycle

```text
INTAKE -> DISCOVERY -> PRODUCT SPEC -> ARCHITECTURE/UI -> PLAN
       -> IMPLEMENTATION -> INTEGRATION -> VALIDATION -> REVIEW
       -> FIX/REPLAN LOOP -> RELEASE READY
```

Small tasks deliberately use a shorter path.

## Core team

- `product-manager`
- `solution-architect`
- `code-mapper`
- `docs-researcher`
- `ui-designer`
- `execution-planner`
- `frontend-developer`
- `backend-developer`
- `database-engineer`
- `fullstack-developer`
- `test-automator`
- `browser-qa`
- `reviewer`
- `security-reviewer`
- `debugger`
- `deployment-engineer`

The main Codex thread owns shared decisions, integration, final validation, and completion. Workers only own bounded slices.

## Model routing

The team deliberately uses only two profiles:

- **Sol low** for the main lead and decision agents (`product-manager`, `solution-architect`, `execution-planner`, `reviewer`, `security-reviewer`).
- **Luna max** for all execution/evidence agents.

No Terra and no other reasoning levels are used. Escalation changes the responsible role rather than switching to a third model.

## Install

```bash
./scripts/install-product-team.sh /path/to/application
```

Validate this framework with:

```bash
python3 scripts/validate-product-team.py
```
