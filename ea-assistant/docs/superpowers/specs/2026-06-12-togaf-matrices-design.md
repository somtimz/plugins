# TOGAF Matrix Artifacts Feature Design

**Date:** 2026-06-12
**Status:** Approved
**Scope:** ea-assistant plugin

---

## Overview

Add first-class support for TOGAF 10 relationship matrices — grid artifacts that expose relationships between architecture elements (actors and roles, applications and data, capabilities and organizations). Catalogs list things, diagrams visualize things, matrices expose relationships between things.

A matrix catalogue reference defines all 18 standard matrices. A new `/ea-matrix` command creates, edits, and checks matrix artifacts stored in per-phase folders. `/ea-interview`, `/ea-brainstorm`, and `/ea-grill` consult the catalogue to suggest, elicit, and validate matrices.

---

## 1. Scope Split — 18 Matrices

### Managed by `/ea-matrix` (14)

| # | Matrix | Key | ADM Phase | Phase folder |
|---|---|---|---|---|
| 1 | Principle / Decision | `principle-decision` | Preliminary / Cross-cutting | `preliminary` |
| 2 | Business Interaction | `business-interaction` | B | `phase-b` |
| 3 | Actor / Role | `actor-role` | B | `phase-b` |
| 4 | Capability / Organization | `capability-organization` | B | `phase-b` |
| 5 | Capability / Value Stream | `capability-value-stream` | B | `phase-b` |
| 6 | Capability / Application | `capability-application` | B / C | `phase-b` |
| 7 | Data Entity / Business Function | `data-function` | C | `phase-c-data` |
| 8 | Application / Data | `app-data` | C | `phase-c-data` |
| 9 | Application / Organization | `app-organization` | C | `phase-c-app` |
| 10 | Role / Application | `role-application` | C | `phase-c-app` |
| 11 | Application / Function | `app-function` | C | `phase-c-app` |
| 12 | Application Interaction | `app-interaction` | C | `phase-c-app` |
| 13 | System / Technology | `system-technology` | D | `phase-d` |
| 14 | Work Package / Dependency | `wp-dependency` | E / F | `phase-f` |

### Managed elsewhere (4) — catalogue documents them with `managedBy:` pointers

| Matrix | Managed by |
|---|---|
| Stakeholder Map Matrix | Existing `stakeholder-map.md` artifact (Phase A) |
| Requirements Traceability Matrix | Existing `traceability-matrix.md` artifact + `/ea-trace` |
| Work Package / Gap | New `/ea-trace` View 9 — rendered from the gaps register's `linkedWorkPackages` field |
| Requirement / Work Package | New `/ea-trace` View 10 — derived transitively from Req→Capability→WP links |

**No new ID prefix.** Matrix files are named artifacts (e.g. `actor-role-matrix.md`); their axes reference existing IDs (CAP-NNN, WP-NNN, ROLE-NNN, BP/DP/AP/TP, ADR-NNN, GAP-NNN, REQ-NNN).

---

## 2. Matrix Catalogue Reference

New file: `skills/ea-artifact-templates/references/matrix-catalogue.md` (beside the existing `diagram-catalogue.md`).

One entry per matrix (all 18). Each entry defines:

| Field | Content |
|---|---|
| `key` | Slug used by commands (e.g. `app-data`) |
| Name, ADM phase(s), phase folder | As per the scope table |
| Axes | Row entity and column entity, with ID prefix where one exists |
| Axis seed sources | Which artifact/register supplies row/column candidates (e.g. Capability Model for CAP rows, Application Architecture for application columns, Role Catalogue for ROLE rows, ADR Register for decisions, Principles artifacts for BP/DP/AP/TP) |
| Cell marker vocabulary | Legal markers per matrix — CRUD for App/Data and Data/Function; primary/secondary/approving/accountable/consulted for Actor/Role; provides-service-to/depends-on/governs/collaborates-with for Business Interaction; tolerate/invest/migrate/retire (plus fit/health/criticality) for Capability/Application; accountable-owner/performer/consumer/governance for Capability/Organization; enabling/differentiating/weak/missing/target for Capability/Value Stream; ownership/heavy-use/light-use/support/funding for App/Organization; use-type/access-level/frequency/mandatory-optional for Role/Application; primary/secondary/duplicate/planned-replacement/target for App/Function; direction/interface/data/frequency/style/criticality for App Interaction; lifecycle-status/risk for System/Technology; predecessor/successor/technical/business/funding/governance for WP/Dependency; supports/constrains/exception/conflict/requires-review for Principle/Decision |
| What it shows / Why use it / How to use it | Condensed from the TOGAF 10 source material |
| Grill checks | 2–4 testable statements per matrix (consumed by `/ea-grill` and `/ea-matrix check`) |
| Elicitation questions | 2–3 targeted interview prompts per matrix (consumed by `/ea-interview` and `/ea-brainstorm`) |

The 4 managed-elsewhere entries carry a `managedBy:` pointer instead of grill checks and elicitation questions.

**Single source of truth:** grill checks and elicitation questions live only in the catalogue. Commands reference the catalogue; they do not restate check or question logic inline (per the no-duplicated-logic rule).

---

## 3. Matrix Artifact File Format

Seeded from new `templates/seeds/matrix-template.md`.

### Frontmatter

```yaml
---
id: actor-role-matrix
name: Actor / Role Matrix
matrixKey: actor-role
phase: B
status: Draft            # Draft | In Review | Approved
version: 0.1.0
relatedArtifacts: []
diagrams: []
links: []
lastModified: YYYY-MM-DD
---
```

### Body sections

| Section | Content |
|---|---|
| `## Overview` | Purpose of this matrix for this engagement |
| `## Matrix` | The grid as a markdown table — rows × columns with cell markers |
| `## Legend` | Marker vocabulary copied from the catalogue entry |
| `## Observations` | Findings the matrix exposes — duplications, orphans, hotspots, missing relationships |
| `## Open Questions` | Unresolved cells or relationships pending stakeholder input |

Matrices are artifacts, not registers — versioned via frontmatter, no `snapshots/` folder, no Appendix A3 (matrices are not in the T3-A3 artifact list).

---

## 4. `/ea-matrix` Command

New top-level command following the multi-mode pattern of `/ea-refarch`.

| Mode | Syntax | Behaviour |
|---|---|---|
| `list` | `/ea-matrix list` (default when no args) | All 18 catalogue entries with per-engagement status: ✅ exists (cell fill %), ⬜ recommended for phases in scope, ➡️ managed elsewhere (with pointer) |
| `new` | `/ea-matrix new <key>` | Creates the matrix file in its phase folder. Axis seeding: reads the catalogue's seed sources, proposes row/column candidates from existing artifacts. User confirms/edits axes; cells elicited row by row or left empty. Errors if matrix already exists (points to `edit`). |
| `show` | `/ea-matrix show <key>` | Renders the matrix file with legend and observations |
| `edit` | `/ea-matrix edit <key>` | Guided editing: add/remove rows or columns (re-offering unseeded candidates), update cells, refresh Observations. Bumps version, updates `lastModified`. |
| `check` | `/ea-matrix check [<key>]` | Runs the catalogue's grill checks for one matrix, or all existing matrices if no key. Same check definitions `/ea-grill` uses. |

Cross-cutting behaviour:

- **Phase awareness:** `new` and `list` highlight matrices whose phase matches `currentPhase`
- **Registration:** `new` registers the artifact in `engagement.json → artifacts` and updates `lastModified`
- **Stale-axis detection:** `edit` and `check` compare axes against current seed sources and flag drift — e.g. "CAP-009 exists in the Capability Model but has no row in this matrix"
- **Error guards:** no active engagement → prompt `/ea-open`; unknown key → list valid keys; managed-elsewhere key → show pointer and stop

---

## 5. `/ea-interview` Integration (phase mode)

New step after the framework-lens offer in `commands/ea-interview.md` phase mode:

1. Read the matrix catalogue; filter to matrices whose phase matches the interview phase
2. Skip matrices that already exist with at least one filled cell
3. Offer: *"This phase has N recommended matrices: {names}. Capture any now? (pick / skip)"*
4. On accept, for each chosen matrix: ask the catalogue's elicitation questions, seed axes from the catalogue's seed sources (same logic as `/ea-matrix new`), and write the matrix file from the template
5. Record answers in the interview notes as usual

Skipping is silent and free — matrices are recommended, not mandated.

---

## 6. `/ea-brainstorm` Integration

Two light touches in `commands/ea-brainstorm.md`:

1. **Context hints (step 3b):** add the phase's recommended matrices to the pad's prefilled context, tagged `[Matrix]` — listing key, axes, and one elicitation question each
2. **New thought category `"relationships"`:** captures cross-element relationship statements ("CRM reads Customer master", "Finance depends on Procurement"). `/ea-interview` and `/ea-matrix new` later harvest these as cell candidates when populating matrices for the same phase.

No other pad UI changes.

---

## 7. `/ea-grill` Integration

Two integration points in `skills/ea-grill-skills/SKILL.md`:

1. **Artifact mode — recommended-matrices block:** when grilling a phase artifact, a block (modeled on the adopted-RA block) flags missing or empty recommended matrices for that phase. Advisory — does not fail the review.
2. **Matrix grilling:** when the grill target is itself a matrix artifact, run the catalogue's grill checks for that `matrixKey`:
   - Axes match the catalogue definition
   - All cell markers are within the matrix's legal vocabulary
   - No orphan rows/columns versus the seed sources (e.g. an application in the Application Architecture with no row in the App/Data matrix)
   - `## Observations` is non-empty when status is Approved

No new T3 compliance rule — matrix presence stays advisory (matrices are recommended per TOGAF tailoring, not mandated).

---

## 8. `/ea-trace` — Two New Views

| View | Rows | Columns | Source | Notes |
|---|---|---|---|---|
| View 9 — Gap → Work Package | GAP-NNN | WP-NNN | Gaps register `linkedWorkPackages` field | Read-only render; no new links in `traceability-index.json` |
| View 10 — Requirement → Work Package | REQ-NNN | WP-NNN | Derived transitively from Req→Capability→WP links | Read-only; composition of View 4 and View 5 |

Both views appear in the persistent menu and in the `--gaps` consolidated report.

---

## 9. Files to Create / Modify

### New files

| File | Purpose |
|---|---|
| `commands/ea-matrix.md` | `/ea-matrix` command definition |
| `skills/ea-artifact-templates/references/matrix-catalogue.md` | 18-matrix catalogue — single source of truth for axes, markers, seed sources, grill checks, elicitation questions |
| `templates/seeds/matrix-template.md` | Blank matrix artifact template used by `new` mode |

### Modified files

| File | Change |
|---|---|
| `commands/ea-interview.md` | Matrix offer step in phase mode (after framework-lens offer) |
| `commands/ea-brainstorm.md` | `[Matrix]` context hints in step 3b; `"relationships"` thought category |
| `skills/ea-grill-skills/SKILL.md` | Recommended-matrices advisory block; matrix grilling checks |
| `commands/ea-trace.md` | View 9 (Gap → WP) and View 10 (Req → WP); menu and `--gaps` report updates |
| `commands/ea-help.md` | `/ea-matrix` row in commands table |
| `CLAUDE.md` | Version 0.9.62; 55 commands; `/ea-matrix` in key entry points |
| `.claude-plugin/plugin.json` | Version 0.9.62 |
| `../.claude-plugin/marketplace.json` | Version 0.9.62 (must match plugin.json) |
| `docs/PRD.md` | v0.9.62 section documenting the feature |
| `README.md` | `/ea-matrix` in commands table; matrix feature bullet |

---

## 10. Out of Scope

- Matrix rendering as diagrams (heatmaps, chord diagrams) — `/ea-generate` integration can come later
- Auto-population of cells from document ingestion
- Matrix diffing between baseline and target states (gap analysis stays in `/ea-gaps`)
- New T3/T4 compliance rules for matrix presence
