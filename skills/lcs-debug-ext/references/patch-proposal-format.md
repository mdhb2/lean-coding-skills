# Patch Proposal Format

Use this reference when writing the patch proposal section. The skill does not apply patches; it only proposes them.

## Required Structure

```markdown
## Patch Proposal
**Changes applied:** None

### Summary
[What should be changed and why.]

### Files likely affected
- `[path]` - [reason]

### Before / After
Before:

```text
[Relevant current behavior or snippet]
```

After:

```text
[Proposed behavior or snippet]
```

### Proposed diff

```diff
[Unified diff if enough context is available]
```

### Risk
[Low / Medium / High]

### Validation

```bash
[Command that should verify the fix after user approves applying it]
```

### Rollback
[How to undo the proposed change if applied later]
```

## Before/After Snippet Guidance

- Use snippets only when they clarify intent.
- Keep snippets focused on the failing path.
- If source context is missing, use `[TODO]` rather than inventing code.
- Do not rewrite unrelated code.

## Unified Diff Guidance

Include a unified diff only when enough file context is available to make a safe proposal. The diff is illustrative unless the user explicitly asks to apply it later.

Good diff proposals:

- Touch only likely affected lines.
- Include enough surrounding context.
- Avoid formatting churn.
- Include validation command.

Avoid diffs when:

- The relevant file was not inspected.
- The root cause is unknown.
- The change depends on missing environment details.
- Architecture makes the fix unsafe without a follow-up design decision.

## Risk Rating

Low:

- Narrow change.
- Clear feedback loop.
- Limited blast radius.

Medium:

- Multiple call sites or integration behavior involved.
- Validation is partial.
- Some assumptions remain.

High:

- Broad architecture impact.
- Data migration or persistence risk.
- Security, auth, billing, or concurrency risk.
- No reliable feedback loop exists.

## Validation Command

Provide the smallest command that would confirm the proposed patch after it is applied. If no command is known, provide a manual checklist and mark signal quality as Weak.

## Rollback Note

Explain how to reverse the patch if applied later. For a proposed diff, the rollback is usually reverting the affected file changes. For config or migration proposals, include any state or data caveats.

## Required Wording

Every patch proposal must clearly state:

```text
Changes applied: None
```

Do not imply that proposed code has already been applied or validated unless evidence shows it was run separately by the user.
