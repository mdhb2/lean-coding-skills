---
title: "Master Session Log: {session-date}"
format_version: "okf/0.2"
authors:
  - type: agent
    name: "lcs-master"
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
artifact_type: session_log
cot_level: standard
version: "1.0"
status: active
tags: [routing, session-log, decisions]
summary: "Routing decisions and session log for {session-date}"
source: "user input"
related: []
---

# Master Session Log: {session-date}

## Session Mode
- **Mode:** confirmation / autopilot
- **Start:** {HH:MM}

## Routing Decisions

| # | User Input | Routed To | Reason | Time |
|---|-----------|-----------|--------|------|
| 1 | "{user text}" | lcs-explore | Ambiguous feature request | {HH:MM} |
| 2 | "{user text}" | lcs-toprd | Exploration complete, ready for PRD | {HH:MM} |

## SOT Blockers Written
| Skill | Blocker | File |
|-------|---------|------|
| {skill} | {what blocked} | {path} |

## Cross-Level Guards Triggered
{List any cross-level guard stops. If none: "None."}

## Session End
- **End:** {HH:MM}
- **Final Status:** {active work item, current phase}

## Handoff

Next recommended skill: lcs-code-review
Next file to read: .lcs/work-items/{timestamp}-{slug-work-item}/session-log.md
Current phase: execution
Current confidence: <low/medium/high>
Blocking questions: <list or None>
Risks to carry forward: <summary or None>
Source of Truth Bundle: .lcs/state.md, task-###.md, srs.md, tests.md, task-coverage.md if present
Must Preserve IDs: <executed SRC/FR/AC/TEST IDs>
Unresolved IDs: <list or None>
Suggested next command: Review implementation against requirements
