---
title: lcs-master Router Design
date: 2026-07-18
context: Socratic explore session — user wants a single "router" skill (lcs-master) that actively routes to other LCS skills, with contract (SOT) enforcement.
---

# lcs-master — Router / Orchestrator Skill Design

## Purpose
One skill to rule them all. `lcs-master` is an **active router**: it analyzes user input,
recommends the next LCS skill in the Chain of Truth workflow, and either (a) asks for
confirmation or (b) runs in autopilot — chaining skills until a critical point is reached.

## Routing Modes
- **Confirmation mode (default):** after each skill completes, lcs-master stops and asks
  the user which skill to run next. User may also name a skill directly at any time.
- **Autopilot mode:** user opts in. lcs-master chains skills forward. Before autopilot
  begins, it uses `lcs-explore` to ask enough probing questions so the plan is solid.
  - Autopilot STOPS (no prompting) and writes a SOT blocker when a critical point is hit
    (see matrix). The user reviews the blocker later and resumes.

## Stop Matrix (autopilot → when to halt & write SOT)
Bound to Chain of Truth level + a structural-change guard:

| CoT Level | Example skills | Autopilot behavior |
|---|---|---|
| Light | lcs-explore | run continuously (conversational only) |
| Standard | lcs-toprd, lcs-debug, lcs-onboarding, lcs-self-improvement | run continuously (markdown artifacts, reversible) |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc | run, but BEFORE any filesystem-mutating step (finalize/archive) → stop & write SOT |
| Very Strict | lcs-task-executor, lcs-debug-ext | ALWAYS stop & write SOT before real changes |

**Cross-level guard:** if the output of the current skill changes an assumption or the
initial plan from an earlier step (e.g. lcs-tosrs reveals the PRD must change), that is
also critical → stop & write SOT regardless of level.

Threshold definition: **stop = skill has a permanent filesystem/code mutation action**;
CoT level is the proxy. Structural-change detection is the override.

## Contract (SOT) Enforcement — 3 responsibilities
1. **Path enforcer:** before handing off to a target skill, verify the skill uses the
   correct path per `lcs-shared/contract.md` (e.g. lcs-doc-finalizer → `.lcs/docs/`,
   NOT `.lcs/work-items/docs/`). Block handoff if path contract violated.
2. **Exact-name routing:** route using the folder name that EXACTLY matches the `name:`
   field in the target skill's SKILL.md frontmatter (AGENTS.md §6). No alternate spellings.
3. **Decision log (SOT):** every routing writes an audit trail entry recording
   "lcs-master called X because Y" to
   `.lcs/work-items/{ts}-lcs-master/session-log.md` (timestamped, mirrors
   lcs-self-improvement convention).

## Open items
- Exact trigger description for aggressive activation (reuse eval kit when built).
- Whether autopilot can be re-entered after a SOT blocker is resolved, or requires a
  fresh user opt-in.
