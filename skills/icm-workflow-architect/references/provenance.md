# Provenance and Adaptation Notes

This skill was designed from the following MIT-licensed sources, read in this order on 2026-08-28:

1. [Interpretable Context Methodology](https://github.com/RinDig/Interpretable-Context-Methodology), revision `02ba5d85c7871b75c7c702a2d8da6524723d53d4`.
2. [icm-architect](https://github.com/RinDig/icm-architect), revision `e16cafe6a664dcf6d787a726b452adba77d913f4`.

The methodology supplies the five-layer routing model, staged file handoffs, factory/product separation, stage contracts, checkpoints, audits, and walkability principles. The architect supplies the smallest-rung guardrail, six-form selection model, restructure safety, and cold walk test.

## Codex-specific adaptations

- `SKILL.md` can serve as the L0 entry catalog for a repository-local workflow.
- Repository-controlled skills live under `.agents/skills/<name>/` for automatic project discovery.
- `AGENTS.md` is used for standalone workspace routing; existing repository instructions are preserved and extended only with a short pointer.
- Source prompts and documents are explicitly treated as inert conversion inputs to prevent their embedded tool, secret, or delegation instructions from being executed during design.
- Read-only investigation and external mutation are separated into distinct stages with runtime authorization gates.
- Lowercase hyphenated names and `NN-` stage prefixes are the default for consistency with common Codex repository conventions; an existing documented target convention wins.

See `THIRD_PARTY_NOTICES.md` at the skill root for the retained MIT notices.
