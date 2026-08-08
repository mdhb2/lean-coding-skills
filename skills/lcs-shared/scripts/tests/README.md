# Validator Regression Tests

Automated regression suite for `validate-okf.py` and `validate-traceability.py`.

## Why

Fixes F1-F3 (quote-stripping, aligned required fields/timestamp regex, `artifact_type:
state` registration) must not silently regress. These fixtures pin the expected
behaviour so `npm test` catches a breakage automatically.

## Run

```bash
python3 skills/lcs-shared/scripts/tests/test-validators.py
# or, as part of the repo test suite:
npm test
```

## Fixtures

### `fixtures/okf/`
| Fixture | Expected | Pins |
|---|---|---|
| `valid-quoted-timestamp.md` | exit 0 | F1: quoted `timestamp` value accepted |
| `valid-no-type.md` | exit 0 | review fix: `type` field optional |
| `valid-date-only.md` | exit 0 | aligned regex: date-only `YYYY-MM-DD` accepted |
| `valid-state.md` | exit 0 | F3: `artifact_type: state` registered |
| `invalid-unknown-type.md` | exit non-zero | registry: unknown type rejected |
| `invalid-bad-status.md` | exit non-zero | lifecycle: `pending` rejected |

### `fixtures/traceability/`
- `valid/` — complete work item that must PASS: quoted timestamps, artifacts
  without `type`, a date-only timestamp (`task-coverage.md`), task dependency
  chain (`task-002 -> task-001`, `task-003 -> task-002`), done tasks with
  verification evidence, full SRC/FR/AC/TEST preservation.
- `invalid-missing-ac-test/` — work item where `AC-002` has no TEST mapping in
  `tests.md`; must FAIL with exactly that finding.

These two fixtures are **shared by both validators**: the Python runner feeds
`fixtures/traceability/valid` and `.../invalid-missing-ac-test` to
`validate-traceability.py`, and `test-traceability-ps1.ps1` feeds the very same
paths to the legacy `validate-traceability.ps1`. This enforces parity: if one
validator is changed without the other, the shared fixture suite catches it on
the platform where PowerShell runs.

### `test-traceability-ps1.ps1`

PowerShell runner (Windows PowerShell 5+ or `pwsh` on any OS) for the legacy
validator, reusing the same traceability fixtures as the Python suite. Called
automatically by `test-validators.py` when `pwsh`/`powershell` is on `PATH`;
otherwise it prints `[SKIP]` so the suite still passes on hosts without
PowerShell. Run it manually with:

```bash
pwsh -File skills/lcs-shared/scripts/tests/test-traceability-ps1.ps1
```

## Notes

- `validate-okf.py` skips any subtree named `tests/`, `fixtures/`, `__pycache__`,
  or `node_modules` when scanning a directory, so the checked-in invalid fixtures
  never fail a whole-repo scan (e.g. `validate-okf.py skills/`).
- Fixture frontmatter uses realistic timestamps (no `{YYYY-MM-DD}` placeholders)
  so validation is meaningful.
- `validate-traceability.ps1` mirrors the Python validator's fixes: quote
  stripping on `status`/`timestamp`/`source`/`previous_artifact`, OKF status
  lifecycle (`draft|reviewed|active|archived`), the shared timestamp regex
  (date-only / `Z` / offset), `type` as an optional field, and `state.md`
  excluded from the work-item frontmatter scan.
