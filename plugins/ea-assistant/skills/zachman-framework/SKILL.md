---
name: Zachman Framework
description: This skill should be used when the user asks to "classify an artifact using Zachman", "which Zachman cell does this belong to", "apply the Zachman framework", "map requirements to Zachman", "what row and column is this", or when classifying EA artifacts, viewpoints, or concerns against the Zachman Framework. Provides full 6×6 Zachman classification guidance.
version: 0.1.0
---

# Zachman Framework

The Zachman Framework is a classification schema for organising architecture artefacts by **audience (rows)** and **interrogative (columns)**. Use it to classify, cross-reference, and identify gaps in EA artefacts.

## The 6×6 Grid

### Rows (Audiences / Perspectives)

| Row | Stakeholder | Perspective |
|---|---|---|
| 1 | Executive / Planner | Contextual — scope and concepts |
| 2 | Business Manager / Owner | Conceptual — business model |
| 3 | Architect / Designer | Logical — system model |
| 4 | Engineer / Builder | Physical — technology model |
| 5 | Technician / Implementer | Detailed — component model |
| 6 | Enterprise / Worker | Functioning enterprise |

### Columns (Interrogatives / Concerns)

| Column | Interrogative | Describes |
|---|---|---|
| 1 | What (Data) | Entities, data, information |
| 2 | How (Function) | Processes, functions, activities |
| 3 | Where (Network) | Locations, nodes, infrastructure |
| 4 | Who (People) | Organisations, roles, actors |
| 5 | When (Time) | Events, cycles, schedules |
| 6 | Why (Motivation) | Goals, strategies, rules |

## Classification Workflow

To classify an artefact:

1. Identify the **primary audience** — who is this for? → determines the row
2. Identify the **primary concern** — what does it describe? → determines the column
3. State the cell: e.g. `Row 2 / Column 1 (Business Manager — What/Data)`
4. Note: many artefacts span multiple cells — identify the primary and secondary cells

### Quick Classification Examples

| Artefact | Row | Column | Cell |
|---|---|---|---|
| Architecture Vision | 1–2 | 6 (Why) | Executive/Business — Motivation |
| Business Process Model | 2 | 2 (How) | Business Manager — Function |
| Logical Data Model | 3 | 1 (What) | Architect — Data |
| Application Architecture | 3–4 | 2 (How) | Architect/Engineer — Function |
| Network Topology | 4 | 3 (Where) | Engineer — Network |
| Security Policy | 2 | 6 (Why) | Business Manager — Motivation |
| Migration Plan | 3–4 | 5 (When) | Architect/Engineer — Time |
| Stakeholder Map | 1–2 | 4 (Who) | Executive/Business — People |
| Requirements Register | 2–3 | 6 (Why) | Business/Architect — Motivation |
| Technology Standards | 4 | 1–3 (What/How/Where) | Engineer — Data/Function/Network |

## Applying Zachman in an EA Engagement

When reviewing the artifact set for an engagement:

1. Map each artifact to its Zachman cell(s)
2. Identify **gaps** — cells with no coverage
3. Flag **conflicts** — artefacts in the same cell that contradict each other
4. Use the matrix to communicate scope to stakeholders (rows 1–2 are executive; rows 3–5 are technical)

### Gap Identification

Present coverage as a matrix. Use ✅ (covered), ⚠️ (partial), ❌ (missing):

```
         What    How    Where   Who    When   Why
Row 1    ✅      ❌     ❌      ✅     ❌     ✅
Row 2    ⚠️      ✅     ❌      ✅     ❌     ✅
Row 3    ✅      ✅     ⚠️      ❌     ❌     ⚠️
...
```

## Relationship to TOGAF

TOGAF and Zachman complement each other:
- TOGAF provides the **process** (ADM phases)
- Zachman provides the **classification** (what each artefact represents)

Map TOGAF ADM phases to Zachman rows:
- Phase A (Architecture Vision) → Rows 1–2
- Phases B/C/D (Architecture domains) → Rows 2–4
- Phase E/F (Roadmap/Migration) → Rows 3–5 (When column)
- Phase G (Governance) → Row 2 (Who/Why columns)

## Additional Resources

- **`references/zachman-cell-descriptions.md`** — Detailed description of all 36 cells with examples
- **`references/togaf-zachman-mapping.md`** — Full mapping of TOGAF artefacts to Zachman cells
