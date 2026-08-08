
## Review Output Format

After review, produce a report saved to `.lcs/work-items/{timestamp}-{slug-work-item}/code-review.md` using the template at `../lcs-code-review/assets/code-review-template.md`.

Copy the template, replace each `{{placeholder}}` with actual content, and write the result.

### Template Fields

| Field | Description | Required |
|---|---|---|
| `{{active_work_item_path}}` | Path to current work item folder | yes |
| `{{iso_timestamp}}` | ISO 8601 timestamp with timezone offset | yes |
| `{{task_file_or_diff}}` | Task file or diff path being reviewed | yes |
| `{{task_file}}` | Previous artifact (task file) | yes |
| `{{task_title}}` | Short title of reviewed task | yes |
| `{{review_status}}` | PASS / PASS_WITH_NOTES / NEEDS_FIX / BLOCKED | yes |
| `{{task_id}}` | Task ID or title | yes |
| `{{highest_severity}}` | P0 / P1 / P2 / P3 / NONE | yes |
| `{{next_skill}}` | Next recommended skill | yes |
| `{{code_files}}` | List of code files reviewed | yes |
| `{{test_run}}` | Yes / No | yes |
| `{{test_command}}` | Test command used | if test_run=Yes |
| `{{test_result}}` | Test output summary | if test_run=Yes |
| `{{explore_status}}` to `{{ac_notes}}` | Chain of Truth compliance per source | yes |
| `{{ac_criteria}}` | List of acceptance criteria | yes |
| `{{ac_check_status}}` | PASS / FAIL / PARTIAL per criteria | yes |
| `{{ac_evidence}}` | Evidence per criteria | yes |
| `{{fix_summary_list}}` | Numbered list of fixes (or empty if PASS) | if NEEDS_FIX |
| `{{fix_entries}}` | Full FIX-### blocks (see FIX template below) | if NEEDS_FIX |
| `{{execution_order}}` | YAML ordered fix list | if NEEDS_FIX |
| `{{total_required_fixes}}` | Count of required fixes | yes |
| `{{total_optional_fixes}}` | Count of optional improvements | yes |
| `{{must_rerun}}` | true / false | yes |
| `{{conclusion}}` | Final conclusion text | yes |
| `{{sources_checked}}` | List of artifacts and code read | yes |
| `{{assumptions}}` | Verified/unverified assumptions | yes |
| `{{actions_taken}}` | Summary of review actions | yes |
| `{{verification}}` | Verification result | yes |
| `{{report_summary}}` | 1-3 sentence summary | yes |
| `{{next_file}}` | Next file for executor to read | yes |
| `{{confidence}}` | low / medium / high | yes |
| `{{blocking_questions}}` | List or None | yes |
| `{{risks}}` | Risks to carry forward | yes |
| `{{source_of_truth}}` | Path to main artifact | yes |
| `{{must_preserve_ids}}` | SRC-### list | yes |
| `{{unresolved_ids}}` | SRC-### list | yes |
| `{{suggested_command}}` | Suggested next action | yes |

### FIX Entry Template

Each FIX entry in `{{fix_entries}}` follows this structure:

```markdown
### FIX-{n} — <title>

**Severity:** `P{n}`
**Target skill:** `<target>`
**Issue type:** `<BUG | REQUIREMENT_GAP | SRS_GAP | TASK_GAP | TEST_GAP | DOC_GAP | SECURITY | DATA_SAFETY>`

#### Problem

```text
Describe the issue briefly.
```

#### Location

```text
File: <path/file>
Area/Function: <function name / component / route>
Related artifact: <prd.md / srs.md / task-coverage.md>
Related requirement: <section / AC / requirement id>
```

#### Expected

```text
Describe the expected behavior based on LCS artifacts.
```

#### Actual

```text
Describe the current implementation behavior.
```

#### Fix Instructions

```text
1. ...
2. ...
```

#### Validation After Fix

```text
- [ ] ...
- [ ] ...
```

#### Fix Request Copy

```markdown
# LCS Fix Request

Target skill: `<target>`

Source review: `FIX-{n}`
