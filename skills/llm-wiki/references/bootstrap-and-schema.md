# Bootstrap and Schema Design

Read this reference when initializing a new LLM Wiki or deliberately redesigning its schema.

## Discover before creating

Inspect the project for existing knowledge directories, source collections, naming conventions, instruction files, privacy rules, and version-control expectations. Reuse established paths when their roles are clear. Do not initialize a second wiki beside an existing one merely because its names differ from the defaults.

Clarify only decisions that materially affect the result:

- the domain and the questions the wiki should answer;
- where immutable sources live and which formats occur;
- whether generated knowledge is private, shared, or mixed;
- expected scale and update frequency;
- whether edits are reviewed interactively or accepted in batches.

When the user has not expressed a preference, start minimal and record assumptions in the schema.

## Minimal default layout

```text
project/
|-- raw/                    Human-curated, immutable source material
|-- wiki/                   Agent-maintained Markdown knowledge
|   |-- index.md            Current content catalog
|   `-- log.md              Append-only operation history
`-- .llm-wiki/
    `-- schema.md           Project-specific knowledge contract
```

Run `python <skill-dir>/scripts/init_wiki.py <project-root>` to create only the missing parts of this layout. Use its path options when the project already has preferred names. The script does not overwrite existing files.

Avoid creating entity, topic, source-summary, or analysis subdirectories until the domain suggests useful categories. Add them to the schema when introduced.

## Schema contents

Keep the schema concise enough to read at the start of every wiki operation. Define:

### Purpose and boundaries

- primary audience and recurring questions;
- what belongs in raw sources, compiled wiki pages, and neither;
- source immutability and generated-content ownership;
- private/shared scopes and prohibited content.

### Layout and identity

- canonical paths for sources, pages, index, log, attachments, and derived indexes;
- stable source IDs and page naming rules;
- entity types relevant to the domain;
- a small controlled relationship vocabulary, such as `uses`, `depends-on`, `owned-by`, `caused`, `contradicts`, `supports`, and `supersedes`.

Prefer relationship types that answer real questions. Do not add generic graph machinery simply to restate prose.

### Page contract

Specify the minimum metadata and sections needed for the domain. A useful starting point is:

```yaml
---
kind: topic
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - source-id
---
```

Common page sections are `Summary`, `Current understanding`, `Evidence`, `Relationships`, `Contradictions`, and `Open questions`. Source summaries may instead use `Key claims`, `Context`, and `Connections`. Treat this as a configurable pattern, not a mandatory universal template.

### Provenance

Define a citation form that preserves a stable source ID plus the most precise available locator: page, section, timestamp, row, commit, message, or line range. Use direct raw-source links where practical. When a page contains many independently sourced claims, cite claims inline rather than relying only on page-level frontmatter.

Mark agent synthesis and inference explicitly. Do not fabricate precision when a source lacks stable locators.

### Claim lifecycle

At minimum support `active`, `contested`, and `superseded`. For changing domains, also record `first_seen`, `last_confirmed`, independent supporting sources, contradictions, and a link from the old claim to its replacement.

If confidence is used, prefer an explainable rubric such as `low`, `medium`, and `high`. Numeric scoring is acceptable only when the schema defines how evidence, independence, authority, recency, and contradictions affect the score. Keep the components visible so the number can be audited.

### Workflow contracts

Define what ingest, query, crystallize, lint, and schema evolution must update. State whether ordinary queries are logged or filed back, whether self-healing edits are automatic, and which mutations require review.

### Scale triggers

Record observable triggers rather than premature infrastructure:

- move beyond a single index when it becomes expensive to load or misses relevant pages;
- add typed graph data when relationship traversal repeatedly improves answers;
- add lifecycle decay when stale material crowds current results;
- automate only stable, well-reviewed operations;
- add writer coordination before parallel edits become common.

## Schema evolution

Update the schema when repeated usage reveals a stable convention or failure mode. Avoid encoding a one-off preference as a universal rule. For each material schema change:

1. explain the observed problem;
2. update affected templates or pages if authorized;
3. append a log entry with the reason and migration scope;
4. check that old pages remain interpretable.
