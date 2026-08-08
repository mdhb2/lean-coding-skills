# Lean Coding Skills

![LCS](/assets/images/lcs-cover.png)

Kumpulan skill AI berbasis markdown yang kecil dan fokus untuk alur kerja coding yang lean dan terarah.

- **Bahasa Indonesia:** file ini
- **English:** [README.md](README.md)

## Skills

| Skill | Tujuan |
|-------|--------|
| `lcs-explore` | Alur explore interaktif untuk brainstorming dan membentuk ide |
| `lcs-toprd` | Penulis PRD lean yang fokus ke implementasi |
| `lcs-prd-reviewer` | Review, hardening, dan security-check PRD yang sudah ada |
| `lcs-tosrs` | Transformasi PRD menjadi Lean SRS deterministik + kontrak test |
| `lcs-task-slicer` | Memecah PRD/SRS menjadi task yang actionable dan muat satu sesi |
| `lcs-task-executor` | Mengeksekusi task plan dengan verifikasi Chain of Truth |
| `lcs-doc-finalizer` | Finalisasi dan pembungkusan pekerjaan selesai menjadi docs kanonik |
| `lcs-debug` | Investigasi bug terfokus dan perencanaan perbaikan |
| `lcs-debug-ext` | Laporan debug berbasis bukti + proposal patch tanpa mengubah kode |
| `lcs-codebase-doc` | Memetakan dan mendokumentasikan repo existing menjadi docs onboarding |
| `lcs-code-review` | Review implementasi terhadap artifact LCS |
| `lcs-domain-modeling` | Membangun dan mempertajam domain model proyek (CONTEXT.md, ADR) |
| `lcs-master` | Router/orchestrator kontekstual untuk semua skill LCS |
| `lcs-onboarding` | Membuat dokumentasi onboarding yang ramah developer |
| `lcs-prototype` | Membangun prototype sekali-pakai untuk memvalidasi keputusan desain |
| `lcs-research` | Riset berbasis bukti terhadap sumber primer |
| `lcs-self-improvement` | Analisis friksi interaksi dan rekomendasi diagnostik |
| `lcs-chain-of-truth` | Meta-skill Chain of Truth — protokol bukti teraudit untuk semua skill LCS |
| `lcs-shared` | Kontrak bersama, konvensi folder, optimasi token (internal) |
| `lcs-wayfinder` | Merencanakan pekerjaan besar dengan decision tickets |
| `lcs-wizard` | Membuat script bash interaktif untuk prosedur human-in-the-loop |

## Chain of Truth

LCS memakai Chain of Truth sebagai protokol lintas-skill untuk alur kerja AI yang teraudit dan berbasis bukti.

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

### Ringkasan Level

| Level | Dipakai Oleh |
|---|---|
| Light | lcs-explore |
| Standard | lcs-toprd, lcs-onboarding, lcs-debug, lcs-self-improvement |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc, lcs-code-review |
| Very Strict | lcs-task-executor, lcs-debug-ext |
| Meta | lcs-chain-of-truth (protokol, tidak dipakai sendiri), lcs-shared (internal) |

### Penamaan Executor
- **Kanonik**: `lcs-task-executor` — satu-satunya skill executor

### Artifacts & Frontmatter OKF

Setiap artifact LCS berisi frontmatter YAML OKF v0.2. Kontrak bersama mendaftarkan **28 artifact types** (mis. `prd`, `srs`, `task`, `state`, `index`, `wayfinder`), masing-masing dengan template di `skills/lcs-shared/templates/{artifact_type}.template.md` (27 file template; `execution_log` memakai ulang `session-log.template.md`).

- `state` → `.lcs/state.md` (state sesi, ditulis `lcs-master`)
- `index` → file navigasi/kontrol: `.lcs/docs/docs-index.md` dan `.lcs/docs/self-improvements/index.md`
- **Validator**: `validate-okf.py` (skema frontmatter) dan `validate-traceability.py` / `.ps1` (preservasi SRC)
- Nama file template memakai kebab-case (`code_review` → `code-review.template.md`).

## Dokumentasi Skill & Contoh Skenario

### Skill Alur Utama

#### `lcs-explore` — Brainstorm & Bentuk Ide
Alur tanya-jawab interaktif untuk memperjelas niat, membandingkan trade-off, dan menilai kelayakan sebelum berkomitmen ke PRD.

**Kapan dipakai:** Kamu punya ide fitur yang masih kabur dan perlu dipertajam sebelum merencanakan.

**Skenario:**
> "Saya mau tambah offline mode di app mobile. Explore dulu opsi-opsinya."
> → LCS bertanya satu per satu (target user, strategi sinkronisasi, batas storage), mencatat Q&A dan opsi di `explore.md`, lalu handoff ke `lcs-toprd`.

#### `lcs-toprd` — Penulis PRD Lean
Mensintesis hasil explore, catatan debug, atau requirement langsung menjadi PRD lean yang fokus implementasi: acceptance criteria, strategi test, dan Affected Areas / Files.

**Kapan dipakai:** Kamu siap mendefinisikan apa yang mau dibangun.

**Skenario:**
> "Buat PRD untuk offline mode berdasarkan explore.md."
> → Menghasilkan `prd.md` dengan Source Requirement Ledger (`SRC-###`), acceptance criteria, dan daftar file yang terdampak, lalu handoff ke `lcs-prd-reviewer`.

#### `lcs-prd-reviewer` — Hardening PRD & Security Check
Me-review PRD yang ada untuk acceptance criteria ambigu, test yang hilang, celah security dan performa, lalu menulis `prd-enhanced.md` yang diperkuat sambil menjaga semua `SRC-###`.

**Kapan dipakai:** Kamu ingin tinjauan kedua yang kritis atas PRD sebelum di-slice.

**Skenario:**
> "Review prd.md dan perbaiki menjadi prd-enhanced.md agar siap di-slice."
> → Menghasilkan `prd-enhanced.md` dengan tabel Preservation Check yang membuktikan tidak ada requirement sumber yang hilang.

#### `lcs-tosrs` — PRD → SRS Deterministik
Mengubah PRD (enhanced) menjadi Lean SRS deterministik: `srs.md`, `tests.md`, opsional `api.md` dan `db.md`, plus `traceability.md` yang memetakan `SRC → FR/BR/VR/EC → AC → TEST`.

**Kapan dipakai:** Kamu butuh engineering contract siap-AI dengan requirement yang bisa diuji.

**Skenario:**
> "PRD to SRS — buat spec deterministik dari prd-enhanced.md."
> → Membuat requirement atomik (`FR-###`, `BR-###`, `VR-###`, `EC-###`), coverage matrix test, dan traceability matrix.

#### `lcs-task-slicer` — Memecah Pekerjaan Menjadi Task
Memecah SRS/PRD menjadi vertical slice tracer-bullet kecil yang sadar dependensi, mengklasifikasi `AFK`/`HITL`, lalu menulis `task/task-###.md` plus `task-coverage.md`.

**Kapan dipakai:** Kamu ingin memecah spec yang sudah di-review menjadi langkah eksekusi seukuran satu sesi.

**Skenario:**
> "Slice prd-enhanced.md menjadi task-###.md."
> → Mengonfirmasi granularitas kepadamu, lalu menulis `task-coverage.md` dan satu file per task dengan Source coverage dan dependensi `blocked_by`.

#### `lcs-task-executor` — Eksekusi Satu Task
Mengeksekusi satu `task-###.md` dalam mode Normal atau TDD, menangkap output verifikasi apa adanya (verbatim), dan memperbarui status task serta `.lcs/state.md`.

**Kapan dipakai:** Kamu siap mengimplementasikan task yang sudah di-slice.

**Skenario:**
> "Eksekusi TASK-001."
> → Membaca task dan sumbernya, merekomendasikan mode Normal vs TDD, implementasi, menjalankan validasi, dan mencatat bukti hasil di Chain of Truth Report.

#### `lcs-code-review` — Review Implementasi
Me-review kode hasil eksekusi terhadap artifact LCS (Explore, PRD, SRS, task, AC), memberi severity P0–P3, dan menulis `code-review.md` berisi FIX entries untuk executor.

**Kapan dipakai:** Setelah satu atau beberapa task selesai, sebelum finalisasi.

**Skenario:**
> "Review code hasil eksekusi terhadap artifacts."
> → Menghasilkan laporan terstruktur dengan bukti file:line, status akhir (PASS / PASS_WITH_NOTES / NEEDS_FIX / BLOCKED), dan arahan routing (fix → eksekusi ulang, bersih → finalisasi).

#### `lcs-doc-finalizer` — Finalisasi & Arsip
Mengonsolidasikan pekerjaan selesai ke `.lcs/docs/{ts}-{slug}/` (`map.md` + `doc.md`), memperbarui `docs-index.md`, dan mengarsipkan artifact sumber dengan traceability utuh.

**Kapan dipakai:** Seluruh work item selesai dan butuh docs kanonik + deskripsi PR.

**Skenario:**
> "Selesaikan dokumentasi untuk offline-mode."
> → Memverifikasi semua task `done`, membuat `doc.md` + `map.md`, menyalin `code-review.md` berdampingan, dan mengarsipkan `.lcs/work-items/`.

### Skill Pendukung

#### `lcs-debug` — Investigasi Bug Terfokus
Menyelidiki bug lewat klarifikasi satu pertanyaan per langkah, lalu menulis hipotesis dan rencana investigasi ke `debug.md` (tanpa perbaikan sampai akar masalah jelas). Memakai 6-fase loop disiplin yang wajib.

**Kapan dipakai:** Kamu punya bug, test gagal, error, atau regresi.

**Skenario:**
> "Ada bug: login selalu timeout setelah 30 detik."
> → Membangun feedback loop yang bisa RED dulu, lalu mereproduksi, berhipotesis, dan merencanakan perbaikan — tanpa menebak.

#### `lcs-debug-ext` — Laporan Debug Berbasis Bukti
Menghasilkan diagnosis report-only: ringkasan bukti, hipotesis falsifiable berperingkat, saran instrumentasi, dan proposal patch — **tanpa mengubah kode sama sekali**.

**Kapan dipakai:** Kamu butuh diagnosis dan proposal patch untuk ditinjau sebelum ada edit apa pun.

**Skenario:**
> "Diagnose test yang flaky ini tapi jangan edit file — buat laporannya."
> → Menulis `.lcs/work-items/{ts}-{slug}-debug-ext/debug.md` dengan keterangan `Changes applied: None`.

#### `lcs-codebase-doc` — Petakan Codebase Existing
Memetakan repo menjadi tujuh dokumen berbasis bukti di `.lcs/codebase/` (STACK, STRUCTURE, ARCHITECTURE, CONVENTIONS, INTEGRATIONS, TESTING, CONCERNS) plus laporan Chain of Truth.

**Kapan dipakai:** Kamu perlu memahami atau onboarding ke repo yang belum dikenal.

**Skenario:**
> "Map this codebase — saya mau paham arsitekturnya dulu."
> → Menanyakan pilihan mode (Quick Update / Standard Refresh / Rebuild), memindai repo, dan menghasilkan dokumentasi terverifikasi dengan path bukti.

#### `lcs-domain-modeling` — Ubiquitous Language
Membangun dan mempertajam domain model proyek: menantang istilah yang kabur, menyelesaikan kosakata yang tumpang tindih, dan memperbarui `CONTEXT.md` (plus ADR saat keputusan sulit dibatalkan).

**Kapan dipakai:** Istilah ambigu atau melenceng, misal "user" punya tiga arti berbeda.

**Skenario:**
> "Kita pakai istilah 'user' untuk auth dan billing — bedain dulu."
> → Mengusulkan istilah kanonik yang presisi, memperbarui `CONTEXT.md` inline, dan menandai kontradiksi dengan kode yang sebenarnya.

#### `lcs-research` — Riset Berbasis Bukti
Menyelidiki pertanyaan terhadap sumber primer tepercaya dan menulis temuan bercitation ke `.lcs/work-items/{ts}-{slug}/research/<topic>.md`.

**Kapan dipakai:** Kamu butuh fakta sebelum keputusan (dokumentasi API, perbandingan library, review RFC).

**Skenario:**
> "Research: bandingkan JWT vs session cookies untuk auth di Node.js."
> → Menjalankan investigasi latar belakang, menelusuri setiap klaim ke sumber primernya, dan mengembalikan temuan dengan URL dan nomor baris yang persis.

#### `lcs-prototype` — Prototype Sekali-Pakai
Membangun kode sekali-pakai yang terisolasi untuk menjawab pertanyaan desain tertentu (cabang LOGIC atau UI), lalu melipat keputusan tervalidasi kembali ke spec asli.

**Kapan dipakai:** Kamu ingin memvalidasi pendekatan sebelum berkomitmen.

**Skenario:**
> "Apakah logika state machine ini sudah benar? Bikin prototype dulu."
> → Membuat prototype di `.lcs/work-items/{ts}-{slug}/prototype/`, memvalidasi keputusan, dan meninggalkan context pointer di PRD/SRS.

#### `lcs-wayfinder` — Rencana Pekerjaan Besar
Merencanakan pekerjaan multi-sesi yang besar dengan peta navigasi dan decision tickets (`DEC-###`), diselesaikan satu ticket per sesi sampai peta jelas.

**Kapan dipakai:** Proyek terlalu besar atau belum jelas untuk satu sesi.

**Skenario:**
> "Refactor monolith jadi modular — ini proyek multi-week. Wayfinder dulu."
> → Menjalankan sesi grilling untuk menamai tujuan, memetakan frontier, menulis `wayfinder-map.md` + decision tickets, lalu handoff ke `lcs-toprd` saat sudah jelas.

#### `lcs-wizard` — Script Human-in-the-Loop
Membuat script bash interaktif untuk prosedur manual (setup infra, kredensial, migrasi), memakai helper `template.sh` (`stage`, `open_url`, `ask_secret`, `write_env`).

**Kapan dipakai:** Prosedur butuh manusia untuk klik di console atau memasukkan secret.

**Skenario:**
> "Buat wizard script untuk setup AWS credentials."
> → Memetakan langkah dan variabel persis, menulis `scripts/<name>-wizard.sh`, memverifikasi dengan `bash -n` + `shellcheck`, lalu handoff untuk eksekusi manual.

#### `lcs-onboarding` — Dokumen Onboarding Developer
Membuat laporan onboarding lean (`onboarding.md`) dan peta struktur (`onboarding-map.md`) untuk proyek existing.

**Kapan dipakai:** Engineer baru perlu cepat paham proyek yang berjalan.

**Skenario:**
> "Buat dokumentasi onboarding untuk repo ini."
> → Memindai file konfigurasi, mengekstrak stack, entrypoint, perintah setup/run/test, dan menulis dua dokumen singleton di `.lcs/work-items/`.

#### `lcs-self-improvement` — Analisis Friksi
Menganalisis konteks percakapan/sesi untuk mengidentifikasi pola friksi dan merekomendasikan perbaikan — murni diagnostik, tidak ada perubahan yang diterapkan otomatis.

**Kapan dipakai:** Kamu ingin memperbaiki perilaku agent atau kualitas skill dari waktu ke waktu.

**Skenario:**
> "Review apa yang salah di sesi kemarin, generate self-improvement recommendations."
> → Menulis `.lcs/docs/self-improvements/{ts}-analysis.md`, melacak siklus hidup rekomendasi di `state.json`, dan mendeduplikasi item yang berulang.

### Skill Meta

#### `lcs-chain-of-truth` — Protokol Bukti Teraudit
Meta-skill protokol yang disuntikkan ke semua skill LCS: setiap artifact menampilkan bukti teraudit (Source → Assumption → Plan → Action → Verification → Report) alih-alih penalaran tersembunyi. Mendeklarasikan level per skill: Light, Standard, Strict, atau Very Strict.

**Kapan dipakai:** Otomatis aktif di dalam setiap skill LCS yang menghasilkan artifact untuk dikomit atau dirilis.

#### `lcs-master` — Router / Orchestrator Kontekstual
Titik masuk tunggal yang menganalisis niat, mengenali situasi awal (on-ramps), merutekan ke skill yang tepat dengan panduan kontekstual kaya, dan menegakkan kontrak bersama di setiap handoff. Berjalan dalam mode konfirmasi (default) atau mode autopilot.

**Kapan dipakai:** Kamu tidak yakin skill LCS mana yang cocok, atau ingin memulai workflow dari nol.

**Skenario:**
> "Start LCS workflow — saya mau build fitur baru."
> → Menjalankan precondition check, mengenali on-ramp alur utama, merekomendasikan `lcs-explore`, dan mencatat keputusan routing.

**Skenario (on-ramp):**
> "There's a bug in production."
> → Merutekan ke `lcs-debug` dengan peringatan kritis bahwa Phase 1 (membangun feedback loop yang bisa RED) harus selesai sebelum berhipotesis.

#### `lcs-shared` — Kontrak Bersama (Internal)
Resource internal berisi konvensi folder kanonik, skema frontmatter OKF, format Handoff, registry artifact, dan aturan optimasi token yang dipakai setiap skill. Tidak diterapkan pada dirinya sendiri.

**Kapan dipakai:** Baca sebagai referensi saat memperluas LCS atau men-debug konvensi artifact.

## Rilis

| Tag | Ringkasan |
|-----|-----------|
| `v2.2` | Penyelarasan lifecycle OKF: ticket DEC wayfinder kini memakai `status: active/archived` di frontmatter; `artifact_type: index` didaftarkan untuk file navigasi (`docs-index.md`, `index.md`) dengan frontmatter OKF lengkap; penyelarasan validator (timestamp ber-quote, frontmatter tanpa `type`, date-only) plus PowerShell parity runner untuk `validate-traceability.ps1`. |
| `v2.1` | Kepatuhan Chain of Truth untuk semua skill, `lcs-task-executer` deprecated demi `lcs-task-executor`, artifact types dan template baru, helper template `lcs-wizard` (`template.sh`), routing evals diperluas, README-ID.md. |

## Instalasi

```
npx skills add https://github.com/mdhb2/lean-coding-skills
```

Pilih **claudecode** saat diminta. Restart Claude Code setelah instalasi.

## Pembaruan

```
npx skills update -y
```

## Verifikasi

Setelah instalasi, pastikan skill tersedia:

```
Test-Path .claude\skills\lcs-explore\SKILL.md
Test-Path .claude\skills\lcs-toprd\SKILL.md
Test-Path .claude\skills\lcs-tosrs\SKILL.md
Test-Path .claude\skills\lcs-debug-ext\SKILL.md
Test-Path .claude\skills\lcs-codebase-doc\SKILL.md
```

## Troubleshooting

- Skill tidak muncul? Pastikan `.claude/skills/` ada dan berisi subfolder dengan `SKILL.md`.
- Restart Claude Code setelah instalasi.
- Pastikan frontmatter YAML `name` unik dan kebab-case valid.

## Kontribusi

Tambahkan skill baru di bawah `skills/<skill-name>/SKILL.md` dengan frontmatter `name` dan `description`. Jaga direktori tetap self-contained dan markdown-only. Saat menambah skill, perbarui juga:
- Tabel skill di `README.md` / `README-ID.md`
- Inventori skill `AGENTS.md` §9
- Registry artifact di `skills/lcs-shared/contract.md`
- `CANONICAL_LEVELS` di `scripts/validate-skills.js`

Saat menambah atau mengganti nama artifact type, perbarui juga:
- Jumlah artifact type di section *Artifacts & Frontmatter OKF* kedua README
- Tabel *Rilis* di kedua README (bump tag + ringkasan)
