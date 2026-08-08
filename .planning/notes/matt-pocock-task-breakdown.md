# Task Breakdown: Matt Pocock Engineering Skills Adoption

**Source PRD:** `.planning/notes/lcs-enhance-matt.md`
**Total Tasks:** 20 tasks across 4 phases
**Estimated Effort:** 3-4 sessions

---

## Phase 1: Foundation (Contract + Templates)

> Update shared infrastructure to support new artifact types and skills.

| # | Task | Files | Dependency |
|---|---|---|---|
| 1.1 | Update `lcs-shared/contract.md` — add 6 new artifact types to registry: `domain_model`, `research`, `prototype`, `wayfinder`, `wizard`, `execution_log` | `skills/lcs-shared/contract.md` | None |
| 1.2 | Create `lcs-shared/templates/domain_model.template.md` | `skills/lcs-shared/templates/` | 1.1 |
| 1.3 | Create `lcs-shared/templates/research.template.md` | `skills/lcs-shared/templates/` | 1.1 |
| 1.4 | Create `lcs-shared/templates/prototype.template.md` | `skills/lcs-shared/templates/` | 1.1 |
| 1.5 | Create `lcs-shared/templates/wayfinder.template.md` | `skills/lcs-shared/templates/` | 1.1 |
| 1.6 | Create `lcs-shared/templates/wizard.template.md` | `skills/lcs-shared/templates/` | 1.1 |
| 1.7 | Update `AGENTS.md` §9 — add 5 new skills to inventory table | `AGENTS.md` | 1.1-1.6 |

**Acceptance:** All 6 templates created, contract registry has 26 types, AGENTS.md lists 21 skills.

---

## Phase 2: New Skills — Standard CoT

> Create the 3 Standard-level skills (lower complexity, fewer constraints).

| # | Task | Source Draft | Key Integration |
|---|---|---|---|
| 2.1 | Create `skills/lcs-domain-modeling/SKILL.md` | Draft 1 | CONTEXT.md creation/update, ubiquitous language tracking, `.lcs/` storage |
| 2.2 | Create `skills/lcs-research/SKILL.md` | Draft 2 | Primary vs secondary source validation, citation format, Orca overlap note |
| 2.3 | Create `skills/lcs-wizard/SKILL.md` | Draft 5 | `template.sh` scaffolding, human-in-the-loop prompts, audit trail |

**Acceptance:** Each skill has SKILL.md with OKF frontmatter, CoT level declared, Handoff section, negative triggers in description.

---

## Phase 3: New Skills — Strict CoT + Enhancements

> Create the 2 Strict-level skills and enhance 5 existing skills.

### 3A: New Strict Skills

| # | Task | Source Draft | Key Integration |
|---|---|---|---|
| 3.1 | Create `skills/lcs-prototype/SKILL.md` | Draft 3 | Isolated execution (`{ts}-{slug}-proto/`), artifact creation, Handoff archive |
| 3.2 | Create `skills/lcs-wayfinder/SKILL.md` | Draft 4 | Local `.lcs/` map, decision tickets, pathfinder comparison note |

### 3B: Enhancements to Existing Skills

| # | Task | Skill to Modify | Change |
|---|---|---|---|
| 3.3 | Enhance `lcs-debug` — add 6-phase disciplined debugging loop | `skills/lcs-debug/SKILL.md` | Append structured loop: Reproduce → Understand → Hypothesize → Test → Fix → Verify. Upgrade CoT to Strict. |
| 3.4 | Enhance `lcs-task-executor` — add seam discipline & TDD rules | `skills/lcs-task-executor/SKILL.md` | Add TDD mode analysis, seam vocabulary, dependency injection guidance. |
| 3.5 | Enhance `lcs-code-review` — add two-axis review | `skills/lcs-code-review/SKILL.md` | Axis 1: Standards (contract, patterns). Axis 2: Spec (PRD/SRS alignment). |
| 3.6 | Enhance `lcs-task-slicer` — add blocking edges & expand-contract | `skills/lcs-task-slicer/SKILL.md` | Blocking edge detection, expand-contract pattern for wide refactors. |
| 3.7 | Enhance `lcs-toprd` — add testing seams section | `skills/lcs-toprd/SKILL.md` | New section: Testing Seams in every PRD. |

**Acceptance:** All 5 enhancements merged into existing SKILL.md files without breaking existing behavior.

---

## Phase 4: Integration & Verification

> Wire everything together, validate, and finalize.

| # | Task | Action |
|---|---|---|
| 4.1 | Update OKF schema — add new artifact types to `lcs-shared/templates/okf-schema.md` | `okf_schema.md` registry |
| 4.2 | Update `lcs-shared/evals/routing-eval.json` — add queries for 5 new skills | `routing-eval.json` |
| 4.3 | Run `validate-okf.py` on all modified/new files | Script execution |
| 4.4 | Cross-check: every new skill has correct Handoff, CoT level, negative triggers | Manual review |
| 4.5 | Update PRD status to `reviewed` after all tasks complete | `lcs-enhance-matt.md` |

**Acceptance:** All 10 skills/enhancements pass validation. Routing eval covers all 15+ skills. PRD marked reviewed.

---

## Execution Order

```
Phase 1 (Foundation) → Phase 2 (Standard Skills) → Phase 3 (Strict + Enhancements) → Phase 4 (Integration)
```

**Parallelization opportunities:**
- Phase 2 tasks (2.1, 2.2, 2.3) are independent — can run in parallel
- Phase 3A tasks (3.1, 3.2) are independent — can run in parallel
- Phase 3B tasks (3.3-3.7) are independent — can run in parallel
- Phase 4 tasks (4.1-4.4) are independent — can run in parallel

**Critical path:** 1.1 → 1.2-1.7 → 2.1-2.3 → 3.1-3.7 → 4.1-4.5
