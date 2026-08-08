# SKILL.md Drafts — LCS Enhancement

Full SKILL.md content for all 5 new skills and 5 enhancements.
Extracted from PRD to reduce token bloat.

---

## Draft 1

```markdown
# LCS Domain Modeling Skill

## Purpose

Actively build and sharpen the project's domain model. Challenge terms, invent edge-case scenarios, and write the glossary/ADRs the moment they crystallize.

## Behavior Checklist

1. Read `.lcs/[state.md](http://state.md)` and project root [`CONTEXT.md`](http://CONTEXT.md) (if exists).

2. **Challenge against glossary:** If user uses a term conflicting with [`CONTEXT.md`](http://CONTEXT.md), call it out immediately.

3. **Sharpen fuzzy language:** Propose precise canonical terms for overloaded words.

4. **Cross-reference with code:** Surface contradictions between user statements and actual codebase.

5. **Update inline:** Update [`CONTEXT.md`](http://CONTEXT.md) in project root immediately when a term is resolved. Do not batch.

6. **Offer ADRs sparingly:** Only create `docs/adr/[XXXX-decision.md](http://XXXX-decision.md)` if: (1) Hard to reverse, (2) Surprising without context, (3) Result of real trade-off.

7. End with Handoff recommending `lcs-toprd` or returning to previous skill.
```

---

## Draft 2

```markdown
# LCS Research Skill

## Purpose

Investigate a question against high-trust primary sources and capture findings as cited Markdown.

## Behavior Checklist

1. Identify the research question and required primary sources (official docs, source code, RFCs).

2. Spin up a background investigation process (or sequential deep-search if background agents unavailable).

3. **Rule:** Follow every claim back to the primary source. Do not cite secondary blog posts or AI summaries.

4. Write findings to `.lcs/work-items/{ts}-{slug}/research/<topic>.md`.

5. Include a `## Citations` section with exact URLs/file paths and line numbers.

6. End with Handoff passing the research artifact back to the invoking skill (e.g., `lcs-explore` or `lcs-wayfinder`).
```

---

## Draft 3

```markdown
# LCS Prototype Skill

## Purpose

Build throwaway code to answer a specific design question.

## Behavior Checklist

1. **Pick a branch:**

   - "Does this logic/state model feel right?" -&gt; LOGIC branch: Single HTML file with state panel + free-play buttons.

   - "What should this look like?" -&gt; UI branch: Multiple variations switchable via URL params.

2. **Rules:** Throwaway from day one. Trivial to run. No persistence by default. Skip polish (no tests/abstractions). Surface state after every action.

3. Create prototype in `.lcs/work-items/{ts}-{slug}/prototype/`.

4. **Capture:** Once validated, fold decision into real code/spec. Archive prototype code to a throwaway git branch and leave a context pointer in the PRD/SRS.

5. End with Handoff to `lcs-toprd` or `lcs-tosrs`.
```

---

## Draft 4

```markdown
# LCS Wayfinder Skill

## Purpose

Plan huge chunks of work as a shared map of decision tickets resolved one at a time.

## Behavior Checklist

1. **Name the destination:** Run a grilling session to pin down the spec/change.

2. **Map the frontier:** Breadth-first fan out across the space to surface open decisions.

3. **Create the map:** Write `.lcs/work-items/{ts}-{slug}/[wayfinder-map.md](http://wayfinder-map.md)`.

4. **Create decision tickets:** Write child files in `.lcs/work-items/{ts}-{slug}/wayfinder-tickets/`. Use YAML frontmatter for `blocked_by` to render dependencies.

5. **Resolve:** Never resolve more than one ticket per session. Record resolution, close ticket, update map.

6. **Handoff:** When map clears, hand off to `lcs-toprd` to collapse decisions into a buildable plan.
```

---

## Draft 5

```markdown
# LCS Wizard Skill

## Purpose

Generate interactive bash scripts for human-in-the-loop manual procedures (infra setup, migrations).

## Behavior Checklist

1. **Scope:** Read `.env.example`, CI configs, and framework configs to identify every required value.

2. **Map journey:** Define exact URLs to open, actions to take, and variables to capture.

3. **Author:** Generate script using [`template.sh`](http://template.sh) helpers `stage`, `open_url`, `ask_secret`, `write_env`).

4. **Verify:** Run `bash -n` and `shellcheck`. NEVER execute end-to-end (it blocks on human input).

5. Save to `scripts/<name>-[wizard.sh](http://wizard.sh)`. End with Handoff to user for manual execution.
```

---

## Draft 6

```markdown
## 6-Phase Disciplined Loop (Mandatory)

- **Phase 1: Build Feedback Loop:** MUST build a tight, deterministic, agent-runnable command that goes RED on this specific bug. (Try: failing test, curl script, replay trace). NO HYPOTHESIZING ALLOWED until Phase 1 is complete.

- **Phase 2: Reproduce + Minimize:** Shrink repro to smallest scenario that still goes red. Cut one element at a time.

- **Phase 3: Hypothesise:** Generate 3-5 ranked, falsifiable hypotheses. Format: "If X is cause, changing Y will make bug disappear". Show to user before testing.

- **Phase 4: Instrument:** Change one variable at a time. Tag all debug logs with `[DEBUG-XXXX]` for easy cleanup.

- **Phase 5: Fix + Regression:** Write regression test BEFORE fix (only if correct seam exists).

- **Phase 6: Cleanup + Post-Mortem:** Remove `[DEBUG-XXXX]` logs. Ask: "What architectural change would have prevented this?" Handoff to `lcs-codebase-doc` or `lcs-toprd` if architecture needs deepening.
```

---

## Draft 7

```markdown
## Seam Discipline &amp; TDD Rules

- **Glossary:** A Seam is the public boundary you test at. Test ONLY at pre-agreed seams.

- **Anti-Patterns (STRICTLY FORBIDDEN):**

  1. *Implementation-coupled:* Mocking internal collaborators or testing private methods.

  2. *Tautological:* Assertion recomputes expected value the same way the code does `expect(add(a,b)).toBe(a+b)`).

  3. *Horizontal slicing:* Writing all tests first, then all implementation. MUST use vertical tracer bullets.

- **Rule:** Refactoring is NOT part of the red-green loop. It belongs to the review stage.
```

---

## Draft 8

```markdown
## Two-Axis Review Execution

- **Axis 1: Standards:** Check coding standards, Fowler smell baseline, consistency with existing patterns.

- **Axis 2: Spec:** Check faithful implementation of originating PRD/SRS/Task. Verify Acceptance Criteria.

- **Execution:** Run both axes. If they conflict (e.g., Standards say "extract method" but Spec says "keep inline for performance"), flag as `CONFLICT` and require user resolution.
```

---

## Draft 9

```markdown
## Blocking Edges &amp; Expand-Contract Pattern

- **Blocking Edges:** Every task file MUST include `blocked_by` in YAML frontmatter. Work the frontier (unblocked tasks first).

- **Wide Refactors (Expand-Contract):** If a task is a mechanical change with massive blast radius (e.g., rename column):

  1. *Expand:* Add new form beside old (Task 1).

  2. *Migrate:* Move call sites in batches (Tasks 2..N).

  3. *Contract:* Delete old form (Task N+1).

  Do NOT force wide refactors into vertical tracer bullets.
```

---

## Draft 10

```markdown
## Testing Seams

Seams at which we will test this feature. Existing seams preferred. The fewer seams across the codebase, the better.

- **Primary seam:** [Highest level public interface]

- **Secondary seams:** [Integration points if needed]

- **New seams needed:** [Propose at highest point possible]
```

