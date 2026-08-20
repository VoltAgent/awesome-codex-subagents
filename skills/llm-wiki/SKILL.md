---
name: llm-wiki
description: Build and maintain a persistent, interlinked Markdown knowledge base from curated sources. Use when initializing an LLM Wiki, ingesting sources, answering from or crystallizing work into the wiki, checking wiki health, or evolving its schema, provenance, lifecycle, graph, search, privacy, or collaboration conventions. Do not use for ordinary project documentation or one-off file summarization that is not meant to compound over time.
---

# LLM Wiki

Treat the wiki as compiled, persistent knowledge: raw evidence stays authoritative and immutable; generated pages accumulate synthesis; a project-specific schema governs how the two relate. Preserve any established project layout and conventions instead of imposing this skill's defaults.

## Establish the local contract

Before reading broadly or writing:

1. Read applicable project instructions.
2. Locate the wiki schema. Check paths named by project instructions first, then likely files such as `.llm-wiki/schema.md`, `wiki/schema.md`, or a clearly marked section of `AGENTS.md`.
3. Read the schema, `index.md`, and the latest relevant `log.md` entries. At larger scale, use the search method named by the schema rather than loading the whole index.
4. Identify the requested mode: bootstrap, ingest, query, crystallize, lint, or evolve.

If a wiki already exists but has no explicit schema, infer its conventions from representative pages, state the inferred contract, and propose a schema before making broad structural changes. Ask only when a missing choice would materially alter the knowledge model, privacy boundary, or existing layout.

## Preserve the three layers

- **Raw sources:** Human-curated evidence. Read but never edit, rename, reorganize, redact in place, or silently discard. If a source contains secrets or sensitive personal data, keep those details out of generated pages and report the exposure without reproducing it.
- **Wiki:** LLM-maintained Markdown pages, summaries, connections, index, and log. Keep it internally consistent and useful to humans, not merely optimized for retrieval.
- **Schema:** The evolving project contract for paths, entity and relationship types, provenance, page creation, contradictions, retention, privacy, and workflows. Change it deliberately and log the reason.

Never blur source text with synthesis. A reader must be able to distinguish direct evidence, supported inference, unresolved interpretation, and the agent's recommendation.

## Choose the operating mode

### Bootstrap

Use only when the user asks to create or initialize a wiki. Read [references/bootstrap-and-schema.md](references/bootstrap-and-schema.md), agree on or infer a minimal domain model, and create the smallest viable layout. Prefer `scripts/init_wiki.py` for the default layout; it creates missing files without overwriting existing ones.

### Ingest

Read [references/operations.md](references/operations.md). Process each source as an integration, not an isolated summary:

- assign a stable source identity and preserve useful locators;
- extract claims, entities, decisions, events, and domain-relevant relationships;
- find existing pages before creating new ones;
- update every materially affected synthesis page;
- represent disagreement and supersession explicitly;
- update the content index and append an audit entry in the same authorized change set;
- verify citations, links, and sensitive-data handling before finishing.

Batch ingest is acceptable when the schema defines deduplication, conflict handling, and review expectations. Otherwise prefer small batches whose effects can be checked.

### Query

Read [references/operations.md](references/operations.md). Search the compiled wiki first, then inspect supporting raw sources for decisive, ambiguous, contested, or freshness-sensitive claims. Follow typed relationships when the question concerns impact, causality, ownership, dependencies, or change over time.

Answer with provenance and calibrate certainty to the evidence. Distinguish absence of evidence from evidence of absence. Filing the answer or logging the query changes the workspace; do so only when the user requested it or the project's established policy explicitly authorizes it.

### Crystallize

Read [references/operations.md](references/operations.md). Turn a completed research thread, debugging session, comparison, or analysis into a durable digest. Record the question, findings, evidence, affected entities, decisions, unresolved issues, and reusable lessons. Integrate strong lessons into existing semantic or procedural pages rather than leaving them only in the digest.

### Lint

Read [references/operations.md](references/operations.md). Check provenance, contradictions, supersession, staleness, broken or missing links, duplicate entities, orphan pages, schema drift, sensitive-data leakage, and index/log consistency. A request to audit or diagnose is read-only; apply repairs only when the user also asks for fixes or existing project policy clearly authorizes self-healing.

### Evolve

Read [references/scaling-and-governance.md](references/scaling-and-governance.md) when adding lifecycle management, a typed knowledge graph, scalable search, automation, quality scoring, privacy scopes, or multi-writer coordination. Add these in response to observed pressure, not as mandatory day-one infrastructure.

## Non-negotiable knowledge invariants

- Every material factual claim has traceable provenance to one or more raw sources or a clearly labeled primary observation.
- New evidence never silently overwrites conflicting old evidence. Preserve history, link superseding claims, and explain the resolution basis.
- A source count is not independent corroboration when sources repeat the same upstream claim.
- Recency matters only for time-sensitive knowledge; authority and directness may outweigh it.
- Retention lowers retrieval priority before it deletes anything. Deletion, bulk merge, and irreversible cleanup require explicit authorization and an audit trail.
- Confidence must be explainable from evidence, freshness, contradiction, and source independence. If the schema uses numeric scores, define the rubric; never present an uncalibrated number as a probability.
- Generated pages must not expose credentials, tokens, private material, or unnecessary PII from sources.
- Keep index and log roles separate: the index describes current content; the log records chronological operations.
- Validate changed links, citations, index entries, and log entries before declaring a write complete.

## Scale proportionally

Start with raw sources, wiki pages, a schema, `index.md`, and `log.md`. Add richer mechanics only when needed:

1. lifecycle and supersession when claims change or rot;
2. typed entities and relationships when cross-page impact questions become common;
3. dedicated search when the index no longer fits comfortably in context;
4. event-driven automation when manual maintenance is measurably burdensome;
5. collaboration controls when multiple writers need shared and private scopes.

Pages remain the human-readable system of record even when a graph or search index augments navigation. Derived indexes are rebuildable; raw evidence and audited wiki history are not.
