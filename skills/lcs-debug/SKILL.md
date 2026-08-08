---
name: lcs-debug
description: Use this skill whenever the user needs a focused bug investigation. Trigger on phrases about bugs, failing tests, errors, regressions, or unexpected behavior. Ask questions one at a time to identify the bug, and write the investigation results and fix plan in .lcs/work-items/{timestamp}-{slug-work-item}/debug.md before planning any fixes. Do NOT trigger for: design review, architecture decisions, new feature implementation, code review, or task execution. Use lcs-explore for design, lcs-code-review for review, lcs-task-executor for implementation.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS Debug Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Investigate bug by asking questions to the user.
- DO NOT plan or implement any fix before the bug is fully understood.
- Save investigation notes and proposed fix plan under `.lcs/work-items/{timestamp}-{slug-work-item}/debug.md` and update `.lcs/state.md`.

Trigger
- Activate on user mentioning bug, failing test, error, regression, or unexpected behavior.

## OKF Frontmatter & Writing Safety

- When creating `debug.md`, include YAML frontmatter following the schema in `../lcs-shared/contract.md`.
- Follow the Artifact Writing Safety rules in contract.md — generate content first, write one file, verify, stop on failure.


### Trigger

Activate when user requests related to this skill's purpose. See description field in YAML frontmatter for trigger phrases.

Behavior checklist
- Confirm work item name and read `state.md` if present to identify active work item folder.
- Ask one question at a time: repro steps, expected vs actual behavior, logs, env, recent commits.
- Prioritize minimal reproduction steps and clear bug understanding.
- DO NOT design or suggest fixes until the root cause is clear.
- Once understood, write proposed hypotheses and quick investigation plan to `.lcs/work-items/{timestamp}-{slug-work-item}/debug.md`.
- When the bug originates from or implies a product/behavior requirement, assign a stable `SRC-###` identifier to that requirement inside `debug.md` (use `SRC-001`, `SRC-002`, ... sequential). This ledger is the upstream source for `lcs-toprd` so the requirement is not lost when synthesized into the PRD. Preserve P0/P1/P2 priority per the Shared Coding Contract Requirement Preservation Rule.
- Update `.lcs/state.md` with current phase `debug` and path.
- End with Handoff section.

Handoff example:

## Source Requirement Ledger

If the investigation implies any product/behavior requirement, list it here so `lcs-toprd` can carry it into the PRD without loss:

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | debug finding | <exact requirement or faithful atomic paraphrase> |

## Chain of Truth Report
Level: Standard

### Sources Checked
- `.lcs/state.md` (if present)
- User-provided repro steps, logs, error messages

### Assumptions
- [unverified by default] Reported behavior is reproducible.
- [unverified by default] Recent commits listed by user are relevant.

### Plan Before Action
1. Read state.md to identify active work item.
2. Ask clarifying questions one at a time.
3. Write hypotheses and investigation plan to debug.md.
4. Update state.md.

### Actions Taken
- <Questions asked and answers recorded>
- <debug.md written at declared path>

### Verification
- Confirmed debug.md exists at `.lcs/work-items/{timestamp}-{slug-work-item}/debug.md`.
- State.md updated with `current_phase: debug`.

### Confidence
<low/medium/high> - <brief justification>



## 6-Phase Disciplined Debugging Loop (Mandatory)

- **Phase 1: Build Feedback Loop:** MUST build a tight, deterministic, agent-runnable command that goes RED on this specific bug. (Try: failing test, curl script, replay trace). NO HYPOTHESIZING ALLOWED until Phase 1 is complete.

**Hard Stop for Phase 1:**
- **Leading Words:** "tight loop", "red-capable", "deterministic"
- **Completion Criterion:** You MUST have a command that reliably goes RED (fails) on this specific bug. It must be fast (<10s), deterministic, and require no human interaction.
- **Enforcement:** Do NOT proceed to Phase 2 (Hypothesise) until this criterion is met and logged. If impossible, state the blocker and HALT.

- **Phase 2: Reproduce + Minimize:** Shrink repro to smallest scenario that still goes red. Cut one element at a time.

- **Phase 3: Hypothesise:** Generate 3-5 ranked, falsifiable hypotheses. Format: "If X is cause, changing Y will make bug disappear". Show to user before testing.

- **Phase 4: Instrument:** Change one variable at a time. Tag all debug logs with `[DEBUG-XXXX]` for easy cleanup.

- **Phase 5: Fix + Regression:** Write regression test BEFORE fix (only if correct seam exists).

- **Phase 6: Cleanup + Post-Mortem:** Remove `[DEBUG-XXXX]` logs. Ask: "What architectural change would have prevented this?" Handoff to `lcs-codebase-doc` or `lcs-toprd` if architecture needs deepening.
## Handoff
Next recommended skill: lcs-toprd
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/debug.md
Current phase: debug
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <risks>
Source of Truth Bundle: .lcs/state.md, debug.md
Must Preserve IDs: SRC-001, SRC-002, ... (from Source Requirement Ledger)
Unresolved IDs: <list or None>
Suggested next command: Buat PRD dari debug.md

## Chain of Truth Level

Level: Standard

This skill follows the LCS Chain of Truth protocol at the declared level.
