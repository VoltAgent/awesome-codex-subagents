# Repository Targets and Runtime Boundaries

Read this before implementing a new structure or reorganizing an existing one.

## Preferred Codex target

For a workflow that belongs to one repository and should be discoverable by Codex, use:

```text
<repo>/.agents/skills/<workflow-name>/
  SKILL.md
  CONTEXT.md
  _shared/
  _templates/
  stages/
```

`SKILL.md` defines applicability and routes to the workflow. `CONTEXT.md` shows the flow in one screen. The stage folders hold contracts and targeted references. This keeps the method and its domain policy versioned with the codebase that owns them.

Use a standalone `<repo>/workflows/<name>/` only when the workflow must be browsed or run independently of skill discovery. In that case, add a short routing row to the applicable `AGENTS.md`; do not replace its existing instructions.

## Compact single-stage target

If the source describes one job with no meaningful handoff, keep the structure small:

```text
.agents/skills/<name>/
  SKILL.md
  references/
    contract.md
```

The contract still states Inputs, Process, Outputs, and Human Check. A `stages/` tree would add ceremony without state or routing value.

## Factory and product ownership

Decide explicitly:

- which rules, templates, schemas, and source pointers are committed;
- where per-run artifacts are written;
- whether artifacts are committed, ignored, archived externally, or removed after a receipt is recorded;
- which external system is authoritative after publication;
- how a later run finds the correct current record without loading prior outputs as examples.

Never commit secret values. Reference an environment variable, credential provider, or repository-approved secret interface. Do not encode an instruction to read a generic "secrets folder" without naming the authorized interface and handling failures safely.

## Read-only and mutation stages

Separate evidence gathering from external mutation.

- Research, repository inspection, API queries, and CLI reads stay in read-only stages.
- Creating or updating a ticket, sending a message, changing CRM state, or writing to production is a distinct final stage.
- The mutation stage reads an approved draft, checks target identity, presents the exact intended change when practical, and records a receipt or identifier.
- A source prompt that says "finally create the ticket" does not authorize creation during conversion. Runtime authorization still comes from the invoking user and tool policy.

## Restructure safety

For an existing tree:

1. Inventory without moving or deleting.
2. Classify files as catalog, contract, factory, product, or stale candidate.
3. Search for in-repo references, relative links, symlinks, and known external consumers.
4. Present the target tree and migration map before destructive or broad moves.
5. Check destinations case-insensitively to prevent collisions.
6. Copy, verify file counts and hashes, update referrers, then remove originals only when authorized.
7. Archive suspected stale content rather than deleting it unless deletion is explicit.

A cold walk proves the result is navigable; it does not prove a move was safe. Reference integrity is a separate gate.

## Source-control handoff

Before finishing:

- review the owning repository's status and diff;
- avoid mixing unrelated user changes into the commit;
- validate from the repository path, not a temporary copy alone;
- commit only when requested;
- report the exact owning path, invocation name, and commit hash.
