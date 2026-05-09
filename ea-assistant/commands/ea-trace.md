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
