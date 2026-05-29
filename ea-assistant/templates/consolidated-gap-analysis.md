---
artifactId: consolidated-gap-analysis
artifact: Consolidated Gap Analysis
artifactId: consolidated-gap-analysis
engagement: {{engagement_name}}
phase: E
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Analysis
  audience: Architecture
  layer: Transition
  sensitivity: Internal
  tags: [gaps, consolidation, roadmap-input, phase-e]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3 | ⚠️ Pending | |
| T3-A4 | ⚠️ Pending | |
| T3-ADR | ⚠️ Pending | |
| T3-RATIONALE | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Consolidated Gap Analysis aggregates and reconciles domain-level gap analyses (from Phases B, C, and D) into a single cross-domain view. It identifies interdependencies between domain gaps, resolves conflicts where domain gaps overlap, and produces the prioritised gap list that drives the Architecture Roadmap work package structure.

**What to include:** A consolidated gap register with all GAP-NNN entries from all domains, cross-domain dependencies (where a gap in one domain blocks or amplifies a gap in another), priority assignments informed by business impact across domains (not just within a domain), and the connection to Architecture Roadmap work packages (WP-NNN). Do not replace domain gap analyses — they remain authoritative per-domain records.

**Quality indicators:**
- Every gap from the domain-level gap analyses appears here — missing gaps mean the roadmap will be incomplete
- Cross-domain dependencies are explicitly mapped — "GAP-B-003 (missing capability) depends on GAP-D-001 (missing platform) being resolved first"
- Priority assignments are consistent across domains — if Business gap GAP-B-003 and Data gap GAP-D-001 both affect the same goal, they should have consistent priority weighting

**Common mistakes:**
- Consolidating only the text from domain analyses without synthesising cross-domain insights — the value of this artifact is the cross-domain view, not a concatenation
- Assigning all gaps the same priority — if everything is high priority, nothing is; the consolidated view should enable sequencing decisions
- Not connecting gaps to roadmap work packages — every gap must trace to a WP that will address it

**TOGAF reference:** TOGAF 10 Part III, Phase E (§29) — the Consolidated Gap Analysis is the cross-domain synthesis that drives the Architecture Roadmap and Transition Architecture planning.

</details>

# Consolidated Gap Analysis

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Provide a brief summary of the total number of gaps across all domains, the highest-priority
gaps, and the overall migration challenge. This section is for executive and programme sponsor
consumption.

</details>

{{executive_summary}}

**Total gaps identified:** {{total_gaps}}
**Critical/High priority gaps:** {{high_priority_count}}

---

## Domain Gap Summary

<details>
<summary>📋 Guidance</summary>

Summarise the gap count and key findings from each domain analysis.
Link to the domain-level gap analysis artifacts for full detail.

</details>

| Domain | Source Artifact | Total Gaps | High | Medium | Low | Key Findings |
|---|---|---|---|---|---|---|
| Business | [Gap Analysis — Business Architecture](../phase-b/gap-analysis-business.md) | {{count}} | {{h}} | {{m}} | {{l}} | {{findings}} |
| Data | [Gap Analysis — Data Architecture](../phase-c-data/gap-analysis-data.md) | {{count}} | {{h}} | {{m}} | {{l}} | {{findings}} |
| Application | [Gap Analysis — Application Architecture](../phase-c-app/gap-analysis-application.md) | {{count}} | {{h}} | {{m}} | {{l}} | {{findings}} |
| Technology | [Gap Analysis — Technology Architecture](../phase-d/gap-analysis-technology.md) | {{count}} | {{h}} | {{m}} | {{l}} | {{findings}} |

---

## Consolidated Gap Register

<details>
<summary>📋 Guidance</summary>

List all gaps from all domains in a single register, ordered by priority.
Assign consolidated GAP-NNN IDs sequentially across all domains.
The "Domain" column indicates which domain-level analysis originated the gap.

</details>

| Gap ID | Domain | Description | Category | Priority | Baseline State | Target State | Effort | Evidence | Related Gaps |
|---|---|---|---|---|---|---|---|---|---|
| [GAP-001](../details/GAP-001.md) | Business | {{description}} | Missing capability | High | {{baseline}} | {{target}} | High | {{evidence}} | [→](../details/GAP-001.md) |
| [GAP-002](../details/GAP-002.md) | Data | {{description}} | {{category}} | {{priority}} | {{baseline}} | {{target}} | {{effort}} | {{evidence}} | GAP-001 |

---

## Cross-Domain Dependencies

<details>
<summary>📋 Guidance</summary>

Identify gaps that span multiple domains or where closing one domain's gap is a
prerequisite or enabler for another. These dependencies inform the sequencing of
work packages in the Architecture Roadmap.

</details>

| Primary Gap | Dependent Gap | Dependency Type | Sequencing Implication |
|---|---|---|---|
| [GAP-001](../details/GAP-001.md) | GAP-004 | Prerequisite | GAP-001 must be closed before GAP-004 begins |

---

## Reconciliation Notes

<details>
<summary>📋 Guidance</summary>

Document any conflicts or inconsistencies found when reconciling domain gap analyses —
for example, where two domain analyses make assumptions about the same system or data asset
that are mutually inconsistent. Record the resolution decision.

</details>

{{reconciliation_notes}}

---

## Roadmap Input Summary

<details>
<summary>📋 Guidance</summary>

Map gaps to candidate work packages for the Architecture Roadmap. This section is the
direct feed from gap analysis to roadmap construction.

</details>

| Work Package Candidate | Closes Gaps | Priority | Effort Estimate | Recommended Wave |
|---|---|---|---|---|
| {{wp_candidate}} | GAP-001, GAP-002 | High | {{effort}} | Wave 1 |

---

## Appendix A3 — Decision Log

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

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

*This document was created using the EA Assistant plugin.*
