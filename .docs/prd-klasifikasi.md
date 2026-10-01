# PRD: LCS Adaptive Routing / Work Classification

**Project:** Lean Coding Skills (LCS)
**Repository:** `https://github.com/mdhb2/lean-coding-skills/`
**Target component:** `lcs-master`
**Version:** 1.0
**Status:** Ready for Implementation
**Scope:** Phase 1 — Adaptive Routing only

---

# 1. Objective

Mengubah `lcs-master` dari router yang terutama memilih **workflow berdasarkan jenis request** menjadi router yang juga menentukan **kedalaman workflow berdasarkan ukuran, risiko, ambiguitas, dan blast radius pekerjaan**.

Tujuan utamanya:

> **Pekerjaan kecil harus selesai dengan cepat tanpa kehilangan verification yang diperlukan, sementara pekerjaan kompleks tetap mendapatkan workflow LCS yang lengkap.**

Contoh target:

```text
Rename variable
    ↓
Direct / Fast Path
    ↓
Inspect → Edit → Verify
    ↓
Done
```

Bukan:

```text
Explore
→ PRD
→ PRD Review
→ SRS
→ Task Slicing
→ Execute
→ Code Review
→ Finalize
```

Perubahan ini merupakan **fondasi Adaptive LCS**.

Phase ini **belum mengubah executor, code reviewer, atau skill lain**.

---

# 2. Problem Statement

LCS saat ini sudah memiliki prinsip bahwa tidak semua pekerjaan harus menjalankan seluruh lifecycle.

Canonical SOT menyatakan:

```text
Not every work item must execute every phase.

The appropriate entry point and depth depend on:
- nature
- size
- risk
- maturity
```

Namun pada reference implementation, `lcs-master` belum memiliki mekanisme eksplisit yang mengklasifikasikan pekerjaan berdasarkan dimensi tersebut sebelum menentukan workflow depth.

Akibatnya, pekerjaan sederhana berpotensi mendapatkan overhead yang tidak proporsional.

Contoh:

```text
"Rename sendMail() to sendEmail()"
```

secara engineering:

* intent jelas
* ambiguity rendah
* scope kecil
* blast radius dapat dicari
* risiko rendah
* verification sederhana

Tetapi apabila diproses menggunakan workflow penuh, fixed overhead menjadi jauh lebih besar daripada nilai engineering yang diperoleh.

---

# 3. Current State

## 3.1 Current LCS Master Role

`lcs-master` saat ini merupakan control-plane/router LCS.

Tanggung jawabnya meliputi:

* mengenali intent user
* mengenali starting situation
* menentukan skill berikutnya
* menjalankan branching logic
* enforcing shared contract
* managing multi-workitem state
* decision logging
* confirmation/autopilot routing

Current main flow:

```text
lcs-explore
    ↓
lcs-toprd
    ↓
lcs-prd-reviewer
    ↓
lcs-tosrs
    ↓
lcs-task-slicer
    ↓
lcs-task-executor
    ↓
lcs-code-review
    ↓
lcs-doc-finalizer
```

`lcs-master` saat ini memiliki Confirmation Mode dan Autopilot Mode, tetapi belum memiliki **Work Classification layer** sebagai decision point utama.

---

# 4. Desired State

Tambahkan layer:

```text
User Request
     ↓
Context Detection
     ↓
Work Classification
     ↓
Adaptive Routing
     ↓
Selected Workflow
```

Work classification menggunakan empat dimensi utama:

```text
Work Class
Risk
Ambiguity
Blast Radius
```

Classification kemudian menentukan workflow depth.

---

# 5. Goals

## G1 — Adaptive workflow depth

LCS harus dapat memilih workflow depth berdasarkan karakter pekerjaan.

## G2 — Fast path untuk pekerjaan trivial

Pekerjaan yang jelas, kecil, dan low-risk harus dapat menghindari workflow artifact-heavy.

## G3 — Preserve engineering quality

Fast path tidak berarti:

```text
skip verification
```

Fast path berarti:

```text
minimum sufficient verification
```

## G4 — Preserve existing full workflow

Feature normal dan complex harus tetap dapat menggunakan workflow LCS yang sekarang.

## G5 — Tidak mengubah methodology

Perubahan ini adalah implementation improvement terhadap `lcs-master`, bukan perubahan fundamental terhadap filosofi LCS.

## G6 — Classification harus explainable

Agent harus dapat menjelaskan secara singkat:

```text
Class: SMALL
Risk: LOW
Reason: ...
Route: ...
```

Tanpa menghasilkan analisis panjang.

---

# 6. Non-Goals

Phase ini TIDAK mencakup:

* perubahan `lcs-task-executor`
* perubahan `lcs-code-review`
* perubahan `lcs-explore`
* perubahan `lcs-toprd`
* perubahan `lcs-tosrs`
* perubahan `lcs-task-slicer`
* perubahan artifact schema global
* perubahan Chain of Truth protocol
* perubahan OKF specification
* perubahan state model
* pembuatan skill baru
* perubahan adapter Claude Code / OpenCode selain yang diperlukan oleh `lcs-master`
* optimasi prompt/token pada skill lain
* penghapusan workflow existing
* penggantian workflow normal/complex

Phase ini hanya membuat:

> **`lcs-master` mampu menentukan kapan workflow penuh diperlukan dan kapan tidak.**

---

# 7. Design Principles

## 7.1 Risk over ceremony

Workflow depth harus mengikuti risiko, bukan jumlah artifact yang tersedia.

## 7.2 Minimum sufficient process

Gunakan proses paling ringan yang masih memberikan confidence yang cukup.

## 7.3 No quality downgrade

Fast path harus tetap memiliki verification yang sesuai.

## 7.4 Ambiguity is a multiplier

Pekerjaan yang terlihat kecil tetapi ambigu tidak boleh otomatis masuk fast path.

## 7.5 Blast radius matters

Perubahan satu baris dapat tetap high-risk jika menyentuh:

* authentication
* payment
* database schema
* security
* production configuration
* destructive operations

## 7.6 User intent has priority

Jika user secara eksplisit meminta workflow tertentu, classification tidak boleh diam-diam mengabaikan permintaan tersebut.

Contoh:

```text
"Rename this function, tapi saya ingin full LCS review."
```

Harus tetap menghormati explicit request.

## 7.7 Classification should be cheap

Jangan membuat classification sendiri menjadi workflow panjang.

Target:

```text
Classification = seconds, not minutes
```

---

# 8. Work Classification Model

Gunakan empat kelas utama.

```text
TRIVIAL
SMALL
NORMAL
COMPLEX
```

## 8.1 TRIVIAL

Karakteristik:

* intent sangat jelas
* perubahan kecil
* low risk
* low ambiguity
* low blast radius
* tidak membutuhkan architectural decision

Contoh:

* rename variable
* rename function
* typo
* copy/text change
* constant sederhana
* formatting
* import cleanup
* obvious mechanical replacement

Default route:

```text
Direct / Fast Path
```

---

# 8.2 SMALL

Karakteristik:

* scope kecil
* behavior sedikit berubah
* risk rendah sampai medium
* beberapa file mungkin berubah
* membutuhkan targeted verification

Contoh:

* small bug fix
* small UI behavior change
* config adjustment
* local refactor
* simple validation rule

Default route:

```text
Quick / Small Path
```

Untuk Phase 1, route detail Small Path boleh menggunakan existing skill sebagai fallback.

Jangan membuat workflow baru khusus Small jika belum diperlukan.

---

# 8.3 NORMAL

Karakteristik:

* behavior berubah secara meaningful
* requirement perlu diperjelas
* beberapa component dapat terlibat
* test strategy diperlukan
* risk medium
* kemungkinan multi-file

Contoh:

* feature normal
* API behavior change
* database-backed feature
* meaningful UI feature

Default route:

```text
Existing Main Workflow
```

---

# 8.4 COMPLEX

Karakteristik:

* architectural impact
* high risk
* large blast radius
* multi-session
* significant data changes
* security-sensitive
* irreversible operation
* unclear/high uncertainty
* major refactor

Contoh:

* authentication redesign
* payment flow
* database migration besar
* architecture refactor
* distributed-system change
* destructive data operation

Default route:

```text
Existing Full / Strict Workflow
```

---

# 9. Classification Dimensions

## 9.1 Scope

Nilai:

```text
tiny
small
medium
large
```

Pertimbangan:

* jumlah file yang kemungkinan disentuh
* luas perubahan
* apakah perubahan lokal atau cross-cutting

---

## 9.2 Risk

Nilai:

```text
low
medium
high
critical
```

High-risk indicators:

* authentication
* authorization
* security
* credentials
* payment
* financial logic
* destructive database operation
* production infrastructure
* migration
* data loss
* privacy-sensitive behavior

---

## 9.3 Ambiguity

Nilai:

```text
low
medium
high
```

Low:

```text
"Rename foo() to bar()"
```

High:

```text
"Improve the customer system."
```

Jika ambiguity tinggi, jangan masuk TRIVIAL meskipun perubahan akhirnya mungkin kecil.

---

## 9.4 Blast Radius

Nilai:

```text
low
medium
high
```

Low:

```text
single local function
```

Medium:

```text
shared service
```

High:

```text
public API
database schema
authentication
shared infrastructure
```

---

# 10. Classification Rules

Gunakan rule-based classification.

Jangan menggunakan scoring numerik kompleks pada Phase 1.

Prioritas decision:

```text
1. Explicit user instruction
2. Critical/high-risk detection
3. Ambiguity
4. Blast radius
5. Scope
6. Default class
```

## Rule A — Critical override

Jika pekerjaan memiliki critical risk:

```text
work_class = COMPLEX
```

meskipun scope kecil.

Contoh:

```text
"Change one line in payment authorization."
```

Tetap:

```text
COMPLEX
```

---

## Rule B — High risk override

Jika:

```text
risk = high
```

maka minimal:

```text
work_class = NORMAL
```

atau `COMPLEX` jika blast radius/ambiguity juga tinggi.

---

## Rule C — High ambiguity override

Jika intent tidak jelas:

```text
Do not classify as TRIVIAL.
```

---

## Rule D — High blast radius override

Jika perubahan kecil tetapi impact luas:

```text
Do not classify as TRIVIAL.
```

---

## Rule E — Mechanical trivial change

Jika semua kondisi terpenuhi:

```text
intent = clear
scope = tiny
risk = low
ambiguity = low
blast_radius = low
```

maka:

```text
TRIVIAL
```

---

# 11. Classification Matrix

| Scope  | Risk     | Ambiguity | Blast Radius | Class        |
| ------ | -------- | --------- | ------------ | ------------ |
| tiny   | low      | low       | low          | TRIVIAL      |
| small  | low      | low       | low          | SMALL        |
| small  | medium   | low       | low          | SMALL        |
| small  | high     | low       | low          | NORMAL       |
| tiny   | critical | low       | low          | COMPLEX      |
| tiny   | low      | high      | low          | SMALL/NORMAL |
| tiny   | low      | low       | high         | NORMAL       |
| medium | low      | low       | low          | NORMAL       |
| medium | medium   | medium    | medium       | NORMAL       |
| large  | any      | any       | any          | COMPLEX      |
| any    | critical | any       | any          | COMPLEX      |
| any    | high     | high      | any          | COMPLEX      |

Important:

> Matrix adalah decision aid, bukan mathematical scoring engine.

Jika kondisi saling bertentangan, gunakan higher-risk classification.

---

# 12. Adaptive Routing

## TRIVIAL

Default:

```text
Inspect
  ↓
Direct change
  ↓
Minimal verification
  ↓
Report
```

Tidak perlu otomatis menjalankan:

* explore
* PRD
* PRD review
* SRS
* task slicer
* formal code review
* finalizer

---

## SMALL

Phase 1 tidak perlu membuat skill baru.

Router dapat memilih existing lightweight route atau meminta clarification jika route belum aman.

Contoh:

```text
SMALL
 ↓
existing appropriate skill
```

Implementasi Phase 1 harus menghindari membuat pseudo-workflow baru yang besar.

---

## NORMAL

Pertahankan existing main workflow:

```text
Explore
→ PRD
→ PRD Review
→ SRS
→ Task Slicer
→ Executor
→ Review
→ Finalize
```

---

## COMPLEX

Pertahankan existing complex workflow dan on-ramp:

```text
Wayfinder
→ Explore
→ PRD
→ PRD Review
→ SRS
→ Task Slicer
→ Executor
→ Code Review
→ Finalizer
```

Routing detail tetap mengikuti current LCS rules.

---

# 13. Fast Path Contract

Fast path hanya boleh dipilih jika:

```text
work_class = TRIVIAL
```

dan tidak ada explicit user instruction yang meminta full workflow.

Fast path harus:

1. Inspect relevant code.
2. Confirm exact change.
3. Make bounded change.
4. Verify changed references/behavior.
5. Report result.
6. Stop.

Fast path tidak boleh:

* memperluas scope
* melakukan refactor tambahan
* membuat PRD hanya karena tersedia
* membuat task breakdown
* melakukan architecture review
* melakukan unrelated cleanup

---

# 14. Verification Policy

Phase 1 hanya menentukan routing.

Namun fast path harus mendefinisikan konsep:

```text
minimum sufficient verification
```

Contoh mechanical rename:

```text
search old symbol
→ apply rename
→ search remaining old references
→ inspect diff
```

Jika test yang relevan murah dan tersedia:

```text
run targeted test
```

Jangan otomatis menjalankan seluruh test suite untuk setiap trivial change.

Catatan:

Perubahan `lcs-task-executor` untuk menerapkan policy verification secara formal adalah **Phase 2**, bukan bagian PRD ini.

---

# 15. User Override

User boleh override classification.

Contoh:

```text
User:
"Ini cuma rename, tapi jalankan full workflow."
```

Router:

```text
Classification:
TRIVIAL

User Override:
FULL_WORKFLOW

Route:
Existing Full Workflow
```

Sebaliknya:

```text
User:
"Implement feature ini langsung."
```

Tidak otomatis berarti skip safety jika pekerjaan terdeteksi high-risk.

Safety-critical classification tidak boleh diturunkan hanya karena user meminta shortcut.

---

# 16. Classification Output

Output classification harus singkat.

Contoh:

```text
Work Classification

Class: TRIVIAL
Risk: LOW
Ambiguity: LOW
Blast Radius: LOW

Reason:
Mechanical rename with clear scope and no expected behavior change.

Route:
FAST PATH
```

Untuk NORMAL:

```text
Work Classification

Class: NORMAL
Risk: MEDIUM
Ambiguity: LOW
Blast Radius: MEDIUM

Reason:
Behavior changes across multiple application components.

Route:
MAIN LCS WORKFLOW
```

Untuk COMPLEX:

```text
Work Classification

Class: COMPLEX
Risk: HIGH
Ambiguity: MEDIUM
Blast Radius: HIGH

Reason:
Changes authentication behavior and shared security boundaries.

Route:
FULL / STRICT WORKFLOW
```

Jangan menghasilkan penjelasan panjang hanya untuk classification.

---

# 17. Persistence / State

Phase 1 **tidak mengubah state schema global**.

Classification boleh ditampilkan sebagai runtime routing decision.

Jika `lcs-master` membutuhkan persistence untuk continuity, gunakan mekanisme session log yang sudah ada.

Jangan menambahkan:

```text
work_class
risk
ambiguity
blast_radius
```

ke `.lcs/state.md` pada Phase 1 kecuali implementasi existing benar-benar membutuhkan field tersebut.

Tujuan Phase 1 adalah menguji routing policy terlebih dahulu.

---

# 18. Decision Logging

Existing `session-log.md` tetap digunakan.

Untuk routing decision, tambahkan informasi:

```yaml
classification:
  work_class: trivial
  risk: low
  ambiguity: low
  blast_radius: low
route: fast-path
```

Jika struktur session log existing tidak mendukung nested object, gunakan format yang kompatibel dengan struktur existing.

Jangan membuat log format baru jika tidak diperlukan.

---

# 19. Implementation Constraints

Agent implementation wajib mengikuti:

### C1

Perubahan utama hanya pada:

```text
skills/lcs-master/SKILL.md
```

### C2

Jika test/reference/documentation diperlukan, perubahan harus tetap berada dalam scope `lcs-master`.

### C3

Jangan mengubah:

```text
skills/lcs-task-executor/
skills/lcs-code-review/
skills/lcs-explore/
skills/lcs-toprd/
skills/lcs-tosrs/
skills/lcs-task-slicer/
```

### C4

Jangan mengubah `contract.md` untuk Phase 1.

### C5

Jangan mengubah LCS SOT methodology hanya karena implementation detail.

### C6

Jangan menambahkan scoring system kompleks.

### C7

Jangan membuat skill baru hanya untuk classification.

### C8

Classification harus tetap cukup pendek sehingga tidak membuat router lebih lambat daripada workflow yang ingin dioptimalkannya.

---

# 20. Acceptance Criteria

## AC-001 — Work classification tersedia

`lcs-master` memiliki mekanisme eksplisit untuk mengklasifikasikan pekerjaan menjadi:

```text
TRIVIAL
SMALL
NORMAL
COMPLEX
```

---

## AC-002 — Classification menggunakan risk dimensions

Classification mempertimbangkan minimal:

```text
scope
risk
ambiguity
blast radius
```

---

## AC-003 — Critical risk override

Task dengan critical/high-risk characteristics tidak boleh masuk TRIVIAL hanya karena perubahan kode kecil.

---

## AC-004 — Ambiguity protection

Task dengan intent yang ambigu tidak boleh otomatis masuk TRIVIAL.

---

## AC-005 — Fast path tersedia

Task TRIVIAL memiliki route yang dapat melewati workflow artifact-heavy.

---

## AC-006 — Existing normal workflow tetap tersedia

Task NORMAL tetap dapat menggunakan main LCS workflow existing tanpa perubahan behavior yang tidak diperlukan.

---

## AC-007 — Complex workflow preserved

Task COMPLEX tetap dapat menggunakan full/strict workflow existing.

---

## AC-008 — User override didukung

User dapat meminta workflow yang lebih lengkap daripada classification default.

---

## AC-009 — Safety cannot be downgraded

User override tidak boleh menurunkan pekerjaan critical/high-risk menjadi unsafe fast path.

---

## AC-010 — Classification output singkat

Classification menghasilkan output yang ringkas dan actionable.

---

## AC-011 — No unrelated skill modification

Implementasi tidak mengubah executor, reviewer, SRS, task slicer, atau skill lain di luar scope.

---

## AC-012 — Backward compatibility

Existing LCS routing scenario tetap berfungsi.

---

# 21. Test Scenarios

Agent wajib menguji minimal scenario berikut.

### T1 — Rename variable

Input:

```text
Rename $customerName to $clientName.
```

Expected:

```text
TRIVIAL
LOW
LOW
LOW
FAST PATH
```

---

### T2 — Typo fix

Input:

```text
Fix typo "recieve" to "receive".
```

Expected:

```text
TRIVIAL
FAST PATH
```

---

### T3 — Simple bug

Input:

```text
Fix null error in UserProfileController.
```

Expected:

```text
SMALL atau NORMAL
```

Tidak boleh otomatis TRIVIAL jika root cause belum jelas.

---

### T4 — New feature

Input:

```text
Add export customer data to CSV.
```

Expected:

```text
NORMAL
MAIN LCS WORKFLOW
```

---

### T5 — Authentication

Input:

```text
Change login authentication flow.
```

Expected:

```text
COMPLEX
FULL / STRICT WORKFLOW
```

---

### T6 — Database migration

Input:

```text
Rename users.email column to users.email_address.
```

Expected minimal:

```text
NORMAL
```

atau:

```text
COMPLEX
```

Tidak boleh TRIVIAL karena blast radius database.

---

### T7 — Security

Input:

```text
Change authorization middleware to allow admins.
```

Expected:

```text
COMPLEX
```

---

### T8 — Ambiguous request

Input:

```text
Improve the customer module.
```

Expected:

```text
NOT TRIVIAL
```

Router harus meminta clarification atau memilih workflow yang sesuai dengan uncertainty.

---

### T9 — Explicit full workflow override

Input:

```text
Rename this variable, but use the full LCS workflow.
```

Expected:

```text
Classification: TRIVIAL
Override: FULL WORKFLOW
Route: FULL WORKFLOW
```

---

### T10 — Dangerous override

Input:

```text
Just directly change the production payment authorization logic.
```

Expected:

```text
Do NOT downgrade to fast path.
```

Risk classification tetap mengontrol safety boundary.

---

# 22. Non-Regression Tests

Pastikan routing berikut tetap bekerja:

```text
New feature
Bug
Huge project
Refactor
Research
Prototype
Wayfinder
Resume existing work item
Switch work item
Autopilot
Confirmation mode
```

Tidak boleh terjadi perubahan routing yang tidak disengaja.

---

# 23. Implementation Tasks

## TASK-001 — Audit Current LCS Master Routing

**Type:** AFK
**Priority:** P0
**Depends on:** None

### Objective

Memetakan routing existing sebelum melakukan perubahan.

### Files

```text
skills/lcs-master/SKILL.md
skills/lcs-shared/contract.md
```

### Actions

1. Read current `lcs-master/SKILL.md`.
2. Identify:

   * entry points
   * on-ramps
   * main flow
   * confirmation mode
   * autopilot
   * stop matrix
   * handoff rules
   * session logging
3. Identify exact insertion point for Work Classification.
4. Do not modify code yet.

### Acceptance

Agent menghasilkan implementation map yang menjelaskan:

```text
current routing
→ classification insertion point
→ resulting routing
```

---

# TASK-002 — Define Work Classification Policy

**Type:** AFK
**Priority:** P0
**Depends on:** TASK-001

### Objective

Menambahkan policy classification ke `lcs-master`.

### Files

```text
skills/lcs-master/SKILL.md
```

### Actions

Tambahkan:

```text
TRIVIAL
SMALL
NORMAL
COMPLEX
```

dengan:

```text
scope
risk
ambiguity
blast radius
```

dan rule priority:

```text
explicit user instruction
→ critical risk
→ high risk
→ ambiguity
→ blast radius
→ scope
```

### Constraints

Jangan membuat numeric score.

Jangan membuat skill baru.

### Acceptance

Classification policy dapat digunakan agent tanpa membutuhkan interpretasi tambahan.

---

# TASK-003 — Implement Adaptive Routing

**Type:** AFK
**Priority:** P0
**Depends on:** TASK-002

### Objective

Menghubungkan classification ke routing decision.

### Expected routing

```text
TRIVIAL
→ FAST PATH

SMALL
→ LIGHT / EXISTING APPROPRIATE PATH

NORMAL
→ EXISTING MAIN WORKFLOW

COMPLEX
→ EXISTING FULL / STRICT WORKFLOW
```

### Important

Jangan mengubah implementasi skill downstream.

Phase 1 hanya menentukan route.

### Acceptance

Semua classification mempunyai route yang deterministik.

---

# TASK-004 — Implement Fast Path Contract

**Type:** AFK
**Priority:** P0
**Depends on:** TASK-003

### Objective

Mendefinisikan behavior Fast Path di dalam `lcs-master`.

### Fast Path

```text
Inspect
→ Change
→ Minimal Verification
→ Report
→ Done
```

### Fast Path must NOT

* generate PRD
* generate SRS
* slice task
* invoke formal review
* expand scope
* perform unrelated cleanup

### Acceptance

TRIVIAL work tidak lagi otomatis diarahkan ke artifact-heavy main flow.

---

# TASK-005 — Implement User Override Rules

**Type:** AFK
**Priority:** P1
**Depends on:** TASK-003

### Objective

Memungkinkan user meminta workflow yang lebih lengkap.

### Example

```text
TRIVIAL
+
"user wants full workflow"
=
FULL WORKFLOW
```

Tetapi:

```text
COMPLEX
+
"user wants shortcut"
≠
FAST PATH
```

### Acceptance

User preference dapat meningkatkan workflow depth tetapi tidak dapat melewati safety boundary.

---

# TASK-006 — Add Classification Output Format

**Type:** AFK
**Priority:** P1
**Depends on:** TASK-003

### Objective

Membuat output classification konsisten dan singkat.

### Format

```text
Work Classification

Class: <TRIVIAL|SMALL|NORMAL|COMPLEX>
Risk: <LOW|MEDIUM|HIGH|CRITICAL>
Ambiguity: <LOW|MEDIUM|HIGH>
Blast Radius: <LOW|MEDIUM|HIGH>

Reason:
<one or two short sentences>

Route:
<route>
```

### Acceptance

Output tidak berubah menjadi long-form analysis.

---

# TASK-007 — Classification Scenario Validation

**Type:** AFK
**Priority:** P0
**Depends on:** TASK-004, TASK-005, TASK-006

### Objective

Memvalidasi behavior classifier terhadap representative cases.

### Required cases

```text
rename
typo
simple bug
new feature
authentication
database migration
security
ambiguous request
explicit full workflow
dangerous shortcut request
```

### Acceptance

Semua scenario pada Section 21 menghasilkan classification dan route yang sesuai.

---

# TASK-008 — Regression Validation

**Type:** AFK
**Priority:** P0
**Depends on:** TASK-007

### Objective

Memastikan routing LCS existing tidak rusak.

### Validate

```text
new feature
bug
huge project
refactor
research
prototype
wayfinder
resume
switch
autopilot
confirmation mode
```

### Acceptance

Tidak ada regression pada existing routing behavior.

---

# TASK-009 — Review and Simplify

**Type:** HITL
**Priority:** P1
**Depends on:** TASK-008

### Objective

Review hasil implementation untuk memastikan Adaptive Routing tidak menjadi sumber complexity baru.

### Review questions

1. Apakah classifier terlalu rumit?
2. Apakah classification membutuhkan terlalu banyak context?
3. Apakah Fast Path benar-benar lebih pendek?
4. Apakah router menjadi lebih lambat?
5. Apakah ada rule yang tumpang tindih?
6. Apakah existing workflow tetap aman?
7. Apakah ada artifact yang tidak diperlukan?
8. Apakah terminology konsisten dengan LCS SOT?

### Acceptance

Human menyetujui:

```text
classification policy
routing behavior
fast path boundary
```

---

# 24. Task Dependency Graph

```text
TASK-001
   ↓
TASK-002
   ↓
TASK-003
   ├────────→ TASK-005
   └────────→ TASK-006
        ↓
TASK-004
        ↓
TASK-007
        ↓
TASK-008
        ↓
TASK-009
```

Secara paralel setelah TASK-003:

```text
             ┌→ TASK-004
TASK-003 ────┼→ TASK-005
             └→ TASK-006
                    ↓
                 TASK-007
```

---

# 25. Definition of Done

Feature ini dianggap selesai apabila:

* [ ] `lcs-master` memiliki Work Classification.
* [ ] Classification memiliki 4 class.
* [ ] Classification mempertimbangkan scope, risk, ambiguity, blast radius.
* [ ] Critical/high-risk work tidak dapat masuk Fast Path.
* [ ] TRIVIAL work memiliki Fast Path.
* [ ] NORMAL work tetap menggunakan main workflow.
* [ ] COMPLEX work tetap menggunakan full workflow.
* [ ] User dapat meminta deeper workflow.
* [ ] User tidak dapat memaksa unsafe downgrade.
* [ ] Classification output ringkas.
* [ ] Scenario validation selesai.
* [ ] Existing routing regression test selesai.
* [ ] Tidak ada perubahan downstream skill.
* [ ] Tidak ada perubahan global contract.
* [ ] Human review terhadap policy selesai.

---

# 26. Expected Result

Setelah Phase 1 selesai, behavior LCS secara konseptual menjadi:

```text
                         USER REQUEST
                              │
                              ▼
                       ┌──────────────┐
                       │ LCS MASTER   │
                       └──────┬───────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ WORK CLASSIFICATION│
                    └─────────┬──────────┘
                              │
          ┌───────────┬───────┼───────────┐
          ▼           ▼       ▼           ▼
       TRIVIAL      SMALL   NORMAL     COMPLEX
          │           │       │           │
          ▼           ▼       ▼           ▼
      FAST PATH    LIGHT    MAIN       FULL
                            FLOW       FLOW
          │           │       │           │
          └───────────┴───────┴───────────┘
                              │
                              ▼
                           VERIFY
                              │
                              ▼
                             DONE
```

---

# 27. Success Metrics

Phase 1 harus diukur berdasarkan **workflow overhead**, bukan hanya correctness.

Target awal:

### Trivial task

```text
Expected:
< 5 minutes total workflow time
```

### Small task

```text
Expected:
significantly lower overhead than full LCS workflow
```

### Normal / Complex

```text
No meaningful degradation of current workflow quality.
```

Metric utama:

```text
Time to implementation
Time to verification
Number of unnecessary workflow stages
Number of artifacts generated
Classification accuracy
Regression rate
```

---

# 28. Future Phase — Explicitly Out of Scope

Setelah Phase 1 terbukti berhasil, barulah Adaptive Policy dapat diteruskan ke:

```text
Phase 2
→ Adaptive Task Executor
```

yang memperkenalkan:

```text
Direct
Normal
TDD
```

kemudian:

```text
Phase 3
→ Adaptive Verification
```

kemudian:

```text
Phase 4
→ Adaptive Code Review
```

dan akhirnya:

```text
Phase 5
→ Full Adaptive LCS
```

Namun **jangan implementasikan phase tersebut sekarang**.

Phase 1 harus membuktikan satu hal terlebih dahulu:

> **LCS dapat memilih workflow yang proporsional terhadap pekerjaan tanpa menurunkan safety dan reliability.**

---

# 29. Source of Truth

Implementation harus menggunakan sumber berikut sebagai acuan:

```text
LCS-SOT.md
skills/lcs-master/SKILL.md
skills/lcs-shared/contract.md
```

Prioritas:

```text
LCS-SOT methodology
        ↓
Current repository implementation
        ↓
This PRD
```

Jika terjadi konflik, jangan mengubah methodology secara diam-diam.

---

# 30. Handoff

**Next recommended skill:** `lcs-task-slicer` atau langsung implementation oleh coding agent menggunakan task list di dokumen ini.

**Implementation starting point:** `TASK-001`

**Primary target:** `skills/lcs-master/SKILL.md`

**Current phase:** PRD / Implementation Ready

**Scope:** `lcs-master` adaptive routing only

**Must preserve:**

* existing LCS routing
* existing confirmation mode
* existing autopilot mode
* existing stop matrix
* existing state management
* existing handoff contract
* existing Chain of Truth concept
* existing human control boundaries

**Must not modify:**

* downstream skills
* shared contract
* global artifact schema
* LCS methodology

**Primary success condition:**

```text
Simple work becomes fast.
Complex work remains rigorous.
```
