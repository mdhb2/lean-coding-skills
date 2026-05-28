#!/usr/bin/env bash
# Install LCS skills into local workspace .agents/skills
# Usage: run from repository root in bash

set -euo pipefail
mkdir -p .agents/skills
cp -R skills/* .agents/skills/

echo "Skills copied to .agents/skills/"

if [ -f .agents/skills/lcs-explore/SKILL.md ]; then
  echo "lcs-explore SKILL.md found"
else
  echo "Warning: lcs-explore SKILL.md missing"
fi
