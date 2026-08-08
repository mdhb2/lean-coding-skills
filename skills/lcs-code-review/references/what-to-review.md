
## What to Review

### 1. Explore Alignment

Check if implementation still matches initial context.

Verify:

- Original problem to solve.
- Technical constraints.
- User goal.
- Scope boundaries.
- Exploration decisions agreed upon.

Review questions:

```text
Does the code solve the same problem identified during exploration?
Is there any implementation that deviates from the initial context?
Are any initial constraints violated?
```

### 2. PRD Alignment

Check if feature matches product requirements.

Verify:

- Feature purpose.
- User story.
- Functional requirements.
- Non-functional requirements.
- Out of scope.
- Success criteria.

Review questions:

```text
Are all main PRD requirements reflected in the code?
Are there any requirements not yet implemented?
Are there any features added that were not requested?
Does the product behavior match user expectations?
```

### 3. PRD Enhance Alignment

Check if PRD reviewer hardening is applied.

Verify:

- Additional edge cases.
- Requirement risks.
- Clarifications.
- Security concerns.
- Data validation.
- Permission rules.
- Failure scenarios.
- UX fallbacks.

Review questions:

```text
Is the PRD hardening output followed?
Are important edge cases handled?
Are previously identified vulnerabilities closed?
```

### 4. SRS Alignment

Check if implementation follows technical specification.

Verify:

- Data model.
- API contract.
- Service behavior.
- State transitions.
- Error handling.
- Validation rules.
- Permission logic.
- Integration points.
- Side effects.
- Dependencies.

Review questions:

```text
Does the code follow the SRS technical design?
Is the data structure correct?
Is the system flow correct?
Is error handling implemented as specified?
Are there any technical behaviors differing from SRS?
```

### 5. Task Breakdown Alignment

Check if completed task matches task breakdown.

Verify:

- Task ID.
- Task scope.
- Acceptance criteria.
- Target files.
- Expected output.
- Work boundaries.
- Task dependencies.

Review questions:

```text
Was the task completed within scope?
Did the task expand into other areas?
Are all acceptance criteria met?
Are there files that should have been touched but were not?
Are there files that should not have been touched?
```

### 6. Potential Bugs

Must check:

- Null / undefined handling.
- Empty state.
- Invalid input.
- Duplicate data.
- Race condition.
- Permission bypass.
- Incorrect validation.
- Incorrect default value.
- Wrong conditional logic.
- Wrong date/time handling.
- Timezone issue.
- Data loss.
- Broken migration.
- Broken relation.
- Broken API response.
- Broken UI state.
- Unhandled errors.
- Regression against existing features.
- Inconsistent naming.
- Inconsistent types.
- Dangerous hardcoded values.

### 7. Security & Data Safety

Must check:

- Auth check.
- Authorization / role permission.
- Input validation.
- SQL injection risk.
- XSS risk.
- CSRF risk.
- Secret/token leakage.
- Sensitive data exposure.
- Unsafe file upload.
- Unsafe external request.
- Missing rate limit if relevant.
- Data ownership rule.

If security is not relevant to the task, write:

```text
No direct security-sensitive surface found for this task.
```

### 8. Error Handling & Failure Mode

Must check:

- Database error.
- API error.
- Network error.
- Empty response.
- Invalid payload.
- Missing config.
- Failed dependency.
- Failed transaction.
- Partial update.
- Retry behavior if relevant.

### 9. Test Coverage

Review:

- Unit test.
- Feature test.
- Integration test.
- Regression test.
- Edge case test.
- Manual test instruction.

If tests are missing, determine whether this is a `Required Fix` or `Recommended Improvement` based on task risk level.

### 10. Maintainability

Check:

- Overly long functions.
- Logic duplication.
- Confusing naming.
- File structure mismatching project patterns.
- Business logic leaking into UI.
- Heavy queries.
- Unclear types.
- Missing comments on complex logic.
- Excessive abstraction.

Maintainability issues are only Required Fix if they risk causing bugs or violating SRS/task.

---
