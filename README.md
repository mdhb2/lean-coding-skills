# Lean Coding Skills

![LCS](/assets/images/lcs-cover.png)

Collection of small, markdown-first AI skills for lean, focused coding workflows.

## Skills

| Skill | Purpose |
|-------|---------|
| `lcs-explore` | Interactive explore flow for brainstorming and shaping ideas |
| `lcs-toprd` | Lean, implementation-focused PRD writer |
| `lcs-prd-reviewer` | Review, harden, and security-check an existing PRD |
| `lcs-tosrs` | Transform PRD into deterministic Lean SRS and test contract |
| `lcs-task-slicer` | Split a PRD or SRS into actionable, session-sized tasks |
| `lcs-task-executor` | Execute a task plan with Chain of Truth verification (canonical) |
| `lcs-task-executer` | Execute a task plan *(legacy — prefer `lcs-task-executor`)* |
| `lcs-doc-finalizer` | Finalize and wrap completed work into canonical docs |
| `lcs-debug` | Focused bug investigation and fix planning |
| `lcs-debug-ext` | Evidence-based debug reports and patch proposals without applying code changes |
| `lcs-codebase-doc` | Map and document existing repositories into verified onboarding docs |
| `lcs-code-review` | Review implementation against LCS artifacts |
| `lcs-onboarding` | Generate developer-friendly onboarding documentation |
| `lcs-self-improvement` | Analyze interaction friction and produce diagnostic recommendations |
| `lcs-chain-of-truth` | Chain of Truth meta-skill — auditable evidence protocol for all LCS skills |
| `lcs-shared` | Shared contract, folder conventions, and token optimization (internal) |

## Chain of Truth

LCS uses Chain of Truth as a cross-skill protocol for auditable, evidence-backed AI workflows.

### Workflow
```text
lcs-explore (Light)
↓
lcs-toprd (Standard)
↓
lcs-prd-reviewer (Strict)
↓
lcs-tosrs (Strict)
↓
lcs-task-slicer (Strict)
↓
lcs-task-executor (Very Strict)
```
### Level Summary

| Level | Used By |
|---|---|
| Light | lcs-explore |
| Standard | lcs-toprd, lcs-onboarding, lcs-debug, lcs-self-improvement |
| Strict | lcs-prd-reviewer, lcs-tosrs, lcs-task-slicer, lcs-doc-finalizer, lcs-codebase-doc, lcs-code-review |
| Very Strict | lcs-task-executor, lcs-task-executer (legacy), lcs-debug-ext |
| Meta | lcs-chain-of-truth (protocol, not self-applied), lcs-shared (internal) |

### Executor Naming
- **Canonical**: `lcs-task-executor` — use for new workflows
- **Legacy**: `lcs-task-executer` — still works; kept for backward compatibility

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
Test-Path .claude\skills\lcs-debug-ext\SKILL.md
Test-Path .claude\skills\lcs-codebase-doc\SKILL.md
```

## Troubleshooting

- Skills not showing? Confirm `.claude/skills/` exists and contains subfolders with `SKILL.md`.
- Restart Claude Code after install.
- Ensure YAML frontmatter `name` is unique and valid kebab-case.

## Contributing

Add new skill under `skills/<skill-name>/SKILL.md` with frontmatter `name` and `description`. Keep directories self-contained and markdown-only.
