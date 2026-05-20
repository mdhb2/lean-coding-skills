---
name: lcs-task-slicer
description: Use this skill whenever the user asks to split a reviewed PRD into executable tasks. Trigger on "slice prd", "break down prd", "create tasks", or similar. Produce small, dependency-aware tasks with IDs, acceptance criteria, likely files touched, and test plans. Aim for session-sized tasks (< 2 hours human time or 1 agent session). Write each task into its own file task-###.md under .lcs/docs/<timestamp>-<slug-work-item>/task/.
---

# LCS Task Slicer Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Convert `prd-enhanced.md` (or `prd.md`) into individual executable task files (`task-001.md`, `task-002.md`, etc.) under `.lcs/docs/<timestamp>-<slug-work-item>/task/`.
- Ensure tasks are small, dependency-aware, and session-friendly (<2 hours human time or one agent session).

Trigger
- Activate when user requests to "slice prd", "break down prd", "slice prd-enhanced.md", "create tasks", or similar.

Behavior checklist
- Read `.lcs/state.md` to identify the active work-item directory: `.lcs/docs/<timestamp>-<slug-work-item>/`.
- Read `prd-enhanced.md` (fallback to `prd.md` if enhanced version is missing).
- Verify PRD has clear acceptance criteria and test strategy. If missing or weak, suggest running `lcs-prd-reviewer` first.
- Create the output directory: `.lcs/docs/<timestamp>-<slug-work-item>/task/` if it does not exist.
- Slice the requirements into granular, structured, dependency-aware tasks.
- Write each task into a separate file `.lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md` where `###` is a sequential 3-digit number starting at `001`.
- Update `.lcs/state.md` with:
  - `current_phase: tasks`
  - `timestamp: <current-ISO-timestamp>`
- Output a structured task list summary.
- End with a Handoff pointing to the next logical step (e.g. `lcs-task-executor` and `task-001.md`).

Prompt templates
- Starter: "Slice prd-enhanced.md menjadi task-###.md"
- Task size rule: "Prefer tasks that take <2 hours human time or can be completed in one agent session."

Task File Structure
Each `task-###.md` must adhere to this exact structure:

```markdown
# TASK-###: <task-name>

* **Status**: pending
* **Depends on**: <TASK-### or None>
* **Priority**: <high/medium/low>
* **Scope**: <what is included in this task>
* **Files likely touched**:
  - <file-path-1>
  - <file-path-2>
* **Implementation notes**:
  - <step-by-step logic, API changes, or structures>
* **Acceptance criteria**:
  - <AC 1 (falsifiable)>
  - <AC 2 (falsifiable)>
* **Test plan**:
  - <Unit test spec or manual verification steps>

## Handoff
Next recommended skill: lcs-task-executor
Next file to read: .lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md
Current phase: tasks
Current confidence: high
Blocking questions: None
Risks to carry forward: <risks>
Suggested next command: Eksekusi task-###.md
```
