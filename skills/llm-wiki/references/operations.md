# Wiki Operations

Read the sections needed for the requested operation. Follow the project's schema when it differs from these defaults.

## Ingest

### 1. Establish source identity

Confirm the source is inside the authorized raw collection or otherwise supplied by the user. Record a stable source ID, title, creator or origin when known, source date, acquisition date if useful, format, and stable locators. Do not edit the raw item.

Inspect text first, then view referenced images, tables, audio, video, or attachments when they carry material information. Do not imply that an uninspected modality was reviewed.

### 2. Extract before integrating

Capture:

- central claims and their evidence;
- entities, events, decisions, concepts, and definitions;
- typed relationships that matter in this domain;
- dates and applicability windows;
- contradictions, caveats, uncertainty, and open questions;
- sensitive details that must not propagate into generated pages.

Separate what the source says from what the agent infers. Notice when multiple sources depend on the same upstream evidence.

### 3. Reconcile with current knowledge

Search the index and likely aliases before creating pages. Read existing pages for each affected entity or topic. For each incoming claim, decide whether it:

- reinforces an existing claim;
- adds detail without changing it;
- conflicts with it;
- supersedes it because the subject changed;
- is unrelated and needs a new page;
- lacks enough support and should remain provisional.

Do not resolve conflicts by recency alone. Weigh directness, source authority, independence, applicability, and whether the world itself changed. Preserve unresolved alternatives.

### 4. Write an atomic knowledge change set

Within the authorized edit:

1. create or update the source summary if the schema uses one;
2. update all materially affected topic, entity, decision, timeline, or procedural pages;
3. add precise citations and typed links;
4. update claim status, last-confirmed data, and supersession links where applicable;
5. update `index.md` with current one-line descriptions;
6. append one parseable `log.md` entry describing the source, changed pages, material conflicts, redactions, and reason.

A useful log heading is `## [YYYY-MM-DD] ingest | Source title`. Do not rewrite old log entries to make history look cleaner; add a corrective entry.

### 5. Verify

Check that raw files are unchanged, new links resolve, citations point to real evidence, index entries match current pages, conflicts are visible, no sensitive values leaked, and the log describes the actual changes.

## Query

### Retrieval

At modest scale, read the schema and index, then search candidate pages using exact terms, aliases, and related entities. `rg` is a useful baseline. Read enough neighboring pages to follow important connections.

When the schema defines a larger-scale search stack, combine the available streams:

- lexical search for exact names and phrases;
- semantic search for conceptually related material;
- graph traversal for dependencies, causes, ownership, contradiction, and impact.

Fuse evidence conceptually even when no formal reciprocal-rank implementation exists. Search indexes and embeddings are derived aids, not sources of truth.

### Synthesis

Answer from the wiki's current understanding, but verify decisive, contested, low-confidence, or freshness-sensitive points against raw sources. Cite the evidence at the granularity needed to audit the answer. State unresolved conflicts and missing evidence.

For impact questions, start at the named entity and traverse outgoing and incoming dependency-like relations. For historical questions, follow supersession and timeline links. For comparison, use the same criteria for every option.

### Filing the result

Crystallize only when the user requests it or the schema authorizes automatic filing. Prefer updating an existing page when the answer refines a known topic. Create a new analysis page when the question, evidence trail, and conclusion form a reusable artifact of their own.

## Crystallize

Distill completed work into a durable page with:

- the original question or objective;
- concise outcome;
- evidence and source locators;
- reasoning or decision criteria;
- entities, files, and relationships involved;
- what changed in the current understanding;
- unresolved issues and next questions;
- reusable semantic facts or procedures extracted from the episode.

Update the relevant entity, topic, or procedure pages so reusable knowledge is not trapped in a session digest. Do not treat chat recollection as stronger evidence than the underlying artifacts. Exclude transient chatter, secrets, and unnecessary personal detail.

## Lint

### Evidence integrity

- unsupported material claims;
- citations to missing or moved sources;
- source-summary drift from raw evidence;
- circular claims where wiki pages cite only each other;
- duplicated sources mistaken for independent corroboration.

### Knowledge lifecycle

- conflicting active claims with no contested status;
- superseded claims still presented as current;
- time-sensitive claims past their review window;
- confidence inconsistent with evidence or contradictions;
- low-value stale material dominating navigation.

Deprioritize before deletion. Recommend fresh evidence when decay reflects uncertainty rather than irrelevance.

### Structure and navigation

- broken, missing, or ambiguous links;
- orphan pages and overloaded hub pages;
- duplicate entities or aliases without canonical mapping;
- important recurring concepts lacking pages;
- relationships encoded inconsistently;
- index entries that are missing, stale, or duplicated.

### Governance and operations

- sensitive data copied into generated pages;
- shared/private scope violations;
- mutations missing from the log;
- log entries inconsistent with the actual change history;
- schema rules that current pages no longer follow.

Report findings by severity, evidence, affected pages, and proposed repair. For an authorized repair pass, fix deterministic issues first, preserve ambiguous conflicts for review, update the index, and append a log entry.
