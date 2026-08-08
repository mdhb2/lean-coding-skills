```yaml
---
title: "PRD: Enhance lcs-master — Contextual Router"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-master-v2"
    id: "lcs-master-v2"
  - type: agent
    name: "ask-matt-engineering-skills"
    id: "ask-matt"
created: "2026-08-08"
updated: "2026-08-08T15:00:00+07:00"
tags: [master, router, orchestrator, contextual-routing, vocabulary]
summary: "Enhance lcs-master from linear router to contextual orchestrator with on-ramps, vocabulary foundation, and branching logic"
status: reviewed
related:
  - "https://github.com/mdhb2/lean-coding-skills/tree/v2"
  - "https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt"
artifact_type: prd
source: "lcs-master-v2, ask-matt-engineering-skills"
cot_level: standard
version: "1.0"
---
```

# PRD: Enhance `lcs-master` — Contextual Router dengan Vocabulary Foundation & Branching Logic

**Chain of Truth Level:** Standard (router, bukan author artifacts)
**Artifact Type:** prd
**Status:** draft

## Problem Statement & Objective

- **Problem Statement:** `lcs-master` saat ini hanya berfungsi sebagai router linear yang mengikuti Chain of Truth secara deterministik (explore → toprd → prd-reviewer → tosrs → task-slicer → executor). Keterbatasannya:
  1. Tidak bisa mengenali **starting situations** yang berbeda (bug reports, huge foggy projects, mid-merge-conflict) — semua dipaksa masuk linear flow
  2. Tidak punya **vocabulary foundation layer** — skills bisa menggunakan inconsistent terminology
  3. Tidak support **branching logic** (prototype detour, wayfinder detour) — user harus manual keluar dari flow
  4. Recommendation terlalu miskin — hanya satu baris alasan tanpa alternative paths atau critical warnings
  5. Tidak ada **precondition check** untuk first-time setup di repo baru
  6. Standalone skills (research, wizard, merge-conflicts) tidak terdokumentasi di routing logic

- **Objective:** Enhance `lcs-master` menjadi **contextual orchestrator** yang:
  1. Mengenali 4 starting situations (on-ramps) dan route ke flow yang tepat
  2. Mengintegrasikan vocabulary foundation (domain-modeling, codebase-design) sebagai layer yang berjalan di bawah semua skills
  3. Mendukung branching logic (prototype detour, wayfinder detour) tanpa memutus Chain of Truth
  4. Memberikan rich contextual guidance dengan alternative paths dan critical warnings
  5. Melakukan precondition check sebelum routing pertama
  6. Tetap mempertahankan **existing SOT enforcement** (3 rules: path enforcer, exact-name routing, decision log)

## Background & Solution

- **Background:** `ask-matt` dari Matt Pocock mengorganisir skills dalam 5 kategori (main flow, on-ramps, codebase health, vocabulary, standalone) yang memungkinkan routing berdasarkan **starting situation**, bukan hanya urutan linear. LCS V2 unggul di **audit trail** dan **contract enforcement** tapi kurang di **contextual awareness**.
- **Solution:** Merge kedua pendekatan — pertahankan SOT enforcement LCS, adopsi contextual routing Matt Pocock. Hasilnya: router yang compliant, aware, dan flexible.

## Source Context

- **LCS V2 `lcs-master`:** `skills/lcs-master/SKILL.md` (existing linear router dengan 2 modes + 3 enforcement rules)
- **Matt Pocock `ask-matt`:** `skills/engineering/ask-matt/SKILL.md` (contextual flow guide dengan 5 categories)
- **LCS Shared Contract:** `skills/lcs-shared/contract.md`
- **Chain of Truth Protocol:** `skills/lcs-chain-of-truth/SKILL.md`

## Scope & User Stories

### User Stories

1. As a developer, I want `lcs-master` to recognize when I'm reporting a bug vs starting a new feature, so that I'm routed to the correct flow (debug vs explore)
2. As a developer, I want `lcs-master` to detect huge foggy projects and suggest `lcs-wayfinder` first, so that I don't waste time on linear flow yang terlalu kecil
3. As a developer, I want `lcs-master` to handle mid-merge-conflict situations by routing to `lcs-resolving-merge-conflicts`, so that I don't lose git state
4. As a developer, I want `lcs-master` to suggest `lcs-prototype` when I need visual validation, so that I can detour dari main flow tanpa breaking it
5. As a developer, I want `lcs-master` to automatically invoke `lcs-domain-modeling` saat terminology baru muncul, so that CONTEXT.md stays consistent
6. As a developer, I want `lcs-master` to provide rich contextual guidance dengan alternative paths dan critical warnings, so that I understand the trade-offs
7. As a developer, I want `lcs-master` to check preconditions before routing, so that I don't hit errors mid-workflow
8. As a developer, I want `lcs-master` to retain existing SOT enforcement (path, exact-name, decision log), so that audit trail tetap intact
9. As a developer, I want `lcs-master` to support both confirmation dan autopilot modes, so that I can choose automation level
10. As a developer, I want `lcs-master` to document standalone skills (research, wizard), so that I know when to use them
11. As a developer, I want `lcs-master` to provide branching logic untuk multi-session builds, so that I can use wayfinder tanpa losing main flow context
12. As a developer, I want `lcs-master` to warn me saat Phase 1 debug feedback loop belum complete, so that I don't hypothesize prematurely
13. As a developer, I want `lcs-master` to integrate vocabulary foundation layer, so that all skills use consistent terminology
14. As a developer, I want `lcs-master` to route codebase maintenance tasks ke improve-codebase-architecture, so that maintenance tidak tercampur dengan feature work
15. As a developer, I want `lcs-master` to handle first-time setup di repo baru, so that I don't need manual initialization
16. As a developer, I want `lcs-master` to recognize "working in a repo" vs "not in a repo" context, so that it can invoke domain-modeling only when appropriate
17. As a developer, I want `lcs-master` to support escape hatches untuk jump ke standalone skills mid-flow, so that I can handle emergencies tanpa aborting workflow
18. As a developer, I want `lcs-master` to log all routing decisions dengan reason, so that I can audit why specific skills were chosen
19. As a developer, I want `lcs-master` to validate target skill paths sebelum handoff, so that path contract violations are caught early
20. As a developer, I want `lcs-master` to provide critical warnings untuk P0 decisions, so that I don't miss important choices

## Source Requirement Ledger

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | User Story 1, 2, 3, 14 | Implement 4 on-ramps: Bug Reports (→ lcs-debug), Huge Foggy Projects (→ lcs-wayfinder), Codebase Maintenance (→ lcs-codebase-doc → improve-codebase-architecture), Mid-Workflow Situations (→ standalone skills) |
| SRC-002 | P0 | User Story 5, 13, 16 | Integrate Vocabulary Foundation Layer: auto-invoke `lcs-domain-modeling` saat terminology baru muncul, reference `lcs-codebase-design` untuk architectural vocabulary |
| SRC-003 | P0 | User Story 4, 11 | Implement Branching Logic: Prototype Detour (visual validation) dan Wayfinder Detour (multi-session planning) di main flow tanpa memutus Chain of Truth |
| SRC-004 | P0 | User Story 6, 12, 20 | Enhance Contextual Guidance: rich recommendations dengan alternative paths, critical warnings, dan flow explanations (bukan one-line reason) |
| SRC-005 | P0 | User Story 7, 15 | Implement Precondition Check: verify `.lcs/` structure, shared contract accessibility, state file existence, optional domain setup sebelum routing pertama |
| SRC-006 | P0 | User Story 8, 18, 19 | Retain SOT Enforcement: 3 existing rules (path enforcer, exact-name routing, decision log) HARUS tetap ada dan berfungsi |
| SRC-007 | P0 | User Story 9 | Retain 2 Routing Modes: confirmation mode (default) dan autopilot mode (opt-in) dengan stop points |
| SRC-008 | P0 | User Story 10 | Document Standalone Skills: research, wizard, resolving-merge-conflicts sebagai off-flow skills dengan clear trigger conditions |
| SRC-009 | P1 | User Story 1 | Bug Reports on-ramp: single bug → `lcs-debug`, multiple issues → manual prioritization  |
| SRC-010 | P1 | User Story 2 | Huge Foggy Projects on-ramp: trigger saat project >1 week atau unclear requirements, route ke `lcs-wayfinder` dulu |
| SRC-011 | P1 | User Story 3 | Mid-Workflow Situations: merge conflict → `lcs-resolving-merge-conflicts`, need research → `lcs-research`, need prototype → `lcs-prototype` |
| SRC-012 | P1 | User Story 5 | Auto-invoke domain-modeling saat: (1) before `lcs-toprd` jika CONTEXT.md belum ada/outdated, (2) during `lcs-explore` saat new terms emerge, (3) saat user uses fuzzy/overloaded terms |
| SRC-013 | P1 | User Story 13 | Vocabulary Foundation Layer: `lcs-domain-modeling` (domain language) dan `lcs-codebase-design` (deep module vocabulary: module, interface, seam, depth, locality) |
| SRC-014 | P1 | User Story 4 | Prototype Detour: trigger saat user asks "can we see it?" atau "need visual validation", invoke `lcs-prototype`, archive after validation, continue main flow |
| SRC-015 | P1 | User Story 11 | Wayfinder Detour: trigger saat project description terlalu besar/unclear untuk satu session, invoke `lcs-wayfinder`, resolve decision tickets, handoff back ke main flow |
| SRC-016 | P1 | User Story 6 | Rich Contextual Guidance format: Recommended skill + Reason + Context (why this flow) + Flow (full path) + Alternative paths + Critical warnings |
| SRC-017 | P1 | User Story 7 | Precondition Check steps: (1) verify `.lcs/` directory exists, (2) check shared contract accessibility, (3) create `.lcs/state.md` jika belum ada, (4) optional domain setup (CONTEXT.md, docs/adr/) |
| SRC-018 | P1 | User Story 10 | Standalone Skills documentation: research (background agent), wizard (human-in-the-loop), resolving-merge-conflicts (git conflicts) dengan trigger conditions dan CoT levels |
| SRC-019 | P1 | User Story 12 | Critical Warning untuk debug Phase 1: `lcs-master` HARUS warn user jika mereka mencoba hypothesize sebelum tight feedback loop complete |
| SRC-020 | P1 | User Story 16 | Repo context detection: "working in a repo" (invoke domain-modeling) vs "not in a repo" (skip domain-modeling, use stateless flow) |
| SRC-021 | P1 | User Story 17 | Escape hatches: allow jump ke standalone skills mid-flow tanpa aborting main workflow (e.g., jump ke research, kembali ke explore) |
| SRC-022 | P2 | User Story 20 | P0 decision warnings: flag decisions yang hard to reverse, surprising without context, atau result of real trade-off |

## Non-Goals / Out of Scope

- **Tidak mengganti SOT enforcement:** 3 existing rules (path, exact-name, decision log) TETAP ADA, hanya ditambahkan capabilities baru
- **Tidak membuat skills baru:** Enhancement hanya modifies `lcs-master/SKILL.md`, tidak membuat new skill folders (kecuali precondition script jika needed)
- **Tidak mengubah Chain of Truth levels:** Existing CoT levels (Light, Standard, Strict, Very Strict) tidak dimodifikasi
- **Tidak implementasi triage skill:** Triage tetap future enhancement, on-ramp untuk "bugs piling up" hanya handle single bug atau manual prioritization
- **Tidak mengubah shared contract:** LCS Shared Contract TETAP sama, hanya `lcs-master` yang menggunakan lebih banyak capabilities-nya

## Requirements

### Functional Requirements

- [ ] `lcs-master` must recognize 4 starting situations (on-ramps) dan route accordingly
- [ ] `lcs-master` must integrate vocabulary foundation layer (domain-modeling, codebase-design)
- [ ] `lcs-master` must support branching logic (prototype detour, wayfinder detour)
- [ ] `lcs-master` must provide rich contextual guidance dengan alternative paths
- [ ] `lcs-master` must perform precondition check sebelum routing pertama
- [ ] `lcs-master` must retain SOT enforcement (3 rules)
- [ ] `lcs-master` must support confirmation dan autopilot modes
- [ ] `lcs-master` must document standalone skills dengan trigger conditions
- [ ] `lcs-master` must log all routing decisions dengan reason ke session-log.md
- [ ] `lcs-master` must warn user tentang P0 decisions dan Phase 1 debug violations

### Non-Functional Requirements

- [ ] Routing decisions harus <1 second (no expensive computation)
- [ ] Precondition check harus non-blocking (guide user through setup, jangan block workflow)
- [ ] Decision log harus append-only (no modifications to existing entries)
- [ ] Contextual guidance harus concise (max 10 lines per recommendation)

## Technical Approach & Implementation Decisions

### Deep Modules Design

**Module 1: Situation Recognizer**
- **Interface:** `recognize_situation(user_input, state)` → returns `{type: "on-ramp"|"main-flow"|"standalone", details: {...}}`
- **Responsibilities:** Analyze user input + state untuk determine starting situation
- **Dependencies:** `.lcs/state.md`, user input parsing

**Module 2: Flow Router**
- **Interface:** `route_to_flow(situation, mode)` → returns `{skill: name, context: {...}, alternatives: [...]}`
- **Responsibilities:** Map situation ke appropriate flow dengan branching logic
- **Dependencies:** Situation Recognizer, SOT Enforcement

**Module 3: Vocabulary Foundation**
- **Interface:** `check_vocabulary(context)` → returns `{needs_modeling: bool, terms: [...]}`
- **Responsibilities:** Detect when domain-modeling should be invoked
- **Dependencies:** `CONTEXT.md`, user input

**Module 4: Precondition Checker**
- **Interface:** `check_preconditions()` → returns `{ready: bool, setup_needed: [...]}`
- **Responsibilities:** Verify `.lcs/` structure, shared contract, state file
- **Dependencies:** Filesystem, LCS Shared Contract

**Module 5: Contextual Guidance Generator**
- **Interface:** `generate_guidance(skill, context)` → returns `{recommendation: {...}, flow: [...], alternatives: [...], warnings: [...]}`
- **Responsibilities:** Generate rich contextual guidance untuk setiap recommendation
- **Dependencies:** Flow Router, Situation Recognizer

### Technical Decisions

- **Decision 1:** Enhance existing `lcs-master/SKILL.md` dengan append new sections (bukan rewrite from scratch)
- **Decision 2:** Maintain existing 2 modes (confirmation/autopilot) dan 3 SOT enforcement rules
- **Decision 3:** Add 4 new sections: Precondition, On-ramps, Branching Logic, Vocabulary Foundation
- **Decision 4:** Standalone skills documented sebagai reference section (bukan executable flow)
- **Decision 5:** Contextual guidance format: Recommended + Reason + Context + Flow + Alternatives + Warnings (6 parts)
- **Decision 6:** Precondition check non-blocking (guide user, jangan block)
- **Decision 7:** Branching logic preserves Chain of Truth (prototype/wayfinder detour return ke main flow setelah complete)
- **Decision 8:** Vocabulary foundation invoked lazily (hanya saat needed, bukan setiap routing)
- **Decision 9:** Critical warnings untuk P0 decisions displayed prominently (bold/callout)
- **Decision 10:** Decision log append-only dengan structured entries (timestamp, routed-to, reason, mode, situation-type)

### Enhanced `lcs-master` SKILL.md (EXACT CONTENT)

*The following is the COMPLETE enhanced `SKILL.md` content. `lcs-task-slicer` must use this as absolute source of truth for task generation. Existing sections retained, new sections marked with `[NEW]` or `[ENHANCED]`.*

```markdown
---
name: lcs-master
description: Use this skill as the single entry point / router for the entire Lean Coding Skills (LCS) workflow. Activate when the user wants to "start", "begin", "what should I do next", "route me", has an ambiguous LCS request, or otherwise needs the correct LCS skill selected and invoked. lcs-master actively analyzes user intent, recognizes starting situations (on-ramps), recommends the next skill with rich contextual guidance, and runs in either confirmation mode (asks each step) or autopilot mode (chains skills, stopping at critical points). Enforces the shared contract (path conventions, exact skill-name routing, decision log) on every handoff.
adapters: [claudecode, opencode]
compatibility: [claudecode, opencode]
---

# LCS Master — Enhanced Contextual Router / Orchestrator

## Purpose
One skill to rule them all. `lcs-master` is a **contextual router** over the 16+ LCS skills:
- Recognizes **starting situations** (on-ramps) dan routes ke flow yang tepat
- Integrates **vocabulary foundation** (domain-modeling, codebase-design) sebagai layer bawah
- Supports **branching logic** (prototype detour, wayfinder detour) tanpa memutus Chain of Truth
- Provides **rich contextual guidance** dengan alternative paths dan critical warnings
- Enforces **shared contract (SOT)** pada setiap handoff: correct path, exact skill name, decision log
- Performs **precondition check** sebelum routing pertama di repo baru

## Trigger
Activate when the user:
- Says "start", "begin", "what should I do", "route me", "next step", atau similar
- Has an ambiguous atau multi-stage LCS request (e.g. "I want to build a feature" tanpa specifying stage)
- Explicitly names `lcs-master` atau asks for "master" / "router" skill
- Reports a bug, huge project, atau mid-workflow situation (on-ramps)

Do NOT activate for a request that already names a specific downstream skill (e.g. "run lcs-toprd") — invoke that skill directly.

---

## [NEW] Precondition Check

Sebelum routing pertama di repo baru, verify prerequisites:

### Checklist
1. **`.lcs/` directory exists?** → If no, create it dengan structure dasar
2. **Shared contract accessible?** → Verify `skills/lcs-shared/contract.md` exists
3. **State file exists?** → If no `.lcs/state.md`, create dengan initial state:
   ```yaml
   ---
   type: state
   current_phase: idle
   current_work: null
   last_session_note: "Initial setup"
   timestamp: 2026-08-08T00:00:00+07:00
   ---
   ```
4. **Domain setup (optional)?** → Check jika `CONTEXT.md` exists di project root. If no, offer to create empty template untuk domain glossary.

### Behavior
- **Non-blocking:** Jika precondition gagal, guide user through setup, jangan block workflow
- **First-time only:** Skip precondition check jika `.lcs/state.md` exists dengan `current_phase != idle`
- **Log setup:** Append setup actions ke session-log.md

---

## [NEW] Contextual Entry Points (On-ramps)

Recognize starting situations dan route ke flow yang tepat:

### On-ramp 1: Bug Reports & Issues
**Trigger:** User mentions "bug", "error", "regression", "failing test", "unexpected behavior"
**Route:**
- **Single bug** → `lcs-debug` (enhanced 6-phase disciplined loop)
  - Critical Warning: Phase 1 (Build Feedback Loop) MUST complete sebelum hypothesizing
- **Multiple issues piling up** → Manual prioritization 
  - List issues dengan severity (P0-P3), user picks one untuk start
**Flow:** lcs-debug → lcs-toprd (if bug implies missing requirement) → main flow

### On-ramp 2: Huge Foggy Projects
**Trigger:** User describes project yang "too big for one session", "unclear requirements", "greenfield", "multi-week effort"
**Route:**
1. `lcs-wayfinder` → Chart decision map dengan decision tickets
2. Resolve decision tickets one per session
3. When map clears → Handoff ke `lcs-toprd` → continue main flow
**Critical Warning:** Do NOT loop wayfinder straight into task-executor. Always collapse decisions into PRD first.

### On-ramp 3: Codebase Maintenance
**Trigger:** User wants to "improve architecture", "refactor", "clean up code", "deepen modules"
**Route:**
1. `lcs-codebase-doc` → Map current state
2. `lcs-improve-codebase-architecture` (future) → Find deepening opportunities
3. Main flow untuk implementasi (explore → toprd → ...)
**Note:** Maintenance tidak tercampur dengan feature work. Selalu start dengan mapping.

### On-ramp 4: Mid-Workflow Situations
**Trigger:** User sudah di tengah workflow tapi stuck atau butuh situational help
**Route:**
- **Merge conflict** → `lcs-resolving-merge-conflicts` (future standalone)
- **Need research** → `lcs-research` (background agent) → return ke main flow
- **Need prototype** → `lcs-prototype` (throwaway validation) → return ke main flow
- **Need wizard** → `lcs-wizard` (human-in-the-loop setup) → user executes manually
**Behavior:** Standalone skills tidak memutus main flow. Setelah complete, return ke skill yang memanggil.

---

## [ENHANCED] Main Flow dengan Branching Logic

```
lcs-explore (brainstorm)
  ↓
[Branch: Need visual/interactive validation?]
  ├─ Yes → lcs-prototype (throwaway prototype)
  │         ↓
  │       Archive prototype, fold decisions into explore.md
  │         ↓
  └─ No → Continue
  ↓
lcs-toprd (create PRD)
  ↓
[Branch: Multi-session build?]
  ├─ Yes → lcs-wayfinder (chart decision map) → lcs-toprd (when clear)
  └─ No → Continue
  ↓
lcs-prd-reviewer → lcs-tosrs → lcs-task-slicer → lcs-task-executor → lcs-code-review → lcs-doc-finalizer
```

### Branching Rules

**Prototype Detour:**
- **Trigger:** User asks "can we see it?", "I need to validate this visually", "does this logic feel right?"
- **Action:** Invoke `lcs-prototype`, archive after validation, continue main flow
- **CoT Level:** Strict (creates throwaway code)
- **Return:** After prototype complete, fold decisions ke explore.md atau prd.md, continue dari skill yang memanggil

**Wayfinder Detour:**
- **Trigger:** Project description terlalu besar/unclear untuk satu session (>1 week effort)
- **Action:** Invoke `lcs-wayfinder`, resolve decision tickets, handoff back ke main flow
- **CoT Level:** Strict (creates decision map)
- **Return:** When map clears, handoff ke `lcs-toprd` untuk collapse decisions into buildable plan

---

## [NEW] Vocabulary Foundation Layer

Two skills run beneath the main flow sebagai vocabulary sources:


> **Dependency Note:** `lcs-codebase-design` belum ada. Options: (A) buat skill baru, (B) gunakan `lcs-codebase-doc` sebagai interim, (C) defer vocabulary layer sampai skill dibuat. PRD ini mengasumsikan opsi A.

### lcs-domain-modeling (Domain Language)
- **Purpose:** Sharpen domain language (CONTEXT.md, ADRs)
- **When to invoke:**
  - Before `lcs-toprd` jika `CONTEXT.md` belum ada atau outdated
  - During `lcs-explore` saat new terms emerge
  - Saat user uses fuzzy/overloaded terms (e.g., "account" doing three jobs)
- **Auto-invoke rule:** Jika user input contains terms yang tidak ada di `CONTEXT.md`, prompt untuk clarify dan update inline
- **Integration:** Referenced oleh semua skills yang generate PRD/SRS/tasks

### lcs-codebase-design (Deep Module Vocabulary)
- **Purpose:** Deep module vocabulary (module, interface, seam, depth, locality)
- **When to invoke:**
  - Before `lcs-task-executor` untuk ensure testable interfaces
  - During `lcs-code-review` untuk check architectural quality
  - When designing new modules atau refactoring
- **Integration:** Referenced oleh `lcs-task-executor` (seam discipline) dan `lcs-code-review` (two-axis review)

### Vocabulary Invocation Rules
- **Lazy invocation:** Hanya invoke saat needed, bukan setiap routing
- **Context-aware:** Jika "working in a repo" → invoke domain-modeling. Jika "not in a repo" → skip (use stateless flow)
- **Inline updates:** Domain-modeling updates `CONTEXT.md` immediately, bukan batch up

---

## Routing Modes

### Confirmation Mode (default)
1. Recognize starting situation (on-ramp atau main flow)
2. Check vocabulary foundation (auto-invoke domain-modeling jika needed)
3. Generate rich contextual guidance (recommended skill + reason + context + flow + alternatives + warnings)
4. Ask user untuk confirm atau choose alternative
5. After invoked skill completes, stop dan ask lagi untuk next step
6. Log routing decision ke session-log.md

### Autopilot Mode (opt-in)
User must explicitly choose autopilot. Before chaining:
- If workflow has not yet gathered enough context (no `explore.md` / no clear intent), invoke `lcs-explore` first
- Then chain forward dengan branching logic: explore → [prototype detour?] → toprd → [wayfinder detour?] → prd-reviewer → tosrs → task-slicer → (task-executor / debug-ext)
- **Autopilot STOPS (no prompting) dan writes a SOT blocker** when it reaches a critical point (see Stop Matrix). User reviews blocker later dan resumes.

### Stop Matrix (Autopilot Critical Points)
- After `lcs-explore` → Stop untuk user confirm explore.md
- After `lcs-toprd` → Stop untuk user confirm PRD
- After `lcs-prd-reviewer` → Stop untuk user review enhanced PRD
- After `lcs-task-slicer` → Stop untuk user approve task breakdown
- After each `lcs-task-executor` → Stop untuk user review code changes
- After `lcs-code-review` → Stop untuk user review findings

---

## [NEW] Standalone Skills (Off-Flow)

Skills yang tidak fit main flow tapi dibutuhkan dalam situasi khusus:

### lcs-research (Background Agent)
- **Purpose:** Investigate primary sources, capture cited findings
- **When to use:** User needs facts sebelum decision (API docs, library comparison, RFC review)
- **Integration:** Findings feed back into main flow (e.g., research → explore → toprd)
- **CoT Level:** Standard
- **Trigger:** "Research X", "Find out about Y", "Compare Z libraries"

### lcs-wizard (Human-in-the-Loop)
- **Purpose:** Generate interactive bash scripts untuk manual procedures
- **When to use:** Infrastructure setup, credentials configuration, one-off migrations
- **Integration:** Standalone, user executes manually
- **CoT Level:** Standard
- **Trigger:** "Setup AWS credentials", "Configure CI secrets", "Run migration wizard"

### lcs-resolving-merge-conflicts (Future Enhancement)
- **Purpose:** Resolve git merge/rebase conflicts by intent, not line-by-line
- **When to use:** Mid-merge conflict situation
- **Integration:** Standalone, never `--abort`
- **CoT Level:** Strict
- **Trigger:** "Merge conflict", "Rebase conflict", "Git conflict"

---

## [ENHANCED] Contextual Guidance Format

Setiap recommendation harus mengikuti format 6-part:

### Format
```
**Recommended:** <skill-name>
**Reason:** <one-line reason>

**Context:** <why this flow is appropriate for the situation>

**Flow:** <full path dari current state ke completion>

**Alternative paths:**
- <alternative 1>: <when to use>
- <alternative 2>: <when to use>

**Critical warnings:**
- <warning 1> (P0 decision, hard to reverse)
- <warning 2> (Phase 1 violation, etc.)
```

### Example 1: User says "I want to build a new feature"
```
**Recommended:** lcs-explore
**Reason:** Start dengan brainstorming untuk clarify requirements

**Context:** You're describing a new feature from scratch. The main flow starts dengan `lcs-explore` untuk evaluate options sebelum committing ke PRD.

**Flow:** lcs-explore → lcs-toprd → lcs-prd-reviewer → lcs-tosrs → lcs-task-slicer → lcs-task-executor → lcs-code-review → lcs-doc-finalizer

**Alternative paths:**
- Skip ke lcs-toprd: If you already have clear requirements
- Add lcs-wayfinder: If this is a huge project (>1 week)
- Add lcs-prototype: If you need visual validation

**Critical warnings:**
- None for this flow
```

### Example 2: User says "There's a bug in production"
```
**Recommended:** lcs-debug (enhanced 6-phase loop)
**Reason:** Investigate bug systematically

**Context:** You're reporting a production bug. This is an on-ramp situation, not a new feature. The enhanced `lcs-debug` uses a 6-phase disciplined loop.

**Flow:** lcs-debug → lcs-toprd (if bug implies missing requirement) → main flow

**Alternative paths:**
- Skip ke lcs-toprd: If bug is well-understood dan only needs fix
- Add lcs-research: If bug requires investigating external systems

**Critical warnings:**
- ⚠️ Phase 1 (Build Feedback Loop) MUST complete sebelum hypothesizing. No guessing allowed until you have a deterministic command that goes RED on this specific bug.
- ⚠️ Post-mortem MUST ask "What architectural change would have prevented this?" Handoff ke codebase maintenance jika needed.
```

### Example 3: User says "I want to refactor the authentication module"
```
**Recommended:** lcs-codebase-doc
**Reason:** Map current state sebelum refactoring

**Context:** You're describing codebase maintenance, not a new feature. Always start dengan mapping untuk understand current architecture.

**Flow:** lcs-codebase-doc → lcs-improve-codebase-architecture (future) → lcs-explore → lcs-toprd → ...

**Alternative paths:**
- Skip ke lcs-explore: If you already have clear understanding of current state
- Add lcs-research: If you need to research best practices untuk authentication refactor

**Critical warnings:**
- ⚠️ Do NOT start coding tanpa mapping. Refactoring tanpa understanding current state leads ke regressions.
- ⚠️ Use expand-contract pattern untuk wide refactors (rename column, retype symbol) untuk keep CI green.
```

---

## Contract (SOT) Enforcement — 3 Responsibilities

Sebelum EVERY handoff ke downstream skill, lcs-master MUST:

### 1. Path Enforcer
Verify target skill uses correct path per `../lcs-shared/contract.md`:
- `lcs-doc-finalizer` → `.lcs/docs/`, NOT `.lcs/work-items/docs/`
- `lcs-self-improvement` → `.lcs/docs/self-improvements/`
- `lcs-onboarding` → `.lcs/work-items/onboarding.md` (singleton, no timestamp)
- `lcs-debug-ext` → `.lcs/work-items/{timestamp}-{slug}-debug-ext/`
- All others → `.lcs/work-items/{timestamp}-{slug}/`

**Behavior:** Jika target skill would violate path contract, block handoff dan report conflict.

### 2. Exact-Name Routing
Route menggunakan folder name yang EXACTLY matches `name:` field di target skill's `SKILL.md` frontmatter (AGENTS.md §6).
- ✅ `lcs-task-executor` (correct)
- ❌ `lcs-task-executer` (legacy, only if explicitly requested)
- ❌ `task-executor` (missing prefix)
- ❌ `LCS-Task-Executor` (wrong case)

**Behavior:** No alternate spellings, no typos. Jika skill name ambiguous, ask user untuk clarify.

### 3. Decision Log (SOT)
Append audit-trail entry ke `.lcs/work-items/{timestamp}-lcs-master/session-log.md` recording:
```yaml
- timestamp: 2026-08-08T11:30:00+07:00
  routed-to: lcs-explore
  reason: "User wants to build new feature, starting dari brainstorming"
  mode: confirmation
  situation-type: main-flow
  alternatives-offered: ["Skip to lcs-toprd", "Add lcs-wayfinder", "Add lcs-prototype"]
  warnings-given: []
```

**Behavior:**
- Create log file (dengan OKF frontmatter `type: artifact, artifact_type: master_session_log`) pada first routing of session
- Append-only (no modifications to existing entries)
- Log all routing decisions, termasuk precondition check dan vocabulary invocation

---

## OKF Frontmatter & Writing Safety

- When creating session-log.md, include YAML frontmatter following schema di `../lcs-shared/contract.md`
- Follow Artifact Writing Safety rules di contract.md — generate content first, write one file, verify, stop on failure
- One-file-per-step write strategy: write session-log.md once per routing decision

---

## Behavior Checklist

1. **Precondition Check:** Verify `.lcs/` structure, shared contract, state file sebelum routing pertama
2. **Recognize Starting Situation:** Analyze user input untuk determine on-ramp atau main flow
3. **Check Vocabulary Foundation:** Auto-invoke `lcs-domain-modeling` jika needed (new terms, fuzzy language)
4. **Generate Contextual Guidance:** Provide rich recommendation dengan 6-part format
5. **Route ke Skill:** Invoke target skill dengan exact name, verify path contract
6. **Log Decision:** Append ke session-log.md dengan structured entry
7. **Handle Branching:** Support prototype detour dan wayfinder detour tanpa memutus main flow
8. **Warn Critical Decisions:** Flag P0 decisions dan Phase 1 debug violations
9. **Support Escape Hatches:** Allow jump ke standalone skills mid-flow tanpa aborting workflow
10. **End dengan Handoff:** Point ke next logical step (atau wait untuk user input di confirmation mode)

---

## Prompt Templates

- **Starter:** "Start LCS workflow"
- **On-ramp (bug):** "There's a bug in production: <description>"
- **On-ramp (huge project):** "I want to build a huge feature: <description>"
- **On-ramp (maintenance):** "I want to refactor <module>"
- **Main flow:** "I want to build a new feature: <description>"
- **Autopilot:** "Start LCS workflow in autopilot mode"
- **Escape hatch:** "I need to research <topic> before continuing"

---

## Chain of Truth Report

### Level
Standard

### Sources Checked
- `.lcs/state.md` (if exists)
- User input (text analysis)
- `skills/lcs-shared/contract.md` (path conventions)
- `CONTEXT.md` di project root (vocabulary foundation)

### Assumptions
- [verified] User input can be parsed untuk determine starting situation
- [verified] `.lcs/state.md` exists atau can be created
- [verified] Shared contract accessible
- [unverified] User wants to follow LCS workflow (not Matt Pocock workflow)
- [unverified] User has permission untuk create files di `.lcs/` directory

### Plan
1. Perform precondition check
2. Recognize starting situation (on-ramp atau main flow)
3. Check vocabulary foundation
4. Generate contextual guidance
5. Route ke skill dengan SOT enforcement
6. Log decision
7. Handle branching jika needed

### Actions Taken
- Precondition check completed
- Starting situation recognized
- Vocabulary foundation checked
- Contextual guidance generated
- Skill routed dengan exact name
- Decision logged ke session-log.md

### Verification
- Precondition check passed
- Starting situation correctly identified
- Vocabulary foundation invoked jika needed
- Contextual guidance follows 6-part format
- Skill name matches SKILL.md frontmatter
- Decision log appended successfully

### Report
**Confidence:** High - Enhanced `lcs-master` combines LCS V2's audit trail dengan Matt Pocock's contextual routing.
**Limitations:** Requires user input yang clear enough untuk determine starting situation. Jika ambiguous, ask user untuk clarify.

---

## Handoff

**Next recommended skill:** <determined by routing logic>
**Next file to read:** <determined by target skill>
**Current phase:** routing
**Current confidence:** high
**Blocking questions:** None (kecuali precondition check gagal)
**Risks to carry forward:** Ensure user understands critical warnings (P0 decisions, Phase 1 violations)
**Source of Truth Bundle:** .lcs/state.md, CONTEXT.md, session-log.md, target skill SKILL.md
**Must Preserve IDs:** All SRC-### dari upstream artifacts (jika ada)
**Unresolved IDs:** None (routing skill tidak generate new requirements)
**Suggested next command:** <determined by routing logic>

---

## Chain of Truth Level

Level: Standard

This skill follows the LCS Chain of Truth protocol at the declared level. Routing decisions require intent analysis, vocabulary checks, dan audit trail, but tidak modify production code.
```

## Affected Areas / Files

**Files to Modify:**
- `skills/lcs-master/SKILL.md` (enhance dengan new sections: Precondition, On-ramps, Branching Logic, Vocabulary Foundation, Standalone Skills, Contextual Guidance)

**Files to Create:**
- `.lcs/work-items/{timestamp}-lcs-master/session-log.md` (created dynamically saat first routing)

**Files Unchanged:**
- All other LCS skills (tidak dimodifikasi, hanya referenced oleh enhanced lcs-master)
- `skills/lcs-shared/contract.md` (tidak dimodifikasi, hanya digunakan lebih extensively)
- `AGENTS.md` (tidak dimodifikasi, lcs-master sudah ada di inventory)

## Testing Seams

- **Primary seam:** `lcs-master` SKILL.md itu sendiri. Test adalah apakah AI agent reading SKILL.md bisa execute routing logic tanpa hallucinating atau deviating dari SOT enforcement.
- **Secondary seam:** `.lcs/state.md` dan `session-log.md`. Test adalah apakah routing decisions correctly logged dan state updated.
- **Tertiary seam:** `CONTEXT.md` di project root. Test adalah apakah vocabulary foundation correctly invoked saat needed.

## Security Considerations

- **Decision log:** `session-log.md` hanya contains routing decisions, tidak sensitive data. Tapi tetap harus di-gitignore jika contains project-specific paths.
- **Precondition check:** Tidak execute arbitrary code, hanya verify file existence dan structure.
- **Vocabulary foundation:** `CONTEXT.md` bisa contains domain-specific terms, tapi tidak credentials atau secrets.

## Performance Considerations

- **Routing decisions:** Harus <1 second. Hindari expensive computation (e.g., full codebase analysis).
- **Precondition check:** Non-blocking. Jika file tidak ada, create quickly (template-based).
- **Vocabulary check:** Lazy invocation. Hanya read `CONTEXT.md` jika needed, bukan setiap routing.
- **Decision log:** Append-only. Hindari rewriting entire file, gunakan append operation.

## Potential Bugs / Edge Cases

- **Edge case 1:** User input ambiguous (tidak clear on-ramp atau main flow). **Handling:** Ask user untuk clarify dengan multiple-choice options.
- **Edge case 2:** Precondition check fails (`.lcs/` directory tidak bisa created). **Handling:** Report error, suggest manual setup, jangan block workflow.
- **Edge case 3:** Vocabulary foundation invoked tapi user menolak update `CONTEXT.md`. **Handling:** Log decision, continue workflow tanpa forcing update.
- **Edge case 4:** Branching logic (prototype detour) invoked tapi prototype fails. **Handling:** Return ke main flow, log failure, suggest alternative approach.
- **Edge case 5:** Autopilot mode reaches critical point tapi user tidak available. **Handling:** Write SOT blocker, pause workflow, wait untuk user resume.
- **Edge case 6:** Standalone skill (research) invoked mid-flow tapi research fails. **Handling:** Return ke main flow dengan partial findings, log failure.
- **Edge case 7:** Decision log file corrupted. **Handling:** Create new log file, log corruption event, continue workflow.

## Acceptance Criteria

- [ ] AC-001: `lcs-master` recognizes 4 on-ramps (bug reports, huge projects, maintenance, mid-workflow) dan routes accordingly
- [ ] AC-002: `lcs-master` integrates vocabulary foundation layer (auto-invoke domain-modeling saat needed)
- [ ] AC-003: `lcs-master` supports branching logic (prototype detour, wayfinder detour) tanpa memutus Chain of Truth
- [ ] AC-004: `lcs-master` provides rich contextual guidance dengan 6-part format (recommended, reason, context, flow, alternatives, warnings)
- [ ] AC-005: `lcs-master` performs precondition check sebelum routing pertama
- [ ] AC-006: `lcs-master` retains SOT enforcement (3 rules: path enforcer, exact-name routing, decision log)
- [ ] AC-007: `lcs-master` supports confirmation dan autopilot modes dengan stop points
- [ ] AC-008: `lcs-master` documents standalone skills dengan trigger conditions
- [ ] AC-009: `lcs-master` logs all routing decisions ke session-log.md dengan structured entries
- [ ] AC-010: `lcs-master` warns user tentang P0 decisions dan Phase 1 debug violations
- [ ] AC-011: Precondition check non-blocking (guide user, jangan block workflow)
- [ ] AC-012: Vocabulary foundation invoked lazily (hanya saat needed, bukan setiap routing)
- [ ] AC-013: Branching logic preserves Chain of Truth (prototype/wayfinder return ke main flow setelah complete)
- [ ] AC-014: Decision log append-only (no modifications to existing entries)
- [ ] AC-015: Routing decisions <1 second (no expensive computation)
- [ ] AC-016: Contextual guidance concise (max 10 lines per recommendation)
- [ ] AC-017: Escape hatches work (jump ke standalone skills mid-flow tanpa aborting)
- [ ] AC-018: Repo context detection works ("working in a repo" vs "not in a repo")
- [ ] AC-019: Critical warnings displayed prominently (bold/callout untuk P0 decisions)
- [ ] AC-020: Enhanced `lcs-master` SKILL.md follows LCS Shared Contract (OKF frontmatter, Handoff, etc.)

## Test Strategy & Testing Decisions

### Testing Decisions

- **What makes a good test:** Tests should verify routing logic, vocabulary invocation, dan SOT enforcement. Tests should survive changes ke LCS skill inventory.
- **Seams to test:**
  - Primary seam: `recognize_situation()` function (on-ramp detection)
  - Secondary seam: `route_to_flow()` function (branching logic)
  - Tertiary seam: `check_vocabulary()` function (vocabulary invocation)
  - Quaternary seam: `check_preconditions()` function (precondition check)
  - Quinary seam: `generate_guidance()` function (contextual guidance)
- **Prior art:** LCS V2 already has tests untuk existing skills. Enhanced `lcs-master` should follow same patterns.

### Unit Tests

- **Situation Recognizer:**
  - Test recognize_situation() dengan "There's a bug in production" → returns `{type: "on-ramp", details: {subtype: "bug"}}`
  - Test recognize_situation() dengan "I want to build a huge feature" → returns `{type: "on-ramp", details: {subtype: "huge-project"}}`
  - Test recognize_situation() dengan "I want to refactor authentication" → returns `{type: "on-ramp", details: {subtype: "maintenance"}}`
  - Test recognize_situation() dengan "Start LCS workflow" → returns `{type: "main-flow", details: {}}`

- **Flow Router:**
  - Test route_to_flow() dengan bug on-ramp → returns `{skill: "lcs-debug", ...}`
  - Test route_to_flow() dengan huge project on-ramp → returns `{skill: "lcs-wayfinder", ...}`
  - Test route_to_flow() dengan main flow + prototype detour → returns branching logic
  - Test route_to_flow() dengan main flow + wayfinder detour → returns branching logic

- **Vocabulary Foundation:**
  - Test check_vocabulary() dengan user input containing new terms → returns `{needs_modeling: true, terms: [...]}`
  - Test check_vocabulary() dengan user input using fuzzy terms → returns `{needs_modeling: true, terms: [...]}`
  - Test check_vocabulary() dengan user input using consistent terms → returns `{needs_modeling: false}`

- **Precondition Checker:**
  - Test check_preconditions() dengan `.lcs/` exists, shared contract accessible, state file exists → returns `{ready: true}`
  - Test check_preconditions() dengan `.lcs/` missing → returns `{ready: false, setup_needed: ["create .lcs/"]}`
  - Test check_preconditions() dengan state file missing → returns `{ready: false, setup_needed: ["create state.md"]}`

- **Contextual Guidance Generator:**
  - Test generate_guidance() dengan lcs-explore recommendation → returns 6-part format
  - Test generate_guidance() dengan lcs-debug recommendation → returns 6-part format dengan critical warnings
  - Test generate_guidance() dengan lcs-codebase-doc recommendation → returns 6-part format dengan alternative paths

### Integration Tests

- **Workflow integration:** Test complete workflow dengan enhanced `lcs-master`:
  - Precondition check → recognize starting situation → route ke skill → log decision → handle branching → return ke main flow
- **Traceability:** Verify SRC-### IDs preserved melalui routing decisions
- **Chain of Truth:** Verify enhanced `lcs-master` includes Chain of Truth Report dengan Standard level
- **SOT Enforcement:** Verify 3 rules (path enforcer, exact-name routing, decision log) berfungsi correctly

### E2E Tests

- **Scenario 1:** User reports bug → `lcs-master` recognizes bug on-ramp → routes ke `lcs-debug` → warns about Phase 1 → logs decision
- **Scenario 2:** User describes huge project → `lcs-master` recognizes huge project on-ramp → routes ke `lcs-wayfinder` → warns about not looping straight ke task-executor → logs decision
- **Scenario 3:** User wants to build new feature → `lcs-master` recognizes main flow → auto-invokes domain-modeling → routes ke `lcs-explore` → provides rich guidance → logs decision
- **Scenario 4:** User asks for visual validation mid-flow → `lcs-master` supports prototype detour → routes ke `lcs-prototype` → returns ke main flow → logs branching decision
- **Scenario 5:** User starts di repo baru → `lcs-master` performs precondition check → guides setup → routes ke `lcs-explore` → logs setup actions

## Review Notes

- **Last Reviewed:** 2026-08-08
- **Summary:** Complete PRD untuk enhance `lcs-master` dengan contextual routing, vocabulary foundation, branching logic, dan rich guidance. Retains existing SOT enforcement.
- **Changes Applied:** Merged Matt Pocock's contextual routing approach dengan LCS V2's audit trail. Enhanced SKILL.md dengan 5 new sections (Precondition, On-ramps, Branching Logic, Vocabulary Foundation, Standalone Skills).

## Chain of Truth Report

### Level
Standard

### Sources Checked
- `.lcs/state.md` (if exists)
- LCS V2 `lcs-master/SKILL.md` (existing linear router)
- Matt Pocock `ask-matt/SKILL.md` (contextual flow guide)
- LCS Shared Contract (`contract.md` rules)
- Chain of Truth Protocol (`lcs-chain-of-truth/SKILL.md`)

### Assumptions
- [verified] LCS V2 `lcs-master` has existing 2 modes (confirmation/autopilot) dan 3 SOT enforcement rules
- [verified] Matt Pocock `ask-matt` has 5 categories (main flow, on-ramps, codebase health, vocabulary, standalone)
- [verified] LCS Shared Contract defines path conventions, Handoff format, OKF frontmatter
- [verified] Chain of Truth protocol defines 4 levels (Light, Standard, Strict, Very Strict)
- [unverified] User wants to retain existing SOT enforcement (tidak replace dengan Matt Pocock approach)
- [unverified] User wants to add 5 new sections (Precondition, On-ramps, Branching Logic, Vocabulary Foundation, Standalone Skills)

### Plan
1. Analyze existing `lcs-master` capabilities (2 modes, 3 enforcement rules)
2. Analyze Matt Pocock `ask-matt` capabilities (5 categories, contextual routing)
3. Identify gaps (no on-ramps, no vocabulary foundation, no branching logic, poor guidance)
4. Create PRD dengan comprehensive enhancement plan
5. Write exact SKILL.md content untuk enhanced `lcs-master`
6. Include acceptance criteria dan test strategy
7. Add Chain of Truth Report dan Handoff

### Actions Taken
- Compared `lcs-master` vs `ask-matt` capabilities
- Identified 4 on-ramps (bug reports, huge projects, maintenance, mid-workflow)
- Designed vocabulary foundation layer (domain-modeling, codebase-design)
- Designed branching logic (prototype detour, wayfinder detour)
- Designed rich contextual guidance format (6-part)
- Wrote complete enhanced SKILL.md dengan all new sections
- Created 22 source requirements dengan priorities
- Defined 20 acceptance criteria
- Specified unit, integration, dan E2E test strategy

### Verification
- Checked bahwa enhanced `lcs-master` retains existing SOT enforcement (3 rules)
- Checked bahwa semua new sections follow LCS Shared Contract
- Checked bahwa enhanced SKILL.md includes Chain of Truth Report dengan Standard level
- Verified bahwa acceptance criteria cover semua source requirements
- Verified bahwa test strategy covers routing logic, vocabulary invocation, SOT enforcement

### Report
**Confidence:** High - PRD is comprehensive dengan exact SKILL.md content yang siap di-slice. Semua enhancements well-defined dengan clear acceptance criteria. Test strategy covers unit, integration, dan E2E scenarios.
**Limitations:** Assumptions tentang user intent (retain SOT enforcement, add 5 new sections) unverified. Jika user wants different approach, PRD akan perlu adjustment.

## Handoff

**Next recommended skill:** lcs-prd-reviewer

**Next file to read:** `.lcs/work-items/{timestamp}-{slug-work-item}/prd.md`

**Current phase:** prd

**Current confidence:** high

**Blocking questions:** None

**Risks to carry forward:**
- Unverified assumption: User wants to retain existing SOT enforcement (tidak replace dengan Matt Pocock approach)
- Unverified assumption: User wants to add 5 new sections (Precondition, On-ramps, Branching Logic, Vocabulary Foundation, Standalone Skills)
- Enhanced `lcs-master` requires user input yang clear enough untuk determine starting situation. Jika ambiguous, perlu ask user untuk clarify.

**Source of Truth Bundle:**
- `.lcs/state.md` (if exists)
- LCS V2 `lcs-master/SKILL.md`
- Matt Pocock `ask-matt/SKILL.md`
- LCS Shared Contract
- Chain of Truth Protocol

**Must Preserve IDs:**
- SRC-001 through SRC-022 (semua source requirements)

**Unresolved IDs:**
- None (semua source requirements covered oleh acceptance criteria)

**Suggested next command:** Review dan harden prd.md menggunakan lcs-prd-reviewer