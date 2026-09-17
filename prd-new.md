---
title: "PRD: Multi-Workitem State Management and lcs-new"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-toprd"
created: "2026-09-17"
updated: "2026-09-17"
artifact_type: prd
cot_level: standard
version: "1.0"
status: draft
tags: [prd, requirements, state, multi-workitem, lcs-new]
summary: "Add multi-workitem state management, work-item switching/resume, lifecycle reconciliation, and the lcs-new registration skill while preserving backward compatibility."
source: "User requirements plus repository inspection of mdhb2/lean-coding-skills master on 2026-09-17"
related: []
---

# PRD: Multi-Workitem State Management and `lcs-new`

## 1. Problem Statement & Objective

### Problem Statement

The current LCS runtime state model treats `.lcs/state.md` primarily as a pointer to one active work item through `current_work` and `current_phase`. This works for a single linear workflow, but it does not represent multiple unfinished work items at the same time.

As a result:

- starting another work item replaces the active pointer and makes older unfinished work invisible from state;
- there is no canonical registry of all unfinished work items;
- there is no canonical list/switch/resume behavior;
- several skills update `current_phase` independently, and some workflow skills do not update state at all, creating phase drift;
- finalization logic still contains a stale `active_work_item` reference even though the canonical state field is `current_work`;
- legacy projects with existing `.lcs/work-items/*` directories have no deterministic migration path into a multi-workitem registry;
- project-level/off-flow skills such as onboarding can mutate the global phase even though they are not a normal feature work item.

### Objective

Evolve LCS state from a single-work pointer into:

1. a registry of all unfinished managed work items; and
2. a backward-compatible pointer to the currently selected work item.

Add a new `lcs-new` skill whose only responsibility is to create/register a blank work item without creating `explore.md`, PRD, tasks, code, or any other work artifact.

The implementation must allow users and coding agents to:

- keep multiple unfinished work items registered simultaneously;
- list them;
- switch the selected work item;
- resume the correct workflow phase;
- finalize one work item without losing the others;
- migrate existing projects safely;
- continue using existing skills that read `current_work` and `current_phase`.

---

## 2. Background & Proposed Solution

### Current State Observed in Repository

Repository inspection of the current `master` branch identified these relevant behaviors:

- `skills/lcs-shared/templates/state.template.md` contains only `current_phase`, `current_work`, `last_session_note`, and `timestamp` as runtime state fields.
- `skills/lcs-master/SKILL.md` creates the same single-pointer state shape.
- `skills/lcs-explore/SKILL.md` writes `current_work` and `current_phase: explore`.
- `skills/lcs-debug/SKILL.md`, `skills/lcs-task-slicer/SKILL.md`, `skills/lcs-task-executor/SKILL.md`, `skills/lcs-code-review/SKILL.md`, and `skills/lcs-improve-architecture/SKILL.md` update `current_phase` directly.
- `skills/lcs-toprd/SKILL.md` currently produces the PRD but does not explicitly synchronize state phase.
- `skills/lcs-prd-reviewer/SKILL.md` produces `prd-enhanced.md` but does not explicitly synchronize state phase.
- `skills/lcs-tosrs/SKILL.md` produces SRS artifacts but does not explicitly synchronize state phase, while its Handoff currently reports `Current phase: tasks`, which conflicts with the actual SRS stage.
- `skills/lcs-doc-finalizer/SKILL.md` uses the canonical `current_work` at the start, but its stale-state guard later refers to `active_work_item`.
- `skills/lcs-onboarding/SKILL.md` is a project-level singleton workflow but updates `.lcs/state.md`; this can conflict with the invariant that `current_phase` mirrors the selected work item.
- `scripts/validate-skills.js` contains a canonical skill-level registry and expects `package.json` to expose an `npm test` script.
- the current `package.json` reports version `2.7.0` and 22 skills, but does not currently contain a `scripts.test` entry.
- `AGENTS.md`, `INSTALL.md`, README files, Chain of Truth mappings, and package metadata must be updated when adding a new skill.

### Proposed Solution

Keep these fields for compatibility:

```yaml
current_work: "20260917-090000-payment-gateway"
current_phase: prd
```

Add a registry:

```yaml
work_items:
  "20260917-080000-feature-a":
    title: "Feature A"
    path: ".lcs/work-items/20260917-080000-feature-a"
    phase: execution
    status: open
    created_at: "2026-09-17T08:00:00+07:00"
    updated_at: "2026-09-17T08:45:00+07:00"

  "20260917-090000-payment-gateway":
    title: "Payment Gateway"
    path: ".lcs/work-items/20260917-090000-payment-gateway"
    phase: prd
    status: open
    created_at: "2026-09-17T09:00:00+07:00"
    updated_at: "2026-09-17T09:20:00+07:00"
```

Semantics:

- `work_items` is the registry of unfinished managed work items.
- `current_work` is the selected work-item ID.
- `current_phase` is a compatibility mirror of `work_items[current_work].phase`.
- a completed work item is removed from `work_items` after successful `lcs-doc-finalizer` archival/finalization.
- completed items are not retained indefinitely in state because canonical history already lives under `.lcs/docs/` and `.lcs/archive/`.
- finalizing one item must never remove or overwrite other open entries.
- finalization must not automatically select a different work item.

---

## 3. Source Context

Sources inspected from the current repository:

- `package.json`
- `AGENTS.md`
- `CHANGELOG.md`
- `INSTALL.md`
- `README.md`
- `README-ID.md`
- `scripts/validate-skills.js`
- `skills/lcs-shared/contract.md`
- `skills/lcs-shared/templates/state.template.md`
- `skills/lcs-shared/scripts/validate-okf.py`
- `skills/lcs-shared/scripts/tests/test-validators.py`
- `skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md`
- `skills/lcs-master/SKILL.md`
- `skills/lcs-explore/SKILL.md`
- `skills/lcs-debug/SKILL.md`
- `skills/lcs-toprd/SKILL.md`
- `skills/lcs-prd-reviewer/SKILL.md`
- `skills/lcs-tosrs/SKILL.md`
- `skills/lcs-task-slicer/SKILL.md`
- `skills/lcs-task-executor/SKILL.md`
- `skills/lcs-code-review/SKILL.md`
- `skills/lcs-improve-architecture/SKILL.md`
- `skills/lcs-doc-finalizer/SKILL.md`
- `skills/lcs-onboarding/SKILL.md`
- `skills/lcs-chain-of-truth/SKILL.md`

Primary user requirements are from the conversation that requested:

- a new skill named `lcs-new`;
- registration of a new work item without generating content;
- state awareness of every unfinished work item;
- ability to move between multiple unfinished work items;
- preservation of those items until documentation finalization.

---

## 4. Scope & User Stories

### In Scope

1. New `lcs-new` skill.
2. Multi-workitem registry in `.lcs/state.md`.
3. Backward-compatible `current_work` and `current_phase` behavior.
4. Work-item list, select/switch, and resume behavior in `lcs-master`.
5. Legacy state/work-item reconciliation.
6. Phase synchronization across main-flow skills.
7. Correct finalization/removal behavior.
8. Off-flow isolation so singleton operations do not corrupt active work-item phase.
9. Validator support for the new state schema and invariants.
10. Validator fixtures and regression tests.
11. Skill inventory, package metadata, Chain of Truth mappings, installation docs, README docs, and changelog updates.
12. Version bump from 2.7.0 to 2.8.0.

### User Stories

1. As an LCS user, I want to register a work item before exploring it, so that I can capture future work without prematurely creating planning artifacts.
2. As an LCS user, I want multiple unfinished work items to remain visible at the same time, so that starting a new task does not hide previous work.
3. As an LCS user, I want to list open work items, so that I can see what is still in progress.
4. As an LCS user, I want to switch to a specific work item, so that downstream skills operate on the intended context.
5. As an LCS user, I want `continue`/`resume` to restore the saved workflow phase, so that I can continue from the correct stage.
6. As an LCS user, I want a blank `lcs-new` work item to be reusable by `lcs-explore`, so that the system does not create duplicate work items for the same planned work.
7. As an LCS user, I want finalization to remove only the completed item from active state, so that unrelated work remains available.
8. As a maintainer, I want legacy projects to migrate safely, so that this feature does not break existing `.lcs/state.md` and `.lcs/work-items/` data.
9. As a maintainer, I want validators to detect phase/pointer drift, so that broken state cannot silently propagate.
10. As a coding agent, I want one authoritative state-management contract, so that every skill follows the same rules.

---

## 5. Source Requirement Ledger

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | user instruction | Add a new skill named `lcs-new`. |
| SRC-002 | P0 | user instruction | `lcs-new` must register a new work item without creating explore, PRD, SRS, task, code, or documentation artifacts. |
| SRC-003 | P0 | user instruction | State must retain all unfinished managed work items, not only the most recently selected item. |
| SRC-004 | P0 | user instruction | Users must be able to move/switch between unfinished work items. |
| SRC-005 | P0 | user instruction | An unfinished work item remains registered until successful documentation finalization by `lcs-doc-finalizer`. |
| SRC-006 | P0 | agreed design | Preserve `current_work` as the selected-work pointer for backward compatibility. |
| SRC-007 | P0 | agreed design | Preserve `current_phase` as a compatibility mirror of the selected work item's phase. |
| SRC-008 | P0 | agreed design | Finalizing one work item must not delete, replace, or mutate other unfinished registry entries. |
| SRC-009 | P0 | agreed design | `lcs-doc-finalizer` must remove only the finalized work item from the open registry after archive/docs guards succeed. |
| SRC-010 | P0 | agreed design | Finalization must not automatically switch to another open work item; set the pointer to no selection instead. |
| SRC-011 | P0 | repository evidence | Replace stale `active_work_item` finalizer logic with canonical `current_work` semantics. |
| SRC-012 | P0 | agreed design | Existing/legacy state files without `work_items` must remain readable and migratable. |
| SRC-013 | P0 | agreed design | Reconciliation must discover eligible legacy unfinished work-item directories without incorrectly registering LCS support/runtime directories. |
| SRC-014 | P0 | agreed design | `*-lcs-master` routing-log directories and `*-debug-ext` report-only directories must not be imported as managed main-flow work items. |
| SRC-015 | P0 | agreed design | `lcs-explore` must reuse the selected blank `phase: new` work item when it represents the same work instead of creating a duplicate. |
| SRC-016 | P0 | agreed design | Creating a blank work item must not require a `.gitkeep` or other placeholder artifact. |
| SRC-017 | P0 | repository evidence | Every main-flow phase transition must keep `current_phase` and `work_items[current_work].phase` synchronized. |
| SRC-018 | P0 | repository evidence | Add missing state phase updates to `lcs-toprd`, `lcs-prd-reviewer`, and `lcs-tosrs`. |
| SRC-019 | P0 | repository evidence | Correct `lcs-tosrs` phase semantics so ToSRS completion is `srs`, not `tasks`; task slicing owns the `tasks` phase. |
| SRC-020 | P0 | repository evidence | Project-level/off-flow `lcs-onboarding` must not overwrite the selected managed work item's phase. |
| SRC-021 | P1 | agreed design | `lcs-master` must support list, switch/select, and resume behaviors against the registry. |
| SRC-022 | P1 | agreed design | If resume is requested with exactly one open item and no selection, it may select that single item automatically; if multiple items exist, present the candidates rather than guessing. |
| SRC-023 | P1 | agreed design | Switching must support exact work-item ID and unique title/slug matching; ambiguous matches require explicit selection. |
| SRC-024 | P1 | agreed design | Work-item IDs use `{YYYYMMDD-HHmmss}-{kebab-slug}` and registry paths use `.lcs/work-items/{id}`. |
| SRC-025 | P1 | agreed design | Registry metadata contains `title`, `path`, `phase`, `status`, `created_at`, and `updated_at`. |
| SRC-026 | P1 | agreed design | `status` is limited to `open` in this release; completed items are removed rather than retained with a completed status. |
| SRC-027 | P1 | agreed design | Validator must validate the multi-workitem structure when `work_items` exists while still accepting legacy state without it. |
| SRC-028 | P1 | repository evidence | Add validator fixtures/tests for a valid multi-workitem state, missing current pointer target, and phase mismatch. |
| SRC-029 | P1 | repository evidence | Add `lcs-new` to canonical Chain of Truth mapping as Standard. |
| SRC-030 | P1 | repository evidence | Update package/inventory/documentation from 22 to 23 skills and bump release to 2.8.0. |
| SRC-031 | P1 | repository evidence | Restore a valid `npm test` script because `scripts/validate-skills.js` explicitly checks for it while current `package.json` does not define it. |
| SRC-032 | P1 | repository evidence | Update relevant repo documentation and changelog so installation, inventory, and usage remain accurate. |
| SRC-033 | P2 | implementation preference | Keep the implementation markdown-first and avoid introducing a new runtime state-management library unless required. |
| SRC-034 | P2 | implementation preference | Prefer additive/backward-compatible edits and avoid unrelated cosmetic churn. |

---

## 6. Non-Goals / Out of Scope

1. True concurrent writes from multiple independent agents/processes to `.lcs/state.md` are not solved in this release.
   - Multi-workitem means multiple open work items, not lock-free parallel mutation of one state file.
2. No database or external state store.
3. No replacement of `current_work` with a new incompatible pointer name.
4. No permanent completed-work history inside `work_items`; completed history remains in `.lcs/docs/` and `.lcs/archive/`.
5. No new `lcs-switch` skill; switching belongs to `lcs-master`.
6. No placeholder file inside a blank work-item directory.
7. No automatic selection of a different work item after finalization.
8. No broad redesign of artifact schemas unrelated to state management.
9. No conversion of every supporting/off-flow skill into a managed work item.
10. No change to the existing docs/archive paths of `lcs-doc-finalizer`.

---

## 7. Requirements

### 7.1 Canonical State Schema

New state template:

```yaml
---
title: "LCS State"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-master"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
tags: [state]
summary: "Open work item registry and selected work item state"
status: active
related: []
artifact_type: state
source: "runtime"
cot_level: standard
version: "1.0"
type: state
current_phase: idle
current_work: null
work_items: {}
last_session_note: "Initial setup"
timestamp: "{YYYY-MM-DDTHH:MM:SS+OFFSET}"
---
```

#### State Invariants

When `work_items` exists:

1. `work_items` MUST be a mapping/object.
2. Every key MUST be a work-item ID.
3. Every entry MUST contain:
   - `title`
   - `path`
   - `phase`
   - `status`
   - `created_at`
   - `updated_at`
4. `status` MUST equal `open` in v2.8.
5. `path` MUST equal `.lcs/work-items/{work-item-id}`.
6. If `current_work` is non-null:
   - the same key MUST exist in `work_items`;
   - `work_items[current_work].status` MUST be `open`;
   - `current_phase` MUST equal `work_items[current_work].phase`.
7. If `current_work` is null, `current_phase` SHOULD be `idle`.
8. A phase transition MUST update:
   - `current_phase`;
   - `work_items[current_work].phase`;
   - `work_items[current_work].updated_at`;
   - state `timestamp`;
   - appropriate `last_session_note`.
9. Merely switching selection MUST NOT pretend work content changed; it may update state `timestamp`/`last_session_note` but does not need to change the item's `updated_at`.
10. Completed work items MUST be removed from `work_items` after successful finalization.

### 7.2 Managed Work Item Definition

A managed work item is one of:

1. an item explicitly registered by `lcs-new`; or
2. a normal timestamped work-item directory containing a recognized main-flow artifact.

Recognized reconciliation markers include at least:

- `explore.md`
- `debug.md` from normal `lcs-debug`
- `prd.md`
- `prd-enhanced.md`
- `srs.md`
- `tests.md`
- `traceability.md`
- `task-coverage.md`
- `task/`
- `code-review.md`
- `architecture-improvement.md`

Do NOT auto-import:

- `.lcs/work-items/{timestamp}-lcs-master/`
- directories ending `-debug-ext`
- flat singleton onboarding files
- `.lcs/codebase/`
- `.lcs/docs/`
- `.lcs/archive/`
- nested `prototype/`, `research/`, or wayfinder resources as independent work items
- arbitrary empty directories not already explicitly registered

### 7.3 `lcs-new` Skill

#### Trigger

Trigger on explicit intents such as:

- `lcs-new`
- "create new work item"
- "buat work item baru"
- "register a work item"
- "daftarkan pekerjaan baru"

Do not trigger when the user is asking to brainstorm, create a PRD, debug, execute tasks, or review code directly.

#### Input

A concise work-item name/title.

If no usable title is supplied, ask only for the work-item name.

#### Behavior

1. Read `.lcs/state.md` if it exists.
2. If state does not exist, create it from the canonical state template.
3. Ensure `.lcs/work-items/` exists.
4. Generate:
   - work ID: `{YYYYMMDD-HHmmss}-{kebab-slug}`
   - path: `.lcs/work-items/{work-id}`
5. Create the work-item directory.
6. Do NOT create any file inside the work-item directory.
7. Add one registry entry:

```yaml
work_items:
  "{work-id}":
    title: "{user title}"
    path: ".lcs/work-items/{work-id}"
    phase: new
    status: open
    created_at: "{ISO timestamp}"
    updated_at: "{ISO timestamp}"
```

8. Select it:

```yaml
current_work: "{work-id}"
current_phase: new
```

9. Update state timestamp and session note.
10. Stop. Do not generate `explore.md`, PRD, task files, code, docs, `.gitkeep`, or session artifacts.
11. If the state write fails after creating the empty directory, delete the directory only if it is still empty, then report failure. Do not leave a silently orphaned blank work item.
12. End with a concise handoff recommending either `lcs-explore` or `lcs-toprd` depending on user intent, but do not invoke them automatically.

#### Chain of Truth Level

Standard.

### 7.4 `lcs-master` Multi-Workitem Operations

Add canonical operations:

#### List

Intent examples:

- "list work items"
- "show open work"
- "apa saja work item yang belum selesai"

Behavior:

- reconcile first;
- show ID, title, phase, and selected marker;
- do not change selection.

#### Switch / Select

Intent examples:

- "switch to feature-a"
- "pindah ke payment gateway"
- "select 20260917-090000-payment-gateway"

Resolution order:

1. exact work-item ID;
2. exact case-insensitive title;
3. unique slug/title match;
4. if ambiguous, show candidates and require explicit ID.

On success:

```yaml
current_work: "{target-id}"
current_phase: "{work_items[target-id].phase}"
```

Do not modify other registry entries.

#### Resume / Continue

1. Reconcile registry.
2. If `current_work` points to a valid item, resume it.
3. If `current_work` is null and exactly one open item exists, select it and resume.
4. If `current_work` is null and multiple items exist, list them and require selection.
5. Route based on stored phase, not based on newest directory timestamp.

#### New Work Item Routing

If a user explicitly asks only to register/create a blank work item, route to `lcs-new`.

If a user explicitly asks to brainstorm immediately, route to `lcs-explore`; `lcs-explore` may create/register the work item itself according to the shared state contract.

### 7.5 Reconciliation / Legacy Migration

`lcs-master` MUST perform idempotent reconciliation before list/switch/resume and when encountering a legacy state.

#### Legacy State Without `work_items`

If `.lcs/state.md` has `current_work`/`current_phase` but no `work_items`:

1. initialize `work_items: {}`;
2. if `current_work` refers to an eligible existing work-item directory, register it using:
   - title inferred from slug;
   - canonical path;
   - phase from legacy `current_phase`;
   - `status: open`;
   - timestamps inferred from the work ID when possible, otherwise from current state/runtime timestamp;
3. scan other eligible legacy work-item directories and import them;
4. preserve the original selected item;
5. ensure `current_phase` matches the imported selected entry.

#### Reconciliation Rules

- idempotent: running it twice does not duplicate entries;
- non-destructive: never delete an open registry entry merely because a scan did not recognize an artifact;
- import eligible unregistered legacy directories;
- never import excluded support/report directories;
- never infer an arbitrary empty legacy directory as a managed item;
- if a registry entry points to a missing directory and phase is `new`, keep it registered because an empty `lcs-new` item may be registry-backed; downstream artifact creation can recreate the directory;
- if a non-`new` registry entry points to a missing directory, report stale state rather than silently deleting it.

### 7.6 Common Phase Synchronization Rule

Any managed-work-item skill that changes workflow phase MUST update the selected entry and compatibility mirror together.

Canonical rule:

```text
new phase = X

state.current_phase = X
state.work_items[state.current_work].phase = X
state.work_items[state.current_work].updated_at = now
state.timestamp = now
state.last_session_note = relevant summary
```

Apply to:

| Skill | Canonical phase after successful stage |
|---|---|
| `lcs-new` | `new` |
| `lcs-explore` | `explore` |
| `lcs-debug` | `debug` |
| `lcs-toprd` | `prd` |
| `lcs-prd-reviewer` | `prd_review` |
| `lcs-tosrs` | `srs` |
| `lcs-task-slicer` | `tasks` |
| `lcs-task-executor` | `execution` |
| `lcs-code-review` | `code-review` |
| `lcs-improve-architecture` | `architecture-planning` |
| `lcs-doc-finalizer` while executing | `finalization` |

### 7.7 `lcs-explore` Blank Work Reuse

When `lcs-explore` starts:

1. read/reconcile state;
2. if selected work item has `phase: new`, no primary artifact, and the user is clearly continuing that same named work, reuse the ID/path;
3. do not generate a second timestamped directory;
4. write `explore.md` into the existing path;
5. set phase to `explore` using the synchronization rule.

If the selected `new` item clearly represents different work, do not silently overwrite it. Start/register another work item or ask the user to select the intended item when ambiguity is material.

### 7.8 Other Work-Item Entry Skills

`lcs-debug` and `lcs-improve-architecture` must operate against the selected managed work item when the user is continuing it.

If they create a new normal work item themselves, they must register it before or together with their state transition using the same registry schema.

### 7.9 Planning/Specification Phase Fixes

#### `lcs-toprd`

After successful `prd.md` creation:

- phase becomes `prd`;
- synchronize registry and compatibility mirror.

#### `lcs-prd-reviewer`

After successful `prd-enhanced.md` creation:

- phase becomes `prd_review`;
- synchronize registry and compatibility mirror.

#### `lcs-tosrs`

After the required ToSRS artifact set is completed successfully:

- phase becomes `srs`;
- synchronize registry and compatibility mirror;
- change Handoff `Current phase` from `tasks` to `srs`;
- `lcs-task-slicer` remains the only owner of transition to `tasks`.

### 7.10 Off-Flow / Project-Level State Isolation

`lcs-onboarding` is a singleton project-level operation, not a normal managed work item.

Rules:

- it MUST NOT replace `current_work`;
- it MUST NOT replace `current_phase` when a managed item is selected;
- it MUST NOT add an onboarding registry entry;
- it may update `last_session_note` and state `timestamp` if desired;
- its output remains the existing singleton paths.

The same principle applies to future project-level/off-flow skills unless explicitly declared as managed work-item producers.

### 7.11 Finalization Lifecycle

`lcs-doc-finalizer` must:

1. resolve the target from canonical `current_work`;
2. verify it exists in `work_items` when the new schema is present;
3. set selected phase to `finalization` while finalization runs;
4. perform all existing docs/archive/copy/delete guards;
5. only after successful docs and archive completion:
   - remove `work_items[current_work]`;
   - set `current_work: null`;
   - set `current_phase: idle`;
   - update state timestamp and session note;
6. do not select another item automatically;
7. preserve every other `work_items` entry unchanged;
8. remove the stale `active_work_item` terminology from finalizer state logic;
9. keep existing `.lcs/docs/` and `.lcs/archive/` semantics unchanged.

If finalization fails before archive guards pass, the registry entry remains open and selected so work can be resumed safely.

### 7.12 Validator Changes

Update `skills/lcs-shared/scripts/validate-okf.py`:

- add `work_items` to recognized runtime fields;
- preserve acceptance of legacy state files without `work_items`;
- when `artifact_type: state` and `work_items` exists, validate the multi-workitem invariants;
- errors must be emitted for:
  - non-mapping `work_items`;
  - malformed entry;
  - invalid/missing selected key;
  - phase mirror mismatch;
  - invalid path;
  - unsupported work-item status;
  - invalid entry timestamps.

Add/update fixtures:

- update `skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md` to represent a valid multi-workitem state;
- create a fixture for `current_work` pointing to a missing registry key;
- create a fixture for `current_phase` not matching the selected registry entry phase;
- include the new invalid fixtures in `skills/lcs-shared/scripts/tests/test-validators.py`.

### 7.13 Skill/Package Validation

Update `scripts/validate-skills.js`:

- canonical level: `lcs-new` = `Standard`;
- include `lcs-new` in relevant cross-document consistency checks;
- continue checking skill-folder/frontmatter consistency;
- retain corruption guards.

Optionally add a small targeted multi-workitem static consistency check if it remains simple and non-brittle.

### 7.14 Package Metadata

Update `package.json`:

- version: `2.8.0`;
- description: 23 skills;
- add `lcs-new` to the `skills` array;
- `skillsConfig.totalSkills`: 23;
- keep the existing workflow string, optionally showing `lcs-new` as an optional pre-flow registration step;
- restore a valid test script:

```json
"scripts": {
  "test": "node scripts/validate-skills.js",
  "test:validators": "python3 skills/lcs-shared/scripts/tests/test-validators.py"
}
```

`npm test` must remain dependency-free and cross-platform at the Node layer.

### 7.15 Chain of Truth Mapping

Add `lcs-new` as Standard to:

- `skills/lcs-chain-of-truth/SKILL.md`
- `skills/lcs-shared/contract.md`
- `scripts/validate-skills.js`
- README level summaries
- `AGENTS.md` level/inventory references

### 7.16 Documentation / Inventory

Update:

- `README.md`
- `README-ID.md`
- `AGENTS.md`
- `INSTALL.md`
- `CHANGELOG.md`

Required documentation changes:

- 22 -> 23 skills;
- add `lcs-new` purpose and usage example;
- document multi-workitem state semantics;
- document optional flow:

```text
lcs-new (optional blank registration)
  -> lcs-explore
  -> lcs-toprd
  -> lcs-prd-reviewer
  -> lcs-tosrs
  -> lcs-task-slicer
  -> lcs-task-executor
  -> lcs-code-review
  -> lcs-doc-finalizer
```

- add release `v2.8` dated `2026-09-17`;
- document backward compatibility and no breaking changes to existing `current_work` consumers.

---

## 8. Technical Approach & Implementation Decisions

### 8.1 Architecture

Use `.lcs/state.md` as the single runtime control artifact.

Do not introduce a separate database, index file, or per-work-item metadata file in v2.8.

Reason:

- lowest migration cost;
- preserves the existing entry point every skill already reads;
- avoids changing all downstream path resolution logic;
- allows incremental adoption because legacy `current_work/current_phase` remain valid.

### 8.2 Authority Model

- Registry (`work_items`) is authoritative for the set of unfinished managed work items.
- `current_work` is authoritative for which item is selected.
- selected registry entry `phase` is authoritative for that item's saved phase.
- `current_phase` is a compatibility mirror and MUST remain equal to the selected registry phase.

### 8.3 Reconciliation Model

Use a hybrid model:

- state registry is the primary runtime index;
- filesystem scanning is a recovery/migration mechanism, not the primary source of identity;
- explicit `lcs-new` registration is required for blank work items because an empty directory has no artifact marker and Git does not preserve empty directories.

### 8.4 Empty Directory Semantics

`lcs-new` creates an empty directory at runtime because that is the user-visible work-item location.

No `.gitkeep` is created.

Durability is provided by `.lcs/state.md`, not by committing an empty directory. If the empty directory disappears after clone/checkout, the registry remains the canonical record and a downstream skill may recreate the directory before writing its first artifact.

### 8.5 No True Write Concurrency in v2.8

A single shared markdown state file still has last-writer-wins behavior if two independent agents write it simultaneously.

This is explicitly out of scope. Do not add locking or merge protocols in this feature.

### 8.6 State Mutation Discipline

Every skill that updates managed-work state must perform one coherent state update using the common invariant instead of inventing its own field names.

Avoid duplicated alternative terminology such as `active_work_item`.

---

## 9. Affected Areas / Files

| File / Area | Change Type | Evidence / Notes |
|---|---|---|
| `skills/lcs-new/SKILL.md` | create | New blank work-item registration skill. |
| `skills/lcs-shared/templates/state.template.md` | modify | Add registry and document state semantics. |
| `skills/lcs-shared/contract.md` | modify | Canonical multi-workitem contract and CoT mapping. |
| `skills/lcs-master/SKILL.md` | modify | Reconciliation, list, switch, resume, lcs-new routing, initial state. |
| `skills/lcs-explore/SKILL.md` | modify | Reuse blank work item and synchronize registry phase. |
| `skills/lcs-debug/SKILL.md` | modify | Register/reuse managed item and synchronize `debug` phase. |
| `skills/lcs-toprd/SKILL.md` | modify | Add missing `prd` state transition. |
| `skills/lcs-prd-reviewer/SKILL.md` | modify | Add missing `prd_review` state transition. |
| `skills/lcs-tosrs/SKILL.md` | modify | Add `srs` state transition and fix Handoff phase. |
| `skills/lcs-task-slicer/SKILL.md` | modify | Synchronize `tasks` phase. |
| `skills/lcs-task-executor/SKILL.md` | modify | Synchronize `execution` phase. |
| `skills/lcs-code-review/SKILL.md` | modify | Synchronize `code-review` phase. |
| `skills/lcs-improve-architecture/SKILL.md` | modify | Synchronize `architecture-planning` phase. |
| `skills/lcs-onboarding/SKILL.md` | modify | Prevent off-flow phase/pointer corruption. |
| `skills/lcs-doc-finalizer/SKILL.md` | modify | Registry removal lifecycle and `active_work_item` fix. |
| `skills/lcs-chain-of-truth/SKILL.md` | modify | Register `lcs-new` Standard level. |
| `skills/lcs-shared/scripts/validate-okf.py` | modify | Validate `work_items` schema/invariants. |
| `skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md` | modify | Multi-workitem valid fixture. |
| `skills/lcs-shared/scripts/tests/fixtures/okf/invalid-state-current-work.md` | create | Missing selected key regression fixture. |
| `skills/lcs-shared/scripts/tests/fixtures/okf/invalid-state-phase-mismatch.md` | create | Phase mirror mismatch regression fixture. |
| `skills/lcs-shared/scripts/tests/test-validators.py` | modify | Run new state fixtures. |
| `scripts/validate-skills.js` | modify | Add `lcs-new` canonical level/inventory consistency. |
| `package.json` | modify | v2.8.0, 23 skills, test scripts. |
| `AGENTS.md` | modify | Current state/inventory and multi-workitem guidance. |
| `README.md` | modify | English usage/docs. |
| `README-ID.md` | modify | Indonesian usage/docs. |
| `INSTALL.md` | modify | 23-skill installation expectations. |
| `CHANGELOG.md` | modify | v2.8 release notes. |

No other file should be edited unless implementation discovers a direct validation dependency.

---

## 10. Security Considerations

This feature does not introduce authentication, secrets, network calls, or external persistence.

Safety requirements:

- never delete a work-item directory as part of switching or reconciliation;
- only `lcs-doc-finalizer` may remove the finalized source directory, using its existing archive/docs guards;
- state migration must be non-destructive;
- a missing non-`new` work-item directory must be reported rather than silently purged;
- ambiguous work-item selection must not guess the target;
- `lcs-new` rollback may remove only the empty directory it just created when state persistence fails.

---

## 11. Performance Considerations

Expected state sizes are small.

- registry operations are O(number of open work items);
- reconciliation scans only the direct children of `.lcs/work-items/` plus marker checks;
- do not recursively scan entire repositories for work-item discovery;
- no caching layer is needed;
- no optimization should be added until state contains enough entries to demonstrate a real performance problem.

---

## 12. Potential Bugs / Edge Cases

1. **Legacy state has `current_work`, no registry**
   - migrate selected item and eligible sibling work items.
2. **Legacy current directory missing**
   - report stale state; do not invent completion.
3. **Blank `lcs-new` directory disappears after Git checkout**
   - keep registry entry; recreate directory on first artifact write.
4. **Two open work items share the same human title**
   - full IDs remain unique; title-based switching becomes ambiguous and requires ID.
5. **`current_work` is null with one open item**
   - resume may auto-select that one item.
6. **`current_work` is null with multiple items**
   - list choices; do not select newest automatically.
7. **Selected entry phase differs from `current_phase`**
   - validator error; runtime reconciliation should prefer registry phase and repair the mirror only when safe/explicitly defined by the contract.
8. **Support directory looks timestamped**
   - exclude `*-lcs-master` and `*-debug-ext` explicitly.
9. **Finalizer fails after docs generation but before archive guard completion**
   - registry remains open; do not remove entry.
10. **Finalizer succeeds while other items are open**
    - remove only finalized item; set selection null; preserve all others.
11. **Onboarding runs while a feature is selected**
    - do not mutate `current_work/current_phase`.
12. **Explore invoked with unrelated blank current work**
    - do not silently reuse; require clear same-work intent or create/select another item.
13. **Agent tries to use `active_work_item`**
    - canonical contract and finalizer must use only `current_work`.
14. **Validator scans a legacy state without registry**
    - must still pass legacy compatibility checks; migration is runtime behavior.
15. **Package validator runs `npm test`**
    - `package.json` must expose a valid `scripts.test` entry.

---

## 13. Acceptance Criteria

### State Schema

- AC-001: A newly initialized `.lcs/state.md` contains `work_items: {}` while retaining `current_work` and `current_phase`.
- AC-002: When a selected work item exists, `current_phase` equals `work_items[current_work].phase`.
- AC-003: Multiple `status: open` entries can coexist in `work_items`.
- AC-004: Every registered entry contains title, canonical path, phase, status, created timestamp, and updated timestamp.

### `lcs-new`

- AC-005: `lcs-new` creates a unique `{YYYYMMDD-HHmmss}-{slug}` work-item ID and directory.
- AC-006: `lcs-new` writes no artifact inside the new work-item directory.
- AC-007: `lcs-new` registers the new item with `phase: new` and `status: open`.
- AC-008: `lcs-new` selects the newly created item through `current_work/current_phase`.
- AC-009: No `.gitkeep`, `explore.md`, `prd.md`, session log, or other file is created by `lcs-new` inside the new work-item folder.

### Multi-Workitem Operations

- AC-010: Starting/registering a second work item does not remove the first unfinished entry.
- AC-011: `lcs-master` can list every open registered work item with ID/title/phase and selected status.
- AC-012: Switching to a target updates only selection fields and does not alter unrelated work-item entries.
- AC-013: Resume uses the selected item's stored phase rather than choosing the newest directory.
- AC-014: Ambiguous title matching does not auto-select a work item.

### Reconciliation / Compatibility

- AC-015: A legacy state without `work_items` can still be read and migrated.
- AC-016: Eligible legacy work-item directories are imported without duplication.
- AC-017: `*-lcs-master` and `*-debug-ext` directories are not imported as managed work items.
- AC-018: Reconciliation is idempotent.
- AC-019: Existing skills that still resolve the active path through `current_work` remain compatible.

### Phase Lifecycle

- AC-020: `lcs-explore` transitions the selected entry to `explore` and mirrors `current_phase`.
- AC-021: `lcs-debug` transitions the selected entry to `debug` and mirrors `current_phase`.
- AC-022: `lcs-toprd` transitions the selected entry to `prd` after successful PRD creation.
- AC-023: `lcs-prd-reviewer` transitions it to `prd_review` after successful enhanced PRD creation.
- AC-024: `lcs-tosrs` transitions it to `srs`, and its Handoff reports `Current phase: srs`.
- AC-025: `lcs-task-slicer` transitions it to `tasks`.
- AC-026: `lcs-task-executor` transitions it to `execution`.
- AC-027: `lcs-code-review` transitions it to `code-review`.
- AC-028: `lcs-improve-architecture` transitions it to `architecture-planning`.
- AC-029: `lcs-onboarding` does not alter the selected managed work item's pointer or phase.

### Finalization

- AC-030: `lcs-doc-finalizer` uses `current_work`, not `active_work_item`.
- AC-031: During finalization, the selected work item's phase becomes `finalization`.
- AC-032: A successful finalization removes only the finalized registry entry.
- AC-033: After successful finalization, `current_work` is null and `current_phase` is `idle`.
- AC-034: Other unfinished work-item registry entries remain unchanged.
- AC-035: Finalization does not auto-select another item.
- AC-036: Failed finalization keeps the item registered/open for safe resume.

### Validation / Repository Integrity

- AC-037: `validate-okf.py` accepts a valid multi-workitem state.
- AC-038: `validate-okf.py` rejects a state whose `current_work` does not exist in `work_items`.
- AC-039: `validate-okf.py` rejects a selected phase mismatch.
- AC-040: Legacy valid-state input without `work_items` remains accepted for backward compatibility.
- AC-041: `scripts/validate-skills.js` recognizes `lcs-new` as Standard.
- AC-042: `npm test` runs `scripts/validate-skills.js` successfully.
- AC-043: `python3 skills/lcs-shared/scripts/tests/test-validators.py` exits 0.
- AC-044: `git diff --check` exits 0.
- AC-045: Package metadata reports version 2.8.0 and 23 skills.
- AC-046: README, README-ID, AGENTS, INSTALL, Chain of Truth mapping, shared contract, and changelog consistently document `lcs-new` and the 23-skill inventory.

---

## 14. Test Strategy & Testing Decisions

### Testing Decisions

This repository is primarily markdown/instruction-driven. Tests should focus on:

1. machine-verifiable state schema invariants;
2. structural skill metadata consistency;
3. regression fixtures;
4. static contract consistency;
5. targeted end-to-end scenario review for workflow semantics.

Avoid testing prose formatting that does not affect behavior.

### Primary Seam

`.lcs/state.md` frontmatter parsed by `validate-okf.py`.

### Secondary Seams

- canonical skill metadata checked by `scripts/validate-skills.js`;
- fixture runner in `skills/lcs-shared/scripts/tests/test-validators.py`;
- skill instructions that perform phase transitions.

### Unit / Schema Tests

At minimum:

1. valid legacy state -> PASS;
2. valid one-item registry -> PASS;
3. valid multi-item registry -> PASS;
4. selected ID absent from registry -> FAIL;
5. selected phase mismatch -> FAIL;
6. bad path -> FAIL;
7. unsupported status -> FAIL;
8. malformed work-item entry -> FAIL.

### Integration / Static Checks

Run:

```bash
npm test
python3 skills/lcs-shared/scripts/tests/test-validators.py
python3 skills/lcs-shared/scripts/validate-okf.py skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md --strict
git diff --check
```

Also verify:

```bash
grep -n "lcs-new" package.json README.md README-ID.md INSTALL.md AGENTS.md skills/lcs-shared/contract.md skills/lcs-chain-of-truth/SKILL.md scripts/validate-skills.js
```

And ensure finalizer no longer uses stale state terminology:

```bash
! grep -n "active_work_item" skills/lcs-doc-finalizer/SKILL.md
```

### End-to-End Behavioral Scenarios

#### Scenario A: Two Blank/New Items

1. `lcs-new "Feature A"`
2. `lcs-new "Feature B"`
3. state contains A and B;
4. B selected;
5. switch A;
6. selected phase becomes A's stored phase.

Expected: both remain open.

#### Scenario B: Blank -> Explore

1. register blank Feature A;
2. run `lcs-explore` for Feature A;
3. verify same work ID is reused;
4. `explore.md` is created in the existing directory;
5. phase becomes `explore`.

Expected: no duplicate timestamped work item.

#### Scenario C: Full Phase Progression

Expected progression:

```text
new -> explore -> prd -> prd_review -> srs -> tasks -> execution -> code-review -> finalization
```

At each step:

```text
current_phase == work_items[current_work].phase
```

#### Scenario D: Finalize One of Two

1. A and B open;
2. select A;
3. finalize A successfully;
4. A removed;
5. B remains untouched;
6. current pointer becomes null/idle.

Expected: no automatic switch to B.

#### Scenario E: Legacy Migration

1. state has only legacy `current_work/current_phase`;
2. two eligible legacy work-item directories exist;
3. one `*-lcs-master` directory exists;
4. one `*-debug-ext` directory exists;
5. reconcile.

Expected:

- eligible main-flow items imported;
- selected legacy item preserved;
- support/report dirs excluded;
- second reconciliation produces no duplicate/change.

#### Scenario F: Onboarding Isolation

1. Feature A selected at phase `execution`;
2. run onboarding;
3. onboarding docs produced;
4. Feature A remains selected at `execution`.

---

## 15. Risks & Assumptions

### Risks

1. **Duplicated phase source:** `current_phase` and registry phase can drift if any skill is missed.
   - Mitigation: shared invariant + audit all state-writing workflow skills + validator.
2. **Naive reconciliation imports support directories.**
   - Mitigation: positive marker rules plus explicit exclusions.
3. **Empty directories do not survive Git.**
   - Mitigation: registry is authoritative; recreate blank directory when first artifact is written.
4. **Legacy state shape varies across user projects.**
   - Mitigation: additive optional registry, tolerant migration, no destructive cleanup.
5. **Single file still has concurrent writer risk.**
   - Mitigation: explicitly out of scope; do not over-engineer locking in v2.8.
6. **Docs/inventory can drift.**
   - Mitigation: validator canonical mappings and final grep checks.

### Assumptions

- The repository remains markdown-first and skills themselves drive file/state operations. [verified]
- `current_work` is the canonical active-work pointer in the current state template. [verified]
- Current package version is 2.7.0 with 22 listed skills. [verified]
- The current package lacks `scripts.test` even though the validator expects one. [verified]
- `lcs-doc-finalizer` currently contains a stale `active_work_item` reference in its stale-state guard. [verified]
- True simultaneous agent writes to state are not a requirement for this feature. [unverified but intentionally declared out of scope]

---

## 16. Open Questions

None blocking for implementation.

The following decisions are intentionally fixed for v2.8:

- completed work items are removed from open registry;
- finalization leaves no selected item;
- no separate `lcs-switch` skill;
- no `.gitkeep` in blank work items;
- no true concurrent-write solution;
- `lcs-new` is Standard Chain of Truth;
- `srs` is the canonical post-ToSRS phase;
- onboarding is off-flow and must not mutate managed-work selection/phase.

---

## 17. Implementation Task Plan

The tasks below are ordered for direct execution by a coding agent. Unless marked HITL, they are AFK and may be executed autonomously if validation passes.

### TASK-001 — Define Canonical Multi-Workitem State Contract

**Type:** AFK  
**Blocked by:** None  
**Covers:** SRC-003, SRC-006, SRC-007, SRC-012, SRC-017, SRC-024, SRC-025, SRC-026  
**Files:**

- `skills/lcs-shared/templates/state.template.md`
- `skills/lcs-shared/contract.md`

**Actions:**

1. Add `work_items: {}` to state template.
2. Document every registry field and invariant.
3. Define selected-pointer semantics.
4. Define common phase mutation rule.
5. Define managed vs off-flow work-item semantics.
6. Define legacy compatibility/reconciliation rules.
7. Keep `current_work/current_phase` intact.

**Acceptance:** AC-001..AC-004, AC-015, AC-019.

**Verification:**

```bash
grep -n "work_items" skills/lcs-shared/templates/state.template.md skills/lcs-shared/contract.md
git diff --check
```

---

### TASK-002 — Extend OKF State Validation and Fixtures

**Type:** AFK  
**Blocked by:** TASK-001  
**Covers:** SRC-027, SRC-028  
**Files:**

- `skills/lcs-shared/scripts/validate-okf.py`
- `skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md`
- `skills/lcs-shared/scripts/tests/fixtures/okf/invalid-state-current-work.md` (new)
- `skills/lcs-shared/scripts/tests/fixtures/okf/invalid-state-phase-mismatch.md` (new)
- `skills/lcs-shared/scripts/tests/test-validators.py`

**Actions:**

1. Recognize `work_items` as a runtime field.
2. Add state-specific multi-workitem validation.
3. Keep legacy state without `work_items` valid.
4. Add valid multi-item fixture.
5. Add invalid missing-selected-entry fixture.
6. Add invalid phase-mismatch fixture.
7. Register fixtures in test runner.

**Acceptance:** AC-037..AC-040, AC-043.

**Verification:**

```bash
python3 skills/lcs-shared/scripts/tests/test-validators.py
python3 skills/lcs-shared/scripts/validate-okf.py skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md --strict
```

Both commands MUST exit 0.

---

### TASK-003 — Create `lcs-new`

**Type:** AFK  
**Blocked by:** TASK-001  
**Covers:** SRC-001, SRC-002, SRC-016, SRC-024, SRC-025, SRC-029  
**Files:**

- `skills/lcs-new/SKILL.md` (new)

**Actions:**

1. Add precise trigger description.
2. Define Standard Chain of Truth level.
3. Read/init state.
4. Generate ID/path.
5. Create empty directory.
6. Register `phase: new`, `status: open`.
7. Select new work item.
8. Explicitly prohibit content/artifact creation.
9. Add safe rollback rule for failed state write.
10. Add Chain of Truth Report before Handoff.

**Acceptance:** AC-005..AC-009.

**Verification:**

```bash
node scripts/validate-skills.js
```

This task may temporarily require TASK-010 before the full validator can pass because canonical mapping will not yet contain `lcs-new`. If so, record the expected dependency rather than weakening the validator.

---

### TASK-004 — Implement Multi-Workitem Control Plane in `lcs-master`

**Type:** AFK  
**Blocked by:** TASK-001, TASK-003  
**Covers:** SRC-003, SRC-004, SRC-012, SRC-013, SRC-014, SRC-021, SRC-022, SRC-023  
**Files:**

- `skills/lcs-master/SKILL.md`

**Actions:**

1. Update initial state block with `work_items: {}`.
2. Add idempotent reconciliation behavior.
3. Add exclusions for `*-lcs-master` and `*-debug-ext`.
4. Add list operation.
5. Add switch/select operation and ambiguity rules.
6. Add resume behavior.
7. Route explicit blank registration to `lcs-new`.
8. Update router inventory count/reference to 23 skills where applicable.
9. Preserve all existing routing modes and unrelated on-ramps.

**Acceptance:** AC-010..AC-019.

**Verification:**

```bash
grep -n "work_items\|reconcil\|switch\|resume\|lcs-new" skills/lcs-master/SKILL.md
git diff --check
```

---

### TASK-005 — Integrate Work-Item Creation/Reuse Entry Skills

**Type:** AFK  
**Blocked by:** TASK-001, TASK-004  
**Covers:** SRC-015, SRC-017  
**Files:**

- `skills/lcs-explore/SKILL.md`
- `skills/lcs-debug/SKILL.md`
- `skills/lcs-improve-architecture/SKILL.md`

**Actions:**

1. `lcs-explore`: reuse selected compatible blank `phase: new` work item.
2. `lcs-explore`: when creating new work directly, register it.
3. `lcs-debug`: use/register selected managed work item correctly.
4. `lcs-improve-architecture`: use/register selected managed work item correctly.
5. All three use the common phase synchronization rule.

**Acceptance:** AC-020, AC-021, AC-028 plus Scenario B.

**Verification:**

```bash
grep -n "work_items\|current_phase" skills/lcs-explore/SKILL.md skills/lcs-debug/SKILL.md skills/lcs-improve-architecture/SKILL.md
git diff --check
```

---

### TASK-006 — Fix Planning and Specification Phase Tracking

**Type:** AFK  
**Blocked by:** TASK-001  
**Covers:** SRC-017, SRC-018, SRC-019  
**Files:**

- `skills/lcs-toprd/SKILL.md`
- `skills/lcs-prd-reviewer/SKILL.md`
- `skills/lcs-tosrs/SKILL.md`

**Actions:**

1. ToPRD successful completion -> `prd`.
2. PRD reviewer successful completion -> `prd_review`.
3. ToSRS successful completion -> `srs`.
4. Update both compatibility mirror and selected registry entry.
5. Fix ToSRS Handoff from `Current phase: tasks` to `Current phase: srs`.
6. Do not let ToSRS claim `tasks`; task slicer owns that transition.

**Acceptance:** AC-022..AC-024.

**Verification:**

```bash
grep -n "current_phase\|work_items" skills/lcs-toprd/SKILL.md skills/lcs-prd-reviewer/SKILL.md skills/lcs-tosrs/SKILL.md
! grep -n "Current phase: tasks" skills/lcs-tosrs/SKILL.md
```

---

### TASK-007 — Synchronize Execution/Review Phase Writers

**Type:** AFK  
**Blocked by:** TASK-001  
**Covers:** SRC-017  
**Files:**

- `skills/lcs-task-slicer/SKILL.md`
- `skills/lcs-task-executor/SKILL.md`
- `skills/lcs-code-review/SKILL.md`

**Actions:**

Update each existing phase transition so it also updates the selected registry entry and timestamp.

Phases:

- task slicer -> `tasks`
- executor -> `execution`
- code review -> `code-review`

**Acceptance:** AC-025..AC-027.

**Verification:**

```bash
grep -n "work_items\|current_phase" skills/lcs-task-slicer/SKILL.md skills/lcs-task-executor/SKILL.md skills/lcs-code-review/SKILL.md
git diff --check
```

---

### TASK-008 — Isolate Project-Level Onboarding State

**Type:** AFK  
**Blocked by:** TASK-001  
**Covers:** SRC-020  
**Files:**

- `skills/lcs-onboarding/SKILL.md`

**Actions:**

1. Remove/replace any instruction that changes managed `current_phase` to onboarding.
2. Explicitly preserve `current_work/current_phase/work_items`.
3. Permit timestamp/session-note update only.
4. Keep singleton output paths unchanged.

**Acceptance:** AC-029 and Scenario F.

**Verification:**

```bash
grep -n "current_phase\|current_work\|work_items" skills/lcs-onboarding/SKILL.md
git diff --check
```

---

### TASK-009 — Update Finalization Lifecycle

**Type:** AFK  
**Blocked by:** TASK-001, TASK-002  
**Covers:** SRC-005, SRC-008, SRC-009, SRC-010, SRC-011  
**Files:**

- `skills/lcs-doc-finalizer/SKILL.md`

**Actions:**

1. Validate selected registry entry.
2. Synchronize phase to `finalization` while running.
3. Preserve existing docs/archive guards.
4. Remove registry entry only after successful finalization.
5. Set pointer null/idle.
6. Preserve other entries byte-for-byte in semantics.
7. Do not auto-switch.
8. Replace stale `active_work_item` terminology.
9. On failure, keep item open and selected.

**Acceptance:** AC-030..AC-036.

**Verification:**

```bash
! grep -n "active_work_item" skills/lcs-doc-finalizer/SKILL.md
grep -n "work_items\|current_work\|current_phase" skills/lcs-doc-finalizer/SKILL.md
git diff --check
```

---

### TASK-010 — Register Skill Level and Restore Package Validation

**Type:** AFK  
**Blocked by:** TASK-003  
**Covers:** SRC-029, SRC-030, SRC-031  
**Files:**

- `skills/lcs-chain-of-truth/SKILL.md`
- `skills/lcs-shared/contract.md`
- `scripts/validate-skills.js`
- `package.json`

**Actions:**

1. Add `lcs-new` as Standard everywhere canonical levels are declared.
2. Add `lcs-new` to package skills array.
3. Set version 2.8.0.
4. Set total skills 23.
5. Restore `scripts.test` -> `node scripts/validate-skills.js`.
6. Add optional `test:validators` Python command.
7. Update package description.
8. Keep installAll/skillsDir semantics unchanged.

**Acceptance:** AC-041, AC-042, AC-045.

**Verification:**

```bash
npm test
node scripts/validate-skills.js
```

Both MUST exit 0.

---

### TASK-011 — Update Documentation and Inventories

**Type:** AFK  
**Blocked by:** TASK-003, TASK-004, TASK-010  
**Covers:** SRC-030, SRC-032  
**Files:**

- `README.md`
- `README-ID.md`
- `AGENTS.md`
- `INSTALL.md`
- `CHANGELOG.md`

**Actions:**

1. Update inventory to 23 skills.
2. Add `lcs-new` purpose and example.
3. Document optional `lcs-new -> lcs-explore` flow.
4. Add multi-workitem state explanation.
5. Update installation expected list/count.
6. Add v2.8 changelog entry dated 2026-09-17.
7. Correct stale inventory references encountered in the touched sections (e.g. old 21/22 counts) without unrelated rewrites.

**Acceptance:** AC-046.

**Verification:**

```bash
grep -n "lcs-new" README.md README-ID.md AGENTS.md INSTALL.md CHANGELOG.md
grep -n "23" package.json README.md README-ID.md AGENTS.md INSTALL.md CHANGELOG.md
git diff --check
```

---

### TASK-012 — Add Multi-Workitem Regression Consistency Checks

**Type:** AFK  
**Blocked by:** TASK-002, TASK-006, TASK-007, TASK-008, TASK-009, TASK-010  
**Covers:** SRC-017, SRC-027, SRC-028  
**Files:**

- `scripts/validate-skills.js` if a small static consistency check is useful
- existing validator fixtures/tests

**Actions:**

1. Ensure state template exposes registry.
2. Ensure `lcs-new` is canonical and valid.
3. Ensure key managed phase-changing skills reference the shared multi-workitem synchronization contract or explicitly update registry phase.
4. Keep checks simple; do not parse English deeply.
5. Prefer checking stable tokens/contract references instead of brittle prose.

**Acceptance:** No phase writer remains obviously single-pointer-only.

**Verification:**

```bash
npm test
python3 skills/lcs-shared/scripts/tests/test-validators.py
git diff --check
```

---

### TASK-013 — Full End-to-End Review and Release Gate

**Type:** HITL  
**Blocked by:** TASK-001 through TASK-012  
**Covers:** All SRC/AC IDs  
**Files:** No new feature files expected; only corrections if validation finds defects.

**Agent Actions:**

1. Run the full validation suite.
2. Execute static inspections for every acceptance group.
3. Review the six E2E scenarios in this PRD against the final skill instructions.
4. Produce a concise report of pass/fail by AC ID.
5. Do not tag/release automatically.

**Required Commands:**

```bash
npm test
python3 skills/lcs-shared/scripts/tests/test-validators.py
python3 skills/lcs-shared/scripts/validate-okf.py skills/lcs-shared/scripts/tests/fixtures/okf/valid-state.md --strict
git diff --check
git status --short
```

All validation commands except `git status --short` MUST exit 0.

**Human Gate:**

Review the final diff before merge/tag.

Recommended release target:

```text
v2.8.0 — Multi-Workitem State Management + lcs-new
```

---

## 18. Task Dependency Graph

```text
TASK-001  State contract/template
   |\
   | +--> TASK-002  Validator + fixtures
   | +--> TASK-003  lcs-new
   | +--> TASK-006  PRD/reviewer/ToSRS phases
   | +--> TASK-007  Tasks/executor/review phases
   | +--> TASK-008  Onboarding isolation
   | +--> TASK-009  Finalizer lifecycle
   |
   +--> TASK-004  lcs-master control plane  <-- TASK-003
           |
           +--> TASK-005  Explore/debug/architecture integration

TASK-003 --> TASK-010  Canonical mapping/package
TASK-004 + TASK-010 --> TASK-011  Docs/inventory

TASK-002 + TASK-006 + TASK-007 + TASK-008 + TASK-009 + TASK-010
   --> TASK-012 Regression consistency

TASK-001..TASK-012 --> TASK-013 Final HITL release gate
```

---

## 19. Suggested Coding-Agent Execution Rules

The coding agent executing this PRD SHOULD:

1. Work task-by-task in dependency order.
2. Avoid unrelated cleanup.
3. Keep existing skill wording/style where possible.
4. Preserve current paths and artifact names unless this PRD explicitly changes them.
5. Run each task's verification commands before marking it done.
6. Stop on validation failure and report the exact command/output.
7. Do not weaken validators merely to make tests pass.
8. Do not silently drop backward compatibility.
9. Do not implement concurrency locking or a second state store.
10. At final review, map every acceptance criterion to evidence.

---

## 20. Review Notes

- Last Reviewed: 2026-09-17
- Summary: Developer-ready PRD created from user requirements and a fresh inspection of the current repository state.
- Changes Applied:
  - expanded the original `lcs-new` request into a full multi-workitem lifecycle feature;
  - added legacy migration/reconciliation;
  - added phase synchronization across the complete main flow;
  - included missing ToPRD/PRD-review/ToSRS state transitions;
  - corrected ToSRS phase ownership;
  - isolated onboarding from managed-work phase state;
  - defined finalizer removal/no-auto-switch semantics;
  - added validator/package/docs/release work;
  - provided 13 executable tasks with dependencies and verification commands.

---

## 21. Chain of Truth Report

### Level

Standard

### Sources Checked

- Current user requirements in this conversation.
- Current `master` versions of the repository files listed in Section 3.
- LCS state template and shared contract.
- Main-flow skill files that read/write state or represent workflow phases.
- Package and validator files that control skill inventory and validation.

### Assumptions

- Multiple unfinished work items means multiple open/resumable items, not simultaneous lock-free writes by independent agents. [unverified, explicitly scoped]
- `lcs-new` should create an empty runtime directory but no placeholder artifact. [verified from agreed design]
- Keeping completed items out of the open registry is preferred because docs/archive already preserve history. [verified from agreed design]
- `lcs-new` belongs at Standard Chain of Truth level because it mutates persistent control state. [verified from agreed design]

### Plan

1. Preserve the user's explicit `lcs-new` and multi-workitem requirements as atomic source requirements.
2. Incorporate repository-specific state writers and discovered inconsistencies.
3. Define one canonical schema and lifecycle.
4. Make behavior testable with acceptance criteria.
5. Produce an ordered task plan suitable for direct coding-agent execution.

### Actions Taken

- Inspected the current repository state relevant to state handling, workflow phases, validators, package metadata, inventory, and documentation.
- Converted requirements into 34 `SRC-###` entries.
- Defined 46 acceptance criteria.
- Defined 13 implementation tasks with dependencies, files, actions, and verification commands.

### Verification

- Requirement preservation reviewed against the current conversation.
- Affected file paths are limited to paths verified in the repository or explicitly marked as new files.
- The task graph covers state schema, migration, every relevant phase writer, finalization, validation, package metadata, and documentation.
- No production patch/code was generated in this artifact.

### Report

Confidence: high for the requested feature scope and affected repository areas. The largest intentionally unresolved architectural concern—true simultaneous multi-agent state writes—is explicitly out of scope rather than silently ignored.

---

## Handoff

Next recommended skill: lcs-prd-reviewer (or direct coding-agent execution using TASK-001 through TASK-013)
Next file to read: prd-new.md
Current phase: prd
Current confidence: high
Blocking questions: None
Risks to carry forward: Single-file state remains susceptible to true simultaneous writers; do not expand scope into locking during v2.8 implementation.
Source of Truth Bundle: prd-new.md plus the repository files listed in Section 3
Must Preserve IDs: SRC-001 through SRC-034
Unresolved IDs: None
Suggested next command: Execute TASK-001 from prd-new.md, then continue in dependency order and stop on any validation failure.
