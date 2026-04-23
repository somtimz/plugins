---
name: ea-direction
description: Display the Direction Register — Goals, Objectives, and Strategies — aggregated from artifacts in the active engagement. Supports filtering by domain or item type.
allowed-tools: [Read, Bash, Glob]
---

You are executing the `/ea-direction` command. Load the `ea-engagement-lifecycle` skill for context.

## Overview

The Direction Register aggregates all Goals (`G-NNN`), Objectives (`OBJ-NNN`), and Strategies (`STR-NNN`) from motivation-layer artifacts across the active engagement into a single cross-artifact view. Items are parsed from artifact sections — not from `engagement.json`. The command is read-only; no file is written.

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one.
3. Load `engagement.json` to confirm the slug and engagement name.

---

## Step 2 — Parse Arguments

| Argument | Effect |
|---|---|
| *(none)* | Full register — all artifacts, all item types |
| `--domain Business\|Data\|Application\|Technology` | Filter by inferred domain (see Domain Mapping below) |
| `goals` | Goals table only |
| `objectives` | Objectives table only |
| `strategies` | Strategies table only |

Arguments are combinable: `/ea-direction goals --domain Business`

---

## Step 3 — Scan Artifacts

### 3a — List files

List all `*.md` files under `EA-projects/{slug}/artifacts/` recursively. Exclude:
- `*.review.md`
- `decision-register-*.md`
- `risk-register-*.md`
- `adr-register-*.md`
- `direction-register-*.md`
- `change-register-*.md`

### 3b — Detect direction-bearing sections

For each file, scan for these section types:

| Section type | Detection rule |
|---|---|
| **Goals** | Heading (any level) whose text contains "Goals" (case-insensitive), AND the next markdown table contains at least one row where the first cell matches `G-\d+` |
| **Objectives** | Heading containing "Objectives", AND next table has rows matching `OBJ-\d+` in first cell |
| **Strategies** | Heading containing "Strategies", AND next table has rows matching `STR-\d+` in first cell |

### 3c — Parse table rows

For each detected section, parse its table:
- Skip header rows (first cell is `ID` or `---`)
- Skip separator rows (all cells are `---` or similar)
- Skip rows where the statement cell (second cell) matches `{{...}}` — these are template placeholders
- Skip rows where the statement cell is empty, `—`, or whitespace only

**Column layouts (from Architecture Vision templates):**

Goals: `| ID | Goal | Business Driver(s) | Linked Strategies |`
- Map to: id, statement, drivers, linkedStrategies

Objectives: `| ID | Objective | Measure | Target | Deadline | Linked Goal |`
- Map to: id, statement, measure, target, deadline, linkedGoal

Strategies: `| ID | Strategy | Supports Goal(s) |`
- Map to: id, statement, supports

If a row has fewer columns than expected (legacy or variant format), populate missing fields as `—`.

### 3d — Domain Mapping

Infer domain from the artifact filename (basename, not path):

| Filename pattern | Domain |
|---|---|
| `architecture-vision*` | All |
| `business-architecture*`, `business-model-canvas*` | Business |
| `data-architecture*` | Data |
| `application-architecture*` | Application |
| `technology-architecture*` | Technology |
| *(anything else)* | — |

Tag each parsed item with:
- `sourceArtifact`: prettified filename (e.g. `architecture-vision.md` → `Architecture Vision`)
- `domain`: inferred from filename above

### 3e — De-duplicate

If the same ID (e.g. `G-001`) appears in multiple artifacts (e.g. Architecture Vision and Architecture Roadmap), keep the first occurrence and skip duplicates. The Architecture Vision is the canonical source — sort files so `architecture-vision*` is processed first.

Collect into three unified lists: `allGoals`, `allObjectives`, `allStrategies`.

---

## Step 4 — Apply Filters

Apply any arguments parsed in Step 2:
- `--domain X`: keep only items where `domain` equals X (case-insensitive) or `All`
- `goals` / `objectives` / `strategies`: restrict which sections are rendered

If filtering yields zero rows for a section, omit that section from output (do not render empty tables).
If filtering yields zero rows across all sections, output: "No direction items match the applied filters." followed by a filter summary, then stop.

---

## Step 5 — Render Inline

Print the register directly in chat. Do not write any file.

```
## Direction Register
Engagement: {name}  ·  Date: {YYYY-MM-DD}

### Goals
| ID | Statement | Domain | Drivers | Linked Strategies | Source |
|---|---|---|---|---|---|
| G-001 | ... | All | DRV-001 | STR-001 | Architecture Vision |

### Objectives
| ID | Statement | Domain | Measure | Target | Deadline | Linked Goal | Source |
|---|---|---|---|---|---|---|---|
| OBJ-001 | ... | All | Time-to-active | < 1 day | Q4 2026 | G-001 | Architecture Vision |

### Strategies
| ID | Statement | Domain | Supports | Source |
|---|---|---|---|---|
| STR-001 | ... | All | G-001 | Architecture Vision |

---
{N} goals · {N} objectives · {N} strategies from {N} artifact(s)
```

Formatting rules:
- Null, empty, or absent fields: show `—`
- If an item-type argument was given (e.g. `/ea-direction goals`), omit the other two sections entirely
- Sort rows within each section by ID number (G-001, G-002, … OBJ-001, OBJ-002, … STR-001, STR-002, …)

---

## Step 6 — Edge Cases

| Scenario | Handling |
|---|---|
| No artifacts directory or no `.md` files found | "No artifacts found in `EA-projects/{slug}/artifacts/`. Run `/ea-phase` to start a phase and create artifacts." |
| Artifacts exist but none contain G/OBJ/STR sections | "No direction items found. Run `/ea-interview` on Phase A (Architecture Vision) to capture Goals, Objectives, and Strategies." |
| Architecture Vision not yet created | Show items from any other artifact that has them; note at footer: "Architecture Vision not found — items sourced from: {list}" |
| `--domain` returns no items | "No direction items found for domain {X}. Check that artifacts for that domain have been created and populated." |
| All items are template placeholders | Treat as empty (same message as no items found) |
| Same ID in multiple artifacts | Keep first occurrence (Architecture Vision takes priority); do not show duplicates |
