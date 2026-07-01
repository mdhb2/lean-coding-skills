---
type: artifact
artifact_type: code_review
status: final
source: {{active_work_item_path}}
timestamp: {{iso_timestamp}}
resource: {{task_file_or_diff}}
previous_artifact: {{task_file}}
next_artifact: null
---

# LCS Code Review — {{task_title}}

```yaml
okf:
  kind: lcs.code_review
  version: 1.0

review:
  status: "{{review_status}}"
  source_skill: "lcs-code-review"
  previous_skill: "lcs-task-executor"
  reviewed_task: "{{task_id}}"
  highest_severity: "{{highest_severity}}"
  next_recommended_skill: "{{next_skill}}"
```

## Reviewed Sources

Artifacts:
- [ ] explore.md
- [ ] prd.md
- [ ] prd-enhance.md
- [ ] srs.md
- [ ] task-breakdown.md
- [ ] active task
- [ ] acceptance criteria

Code:
- {{code_files}}

Tests:
- Test run: {{test_run}}
- Command: {{test_command}}
- Result: {{test_result}}

## Chain of Truth Compliance

| Source | Status | Notes |
|---|---|---|
| Explore | {{explore_status}} | {{explore_notes}} |
| PRD | {{prd_status}} | {{prd_notes}} |
| PRD Enhance | {{prd_enhance_status}} | {{prd_enhance_notes}} |
| SRS | {{srs_status}} | {{srs_notes}} |
| Task Breakdown | {{task_breakdown_status}} | {{task_breakdown_notes}} |
| Acceptance Criteria | {{ac_status}} | {{ac_notes}} |

## Acceptance Criteria Check

| Criteria | Status | Evidence |
|---|---|---|
| {{ac_criteria}} | {{ac_check_status}} | {{ac_evidence}} |

## Ringkasan

Status: **{{review_status}}**

{{fix_summary_list}}

---

# Daftar Perbaikan

{{fix_entries}}

---

# Execution Order

```yaml
execution_order:
{{execution_order}}
```

Execution sequence:

1. Fix all `P0` issues first.
2. Proceed with `P1`.
3. Re-run `lcs-code-review`.
4. If safe, proceed with `P2`.
5. `P3` may go to optional improvements.

---

# Final Status

```yaml
final:
  review_status: "{{review_status}}"
  total_required_fixes: {{total_required_fixes}}
  total_optional_fixes: {{total_optional_fixes}}
  must_rerun_code_review: {{must_rerun}}
  recommended_next_skill: "{{next_skill}}"
```

Conclusion:

```text
{{conclusion}}
```

## Chain of Truth Report

### Level
Strict

### Sources Checked
{{sources_checked}}

### Assumptions
{{assumptions}}

### Actions Taken
{{actions_taken}}

### Verification
{{verification}}

### Report
{{report_summary}}

## Handoff

Next recommended skill: {{next_skill}}
Next file to read: {{next_file}}
Current phase: code-review
Current confidence: {{confidence}}
Blocking questions: {{blocking_questions}}
Risks to carry forward: {{risks}}
Source of Truth Bundle: {{source_of_truth}}
Must Preserve IDs: {{must_preserve_ids}}
Unresolved IDs: {{unresolved_ids}}
Suggested next command: {{suggested_command}}
