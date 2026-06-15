---
name: ea-lens
description: Apply an opinionated practitioner lens to the full engagement — cuts through completeness theatre to identify what actually matters, where real risk lies, and what a seasoned architect would do differently
argument-hint: "[architect] [--quick]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

You are executing the `/ea-lens` command. Load the `ea-architect-lens` skill for the lens logic.

## Overview

This command provides an opinionated engagement-level review from the perspective of a senior EA practitioner focused on what actually matters. Unlike `/ea-engage-review` (a structured health check across four dimensions) or `/ea-grill` (a deep artifact review), `/ea-lens` applies practitioner judgment to the full engagement — separating signal from noise, identifying real risk, and recommending specific next moves.

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load full `engagement.json` — extract: name, slug, currentPhase, direction (all items: drivers, goals, objectives, strategies, issues, problems, opportunities, gaps if present), phases, metrics, artifacts list.

---

## Step 2 — Load Engagement Context

If `--quick` flag is set: **skip this step** and proceed to Step 3 using engagement.json state only.

Otherwise, read:
- All artifact `.md` files in `EA-projects/{slug}/artifacts/` (exclude `*.review.md`, `decision-register*.md`, `risk-register*.md`, `concerns-register*.md`, `adr-register*.md`, `change-register*.md`, `gap-register*.md`, `drivers-register*.md`)
- All A3 appendices (scan each artifact for `## Appendix A3`)
- All A4 appendices (scan each artifact for `## Appendix A4`)
- `artifacts/cross-cutting/risk-register*.md` if present, else scan A4 rows for Category = Risk items
- `artifacts/cross-cutting/adr-register*.md` or individual ADR files in `artifacts/`
- Open PAD-NNN entries (scan artifacts for `PAD-\d{3}` tokens)
- `engagement.json → direction.gaps[]` if present

---

## Step 3 — Load Skill and Apply Lenses

Load the `ea-architect-lens` skill. Pass the loaded context (engagement.json fields + artifact content). The skill applies eight lenses and produces a structured report.

---

## Step 4 — Present Report

Present the lens report in full.

Then offer:
```
Save this lens review to file? (y/n)
```
If yes: write to `EA-projects/{slug}/artifacts/cross-cutting/notes/lens-review-{YYYY-MM-DD}.md`.

---

## Handling `--quick`

When invoked as `/ea-lens --quick` or `/ea-lens architect --quick`:
- Skip Step 2 (artifact scan)
- Load `ea-architect-lens` skill in quick mode (Lenses 1, 7, and 8 only)
- Label the output: "(Quick mode — based on engagement.json state only)"
