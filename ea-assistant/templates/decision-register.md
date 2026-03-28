---
artifact: Decision Register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
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
---

<details>
<summary>📋 Guidance</summary>

The Decision Register aggregates all Appendix A3 Decision Log rows from every artifact
in this engagement into a single cross-artifact view. It is generated on demand via
/ea-decisions and can be tailored to any audience, decision maker, domain, or status.
Rows are sourced from A3 tables; do not edit this document directly — regenerate it.

</details>

# Decision Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Filters applied:** {{applied_filters_or_None}}
**Audience:** {{audience_or_All}}

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
