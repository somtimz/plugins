---
artifact: ADR Register
artifactId: adr-register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [Preliminary, Requirements, A, B, C-Data, C-App, D, E, F, G, H]
  zachmanCell: ""
  domain: Cross-cutting
  category: Register
  audience: Governance
  layer: Governance
  sensitivity: Internal
  tags: [adr, decisions, register, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| All ADRs indexed and cross-referenced | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The ADR Register is a cross-cutting artifact that aggregates all Architecture Decision Records
(ADRs) for the engagement into a single navigable view. Use `/ea-adrs` to generate or update
this register; it will scan all `adr-*.md` files in the artifacts directory.

ADR lifecycle:
  Candidate   → Decision identified; options analysis not yet started
  In Progress → Options analysis underway; decision not yet made
  Completed   → Decision made and documented
  Superseded  → Replaced by a newer ADR (link shown)
  Deprecated  → No longer applicable (reason recorded)

Each ADR has a stable `ADR-NNN` identifier. When an ADR supersedes another, the old ADR is
marked Superseded and the new ADR ID is recorded. The superseding chain is preserved.

Use `/ea-adrs status` for an inline summary without writing a file.
Use `/ea-adrs new` to create a new ADR document.
Use `/ea-adrs update ADR-NNN <field> <value>` to update a single field.

**Quality indicators:**
- Every ADR in the engagement has an entry here — if an ADR-NNN ID is referenced in an artifact but does not appear in this register, the register is incomplete
- Superseded ADRs are retained (with supersession link) — deleting superseded ADRs destroys the decision history
- Status is current — In Progress ADRs that have not been updated in 30+ days need a review

**Common mistakes:**
- Manually editing the register instead of using `/ea-adrs` — manual edits drift from source ADR files; regenerate from source
- Omitting PAD-NNN links — where an ADR was preceded by a Pending Architecture Decision, the link should appear in the register for traceability
- Register not updated when ADRs change status — a Completed ADR that still shows In Progress creates false information about the decision portfolio

**TOGAF reference:** TOGAF 10 §35 — Architecture Repository, Architecture Decisions. The ADR Register is the decision index within the Architecture Repository, maintaining the authoritative history of all significant architecture choices.

</details>

# ADR Register — {{engagement_name}}

**Engagement:** {{engagement_name}}
**Generated:** {{YYYY-MM-DD}}
**Phase:** All Phases

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of architecture decisions made in this engagement: count by status and domain, and key decisions requiring executive awareness.
Diagram: Decision timeline (key decisions only)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Summary

| Status | Count |
|---|---|
| Candidate | {{N}} |
| In Progress | {{N}} |
| Completed | {{N}} |
| Superseded | {{N}} |
| Deprecated | {{N}} |
| **Total** | **{{N}}** |

---

## 2. All ADRs by Phase

### Preliminary

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Preliminary)* | — | — | — | — | — |

### Phase A — Architecture Vision

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase A)* | — | — | — | — | — |

### Phase B — Business Architecture

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase B)* | — | — | — | — | — |

### Phase C — Information Systems Architecture

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase C)* | — | — | — | — | — |

### Phase D — Technology Architecture

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase D)* | — | — | — | — | — |

### Phase E — Opportunities and Solutions

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase E)* | — | — | — | — | — |

### Phase F — Migration Planning

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase F)* | — | — | — | — | — |

### Phase G — Implementation Governance

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase G)* | — | — | — | — | — |

### Phase H — Architecture Change Management

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no ADRs in Phase H)* | — | — | — | — | — |

### Cross-Phase / Engagement-Wide

| ADR ID | Title | Status | Owner | Date | Superseded By |
|---|---|---|---|---|---|
| *(no cross-phase ADRs)* | — | — | — | — | — |

---

## 3. Open ADRs (Candidate + In Progress)

*ADRs requiring action — options analysis or decision pending.*

| ADR ID | Title | Status | Owner | Phase | Age (days) | Next Action |
|---|---|---|---|---|---|---|
| *(no open ADRs)* | — | — | — | — | — | — |

---

## 4. Completed ADRs

*Decisions made and documented.*

| ADR ID | Title | Chosen Option | Owner | Completed | A3 Reference |
|---|---|---|---|---|---|
| *(no completed ADRs)* | — | — | — | — | — |

---

## 5. Superseded ADRs

*ADRs replaced by newer decisions.*

| ADR ID | Title | Superseded By | Date Superseded | Reason |
|---|---|---|---|---|
| *(no superseded ADRs)* | — | — | — | — |

---

## 6. ADR — Artifact Impact Map

*Shows which artifacts are materially affected by each ADR.*

| ADR ID | Title | Affected Artifacts | Nature of Impact |
|---|---|---|---|
| *(populate from ADR §9 Affected Artifacts)* | — | — | — |

---

## 7. Decision Chain — Supersession Tree

*Traces ADR lineage where one decision replaced another.*

```
ADR-NNN: {original title}
  └─ Superseded by ADR-NNN: {newer title}
       └─ Superseded by ADR-NNN: {latest title}  ← current
```

*(no supersession chains recorded)*

---

## Artifact Working Notes

> Working-layer: persists across reviews. Populated by `/ea-grill` (Critiques), `/ea-review` (Comments), and manually. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

*Ad-hoc notes from architects, reviewers, or stakeholders.*

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Critiques

*Formal findings from `/ea-grill` or `/ea-review` that require a response before this artifact can be approved.*

| # | Section | Finding | Source | Date | Status |
|---|---|---|---|---|---|
| — | — | — | — | — | Open |

### Exceptions

*Formal exceptions granted to a standard, principle, or compliance rule — each must have a rationale and approver.*

| # | Rule / Principle Waived | Rationale | Approver | Date |
|---|---|---|---|---|
| — | — | — | — | — |

### Outstanding Tasks

*Things that must be completed before this artifact can move to Approved status.*

- [ ] *(Add tasks — e.g. "Populate §3 Assumptions before Phase B sign-off")*

*Generated by `/ea-adrs generate`. Use `/ea-adrs status` for an inline view. Use `/ea-adrs new` to create a new ADR.*
