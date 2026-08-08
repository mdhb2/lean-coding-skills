# Regression tests for validate-traceability.ps1 (legacy PowerShell validator).
#
# Reuses the SAME fixtures as the Python suite (fixtures/traceability/valid and
# fixtures/traceability/invalid-missing-ac-test) so parity with the canonical
# Python validator is enforced. Run on any host with PowerShell 5+ or pwsh.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File tests/test-traceability-ps1.ps1
#   pwsh -File skills/lcs-shared/scripts/tests/test-traceability-ps1.ps1
#
# Exit code: 0 = all checks passed, 1 = regression detected.
param()

$ErrorActionPreference = "Stop"

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
# tests -> scripts -> lcs-shared -> skills -> repo root (4 levels up)
$Repo = Resolve-Path (Join-Path $Here "../../../..")
$ValidateTrace = Join-Path $Repo "skills/lcs-shared/scripts/validate-traceability.ps1"
$Fixtures = Join-Path $Here "fixtures/traceability"
# Use the PowerShell executable that is running this script (works for both
# Windows PowerShell and pwsh), so the validator runs in a child process whose
# exit code we can read via $LASTEXITCODE without terminating this runner.
$PSExe = (Get-Process -Id $PID).Path

$failures = 0

function Run-Check {
    param(
        [string]$Name,
        [string]$WorkItem,
        [bool]$ExpectOk
    )
    $output = & $PSExe -NoProfile -ExecutionPolicy Bypass -File $ValidateTrace -WorkItemPath $WorkItem 2>&1
    $code = $LASTEXITCODE
    $ok = ($code -eq 0) -eq $ExpectOk
    $status = if ($ok) { "PASS" } else { "FAIL" }
    Write-Host "[$status] $Name (exit=$code, expected $(if ($ExpectOk) { '0' } else { 'non-zero' }))"
    if (-not $ok) {
        Write-Host ($output | Select-Object -First 8)
    }
    if (-not $ok) {
        $script:failures++
    }
}

Write-Host "=== validate-traceability.ps1 fixtures ==="
Run-Check -Name "ps1: valid work item (quoted ts, no type, date-only, deps)" -WorkItem (Join-Path $Fixtures "valid") -ExpectOk $true
Run-Check -Name "ps1: invalid work item (AC-002 missing TEST mapping)" -WorkItem (Join-Path $Fixtures "invalid-missing-ac-test") -ExpectOk $false

Write-Host ""
if ($script:failures -gt 0) {
    Write-Host "RESULT: $script:failures check(s) FAILED"
    exit 1
}
Write-Host "RESULT: all PS1 checks passed"
exit 0
