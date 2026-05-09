---
name: ea-trace
description: Interactive traceability views across the motivation chain — Driver → Goal → Strategy → Requirement → Capability → Work Package — with gap and contradiction detection
argument-hint: "[--gaps]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

You are executing the `/ea-trace` command.

## Overview

Renders traceability views across the EA motivation chain. Reads from `traceability-index.json` (graph of cross-entity links) and artifact files. Surfaces gaps (missing links) and contradictions (conflicting relationships) with suggested fix actions.

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
  6. Full gap report               (all views, gaps + contradictions only)
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
