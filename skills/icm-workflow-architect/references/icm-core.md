# ICM Core for Codex Workflows

Use this reference when writing contracts or resolving a structural disagreement.

## Five design principles

1. **One stage, one job.** A stage completes one transformation and writes one reviewable artifact.
2. **Plain text is the interface.** Markdown, JSON, and other inspectable text carry handoffs. Binary deliverables may exist, but their decision state and provenance remain readable.
3. **Load context in layers.** Give each stage only the catalog, contract, stable rules, and working artifact it needs.
4. **Every output is editable.** A human can inspect and change the artifact before downstream work begins.
5. **Configure the factory, not each product.** Stable preferences, schemas, voice, and constraints are maintained once and reused by every run.

The filesystem encodes four behaviors: folder numbering is sequencing, hierarchy is context scope, files are state, and downstream inputs are coordination.

## Five-layer mapping

| Layer | Codex repo-local workflow | Question |
|---|---|---|
| L0 | `SKILL.md` or root `AGENTS.md` | When does this apply and where do I start? |
| L1 | workflow `CONTEXT.md` | Which stage or node handles this task? |
| L2 | stage `CONTEXT.md` | What exactly do I read, do, write, and ask a human to check? |
| L3 | `_shared/`, `references/`, templates | What stable rules apply every run? |
| L4 | `output/`, run folders, drafts, receipts | What evidence and artifacts belong to this run? |

L0 through L2 are catalogs and contracts, not content stores. L2 is the control surface because it declares the exact context a stage loads.

## Stage contract

Each stage `CONTEXT.md` contains:

```markdown
# 02-ticket-draft

One job: turn an approved evidence report into a reviewable ticket draft.

## Inputs

- Working: `../01-investigation/output/<slug>-evidence.md`
- Reference: `../../_shared/ticket-policy.md`
- Do not load: unrelated prior runs or credential files

## Process

1. Read the approved evidence report.
2. Draft the ticket to the repository's ticket schema.
3. Verify every claim is supported or marked as an assumption.

## Audit

| Check | Pass condition |
|---|---|
| Evidence | Every factual claim points to evidence in the input report. |

## Outputs

- `output/<slug>-ticket-draft.md`

## Human Check

Confirm scope, priority, and acceptance criteria before any ticket is created.
```

Use exact paths for stable references. Working artifact paths may include a documented run slug. Keep the process short; detailed domain rules belong in L3.

## Canonical sources

- A rule, schema, or definition has one authoritative file.
- Routing files link to that file and do not restate it.
- Previous outputs are evidence, not templates for quality. Use maintained reference docs to define how future output should look.
- Generated indexes are rebuilt, not hand-maintained.
- If an external service is the source of truth, store an identifier and retrieval rule rather than a stale copy unless an audit snapshot is explicitly required.

## Context and size discipline

A useful stage load is generally entry + contract + targeted references + the current working artifact. If that set becomes unwieldy, split the stage, narrow the Inputs list, or split a large reference by decision-relevant topic.

Targets:

- entry catalog: about 60 lines or fewer;
- `CONTEXT.md`: under 80 lines;
- focused reference: under 200 lines;
- total stage context: roughly 2,000 to 8,000 tokens when practical.

## Where ICM is a poor fit

Do not pretend folder orchestration solves:

- real-time agent-to-agent negotiation;
- high-concurrency multi-user execution requiring queues and isolated state;
- complex automatic branching driven by model output;
- a one-off task with no durable review boundary.

Those cases may need ordinary code, workflow infrastructure, or just a concise prompt.
