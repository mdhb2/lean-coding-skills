---
title: "Onboarding Guide: {repo-name}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-onboarding"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: onboarding
cot_level: standard
version: "1.0"
status: active
tags: [onboarding, getting-started]
summary: "Developer onboarding guide for {repo-name}"
source: "repository scan, config files"
related: ["onboarding-map.md"]
---

# Onboarding Guide: {repo-name}

## Quick Start
```bash
# Clone
git clone {repo-url}

# Install dependencies
{install command}

# Run
{run command}

# Test
{test command}
```

## Prerequisites
- {Runtime version}
- {Required tools}

## Project Overview
{What this project does in 2-3 sentences.}

## Architecture Snapshot
{Key modules and how they connect. Link to onboarding-map.md for details.}

## Development Workflow
1. {Step 1 — create branch}
2. {Step 2 — make changes}
3. {Step 3 — run tests}
4. {Step 4 — submit PR}

## Common Tasks
### How to add a new {thing}
{Steps}

### How to debug {common issue}
{Steps}

## Key Files
| File | Purpose |
|------|---------|
| {path} | {what it does} |

## Handoff
→ `lcs-toprd` — Start feature development with full context.
