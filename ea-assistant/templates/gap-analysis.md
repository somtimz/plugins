---
artifact: Gap Analysis
engagement: {{engagement_name}}
phase: {{phase}}
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Analysis
  audience: Architecture
  layer: Transition
  sensitivity: Internal
  tags: [gaps, baseline, target, phase-e]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

Gap Analysis documents the differences between the Baseline (current) and Target architectures.
A separate Gap Analysis is typically produced for each architecture domain (B, C-Data, C-App, D).
Gaps feed directly into the Architecture Roadmap in Phase E.

</details>

# Gap Analysis — {{domain}} Architecture

**Engagement:** {{engagement_name}}
**Domain:** {{domain}} (Business / Data / Application / Technology)
**Date:** {{YYYY-MM-DD}}

---

## Baseline Architecture Summary

<details>
<summary>📋 Guidance</summary>

Brief description of the current state architecture for this domain.
Reference the relevant baseline artifact if it exists.

</details>

{{baseline_summary}}

---

## Target Architecture Summary

<details>
<summary>📋 Guidance</summary>

Brief description of the target state architecture for this domain.
Reference the target architecture document.

</details>

{{target_summary}}

---

## Gap Register

<details>
<summary>📋 Guidance</summary>

List each gap between baseline and target.
Categories: Missing capability, Retiring component, Consolidation, New requirement, Enhancement

</details>

| Gap ID | Description | Category | Priority | Baseline State | Target State | Effort | Evidence |
|---|---|---|---|---|---|---|---|
| GAP-001 | {{description}} | Missing capability | High/Med/Low | {{baseline}} | {{target}} | High/Med/Low | {{evidence}} |

---

## Capability Gap Register

<details>
<summary>📋 Guidance</summary>

Capability gaps are the primary output of Phase B gap analysis. Each row represents a capability
that is absent or below the required maturity level. These gaps prevent Goals from being achieved
and drive Work Package definitions in Phase E.

Populate from Business Architecture §3 — copy any row where Current Maturity is below Target
Maturity. Link each gap to the G-NNN or OBJ-NNN it prevents.

</details>

| CAP-NNN | Capability | L1 Domain | Current Maturity | Target Maturity | Prevents (G-NNN / OBJ-NNN) | Priority | Evidence |
|---|---|---|---|---|---|---|---|
| CAP-001 | {{capability_name}} | {{domain}} | Absent / Immature / Developing | {{target}} | {{G-NNN}} | High / Med / Low | {{evidence}} |

---

## Zachman Coverage Analysis

<details>
<summary>📋 Guidance</summary>

Assess Zachman cell coverage for this domain. Identify which cells have gaps.

</details>

| | What (Data) | How (Function) | Where (Network) | Who (People) | When (Time) | Why (Motivation) |
|---|---|---|---|---|---|---|
| **Executive** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Business** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Architect** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Engineer** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Legend: ✅ Covered | ⚠️ Partial | ⬜ Gap

---

## Recommended Actions

| Gap ID | Recommended Action | Phase | Owner |
|---|---|---|---|
| GAP-001 | {{action}} | E / F | {{owner}} |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Each row captures the decision item, agreed value, governance state, who captured it,
who owns or must verify it, and classification fields used by /ea-decisions.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |


## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.
Use `/ea-adrs` to manage the ADR Register and surface ADR summaries.

When a significant decision is made during an interview for this artifact, the
`ea-interviewer` will suggest creating an ADR if the decision meets the threshold
criteria (technology/vendor selection, high cost/risk, hard to reverse, etc.).

</details>

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

---

*This document was created using the EA Assistant plugin.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
