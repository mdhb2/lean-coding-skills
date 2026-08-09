# LCS Installation Guide

## Quick Install (Recommended)

### Install All Skills at Once

If your skill installer supports package-level installation:

```bash
# Install entire skill pack (all 22 skills)
npx skills add https://github.com/mdhb2/lean-coding-skills
```

The repository now includes `package.json` with `skillsConfig.installAll: true`, which signals to compatible installers to auto-select all skills.

### Alternative: Auto-Accept All

If the installer still shows individual selection, use `yes` to auto-accept:

```bash
yes | npx skills add https://github.com/mdhb2/lean-coding-skills
```

### Alternative: Install as Single Entry

Some installers allow installing the repo as a single skill folder:

```bash
npx skills add https://github.com/mdhb2/lean-coding-skills \
  --name "lean-coding-skills" \
  --all-skills
```

## Verify Installation

After installation, check all skills are available:

```bash
# List installed LCS skills
npx skills list | grep "lcs-"

# Expected output (22 skills):
# ✓ lcs-explore
# ✓ lcs-toprd
# ✓ lcs-prd-reviewer
# ✓ lcs-tosrs
# ✓ lcs-task-slicer
# ✓ lcs-task-executor
# ✓ lcs-doc-finalizer
# ✓ lcs-debug
# ✓ lcs-debug-ext
# ✓ lcs-codebase-doc
# ✓ lcs-code-review
# ✓ lcs-improve-architecture
# ✓ lcs-domain-modeling
# ✓ lcs-master
# ✓ lcs-onboarding
# ✓ lcs-prototype
# ✓ lcs-research
# ✓ lcs-self-improvement
# ✓ lcs-chain-of-truth
# ✓ lcs-shared
# ✓ lcs-wayfinder
# ✓ lcs-wizard
```

## Package Metadata

This repository includes `package.json` with:

- `skills`: Array of all 22 skill names
- `skillsConfig.installAll: true`: Hint for installers to auto-select all
- `skillsConfig.skillsDir: "skills"`: Directory containing skills
- `skillsConfig.totalSkills: 22`: Expected skill count

Compatible skill installers can use this metadata to:
1. Detect this is a skill pack (not individual skill)
2. Auto-select all skills by default
3. Verify installation completeness

## Workflow Overview

LCS skills follow this workflow:

```
Exploration → Planning → Review → Specification → Execution → Verification

lcs-explore          ─→  Brainstorm & clarify
lcs-toprd            ─→  Write lean PRD
lcs-prd-reviewer     ─→  Review & harden PRD
lcs-tosrs            ─→  Transform to SRS
lcs-task-slicer      ─→  Slice into tasks
lcs-task-executor    ─→  Execute tasks
lcs-code-review      ─→  Review implementation
lcs-doc-finalizer    ─→  Finalize documentation

Supporting Skills:
lcs-debug, lcs-debug-ext, lcs-codebase-doc, lcs-improve-architecture,
lcs-domain-modeling, lcs-master (router), lcs-onboarding, lcs-prototype,
lcs-research, lcs-self-improvement, lcs-chain-of-truth (meta-protocol),
lcs-shared (internal), lcs-wayfinder, lcs-wizard
```

## Troubleshooting

### Skills not showing up after install

1. Refresh skill list: `npx skills refresh`
2. Check installation directory
3. Verify YAML frontmatter is valid (should be after recent fix)

### Want to install only specific skills

If you don't want all 22 skills:

```bash
# Install manually and deselect unwanted skills during prompt
npx skills add https://github.com/mdhb2/lean-coding-skills
# Uncheck skills you don't need
```

Or install individual skills:

```bash
npx skills add https://github.com/mdhb2/lean-coding-skills/skills/lcs-explore
npx skills add https://github.com/mdhb2/lean-coding-skills/skills/lcs-toprd
# ... etc
```

## Support

- Issues: https://github.com/mdhb2/lean-coding-skills/issues
- Docs: See README.md and AGENTS.md
