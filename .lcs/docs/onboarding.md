# Project Onboarding: Lean Coding Skills (LCS) Pack

## 1. Overview
- **Language & Stack**: Markdown, Shell/Powershell script wrappers, AI Agent Skills configuration.
- **Core Purpose**: A structured, lean framework and contract for AI-assisted development sessions. It implements systematic workflows from feature exploration, PRD review, task slicing, task execution, to final documentation review.
- **Key Entrypoints**:
  - `skills/lcs-shared/contract.md`: Defines the canonical runtime artifact format, folder conventions (`.lcs/docs/<timestamp>-<slug-work-item>/`), state management file, and token optimization rules.
  - `AGENTS.md`: Behavioral guidelines that enforce surgical code quality, beautiful Diátaxis documentation standards, simplicity/YAGNI, and skill-creation specifications.

## 2. Setup & Local Development
### Prerequisites
- Active LLM Agent Client/CLI configured with capability to trigger skills locally.
- Powershell 5.1 / Bash shell for command executions.

### Installation
Cloning the project and ensuring `.agents/skills` or local directory contains these custom skills:
```bash
# Skills should be loaded into your agent runtime path
```

### Running Locally
To track session progress:
1. Initialize `.lcs/state.md` with:
   ```markdown
   current_phase: explore
   current_work: <timestamp>-<slug-work-item>
   last_session_note: <details>
   timestamp: <ISO-timestamp>
   ```
2. Save active workspace sessions within `.lcs/docs/<timestamp>-<slug-work-item>/` folder.

### Environment Variables
No custom application environment variables needed. Relies entirely on the LLM runtime variables.

## 3. Architecture & Code Structure
### Component Directory Map
- `skills/lcs-shared/`: Contains the foundational contract (`contract.md`) and common configurations for the LCS pack.
- `skills/lcs-explore/`: Interactive feature exploration and brainstorming logic. Generates `explore.md`.
- `skills/lcs-toprd/`: Generates an implementation-focused, lean `prd.md` based on initial findings.
- `skills/lcs-prd-reviewer/`: Audits `prd.md`, validates security/performance, and generates `prd-enhanced.md`.
- `skills/lcs-task-slicer/`: Slices `prd-enhanced.md` into granular `task-###.md` files under `task/` directory.
- `skills/lcs-task-executer/`: Executes/verifies tasks sequentially in Normal or TDD mode, updating the task status.
- `skills/lcs-doc-finalizer/`: Gathers all completed task metrics, produces final `map.md` and `doc.md` under `reff/`, archives workspace, and regenerates references index.
- `skills/lcs-onboarding/`: Automates initial onboarding summary scanning and outputs `onboarding.md`.

### High-level Flow
```text
[lcs-explore] -> explore.md
      |
[lcs-toprd] -> prd.md
      |
[lcs-prd-reviewer] -> prd-enhanced.md
      |
[lcs-task-slicer] -> task-###.md
      |
[lcs-task-executer] -> Executes tasks
      |
[lcs-doc-finalizer] -> Generates map.md & doc.md, cleans folders
```

## 4. Testing
No automated engine tests exist inside the repo structure. Verification is done structurally by evaluating skill metadata definitions, verifying that outputs strictly match contract shapes, and ensuring `state.md` correctly guides transitions.

### Verification of Skills
Run structural validation manually or test each skill trigger on raw inputs to ensure schema match.

## Handoff
Next recommended skill: lcs-explore
Next file to read: .lcs/docs/onboarding.md
Current phase: onboarding
Current confidence: high
Blocking questions: None
Risks to carry forward: None
Suggested next command: Explore new features using lcs-explore skill or create a PRD
