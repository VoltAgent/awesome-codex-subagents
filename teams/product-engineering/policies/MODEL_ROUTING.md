# Model Policy

This team intentionally uses exactly two model profiles. Do not route work to Terra or any other model/effort combination.

## Decision profile — Sol low

Use `gpt-5.6-sol` with `model_reasoning_effort = "low"` for decisions whose mistakes can propagate across the product:

- primary engineering lead (main Codex thread)
- `product-manager`
- `solution-architect`
- `execution-planner`
- `reviewer`
- `security-reviewer`

These roles decide scope, architecture, ownership, acceptance, security, and whether work must be replanned. They should return concise decisions and contracts rather than doing broad implementation.

## Worker profile — Luna max

Use `gpt-5.6-luna` with `model_reasoning_effort = "max"` for execution and evidence gathering:

- `code-mapper`
- `docs-researcher`
- `ui-designer`
- `frontend-developer`
- `backend-developer`
- `database-engineer`
- `fullstack-developer`
- `test-automator`
- `browser-qa`
- `debugger`
- `deployment-engineer`

Luna max owns bounded work: inspect, implement, test, debug, verify, and report evidence.

## Escalation rule

Do not change model tiers dynamically. Escalation changes **role**, not model:

1. Luna max owner attempts the bounded task.
2. On repeated failure, Luna max `debugger` establishes root cause.
3. If the failure indicates a bad requirement, architecture, ownership split, or system-wide contradiction, Sol low `solution-architect` / `execution-planner` / main lead decides the new approach.
4. Luna max workers execute the revised plan.

This preserves a simple hierarchy: **Sol decides; Luna executes.**
