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

## Notes

- `validate-okf.py` skips any subtree named `tests/`, `fixtures/`, `__pycache__`,
  or `node_modules` when scanning a directory, so the checked-in invalid fixtures
  never fail a whole-repo scan (e.g. `validate-okf.py skills/`).
- Fixture frontmatter uses realistic timestamps (no `{YYYY-MM-DD}` placeholders)
  so validation is meaningful.
