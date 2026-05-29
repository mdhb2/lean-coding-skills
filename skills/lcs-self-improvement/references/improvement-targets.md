# Improvement Targets Mapping

Map each recommendation to durable target so accepted changes can affect future sessions.

## Target Selection Rules

1. Prefer smallest stable target that matches scope.
2. Keep model-specific behavior in model-specific files only when relevant.
3. Keep reusable workflows in `skills/`.
4. Keep human process guidance in docs/readme.
5. If no clear target exists, mark item `[ASK USER]`.

## Recommendation Type -> Target

### General coding-agent behavior

- Target: `AGENTS.md`
- Use for response style, execution discipline, ambiguity handling, verification norms.

### Claude-specific behavior (optional, if present and relevant)

- Target: `CLAUDE.md`
- Use only for provider/runtime-specific behavior tied to Claude ecosystems.

### Gemini-specific behavior (optional, if present and relevant)

- Target: `GEMINI.md`
- Use only for provider/runtime-specific behavior tied to Gemini ecosystems.

### Reusable local policy/rules

- Target: `.lcs/rules/`
- Use for portable local constraints, checklists, naming rules, privacy conventions.

### Project process and reference documentation

- Target: `.lcs/docs/`
- Use for team process, review workflows, governance, decision references.

### Repeatable execution workflow

- Target: `skills/`
- Use for deterministic operational flows that should trigger by intent.

### Human-facing setup/usage guidance

- Target: `README.md` or onboarding docs
- Use for contributor instructions, install/update/usage expectations.

### Validation-heavy controls

- Target: checklist documents and/or scripts
- Use for repeatable validation that should run pre-delivery or pre-merge.

## When To Use `[ASK USER]`

Mark `[ASK USER]` when:

- recommendation has multiple valid destinations
- change impacts policy or ownership boundaries
- recommendation alters team preference, tone, or governance
- implementation has tradeoffs requiring explicit approval

## Reminder

Self-improvement report is diagnostic only. Nothing changes until accepted recommendations are applied to persistent targets.
