# Reference Architecture Feature Design

**Date:** 2026-06-11
**Status:** Approved
**Scope:** ea-assistant plugin

---

## Overview

Add support for creating, managing, and using Reference Architectures (RA-NNN) within the ea-assistant plugin. A reference architecture is a named architectural pattern with ABB/SBB references, key decisions, constraints, and implied principles — a reusable template an engagement can adopt and adapt.

---

## 1. ID Scheme

New prefix: `RA-NNN` (e.g. `RA-001`)

Added to:
- `CLAUDE.md` ID Scheme table
- `templates/seeds/engagement-rules.md`
- `skills/ea-engagement-lifecycle/references/engagement-rules-reference.md`

---

## 2. Storage

### Repo-level (cross-engagement)

```
Architecture-Repository/
└── reference-library/
    ├── reference-architecture-index.md
    └── entries/
        └── RA-NNN.md
```

### Per-engagement (local, not shared)

```
EA-Projects/{slug}/artifacts/cross-cutting/reference-architectures/
├── reference-architecture-index.md
└── RA-NNN.md
```

Per-engagement RAs use the same ID format; IDs allocated from `engagement.json → localRA.nextId`. If an engagement is later linked to a repo that already contains RA entries, the local IDs are kept as-is (they are scoped by location, not globally unique). `/ea-refarch show` resolves repo-first to avoid ambiguity; local-only IDs are labelled `(local)` in list output.

---

## 3. RA-NNN Entry Schema

### Frontmatter

```yaml
---
id: RA-001
name: Event-Driven Microservices
domain: Application              # Business | Data | Application | Technology | Cross-cutting
status: Approved                 # Draft | Approved | Deprecated
version: 1.0.0
source: internal                 # internal | industry
linkedSTDs: []
linkedADRs: []
createdDate: YYYY-MM-DD
lastModified: YYYY-MM-DD
---
```

### Markdown sections

| Section | Content |
|---|---|
| `## Overview` | Description and when to use the pattern |
| `## Architecture Layers` | Table: layer → ABB-NNN references |
| `## Key Decisions` | Table: decision title, rationale summary, candidate ADR title |
| `## Constraints` | Table: description + candidate CST title |
| `## Implied Principles` | BP/DP/AP/TP IDs or descriptions this RA assumes |
| `## Adoption Notes` | What is mandatory vs. flexible when adopting |
| `## Grill Checklist` | Explicit checks run by `/ea-grill` when RA is adopted |

The `## Grill Checklist` section drives the grill integration — each item is a testable statement against the engagement's artifacts.

---

## 4. `repo.json` Changes

New block added alongside `sib`, `vendorLandscape`, `technologyHorizon`:

```json
"referenceArchitecture": {
  "enabled": true,
  "indexFile": "reference-library/reference-architecture-index.md",
  "entriesPath": "reference-library/entries/",
  "nextId": 1
}
```

`/ea-repo init` updated to:
- create `Architecture-Repository/reference-library/entries/`
- write `reference-library/reference-architecture-index.md` stub
- seed `referenceArchitecture` block in `repo.json`

`/ea-repo status` updated to show RA count.

---

## 5. `engagement.json` Changes

Two new fields:

```json
"adoptedRAs": [],
"localRA": { "nextId": 1 }
```

`/ea-new` seeds both fields in all new engagements.

---

## 6. `/ea-refarch` Command

New top-level command. Modes:

| Mode | Syntax | Behaviour |
|---|---|---|
| `new` | `/ea-refarch new [--local]` | Interview: name, domain, source. Creates RA-NNN.md stub. `--local` writes to engagement's `artifacts/cross-cutting/reference-architectures/`; default writes to repo. |
| `list` | `/ea-refarch list [--local]` | Table of all RAs (id, name, domain, status). Default = repo; `--local` = engagement; both shown with scope column if both exist. |
| `show` | `/ea-refarch show RA-NNN` | Renders full RA-NNN.md. Searches repo first, then local. |
| `edit` | `/ea-refarch edit RA-NNN` | Guided re-editing of RA sections. |
| `adopt` | `/ea-refarch adopt RA-NNN` | Records RA-NNN in `engagement.json → adoptedRAs[]`. Surfaces RA's ABBs and key decisions as suggestions (user confirms each). |
| `unadopt` | `/ea-refarch unadopt RA-NNN` | Removes from `adoptedRAs[]`. Warns if grill checks reference it. |
| `status` | `/ea-refarch status` | Lists adopted RAs and their grill-check coverage for active engagement. |

---

## 7. Engagement Integration Points

No new commands required for these — hooks into existing flow:

| Integration point | Behaviour |
|---|---|
| Phase C/D interview | If `adoptedRAs[]` non-empty, surfaces RA `## Architecture Layers` ABBs as candidates |
| Phase C/D interview | Surfaces RA `## Key Decisions` as candidate ADRs |
| `/ea-grill` | Runs `## Grill Checklist` items from each adopted RA as an additional check block |
| `/ea-abbs`, `/ea-sbbs` | When creating ABB/SBB in a domain covered by an adopted RA, surfaces RA layer catalogue as reference |
| `/ea-repo status` | Shows RA entry count alongside STD/VDR/THR |

---

## 8. Files to Create / Modify

### New files

| File | Purpose |
|---|---|
| `commands/ea-refarch.md` | `/ea-refarch` command definition |
| `skills/ea-architecture-repository/references/reference-architecture-schema.md` | RA-NNN schema reference |
| `templates/seeds/ra-entry-template.md` | Blank RA-NNN.md template used by `new` mode |
| `templates/seeds/ra-index.md` | Blank reference-architecture-index.md stub |

### Modified files

| File | Change |
|---|---|
| `CLAUDE.md` | Add `RA-NNN` to ID Scheme table |
| `skills/ea-architecture-repository/SKILL.md` | Add Reference Architecture register section + workspace structure update |
| `skills/ea-architecture-repository/references/repo-schema.md` | Add `referenceArchitecture` block to repo.json fields |
| `commands/ea-repo.md` | Add `entries/` creation + index stub + `referenceArchitecture` seeding to `init` mode; add RA count to `status` mode |
| `commands/ea-new.md` | Seed `adoptedRAs` and `localRA` in new engagement.json |
| `commands/ea-abbs.md` | Surface adopted RA layer catalogue when creating ABBs |
| `commands/ea-sbbs.md` | Surface adopted RA layer catalogue when creating SBBs |
| `skills/ea-grill-skills/SKILL.md` | Add RA grill check block |
| `templates/seeds/engagement-rules.md` | Add RA-NNN to ID scheme |
| `skills/ea-engagement-lifecycle/references/engagement-rules-reference.md` | Add RA-NNN to ID scheme |
| `commands/ea-help.md` | Add `/ea-refarch` to commands table |
| `.claude-plugin/plugin.json` | Version bump |
| `../. claude-plugin/marketplace.json` | Version bump + description sync |
| `docs/PRD.md` | Document new feature |
| `README.md` | Add `/ea-refarch` to feature bullets and commands table |

---

## 9. Out of Scope

- Generative adoption (auto-writing ABB stubs / ADR entries into engagement artifacts) — can be added on top later
- RA versioning / diff tracking beyond the `version` frontmatter field
- Cross-RA dependency modelling
