# Lean Coding Skills

![LCS](/assets/images/lcs-cover.png)

Collection of small, markdown-first AI skills for lean, focused coding workflows.

Overview
- Skills are packaged under `skills/` as self-contained folders. Each skill is Markdown-first and compatible with Claude/Anthropic style skill loaders. No runtime code or API keys required in the skill files.
- `lcs-explore`: interactive explore flow. Agent/runtime performs iterative question loop and persists results to `.lcs/docs/<timestamp>-<slug-work-item>/explore.md`. See `skills/lcs-explore/SKILL.md` for spec.
- `lcs-toprd`: lean, implementation-focused PRD writer. Agent/runtime creates developer-ready specifications under `.lcs/docs/<timestamp>-<slug-work-item>/prd.md` to limit code reads. See `skills/lcs-toprd/SKILL.md` for spec.
- `lcs-prd-reviewer`: review, harden, and security-check an existing PRD. Agent writes output to `.lcs/docs/<timestamp>-<slug-work-item>/prd-enhanced.md`. See `skills/lcs-prd-reviewer/SKILL.md` for spec.
- `lcs-task-slicer`: split a reviewed PRD into actionable, session-sized tasks. Agent writes output to `.lcs/docs/<timestamp>-<slug-work-item>/task/task-###.md`. See `skills/lcs-task-slicer/SKILL.md` for spec.
- `lcs-task-executer`: execute the selected task plan and update status to done. See `skills/lcs-task-executer/SKILL.md` for spec.
- `lcs-doc-finalizer`: finalize and wrap completed work into canonical documentation (map.md and doc.md) under `.lcs/docs/reff/<timestamp>-<slug-work-item>/`. See `skills/lcs-doc-finalizer/SKILL.md` for spec.
- `lcs-onboarding`: generate developer-friendly onboarding documentation (`onboarding.md` and `onboarding-map.md`) under `.lcs/docs/`. See `skills/lcs-onboarding/SKILL.md` for spec.

Install (recommended)

Single command (packager):
```
# installs and registers skills for Claude Code adapter
npx skills add https://github.com/mdhb2/lean-coding-skills -a claudecode -y
```

After install, restart Claude Code/agent runtime so it reloads `.agents/skills`.

Update
To update the skills to the latest version, run:

PowerShell / Bash (copy-paste):
```
npx skills update -y
```

Verification
After install, confirm skill present in target repo:

PowerShell (copy-paste):
```
Test-Path .\agents\skills\lcs-explore\SKILL.md
Test-Path .\agents\skills\lcs-toprd\SKILL.md
Test-Path .\agents\skills\lcs-prd-reviewer\SKILL.md
Test-Path .\agents\skills\lcs-task-slicer\SKILL.md
Test-Path .\agents\skills\lcs-task-executer\SKILL.md
Test-Path .\agents\skills\lcs-doc-finalizer\SKILL.md
Test-Path .\agents\skills\lcs-onboarding\SKILL.md
```

Bash (copy-paste):
```
[ -f .agents/skills/lcs-explore/SKILL.md ] && echo "explore ok"
[ -f .agents/skills/lcs-toprd/SKILL.md ] && echo "toprd ok"
[ -f .agents/skills/lcs-prd-reviewer/SKILL.md ] && echo "reviewer ok"
[ -f .agents/skills/lcs-task-slicer/SKILL.md ] && echo "slicer ok"
[ -f .agents/skills/lcs-task-executer/SKILL.md ] && echo "executer ok"
[ -f .agents/skills/lcs-doc-finalizer/SKILL.md ] && echo "finalizer ok"
[ -f .agents/skills/lcs-onboarding/SKILL.md ] && echo "onboarding ok"
```

Usage after install
- Agent/runtime that supports Claude/Anthropic style skills should load `.agents/skills/lcs-explore` or `.agents/skills/lcs-toprd` and follow the `SKILL.md` instructions to run interactive sessions.

Notes
- Skills are markdown-only. No runtime, no API keys, no Node scripts included in the published skill.
- Persistence (writing `.lcs/docs/*` and `.lcs/state.md`) is the responsibility of the agent/runtime that loads the skill.
- Repo: https://github.com/mdhb2/lean-coding-skills


Claude Code / Local install: make skills detectable and installable
- Claude Code and similar agent-runtimes expect skills under `.agents/skills/<skill-name>/SKILL.md`.
- You can install pack into local workspace by copying `skills/` into `.agents/skills/`.

PowerShell (run in repo root):
```
New-Item -ItemType Directory -Force .agents\skills
Copy-Item -Path "skills\*" -Destination ".agents\skills\" -Recurse -Force
```

Bash (run in repo root):
```
mkdir -p .agents/skills && cp -R skills/* .agents/skills/
```

Quick install scripts
- scripts/install-skills.ps1: PowerShell installer to copy skills into `.agents/skills`.
- scripts/install-skills.sh: Bash installer for POSIX shells.

Verification after local install
- PowerShell:
```
Test-Path .\agents\skills\lcs-explore\SKILL.md
```
- Bash:
```
[ -f .agents/skills/lcs-explore/SKILL.md ] && echo "lcs-explore installed"
```

Make pack manager friendly
- Ensure each skill folder contains `SKILL.md` with YAML frontmatter `name` and `description` (already present under `skills/*/SKILL.md`).
- Optional: add `SKILLPACK.md` or repository README (this file) so packagers can surface list of skills and metadata.

Troubleshooting
- If Claude Code does not show skills: confirm `.agents/skills` exists and contains subfolders with `SKILL.md`; restart Claude Code/agent runtime; check runtime logs for skill-loader errors.
- If a skill is not loaded, open `.agents/skills/<skill>/SKILL.md` and ensure YAML frontmatter `name` is unique and valid (kebab-case recommended).

Contributing
- Add new skill under `skills/<skill-name>/SKILL.md` with frontmatter `name` and `description`.
- Keep skill directories self-contained and markdown-only.


Generated files in this repo
- scripts/install-skills.ps1
- scripts/install-skills.sh


