# ICM Form Selection

Choose the form from the repeating unit, not from the vocabulary in the source prompt.

| Repeating unit | Form | Optimizes for |
|---|---|---|
| One run that produces a deliverable | Pipeline | Ordered handoffs and review gates |
| Several kinds of runs sharing stable context | Umbrella | Routing across sibling pipelines without duplicating shared rules |
| A record that accumulates over time | Record library | Uniform creation, lookup, lifecycle, and history |
| Knowledge, claims, and evidence | Knowledge bundle | Layered retrieval, provenance, and links |
| Teams, processes, data, and handoffs | Context map | Navigating an organization as typed nodes and edges |
| A repository or folder later agents will edit | System map | Source-backed object/process cards and change impact |

## Pipeline

Use for SOPs, reporting, investigation, content production, and other repeatable sequences. Put stage boundaries where a durable artifact is reviewed or responsibility changes. Each stage consumes the prior artifact and stable references, produces one edit surface, and stops at a human check.

Avoid stages that merely rename an internal thought. If no one benefits from seeing or editing the intermediate result, combine it with the adjacent stage.

## Umbrella

Use when several pipelines share policy, voice, schemas, or identity but have different runs and outputs. The umbrella entry routes to each pipeline. It does not summarize the pipelines' internal stages. Shared factory files have one home and are linked from children.

## Record library

Use when the main object persists and accumulates: client, incident, account, interview, session, or ticket. Create each record from `_templates/`, use stable identifiers, and define a small lifecycle. Keep indexes terse and derivable where possible.

## Knowledge bundle

Use when the deliverable is a navigable model of a domain. Separate raw evidence from maintained synthesis, label provenance and confidence, and route by topic or task. Links form the graph; folders scope loading. Do not turn the catalog into a copied encyclopedia.

## Context map

Use for an organization. Define a closed set of useful node types such as team, process, job, data asset, and governance rule. Capture ownership and `consumes`/`produces` relationships so the connections are queryable. Add a new node type only when someone will actually query it.

## System map

Use when later agents must safely change a code or mixed-content tree. The subject remains authoritative. Cards cite source paths and distinguish live, leftover, and aspirational or unwired elements. Map nouns first, then real movements, then a change-impact index. Do not copy implementation behavior into the map.

## Composition

Forms can nest:

- a Pipeline can emit a Record library entry;
- each Record can contain a Knowledge bundle;
- an Umbrella can share one Knowledge bundle across multiple Pipelines;
- a repository can host a System map beside a Pipeline skill.

At every level, the local catalog routes one level down and stops. It does not duplicate the child's contents.
