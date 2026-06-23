param(
    [string]$WorkItemPath = ""
)

function Read-Text($path) {
    if (Test-Path $path) {
        return Get-Content -Path $path -Raw -Encoding UTF8
    }
    return ""
}

function Get-Ids($text, $pattern) {
    $matches = [regex]::Matches($text, $pattern)
    $result = @()
    foreach ($m in $matches) {
        if ($result -notcontains $m.Value) {
            $result += $m.Value
        }
    }
    return $result
}

function Report($level, $message) {
    Write-Host "$level`: $message"
}

function Find-WorkItem($explicit) {
    if ($explicit) {
        return $explicit
    }
    $state = Read-Text ".lcs/state.md"
    $match = [regex]::Match($state, '\.lcs[\\/]work-items[\\/][A-Za-z0-9._-]+')
    if ($match.Success) {
        return $match.Value
    }
    return $null
}

function Check-ChainOfTruth($text, $label) {
    $failures = @()
    if ($text -match "## Handoff") {
        if ($text -notmatch "(?s)## Chain of Truth Report.*## Handoff") {
            $failures += "$label`: missing Chain of Truth Report before Handoff"
        }
    }
    return $failures
}

function Has-TestMapping($acId, $tests) {
    foreach ($line in ($tests -split "`r?`n")) {
        if (($line -match [regex]::Escape($acId)) -and ($line -match 'TEST-\d{3}')) {
            return $true
        }
    }

    $sections = [regex]::Split($tests, '(?m)(?=^#{2,3}\s+TEST-\d{3}\b)')
    foreach ($section in $sections) {
        if (($section -match [regex]::Escape($acId)) -and ($section -match '(?m)^#{2,3}\s+TEST-\d{3}\b')) {
            return $true
        }
    }

    return $false
}

$failures = @()
$warnings = @()

$workItem = Find-WorkItem $WorkItemPath
if (-not $workItem) {
    Report "FAIL" "Cannot locate active work item from .lcs/state.md. Pass -WorkItemPath explicitly."
    exit 1
}
if (-not (Test-Path $workItem)) {
    Report "FAIL" "Work item path not found: $workItem"
    exit 1
}

$prd = Read-Text "$workItem/prd.md"
$enhanced = Read-Text "$workItem/prd-enhanced.md"
$srs = Read-Text "$workItem/srs.md"
$tests = Read-Text "$workItem/tests.md"
$traceability = Read-Text "$workItem/traceability.md"

$srcIds = Get-Ids $prd "SRC-\d{3}"
$enhancedSrcIds = Get-Ids $enhanced "SRC-\d{3}"
$acIds = Get-Ids $srs "AC-\d{3}"
$frIds = Get-Ids $srs "FR-\d{3}"

if (-not $srcIds) {
    $warnings += "No SRC IDs found in prd.md; legacy workflow allowed but requirement preservation is not enforceable."
}

if ($enhanced) {
    foreach ($srcId in $srcIds) {
        if ($enhancedSrcIds -notcontains $srcId) {
            $failures += "$srcId exists in prd.md but not prd-enhanced.md"
        }
    }
    $failures += Check-ChainOfTruth $enhanced "prd-enhanced.md"
}

foreach ($item in @(@{name="prd.md"; text=$prd}, @{name="srs.md"; text=$srs}, @{name="tests.md"; text=$tests}, @{name="traceability.md"; text=$traceability})) {
    if ($item.text) {
        $failures += Check-ChainOfTruth $item.text $item.name
    }
}

foreach ($acId in $acIds) {
    if ($tests -and -not (Has-TestMapping $acId $tests)) {
        $failures += "$acId has no TEST mapping in tests.md"
    }
}
if ($srs -and -not $tests) {
    $warnings += "srs.md exists but tests.md is missing; AC-to-TEST validation incomplete."
}

$taskDir = "$workItem/task"
$taskTexts = @{}
if (Test-Path $taskDir) {
    $taskFiles = Get-ChildItem "$taskDir/task-*.md" | Sort-Object Name
    foreach ($taskFile in $taskFiles) {
        $taskTexts[$taskFile.Name] = Read-Text $taskFile.FullName
    }
} else {
    $warnings += "task directory missing; AC/FR-to-TASK validation incomplete."
}

foreach ($name in $taskTexts.Keys) {
    $text = $taskTexts[$name]
    if ($text -notmatch '\* \*\*Source coverage\*\*:') {
        $failures += "$name missing Source coverage section"
    }
    $failures += Check-ChainOfTruth $text $name
}

foreach ($reqId in ($acIds + $frIds)) {
    $covered = $false
    foreach ($text in $taskTexts.Values) {
        if ($text -match [regex]::Escape($reqId)) {
            $covered = $true
            break
        }
    }
    if (-not $covered -and $taskTexts.Keys.Count -gt 0) {
        $failures += "$reqId has no TASK coverage"
    }
}

if ($traceability) {
    foreach ($srcId in $srcIds) {
        if ($traceability -notmatch [regex]::Escape($srcId)) {
            $failures += "$srcId missing from traceability.md"
        }
    }
    $failures += Check-ChainOfTruth $traceability "traceability.md"
} elseif ($srcIds.Count -gt 0) {
    $warnings += "traceability.md missing; SRC downstream mapping not fully enforceable."
}

foreach ($w in $warnings) { Report "WARN" $w }
foreach ($f in $failures) { Report "FAIL" $f }

if ($failures.Count -gt 0) {
    exit 1
}
Report "PASS" "Traceability validation passed for $workItem"
exit 0
