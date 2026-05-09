# Design Spec: /ea-trace — EA Traceability Views

**Date:** 2026-05-08
**Status:** Approved
**Plugin:** ea-assistant
**Target version:** 0.9.44

---

## 1. Problem

The ea-assistant has no dedicated way to trace entities across the motivation architecture (drivers → goals → strategies → requirements → capabilities → work packages). The existing `/ea-requirements trace` produces a flat requirements-to-artifact matrix. There is no view of the full motivation chain, no gap detection across entity types, and no contradiction surfacing.

---

## 2. Solution

A new `/ea-trace` command with a persistent menu of traceability views. Each view traverses one link in the motivation chain, surfaces gaps (missing links) and contradictions (conflicting relationships), and suggests a fix action. A `traceability-index.json` graph file stores all cross-entity links.

---

## 3. Data Model

### 3.1 `traceability-index.json`

New file at `EA-projects/{slug}/artifacts/requirements/traceability-index.json`.

```json
{
  "lastUpdated": "YYYY-MM-DDTHH:MM:SSZ",
  "links": [
    {"from": "DRV-001", "to": "G-001",   "type": "motivates"},
    {"from": "G-001",   "to": "STR-001", "type": "addresses"},
    {"from": "STR-001", "to": "REQ-001", "type": "supports"},
    {"from": "REQ-001", "to": "CAP-003", "type": "satisfiedBy"},
    {"from": "CAP-003", "to": "WP-002",  "type": "deliveredBy"}
  ]
}
```

### 3.2 Link Type Vocabulary

| Type | From | To | Meaning |
|---|---|---|---|
| `motivates` | DRV-NNN | G-NNN | Driver motivates a goal |
| `addresses` | G-NNN | STR-NNN | Goal is addressed by a strategy |
| `supports` | STR-NNN | REQ-NNN | Requirement supports a strategy |
| `satisfiedBy` | REQ-NNN | CAP-NNN | Requirement is satisfied by a capability |
| `deliveredBy` | CAP-NNN | WP-NNN | Capability is delivered by a work package |

### 3.3 Backward Compatibility

`requirements-index.json` is unchanged. Existing engagements start with an empty `links` array — all entities appear as gaps until links are added.

### 3.4 Future Link Types (v2)

Reserved for v2 (not implemented in v1):

| Type | From | To |
|---|---|---|
| `ownedBy` | REQ-NNN | Stakeholder |
| `measuredBy` | G-NNN | MET-NNN |
| `enabledBy` | VS-NNN | CAP-NNN |

---

## 4. Command: `/ea-trace`

### 4.1 Entry Point

1. Resolve active engagement (check context; if none, scan `EA-projects/*/engagement.json` and prompt).
2. Load `traceability-index.json` (create empty file if absent).
3. Build a quick gap count per view by scanning entity IDs in relevant artifact files and comparing against links in the graph.
4. Display the persistent menu.

### 4.2 Persistent Menu

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

After any view completes, return to this menu.

### 4.3 View Output Format

Each view renders:

1. **Matrix** — rows are the "from" entities, columns are the "to" entities; cells show ✅ (linked), ⬜ (not linked).
2. **Gaps section** — each unlinked entity with a suggested fix action.
3. **Contradictions section** — conflicting relationships with a suggested resolution action.

Example (Strategy → Requirement):

```
Strategy → Requirement
══════════════════════════════════════════════════════

Strategy              | REQ-001 | REQ-002 | REQ-003
STR-001 Cost Reduce   | ✅      | ⬜      | ✅
STR-002 CX Improve    | ⬜      | ✅      | ⬜
[No strategy]         |         |         | ⬜      ← REQ-002 unlinked

Gaps (2):
⚠️ REQ-002 is not linked to any strategy
   → Bootstrap: found STR-002 co-mentioned in Biz Arch — add this link? [Y/n]
   → Or link manually: add {"from":"STR-002","to":"REQ-002","type":"supports"}

⚠️ STR-002 links to only 1 requirement — verify coverage is complete
   → Review via /ea-grill phase-b

Contradictions (1):
⚠️ REQ-001 and REQ-003 both support STR-001 but have conflicting NFR targets (99.9% vs 95% availability)
   → Resolve via /ea-grill

[Return to menu: Enter | Quit: Q]
```

### 4.4 Gap Detection Logic

| View | Gap condition | Contradiction condition |
|---|---|---|
| Driver → Goal | Driver in Architecture Vision with no `motivates` link; Goal with no incoming `motivates` link | Two goals motivated by the same driver with conflicting priorities |
| Goal → Strategy | Goal with no `addresses` link; Strategy with no incoming `addresses` link | Strategy contradicts another strategy addressing the same goal |
| Strategy → Requirement | Strategy with no `supports` link; Requirement with no incoming `supports` link | Two requirements supporting the same strategy have conflicting NFR targets |
| Requirement → Capability | Approved/Draft requirement with no `satisfiedBy` link; Capability in Phase B with no incoming `satisfiedBy` link | Two requirements link to same capability with conflicting NFR targets |
| Capability → Work Package | Capability with no `deliveredBy` link; WP in Roadmap that delivers no capability | Capability linked to WP scheduled in a later wave than a dependent capability |

### 4.5 Bootstrap Mechanism

When a "from" entity has no outgoing links of the relevant type, the command:

1. Scans the relevant artifact file (e.g., Business Architecture for STR→REQ) for ID co-occurrences in the same table row or section.
2. Surfaces candidate links: `"Found CAP-007 co-mentioned with REQ-001 in Business Architecture — add link? [Y/n]"`
3. On confirmation, appends the link to `traceability-index.json` and updates `lastUpdated`.

### 4.6 Full Gap Report (option 6)

Runs all five views silently (no matrices). Prints only the Gaps and Contradictions sections, consolidated:

```
Full Gap Report — {engagement name}
════════════════════════════════════

Driver → Goal          2 gaps, 0 contradictions
Goal → Strategy        1 gap,  0 contradictions
Strategy → Requirement 3 gaps, 1 contradiction
Requirement → Capability 2 gaps, 0 contradictions
Capability → Work Package 4 gaps, 0 contradictions

[Gaps and contradictions listed...]
```

---

## 5. Artifact Sources per View

| View | Entity sources |
|---|---|
| Driver → Goal | Architecture Vision (`phase-a/`) for DRV-NNN and G-NNN |
| Goal → Strategy | Architecture Vision for G-NNN; Business Architecture (`phase-b/`) for STR-NNN |
| Strategy → Requirement | Business Architecture for STR-NNN; `requirements/requirements.md` for REQ-NNN |
| Requirement → Capability | `requirements/requirements.md` for REQ-NNN; Business Architecture for CAP-NNN |
| Capability → Work Package | Business Architecture for CAP-NNN; Architecture Roadmap (`phase-e/`) for WP-NNN |

---

## 6. Files Changed

| File | Change |
|---|---|
| `commands/ea-trace.md` | New command |
| `skills/ea-requirements-management/SKILL.md` | Add `traceability-index.json` schema + link type vocabulary |
| `commands/ea-requirements.md` | Update `trace` mode note to point to `/ea-trace` for full views |
| `commands/ea-help.md` | Add `/ea-trace` row |
| `CLAUDE.md` | Bump command count (35 → 36) |
| `.claude-plugin/plugin.json` | Version bump → 0.9.44 |
| `../.claude-plugin/marketplace.json` | Version bump → 0.9.44, match description |

---

## 7. Out of Scope (v1)

- Stakeholder → Requirement view
- Goal → Metric view
- Value Stream → Capability view
- Auto-resolving contradictions
- Exporting the traceability graph to docx/xlsx
