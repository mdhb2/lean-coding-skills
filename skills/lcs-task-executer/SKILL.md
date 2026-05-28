---
name: lcs-task-executer
description: Use this skill whenever the user asks to implement, execute, or continue a specific task from sliced tasks. Trigger on "Eksekusi TASK-###", "Eksekusi task-###.md", "continue TASK-###", "implement TASK-###". Always read .lcs/state.md first, check dependencies, analyze and recommend Normal vs TDD mode, confirm with user, and update task status and .lcs/state.md when done.
---

# LCS Task Executer Skill

Shared Coding Contract
- Refer to Shared Coding Workflow Contract in `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

Purpose
- Execute a single task (`task-###.md`), update its status to `done` (or `blocked`), and support Normal or TDD development flows with automatic analysis and user recommendation.

Trigger
- Activate when the user requests to "Eksekusi TASK-###", "Eksekusi task-###.md", "continue TASK-###", or "implement TASK-###".

Behavior checklist
1. Read `.lcs/state.md` first to identify the active work-item directory: `.lcs/work-items/<timestamp>-<slug-work-item>/`. 
2. Locate and read the target task file `.lcs/work-items/<timestamp>-<slug-work-item>/task/task-###.md`. 
3. Check task dependencies listed in `Depends on`. If they are not `done` (or not met), update the task status to `blocked`, report the blocker, and stop.
4. Analyze task requirements and recommend development mode:
   - **TDD Mode Criteria**: Logic-heavy, complex state transitions, algorithm/data transformations, high-risk code, or tasks explicitly requiring testing.
   - **Normal Mode Criteria**: UI/styling only, configurations, plain boilerplates, low-risk documentation, or trivial chores.
   - *Action*: Present the recommendation with brief rationale. Ask user for confirmation.
5. If **Normal mode** is chosen:
   - Implement target logic.
   - Add/update tests if relevant.
   - Run validation commands (linter, tests).
   - Record execution results.
6. If **TDD mode** is chosen (based on vertical slices / tracer bullets):
   - **Step A: Plan Interfaces & Behaviors**: Confirm public interfaces and testable behaviors first. Avoid vertical slicing of private details.
   - **Step B: Tracer Bullet (RED -> GREEN)**: Write ONE failing test checking ONE public behavior. Implement minimal code to pass.
   - **Step C: Incremental Vertical Slices**: Loop writing one failing test and minimal implementation for each remaining behavior. Do not write all tests first.
   - **Step D: Refactor**: Extract duplication, deepen modules (keep interfaces small/simple), and apply SOLID principles. *Never refactor while test is RED*.
7. Once task is fully executed and verified:
   - Update `Status: done` inside the `.lcs/work-items/<timestamp>-<slug-work-item>/task/task-###.md` file.
8. Update `.lcs/state.md` with:
   - `current_phase: execution`
   - `last_session_note: Executed TASK-###: <task-name> successfully`
   - `timestamp: <current-ISO-timestamp>`
9. End with Handoff pointing to the next logical step (e.g., the next sequential task or `lcs-doc-finalizer`).

Prompt templates
- Starter Task Execution: "Eksekusi TASK-001"
- Starter TDD explicitly: "Eksekusi TASK-001 dengan TDD"
- Starter Normal explicitly: "Eksekusi TASK-001 mode normal"

Handoff example:

## Handoff
Next recommended skill: lcs-task-executer
Next file to read: .lcs/work-items/<timestamp>-<slug-work-item>/task/task-###.md
Current phase: execution
Current confidence: high
Blocking questions: None
Risks to carry forward: None
Suggested next command: Eksekusi TASK-002
