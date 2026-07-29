---

name: multi-agent-debate
description: Analyze consequential technical, architectural, product, debugging, research, or planning questions through independent expert review, adversarial debate, and structured synthesis. Use when the decision contains meaningful uncertainty, competing trade-offs, or assumptions that benefit from challenge. Do not use for routine, low-risk, or narrowly factual tasks.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multi-Agent Debate

Use a bounded multi-agent debate to analyze the user's question.

The purpose of this workflow is not to manufacture consensus. Its purpose is to expose competing assumptions, identify disagreements, test arguments, and produce a decision that preserves material uncertainty.

## Applicability

Use this workflow when at least one of the following applies:

* The decision has meaningful architectural, operational, financial, security, product, or delivery consequences.
* Several plausible approaches have different trade-offs.
* The problem contains uncertain or weakly supported assumptions.
* A premature consensus could hide an important risk.
* Independent investigation can materially improve the answer.

Do not use this workflow when:

* The question has a straightforward factual answer.
* The task is routine or low consequence.
* The agents would perform substantially identical work.
* Coordination cost is likely to exceed the value of additional analysis.
* The user has requested a fast or minimal answer.

## Default Configuration

Unless the user specifies otherwise:

* Use 3 to 5 expert agents.
* Use 2 debate rounds after the initial analysis.
* Run independent analysis in parallel.
* Keep all agents read-only unless implementation is explicitly requested.
* Do not modify files or execute a proposed decision during the debate.
* Use a separate synthesis step after debate concludes.
* Stop early when another round is unlikely to materially change the decision.

## Phase 1: Frame the Question

Before spawning agents, state:

1. The decision or question being evaluated.
2. The relevant constraints.
3. The known facts.
4. The assumptions requiring validation.
5. The decision criteria.
6. The expected final deliverable.

Do not silently change the user's question.

If necessary information is unavailable, record it as an evidence gap rather than inventing it.

## Phase 2: Select the Experts

Select 3 to 5 experts with narrow, materially different mandates.

Choose roles based on the question rather than using the same team for every task.

Possible roles include:

* Implementation Simplifier
* Software Architect
* Product Manager
* Security Reviewer
* Reliability Engineer
* Test Strategist
* Operations Reviewer
* Cost and Delivery Analyst
* User Advocate
* Data Model Reviewer
* Domain Specialist
* Skeptical Generalist

Each role must have:

* A distinct mandate.
* A specific decision criterion.
* A failure mode it is responsible for detecting.
* Explicit boundaries on what it should not optimize.

Avoid assigning multiple roles that differ only in title.

Present the selected panel before beginning the analysis:

| Expert | Mandate | Primary criterion | Failure mode |
| ------ | ------- | ----------------- | ------------ |

## Phase 3: Independent Analysis

Spawn one subagent for each expert.

Run these agents in parallel.

Do not provide one expert with another expert's initial analysis. Wait until every expert has returned before beginning debate.

Give every expert:

* The same problem statement.
* The same known evidence.
* The same constraints.
* Its unique role and mandate.
* The required response format below.

Require each expert to return:

### Position

A concise recommendation from the assigned perspective.

### Key assumptions

List the assumptions on which the position depends.

### Evidence

Identify supporting evidence. Distinguish verified facts from inference.

### Strongest argument

State the strongest reason to adopt the position.

### Primary risks

Identify the most consequential risks or failure modes.

### Rejected alternatives

Identify plausible alternatives and explain why the expert rejects them.

### Falsification conditions

State what evidence would cause the expert to change its conclusion.

### Confidence

Use:

* HIGH: directly supported by authoritative or primary evidence.
* MEDIUM: supported by incomplete evidence or defensible inference.
* LOW: speculative, weakly supported, or dependent on major assumptions.

## Initial Position Summary

After every expert returns, summarize the initial positions before allowing debate.

Use this structure:

### Initial positions

| Expert | Recommendation | Strongest argument | Primary risk | Confidence |
| ------ | -------------- | ------------------ | ------------ | ---------- |

### Areas of agreement

Record propositions supported by multiple experts.

### Material disagreements

Record:

* The proposition in dispute.
* The experts on each side.
* The assumptions causing the disagreement.
* The evidence needed to resolve it.

### Evidence gaps

List missing facts that could materially change the result.

Do not synthesize the final recommendation yet.

## Phase 4: Debate Round 1, Cross-Examination

Provide every expert with the summarized initial positions and the full public conclusions of the other experts.

Do not ask agents to merely restate their positions.

Require each expert to:

1. Identify the strongest conflicting position.
2. Restate that position fairly.
3. Challenge its weakest material assumption.
4. Identify any evidence the opposing expert overlooked.
5. Acknowledge at least one valid point from another expert.
6. Revise its own position when warranted.
7. State whether its confidence increased, decreased, or remained unchanged.

Require this response format:

### Position challenged

Identify the expert and proposition being challenged.

### Fair restatement

Restate the opposing argument without caricature.

### Challenge

Explain the material weakness, unsupported assumption, or overlooked consequence.

### Valid opposing point

Identify what the opposing position gets right.

### Revised position

State any change to the original recommendation.

### Confidence change

State the new confidence and why it changed.

## Round 1 Summary

After every expert responds, create:

### Challenges raised

| Challenger | Position challenged | Core challenge | Evidence cited |
| ---------- | ------------------- | -------------- | -------------- |

### Position changes

| Expert | Original position | Revised position | Reason |
| ------ | ----------------- | ---------------- | ------ |

### Disagreements resolved

List disagreements resolved during the round and explain how they were resolved.

### Disagreements remaining

For each unresolved disagreement, record:

* The competing conclusions.
* The underlying assumptions.
* Whether the disagreement is factual, predictive, or value-based.
* What evidence would resolve it.

### Round 1 synthesis

Produce a provisional synthesis that:

* Combines compatible conclusions.
* Rejects arguments weakened by cross-examination.
* Preserves unresolved disagreements.
* Does not force consensus.
* Identifies the current leading option and its principal vulnerability.

## Phase 5: Debate Round 2, Adversarial Review

Use a second round only when unresolved disagreements or consequential uncertainty remain.

Assign one agent as the devil's advocate. Prefer an expert whose original mandate is suited to challenging consensus. Spawn a separate devil's advocate when necessary.

Provide the Round 1 synthesis to all experts.

Require each expert to examine the proposed synthesis rather than defend its original identity.

Each expert must answer:

1. What is the strongest argument against the provisional synthesis?
2. What shared assumption might all experts have inherited?
3. What important second-order consequence remains underexamined?
4. What could make the recommended option fail in practice?
5. What safeguard, experiment, or decision gate would reduce that risk?
6. Does the expert accept, conditionally accept, or reject the synthesis?

The devil's advocate must specifically:

* Attack apparent consensus.
* Look for correlated assumptions.
* Identify missing stakeholders.
* Test reversibility and exit costs.
* Examine the cost of being wrong.
* Propose at least one plausible counterexample.
* Avoid disagreement that is merely rhetorical.

## Round 2 Summary

Create:

### Consensus stress test

| Risk or challenge | Raised by | Severity | Synthesis response |
| ----------------- | --------- | -------- | ------------------ |

### Shared assumptions discovered

List assumptions shared across otherwise different expert positions.

### Remaining minority positions

Preserve any position that remains plausible but does not command majority support.

### Safeguards and validation steps

List concrete measures that would reduce uncertainty or contain downside risk.

### Round 2 synthesis

State:

* What survived adversarial review.
* What changed.
* What was rejected.
* What remains unresolved.
* Whether another debate round would likely change the result.

Do not run another round unless the expected informational value clearly exceeds the additional coordination cost.

## Phase 6: Final Synthesis

The parent agent, or a separately spawned synthesizer, must produce the final report.

The synthesizer must not simply count votes.

Weight arguments according to:

1. Quality and relevance of evidence.
2. Validity of assumptions.
3. Ability to survive counterarguments.
4. Consequence of being wrong.
5. Reversibility of the decision.
6. Fit with the user's stated constraints.
7. Feasibility of implementation and validation.

Use the following final format.

# Multi-Agent Debate Report

## Question

Restate the decision being evaluated.

## Constraints and decision criteria

Summarize the controlling constraints and criteria.

## Expert panel

| Expert | Mandate | Primary concern |
| ------ | ------- | --------------- |

## Initial positions

Summarize each expert's independent position.

## Debate Round 1

### Main challenges

Summarize the strongest cross-examination arguments.

### Position changes

Record which experts changed their conclusions or confidence.

### Round synthesis

Explain what the round established and what remained unresolved.

## Debate Round 2

Omit this section when the second round was unnecessary.

### Consensus challenges

Summarize attacks on the provisional synthesis.

### Shared assumptions

Identify correlated or inherited assumptions.

### Round synthesis

Explain how adversarial review changed the recommendation.

## Agreements

List the conclusions supported across materially different perspectives.

## Unresolved disagreements

For each unresolved disagreement, include:

* Competing positions.
* Cause of disagreement.
* Consequence of choosing incorrectly.
* Evidence that would resolve it.

## Rejected alternatives

Explain which alternatives were rejected and why.

## Final recommendation

Give one clear recommendation.

When appropriate, make it conditional rather than falsely definitive.

## Rationale

Explain why the recommendation survived the debate.

## Risks and dissent

Preserve the strongest minority position and the conditions under which it could prove correct.

## Confidence

Assign HIGH, MEDIUM, or LOW confidence to the final recommendation and explain the rating.

## Validation plan

Provide the smallest practical experiment, investigation, prototype, or decision gate that would most reduce the remaining uncertainty.

## Decision record

Conclude with:

* Decision:
* Deciding factors:
* Material assumptions:
* Principal risk:
* Reversal trigger:
* Next action:

## Quality Rules

Throughout the workflow:

* Do not reveal or request hidden chain-of-thought.
* Report concise conclusions, evidence, assumptions, and reasoning summaries.
* Distinguish facts from inference.
* Cite sources or repository evidence when available.
* Do not equate majority agreement with correctness.
* Do not erase minority positions during synthesis.
* Do not allow experts to change criteria merely to defend their original conclusion.
* Do not invent evidence to make the debate appear complete.
* Do not create unnecessary rounds.
* Do not let debate delay a reversible, low-risk decision without justification.
* Prefer a conditional recommendation when evidence does not support certainty.
