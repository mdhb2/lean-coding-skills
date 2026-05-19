---
name: lcs-explore
description: Use this skill whenever the user needs to explore, brainstorm, clarify, or shape a coding idea before a PRD or implementation. Trigger on requests mentioning explore, brainstorm, evaluate options, compare trade-offs, feasibility, or ask for recommended direction. Use this skill even when the user does not explicitly ask for a PRD but wants options or trade-off analysis.
---

LCS Explore Skill

Purpose
- Clarify user intent, brainstorm technical options, ask iterative questions until PRD readiness or blocker found.
- Persist results under .lcs/docs/<yyyymmdd-HHMMSS>-<work-name>/explore.md
- Do not create PRD, tasks, or code.

Trigger
- Activate when user mentions explore, brainstorm, clarify, evaluate options, compare trade-offs, feasibility, or asks for recommended direction.

Behavior checklist
- Confirm work-name. If .lcs/state.md exists in workspace, read it.
- Ask exactly one short question at a time until either: ready for PRD or blocker discovered.
- After each user response produce a short recommendation (1–3 lines).
- Do not create PRD, tasks, or code.
- Persist file: .lcs/docs/<yyyymmdd-HHMMSS>-<work-name>/explore.md
- Update .lcs/state.md with:
  - current_phase: explore
  - current_work: <yyyymmdd-HHMMSS>-<work-name>
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
  * Recommendation: <1–3 lines>  (mark recommended option when relevant)

## 3. Findings & Options
- Option A — Pros / Cons
- Option B — Pros / Cons

## 4. Risks & Assumptions
- risk: <short>
- assumption: <short>

## Decisions
- Decision: <text> — Owner: <name> — Timestamp: <ISO>

## Handoff
Next recommended skill: lcs-toprd
Next file to read: .lcs/docs/<timestamp>-<slug-work-name>/explore.md
Current phase: explore
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary>
Suggested next command: Buat PRD dari explore.md
