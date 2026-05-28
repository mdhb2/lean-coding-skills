# Install LCS skills into local workspace .claude/skills
# Usage: run from repository root in PowerShell

# Create target dir
New-Item -ItemType Directory -Force .claude\skills | Out-Null

# Copy skills folder contents into .claude/skills
Copy-Item -Path "skills\*" -Destination ".claude\skills\" -Recurse -Force

Write-Host "Skills copied to .claude/skills/" -ForegroundColor Green

# Verify
if (Test-Path ".claude\skills\lcs-explore\SKILL.md") {
    Write-Host "lcs-explore SKILL.md found" -ForegroundColor Green
} else {
    Write-Host "Warning: lcs-explore SKILL.md missing" -ForegroundColor Yellow
}
