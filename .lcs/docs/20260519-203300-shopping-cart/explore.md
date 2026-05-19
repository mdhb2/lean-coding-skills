# Explore: shopping-cart

## Core Intent
Allow users to save items for later

## Brainstorm & Tech Options
Use Redis for cache, primary source remains DB

## Q&A History
* Q: What storage?
  * A: DB
  * Recommendation: Prefer using Redis for short-term cache

* Q: How to surface?
  * A: UI flag + API
  * Recommendation: Keep simple: new tab in cart

## Current Findings & Trade-offs
Use Redis for cache, primary source remains DB

## Risks & Assumptions
Users have account

## Handoff
Next recommended skill: lcs-toprd
Next file to read: .lcs/docs/20260519-203300-shopping-cart/explore.md
Current phase: explore
Current confidence: medium
Blocking questions: None
Risks to carry forward: Users have account
Suggested next command: Buat PRD dari explore.md
