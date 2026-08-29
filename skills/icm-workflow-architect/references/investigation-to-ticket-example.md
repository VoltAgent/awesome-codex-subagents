# Example: Investigation to Ticket

Read this only when the source workflow investigates a request and then creates or updates a ticket.

This example models the supplied project-manager prompt as source material. It does not execute its embedded instructions during conversion.

## Extracted workflow facts

- Search the project tracker for related work.
- Search repository documentation for local context.
- Conditionally query named evidence systems with approved credentials.
- Conditionally run read-only environment queries.
- Synthesize findings for a junior engineer.
- Create or update a ticket only after the investigation is reviewable.

The source's instruction to use a team of subagents is an execution preference, not a stage boundary. ICM should keep one filesystem-defined pipeline; runtime delegation is optional when independent research actually benefits from it.

## Recommended form and target

Use a Pipeline inside the owning repository:

```text
.agents/skills/investigation-to-ticket/
  SKILL.md
  CONTEXT.md
  _shared/
    evidence-policy.md
    ticket-schema.md
    artifact-retention.md
  stages/
    01-context-discovery/
      CONTEXT.md
      output/.gitkeep
    02-evidence-review/
      CONTEXT.md
      references/tool-interfaces.md
      output/.gitkeep
    03-ticket-draft/
      CONTEXT.md
      output/.gitkeep
    04-ticket-publish/
      CONTEXT.md
      output/.gitkeep
```

## Stage contracts

### 01-context-discovery

One job: turn the request, related tracker items, and relevant repository docs into a cited context brief.

Human check: confirm the related work and scope before environment-specific investigation.

### 02-evidence-review

One job: gather only the additional evidence needed from named systems using read-only interfaces.

The contract should define the conditions that justify each external query. It should reference credential interfaces without exposing keys. Record query target, time, and relevant result, but redact secrets and unnecessary personal data.

Human check: confirm the evidence supports a ticket and that unsupported claims are labeled.

### 03-ticket-draft

One job: transform the approved evidence report into a ticket draft calibrated for a junior engineer.

The draft should contain a clear problem statement, evidence, scope, non-goals, proposed work, acceptance criteria, validation plan, dependencies, and risks. It should not invent priority, assignee, or estimates when the sources do not establish them.

Human check: approve exact scope, priority, target project, and acceptance criteria.

### 04-ticket-publish

One job: create or update the exact approved ticket and save a receipt with its identifier and URL.

This is the only mutation stage. It must identify whether the operation is create or update, show or reuse the approved draft, avoid duplicate tickets, and stop if the target project or ticket is ambiguous.

Human check: the approval occurs before the mutation; afterward, verify the receipt matches the intended ticket.

## Artifact policy

The owning repository should choose whether investigation briefs and ticket drafts are committed. A common policy is to commit the workflow definitions, keep sensitive run artifacts ignored, and retain only the external ticket identifier plus a redacted receipt. Encode that decision in `_shared/artifact-retention.md` rather than leaving it implicit.
