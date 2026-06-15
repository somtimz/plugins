---
name: ea-zachman
description: Create, populate, review, and audit the Zachman Diagram for an EA engagement — generate from existing artifacts, interview to fill gaps, produce coverage analysis, audit completeness and consistency, and classify any artifact against the 6×6 grid
argument-hint: "[generate | review | gap | interview | audit | classify <artifact-name>]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-zachman` command. Load the `zachman-framework` skill and the `ea-artifact-templates` skill for context.

## Overview

Manages the Zachman Diagram artifact for the active engagement. The Zachman Framework classifies architecture content by **audience row** (Contextual through Functioning) and **interrogative column** (What / How / Where / Who / When / Why).

**Modes:** `generate` (default), `review`, `gap`, `interview`, `audit`, `classify <artifact-name>`

**Reference files:**
- `skills/zachman-framework/references/cell-extraction-map.md` — which artifacts feed which cells, coverage symbols, and artifact→cell relationship table
- `skills/zachman-framework/references/interview-questions.md` — question bank for all rows
- `skills/zachman-framework/references/zachman-cell-descriptions.md` — one-sentence purpose per cell
- `skills/zachman-framework/references/zachman-audit-checklist.md` — six audit check categories, severity model, report format (used by `audit` mode and `/ea-grill`)
- `skills/zachman-framework/references/togaf-zachman-mapping.md` — TOGAF artifact classification

---

## Step 1 — Resolve Active Engagement

Check context for active slug; if none, scan `EA-projects/*/engagement.json`. Load `engagement.json`: name, slug, currentPhase, artifacts, architectureDomains.

---

## Mode: `generate` (default)

Scans all artifacts, extracts content per cell, writes a populated Zachman Diagram.

1. **Build cell extraction map** — read `skills/zachman-framework/references/cell-extraction-map.md`
2. **Scan artifacts** — for each artifact in `engagement.json → artifacts[]`, read the file, identify contributing cells, extract key statements and IDs with source traceability; classify each cell as ✅/⚠️/❌/🚫 per the coverage rules in `cell-extraction-map.md`
3. **Write the diagram:**
   - Read template from `templates/cross-cutting/zachman-diagram.md`
   - Replace `{{placeholder}}` frontmatter tokens from `engagement.json`
   - Populate Coverage Summary table and cell sections with extracted content (bullet lists) and source references
   - Populate Gap Analysis table (see `gap` mode rules below)
   - Write to: `EA-projects/{slug}/artifacts/cross-cutting/context/zachman-diagram-{YYYY-MM-DD}.md`
   - Register in `engagement.json → artifacts[]`
4. Confirm: `"Zachman Diagram written: {N} cells populated (✅ {N} / ⚠️ {N} / ❌ {N})"` then offer: review, see gaps, fill empty cells, done
5. Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

## Mode: `review`

Produces an inline coverage matrix without writing a file.

Scan existing `zachman-diagram-*.md` (most recent) or compute coverage on-the-fly from artifacts if no file exists.

Output:
```
════════════════════════════════════════════════════════════════
ZACHMAN COVERAGE — {engagement name}
Generated: {YYYY-MM-DD}  |  Phase: {currentPhase}
════════════════════════════════════════════════════════════════

         What      How      Where    Who      When     Why
R1  ✅ Scope    ✅ Scope  ✅ Scope  ✅ Scope ⚠️ Scope  ✅ Scope
R2  ✅ Concept ✅ Concept ❌       ✅ Org   ⚠️ Events ✅ Strategy
R3  ✅ Logical ⚠️ App    ⚠️ Dist   ❌       ❌        ⚠️ Rules
R4  ❌         ⚠️ Design ✅ Infra  ❌       ❌        ❌
R5  🚫         🚫        🚫        🚫       🚫        🚫

Populated : {N}   Partial : {N}   Empty : {N}
Coverage  : {N}% of in-scope cells
════════════════════════════════════════════════════════════════
```
Then list the top 3 empty cells most impactful to address with a one-line reason each.

---

## Mode: `gap`

Identifies ❌ and ⚠️ cells, classifies severity, recommends remediation.

**Severity:**
- **High** — cell is in-scope and relevant artifacts exist (content should have been extracted but wasn't), or cell is on the critical path for the current phase
- **Medium** — cell is in-scope but the relevant artifact hasn't been created yet
- **Low** — cell is in Row 4/5 (phase hasn't reached that depth), or domain is explicitly out of scope

**Remediation per cell pattern:**
- R1,Cx empty → check Engagement Charter and Architecture Vision; re-run generate after updating
- R2,Cx empty → run `/ea-interview` for relevant Phase B artifact
- R3,C1 empty → Data Architecture §3 Logical Data Model not populated
- R3,C2 empty → Application Architecture §3/§4 not populated
- R3,C3 empty → Application Communication Diagram missing
- R3,C4 empty → Role–Application Matrix missing (Application Architecture §7)
- R3,C5 empty → Processing/event model missing (Application Architecture §8)
- R3,C6 empty → Business rules not captured; run `/ea-requirements`
- R4,Cx empty → Technology Architecture not yet populated; run Phase D interview
- Any ⚠️ Partial → run `/ea-zachman interview` and jump to that cell

Output a structured gap report (High / Medium / Low sections, each gap with action), then offer: "Run '/ea-zachman interview' to fill the high-priority gaps now? (y/n)"

After the gap report and the above offer, ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

## Mode: `interview`

Guided Q&A to fill empty/partial cells row by row.

1. **Determine cells** — scan diagram or compute coverage on-the-fly; build ordered list of ❌/⚠️ cells (R1→R2→R3→R4; skip 🚫 and ✅ unless re-interview requested)
2. **Present plan** — show row-by-row counts and offer: all empty cells, one row only, jump to specific cell, cancel
3. **For each cell:**
   - Announce: `"── Cell R{N},C{N} — {Row Name} / {Column Name} ({Perspective}) ──"` with one-sentence purpose from `zachman-cell-descriptions.md`
   - Show existing content if partial; ask: add / replace / skip
   - Ask the interview question from `skills/zachman-framework/references/interview-questions.md`
   - Accept multi-line input; `done` or double-Enter to finish
   - Ask for source artifact reference (optional)
   - Write answer to Zachman Diagram file; update coverage status
4. **Session completion** — report cells populated/updated/skipped and new coverage %; offer: view coverage, see remaining gaps, done
5. Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

## Mode: `classify <artifact-name>`

Classifies a named artifact or concept against the Zachman grid.

Accept: a known artifact name or a freeform description.

Apply the Classification Workflow from `skills/zachman-framework/SKILL.md`:
1. Identify the primary audience → row
2. Identify the primary concern → column
3. Check `skills/zachman-framework/references/togaf-zachman-mapping.md` for known TOGAF artifacts
4. If not in the mapping table, apply classification rules directly

Output:
```
Classification: {artifact name}
──────────────────────────────────
Primary cell  : R{N},C{N} — {Row label} / {Column label}
Secondary cells: R{N},C{N}, R{N},C{N}
Audience      : {who should review/produce this}
Interrogative : {what question this artifact answers}

Rationale: {one paragraph}

Related cells: {cells this artifact informs or is informed by}
TOGAF mapping: {TOGAF phase and artifact name, if applicable}
```

Offer: "Update the Zachman Diagram to mark this cell as populated? (y/n)"
---

## Mode: `audit`

Quality audit of the Zachman Diagram — completeness honesty, consistency, currency, scope, and perspective purity. Complements `review`/`gap` (presence) with quality checks.

1. **Locate the diagram.** Find the most recent `EA-projects/{slug}/artifacts/cross-cutting/context/zachman-diagram-*.md`. If none exists, error: "No Zachman Diagram found — run `/ea-zachman generate` first."
2. **Run the checklist.** Load `skills/zachman-framework/references/zachman-audit-checklist.md` and execute all six categories with cross-artifact verification: open contributing artifacts per `cell-extraction-map.md`, verify cited IDs against their registers, compare modification dates, and compare cell content against each cell's `Expected Model:` line in `zachman-cell-descriptions.md`. The check definitions live in the checklist — do not restate them here.
3. **Render the report inline** using the checklist's Report Format: category scorecard, findings grouped High / Medium / Low (each with cell reference, evidence, and concrete action), and the verdict (Ready / Needs revision / Stale, per the checklist's verdict rules).
4. **Save the report** to `EA-projects/{slug}/artifacts/cross-cutting/notes/reviews/zachman-audit-{YYYY-MM-DD}.md` (create the folder if needed).
5. **Offer next actions:**
   - Verdict Stale → "Re-run `/ea-zachman generate` to refresh from current artifacts? (y/n)"
   - Otherwise → "Run `/ea-zachman interview` jumping to the failing cells? (y/n)"
   - Then ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.
