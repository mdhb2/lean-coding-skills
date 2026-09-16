# LCS Explore Interview Protocol

Use this protocol for every interactive `lcs-explore` session.

The goal is to resolve meaningful uncertainty quickly without making the user feel trapped in an endless interview.

## Contents

1. Explore Levels
2. Level Selection & Adaptation
3. Question Budget
4. Interview Rounds
5. Multiple-Choice & Recommendations
6. Technical Explanations
7. Progress & Recaps
8. Partial / Custom / Contradictory Answers
9. Adaptive Follow-Up
10. End-of-Explore Control

## 1. Explore Levels

Before the main interview, recommend one Explore Level.

### Easy

Estimated question budget: **6-9**

Use for:

- small features,
- simple changes,
- few dependencies,
- low architectural impact,
- low-risk decisions.

### Medium

Estimated question budget: **12-15**

Use for:

- normal features,
- multiple connected decisions,
- moderate technical uncertainty,
- moderate dependencies or trade-offs.

### Hard

Estimated question budget: **18-24**

Use for:

- architecture work,
- complex systems,
- many integrations,
- security-sensitive work,
- significant operational or deployment concerns,
- high-impact or difficult-to-reverse decisions.

### Auto

The agent determines the appropriate level from actual complexity.

Evaluate:

- number of decision areas,
- dependencies,
- architecture impact,
- integrations,
- technical uncertainty,
- security/data risk,
- deployment/operational impact,
- reversibility of decisions.

Do not estimate complexity from prompt length alone.

## 2. Level Recommendation

Always recommend a level and explain why in 1-2 lines.

Example:

> ⭐ Recommended: Medium — this feature affects authentication, data flow, and deployment, but does not yet require a full architecture-level exploration.

The user makes the final choice.

## 3. Manual Level Mismatch

When the user manually selects a level that appears materially unsuitable:

1. respect the selection,
2. explain the mismatch,
3. warn about the consequence,
4. ask whether they want to keep or change it.

Example:

> You selected Easy, but I recommend Medium because several architecture and deployment decisions are interconnected.
>
> Keep Easy or switch to Medium?

Do not continue the main interview until the user resolves this choice.

Never change a manually selected level automatically.

## 4. Auto Adaptation

When using Auto, the level may change as new information appears.

Notify the user whenever this happens.

Example:

> **Auto Explore adjusted: Medium → Hard**
>
> Authentication and deployment dependencies introduced additional material decisions. Estimated budget changed from 12-15 to 18-24 questions.

Auto changes do not require approval, because the user explicitly delegated level selection.

## 5. Question Budget

Question budgets are estimates, not quotas.

- Easy: 6-9
- Medium: 12-15
- Hard: 18-24
- Auto: use the active level's range

Finish earlier when material uncertainty is sufficiently resolved.

Do not invent low-value questions just to reach the budget.

If important new uncertainty appears, the estimated session length may increase.

Tell the user when the estimate materially changes.

## 6. Interview Rounds

Ask **3 questions per round**.

The three questions should:

- share one coherent theme,
- address high-value uncertainty,
- be related without being so dependent that Q1 can invalidate Q2 and Q3 entirely.

Possible round themes:

- problem and outcome,
- users and permissions,
- feature behavior,
- UX,
- architecture,
- data flow,
- integrations,
- security,
- deployment,
- performance,
- scope and non-goals.

Do not follow a fixed category sequence.

## 7. Question Priority

Always prefer:

> Collapse the largest material uncertainty first.

Do not prioritize questions merely because they are:

- easy to ask,
- first in a checklist,
- technically interesting.

A question is valuable when its answer materially changes:

- scope,
- architecture,
- behavior,
- risk,
- implementation direction,
- PRD requirements.

## 8. Multiple-Choice Format

Every normal interview question should provide:

- A
- B
- C
- D

Default pattern:

- A-C: concrete useful alternatives
- D: Other / Custom answer

Avoid fake alternatives that differ only cosmetically.

The user may answer using:

- `1b, 2c, 3a`
- `b, c, a`
- prose,
- option plus explanation,
- fully custom answers.

The options are a UX accelerator, not a parser constraint.

## 9. Recommendations

Provide a recommendation for every question by default.

Format:

> ⭐ **Recommended: B** — <brief reason>

Keep the reason short, normally one sentence.

Recommendations should reflect:

- user goals,
- known constraints,
- previous decisions,
- reversibility,
- complexity,
- trade-offs.

If no option is genuinely dominant, say so.

Example:

> No dominant option — the right choice depends mainly on whether simplicity or extensibility matters more here.

Do not manufacture certainty merely to provide a recommendation.

## 10. Technical Questions

When a question contains technical terminology or concepts that materially affect the decision, add a short plain-language explanation before the options.

Target length: **1-3 sentences**.

Prefer:

- analogy,
- practical consequence,
- simple comparison.

Example:

> **Plain-language explanation:** WebSocket is like keeping a phone call open, while REST is more like sending a message and waiting for a reply.

Do not add beginner explanations to ordinary non-technical questions.

## 11. Progress Indicator

Show progress at the start of every round.

Preferred format:

> **Explore Medium · Round 2/±5 · Questions 4-6/12-15 · Progress ~40%**

Include:

- active Explore Level,
- current round,
- approximate expected rounds,
- question range,
- estimated question budget,
- approximate progress percentage.

Use `~` or another approximation indicator.

Do not present adaptive estimates as exact facts.

## 12. Progress Estimation

Do not calculate progress from question count alone.

Estimate progress using both:

1. questions completed,
2. material uncertainty resolved.

Examples:

> Progress ~80% — exploration is converging faster than estimated.

> Progress ~55% — a new deployment uncertainty was discovered.

The purpose of progress reporting is to reduce interview fatigue and make the remaining effort visible.

## 13. Round Recap

After each user response batch, provide a 1-3 line recap.

Summarize:

- decisions reached,
- meaningful custom answers,
- unresolved material questions,
- newly discovered blockers when relevant.

Example:

> **Round recap:** Session authentication and role-based access are agreed. Social login is out of scope. No new blocker was discovered.

Do not produce a long summary after every round.

## 14. Partial Answers

If the user answers only part of a round:

Example:

> `1b, 3c`

Then:

- record Q1 and Q3 as resolved,
- keep Q2 unresolved,
- do not re-ask Q1 or Q3,
- carry Q2 forward only if still material.

If Q2 becomes irrelevant because of the other answers, drop it.

## 15. Custom Answers

Custom answers take precedence over predefined options.

Example:

> `2: hybrid between B and C`

Record the user's actual decision.

Do not rewrite it as B or C unless the user explicitly agrees.

## 16. Contradictory Answers

If a new answer conflicts with an earlier agreed decision:

- identify the conflict,
- explain it briefly,
- ask the user which decision should prevail.

Do not silently overwrite earlier decisions.

Preserve the final chosen decision in the Decision Ledger.

## 17. Adaptive Follow-Up

After every round:

1. reassess remaining material uncertainty,
2. remove questions already answered,
3. remove questions made irrelevant,
4. prioritize the next most impactful theme,
5. update the progress estimate.

Do not precommit to all future questions at session start.

## 18. Early Completion

If all material uncertainty becomes resolved before reaching the estimated question budget:

- stop generating new interview questions,
- report that exploration converged earlier than expected,
- evaluate PRD readiness,
- proceed to End-of-Explore Control.

Example:

> Main exploration converged after 9 of the estimated 12-15 questions because all major uncertainties are resolved.

## 19. Budget Exhaustion

When the estimated main budget has been reached, evaluate PRD readiness independently.

If readiness is not sufficient:

> **Main interview budget complete · PRD readiness: Medium**
>
> Deployment remains materially unresolved.
>
> ⭐ Recommended: add one focused deployment round.

Do not claim PRD-ready solely because the budget was consumed.

## 20. End-of-Explore Control

When the main exploration reaches a natural stopping point, offer:

### A. Finish & continue to PRD
Finalize exploration and hand off to `lcs-toprd`.

### B. Add one more round
Ask 3 additional questions.

### C. Deep-dive a specific area
Let the user name or choose the area.

### D. Increase Explore Level
Examples:

- Easy → Medium
- Medium → Hard

Recommend one of these options based on current PRD readiness.

If PRD-ready is high:

> ⭐ Recommended: A — Finish & continue to PRD.

If uncertainty remains:

> ⭐ Recommended: B or C — <brief reason>.

Do not automatically finish without offering this choice.

## 21. Extended Exploration

When the user continues:

- preserve all previous decisions,
- continue numbering questions,
- do not reset progress,
- do not repeat resolved topics,
- focus on remaining uncertainty.

Example:

> **Explore Medium · Extended Round 6 · Questions 16-18 · Main interview complete + deployment deep dive**

## 22. Interview Principle

The interaction should feel like:

> an active product and architecture advisor

not:

> a long questionnaire.

Be concise, opinionated when evidence supports it, adaptive, and transparent about remaining work.

The user retains final decision authority.
