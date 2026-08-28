# Failure Recovery Policy

Do not repeatedly apply speculative patches to one failure family.

1. First failure -> original owner fixes from evidence.
2. Repeated failure -> read-only `debugger` establishes root cause; proper writer fixes.
3. Third failure or structural contradiction -> `solution-architect` revises contract/plan before broad new edits.

Prefer the first/primary failing signal. After a fix, run the narrow discriminating check first, then broader gates.
