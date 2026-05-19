# Lean Coding Skills

Collection of small, markdown-only AI skills for lean, focused coding workflows.

Overview
- Skills are packaged under skills/ as self-contained folders. Each skill is Markdown-first and compatible with Claude/Anthropic style skill loaders. No runtime or API keys required in the skill files.
- lcs-explore: interactive explore flow. Agent/runtime performs iterative question loop and persists results to .lcs/docs/<timestamp>-<slug>/explore.md. See skills/lcs-explore/SKILL.md for spec.

Install (recommended)
- Single command installer (preferred):

  npx skills add https://github.com/mdhb2/lean-coding-skills -a opencode -y

Verification
- After install, confirm skill present in target repo:

  PowerShell: Test-Path .\\agents\\skills\\lcs-explore\\SKILL.md
  Bash: [ -f .agents/skills/lcs-explore/SKILL.md ] && echo ok

Usage after install
- Agent/runtime that supports Claude/Anthropic style skills should load .agents/skills/lcs-explore and follow the SKILL.md instructions to run interactive explore sessions.

Notes
- Skills are markdown-only. No runtime, no API keys, no node scripts included.
- Persistence (write .lcs/docs/* and .lcs/state.md) is responsibility of agent/runtime that loads the skill.
- Repo: https://github.com/mdhb2/lean-coding-skills

Notes
- Skill files are markdown-only. Persistence and iterative behaviour implemented by the agent/runtime that installs the skill.
- Repo: https://github.com/mdhb2/lean-coding-skills
