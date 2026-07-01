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

function Check-ArtifactExistence($workItem) {
    $failures = @()
    $indexPath = "$workItem/index.md"
    if (Test-Path $indexPath) {
        $indexContent = Read-Text $indexPath
        $lines = $indexContent -split "`r?`n"
        foreach ($line in $lines) {
            if ($line -match '\|.*\[([^\]]+)\]\(([^)]+)\).*\|') {
                $artifactPath = Join-Path $workItem $matches[2]
                if (-not (Test-Path $artifactPath)) {
                    $failures += "index.md lists $($matches[1]) at $($matches[2]) but file does not exist"
                }
            }
        }
    }
    return $failures
}

function Check-FrontmatterFields($path) {
    $failures = @()
    $content = Read-Text $path
    if ($content -match '^---\s*\n(.*?)\n---') {
        $yaml = $matches[1]
        $required = @("type", "artifact_type", "status", "source", "timestamp")
        foreach ($field in $required) {
            if ($yaml -notmatch "(?m)^$field\s*:") {
                $failures += "$path missing required frontmatter field: $field"
            }
        }
        if ($yaml -match "(?m)^status\s*:\s*(.+)$") {
            $status = $matches[1].Trim()
            if ($status -notmatch '^(draft|review|final)') {
                $failures += "$path invalid status value: $status (expected draft, review, or final)"
            }
        }
        if ($yaml -match "(?m)^timestamp\s*:\s*(.+)$") {
            $ts = $matches[1].Trim()
            if ($ts -notmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$') {
                $failures += "$path invalid timestamp format: $ts (expected ISO 8601)"
            }
        }
    }
    return $failures
}

function Check-TaskVerification($taskDir) {
    $failures = @()
    if (-not (Test-Path $taskDir)) { return $failures }
    $taskFiles = Get-ChildItem "$taskDir/task-*.md" | Sort-Object Name
    foreach ($taskFile in $taskFiles) {
        $text = Read-Text $taskFile.FullName
        if ($text -match '\*\*Status\*\*:\s*done') {
            if ($text -notmatch 'Verif(ication|y)|evidence|Task result') {
                $failures += "$($taskFile.Name) is done but missing verification or execution evidence"
            }
        }
    }
    return $failures
}

function Check-Dependency($taskDir) {
    $failures = @()
    if (-not (Test-Path $taskDir)) { return $failures }
    $taskFiles = Get-ChildItem "$taskDir/task-*.md" | Sort-Object Name
    $statuses = @{}
    foreach ($taskFile in $taskFiles) {
        $text = Read-Text $taskFile.FullName
        if ($text -match '\*\*Status\*\*:\s*(\w+)') {
            $statuses[$taskFile.Name] = $matches[1]
        }
    }
    foreach ($taskFile in $taskFiles) {
        $text = Read-Text $taskFile.FullName
        if ($text -match '\*\*Depends on\*\*:\s*(.+)') {
            $deps = $matches[1]
            foreach ($dep in ($deps -split ',')) {
                $dep = $dep.Trim()
                if ($dep -and $statuses[$dep] -and $statuses[$dep] -ne 'done') {
                    $failures += "$($taskFile.Name) depends on $dep which is not done (status: $($statuses[$dep]))"
                }
            }
        }
    }
    return $failures
}

function Check-ResourcePath($content, $label) {
    $failures = @()
    if ($content -match '^---\s*\n(.*?)\n---') {
        $yaml = $matches[1]
        if ($yaml -match "(?m)^previous_artifact\s*:\s*(.+)$") {
            $path = $matches[1].Trim()
            if ($path -and $path -ne 'optional/path' -and -not (Test-Path $path)) {
                $failures += "$label: previous_artifact path does not exist: $path"
            }
        }
    }
    return $failures
}

function Check-SourcePath($content, $label) {
    $failures = @()
    if ($content -match '^---\s*\n(.*?)\n---') {
        $yaml = $matches[1]
        if ($yaml -match "(?m)^source\s*:\s*(.+)$") {
            $source = $matches[1].Trim()
            if ($source -match '^\.\.[\\/]') {
                $failures += "$label: source field escapes .lcs/ directory: $source"
            }
        }
    }
    return $failures
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

# New validation checks (TASK-004)
$failures += Check-ArtifactExistence $workItem

$artifactNames = @("explore.md", "debug.md", "prd.md", "prd-enhanced.md", "srs.md", "tests.md", "api.md", "db.md", "traceability.md", "task-coverage.md", "final-doc.md", "state.md")
foreach ($name in $artifactNames) {
    $path = Join-Path $workItem $name
    if (Test-Path $path) {
        $content = Read-Text $path
        $failures += Check-FrontmatterFields $path
        $failures += Check-ResourcePath $content $name
        $failures += Check-SourcePath $content $name
    }
}

$failures += Check-TaskVerification "$workItem/task"
$failures += Check-Dependency "$workItem/task"

foreach ($w in $warnings) { Report "WARN" $w }
foreach ($f in $failures) { Report "FAIL" $f }

if ($failures.Count -gt 0) {
    exit 1
}
Report "PASS" "Traceability validation passed for $workItem"
exit 0
