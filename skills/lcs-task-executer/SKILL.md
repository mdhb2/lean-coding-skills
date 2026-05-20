---
name: lcs-task-executer
description: Use this skill whenever the user asks to implement, execute, or continue a specific task from sliced tasks. Trigger on "Eksekusi TASK-###", "Eksekusi task-###.md", "continue TASK-###", "implement TASK-###". Always read .lcs/state.md first, check dependencies, confirm normal vs TDD mode, and update task status and .lcs/state.md when done.
---

# LCS Task Executer Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Execute a single task (`task-###.md`), update its status to `done` (or `blocked`), and support Normal or TDD development flows.

Trigger
- Activate when the user requests to "Eksekusi TASK-###", "Eksekusi task-###.md", "continue TASK-###", or "implement TASK-###".

Behavior checklist
1. Read `.lcs/state.md` first to identify the active work-item directory: `.lcs/docs/<timestamp>-<slug-work-item>/`.
2. Locate and read the target task file `.lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md`.
3. Check task dependencies listed in `Depends on`. If they are not `done` (or not met), update the task status to `blocked`, report the blocker, and stop.
4. Verify development mode:
   - If not specified, ask: "Eksekusi task ini dengan mode normal atau TDD?"
   - **Normal mode**: Implement target logic, add/update tests if relevant, run validation commands, and record execution results.
   - **TDD mode**: Write a failing test first to reproduce acceptance criteria, implement minimal code changes to pass the test, refactor, and record execution results.
5. Once task is fully executed and verified:
   - Update `Status: done` inside the `.lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md` file.
6. Update `.lcs/state.md` with:
   - `current_phase: execution`
   - `last_session_note: Executed TASK-###: <task-name> successfully`
   - `timestamp: <current-ISO-timestamp>`
7. End with Handoff pointing to the next logical step (e.g., the next sequential task or `lcs-doc-finalizer`).

Prompt templates
- Starter TDD: "Eksekusi TASK-001 dengan TDD"
- Starter Normal: "Eksekusi TASK-001 mode normal"

Handoff example:

## Handoff
Next recommended skill: lcs-task-executer
Next file to read: .lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md
Current phase: execution
Current confidence: high
Blocking questions: None
Risks to carry forward: None
Suggested next command: Eksekusi TASK-002
