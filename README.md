# Lean Coding Skills

Collection of small, markdown-first AI skills for lean, focused coding workflows.

Overview
- Skills are packaged under `skills/` as self-contained folders. Each skill is Markdown-first and compatible with Claude/Anthropic style skill loaders. No runtime code or API keys required in the skill files.
- `lcs-explore`: interactive explore flow. Agent/runtime performs iterative question loop and persists results to `.lcs/docs/<timestamp>-<slug-work-item>/explore.md`. See `skills/lcs-explore/SKILL.md` for spec.
- `lcs-toprd`: lean, implementation-focused PRD writer. Agent/runtime creates developer-ready specifications under `.lcs/docs/<timestamp>-<slug-work-item>/prd.md` to limit code reads. See `skills/lcs-toprd/SKILL.md` for spec.

Install (recommended)
Run single command to add skills into a target repo (packager will place files under `.agents/skills`):

PowerShell / Bash (copy-paste):
```
npx skills add https://github.com/mdhb2/lean-coding-skills -a opencode -y
```

Verification
After install, confirm skill present in target repo:

PowerShell (copy-paste):
```
Test-Path .\agents\skills\lcs-explore\SKILL.md
Test-Path .\agents\skills\lcs-toprd\SKILL.md
```

Bash (copy-paste):
```
[ -f .agents/skills/lcs-explore/SKILL.md ] && echo "explore ok"
[ -f .agents/skills/lcs-toprd/SKILL.md ] && echo "toprd ok"
```

Usage after install
- Agent/runtime that supports Claude/Anthropic style skills should load `.agents/skills/lcs-explore` or `.agents/skills/lcs-toprd` and follow the `SKILL.md` instructions to run interactive sessions.

Notes
- Skills are markdown-only. No runtime, no API keys, no Node scripts included in the published skill.
- Persistence (writing `.lcs/docs/*` and `.lcs/state.md`) is the responsibility of the agent/runtime that loads the skill.
- Repo: https://github.com/mdhb2/lean-coding-skills
