# Codebase Map: Lean Coding Skills (LCS) Pack

## Description
A structured workspace comprising custom LLM Agent Skills designed to enforce systemic, lean, and self-correcting development contracts.

## Key Files
This section lists key files essential to the framework architecture and skill operations.
* **Core Rules & Contracts**:
  - `skills/lcs-shared/contract.md`: Defines the canonical folder structures, artifact specifications, and token optimization rules.
  - `AGENTS.md`: Outlines behavioral constraints, surgical code standards, and Diátaxis specifications.
* **Active Skills**:
  - `skills/lcs-explore/SKILL.md`: Skill definition for initial feature exploration and brainstorming.
  - `skills/lcs-toprd/SKILL.md`: Skill definition for generating developer-friendly, implementation-ready PRDs.
  - `skills/lcs-prd-reviewer/SKILL.md`: Skill definition for security, test-ability, and performance audits on PRDs.
  - `skills/lcs-task-slicer/SKILL.md`: Skill definition for decomposing verified PRDs into atomic task packages.
  - `skills/lcs-task-executer/SKILL.md`: Skill definition to execute and test tasks in Normal or TDD mode.
  - `skills/lcs-doc-finalizer/SKILL.md`: Skill definition for task audits, canonical map/doc reference compilation, and workspace cleanup.
  - `skills/lcs-onboarding/SKILL.md`: Skill definition for codebase structural scans and project onboarding.

## Rationale
* `skills/lcs-shared/contract.md`: Establishes workspace directory boundaries (`.lcs/docs/`) and handoff conventions to maintain persistent state between tool steps.
* `AGENTS.md`: Keeps the AI agent aligned with the team's engineering philosophies, strict testing, and styling conventions.
* `skills/lcs-onboarding/SKILL.md`: Runs automated discovery and outputs index-level onboarding guides for developers entering the repository.

## System Relations
Skills operate as a unified pipeline where the output of one skill (`explore.md` -> `prd.md` -> `prd-enhanced.md` -> `task-###.md`) serves as the strict contract for the next sequential skill, ensuring rigorous alignment from requirements to final verified source code.
