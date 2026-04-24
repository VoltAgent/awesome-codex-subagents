# Contributing to Awesome Codex Subagents

Thanks for contributing.

This repository is a curated collection of Codex-native subagents (`.toml` files). Contributions should prioritize practical usefulness, clear scope, and compatibility with official Codex behavior.

## How to Contribute

### Add a New Subagent

1. Choose the correct category under `categories/`.
2. Add one `.toml` file for the new agent.
3. Update both:
   - `README.md` (main category listing)
   - `categories/<category>/README.md` (linked bullet + short description)
4. Keep agent names sorted alphabetically where possible.
5. Open a PR with the use case and why this agent is distinct.

### Improve an Existing Subagent

1. Keep the role bounded (avoid broad persona text).
2. Preserve Codex-native format.
3. Update relevant README descriptions if behavior or intent changed.
4. Include before/after rationale in your PR.

## Required Agent Format

Each agent must be a valid TOML file and include:

- `name`
- `description`
- `developer_instructions`

Common optional fields:

- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `mcp_servers`

## Authoring Quality Bar

`developer_instructions` should be concrete and task-shaped. Use this structure:

- `Working mode`
- `Focus on`
- `Quality checks`
- `Return`
- `Do not ... unless explicitly requested by the parent agent.`

Avoid:

- Unsupported tool/platform assumptions
- Generic roleplay text with no output contract
- Scope creep instructions ("always do everything")

## Model and Sandbox Guidance

- Prefer `gpt-5.5` for complex reasoning/review roles.
- Prefer `gpt-5.4-mini` for lighter search/synthesis roles.
- Use `read-only` by default for review/research agents.
- Use `workspace-write` only when the agent must implement changes.

## Validation Checklist (Before PR)

- All links in `README.md` and category READMEs resolve.
- New/edited `.toml` files parse correctly.
- Agent `name` is unique across repository.
- Main and category READMEs include the new agent.
- Descriptions stay concise and accurate to current behavior.

## Pull Request Checklist

- [ ] Added/updated agent TOML file(s)
- [ ] Updated main `README.md`
- [ ] Updated category `README.md`
- [ ] Verified links and TOML validity
- [ ] Included clear PR description and motivation

## Style Notes

- Keep documentation in English.
- Prefer precise, practical wording over marketing language.
- Keep descriptions short; keep instructions high-signal.

## License

By contributing, you agree your contributions are provided under the repository license terms.
