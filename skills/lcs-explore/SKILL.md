---
name: lcs-explore
description: 'Use this skill whenever the user needs to explore, brainstorm, clarify, or shape a coding idea before a PRD or implementation. Trigger on requests mentioning explore, brainstorm, evaluate options, compare trade-offs, feasibility, or ask for recommended direction. Use this skill even when the user does not explicitly ask for a PRD but wants options or trade-off analysis. Do NOT trigger for: PRD writing (use lcs-toprd), task slicing (use lcs-task-slicer), code review (use lcs-code-review), bug investigation (use lcs-debug), or implementation (use lcs-task-executor). Explore is for ideation only, not execution.'
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS Explore

## Shared Contract

Follow `../lcs-shared/contract.md` for:

- folder conventions,
- OKF frontmatter,
- artifact writing safety,
- Source of Truth rules,
- stable IDs,
- Handoff format.

Chain of Truth level: **Light**.

## Purpose

- Clarify user intent before PRD creation.
- Explore meaningful alternatives and trade-offs.
- Resolve material uncertainty through structured interactive brainstorming.
- Record decisions, assumptions, risks, and stable source requirements.
- Persist the result as:
  `.lcs/work-items/{timestamp}-{slug-work-item}/explore.md`
- Do not create PRD, tasks, production code, or patches.

## Required References

Before starting an interactive explore session, read:

`references/interview-protocol.md`

When generating `explore.md`, read:

`../lcs-shared/templates/explore.template.md`

Do not load the artifact template during normal interview rounds unless the artifact is about to be generated.

## Workflow

1. Establish a concise work name from the user's intent.
2. If `.lcs/state.md` exists, read it before continuing.
3. Assess the topic complexity.
4. Recommend an Explore Level:
   - Easy
   - Medium
   - Hard
   - Auto
5. Let the user choose the level.
6. If the user's manual level is materially lower or higher than recommended:
   - explain the mismatch briefly,
   - warn about the likely consequence,
   - ask whether they want to keep their choice or switch.
   - Never override a manually selected level without confirmation.
7. Run the interview using `references/interview-protocol.md`.
8. Ask 3 related high-value questions per round.
9. After each round:
   - interpret the answers,
   - separate resolved decisions from unresolved questions,
   - provide a 1-3 line recap,
   - update remaining uncertainty,
   - update approximate progress.
10. Continue until:
    - the work becomes PRD-ready,
    - the selected question budget is reached,
    - or a blocker prevents responsible progress.
11. Question count does not determine PRD readiness.
12. At the end of the main exploration, let the user choose whether to:
    - finish and hand off to PRD,
    - add one round,
    - deep-dive a specific area,
    - increase the Explore Level.
13. When the user finishes exploration:
    - read `../lcs-shared/templates/explore.template.md`,
    - synthesize the complete artifact,
    - persist `explore.md`,
    - update `.lcs/state.md`,
    - hand off to `lcs-toprd`.

## Exploration Priorities

Prefer questions that collapse the largest material uncertainty first.

Typical dimensions include:

- problem and intended outcome,
- users and actors,
- must-have behavior,
- existing-system constraints,
- architecture and data flow,
- integrations,
- UX expectations,
- security and privacy,
- deployment/runtime,
- scale/performance,
- alternatives and trade-offs,
- explicit non-goals.

Do not mechanically ask every category.

Do not ask questions whose answers are already known from:

- the user's current input,
- previous rounds,
- existing Source of Truth artifacts.

## Adaptive Behavior

After every round, reassess what still matters.

If an answer makes a future question irrelevant:

- drop the irrelevant question,
- do not re-ask it,
- adapt the next round.

If the user answers only part of a round:

- preserve resolved answers,
- mark only the unanswered material items unresolved,
- do not repeat the entire round.

If the user gives a custom answer instead of selecting A-D:

- accept it,
- interpret it faithfully,
- do not force it into an existing option.

## Decision Discipline

Keep agreed decisions separate from:

- assumptions,
- recommendations,
- unresolved questions.

Every agreed decision that implies a product, behavior, interface, data, security, or operational requirement must enter the Decision Ledger as an atomic stable `SRC-###` entry.

Rules:

- one question may create multiple `SRC-###` entries,
- one round may create zero, one, or many `SRC-###` entries,
- do not invent agreement,
- preserve existing IDs,
- mark unresolved assumptions `[verified]` or `[unverified]`.

## PRD Readiness

Treat exploration as PRD-ready only when:

- intended outcome is clear,
- major constraints are known,
- meaningful options and trade-offs have been considered,
- material risks and assumptions are visible,
- unresolved questions are non-blocking or explicitly carried forward,
- agreed requirements are captured as stable `SRC-###` entries.

A completed question budget does not automatically mean PRD-ready.

If the main budget ends while important uncertainty remains:

- state the remaining uncertainty,
- report current PRD readiness,
- recommend another round or focused deep dive.

## Completion

When exploration finishes:

1. Generate `explore.md` using the canonical shared template.
2. Follow Artifact Writing Safety from `../lcs-shared/contract.md`.
3. Update `.lcs/state.md` with:
   - `current_phase: explore`
   - `current_work: {timestamp}-{slug-work-item}`
   - `last_session_note: <brief summary>`
4. End with Handoff recommending `lcs-toprd`.

If filesystem or repository access is unavailable:

- provide the complete artifact in chat,
- mark file/state operations as not performed,
- never claim a file was read or written when it was not.

## Chain of Truth

Level: **Light**

Expose:

- sources checked,
- assumptions,
- actions taken,
- verification status,
- risks.

Do not expose hidden chain-of-thought.
