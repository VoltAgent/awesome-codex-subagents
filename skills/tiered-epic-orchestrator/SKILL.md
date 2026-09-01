---
name: tiered-epic-orchestrator
description: Plan and execute large ticketed epics through one authoritative Sol root and bounded Terra/Luna subagents, using dependency-aware work packets, controlled writes, staged integration, and epic-level verification. Use for multi-ticket or cross-module implementation whose dependencies, ownership, or acceptance paths make flat delegation unsafe. Do not use for routine single-ticket changes, analysis-only decisions, or work that cannot benefit from independent bounded tasks.
---

# Tiered Epic Orchestrator

Complete a complex epic as one integrated result, not as a collection of locally finished tickets. Use the expensive root for ambiguity and control; use cheaper agents for evidence, bounded implementation, and review.

This skill does not broaden the user's authorization. Preserve existing changes, repository instructions, approval boundaries, and restrictions on destructive or external actions.

## Applicability

Use this workflow when several tickets or modules must compose and at least one of these conditions holds:

- implementation can proceed in independent dependency waves;
- interfaces, schemas, migrations, configuration, generated artifacts, or shared tests connect multiple tickets;
- multiple writers would otherwise contend for the same repository state;
- ticket completion is weaker than the required end-to-end outcome;
- hidden dependencies or expensive rework make an explicit execution plan valuable.

Do not invoke the full workflow for a small, obvious, single-owner change. Handle that directly or with one bounded worker. For a consequential decision without implementation, use a decision-analysis workflow instead.

## Authority invariants

1. **One root owns the epic.** The root approves scope, the dependency graph, plan versions, dispatch, integration order, exceptions, and final acceptance.
2. **Assume a Sol root.** This workflow is designed for an active `gpt-5.6-sol` root. A skill cannot upgrade the current root. Inspect effective session metadata when available; if it is unavailable, record the Sol assumption. If the root is known not to be Sol, pause before write-bearing fan-out unless the user explicitly accepts another control-plane model, and do not describe the run as Sol-led.
3. **No recursive spawning.** Workers must not create descendants. They return a dependency request or `plan_drift`; the root decides whether to add work.
4. **One owner per mutable scope.** Parallel task labels do not make overlapping files, contracts, migrations, generated outputs, fixtures, or configuration safe.
5. **Workers propose evidence; the root changes state.** A worker cannot mark dependencies satisfied, close tickets, waive checks, or declare the epic complete.
6. **Integrated evidence defines done.** Local changes and passing packet tests make work eligible for integration, not complete.

## Load the operating references as needed

- Before compiling tickets, defining the ledger, or re-planning, read [work packets and state](references/work-packets-and-state.md).
- Before choosing a planner or worker model, setting fan-out, retrying, or escalating, read [model routing](references/model-routing.md).
- Before any parallel write, merge, integration decision, or completion claim, read [integration and verification](references/integration-and-verification.md).
- When a durable file-backed ledger is warranted and permitted, copy and adapt [the epic manifest template](assets/epic-manifest.template.yaml). Prefer an existing project or ticket-system convention; do not add a tracked runtime artifact merely because the template exists.

## 1. Intake and preflight

Before delegation:

1. Read applicable project instructions and inspect the actual repository state, including user-owned uncommitted changes.
2. Normalize the epic into observable outcomes, source tickets, in-scope and out-of-scope behavior, nonfunctional requirements, constraints, and epic-level acceptance criteria.
3. Identify external or destructive operations that need separate authorization. Planning the operation is not authorization to perform it.
4. Establish the authoritative state location. Use an existing tracker or project artifact when available; otherwise keep a structured task ledger. Persist a new repository file only when it is useful and within scope.
5. Set a child-agent budget. Start with no more than three concurrent task workers and a hard ceiling of four active children, leaving capacity for a planner, reviewer, or diagnostic agent. Use fewer when the dependency graph or integration capacity does not justify the slots.

If ticket text conflicts with repository evidence, record the conflict. Do not silently rewrite the user's intended outcome.

If normalized requirements materially conflict and the choice belongs to a product, legal, compliance, operational, or other authorized human decision maker, limit work to safe read-only discovery and planning. Present the conflict and request the decision before dispatching dependent writers.

## 2. Gather evidence without over-planning

Skip a discovery swarm when the affected code, ownership, dependencies, and tests are already clear.

Otherwise dispatch narrowly scoped, read-only Luna agents to gather independent evidence such as:

- ticket-to-code and owner mapping;
- public and internal interface consumers;
- schemas, migrations, configuration, generated files, locks, and fixtures;
- authoritative build, test, and validation commands;
- hidden cross-ticket write or runtime dependencies.

Require paths, symbols, commands, observed facts, uncertainty, and unresolved questions. Luna findings are evidence candidates, not architectural decisions.

Keep prompts neutral and minimal. Do not give a planning challenger the root's chain of reasoning or another worker's conclusion unless the task is explicitly to critique that conclusion.

## 3. Compile the epic into an executable graph

Do not map one agent to each ticket automatically. A ticket is a product boundary; a work packet is an execution and integration boundary.

The root must produce a versioned dependency graph whose nodes have one owner, bounded mutable scope, explicit inputs and outputs, observable acceptance checks, and typed dependencies. Separate verified edges from inferred or precautionary edges.

Use a read-only Terra-high planning challenger when any trigger is present:

- cross-package or cross-service dependencies;
- public API, schema, migration, configuration, or generated-artifact impact;
- security, authorization, data-integrity, reliability, or rollback consequences;
- contradictory requirements or missing executable acceptance criteria;
- overlapping ownership, a cycle, or low-confidence critical-path edges.

Use a second Sol planning pass only for an irreversible decision or a material unresolved dispute about a public contract, migration, security property, data policy, or critical-path dependency. The planner is advisory. The root records accepted and rejected deltas and remains the only coordinator.

Freeze shared boundary contracts before dependent workers begin when practical. If the contract cannot be frozen, serialize the affected work and make the uncertainty explicit.

## 4. Dispatch dependency waves

Dispatch only nodes whose predecessor evidence has been accepted by the root.

Every worker prompt must state:

- epic and packet identifiers plus plan version and base revision;
- one objective and explicit non-goals;
- prerequisite evidence and consumed/produced contracts;
- allowed and forbidden mutable scope;
- effective model, reasoning effort, sandbox, workspace or worktree, and budget;
- acceptance checks and expected receipt;
- escalation and stop conditions;
- that other workers may be active and their changes must not be reverted.

Prefer the smallest context that makes the packet self-contained. Send relevant evidence and repository locators, not the entire epic transcript.

Continue useful root work while independent children run, but do not change contracts underneath active packets. Wait at dependency and integration gates rather than after every minor update.

## 5. Accept results or re-plan

Treat each worker response as a claim to evaluate against its receipt contract.

- `complete`: checks passed and evidence is present; the packet may enter review or integration.
- `blocked`: a declared dependency, permission, environment, or decision is unavailable.
- `failed`: work stayed in scope but did not satisfy its checks.
- `plan_drift`: an assumption, dependency, contract, base revision, or ownership boundary is no longer valid.

Before integrating a change to security or authorization behavior, data integrity, a public contract, an irreversible migration, or a generated shared artifact, run an independent read-only Terra-high review of the actual diff and its evidence. The earlier planning challenge does not replace changed-artifact review. If the required reviewer is unavailable, use an independent higher-capability reviewer or pause and disclose the missing gate rather than silently lowering it.

Retry only a demonstrably transient tool or environment failure, once, while preserving the first failure. Fix an ordinary packet-local defect within the same ownership boundary. Escalate ambiguity or cross-file reasoning from Luna to Terra. Re-plan when a contract, dependency, acceptance criterion, or ownership boundary changes. Never retry deterministic failures until they disappear.

When a plan change affects active or completed downstream packets, mark them stale and revalidate or reissue them against the new plan version.

## 6. Integrate through one queue

Use one authoritative integration branch or checkout and one integration owner. The root may delegate the mechanics to a bounded Terra integrator, but not the acceptance decision.

In a shared checkout, allow one writer. Permit concurrent worktree writers only when mutable scopes and test resources are demonstrably isolated. Integrate results one at a time in dependency order and re-run affected contract and vertical-path checks after each shared-boundary change.

Do not resolve a semantic conflict by textual merge alone. Revisit ownership and contract evidence, then validate the reconciled behavior.

## 7. Verify the assembled epic

Distinguish these states:

- **implemented:** the packet passes its local gate;
- **integrated:** its change is accepted into the authoritative state and passes affected integration checks;
- **closed:** its mapped epic acceptance behavior passes or an authorized decision explicitly changes the requirement.

Before declaring the epic complete, map every original acceptance criterion to evidence on the assembled state. Run the authoritative relevant regression suite, contract checks, migration or configuration checks, and end-to-end paths proportionate to the epic's risk. An unexplained critical-path flake, unresolved contract, stale packet, or material blocked requirement prevents completion.

## 8. Report the outcome

Return a concise delivery record containing:

- epic outcome and acceptance status;
- ticket and packet states, including blocked or deferred work;
- integrated changes and contract decisions;
- verification commands and results;
- planner challenges, re-plans, retries, and escalations that materially affected the result;
- residual risks, waivers, and any user decision still required;
- effective model routing and concurrency at a useful aggregate level.

Do not equate agent activity, commits, merged files, or ticket checkboxes with a verified epic.
