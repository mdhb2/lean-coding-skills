---
name: lcs-wayfinder
description: "Use this skill to plan huge chunks of work with a shared map and decision tickets. Trigger on 'wayfinder', 'map the codebase', 'plan this refactor', 'decision tickets', 'blocked on'. Do NOT trigger for: architecture documentation (use lcs-codebase-doc), onboarding (use lcs-onboarding), or simple tasks (use lcs-task-slicer). This is distinct from lcs-pathfinder."
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS Wayfinder Skill

Shared Coding Contract: Refer to `../lcs-shared/contract.md` for folder conventions, Handoff format, and token optimization.

**Purpose:** Plan huge chunks of work with a shared map and decision tickets resolved one at a time.

**Chain of Truth Level:** Strict

## OKF Frontmatter & Writing Safety

When creating artifacts, include YAML frontmatter following the schema in `../lcs-shared/contract.md`. Follow Artifact Writing Safety rules: generate content first, write one file, verify, stop on failure.

### Trigger

Activate when user wants to: map out a large refactor, plan multi-session work, create decision tickets, or navigate blocked work.

### Behavior Checklist

1. **Name the destination:** Run a grilling session to pin down the spec/change. What does "done" look like?

2. **Map the frontier:** Breadth-first fan-out across the codebase space. Surface open decisions — don't solve them yet, just name them.

3. **Create the map:** Write `.lcs/work-items/{ts}-{slug}/wayfinder-map.md`.

4. **Create decision tickets:** Write child files in `.lcs/work-items/{ts}-{slug}/wayfinder-tickets/`. Use YAML frontmatter with `blocked_by` to render dependencies.

5. **Resolve incrementally:** Do NOT resolve more than one ticket per session. Record the resolution, close the ticket, update the map.

6. **Handoff:** When the map clears (no open decisions), hand off to `lcs-toprd` to collapse decisions into a buildable plan.

### Output

- `.lcs/work-items/{ts}-{slug}/wayfinder-map.md` — navigation map
- `.lcs/work-items/{ts}-{slug}/wayfinder-tickets/DEC-###.md` — decision tickets

### Handoff

Next recommended skill: lcs-toprd
Next file read: .lcs/work-items/{ts}-{slug}/wayfinder-map.md
Current phase: wayfinder

### Note

This is distinct from `lcs-pathfinder` (understanding skill).
- **Wayfinder** = codebase navigation during active work.
- **Pathfinder** = one-time architecture mapping for onboarding/learning.
