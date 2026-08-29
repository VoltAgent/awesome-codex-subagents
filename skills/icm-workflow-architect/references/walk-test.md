# ICM Walk Test

Run the deterministic validator first, then walk the result as a cold agent with no conversation memory.

## Deterministic validation

From the installed or repository skill directory:

```bash
python3 scripts/validate_icm.py /absolute/path/to/workspace
```

Use `--allow-placeholders` only while the workspace is intentionally an unconfigured template. Use `--strict` when line-count and continuity warnings must fail CI.

The validator checks entry files, stage names and numbering, stage contracts, output folders, unresolved placeholders, reference sizes, and stable paths declared in stage Inputs.

## Cold walk

1. **Orient.** Open only `SKILL.md` or `AGENTS.md`. Can you say what the workflow handles and where to start?
2. **Route.** Open `CONTEXT.md`. Can you choose the correct stage without reading domain references?
3. **Act.** Open one stage contract. Does it name the working input, stable references, one job, one output, and the human check?
4. **Scope.** Follow only the declared references and working input. Can the stage run without loading the whole tree?
5. **Inspect state.** Can status be derived from outputs, run frontmatter, or external receipts?
6. **Trace ownership.** Does each rule have one canonical home? Do links land on the owning file rather than a second explanation?
7. **Check side effects.** Is every external mutation isolated behind approval and exact target identification?
8. **Check secrets.** Are only credential interfaces or variable names present, with no copied values?
9. **Check tokens.** Is entry + route + one contract + its declared inputs plausibly within the 2,000 to 8,000 token band?

## Failure interpretation

- If orientation takes more than two routing reads, shrink or split the catalog.
- If a contract repeats policy, move the policy to a reference and link it.
- If two stages share no reviewable artifact, combine them.
- If a stage needs unrelated prior outputs to infer quality, improve the maintained reference docs.
- If status depends on conversation memory, add a file, frontmatter field, or external receipt.
- If a mutation is mixed with investigation, split it into an approved final stage.

Fix structure rather than adding a long explanation about how to navigate a confusing structure.
