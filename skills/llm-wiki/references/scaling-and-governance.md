# Scaling and Governance

Read this reference only when the minimal wiki is under real pressure or the user explicitly asks for an advanced capability.

## Memory lifecycle

Use tiers when the project accumulates many raw observations or repeated sessions:

- **Working:** recent, unprocessed observations with short retention.
- **Episodic:** session or event digests tied to a time and context.
- **Semantic:** cross-episode facts supported across observations.
- **Procedural:** repeatable workflows or patterns supported by practice.

Promotion is evidence-based, not merely age-based. Record the supporting lower-tier items. Do not promote a repeated claim when repetitions share the same origin.

Model forgetting as retrieval priority, not silent erasure. A retention policy may consider time since confirmation or useful access, knowledge type, stability of the domain, downstream importance, and contradiction. Reinforcement can raise priority, but simple access should not automatically increase truth confidence.

## Typed knowledge graph

Introduce a graph when users repeatedly ask questions that flat search handles poorly. Keep pages canonical and store graph data in frontmatter, structured blocks, or a rebuildable sidecar defined by the schema.

Define a controlled entity and relation vocabulary. Every edge should have:

- source and target identities;
- relationship type and direction;
- provenance;
- current status or applicability window;
- confidence rationale when uncertain.

Prefer meaningful relations such as `depends-on`, `uses`, `owned-by`, `caused`, `fixed-by`, `supports`, `contradicts`, and `supersedes` over `related-to`. Validate inverse and duplicate edges. Use graph traversal alongside text retrieval, not as a replacement for reading evidence.

## Search beyond a single index

Keep `index.md` as the human catalog. When it becomes too large or recall declines, add search in stages:

1. structured indexes by page type or domain;
2. lexical search with aliases and stemming;
3. semantic retrieval;
4. graph traversal;
5. rank fusion across independent result lists.

Evaluate retrieval against representative questions before adding complexity. Store only rebuildable search artifacts outside the canonical wiki, and document refresh behavior in the schema.

## Automation

Automate a workflow only after its manual form is stable and reviewable. Candidate events include new-source ingest, session-start context retrieval, session-end crystallization, contradiction checks on memory writes, and scheduled lint or retention review.

For every hook define:

- trigger and exact scope;
- authorized reads and writes;
- idempotency key or duplicate-detection behavior;
- sensitive-data filtering;
- failure and retry limits;
- human review threshold;
- audit record and rollback path.

Automation does not create permission for external sources, messages, schedules, or workspace mutations that the user has not authorized.

## Quality controls

Score or review outputs against observable dimensions: source coverage, citation validity, internal consistency, schema compliance, clarity, and sensitive-data safety. A second pass can improve quality, but it is not independent evidence.

Use thresholds to route low-quality material to review or rewrite. Keep the reasons alongside the score. Sample high-scoring outputs too, because self-evaluation can be confidently wrong.

## Privacy scopes

Define what is public, team-shared, project-private, and personal. Default derived knowledge to the most restrictive scope of its supporting sources unless an explicit policy permits broader disclosure. Promotion between scopes is a governed operation, not ordinary consolidation.

On ingest, detect likely credentials, tokens, secrets, private conversations, and unnecessary PII. Do not copy them into wiki pages or logs. Never mutate the immutable source to hide an exposure; report it and follow the project's incident or redaction process.

Bulk export, deletion, entity merge, and scope changes must be previewable, audited, and reversible where practical.

## Multiple writers

Before parallel writes, define ownership or partition work by source or page set. Each writer should record source IDs and intended pages, then re-read overlapping pages before applying changes.

Use deterministic merge for non-conflicting additions. Do not use last-write-wins for semantic conflicts: preserve both claims, mark the conflict, and resolve through evidence or human review. Keep private observations out of shared pages until the promotion policy allows them.

Coordination should remain lightweight: current scope, ownership, blockers, completion, and conflicts. It should prevent duplicate work without turning the wiki into a task-management system.
