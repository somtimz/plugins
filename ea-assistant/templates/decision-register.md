---
artifact: Decision Register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
generated: {{YYYY-MM-DD}}
filters: {{applied_filters_or_None}}
audience: {{audience_or_All}}
taxonomy:
  domain: Cross-cutting
  category: Register
  audience: Governance
  layer: Governance
  sensitivity: Internal
  tags: [decisions, register, a3, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| All A3 decisions consolidated | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Decision Register aggregates all Appendix A3 Decision Log rows from every artifact into a single cross-engagement view, enabling governance authorities to see the full decision landscape without navigating individual artifacts. It is the primary governance accountability tool: who decided what, at what authority level, and whether the rationale has been documented.

**What to include:** All A3 Decision Log rows across all artifacts, organised by status, domain, or audience (use `/ea-decisions` with filters). Strategic decisions must have A3.N rationale blocks — the register surfaces which strategic decisions are missing rationale documentation. Do not edit this register directly — regenerate it from source A3 tables.

**Quality indicators:**
- Every Strategic decision has a linked A3.N rationale block in its source artifact — the register makes missing rationale visible
- The register is regenerated at each phase gate to ensure currency — a stale decision register misleads governance authorities
- Filter views are tailored to the audience — an ARB briefing view should show only Strategic decisions pending or recently ratified

**Common mistakes:**
- Using the Decision Register as the primary authoring surface — decisions are authored in artifact A3 tables; the register is a view, not a source
- Including A3 entries for trivial decisions (wording changes, date corrections) — A3 should capture governance-material decisions only; the register reflects this discipline

**TOGAF reference:** TOGAF 10 §38 — Architecture Governance. The Decision Register provides the governance audit trail of all significant decisions made across the ADM cycle, satisfying the governance accountability requirements.

</details>

# Decision Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Filters applied:** {{applied_filters_or_None}}
**Audience:** {{audience_or_All}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of all A3 governance decisions across the engagement: count by authority level and verification status.
Diagram: Decision status summary chart
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Summary

| Total | Open | Verified | Voted | Fiat | Returned |
|---|---|---|---|---|---|
| {{total}} | {{open}} | {{verified}} | {{voted}} | {{fiat}} | {{returned}} |

| Authority | Total | Open |
|---|---|---|
| Strategic | {{strategic_total}} | {{strategic_open}} |
| Tactical | {{tactical_total}} | {{tactical_open}} |
| Operational | {{operational_total}} | {{operational_open}} |

| Domain | Total | Open |
|---|---|---|
| Business | {{business_total}} | {{business_open}} |
| Data | {{data_total}} | {{data_open}} |
| Application | {{app_total}} | {{app_open}} |
| Technology | {{tech_total}} | {{tech_open}} |
| Cross | {{cross_total}} | {{cross_open}} |

---

## Open Decisions — Action Required

<details>
<summary>📋 Guidance</summary>

All decisions with state: Provisional, Awaiting Verification, or Returned.
These require an owner to act before they can be considered resolved.

</details>

| # | Item | Value | State | Owner | Authority | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

---

## By Authority

### Strategic Decisions

<details>
<summary>📋 Guidance</summary>

Enterprise-wide, long-term commitments. High scrutiny — these bind the organisation.

</details>

| # | Item | Value | State | Owner | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Tactical Decisions

| # | Item | Value | State | Owner | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Operational Decisions

| # | Item | Value | State | Owner | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

---

## By Domain

### Business

| # | Item | Value | State | Owner | Authority | Cost | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{cost}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Data

| # | Item | Value | State | Owner | Authority | Cost | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{cost}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Application

| # | Item | Value | State | Owner | Authority | Cost | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{cost}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Technology

| # | Item | Value | State | Owner | Authority | Cost | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{cost}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Cross-Domain

| # | Item | Value | State | Owner | Authority | Cost | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{cost}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

---

## By Cost Profile

### High Cost

| # | Item | Value | State | Owner | Authority | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Medium Cost

| # | Item | Value | State | Owner | Authority | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

### Low Cost

| # | Item | Value | State | Owner | Authority | Domain | Impact | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{impact}} | {{risk}} | {{source_artifact}} | {{date}} |

---

## By Impact Profile

### High Impact

| # | Item | Value | State | Owner | Authority | Domain | Cost | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{risk}} | {{source_artifact}} | {{date}} |

### Medium Impact

| # | Item | Value | State | Owner | Authority | Domain | Cost | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{risk}} | {{source_artifact}} | {{date}} |

### Low Impact

| # | Item | Value | State | Owner | Authority | Domain | Cost | Risk | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{risk}} | {{source_artifact}} | {{date}} |

---

## By Risk Level

### High Risk

| # | Item | Value | State | Owner | Authority | Domain | Cost | Impact | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{impact}} | {{source_artifact}} | {{date}} |

### Medium Risk

| # | Item | Value | State | Owner | Authority | Domain | Cost | Impact | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{impact}} | {{source_artifact}} | {{date}} |

### Low Risk

| # | Item | Value | State | Owner | Authority | Domain | Cost | Impact | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{impact}} | {{source_artifact}} | {{date}} |

---

## Full Decision Index

<details>
<summary>📋 Guidance</summary>

Complete flat table of all decisions in this register, regardless of filters.
Sortable reference for architects and auditors.

</details>

| # | Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Source Artifact | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| {{n}} | {{item}} | {{value}} | {{state}} | {{captured_by}} | {{owner}} | {{authority}} | {{domain}} | {{cost}} | {{impact}} | {{risk}} | {{subject}} | {{source_artifact}} | {{date}} |

---

**State legend:** 🔄 Provisional | ⏳ Awaiting Verification | ✓ Verified | 🗳️ Under Vote | ✅ Voted | 👑 Fiat | ↩️ Returned

*This document was generated using the EA Assistant plugin via `/ea-decisions`.*
*Source artifacts scanned: {{source_artifacts_scanned}}*
*Regenerate with `/ea-decisions` to pick up new decisions from A3 tables.*

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
