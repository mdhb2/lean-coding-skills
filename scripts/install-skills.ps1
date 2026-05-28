# Install LCS skills into local workspace .agents/skills
# Usage: run from repository root in PowerShell

# Create target dir
New-Item -ItemType Directory -Force .agents\skills | Out-Null

# Copy skills folder contents into .agents/skills
Copy-Item -Path "skills\*" -Destination ".agents\skills\" -Recurse -Force

Write-Host "Skills copied to .agents/skills/" -ForegroundColor Green

# Verify
if (Test-Path ".agents\skills\lcs-explore\SKILL.md") {
    Write-Host "lcs-explore SKILL.md found" -ForegroundColor Green
} else {
    Write-Host "Warning: lcs-explore SKILL.md missing" -ForegroundColor Yellow
}
