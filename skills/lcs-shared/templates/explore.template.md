---
title: "Explore: {short-description}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-explore"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: explore
cot_level: light
version: "1.0"
status: draft
tags: [explore, brainstorm]
summary: "Exploration and trade-off analysis for {feature/problem}"
source: "user input"
related: []
---

# Explore: {short-description}

## 1. One-line Summary

{One-sentence description of the problem or feature being explored.}

## 2. Context

- Problem: {what problem are we solving}
- Intended outcome: {desired result}
- Explore level: {easy|medium|hard|auto}
- Final active level: {easy|medium|hard}
- Interview scope: {brief summary}

## 3. Q&A History

### Round 1 — {theme}

#### Q1. {question}

- Answer: {user answer}
- Recommendation: {recommended option and brief reason}
- Resolution: {resolved|unresolved|superseded}

#### Q2. {question}

- Answer: {user answer}
- Recommendation: {recommended option and brief reason}
- Resolution: {resolved|unresolved|superseded}

#### Q3. {question}

- Answer: {user answer}
- Recommendation: {recommended option and brief reason}
- Resolution: {resolved|unresolved|superseded}

{Repeat rounds as needed.}

## 4. Findings & Options

### Option A: {name}

- Description: ...
- Pros: ...
- Cons: ...

### Option B: {name}

- Description: ...
- Pros: ...
- Cons: ...

{Add only meaningful alternatives that were actually considered.}

## 5. Risks & Assumptions

### Risks

- {risk}

### Assumptions

- {assumption} [verified|unverified]

## 6. Decisions

- Decision: {decision}
  - Owner: {user|role}
  - Origin: {round/question or direct instruction}
  - Timestamp: {ISO-8601}

## 7. Decision Ledger

Every agreed decision that creates a product, behavior, interface, data,
security, compatibility, or operational requirement must be represented as
an atomic stable `SRC-###` entry.

| SRC ID | Priority | Origin | Description |
|---|---|---|---|
| SRC-001 | P0 | explore decision | {atomic requirement} |
| SRC-002 | P1 | explore decision | {atomic requirement} |

Do not create one ID per question mechanically.
One answer may create multiple requirements.

## 8. Remaining Open Questions

- {question or None}

## 9. PRD Readiness

- Status: {low|medium|high}
- Blocking uncertainty: {list or None}
- Non-blocking uncertainty: {list or None}
- Reason: {brief explanation}

## 10. Chain of Truth Report

### Level

Light

### Sources Checked

- `.lcs/state.md` {if read}
- {other files/evidence actually checked}

### Assumptions

- {assumption} [verified|unverified]

### Actions Taken

- {what was actually explored, checked, or decided}

### Verification

{manual consistency check, source check, or not applicable}

### Report

{1-3 sentence evidence summary and confidence}

## Handoff

Next recommended skill: lcs-toprd
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/explore.md
Current phase: explore
Current confidence: {low|medium|high}
Blocking questions: {list or None}
Risks to carry forward: {summary or None}
Source of Truth Bundle: .lcs/state.md, explore.md
Must Preserve IDs: SRC-001, SRC-002, ...
Unresolved IDs: {list or None}
Suggested next command: Create PRD from exploration
