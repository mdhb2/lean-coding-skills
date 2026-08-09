# Lean Coding Skills

![LCS](/assets/images/lcs-cover.png)

Collection of small, markdown-first AI skills for lean, focused coding workflows.

- **English:** this file
- **Bahasa Indonesia:** [README-ID.md](README-ID.md)

## Skills

| Skill | Purpose |
|-------|---------|
| `lcs-explore` | Interactive explore flow for brainstorming and shaping ideas |
| `lcs-toprd` | Lean, implementation-focused PRD writer |
| `lcs-prd-reviewer` | Review, harden, and security-check an existing PRD |
| `lcs-tosrs` | Transform PRD into deterministic Lean SRS and test contract |
| `lcs-task-slicer` | Split a PRD or SRS into actionable, session-sized tasks |
| `lcs-task-executor` | Execute a task plan with Chain of Truth verification |
| `lcs-doc-finalizer` | Finalize and wrap completed work into canonical docs |
| `lcs-debug` | Focused bug investigation and fix planning |
| `lcs-debug-ext` | Evidence-based debug reports and patch proposals without applying code changes |
| `lcs-codebase-doc` | Map and document existing repositories into verified onboarding docs |
| `lcs-code-review` | Review implementation against LCS artifacts |
| `lcs-improve-architecture` | Generate visual architecture improvement plans by analyzing features and proposing unified refactoring |
| `lcs-domain-modeling` | Build and sharpen the project's domain model (CONTEXT.md, ADRs) |
| `lcs-master` | Contextual router/orchestrator over all LCS skills |
| `lcs-onboarding` | Generate developer-friendly onboarding documentation |
| `lcs-prototype` | Build throwaway prototypes to validate design questions |
| `lcs-research` | Evidence-based research against primary sources |
| `lcs-self-improvement` | Analyze interaction friction and produce diagnostic recommendations |
| `lcs-chain-of-truth` | Chain of Truth meta-skill — auditable evidence protocol for all LCS skills |
| `lcs-shared` | Shared contract, folder conventions, and token optimization (internal) |
| `lcs-wayfinder` | Plan huge chunks of work with decision tickets |
| `lcs-wizard` | Generate interactive bash scripts for human-in-the-loop procedures |

## Chain of Truth

LCS uses Chain of Truth as a cross-skill protocol for auditable, evidence-backed AI workflows.

### Workflow
```text
lcs-explore (Light)
↓
lcs-toprd (Standard)
↓
lcs-prd-reviewer (Strict)
↓
lcs-tosrs (Strict)
↓
lcs-task-slicer (Strict)
↓
lcs-task-executor (Very Strict)
↓
lcs-code-review (Strict)
↓
lcs-doc-finalizer (Strict)
```
### Level Summary

| Level | Used By |
|---|---|
| Light | lcs-explore |
| Standard | lcs-toprd, lcs-onboarding, lcs-debug, lcs-self-improvement |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc, lcs-code-review |
| Very Strict | lcs-task-executor, lcs-debug-ext |
| Meta | lcs-chain-of-truth (protocol, not self-applied), lcs-shared (internal) |

### Executor Naming
- **Canonical**: `lcs-task-executor` — the only executor skill

### Artifacts & OKF Frontmatter

Every LCS artifact carries OKF v0.2 YAML frontmatter. The shared contract registers **28 artifact types** (e.g. `prd`, `srs`, `task`, `state`, `index`, `wayfinder`), each with a template under `skills/lcs-shared/templates/{artifact_type}.template.md` (27 template files; `execution_log` reuses `session-log.template.md`).

- `state` → `.lcs/state.md` (session state, written by `lcs-master`)
- `index` → navigation/control files: `.lcs/docs/docs-index.md` and `.lcs/docs/self-improvements/index.md`
- **Validators**: `validate-okf.py` (frontmatter schema) and `validate-traceability.py` / `.ps1` (SRC preservation)
- Template filenames are kebab-case (`code_review` → `code-review.template.md`).

## Skill Documentation & Usage Scenarios

### Main Flow Skills

#### `lcs-explore` — Brainstorm & Shape Ideas
Interactive question-and-answer flow to clarify intent, compare trade-offs, and assess feasibility before committing to a PRD.

**When to use:** You have a vague feature idea and need to sharpen it before planning.

**Scenario:**
> "I want to add offline mode to our mobile app. Explore what options exist."
> → LCS asks one question at a time (target users, sync strategy, storage limits), records Q&A and options in `explore.md`, then hands off to `lcs-toprd`.

#### `lcs-toprd` — Lean PRD Writer
Synthesizes exploration, debug notes, or direct requirements into a lean, implementation-focused PRD with acceptance criteria, test strategy, and Affected Areas / Files.

**When to use:** You are ready to define what to build.

**Scenario:**
> "Create a PRD for offline mode based on explore.md."
> → Produces `prd.md` with a Source Requirement Ledger (`SRC-###`), acceptance criteria, and a list of affected files, then hands off to `lcs-prd-reviewer`.

#### `lcs-prd-reviewer` — PRD Harden & Security Check
Reviews an existing PRD for ambiguous acceptance criteria, missing tests, security and performance gaps, and writes a hardened `prd-enhanced.md` while preserving every `SRC-###`.

**When to use:** You want a second, critical pass on the PRD before slicing.

**Scenario:**
> "Review prd.md dan perbaiki menjadi prd-enhanced.md agar siap di-slice."
> → Produces `prd-enhanced.md` with a Preservation Check table proving no source requirement was dropped.

#### `lcs-tosrs` — PRD → Deterministic SRS
Transforms the (enhanced) PRD into a deterministic Lean SRS: `srs.md`, `tests.md`, optional `api.md` and `db.md`, plus `traceability.md` mapping `SRC → FR/BR/VR/EC → AC → TEST`.

**When to use:** You need an AI-ready engineering contract with testable requirements.

**Scenario:**
> "PRD to SRS — buat spec deterministik dari prd-enhanced.md."
> → Generates atomic requirements (`FR-###`, `BR-###`, `VR-###`, `EC-###`), test coverage matrix, and a traceability matrix.

#### `lcs-task-slicer` — Split Work into Tasks
Splits the SRS/PRD into small, dependency-aware tracer-bullet vertical slices, classifies them `AFK`/`HITL`, and writes `task/task-###.md` files plus `task-coverage.md`.

**When to use:** You want to break a reviewed spec into session-sized execution steps.

**Scenario:**
> "Slice prd-enhanced.md menjadi task-###.md."
> → Confirms granularity with you, then writes `task-coverage.md` and one file per task with Source coverage and `blocked_by` dependencies.

#### `lcs-task-executor` — Execute a Task
Executes a single `task-###.md` in Normal or TDD mode, captures verification output verbatim, and updates task status and `.lcs/state.md`.

**When to use:** You are ready to implement a sliced task.

**Scenario:**
> "Eksekusi TASK-001."
> → Reads the task and its sources, recommends Normal vs TDD mode, implements, runs validation, and records proof of result in the Chain of Truth Report.

#### `lcs-code-review` — Review Implementation
Reviews the executed code against LCS artifacts (Explore, PRD, SRS, tasks, AC), assigns P0–P3 severities, and writes `code-review.md` with FIX entries for the executor.

**When to use:** After one or more tasks are done, before finalizing.

**Scenario:**
> "Review code hasil eksekusi terhadap artifacts."
> → Produces a structured report with file:line evidence, final status (PASS / PASS_WITH_NOTES / NEEDS_FIX / BLOCKED), and routing advice (fix → re-execute, clean → finalize).

#### `lcs-doc-finalizer` — Finalize & Archive
Consolidates completed work into `.lcs/docs/{ts}-{slug}/` (`map.md` + `doc.md`), updates `docs-index.md`, and archives source artifacts with full traceability.

**When to use:** The whole work item is done and needs canonical docs + PR description.

**Scenario:**
> "Selesaikan dokumentasi untuk offline-mode."
> → Verifies all tasks are `done`, generates `doc.md` + `map.md`, copies `code-review.md` alongside, and archives `.lcs/work-items/`.

### Supporting Skills

#### `lcs-debug` — Focused Bug Investigation
Investigates a bug through one-question-at-a-time clarifications, then writes hypotheses and an investigation plan to `debug.md` (no fixes until the root cause is clear). Uses a mandatory 6-phase disciplined loop.

**When to use:** You have a bug, failing test, error, or regression.

**Scenario:**
> "Ada bug: login selalu timeout setelah 30 detik."
> → Builds a red-capable feedback loop first, then reproduces, hypothesizes, and plans the fix — without guessing.

#### `lcs-debug-ext` — Evidence-Based Debug Report
Produces a report-only diagnosis: evidence summary, ranked falsifiable hypotheses, instrumentation suggestions, and a patch proposal — **without applying any code changes**.

**When to use:** You need a diagnosis and patch proposal for review before any edits.

**Scenario:**
> "Diagnose this flaky test but do not edit files — create a report."
> → Writes `.lcs/work-items/{ts}-{slug}-debug-ext/debug.md` with `Changes applied: None`.

#### `lcs-codebase-doc` — Map an Existing Codebase
Maps a repository into seven evidence-based docs under `.lcs/codebase/` (STACK, STRUCTURE, ARCHITECTURE, CONVENTIONS, INTEGRATIONS, TESTING, CONCERNS) plus a Chain of Truth report.

**When to use:** You need to understand or onboard into an unfamiliar repo.

**Scenario:**
> "Map this codebase — saya mau paham arsitekturnya dulu."
> → Asks you to pick a mode (Quick Update / Standard Refresh / Rebuild), scans the repo, and produces verified documentation with evidence paths.

#### `lcs-domain-modeling` — Ubiquitous Language
Builds and sharpens the project's domain model: challenges fuzzy terms, resolves overloaded vocabulary, and updates `CONTEXT.md` (plus ADRs when a decision is hard to reverse).

**When to use:** Terms are ambiguous or drifting, e.g. "account" means three different things.

**Scenario:**
> "Kita pakai istilah 'user' untuk auth dan billing — bedain dulu."
> → Proposes precise canonical terms, updates `CONTEXT.md` inline, and flags contradictions with actual code.

#### `lcs-research` — Evidence-Based Research
Investigates a question against high-trust primary sources and writes cited findings to `.lcs/work-items/{ts}-{slug}/research/<topic>.md`.

**When to use:** You need facts before a decision (API docs, library comparison, RFC review).

**Scenario:**
> "Research: compare JWT vs session cookies untuk auth di Node.js."
> → Spins up a background investigation, follows every claim to its primary source, and returns findings with exact URLs and line numbers.

#### `lcs-prototype` — Throwaway Prototype
Builds isolated throwaway code to answer a specific design question (LOGIC or UI branch), then folds the validated decision back into the real spec.

**When to use:** You want to validate an approach before committing.

**Scenario:**
> "Does this state machine logic feel right? Bikin prototype dulu."
> → Creates a throwaway prototype in `.lcs/work-items/{ts}-{slug}/prototype/`, validates the decision, and leaves a context pointer in the PRD/SRS.

#### `lcs-wayfinder` — Plan Huge Chunks of Work
Plans large, multi-session work with a navigation map and decision tickets (`DEC-###`), resolved one ticket per session until the map clears.

**When to use:** The project is too big or unclear for one session.

**Scenario:**
> "Refactor monolith jadi modular — ini proyek multi-week. Wayfinder dulu."
> → Runs a grilling session to name the destination, maps the frontier, writes `wayfinder-map.md` + decision tickets, and hands off to `lcs-toprd` when clear.

#### `lcs-wizard` — Human-in-the-Loop Scripts
Generates interactive bash scripts for manual procedures (infra setup, credentials, migrations), using `template.sh` helpers (`stage`, `open_url`, `ask_secret`, `write_env`).

**When to use:** A procedure needs a human to click through a console or enter secrets.

**Scenario:**
> "Buat wizard script untuk setup AWS credentials."
> → Maps the exact steps and variables, authors `scripts/<name>-wizard.sh`, verifies with `bash -n` + `shellcheck`, and hands off for manual execution.

#### `lcs-onboarding` — Developer Onboarding Docs
Generates a lean onboarding report (`onboarding.md`) and structural map (`onboarding-map.md`) for an existing project.

**When to use:** A new engineer needs to get up to speed on a running project.

**Scenario:**
> "Buat dokumentasi onboarding untuk repo ini."
> → Scans configuration files, extracts stack, entrypoints, setup/run/test commands, and writes the two singleton docs under `.lcs/work-items/`.

#### `lcs-self-improvement` — Friction Analysis
Analyzes conversation/session context to identify friction patterns and recommend improvements — diagnostic only, no changes applied automatically.

**When to use:** You want to improve agent behavior or skill quality over time.

**Scenario:**
> "Review apa yang salah di sesi kemarin, generate self-improvement recommendations."
> → Writes `.lcs/docs/self-improvements/{ts}-analysis.md`, tracks recommendation lifecycle in `state.json`, and deduplicates recurring items.

### Meta Skills

#### `lcs-chain-of-truth` — Auditable Evidence Protocol
A meta-skill protocol injected into all LCS skills: every artifact exposes auditable evidence (Source → Assumption → Plan → Action → Verification → Report) instead of hidden reasoning. Declares a level per skill: Light, Standard, Strict, or Very Strict.

**When to use:** Automatically active inside every LCS skill that produces a commitable or shipped artifact.

#### `lcs-master` — Contextual Router / Orchestrator
The single entry point that analyzes intent, recognizes starting situations (on-ramps), routes to the correct skill with rich contextual guidance, and enforces the shared contract on every handoff. Runs in confirmation mode (default) or autopilot mode.

**When to use:** You are unsure which LCS skill fits, or you want to start the workflow from scratch.

**Scenario:**
> "Start LCS workflow — saya mau build fitur baru."
> → Runs a precondition check, recognizes the main-flow on-ramp, recommends `lcs-explore`, and logs the routing decision.

**Scenario (on-ramp):**
> "There's a bug in production."
> → Routes to `lcs-debug` with the critical warning that Phase 1 (build a red-capable feedback loop) must complete before hypothesizing.

#### `lcs-shared` — Shared Contract (Internal)
Internal resource holding the canonical folder conventions, OKF frontmatter schema, Handoff format, artifact registry, and token-optimization rules used by every skill. Not self-applied.

**When to use:** Read it as a reference when extending LCS or debugging artifact conventions.

## Releases

| Tag | Summary |
|-----|---------|
|`v2.3`| Contract.md alignment (13 GAP fixes): 10-field Handoff format in all 8 templates; AFK/HITL enforcement in `lcs-task-executor`; artifact preservation (explore.md → prd → srs flow); Source Requirement Ledger P0/P1/P2 notation; `lcs-tosrs` added to routing chain; task-coverage.md validation; prototype.md tracking. Zero contract violations. |
|`v2.2`| OKF lifecycle alignment: wayfinder DEC tickets now use `status: active/archived` frontmatter; `artifact_type: index` registered for navigation files `docs-index.md`/`index.md` with full OKF frontmatter; validator alignment (quoted timestamps, no `type` frontmatter, date-only) plus PowerShell parity runner `validate-traceability.ps1`. |

## Install

```
npx skills add https://github.com/mdhb2/lean-coding-skills
```

Select **claudecode** when prompted. Restart Claude Code after install.

## Update

```
npx skills update -y
```

## Verify

After install, confirm skills are present:

```
Test-Path .claude\skills\lcs-explore\SKILL.md
Test-Path .claude\skills\lcs-toprd\SKILL.md
Test-Path .claude\skills\lcs-tosrs\SKILL.md
Test-Path .claude\skills\lcs-debug-ext\SKILL.md
Test-Path .claude\skills\lcs-codebase-doc\SKILL.md
```

## Troubleshooting

- Skills not showing? Confirm `.claude/skills/` exists and contains subfolders with `SKILL.md`.
- Restart Claude Code after install.
- Ensure YAML frontmatter `name` is unique and valid kebab-case.

## Contributing

Add new skill under `skills/<skill-name>/SKILL.md` with frontmatter `name` and `description`. Keep directories self-contained and markdown-only. When adding a skill, also update:
- `README.md` / `README-ID.md` skill tables
- `AGENTS.md` §9 skill inventory
- `skills/lcs-shared/contract.md` artifact registry
- `scripts/validate-skills.js` `CANONICAL_LEVELS`

When adding or renaming an artifact type, also update:
- The artifact type count in the *Artifacts & OKF Frontmatter* section of both READMEs
- The *Releases* table in both READMEs (bump tag + summary)
