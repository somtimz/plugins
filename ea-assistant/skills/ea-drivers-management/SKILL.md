---
name: ea-drivers-management
description: This skill should be used when the user asks to "manage business drivers", "add a driver", "view drivers", "list drivers", "trace a driver to goals", "update the drivers register", or "generate the drivers register". Handles the full driver lifecycle from capture through traceability and linkage to goals and strategies.
version: 0.9.84
---

# EA Drivers Management

Business Drivers Management captures, classifies, traces, and manages the external pressures and internal imperatives that justify an architecture engagement. Drivers sit at the top of the motivation chain and every goal must trace to at least one driver.

## Business Drivers Storage

Business drivers are stored in `engagement.json → direction.drivers[]`. This is the single source of truth.

The generated register file (`artifacts/cross-cutting/drivers-register.md`) is output only — never edited directly. Re-generate it with `/ea-drivers generate` after any updates; the previous version is archived to `snapshots/` per the register snapshot convention.

## Schema

```json
{
  "id": "DRV-NNN",
  "statement": "",
  "type": "External | Internal",
  "priority": "High | Medium | Low",
  "evidence": "",
  "linkedGoals": ["G-NNN"]
}
```

**Field definitions:**
- `statement` — the business pressure or imperative in plain language (e.g. "Regulatory mandates for data residency in the EU by 2027")
- `type` — `External`: market forces, regulatory requirements, competitive pressure, customer demands; `Internal`: strategic initiatives, cost targets, capability gaps, board mandates
- `priority` — relative importance for this engagement (High / Medium / Low)
- `evidence` — source document, metric, or external reference that substantiates this driver; strongly recommended for credibility; absence flagged as a warning
- `linkedGoals` — array of G-NNN IDs representing goals that respond to this driver

## ID Assignment Algorithm

1. Read `engagement.json → direction.drivers[]`.
2. If the array is empty or missing, assign `DRV-001`.
3. Otherwise: extract all existing IDs matching `DRV-\d{3}`, find the maximum numeric suffix N, assign `DRV-{N+1}` zero-padded to 3 digits.
4. IDs are permanent — once assigned, never reused or reassigned even if the driver is removed.

## Driver Lifecycle

Drivers have no explicit status field — they are either present in `engagement.json` (active) or removed (if confirmed invalid or superseded by a refined statement). Unlike policies or constraints, drivers are not "waived" or "retired" — they are either true drivers of the engagement or they are not.

When removing a driver: check whether any goals in `direction.goals[]` have `drivers: ["DRV-NNN"]` referencing it. If so, warn before removal and offer to update the linked goals first.

## Traceability Walk Algorithm

Starting from a DRV-NNN:

1. **Goals:** Read `direction.goals[]`, collect all entries where `drivers` array contains `DRV-NNN` → set of G-NNN IDs
2. **Objectives:** Read `direction.objectives[]`, collect entries where `linkedGoal` is in the goal set → set of OBJ-NNN IDs
3. **Strategies:** Read `direction.strategies[]`, collect entries where `supports` array intersects the goal set or objective set → set of STR-NNN IDs
4. **Work Packages:** Scan Architecture Roadmap artifact (`artifacts/phase-e/architecture-roadmap.md` or any file matching `gap-analysis*.md` or `architecture-roadmap*.md`) for WP-NNN table rows where `Advances Goals/Objectives` or `Executes Strategies` column references any ID in the goal, objective, or strategy sets

Flag any referenced IDs not found in `engagement.json` as broken links.

## Register Format

The generated `drivers-register.md` follows this structure:

```markdown
---
artifact: Drivers Register
artifactId: drivers-register
engagement: {name}
phase: cross-cutting
status: Draft
generated: {YYYY-MM-DD}
---

# Business Drivers Register

**Engagement:** {name}
**Generated:** {YYYY-MM-DD}
**Total Drivers:** {N} ({N} External, {N} Internal)

---

## DRV-NNN: {statement truncated to 60 chars}

| Field | Value |
|---|---|
| **ID** | DRV-NNN |
| **Statement** | {full statement} |
| **Type** | External / Internal |
| **Priority** | High / Medium / Low |
| **Evidence** | {evidence or —} |
| **Linked Goals** | {G-NNN, G-NNN or —} |

### Downstream Chain
- **Goals:** G-NNN — {statement}, G-NNN — {statement}
- **Objectives:** OBJ-NNN — {statement}
- **Strategies:** STR-NNN — {statement}
- **Work Packages:** WP-NNN — {name}
```

## Validation Rules

| Rule | Check | Action |
|---|---|---|
| Orphan driver | `linkedGoals` is empty or null | Flag with ⚠️ in `list`; suggest `/ea-drivers update DRV-NNN linkedGoals G-NNN` |
| No evidence | `evidence` is blank | Flag with ⚠️ No evidence cited in `list` |
| Broken goal reference | G-NNN in `linkedGoals` not found in `direction.goals[]` | Flag as broken link in `trace` output |
| Duplicate ID | Two entries share the same `id` value | Report and offer to renumber the second entry |

## Integration Points

- **`/ea-engage-review`** — checks DRV-NNN → G-NNN chain coverage in the Alignment dimension
- **`/ea-interview start engagement`** — captures drivers during engagement-level interviews; recorded in `direction.drivers[]`
- **`/ea-brainstorm`** — top-3 priority drivers pre-filled as context in the Goals dimension
- **`/ea-grill` on Architecture Vision** — direction quality check verifies every goal traces to a driver
- **`/ea-trace`** — full motivation chain view includes DRV-NNN as the top tier
