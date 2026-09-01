# Model Routing

Route work by uncertainty, coupling, and consequence. Model choice is a risk
control, not a status signal: use the least capable model that can complete
the packet with reliable evidence.

## Authority and ownership

- The `gpt-5.6-sol` root is the sole orchestration authority. It frames the
  epic, owns the DAG and run state, resolves conflicts, and performs final
  integration and closure.
- Workers do not recursively spawn agents or change the DAG. They receive one
  typed work packet with owned paths, dependencies, acceptance checks, and a
  stop/escalation rule.
- Parallel investigation is allowed. In a shared checkout, at most one writer
  is active at a time; contracts, schemas, configuration, and generated files
  are serialized. Isolated worktree writers are an explicit exception only
  when mutable ownership and test resources are disjoint.

Before routing, inspect the models and reasoning levels available on the active
host when that information is exposed. Record the effective model rather than
only the requested model. If a named model is unavailable, substitute upward
in capability and record the cost/latency tradeoff; never silently route a
required review or consequential decision downward. If no independent capable
reviewer is available for a mandatory gate, pause and disclose the limitation.

## Model classes

### `gpt-5.6-luna`

Use for low-uncertainty, checkable work: path and dependency reconnaissance,
evidence extraction, narrowly scoped static analysis, mechanical localized
changes, and tests with explicit expected behavior. Luna must cite paths or
commands that support its result and must flag uncertainty rather than infer
across packet boundaries.

### `gpt-5.6-terra`

Use for coupled or ambiguous implementation, cross-file debugging, interface
or migration reasoning, test design, and substantive review. A Terra reviewer
is mandatory for predefined high-impact boundaries such as security, data
integrity, public contracts, irreversible migrations, or generated artifacts.

### `gpt-5.6-terra` high-reasoning challenger

The root may run one sequential read-only Terra-high planning challenger when
the epic crosses subsystem boundaries, has unresolved dependency uncertainty,
or presents consequential ambiguity. The challenger returns claim-level
evidence, risks, and plan deltas; it does not become a second authority.

### `gpt-5.6-sol` second planner

Use a second Sol planner only for an irreversible or materially disputed
re-plan: for example, an unresolved conflict involving a public contract,
schema, migration, security property, or critical-path dependency. Do not use
it for stylistic disagreement or routine decomposition.

## Capacity and failure policy

- Start with three task workers when parallel work has clear value. Four is the
  hard child ceiling; a fourth slot is reserved for a planner, reviewer, or
  diagnostic when needed.
- Never recursively fan out. Queue additional packets behind the cap.
- Retry once only for transient infrastructure failures (timeout, unavailable
  service, or lost connection), with bounded backoff.
- A deterministic failure (test assertion, type error, unmet acceptance
  criterion, or contradictory evidence) is not blindly retried. Return an
  ordinary packet-local defect to the same owner for a bounded fix; escalate
  Luna to Terra on capability mismatch, or return Terra work to the Sol root
  when the packet or plan is wrong. Permit one model escalation per packet
  before root triage.
- Stop an escalation chain after the permitted retry/escalation budget. Mark
  the packet blocked or re-plan it; do not loop.

## Context and budget controls

Keep a versioned manifest of the effective model, reasoning effort, sandbox,
worker slot, token/call budget, retries, escalations, owned paths, and
verification evidence. Pass a compact immutable epic brief plus the packet;
refer to repository paths instead of embedding large snapshots. First-pass
workers must not see peer conclusions. Upward handoffs contain decisions,
evidence references, changed paths, tests, blockers, and falsification
conditions, not full transcripts. Escalate only when expected defect/rework
avoidance justifies the extra call and coordination latency.

## Decision table

| Signal | Route | Required gate |
| --- | --- | --- |
| Narrow, local, deterministic | `gpt-5.6-luna` | Packet acceptance checks |
| Cross-file coupling or meaningful ambiguity | `gpt-5.6-terra` | Tests plus evidence review |
| High-impact boundary or consequential uncertainty | Terra review/challenger | Sol decision before integration |
| Irreversible or materially disputed re-plan | Second `gpt-5.6-sol` | Root reconciles typed plan deltas |
| Final DAG, integration, and closure | Sol root | Integrated acceptance evidence |

## Stop rules

Stop dispatch when the DAG has no unowned ready work, the child cap or epic
budget is reached, or additional workers are unlikely to change the decision.
Stop after one transient retry and one model escalation per packet. Stop and
re-plan on dependency conflict, scope change, or failed critical acceptance
evidence. An implemented ticket is not closed until its changes are integrated
by the root and the epic-level acceptance evidence passes.
