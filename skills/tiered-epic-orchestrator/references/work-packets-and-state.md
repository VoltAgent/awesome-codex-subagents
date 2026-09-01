# Work packets and epic state

This reference defines the planning and handoff contract for a ticketed epic.
The Sol root is the sole authority for the manifest, DAG, state transitions,
replanning, integration, and closure. Workers are read-only unless a packet
explicitly grants a bounded write scope. A shared checkout permits only one
writer; concurrent writers require approved isolated worktrees. Workers cannot
recursively spawn workers or revise the plan.

## Ticket boundaries versus execution boundaries

A ticket is a product or delivery boundary: it names an outcome, requester,
and acceptance intent. It is not automatically a safe unit of concurrent work.
An execution boundary is the smallest independently verifiable change with a
declared mutable scope and stable inputs/outputs.

Split a ticket when it crosses interfaces, schemas, migrations, services,
packages, ownership, or distinct verification gates. Combine ticket fragments
only when one worker can own the scope and the combined acceptance criteria are
unambiguous. A packet may map to many tickets, and one ticket may map to many
packets; the manifest must record both mappings.

## Typed dependency DAG

Each packet is a node. Each edge has a type and evidence level:

| Edge type | Meaning |
| --- | --- |
| `data` | Node consumes an artifact or data shape produced by another. |
| `interface` | API, event, function, schema, or contract must agree. |
| `ordering` | A prerequisite must land or be verified first. |
| `test` | A test, fixture, or harness depends on the behavior. |
| `write-conflict` | Mutable scope or generated output cannot be changed concurrently. |
| `operational` | Deployment, migration, configuration, or rollout sequencing applies. |

Edges are `verified` (directly supported by repository evidence), `inferred`
(reasonable but not confirmed), or `precautionary` (temporary safety ordering).
Only verified or safety-critical edges should hard-block execution. Inferred
edges require confirmation or an explicit risk acceptance before release.

The root validates that the graph is acyclic, every node has an owner and
acceptance gate, every consumer has a producer or declared external input, and
shared artifacts have serialized ownership. The graph revision and edge
rationale are part of the manifest.

```yaml
node: P-014
tickets: [EPIC-42, API-17]
objective: "Add versioned export endpoint"
preconditions: ["P-009 schema shape verified"]
postconditions: ["OpenAPI and contract tests pass"]
mutable_scope: ["services/export/**", "docs/openapi.yaml"]
forbidden_scope: ["db/migrations/**"]
dependencies:
  - {from: P-009, type: interface, evidence: verified, rationale: "reads export schema"}
owner: terra-worker
verification: ["npm test -- export", "npm run lint"]
```

## Minimal work-packet schema

Every packet must be self-contained enough to survive a context handoff:

1. `id`, mapped ticket IDs, objective, and non-goals.
2. Baseline commit/revision and relevant evidence paths or symbols.
3. Preconditions, dependencies, assumptions, and unresolved questions.
4. Exact mutable scope, forbidden scope, generated artifacts, and test-resource constraints.
5. Input/output and interface contract, including compatibility requirements.
6. Observable acceptance criteria and commands that verify each criterion.
7. Expected receipt, escalation triggers, and rollback or recovery note.

Workers must not expand scope because a neighboring ticket appears related.
They return the discovery to the root, which either creates a graph revision or
records why the scope remains unchanged.

## Worker receipt and statuses

A worker reports `complete`, `blocked`, `failed`, or `plan_drift`; this is a
claim, not an authoritative state transition. The root records packet lifecycle
states:

`planned` -> `ready` -> `in_progress` -> `submitted` -> `accepted`.

Invalidation or terminal alternatives are `stale`, `blocked`, `rejected`,
`superseded`, and `cancelled`. The root uses `submitted` after receiving a
`complete` receipt and `accepted` only after verifying its evidence and
acceptance criteria. It maps a `blocked` report to `blocked`, a `failed` report
to `in_progress` only when the root explicitly authorizes a bounded correction
inside the same packet; otherwise it maps the failed attempt to `rejected` and
reissues or replaces the packet deliberately. It maps `plan_drift` to `stale`
plus an epic-level `replanning` transition. A failed check must not be hidden
by any label.

```yaml
packet: P-014
reported_status: complete
worker: terra-worker
model: gpt-5.6-terra
base_revision: abc123
changed_files: [services/export/handler.ts, docs/openapi.yaml]
checks:
  - {command: "npm test -- export", result: pass}
  - {command: "npm run lint", result: pass}
contract_changes: "None"
unresolved: []
scope_deviation: false
next_action: "Root integration review"
```

## Authoritative manifest and state machine

The manifest is the canonical state record; ticket systems and chat summaries
are references, not authority. It includes:

- `epic.id`, title, owner, repository, `run.baseline_revision`, and creation time;
- source ticket IDs and normalized success criteria;
- plan version, DAG location, packet index, and model/capability policy;
- assumptions, evidence ledger, risk register, and unresolved questions;
- concurrency/write policy, worker assignments, receipts, and retry count;
- replan history, stale packets, integration checks, final acceptance evidence;
- current state and stop reason.

```yaml
state: executing
run:
  plan_version: 3
  baseline_revision: abc123
  integration_revision: def456
packets:
  - {id: P-014, state: in_progress, plan_version: 3, base_revision: def456}
```

Permitted epic states are:

`intake` -> `evidence_gathering` -> `planned` -> `challenged` -> `ready` ->
`executing` -> `integrating` -> `verified` -> `closed`.

Any state may move to `blocked` or `replanning`; only the root performs those
transitions. `closed` requires integrated acceptance evidence, not merely all
tickets having `accepted` receipts. A failed integration returns to
`replanning` or `executing` with affected packets marked stale.

## Revision, staleness, and replanning

The epic records `run.baseline_revision` and a monotonically increasing
`run.plan_version`. Each packet records the `plan_version` from which it was
compiled and its own `base_revision`, normally the latest accepted integration
revision at dispatch. Packets derived from an older plan or baseline are stale
when their contract, dependency, mutable scope, or required test changed. Stale
packets cannot be accepted without root revalidation.

Replan on an undeclared dependency; incompatible interface/schema/migration;
overlapping scope; falsified assumption; contradictory or non-observable
acceptance criterion; material baseline change; failed integration check; a
worker capability/model/sandbox mismatch; or a retry that does not resolve a
transient failure. Record changed nodes/edges, affected packets, and validity
of prior receipts.

## Documentation depth

Compact mode is suitable for routine, low-coupling epics: one manifest, a
short evidence index, typed packet list, explicit tests, and one integration
checkpoint. Forensic mode is required for cross-boundary, ambiguous,
irreversible, or security/data/reliability-sensitive epics: retain source
citations, assumption IDs, edge rationales, interface snapshots, risk and
rollback notes, challenge receipts, wave decisions, and stale-receipt history.

Depth may be reduced only by the root, with the reason recorded. No documentation
mode permits recursive spawning, parallel shared-checkout writers, or closure
without integrated verification.
