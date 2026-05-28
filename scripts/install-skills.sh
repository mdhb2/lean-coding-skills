#!/usr/bin/env bash
# Install LCS skills into local workspace .claude/skills
# Usage: run from repository root in bash

set -euo pipefail
mkdir -p .claude/skills
cp -R skills/* .claude/skills/

echo "Skills copied to .claude/skills/"

if [ -f .claude/skills/lcs-explore/SKILL.md ]; then
  echo "lcs-explore SKILL.md found"
else
  echo "Warning: lcs-explore SKILL.md missing"
fi
