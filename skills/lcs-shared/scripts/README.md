# LCS Shared Scripts

## validate-traceability.py (Canonical)

Python script for validating traceability matrix completeness.
Checks SRC-###, FR-###, BR-###, VR-###, EC-###, AC-###, TEST-###, API-###, DB-### cross-references.

```bash
python skills/lcs-shared/scripts/validate-traceability.py --work-item .lcs/work-items/{ts}-{slug}/
```

## validate-traceability.ps1 (Legacy)

PowerShell version of the same validation. Kept for Windows/PowerShell environments.
Python version is canonical — all new features and fixes go to `.py` first.

## validate-okf.py

Validates OKF v0.2 frontmatter in LCS artifact files.

```bash
python skills/lcs-shared/scripts/validate-okf.py .lcs/work-items/{ts}-{slug}/ --strict
```

Checks: required OKF fields, LCS extensions, status lifecycle, timestamps, artifact_type registry.

> **Note:** when scanning a directory, `validate-okf.py` skips subtrees named
> `tests/`, `fixtures/`, `__pycache__`, or `node_modules` so checked-in test
> fixtures never fail a whole-repo scan.

## tests/ — Validator Regression Tests

Automated regression suite for `validate-okf.py` and `validate-traceability.py`.
Pins the F1-F3 fixes (quoted timestamps, optional `type` field, aligned timestamp
regex, registered `artifact_type: state`) so they never silently regress.

```bash
python3 skills/lcs-shared/scripts/tests/test-validators.py
# or as part of the repo suite:
npm test
```

See `tests/README.md` for the fixture matrix.
