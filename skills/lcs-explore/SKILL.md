---
name: lcs-explore
description: 'Use this skill whenever the user needs to explore, brainstorm, clarify, or shape a coding idea before a PRD or implementation. Trigger on requests mentioning explore, brainstorm, evaluate options, compare trade-offs, feasibility, or ask for recommended direction. Use this skill even when the user does not explicitly ask for a PRD but wants options or trade-off analysis. Do NOT trigger for: PRD writing (use lcs-toprd), task slicing (use lcs-task-slicer), code review (use lcs-code-review), bug investigation (use lcs-debug), or implementation (use lcs-task-executor). Explore is for ideation only, not execution.'
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

LCS Explore Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Clarify user intent, brainstorm technical options, ask iterative questions until PRD readiness or blocker found.
- Persist results under .lcs/work-items/{timestamp}-{slug-work-item}/explore.md
- Do not create PRD, tasks, or code.

Trigger
- Activate when user mentions explore, brainstorm, clarify, evaluate options, compare trade-offs, feasibility, or asks for recommended direction.

## OKF Frontmatter & Writing Safety

- When creating `explore.md`, include YAML frontmatter following the schema in `../lcs-shared/contract.md`.
- Follow the Artifact Writing Safety rules in contract.md — generate content first, write one file, verify, stop on failure.


### Trigger

Activate when user requests related to this skill's purpose. See description field in YAML frontmatter for trigger phrases.

Behavior checklist
- Confirm work-name. If .lcs/state.md exists in workspace, read it.
- Ask exactly one short question at a time until either: ready for PRD or blocker discovered.
- After each user response produce a short recommendation (1-3 lines).
- Do not create PRD, tasks, or code.
- Persist file: .lcs/work-items/{timestamp}-{slug-work-item}/explore.md
- Update .lcs/state.md with:
  - current_phase: explore
  - current_work: {timestamp}-{slug-work-item}
  - last_session_note: <brief summary>
- End session with Handoff recommending lcs-toprd.

Prompt templates
- Starter: "Explore feature <short-name>: <raw intent>. Save as explore.md"
- Clarify Q: "Short question: <question>"

explore.md structure (write to file)
# Explore: <work-name>

## 1. One-line summary
<one-line summary>

## 2. Q&A History
- Q | A | Rec  <-- parser-friendly pipe triples
- Q | A | Rec

Human-friendly:
* Q: <question 1>
  * A: <answer 1>
  * Recommendation: <1-3 lines>  (mark recommended option when relevant)

## 3. Findings & Options
- Option A - Pros / Cons
- Option B - Pros / Cons

## 4. Risks & Assumptions
- risk: <short>
- assumption: <short>

## Decisions
- Decision: <text> - Owner: <name> - Timestamp: <ISO>

## Decision Ledger (upstream of PRD Source Requirement Ledger)
Every agreed decision above that implies a product/behavior requirement must be carried into the PRD as a stable `SRC-###` ID by `lcs-toprd`. List them here so nothing is lost in synthesis:

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | explore decision | <exact requirement or faithful atomic paraphrase> |

## Chain of Truth Report
### Level
Light

### Sources Checked
<List file paths read>

### Assumptions
- <label each [verified] or [unverified]>

### Actions Taken
<Summary of what was done>

### Verification
<Manual check result or "not applicable">

### Report
<1-3 sentence summary>

## Handoff
Next recommended skill: lcs-toprd
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/explore.md
Current phase: explore
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary>
Source of Truth Bundle: .lcs/state.md, explore.md
Must Preserve IDs: SRC-001, SRC-002, ... (from Decision Ledger)
Unresolved IDs: <list or None>
Suggested next command: Create PRD from explore.md

## Chain of Truth Level

Level: Light

This skill follows the LCS Chain of Truth protocol at the declared level.
