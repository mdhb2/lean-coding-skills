---
title: Implement lcs-master Skill
date: 2026-07-18
priority: high
context: Design captured in .planning/notes/lcs-master-router-design.md
---

# Todo: Implement `lcs-master` Skill

## Goal
Create `skills/lcs-master/SKILL.md` — an active router/orchestrator over all LCS skills.

## Requirements (from design note)
- [ ] Aggressive trigger description (keywords: "start", "begin", "what should I do",
      "route me", ambiguous LCS requests).
- [ ] Two routing modes: confirmation (default) + autopilot (opt-in).
- [ ] Autopilot uses `lcs-explore` first to gather enough context before chaining.
- [ ] Stop matrix bound to Chain of Truth levels (Light/Standard/Strict/Very Strict)
      + cross-level structural-change guard. On stop: write SOT blocker, no prompting.
- [ ] Contract enforcement before every handoff:
      1. path check vs `lcs-shared/contract.md`
      2. exact folder-name == `name:` frontmatter match
- [ ] Decision-log writer → `.lcs/work-items/{ts}-lcs-master/session-log.md`.
- [ ] Declare Chain of Truth level in frontmatter (recommend: Standard — planning/router).
- [ ] Folder name `lcs-master` MUST equal `name:` field.

## Verification
- Load skill, simulate: (a) confirmation mode routes to lcs-explore; (b) autopilot stops
  before lcs-task-executor and writes SOT; (c) routing to a misnamed skill is blocked.
- Run lcs-master eval seed once available.

## Status: DONE (2026-07-18)
- Created `skills/lcs-master/SKILL.md` with: aggressive trigger, confirmation + autopilot
  modes, Stop Matrix bound to CoT levels (from contract.md) + structural-change guard,
  SOT blocker writer, 3 contract-enforcement responsibilities (path / exact-name / decision
  log), Handoff block. Folder name == name: frontmatter verified. chain_of_truth_level:
  Standard declared.
