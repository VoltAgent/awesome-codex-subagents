# Integration and Verification

Use this reference when an epic has work that may change the repository. The
Sol root owns integration authority and is the only actor that may accept a
work unit, advance epic state, or close a ticket. It may assign one bounded
Terra operator to perform integration mechanics through the approved queue.

## Non-negotiable invariants

1. Every mutable scope has exactly one current owner.
2. Every write packet names a base revision and a validation contract.
3. A worker result is evidence, not an integration decision.
4. Shared boundaries are serialized even when feature files appear disjoint.
5. The root, or its single bounded integration operator, integrates one
   accepted result at a time into the authoritative epic revision; the root
   alone records acceptance.
6. A packet whose assumptions or base revision are invalidated must not keep
   writing or be accepted without reissue.

The root records ownership, base revision, effective permissions, validation
evidence, integration status, and stop reason in the epic manifest. Workers
may propose updates but must not edit the authoritative manifest.

## Choose a workspace mode

| Mode | Allowed concurrent writers | Use when | Root rule |
| --- | ---: | --- | --- |
| Shared checkout | 1 | Work is coupled, tooling shares mutable state, or isolation is unavailable | Serialize all writes. Other active workers are read-only. |
| Isolated worktrees | 1 per approved worktree | Units have disjoint mutable ownership and isolated test resources | Queue completed commits for root-owned integration. |

Do not infer worktree safety from ticket titles or directory names. The root
must confirm all of the following before allowing parallel writers:

- each unit has a disjoint mutable scope, including generated output;
- neither unit changes a shared API, schema, configuration, package lock,
  migration chain, build graph, code-generation input, or test fixture;
- each writer has an isolated worktree and any required service, database,
  port, cache, or test-resource isolation;
- both packets name compatible base revisions and validation commands; and
- the integration queue has capacity for sequential reconciliation.

If any condition is uncertain, use a shared checkout with one writer or run a
read-only discovery packet first.

## Establish mutable ownership

Before dispatch, the root assigns one owner to each mutable scope. Scope is
more than a path list: it includes the contracts and generated artifacts that
the work can alter.

Every write packet must list:

- `work_unit_id` and `plan_version`;
- the approved worktree or shared checkout identity;
- `base_revision`, the last accepted integrated revision the worker starts
  from;
- allowed mutable paths and explicitly shared/prohibited boundaries;
- required inputs, dependency evidence, and acceptance criteria;
- validation commands and their expected evidence; and
- the escalation condition for a discovered dependency, scope conflict, or
  contract change.

Do not assign two owners to one scope. If a worker needs an unowned adjacent
file, it reports a dependency request; the root either expands and reissues
the packet or creates a new ordered unit. It does not grant informal access in
chat.

## Verify effective permissions before dispatch

Custom-agent defaults are not sufficient proof of runtime permissions. Before
each dispatch, the root confirms and records:

| Check | Required outcome |
| --- | --- |
| Effective sandbox/approval mode | Matches the packet's read-only or write authority. |
| Workspace identity | The worker is in the named shared checkout or approved worktree. |
| Write authority | A write packet has one active owner; a read-only packet has no write scope. |
| Child authority | The worker is told it cannot spawn, delegate, integrate, or change epic state. |

If the runtime permission mode is broader than the packet requires, treat that
as a dispatch risk and restate the packet's restriction. If it cannot be
verified, do not dispatch a concurrent writer.

## Serialize contracts and shared boundaries

The following are shared boundaries by default and require one ordered owner,
even with isolated worktrees:

- public APIs, interfaces, schemas, database migrations, and event contracts;
- application configuration, dependency manifests and locks, build tooling,
  code-generation inputs, and generated artifacts;
- shared fixtures, golden files, test harnesses, snapshots, and environment
  setup; and
- release/version metadata, deployment configuration, and repository-wide
  documentation that describes changed behavior.

The root may split a boundary only after explicitly defining a compatibility
contract and integration order. A worker that discovers a shared-boundary
change returns `plan_drift`; it must not change that boundary opportunistically.

## Integration queue

Workers submit a handoff containing the work-unit ID, plan version, base
revision, commit or diff identity, changed scope, validation evidence, known
limitations, and any discovered dependencies. The root queues only handoffs
whose local validation is complete.

For each queued result, the root:

1. checks that the packet remains current and its scope/permissions were
   honored;
2. compares the base revision with the latest accepted epic revision;
3. rebases or otherwise reconciles the result against that revision;
4. runs the packet's required validation again when reconciliation can affect
   behavior;
5. integrates the result alone, records the new accepted revision, and updates
   dependency evidence; then
6. invalidates or reissues packets affected by the integration.

Never batch-integrate independent-looking results without checking their
shared boundaries and validation evidence. The queue preserves a deterministic
integration order; urgency does not override dependency correctness.

## Gates

### Per-packet gate

A packet is eligible for integration only when it has all of the following:

- accepted dependencies and a current plan version;
- no mutable-scope violation or unapproved boundary change;
- evidence that the specified validation commands passed, or an approved
  documented exception;
- a handoff with the base revision and reproducible change identity; and
- no unresolved `blocked` or `plan_drift` report.

### Contract gate

Before accepting any changed shared contract, the root confirms compatible
consumers, migrations, generated output, tests, documentation, and rollback
or compatibility handling. Contract changes are integrated before dependent
implementation packets are reissued.

### Epic gate

An epic can close only after all required units are integrated, dependency
evidence is accepted, cross-unit and ticket acceptance checks pass against the
latest integrated revision, and no unresolved blocker or stale packet remains.

## Classify failures before acting

| Classification | Examples | Root action |
| --- | --- | --- |
| Transient | Tool/service timeout, temporary network failure, flaky runner with no product failure signal | Retry once with the same packet and record the attempt. |
| Deterministic validation failure | Reproducible failing test, compiler error, unmet acceptance criterion | Do not retry blindly; return to the owner for a bounded fix or create a diagnostic unit. |
| Scope/ownership conflict | Changed prohibited path, two units need one boundary | Block and re-plan ownership/order. |
| Plan drift | New dependency, changed contract, invalid assumption, incompatible integration | Invalidate affected packets and publish a new plan version. |
| Environment/isolation failure | Shared port/database/cache, worktree contamination, non-reproducible setup | Stop parallel writes; serialize or repair isolation before re-dispatch. |

A repeated transient failure becomes an environment or diagnostic problem. A
deterministic failure is not made transient by trying a different agent.

## Invalidate stale packets

When an accepted integration changes a packet's base revision, dependency,
contract, schema, generated artifact, configuration, fixture, or acceptance
assumption, the root marks that packet stale. A stale worker must stop at a
safe boundary and return its current evidence; it must not continue writing
against the old contract.

The root then chooses one of: reissue the packet with the new plan version,
convert the remaining task to a diagnostic unit, serialize it behind another
unit, or cancel it as superseded. Do not accept work from a stale packet unless
the root explicitly verifies that the changed assumptions are irrelevant.

## Completion vocabulary

Use these terms precisely:

- **Implemented:** the assigned worker has made its bounded change and supplied
  local evidence. It says nothing about mergeability, dependencies, or epic
  success.
- **Integrated:** the root has reconciled the change into the authoritative
  epic revision, rerun required checks, and recorded accepted evidence. It may
  still leave the ticket or epic open.
- **Closed:** the root has confirmed the ticket's full acceptance criteria in
  the integrated state, including required cross-unit behavior and
  documentation/operational obligations.
- **Epic complete:** every required ticket is closed and the epic-level gate
  passes on the latest integrated revision.

Never use a worker's `implemented` status as a synonym for `integrated`,
`closed`, or `epic complete`.
