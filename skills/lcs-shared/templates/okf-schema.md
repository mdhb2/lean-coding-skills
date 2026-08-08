# OKF Frontmatter Schema — LCS v1.0

Canonical YAML frontmatter schema for all Lean Coding Skills artifacts.
Based on [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) with LCS-specific extensions.

---

## 1. Field Classification

### OKF Required (wajib di semua artifact)
| Field | Type | Description |
|-------|------|-------------|
| `title` | string | Judul deskriptif artifact |
| `format_version` | string | Selalu `"okf/0.2"` |
| `authors` | list | `[{type: "human"\|"agent", name: "...", id: "..."?}]` |
| `created` | ISO-8601 | `YYYY-MM-DD` atau `YYYY-MM-DDTHH:MM:SSZ` |
| `updated` | ISO-8601 | Terakhir diupdate |

### OKF Recommended (sangat dianjurkan)
| Field | Type | Description |
|-------|------|-------------|
| `tags` | list[string] | Topik/kategori |
| `summary` | string | Satu kalimat ringkasan |
| `status` | enum | `draft` → `active` → `archived` (LCS: tambah `reviewed`) |
| `related` | list[string] | Path ke artifact terkait (relative) |

### LCS Extension (khusus LCS workflow)
| Field | Type | Description |
|-------|------|-------------|
| `artifact_type` | enum | Lihat §2 Artifact Type Registry |
| `artifact_id` | string | ID unik (`SRC-001`, `FR-001`, `AC-001`, `TEST-001`, `task-001`) |
| `source` | string\|list | Path artifact sumber (relative ke work-item) |
| `cot_level` | enum | `light` \| `standard` \| `strict` \| `very_strict` |
| `version` | string | Versi artifact (default `"1.0"`) |

---

## 2. Artifact Type Registry

| Type | File(s) | Skill | Artifact ID Prefix |
|------|---------|-------|--------------------|
| `explore` | explore.md | lcs-explore | — |
| `prd` | prd.md | lcs-toprd | `SRC-###` |
| `prd_enhanced` | prd-enhanced.md | lcs-prd-reviewer | `SRC-###` |
| `srs` | srs.md | lcs-tosrs | `FR-###`, `BR-###`, `VR-###`, `EC-###` |
| `tests` | tests.md | lcs-tosrs | `TEST-###` |
| `api` | api.md | lcs-tosrs | `API-###` |
| `db` | db.md | lcs-tosrs | `DB-###` |
| `traceability` | traceability.md | lcs-tosrs | — |
| `task_coverage` | task-coverage.md | lcs-task-slicer | — |
| `task` | task-###.md | lcs-task-slicer/executor | `task-###` |
| `debug` | debug.md | lcs-debug | `DBG-###` |
| `debug_ext` | debug.md | lcs-debug-ext | — |
| `code_review` | code-review.md | lcs-code-review | — |
| `codebase_doc` | *.md | lcs-codebase-doc | — |
| `onboarding` | onboarding.md | lcs-onboarding | — |
| `onboarding_map` | onboarding-map.md | lcs-onboarding | — |
| `final_doc` | doc.md | lcs-doc-finalizer | — |
| `final_map` | map.md | lcs-doc-finalizer | — |
| `analysis` | {ts}-analysis.md | lcs-self-improvement | — |
| `session_log` | session-log.md | lcs-master | — |
| `domain_model` | CONTEXT.md | lcs-domain-modeling | standard | Domain model and ubiquitous language |
| `research` | research.md | lcs-research | standard | Evidence-based research findings |
| `prototype` | prototype.md | lcs-prototype | strict | Throwaway prototype for design validation |
| `wayfinder` | wayfinder-map.md | lcs-wayfinder | strict | Codebase navigation and decision tickets |
| `wizard` | wizard.sh | lcs-wizard | standard | Human-in-the-loop procedure scripts |

---

## 3. Status Lifecycle

```
draft → reviewed → active → archived
```

| Status | Meaning | Siapa yang set |
|--------|---------|----------------|
| `draft` | Work in progress, belum review | Skill yang membuat |
| `reviewed` | Sudah di-review, mungkin ada catatan | lcs-prd-reviewer, lcs-code-review |
| `active` | Approved, siap di-eksekusi | User approval / lcs-task-executor |
| `archived` | Finalized, tidak boleh diubah | lcs-doc-finalizer |

---

## 4. Template Location

Semua template ada di:
```
skills/lcs-shared/templates/{artifact_type}.template.md
```

Cara pakai:
1. Copy template ke work-item directory
2. Rename sesuai nama file artifact
3. Isi frontmatter fields
4. Tulis konten di bawah frontmatter

---

## 5. Validation

Frontmatter WAJIB parseable YAML. Field wajib (required) harus ada.
Field opsional boleh di-skip.

Required checklist per artifact:
- [ ] `title` ada dan deskriptif
- [ ] `format_version: "okf/0.2"`
- [ ] `authors` minimal 1 entry
- [ ] `created` format ISO-8601
- [ ] `updated` format ISO-8601
- [ ] `artifact_type` sesuai registry
- [ ] `cot_level` sesuai skill yang membuat

---

## 6. OKF Compliance Notes

### Yang LCS ikuti dari OKF v0.2
- ✅ YAML frontmatter di semua artifact
- ✅ Required fields: title, format_version, authors, created, updated
- ✅ Recommended: tags, summary, status, related
- ✅ Author format: {type, name, id?}
- ✅ Status lifecycle (extended: draft → reviewed → active → archived)
- ✅ Extension fields allowed
- ✅ File naming: kebab-case.md
- ✅ Provenance tracking (via source field + Chain of Truth)

### Yang LCS tambah di atas OKF
- `artifact_type` — spesifik ke LCS workflow
- `artifact_id` — traceability identifier
- `source` — explicit upstream reference
- `cot_level` — Chain of Truth level enforcement
