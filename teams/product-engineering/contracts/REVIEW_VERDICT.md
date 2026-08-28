# Review Verdict Contract

Return exactly one:

- `ACCEPT`
- `ACCEPT_WITH_CHANGES`
- `REPLAN_REQUIRED`

Each material finding includes severity (blocker/high/medium/low), confidence, concrete evidence, affected AC/invariant, impact, recommended owner, and required revalidation.

Do not ACCEPT with unresolved blocker/high findings. Use REPLAN_REQUIRED when an accepted architecture/contract is invalidated rather than locally fixable.
