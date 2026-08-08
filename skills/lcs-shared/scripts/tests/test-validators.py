#!/usr/bin/env python3
"""Regression tests for validate-okf.py and validate-traceability.py.

Runs both validators against checked-in fixtures and asserts the expected
exit codes. Exits 0 when everything passes, non-zero on regression.

Usage:
    python3 skills/lcs-shared/scripts/tests/test-validators.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent  # .../skills/lcs-shared/scripts/tests
REPO = HERE.parents[3]  # scripts/tests -> scripts -> lcs-shared -> skills -> repo root
FIXTURES = HERE / "fixtures"
VALIDATE_OKF = REPO / "skills/lcs-shared/scripts/validate-okf.py"
VALIDATE_TRACE = REPO / "skills/lcs-shared/scripts/validate-traceability.py"
PS1_RUNNER = HERE / "test-traceability-ps1.ps1"


def find_powershell() -> str | None:
    """Return the PowerShell executable if available (pwsh on non-Windows, else powershell)."""
    for name in ("pwsh", "powershell"):
        path = shutil.which(name)
        if path:
            return path
    return None


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def check(name: str, cmd: list[str], expect_ok: bool) -> bool:
    code, output = run(cmd)
    ok = (code == 0) if expect_ok else (code != 0)
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name} (exit={code}, expected {'0' if expect_ok else 'non-zero'})")
    if not ok:
        print(f"        output: {output[:400]}")
    return ok


def main() -> int:
    failures = 0

    print("=== validate-okf.py fixtures ===")
    okf_valid = [
        "valid-quoted-timestamp.md",
        "valid-no-type.md",
        "valid-date-only.md",
        "valid-state.md",
        "valid-index.md",
    ]
    okf_invalid = [
        "invalid-unknown-type.md",
        "invalid-bad-status.md",
    ]
    for f in okf_valid:
        if not check(f"okf: {f}", [sys.executable, str(VALIDATE_OKF), str(FIXTURES / "okf" / f)], expect_ok=True):
            failures += 1
    for f in okf_invalid:
        if not check(f"okf: {f}", [sys.executable, str(VALIDATE_OKF), str(FIXTURES / "okf" / f)], expect_ok=False):
            failures += 1

    print()
    print("=== validate-traceability.py fixtures ===")
    if not check(
        "trace: valid work item (quoted ts, no type, date-only, deps)",
        [sys.executable, str(VALIDATE_TRACE), "--work-item", str(FIXTURES / "traceability" / "valid")],
        expect_ok=True,
    ):
        failures += 1
    if not check(
        "trace: invalid work item (AC-002 missing TEST mapping)",
        [sys.executable, str(VALIDATE_TRACE), "--work-item", str(FIXTURES / "traceability" / "invalid-missing-ac-test")],
        expect_ok=False,
    ):
        failures += 1

    print()
    print("=== cross-consistency: okf must also accept the valid work item dir ===")
    if not check(
        "okf: valid work item dir scans clean",
        [sys.executable, str(VALIDATE_OKF), str(FIXTURES / "traceability" / "valid")],
        expect_ok=True,
    ):
        failures += 1

    print()
    print("=== validate-traceability.ps1 (legacy) parity fixtures ===")
    pwsh = find_powershell()
    if pwsh:
        code, output = run([pwsh, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(PS1_RUNNER)])
        print(output)
        if code != 0:
            print(f"[FAIL] ps1 runner exited {code} (expected 0)")
            failures += 1
    else:
        print("[SKIP] PowerShell (pwsh/powershell) not found on this host; PS1 parity checks skipped.")
        print("        Run test-traceability-ps1.ps1 on a Windows host or with pwsh installed.")

    print()
    if failures:
        print(f"RESULT: {failures} check(s) FAILED")
        return 1
    print("RESULT: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
