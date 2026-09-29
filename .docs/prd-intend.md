# PRD: LCS Explore — Problem Definition, Intent & Solution Discovery

**Status:** Draft for Implementation
**Target:** LCS Reference Implementation
**Primary Skill:** `lcs-explore`

---

# 1. Overview

LCS saat ini menggunakan `lcs-explore` sebagai tahap untuk memahami problem, mengklarifikasi goals dan constraints, menginspeksi codebase/context, mengidentifikasi unknowns dan assumptions, serta menghindari premature implementation.

Saat ini output utama Explore adalah:

```text
explore.md
```

Perubahan ini memperluas fungsi Explore agar tidak hanya mencatat proses eksplorasi, tetapi juga secara eksplisit:

1. **menemukan dan mendefinisikan masalah sebenarnya dari user;**
2. **menemukan dan memurnikan Intent user;**
3. **mengeksplorasi kemungkinan solusi dan alternatif;**
4. menghasilkan dua artifact:

   * `explore.md`
   * `intent.md`

Setelah Intent cukup matang dan dikonfirmasi, `intent.md` menjadi **guard rail** untuk PRD dan seluruh downstream workflow.

---

# 2. Problem Statement

User sering memulai pekerjaan software dengan bentuk yang belum matang:

> "Saya ingin bikin dashboard."

> "Tambahkan export Excel."

> "Buat fitur login."

> "Saya ingin sistem yang lebih cepat."

Pernyataan tersebut belum tentu merupakan definisi masalah.

Sering kali user:

* sudah mempunyai solusi dalam pikirannya tetapi belum menjelaskan masalahnya;
* hanya mempunyai ide kasar;
* belum mengetahui outcome yang sebenarnya diinginkan;
* belum mengetahui batasan sistem;
* belum mengetahui solusi terbaik;
* atau bahkan belum memahami apa yang sebenarnya menyebabkan masalah.

Jika agent langsung mengubah request menjadi requirement, terdapat risiko:

```text
User Request
    ↓
Assumed Problem
    ↓
Assumed Solution
    ↓
Implementation
```

Akibatnya agent dapat membangun solusi yang secara teknis benar tetapi menyelesaikan masalah yang salah.

LCS membutuhkan proses yang lebih kuat:

```text
User Request
    ↓
Understand Context
    ↓
Discover Actual Problem
    ↓
Define Intent
    ↓
Explore Possible Solutions
    ↓
Define Product Requirements
    ↓
Technical Specification
    ↓
Implementation
```

---

# 3. Objective

Perubahan ini bertujuan menjadikan `lcs-explore` sebagai proses untuk mengubah:

> **ide/request yang masih ambigu**

menjadi:

> **problem yang terdefinisi + intent yang jelas + arah solusi yang memiliki dasar.**

Secara khusus Explore harus membantu agent menjawab tiga pertanyaan:

### A. Problem

> **Masalah apa yang sebenarnya ingin diselesaikan?**

### B. Intent

> **Apa yang sebenarnya ingin dicapai user dan mengapa?**

### C. Solution

> **Pendekatan seperti apa yang masuk akal untuk menyelesaikan masalah tersebut dalam konteks sistem yang ada?**

Explore tidak harus menghasilkan desain teknis final.

---

# 4. Core Principle

## 4.1 Don't blindly implement the request

Request user bukan otomatis merupakan problem definition.

Contoh:

```text
User:
"Saya ingin export Excel."
```

Explore harus mencari tahu:

```text
Mengapa?
↓
Informasi apa yang ingin diperoleh?
↓
Siapa yang membutuhkan?
↓
Masalah apa yang terjadi sekarang?
↓
Apakah Excel memang solusi yang diperlukan?
```

Possible conclusion:

```text
Problem:
Accounting harus melakukan rekap transaksi manual.

Intent:
User ingin accounting dapat memperoleh laporan transaksi
tanpa melakukan rekap manual.

Possible solutions:
- Export Excel
- Report generator
- Scheduled report
```

Excel mungkin tetap menjadi solusi.

Tetapi keputusan tersebut harus berasal dari pemahaman problem, bukan asumsi awal agent.

---

# 5. Core Model

Model mental LCS Explore menjadi:

```text
                    USER
                     │
                     ▼
               IDEA / REQUEST
                     │
                     ▼
              ┌──────────────┐
              │    EXPLORE   │
              │              │
              │ Understand   │
              │ Problem      │
              │ Intent       │
              │ Context      │
              │ Constraints  │
              │ Solutions    │
              └──────┬───────┘
                     │
           ┌─────────┼─────────┐
           ▼         ▼         ▼
        Problem    Intent    Solutions
           │         │         │
           └─────────┼─────────┘
                     │
              ┌──────┴──────┐
              ▼             ▼
         explore.md     intent.md
                            │
                            │ GUARD RAIL
                            ▼
                           PRD
                            │
                            ▼
                       PRD REVIEW
                            │
                            ▼
                           SRS
                            │
                            ▼
                         TASKS
                            │
                            ▼
                         CODE
                            │
                            ▼
                       VERIFY
                            │
                            ▼
                         REVIEW
                            │
                            ▼
                   INTENT ALIGNMENT
```

---

# 6. Explore Has Three Responsibilities

## 6.1 Problem Discovery & Definition

Explore harus membedakan:

```text
User Request
```

dari:

```text
Actual Problem
```

Agent harus mencari evidence dan informasi yang cukup untuk mendefinisikan problem.

Problem definition harus menjelaskan, jika relevan:

* siapa yang mengalami masalah;
* kondisi saat ini;
* apa yang tidak berjalan dengan baik;
* dampak masalah;
* mengapa masalah tersebut penting;
* konteks sistem yang terkait;
* existing workflow/capability;
* penyebab yang diketahui;
* hal yang masih belum diketahui.

Agent tidak boleh mengubah asumsi menjadi fakta.

---

## 6.2 Intent Discovery & Refinement

Intent tidak harus sudah diketahui user sejak awal.

Intent ditemukan melalui proses Explore.

Model:

```text
Initial Idea
    ↓
Question
    ↓
User Answer
    ↓
Better Understanding
    ↓
Intent Refinement
    ↓
More Questions
    ↓
Intent Refinement
    ↓
Intent Confirmed
```

Intent harus menjawab:

> **Apa outcome yang sebenarnya diinginkan user setelah masalah tersebut diselesaikan?**

Intent harus tetap menggunakan bahasa yang dekat dengan user dan tidak memasukkan keputusan teknis yang belum diperlukan.

---

## 6.3 Solution Exploration

Explore juga harus menyelidiki kemungkinan solusi ketika hal tersebut relevan.

Tujuannya bukan membuat technical design final.

Tujuannya adalah mencegah agent:

```text
User proposed solution
        ↓
Blind implementation
```

Explore dapat:

* memeriksa existing system;
* mencari capability yang sudah tersedia;
* mengidentifikasi kemungkinan pendekatan;
* membandingkan alternatif;
* menemukan trade-off penting;
* menemukan solusi yang lebih sederhana;
* mengidentifikasi risiko;
* menentukan apakah solusi awal user memang relevan terhadap problem.

Prinsipnya:

> **Prefer the simplest solution that adequately solves the validated problem within the established constraints.**

"Simple" bukan berarti selalu paling sedikit code.

Yang dicari adalah solusi yang proporsional terhadap problem, constraint, risiko, dan kebutuhan.

---

# 7. Intent Is Discovered, Not Assumed

Intent **tidak menjadi artifact yang wajib dibuat sebelum Explore**.

Urutan yang benar:

```text
Initial User Idea
       ↓
     Explore
       ↓
Problem becomes clearer
       ↓
Intent becomes clearer
       ↓
Intent refined
       ↓
Intent confirmed
       ↓
PRD
```

Karena itu `intent.md` merupakan **output dari Explore**, bukan input sebelum Explore.

---

# 8. Relationship Between `explore.md` and `intent.md`

Kedua artifact mempunyai fungsi berbeda.

## `explore.md`

Menjawab:

> **"Apa yang kita temukan selama proses eksplorasi?"**

Dapat berisi:

* initial request;
* questions;
* answers;
* context;
* codebase findings;
* existing capabilities;
* problem discovery;
* assumptions;
* evidence;
* alternatives;
* trade-offs;
* risks;
* decisions;
* unresolved questions;
* solution exploration.

`explore.md` adalah **exploration record**.

---

## `intent.md`

Menjawab:

> **"Setelah eksplorasi, apa sebenarnya yang ingin dicapai user?"**

`intent.md` harus jauh lebih ringkas.

Ia adalah:

> **refined user intent / proto-spec**

Bukan transcript.

Bukan PRD.

Bukan SRS.

Bukan technical design.

---

# 9. `intent.md` Structure

Minimal:

```markdown
# Intent: <short title>

## Problem

<problem yang sebenarnya ingin diselesaikan>

## Proposed Outcome

<hasil yang ingin dicapai>

## Affected Users and Systems

<user, actor, atau system yang terdampak>

## Constraints

<batasan yang harus dipertahankan>

## Out of Scope

<hal yang secara eksplisit tidak termasuk>

## Open Questions

<hal penting yang masih belum terjawab>
```

---

# 10. Meaning of Each Intent Section

## Problem

Harus menggambarkan masalah, bukan solusi.

Kurang tepat:

```text
User membutuhkan dashboard.
```

Lebih tepat:

```text
User kesulitan mengetahui project mana yang sedang
berjalan, mendekati deadline, atau blocked.
```

---

## Proposed Outcome

Menggambarkan perubahan yang diinginkan.

Contoh:

```text
User dapat melihat status project, deadline,
dan blocked project dari satu tempat.
```

Tidak perlu menjelaskan bagaimana sistem melakukannya.

---

## Affected Users and Systems

Mengidentifikasi pihak dan sistem yang relevan.

Contoh:

```text
Users:
- Project manager

Systems:
- Existing project management data
```

---

## Constraints

Batasan yang harus dihormati.

Contoh:

```text
- Monitoring only
- Existing project data harus digunakan
- Tidak mengubah workflow project
```

---

## Out of Scope

Hal yang secara eksplisit tidak termasuk.

Contoh:

```text
- Editing project
- Rescheduling
- Notification system
```

Bagian ini menjadi salah satu guard rail utama terhadap scope creep.

---

## Open Questions

Hal yang belum diketahui.

Contoh:

```text
- Apakah task-level information perlu ditampilkan?
- Apakah dashboard perlu real-time?
```

Open Question tidak boleh diam-diam dijadikan requirement.

---

# 11. Intent Refinement Rules

Selama Explore:

### Agent MAY

* merapikan bahasa user;
* menggabungkan jawaban user;
* menyimpulkan informasi yang didukung evidence;
* mengidentifikasi pola;
* memperjelas hubungan problem → outcome;
* memperbarui Intent ketika user memberikan informasi baru.

### Agent MUST NOT

* mengarang kebutuhan;
* memasukkan preference yang belum diberikan;
* mengubah assumption menjadi fact;
* memaksakan solusi teknis;
* memperluas scope tanpa dasar;
* memasukkan implementation detail ke Intent tanpa alasan yang berasal dari constraint atau requirement eksplisit.

---

# 12. Problem Definition Rules

Explore harus membedakan setidaknya empat hal:

```text
Request
Problem
Intent
Solution
```

Contoh:

```text
Request:
"Buat export Excel."

Problem:
"Accounting harus merekap transaksi secara manual."

Intent:
"Accounting dapat memperoleh laporan transaksi
tanpa rekap manual."

Solution:
"Generate Excel report."
```

Keempatnya tidak boleh diperlakukan sebagai hal yang sama.

---

# 13. Solution Exploration Rules

Agent tidak wajib selalu melakukan extensive solution exploration.

Depth bergantung pada:

* complexity;
* risk;
* ambiguity;
* existing system;
* architectural impact;
* cost of being wrong.

Untuk pekerjaan sederhana:

```text
Problem
 ↓
Intent
 ↓
Obvious solution
```

cukup.

Untuk pekerjaan kompleks:

```text
Problem
 ↓
Intent
 ↓
Existing System
 ↓
Alternatives
 ↓
Trade-offs
 ↓
Recommended Direction
```

dapat diperlukan.

Ini mempertahankan prinsip Lean LCS: tidak semua work item membutuhkan seluruh lifecycle atau kedalaman yang sama.

---

# 14. Solution Recommendation

Jika beberapa solusi ditemukan, Explore boleh memberikan recommendation.

Namun recommendation harus:

* didasarkan pada problem;
* mempertimbangkan existing system;
* mempertimbangkan constraints;
* mempertimbangkan complexity;
* mempertimbangkan maintenance;
* mempertimbangkan risiko;
* menjelaskan trade-off.

Recommendation bukan keputusan final jika membutuhkan keputusan manusia.

Human tetap memiliki authority terhadap product direction, significant trade-offs, scope approval, dan ambiguous business decisions.

---

# 15. Intent Status

`intent.md` dapat menggunakan metadata:

```yaml
---
type: intent
status: refining
---
```

Selama Explore:

```text
refining
```

Setelah cukup jelas:

```text
confirmed
```

Jika masih terdapat ambiguity yang menghalangi downstream work:

```text
blocked
```

Jika Intent kemudian digantikan oleh Intent baru:

```text
superseded
```

Status minimal yang diperlukan untuk v1:

```text
refining
confirmed
```

Status tambahan hanya digunakan jika memang diperlukan oleh implementation.

---

# 16. When Is Intent Ready?

Intent dianggap cukup matang apabila:

1. Problem dapat dijelaskan dengan jelas.
2. Proposed Outcome dapat dijelaskan.
3. Affected Users/Systems cukup diketahui.
4. Material constraints telah diketahui.
5. Out of Scope penting telah diidentifikasi.
6. Tidak terdapat ambiguity yang secara material menghalangi PRD.
7. User telah memiliki kesempatan untuk mengoreksi interpretation agent.
8. Tidak ada assumption kritis yang disamarkan sebagai confirmed intent.

Tidak semua Open Questions harus selesai.

Pertanyaan yang tidak menghalangi downstream work dapat tetap dibawa sebagai Open Questions.

---

# 17. Intent Confirmation

Sebelum Explore selesai, agent harus memberikan kesempatan kepada user untuk mengoreksi hasil Intent apabila terdapat material ambiguity.

Contoh:

```text
"Jadi yang saya pahami:
- Problem: ...
- Outcome: ...
- Constraint: ...
- Out of Scope: ...

Apakah ini sudah sesuai?"
```

Agent tidak boleh menganggap silence sebagai explicit approval jika keputusan tersebut material.

Human approval tetap mengikuti kebutuhan HITL LCS.

---

# 18. Solution Direction vs Technical Design

Explore boleh menghasilkan:

```text
Recommended Solution Direction
```

Tetapi tidak boleh menggantikan SRS.

Contoh yang sesuai:

```text
Recommended Direction:
Reuse existing project data and add a read-only
summary view instead of creating a separate
project management system.
```

Contoh yang terlalu dini:

```text
Create:
- Laravel controller
- Vue component
- Redis cache
- PostgreSQL materialized view
```

Detail tersebut menjadi tanggung jawab PRD/SRS ketika memang diperlukan.

---

# 19. PRD Guard Rail

Setelah Intent confirmed:

```text
intent.md
     │
     │ guard rail
     ▼
   PRD
     │
     ▼
   SRS
     │
     ▼
  TASKS
     │
     ▼
IMPLEMENTATION
```

Downstream artifacts harus tetap aligned dengan:

* Problem;
* Proposed Outcome;
* Constraints;
* Out of Scope.

Downstream artifact tidak boleh memperkenalkan behavior yang secara material bertentangan dengan Intent tanpa explicit scope/intent change.

---

# 20. Intent Drift

Intent drift terjadi ketika:

```text
Original Intent
      ↓
PRD
      ↓
SRS
      ↓
Implementation
```

secara bertahap menghasilkan sesuatu yang berbeda dari tujuan awal.

Contoh:

Intent:

```text
Monitoring only.
```

PRD:

```text
Dashboard + edit project.
```

Ini merupakan potential Intent drift.

Agent harus mendeteksi dan menandai konflik tersebut.

---

# 21. Intent Change

Intent bukan immutable selama seluruh lifecycle.

Perubahan diperbolehkan apabila kebutuhan memang berubah.

Namun:

```text
Intent Change
     ↓
Explicit
     ↓
Traceable
     ↓
Downstream artifacts reconsidered
```

Perubahan material terhadap Intent harus tidak terjadi secara diam-diam.

Jika Intent berubah secara material setelah PRD dibuat, PRD/SRS/tasks yang terdampak harus ditinjau kembali.

---

# 22. Intent Traceability

Intent memperkuat existing LCS requirement traceability.

Conceptual chain:

```text
USER INPUT
   ↓
PROBLEM
   ↓
INTENT
   ↓
SRC
   ↓
FR / BR / VR / EC
   ↓
AC
   ↓
TEST
   ↓
TASK
   ↓
CODE
   ↓
VERIFICATION
```

Existing LCS requirement traceability tetap menjadi mekanisme utama requirement-to-verification.

`intent.md` tidak menggantikan Source Requirement Ledger.

Ia memberikan **higher-level semantic anchor** di atas requirement chain.

---

# 23. Final Intent Alignment Review

Pada review akhir, agent harus dapat menjawab:

### Problem

Apakah implementation menyelesaikan problem yang didefinisikan?

### Outcome

Apakah intended outcome tercapai?

### Constraints

Apakah constraints tetap dipenuhi?

### Scope

Apakah sesuatu yang masuk Out of Scope ikut dibangun?

### Drift

Apakah implementation menghasilkan behavior yang tidak berasal dari Intent/requirements?

### Changes

Apakah ada perubahan Intent yang belum tercatat?

Conceptual reverse trace:

```text
CODE
 ↓
TASK
 ↓
SRS
 ↓
PRD
 ↓
INTENT
 ↓
PROBLEM
```

---

# 24. Explore Artifact

`explore.md` harus tetap menjadi exploration record.

Suggested high-level structure:

```markdown
# Explore: <title>

## Initial Request

## Context

## Problem Discovery

## User Intent Discovery

## Existing System / Codebase Findings

## Constraints

## Assumptions

## Solution Exploration

## Alternatives

## Trade-offs

## Decisions

## Risks

## Open Questions

## Recommended Direction

## Exploration Summary
```

Exact sections may remain adaptive according to existing LCS Explore conventions.

Tidak semua section wajib muncul pada pekerjaan sederhana.

---

# 25. Intent Artifact

Expected:

```text
.lcs/
└── work-items/
    └── <work-item>/
        ├── explore.md
        └── intent.md
```

`intent.md` berada pada work item yang sama dengan `explore.md`.

---

# 26. Changes to `lcs-explore`

Modify `lcs-explore` so that it:

1. Continues the existing interactive Explore workflow.
2. Understands the initial request.
3. Investigates the actual problem.
4. Distinguishes request from problem.
5. Clarifies user intent.
6. Refines Intent during the conversation.
7. Inspects relevant project/codebase context.
8. Identifies constraints.
9. Identifies assumptions and unknowns.
10. Explores possible solution directions where useful.
11. Identifies relevant alternatives and trade-offs.
12. Avoids premature technical implementation.
13. Produces `explore.md`.
14. Produces `intent.md`.
15. Allows Intent to be updated during Explore.
16. Determines whether Intent is sufficiently mature for PRD.
17. Provides the user an opportunity to correct material interpretation.
18. Produces a clear handoff to `lcs-toprd`.

---

# 27. Changes to `lcs-toprd`

`lcs-toprd` must consume:

```text
explore.md
intent.md
```

`intent.md` becomes the primary source for:

* user problem;
* intended outcome;
* constraints;
* out-of-scope boundaries.

`explore.md` remains the supporting source for:

* findings;
* evidence;
* alternatives;
* assumptions;
* decisions;
* solution exploration;
* context.

PRD must not blindly reproduce the initial user request if Explore established a more accurate problem/intent.

---

# 28. PRD Solution Responsibility

PRD is where the refined problem and intent become an explicit product solution.

Conceptually:

```text
Explore
    ↓
Understand Problem
    ↓
Understand Intent
    ↓
Explore Solution Space
    ↓
PRD
    ↓
Define Product Solution
```

PRD should answer:

> **What should be built to solve the validated problem and achieve the confirmed outcome?**

It should not merely restate:

> "User asked for X."

---

# 29. Downstream Skill Changes

Inspect and update only the downstream skills that need to understand Intent.

Potentially affected:

* `lcs-toprd`
* `lcs-prd-reviewer`
* `lcs-tosrs`
* `lcs-task-slicer`
* `lcs-task-executor`
* `lcs-code-review`
* `lcs-doc-finalizer`
* `lcs-chain-of-truth`
* shared contract/documentation

Do not redesign unrelated skills.

---

# 30. Chain of Truth Compatibility

The Intent artifact must remain compatible with the existing LCS Chain of Truth.

Existing canonical structure:

```text
Source
 ↓
Assumption
 ↓
Plan
 ↓
Action
 ↓
Verification
 ↓
Report
```

Intent is an external engineering artifact.

It is not model chain-of-thought.

Intent should be based on:

* user statements;
* project evidence;
* verified findings;
* explicitly acknowledged assumptions.

The Chain of Truth remains authoritative for evidence and action traceability.

---

# 31. Human / Agent Boundary

The agent is responsible for:

* asking useful questions;
* exploring context;
* discovering problems;
* drafting Intent;
* exploring solution alternatives;
* surfacing trade-offs;
* identifying uncertainty;
* maintaining artifacts.

The human remains responsible for:

* correcting Intent;
* product direction;
* significant scope decisions;
* significant trade-offs;
* risk acceptance;
* ambiguous business decisions;
* final acceptance where appropriate.

This preserves the existing LCS human-supervision principle.

---

# 32. Lean Principle

This feature must not turn Explore into a mandatory heavyweight process.

Depth must scale with:

```text
Ambiguity
Complexity
Risk
Impact
```

Simple work:

```text
Question
 ↓
Problem
 ↓
Intent
 ↓
Obvious Solution
```

Complex work:

```text
Context
 ↓
Problem
 ↓
Intent
 ↓
Existing System
 ↓
Alternatives
 ↓
Trade-offs
 ↓
Solution Direction
 ↓
PRD
```

The goal is not maximum documentation.

The goal is:

> **Reduce ambiguity before downstream implementation.**

This is consistent with the existing LCS principle that artifacts should earn their place by reducing ambiguity without creating unnecessary documentation overhead.

---

# 33. Non-Goals

This change does NOT aim to:

* create a standalone `lcs-intent` skill;
* replace `lcs-explore`;
* replace PRD;
* replace SRS;
* make Intent a technical design;
* force users to know their complete goal before Explore;
* force every Explore to perform extensive solution comparison;
* require every work item to have extensive documentation;
* replace Source Requirement Ledger;
* replace Chain of Truth;
* introduce a database;
* introduce a new runtime dependency;
* redesign the entire LCS workflow.

---

# 34. Backward Compatibility

Existing work items may contain only:

```text
explore.md
```

Historical artifacts must remain readable.

New Explore sessions should produce:

```text
explore.md
intent.md
```

Downstream skills should degrade gracefully when processing historical work items without `intent.md`, where practical.

Historical artifact migration is not required for this change.

---

# 35. Acceptance Criteria

## AC-01 — Two Explore artifacts

A completed normal Explore produces:

```text
explore.md
intent.md
```

---

## AC-02 — Problem is explicitly defined

The Explore process distinguishes the user's initial request from the actual problem when they are different.

---

## AC-03 — Intent is refined during Explore

Intent may evolve as the agent learns more from user answers and project evidence.

---

## AC-04 — Intent represents user meaning

Intent reflects the user's desired outcome rather than the agent's preferred implementation.

---

## AC-05 — Intent contains required sections

`intent.md` contains:

* Problem
* Proposed Outcome
* Affected Users and Systems
* Constraints
* Out of Scope
* Open Questions

---

## AC-06 — No premature technical design

Intent does not contain implementation details unless explicitly required as a user constraint or established requirement.

---

## AC-07 — Solution exploration exists where relevant

For ambiguous or non-trivial work, Explore identifies relevant solution directions or alternatives.

---

## AC-08 — Existing system is considered

Where applicable, Explore investigates whether existing capabilities can solve the problem before proposing unnecessary new systems.

---

## AC-09 — Solution is proportional

The resulting solution direction does not introduce unnecessary complexity when a simpler approach adequately satisfies the validated problem and constraints.

---

## AC-10 — User correction is supported

If the user corrects the agent's interpretation, `intent.md` is updated.

---

## AC-11 — Open Questions remain explicit

Unknowns are not silently converted into requirements.

---

## AC-12 — PRD consumes Intent

`lcs-toprd` reads both:

```text
explore.md
intent.md
```

---

## AC-13 — PRD preserves Intent

PRD remains aligned with:

* Problem
* Proposed Outcome
* Constraints
* Out of Scope

---

## AC-14 — Intent drift can be detected

A downstream artifact that materially conflicts with confirmed Intent can be identified during review.

---

## AC-15 — Intent changes are explicit

Material Intent changes after confirmation are traceable and trigger reconsideration of affected downstream artifacts.

---

## AC-16 — Existing traceability remains valid

Existing LCS requirement traceability continues to function.

---

## AC-17 — Chain of Truth remains valid

The new artifact does not weaken or bypass Chain of Truth requirements.

---

## AC-18 — No standalone intent skill

The implementation enhances `lcs-explore` rather than creating `lcs-intent`.

---

## AC-19 — Lean behavior

Simple work does not result in unnecessary Explore overhead.

---

## AC-20 — Historical compatibility

Existing work items without `intent.md` remain usable where practical.

---

# 36. Behavioral Test Scenarios

## Scenario A — Vague Idea

User:

> "Saya ingin dashboard project."

Expected Explore:

* asks why the dashboard is needed;
* identifies the actual problem;
* identifies desired outcome;
* identifies relevant users;
* identifies constraints;
* generates refined `intent.md`.

---

## Scenario B — User Gives a Solution Instead of a Problem

User:

> "Buatkan export Excel."

Expected:

Agent investigates the reason behind the request.

It must not automatically define:

```text
Problem = Need Excel export
```

---

## Scenario C — Discover Better Problem Definition

Initial:

> "Saya ingin membuat calendar project."

Explore discovers:

> User actually needs visibility into overlapping deadlines.

Expected Intent focuses on the validated problem/outcome rather than blindly preserving "calendar" as the solution.

---

## Scenario D — Existing Capability

User asks for a new dashboard.

Explore discovers existing project page already contains the required data.

Expected:

* existing capability is documented;
* unnecessary duplication is identified;
* solution alternatives are explored.

---

## Scenario E — User Correction

Agent drafts:

```text
Constraint:
Dashboard allows project editing.
```

User says:

> "Tidak, hanya untuk melihat."

Expected:

```text
Out of Scope:
Project editing.
```

Intent is updated before confirmation.

---

## Scenario F — Open Question

User does not know whether task-level data should be displayed.

Expected:

```text
Open Questions:
Should task-level information be included?
```

Agent does not silently decide.

---

## Scenario G — Alternative Solutions

Problem:

> Accounting performs manual report aggregation.

Possible solutions:

```text
A. Excel export
B. Report generator
C. Scheduled report
```

Expected:

Explore records relevant alternatives and trade-offs when the decision materially affects the product direction.

---

## Scenario H — Intent Drift

Confirmed Intent:

```text
Monitoring only.
```

PRD introduces:

```text
Project editing.
```

Expected:

The conflict is surfaced rather than silently accepted.

---

## Scenario I — Scope Proportionality

Simple change:

> Change the label of an existing button.

Expected:

The workflow does not require extensive problem discovery or solution comparison.

---

# 37. Documentation Changes

Update relevant LCS documentation to describe:

```text
Explore
 ├── explore.md
 └── intent.md
```

Document the distinction:

| Artifact     | Primary Question                             |
| ------------ | -------------------------------------------- |
| `explore.md` | What did we discover?                        |
| `intent.md`  | What does the user actually want to achieve? |
| `prd.md`     | What product solution should be built?       |
| `srs.md`     | How should the system behave technically?    |
| Tasks        | What needs to be implemented?                |
| Verification | Did the implementation work?                 |

Also document:

```text
Problem
   ↓
Intent
   ↓
Solution
```

as distinct concepts.

---

# 38. Implementation Constraints

Keep implementation lean.

Prefer:

* existing Markdown artifacts;
* existing LCS work-item structure;
* existing skill conventions;
* existing shared contract;
* existing Chain of Truth;
* existing handoff mechanism.

Do not introduce:

* new runtime dependency;
* database;
* separate intent service;
* standalone intent skill;

unless repository inspection proves an existing architectural constraint requires it.

---

# 39. Expected Workflow After This Change

Before:

```text
User
 ↓
Explore
 ↓
explore.md
 ↓
PRD
 ↓
SRS
 ↓
Tasks
 ↓
Code
```

After:

```text
User
 ↓
Explore
 │
 ├── Understand Context
 │
 ├── Define Problem
 │
 ├── Discover Intent
 │
 ├── Investigate Existing System
 │
 └── Explore Solutions
 │
 ├───────────────┐
 ▼               ▼
explore.md    intent.md
                  │
                  │ GUARD RAIL
                  ▼
                 PRD
                  │
                  ▼
             PRD Review
                  │
                  ▼
                 SRS
                  │
                  ▼
                Tasks
                  │
                  ▼
                 Code
                  │
                  ▼
              Verification
                  │
                  ▼
                Review
                  │
                  ▼
          Intent Alignment Check
```

---

# 40. Definition of Done

The feature is complete when:

1. `lcs-explore` explicitly performs problem discovery.
2. `lcs-explore` distinguishes request, problem, intent, and solution.
3. `lcs-explore` refines Intent through interaction rather than assuming it initially.
4. `lcs-explore` produces `explore.md`.
5. `lcs-explore` produces `intent.md`.
6. `intent.md` follows the defined structure.
7. Intent remains free from premature implementation details.
8. Explore performs solution exploration when complexity/ambiguity warrants it.
9. Existing system capabilities are considered where relevant.
10. `lcs-toprd` consumes both artifacts.
11. PRD preserves the confirmed Intent.
12. Downstream workflow can detect material Intent drift.
13. Material Intent changes remain explicit and traceable.
14. Existing Chain of Truth remains intact.
15. Existing requirement traceability remains intact.
16. Simple work does not receive unnecessary process overhead.
17. Behavioral scenarios pass.
18. Relevant documentation is updated.
19. Historical work items remain usable.
20. No standalone `lcs-intent` skill is introduced.

---

# 41. Guiding Principle

The resulting LCS Explore philosophy is:

> **Do not blindly implement the user's request.**

Instead:

```text
Understand the request.
        ↓
Discover the actual problem.
        ↓
Define what the user really wants to achieve.
        ↓
Understand the existing system.
        ↓
Explore appropriate solution directions.
        ↓
Define the product solution.
        ↓
Build and verify it.
```

Or, more concisely:

> **Understand the problem. Clarify the intent. Explore the solution. Then build.**
