# Task Breakdown: Enhance lcs-master — Contextual Router

**Source PRD:** `.planning/notes/lcs-master-enhance.md`
**Total Tasks:** 18 tasks across 5 phases
**Estimated Effort:** 2-3 sessions
**Status:** ✅ COMPLETED (2026-08-08)

---

## Phase 1: Precondition & Foundation (SRC-005, SRC-006)

> Setup yang harus ada sebelum routing contextual bisa jalan.

| # | Task | Files | Dependency |
|---|---|---|---|
| 1.1 | Implement Precondition Check di `lcs-master` SKILL.md — verifikasi `.lcs/`, `contract.md`, `state.md`, offer `CONTEXT.md` | `skills/lcs-master/SKILL.md` | None |
| 1.2 | Retain SOT Enforcement — pastikan 3 rules (path enforcer, exact-name, decision log) tetap ada di enhanced SKILL.md | `skills/lcs-master/SKILL.md` | None |
| 1.3 | Retain 2 Routing Modes — confirmation (default) + autopilot dengan stop matrix | `skills/lcs-master/SKILL.md` | None |

**Acceptance:** Precondition check non-blocking, SOT rules preserved, routing modes unchanged.

---

## Phase 2: On-Ramps (SRC-001, SRC-009-011)

> 4 starting situations yang harus dikenali `lcs-master`.

| # | Task | On-Ramp | Route |
|---|---|---|---|
| 2.1 | Implement Bug Reports on-ramp | Single bug → `lcs-debug` (6-phase loop) | `lcs-debug` → `lcs-toprd` if missing requirement |
| 2.2 | Implement Huge Foggy Projects on-ramp | Project >1 week / unclear requirements | `lcs-wayfinder` → `lcs-explore` → main flow |
| 2.3 | Implement Codebase Maintenance on-ramp | Code smells, architecture debt | `lcs-codebase-doc` → `lcs-domain-modeling` |
| 2.4 | Implement Mid-Workflow Situations on-ramp | Merge conflict, partial implementation | Route to appropriate standalone skill |

**Acceptance:** AC-001 (recognizes 4 on-ramps), AC-017 (escape hatches work).

---

## Phase 3: Branching Logic (SRC-003, SRC-014-015)

> Prototype dan Wayfinder detour tanpa memutus Chain Truth.

| # | Task | Detour | Trigger |
|---|---|---|---|
| 3.1 | Implement Prototype Detour | Visual validation → `lcs-prototype` → archive → return to main flow | "can I see it?", "what does it look like?" |
| 3.2 | Implement Wayfinder Detour | Multi-session planning → `lcs-wayfinder` → resolve tickets → return to main flow | Project description too large/unclear |

**Acceptance:** AC-003 (branching preserves Chain Truth), AC-013 (prototype/wayfinder return to main flow).

---

## Phase 4: Vocabulary & Guidance (SRC-002, SRC-004, SRC-012-013)

> Vocabulary foundation layer dan contextual guidance format.

| # | Task | Feature | Mechanism |
|---|---|---|---|
| 4.1 | Integrate Vocabulary Foundation — `lcs-domain-modeling` | Auto-invoke before `lcs-toprd` if `CONTEXT.md` missing/stale | Check before routing |
| 4.2 | Integrate Vocabulary Foundation — `lcs-codebase-design` | Defer or use `lcs-codebase-doc` as interim | Decision needed |
| 4.3 | Implement Contextual Guidance Format | 6-part format: recommended, reason, context, flow, alternatives, warnings | Every recommendation |
| 4.4 | Add Critical Warnings | P0 decisions, Phase 1 debug violations | Prominent display |

**Acceptance:** AC-002 (vocabulary integration), AC-004 (6-part format), AC-019 (critical warnings).

---

## Phase 5: Standalone & Integration (SRC-007-008, SRC-016-018)

> Standalone skills routing dan final integration.

| # | Task | Feature | Details |
|---|---|---|---|
| 5.1 | Document Standalone Skills routing | research, wizard, resolving-merge-conflicts | When to invoke, handoff rules |
| 5.2 | Update `lcs-master` SKILL.md with all changes | Complete rewrite | All on-ramps, branching, vocabulary, guidance |
| 5.3 | Update `routing-eval.json` | Add test cases for on-ramps, branching, standalone | 28 → 40+ queries |
| 5.4 | Update `AGENTS.md` §9 | Add `lcs-codebase-design` if created | Conditional |
| 5.5 | Run validation | `validate-okf.py` on enhanced SKILL.md | Final check |

**Acceptance:** AC-005 (standalone routing), AC-020 (follows LCS contract), all eval queries pass.

---

## Execution Order

```
Phase 1 (Foundation) → Phase 2 (On-Ramps) → Phase 3 (Branching) → Phase 4 (Vocabulary & Guidance) → Phase 5 (Integration)
```

**Parallelization:**
- Phase 2 tasks (2.1-2.4) are independent — can run in parallel
- Phase 3 tasks (3.1-3.2) are independent — can run in parallel
- Phase 4 tasks (4.1-4.4) are mostly independent (4.2 has a decision gate)
- Phase 5 tasks (5.1-5.5) are sequential (5.2 depends on 2-4, 5.3-5.5 depend on 5.2)

**Critical path:** 1.1 → 2.1-2.4 → 3.1-3.2 → 4.1-4.4 → 5.2 → 5.3-5.5

---

## Decision Gates

| Gate | Decision | Options | Recommendation |
|---|---|---|---|
| G1 | `lcs-codebase-design` | A: Create new skill, B: Use `lcs-codebase-doc`, C: Defer | B (interim) — create later if needed |
| G2 | Vocabulary Foundation mandatory? | Yes / No / Optional | Optional — suggest but don't force |
| G3 | Autopilot stop matrix changes? | Same as current / Add new stops | Same — no changes needed |
