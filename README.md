# Lean Coding Skills

![LCS](/assets/images/lcs-cover.png)

Collection of small, markdown-first AI skills for lean, focused coding workflows.

## Skills

| Skill | Purpose |
|-------|---------|
| `lcs-onboarding` | Generate developer-friendly onboarding documentation |
| `lcs-explore` | Interactive explore flow for brainstorming and shaping ideas |
| `lcs-toprd` | Lean, implementation-focused PRD writer |
| `lcs-prd-reviewer` | Review, harden, and security-check an existing PRD |
| `lcs-tosrs` | Transform PRD into deterministic Lean SRS and test contract |
| `lcs-task-slicer` | Split a reviewed PRD into actionable, session-sized tasks |
| `lcs-task-executer` | Execute a task plan and update status to done |
| `lcs-doc-finalizer` | Finalize and wrap completed work into canonical docs |
| `lcs-debug` | Focused bug investigation and fix planning |

## Install

```
npx skills add https://github.com/mdhb2/lean-coding-skills
```

Select **claudecode** when prompted. Restart Claude Code after install.

## Update

```
npx skills update -y
```

## Verify

After install, confirm skills are present:

```
Test-Path .claude\skills\lcs-explore\SKILL.md
Test-Path .claude\skills\lcs-toprd\SKILL.md
Test-Path .claude\skills\lcs-tosrs\SKILL.md
```

## Troubleshooting

- Skills not showing? Confirm `.claude/skills/` exists and contains subfolders with `SKILL.md`.
- Restart Claude Code after install.
- Ensure YAML frontmatter `name` is unique and valid kebab-case.

## Contributing

Add new skill under `skills/<skill-name>/SKILL.md` with frontmatter `name` and `description`. Keep directories self-contained and markdown-only.
