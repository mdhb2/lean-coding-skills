---
name: lcs-master
description: Use this skill as the single entry point / router for the entire Lean Coding Skills (LCS) workflow. Activate when the user wants to "start", "begin", "what should I do next", "route me", has an ambiguous LCS request, or otherwise needs the correct LCS skill selected and invoked. lcs-master actively analyzes user intent, recommends the next skill in the Chain of Truth workflow, and runs in either confirmation mode (asks each step) or autopilot mode (chains skills, stopping at critical points to write a Source-of-Truth blocker). Enforces the shared contract (path conventions, exact skill-name routing, decision log) on every handoff.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
chain_of_truth_level: Standard
---

# LCS Master — Router / Orchestrator Skill

## Shared Coding Contract
- Refer to the Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, Chain of Truth level mapping, and token optimization.
- This skill is a **router** — it does not author artifacts itself. It selects and invokes the correct downstream LCS skill, enforces the contract on every handoff, and records a decision log.

## Purpose
One skill to rule them all. `lcs-master` is an **active router** over the 16 LCS skills:
- Analyzes the user's input and the current workflow state.
- Recommends the next skill in the Chain of Truth progression.
- Runs in **confirmation mode** (default) or **autopilot mode** (user opt-in).
- Enforces the shared contract (SOT) on every handoff: correct path, exact skill name, decision log.

## Trigger
Activate when the user:
- Says "start", "begin", "what should I do", "route me", "next step", or similar.
- Has an ambiguous or multi-stage LCS request (e.g. "I want to build a feature" without specifying the stage).
- Explicitly names `lcs-master` or asks for the "master" / "router" skill.
Do NOT activate for a request that already names a specific downstream skill (e.g. "run lcs-toprd") — invoke that skill directly.

## Routing Modes

### Confirmation Mode (default)
1. Analyze input + read `.lcs/state.md` if present to find the active work item and current phase.
2. Recommend the next skill (with a one-line reason).
3. Ask the user to confirm, or let them name a different skill.
4. After the invoked skill completes, stop and ask again for the next step.

### Autopilot Mode (opt-in)
User must explicitly choose autopilot. Before chaining:
- If the workflow has not yet gathered enough context (no `explore.md` / no clear intent), invoke `lcs-explore` first and ask enough probing questions to solidify the plan.
- Then chain forward: explore → toprd → prd-reviewer → tosrs → task-slicer → (task-executor / debug-ext).
- **Autopilot STOPS (no prompting) and writes a SOT blocker** when it reaches a critical point (see Stop Matrix). The user reviews the blocker later and resumes — lcs-master does not re-prompt.

## Stop Matrix (autopilot → when to halt & write SOT)
Bound to the Chain of Truth level mapping in `../lcs-shared/contract.md` plus a structural-change guard.

| CoT Level | Example skills | Autopilot behavior |
|---|---|---|
| Light | lcs-explore | run continuously (conversational only) |
| Standard | lcs-toprd, lcs-debug, lcs-onboarding, lcs-self-improvement | run continuously (markdown artifacts, reversible) |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc, lcs-code-review | run, but BEFORE any filesystem-mutating step (finalize / archive / move) → stop & write SOT |
| Very Strict | lcs-task-executor, lcs-task-executer (legacy), lcs-debug-ext | ALWAYS stop & write SOT before real changes |

**Cross-level guard:** if the output of the current skill changes an assumption or the initial plan from an earlier step (e.g. `lcs-tosrs` reveals the PRD must change), that is also critical → stop & write SOT regardless of level.

Threshold definition: **stop = the skill has a permanent filesystem / code mutation action**; CoT level is the proxy. Structural-change detection is the override.

### Writing the SOT Blocker
When autopilot stops, write a blocker file (do NOT prompt the user):
```
.lcs/work-items/{timestamp}-{slug-work-item}/master-blocker.md
```
With frontmatter `type: artifact, artifact_type: master_blocker, status: blocked` and body:
- What was reached (skill + step).
- Why it is critical (CoT level / structural change).
- The decision needed from the user.
- Suggested resume command.
Then end the session with a Handoff pointing to the blocker.

## Contract (SOT) Enforcement — 3 responsibilities
Before EVERY handoff to a downstream skill, lcs-master MUST:
1. **Path enforcer:** verify the target skill uses the correct path per `../lcs-shared/contract.md` (e.g. `lcs-doc-finalizer` → `.lcs/docs/`, NOT `.lcs/work-items/docs/`; `lcs-self-improvement` → `.lcs/docs/self-improvements/`). If the target skill would violate the path contract, block the handoff and report the conflict.
2. **Exact-name routing:** route using the folder name that EXACTLY matches the `name:` field in the target skill's `SKILL.md` frontmatter (AGENTS.md §6). No alternate spellings, no typos.
3. **Decision log (SOT):** append an audit-trail entry to
   `.lcs/work-items/{timestamp}-lcs-master/session-log.md` recording
   `timestamp | routed-to: <skill> | reason: <why> | mode: <confirmation|autopilot>`.
   Create the log file (with OKF frontmatter `type: artifact, artifact_type: master_session_log`) on first routing of the session.

## Behavior Checklist
- Read `.lcs/state.md` first when continuing work (token optimization rule).
- Identify the active work item and current Chain of Truth phase.
- Pick the next skill from the canonical workflow order, honoring the Stop Matrix.
- Enforce the 3 contract responsibilities before invoking.
- In confirmation mode: stop and ask after each skill.
- In autopilot mode: chain until a Stop Matrix condition hits, then write SOT blocker and end.
- Never author downstream artifacts itself — always delegate to the correct skill.

## Canonical Workflow Order (reference)
lcs-explore (Light) → lcs-toprd (Standard) → lcs-prd-reviewer (Strict) → lcs-tosrs (Strict) → lcs-task-slicer (Strict) → lcs-task-executor (Very Strict).
Supporting: lcs-debug / lcs-debug-ext, lcs-code-review, lcs-codebase-doc, lcs-onboarding, lcs-self-improvement, lcs-doc-finalizer.
Always consult `../lcs-shared/contract.md` for the authoritative CoT level mapping and path exceptions.

## Handoff
Must appear at bottom of every lcs-master response (per contract Handoff format):
```markdown
## Handoff

Next recommended skill:
Next file to read:
Current phase:
Current confidence:
Blocking questions:
Risks to carry forward:
Source of Truth Bundle:
Must Preserve IDs:
Unresolved IDs:
Suggested next command:
```
