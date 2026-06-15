---
name: ea-trace
description: Interactive traceability views across the motivation and implementation chain — Driver → Goal → Strategy → Requirement → Capability → Work Package, and Requirement → ABB → SBB → Story — with gap and contradiction detection
argument-hint: "[--gaps]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

You are executing the `/ea-trace` command.

## Overview

Renders traceability views across the EA motivation chain and implementation chain. Reads from `traceability-index.json` (graph of cross-entity links) and artifact files. Surfaces gaps (missing links) and contradictions (conflicting relationships) with suggested fix actions.

Two chains are traced:
- **Motivation chain:** Driver → Goal → Strategy → Requirement → Capability → Work Package
- **Implementation chain:** Requirement → ABB → SBB → Story

**Modes:**

| Args | Mode |
|---|---|
| (none) | Persistent interactive menu |
| `--gaps` | Full gap report only — no matrices, runs all views and consolidates gaps |

---

## Step 1 — Resolve Active Engagement

Check context for active slug. If none, scan `EA-projects/*/engagement.json` and ask the user to select. Load `engagement.json` and extract `name` and `slug`.

---

## Step 2 — Load Traceability Graph

Read `EA-projects/{slug}/artifacts/requirements/traceability-index.json`.

If the file does not exist, create it with:
```json
{"lastUpdated": "", "links": []}
```

Build two in-memory indexes from the `links` array:
- **outgoing:** `{ "DRV-001": [{"to": "G-001", "type": "motivates"}], ... }`
- **incoming:** `{ "G-001": [{"from": "DRV-001", "type": "motivates"}], ... }`

---

## Step 3 — Build Gap Counts

For each view, count entities with no outgoing link of the required type. Use the artifact sources listed in Step 4 to find entity IDs. Gap count = entities with no matching outgoing entry in the outgoing index.

Display the persistent menu:

```
EA Traceability Views — {engagement name}
════════════════════════════════════════════

  1. Driver → Goal                 ({N} gaps)
  2. Goal → Strategy               ({N} gaps)
  3. Strategy → Requirement        ({N} gaps, {N} contradictions)
  4. Requirement → Capability      ({N} gaps)
  5. Capability → Work Package     ({N} gaps)
  6. Requirement → ABB             ({N} gaps)
  7. ABB → SBB                     ({N} gaps)
  8. SBB → Story                   ({N} gaps)
  9. Gap → Work Package            ({N} gaps)
 10. Requirement → Work Package    ({N} gaps)
 11. Full gap report               (all views, gaps + contradictions only)
  Q. Quit

Enter a number:
```

After each view completes, return to this menu (recompute gap counts before redisplaying).

If `--gaps` was passed, skip this menu and go directly to Step 6 (Full Gap Report).

---

## Step 4 — View Dispatch

Route to the section below based on the user's menu selection.

---

### View 1: Driver → Goal

**Entity sources:**
- DRV-NNN: scan `EA-projects/{slug}/artifacts/phase-a/*.md` for all tokens matching `DRV-\d{3}`
- G-NNN: scan same files for all tokens matching `G-\d{3}`

**Render matrix:**

```
Driver → Goal
══════════════════════════════════════════

           | G-001 | G-002 | G-003
DRV-001    | ✅    | ⬜    | ⬜
DRV-002    | ⬜    | ✅    | ✅
[No driver]|       |       | ⬜    ← G-003 has no driver
```

Cell is ✅ if a link `{"from": "DRV-X", "to": "G-Y", "type": "motivates"}` exists in the graph. ⬜ otherwise. A goal with no incoming `motivates` link appears in a `[No driver]` row.

**Gaps section:**

For each DRV-NNN with no outgoing `motivates` link:
```
⚠️ DRV-001 has no goal linked
   → Bootstrap: [offer if co-occurrence found, see below]
   → Or add a link: {"from":"DRV-001","to":"G-XXX","type":"motivates"}
   → Or define the goal via /ea-interview phase-a
```

For each G-NNN with no incoming `motivates` link:
```
⚠️ G-002 has no driver motivating it
   → Link to a driver or verify this goal belongs to the engagement scope
```

**Contradictions section:**

Two goals motivated by the same driver with conflicting priorities in `requirements-index.json` (one requirement derived from G-A is High, another from G-B is Low, where both G-A and G-B share the same DRV source):
```
⚠️ G-001 and G-002 both motivated by DRV-001 — requirements derived from these goals have conflicting priorities (High vs Low). Verify goal hierarchy is intentional.
   → Review via /ea-grill phase-a
```
If no such conflict is detectable from available data, skip the contradictions section.

**Bootstrap mechanism:**

For each gap (DRV with no outgoing `motivates` link), scan `EA-projects/{slug}/artifacts/phase-a/*.md` for rows where both the DRV-NNN and a G-NNN appear in the same table row or within the same `##` section. For each candidate pair found, propose:
```
Found G-001 co-mentioned with DRV-001 in Architecture Vision — add link motivates? [Y/n]
```
On Y: append `{"from":"DRV-001","to":"G-001","type":"motivates"}` to the links array, update `lastUpdated`, write `traceability-index.json`. Rebuild indexes. Show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 2: Goal → Strategy

**Entity sources:**
- G-NNN: scan `EA-projects/{slug}/artifacts/phase-a/*.md`
- STR-NNN: scan `EA-projects/{slug}/artifacts/phase-b/*.md`

**Render matrix:** rows = G-NNN, columns = STR-NNN, link type = `addresses`

**Gaps section:**

For each G-NNN with no outgoing `addresses` link:
```
⚠️ G-001 has no strategy addressing it
   → Define strategies via /ea-interview phase-b
   → Or add a link: {"from":"G-001","to":"STR-XXX","type":"addresses"}
```

For each STR-NNN with no incoming `addresses` link:
```
⚠️ STR-002 is not linked to any goal
   → Link to a goal or verify this strategy is still in scope
```

**Contradictions section:**

Two strategies both addressing the same goal that appear to be directionally opposed (e.g. strategy text contains "reduce" vs "increase" for the same dimension — detected by reading the strategy description field or title in the artifact):
```
⚠️ STR-001 ("Reduce operational cost") and STR-002 ("Increase headcount investment") both address G-001 — verify these are complementary, not contradictory.
   → Resolve via /ea-grill phase-b
```
Only flag when the title or description contains obviously opposing terms. If ambiguous, skip.

**Bootstrap mechanism:** Scan phase-b artifacts for rows where G-NNN and STR-NNN co-occur in the same table row or section. Propose each candidate pair for confirmation before linking.

**After view:** Return to the persistent menu (Step 3).

---

### View 3: Strategy → Requirement

**Entity sources:**
- STR-NNN: scan `EA-projects/{slug}/artifacts/phase-b/*.md`
- REQ-NNN: read `EA-projects/{slug}/artifacts/requirements/requirements-index.json` — include all requirements with status `Draft` or `Approved` only (exclude `Deferred`, `Rejected`, `Waived`)

**Render matrix:** rows = STR-NNN, columns = REQ-NNN, link type = `supports`

**Gaps section:**

For each STR-NNN with no outgoing `supports` link:
```
⚠️ STR-001 has no requirements supporting it
   → Derive requirements via /ea-requirements add or /ea-interview phase-b
   → Or add a link: {"from":"STR-001","to":"REQ-XXX","type":"supports"}
```

For each active (Draft/Approved) REQ-NNN with no incoming `supports` link:
```
⚠️ REQ-003 is not linked to any strategy
   → Bootstrap: [offer if co-occurrence found]
   → Or link manually: add {"from":"STR-XXX","to":"REQ-003","type":"supports"}
```

**Contradictions section:**

Two requirements with the same `nfrSubType` (e.g. both `Performance`) that both have `supports` links to the same STR-NNN but have different `measurableTarget` values:
```
⚠️ REQ-001 (Performance: <200ms p95) and REQ-004 (Performance: <500ms p95) both support STR-002 — conflicting NFR targets for the same strategy.
   → Reconcile via /ea-grill or update one requirement's measurableTarget
```
Only flag when both `nfrSubType` and `measurableTarget` are non-null and the targets differ.

**Bootstrap mechanism:** Scan phase-b artifacts for rows where STR-NNN and REQ-NNN co-occur in the same table row or section. For each candidate pair found, propose: `Found REQ-001 co-mentioned with STR-001 in Business Architecture — add link supports? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 4: Requirement → Capability

**Entity sources:**
- REQ-NNN: read `requirements-index.json` — Draft and Approved only
- CAP-NNN: scan `EA-projects/{slug}/artifacts/phase-b/*.md`

**Render matrix:** rows = REQ-NNN, columns = CAP-NNN, link type = `satisfiedBy`

**Gaps section:**

For each active REQ-NNN with no outgoing `satisfiedBy` link:
```
⚠️ REQ-001 has no capability satisfying it
   → Bootstrap: [offer if co-occurrence found]
   → Or define a capability via /ea-interview phase-b
   → Or add: {"from":"REQ-001","to":"CAP-XXX","type":"satisfiedBy"}
```

For each CAP-NNN with no incoming `satisfiedBy` link:
```
⚠️ CAP-005 is not linked to any requirement
   → Verify this capability is in scope, or link it to a requirement
```

**Contradictions section:**

Two requirements with the same `nfrSubType` both linked (`satisfiedBy`) to the same CAP-NNN but with different `measurableTarget` values:
```
⚠️ REQ-001 (Availability: 99.9%) and REQ-006 (Availability: 95%) both map to CAP-003 — conflicting NFR targets for the same capability.
   → Reconcile targets or split into separate capabilities
   → Resolve via /ea-grill
```
Only flag when both `nfrSubType` and `measurableTarget` are non-null and the targets differ.

**Bootstrap mechanism:** Scan phase-b artifacts for rows where REQ-NNN and CAP-NNN co-occur in the same table row or section. For each candidate pair found, propose: `Found CAP-003 co-mentioned with REQ-001 in Business Architecture — add link satisfiedBy? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 5: Capability → Work Package

**Entity sources:**
- CAP-NNN: scan `EA-projects/{slug}/artifacts/phase-b/*.md`
- WP-NNN: scan `EA-projects/{slug}/artifacts/phase-e/*.md` (Architecture Roadmap)

**Render matrix:** rows = CAP-NNN, columns = WP-NNN, link type = `deliveredBy`

**Gaps section:**

For each CAP-NNN with no outgoing `deliveredBy` link:
```
⚠️ CAP-003 has no work package delivering it
   → Add a work package via /ea-artifact or /ea-interview phase-e
   → Or add: {"from":"CAP-003","to":"WP-XXX","type":"deliveredBy"}
```

For each WP-NNN with no incoming `deliveredBy` link:
```
⚠️ WP-004 does not deliver any capability
   → Link to a capability or verify this WP is in scope
```

**Contradictions section:**

Detect sequencing issues: if two capabilities A and B both appear in the phase-b artifact and A's description or the Architecture Vision implies A depends on B (e.g. "CAP-001 builds on CAP-003" or "CAP-001 requires CAP-003 to be in place"), but the WP delivering A (WP-001) is in an earlier wave than the WP delivering B (WP-004):
```
⚠️ CAP-001 (delivered by WP-001, Wave 1) references CAP-003 (delivered by WP-004, Wave 2) — verify Wave 1 delivery of CAP-001 is not blocked by Wave 2 delivery of CAP-003.
   → Review roadmap sequencing via /ea-grill phase-e
```
Wave number is extracted from the WP row in the Roadmap artifact (look for a `Wave` or `Phase` column). Only flag when the wave numbers can be unambiguously read. If not found, skip contradiction detection for this view.

**Bootstrap mechanism:** Scan phase-e (Roadmap) artifact for rows where CAP-NNN and WP-NNN co-occur in the same table row. For each candidate pair found, propose: `Found WP-002 co-mentioned with CAP-003 in Architecture Roadmap — add link deliveredBy? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 6: Requirement → ABB

**Entity sources:**
- REQ-NNN: read `requirements-index.json` — Draft and Approved only
- ABB-NNN: scan `EA-projects/{slug}/artifacts/phase-c*/**/*.md` and `EA-projects/{slug}/artifacts/phase-d*/**/*.md` for tokens matching `ABB-\d{3}`

**Render matrix:** rows = REQ-NNN, columns = ABB-NNN, link type = `realisedBy`

**Gaps section:**

For each active REQ-NNN with no outgoing `realisedBy` link:
```
⚠️ REQ-001 has no ABB realising it
   → Define an ABB via /ea-interview phase-c or phase-d
   → Or add: {"from":"REQ-001","to":"ABB-XXX","type":"realisedBy"}
```

For each ABB-NNN with no incoming `realisedBy` link:
```
⚠️ ABB-003 is not linked to any requirement
   → Verify this ABB is in scope, or link it to a requirement
```

**Contradictions section:**

Two ABBs linked (`realisedBy`) to the same REQ-NNN but with overlapping or conflicting domain assignments (e.g. both ABBs claim to be the primary realisation of the same requirement in different architecture layers):
```
⚠️ ABB-001 (Application) and ABB-002 (Technology) both realise REQ-003 — verify this dual realisation is intentional, or split the requirement.
   → Resolve via /ea-grill phase-c
```
Only flag when the ABB descriptions or domain fields clearly indicate overlapping scope.

**Bootstrap mechanism:** Scan phase-c (Application Architecture) and phase-d (Technology Architecture) artifacts for rows where REQ-NNN and ABB-NNN co-occur in the same table row or section. For each candidate pair found, propose: `Found ABB-001 co-mentioned with REQ-001 in Technology Architecture — add link realisedBy? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 7: ABB → SBB

**Entity sources:**
- ABB-NNN: scan `EA-projects/{slug}/artifacts/phase-c*/**/*.md` and `EA-projects/{slug}/artifacts/phase-d*/**/*.md` for tokens matching `ABB-\d{3}`
- SBB-NNN: scan `EA-projects/{slug}/artifacts/phase-d*/**/*.md` for tokens matching `SBB-\d{3}` (Technology Architecture SBB Register)

**Render matrix:** rows = ABB-NNN, columns = SBB-NNN, link type = `implementedBy`

**Gaps section:**

For each ABB-NNN with no outgoing `implementedBy` link:
```
⚠️ ABB-001 has no SBB implementing it
   → Select an SBB via /ea-interview phase-d
   → Or add: {"from":"ABB-001","to":"SBB-XXX","type":"implementedBy"}
```

For each SBB-NNN with no incoming `implementedBy` link:
```
⚠️ SBB-002 is not linked to any ABB
   → Verify this SBB is in scope, or link it to an ABB
   → An SBB without an ABB may indicate vendor-first selection — flag as anti-pattern
```

**Contradictions section:**

Two SBBs linked (`implementedBy`) to the same ABB-NNN but with conflicting vendor constraints or overlapping functional scope:
```
⚠️ SBB-001 (AWS CloudTrail) and SBB-002 (Azure Monitor) both implement ABB-001 (Immutable Log Store) — verify multi-cloud intent, or consolidate to a single SBB per environment.
   → Resolve via /ea-grill phase-d
```

**Bootstrap mechanism:** Scan Technology Architecture artifact SBB Register table for rows where ABB-NNN and SBB-NNN co-occur in the same table row. For each candidate pair found, propose: `Found SBB-001 co-mentioned with ABB-001 in Technology Architecture — add link implementedBy? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 8: SBB → Story

**Entity sources:**
- SBB-NNN: scan `EA-projects/{slug}/artifacts/phase-d*/**/*.md` for tokens matching `SBB-\d{3}`
- STY-NNN: scan `EA-projects/{slug}/artifacts/requirements/*.md` and `EA-projects/{slug}/artifacts/phase-e*/**/*.md` for tokens matching `STY-\d{3}`

**Render matrix:** rows = SBB-NNN, columns = STY-NNN, link type = `deliveredAs`

**Gaps section:**

For each SBB-NNN with no outgoing `deliveredAs` link:
```
⚠️ SBB-001 has no story delivering it
   → Create a story via /ea-interview phase-e or /ea-detail new STY-NNN
   → Or add: {"from":"SBB-001","to":"STY-XXX","type":"deliveredAs"}
```

For each STY-NNN with no incoming `deliveredAs` link:
```
⚠️ STY-003 is not linked to any SBB
   → Verify this story is in scope, or link it to an SBB
   → A story without an SBB may be an enabler story — tag as [Enabler] if so
```

**Contradictions section:**

Two stories linked (`deliveredAs`) to the same SBB-NNN but with conflicting acceptance criteria or actor goals:
```
⚠️ STY-001 ("As an operator, I want automated backups") and STY-002 ("As a security officer, I want encrypted backups") both deliver SBB-001 (AWS Backup) — verify both acceptance criteria are supported by the same SBB version.
   → Resolve via /ea-grill phase-e
```

**Bootstrap mechanism:** Scan requirements and phase-e artifacts for rows where SBB-NNN and STY-NNN co-occur in the same table row or section. For each candidate pair found, propose: `Found STY-001 co-mentioned with SBB-001 in Requirements Register — add link deliveredAs? [Y/n]`. On Y: append link, update `lastUpdated`, write `traceability-index.json`, rebuild indexes, show updated matrix.

**After view:** Return to the persistent menu (Step 3).

---

### View 9: Gap → Work Package (read-only)

**Entity sources:**
- GAP-NNN: read `engagement.json → direction.gaps[]` — each entry's `id` and `linkedWorkPackages` field
- WP-NNN: scan `EA-projects/{slug}/artifacts/phase-e*/**/*.md` for tokens matching `WP-\d{3}`

**Render matrix:** rows = GAP-NNN, columns = WP-NNN. A cell is marked `R` (resolves) when the WP appears in the gap's `linkedWorkPackages`. This view renders from the gaps register only — it does NOT read or write `traceability-index.json`, and no bootstrap mechanism applies. Edit links via `/ea-gaps update GAP-NNN linkedWorkPackages WP-NNN`.

**Gaps section:**

For each GAP-NNN with an empty `linkedWorkPackages`:
```
⚠️ GAP-001 ({severity}) has no work package resolving it
   → Link one via /ea-gaps update GAP-001 linkedWorkPackages WP-NNN
   → Or accept the gap deliberately and record the acceptance in the Gap Analysis
```

For each WP-NNN appearing in no gap's `linkedWorkPackages`:
```
⚠️ WP-002 resolves no recorded gap — orphaned work package
   → Verify the WP traces to a goal/objective instead (see T3-ROAD-WP), or link a gap
```

**After view:** Return to the persistent menu (Step 3).

---

### View 10: Requirement → Work Package (derived, read-only)

**Entity sources:**
- REQ-NNN: scan `EA-projects/{slug}/artifacts/requirements/*.md` for tokens matching `REQ-\d{3}`
- WP-NNN: scan `EA-projects/{slug}/artifacts/phase-e*/**/*.md` for tokens matching `WP-\d{3}`

**Render matrix:** rows = REQ-NNN, columns = WP-NNN. A cell is marked `~` (derived) when a transitive path exists in `traceability-index.json`: REQ —`satisfiedBy`→ CAP —`deliveredBy`→ WP. This view is a composition of Views 4 and 5 — it writes nothing and has no bootstrap mechanism. To change it, edit the underlying links via View 4 or View 5.

**Gaps section:**

For each REQ-NNN with no derived path to any WP:
```
⚠️ REQ-003 has no delivery path (no Requirement → Capability → Work Package chain)
   → Add the missing link via View 4 (Requirement → Capability) or View 5 (Capability → Work Package)
```

**After view:** Return to the persistent menu (Step 3).

---

## Step 5 — Write Links

When a user confirms a bootstrap suggestion or manually adds a link (by typing the JSON):

1. Parse the link object: `{"from": "X", "to": "Y", "type": "Z"}`
2. Validate that `type` is one of the eight types: `motivates`, `addresses`, `supports`, `satisfiedBy`, `deliveredBy`, `realisedBy`, `implementedBy`, `deliveredAs`
3. Check for duplicates: if an identical `from`/`to`/`type` triple already exists, skip and notify: `Link already exists — no change made.`
4. Append to the `links` array in `traceability-index.json`
5. Set `lastUpdated` to the current ISO 8601 timestamp
6. Write the file
7. Rebuild the outgoing and incoming indexes
8. Recount gaps and return to menu

---

## Step 6 — Full Gap Report

Triggered by menu option 11 or the `--gaps` argument.

Run all ten views silently (generate findings but do not render matrices). Collect all gap and contradiction findings. Print:

```
Full Gap Report — {engagement name}
════════════════════════════════════════════════════
Generated: {ISO timestamp}

Summary
───────────────────────────────────────────────────
Driver → Goal             {N} gaps, {N} contradictions
Goal → Strategy           {N} gaps, {N} contradictions
Strategy → Requirement    {N} gaps, {N} contradictions
Requirement → Capability  {N} gaps, {N} contradictions
Capability → Work Package {N} gaps, {N} contradictions
Requirement → ABB         {N} gaps, {N} contradictions
ABB → SBB                 {N} gaps, {N} contradictions
SBB → Story               {N} gaps, {N} contradictions
Gap → Work Package        {N} gaps
Requirement → Work Package {N} gaps

Total: {N} gaps, {N} contradictions

── Gaps ────────────────────────────────────────────
[All gap findings, grouped by view, with fix actions]

── Contradictions ──────────────────────────────────
[All contradiction findings, grouped by view]

✅ No gaps found.   ← shown only if total gaps = 0
```

After the report, offer:
```
  1. Open a specific view  →  enter 1–10
  2. Run /ea-consistency for artifact-level checks
  Q. Quit
```
