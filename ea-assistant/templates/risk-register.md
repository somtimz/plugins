---
artifact: Risk Register
artifactId: risk-register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.59
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Register
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [risks, register, mitigation, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Risks linked to goals/objectives | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The Risk Register is a cross-cutting artifact that aggregates and tracks all architecture risks
across the engagement — from initial identification in the Architecture Vision through to
delivery in the Migration Plan. Use `/ea-risks` to generate or update this register; it will
scan all artifacts for risk content and compile them here.

A risk is an uncertain future event or condition that, if it occurs, will have a negative effect
on one or more objectives. Every risk must have a likelihood, impact, and mitigation strategy.

Risk rating is derived from likelihood × impact using a 3×3 matrix (High/Medium/Low for both
axes). Do NOT extend the scale to add a "Very High" likelihood or impact tier unless you
explicitly define it in the rating scale table — an undefined scale level leaves practitioners
unable to classify risks consistently and creates gaps in heatmap coverage. If the engagement
requires a fourth tier, define it with a concrete description (e.g., "Very High likelihood:
near-certain even with planned controls in place") before using it.

  Critical: High likelihood + High impact
  High:     High likelihood + Medium impact, OR Medium likelihood + High impact
  Medium:   Medium likelihood + Medium impact, OR High/Low likelihood + Low/High impact
  Low:      Low likelihood + Low/Medium impact

**Binding mitigations for high-consequence risks:** Mitigations for Critical or High risks
should be stated as binding conditions of deployment or operation approval — not as
recommendations. Use "required before deployment" or "mandatory control", not "should" or
"is recommended." Agentic AI risks, citizen data risks, and enforcement-adjacent risks warrant
this treatment regardless of overall rating.

Statuses:
  Open:       Active risk — mitigation planned or in progress
  Monitoring: Risk is being watched; likelihood has reduced but not closed
  Accepted:   Risk acknowledged with no mitigation (owner accepts consequence)
  Closed:     Risk no longer applies (resolved, expired, or fully mitigated)

**Quality indicators:**
- Every risk has a named owner (a person, not a team) who is accountable for the mitigation
- Critical and High risks have specific mitigations, not generic statements ("monitor closely" is not a mitigation for a High-impact risk)
- The register is reviewed at every phase gate — stale risks (not reviewed in 60+ days) should be either updated or closed

**Common mistakes:**
- Accepting risks without documenting the consequence if they materialise — "Accepted" without a consequence statement is not risk management
- Risk descriptions so vague they cannot be monitored ("risk of scope creep") — every risk should be specific enough that the owner knows what to watch for
- No connection to architecture mitigations — where a risk is mitigated by an architecture decision (ADR-NNN), record the link

**TOGAF reference:** TOGAF 10 §28 — Architecture Risk Management. The Risk Register is maintained as a cross-cutting artifact throughout the ADM cycle, from Architecture Vision through Phase H.

</details>

# Risk Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Status of key architecture risks: total count, severity distribution, and top risks requiring executive attention.
Diagram: Risk heat map (likelihood × impact)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Risk Summary

| Total | Critical | High | Medium | Low | Open | Monitoring | Accepted | Closed |
|---|---|---|---|---|---|---|---|---|
| {{total}} | {{critical}} | {{high}} | {{medium}} | {{low}} | {{open}} | {{monitoring}} | {{accepted}} | {{closed}} |

---

## Risk Appetite & Tolerance

<details>
<summary>📋 Guidance</summary>

The appetite statement records how much risk the organisation is willing to carry in pursuit of the engagement's goals — agreed with the sponsor, not assumed. Tolerance thresholds make the appetite operational: they determine who may accept a risk at each rating and when escalation is mandatory. `/ea-risks accept` enforces the acceptance-authority column.

</details>

**Appetite statement:** {{risk_appetite_statement}}

| Rating | Tolerance | Acceptance authority | Escalation trigger |
|---|---|---|---|
| Critical | {{tolerance_critical — e.g. "Outside appetite — must be mitigated or escalated"}} | Sponsor | Immediately on identification |
| High | {{tolerance_high}} | Sponsor or ARB | Open > 30 days without mitigation plan |
| Medium | {{tolerance_medium}} | Lead architect | Open > 90 days |
| Low | {{tolerance_low — e.g. "Within appetite — monitor"}} | Lead architect | — |

---

## Critical Risks

<details>
<summary>📋 Guidance</summary>

Critical risks have High likelihood AND High impact. These require immediate attention,
active mitigation, and should be escalated to the programme sponsor. Each critical risk
should have a named owner and a documented response plan with a target resolution date.

</details>

---

### RIS-001: {{risk_title}}

| Field | Value |
|---|---|
| **ID** | [[RIS-001]] |
| **Description** | {{what_could_happen_and_why}} |
| **Source** | {{artifact_name_where_risk_was_identified}} |
| **Phase Identified** | {{ADM_phase}} |
| **Likelihood** | High / Medium / Low |
| **Impact** | High / Medium / Low |
| **Rating** | Critical / High / Medium / Low |
| **Affected Objectives** | OBJ-NNN, G-NNN (which goals or objectives this risk threatens) |
| **Mitigation** | {{what_action_reduces_the_likelihood_or_impact}} |
| **Contingency** | {{what_to_do_if_the_risk_materialises}} |
| **Owner** | {{name_and_role}} |
| **Status** | Open / Monitoring / Accepted / Closed |
| **Last Reviewed** | {{YYYY-MM-DD}} |
| **Details** | [[RIS-001\|→]] |

---

## High Risks

<details>
<summary>📋 Guidance</summary>

High risks have High likelihood + Medium impact, or Medium likelihood + High impact.
These should have documented mitigations and be reviewed at every architecture checkpoint.

</details>

---

### RIS-00N: {{risk_title}}

| Field | Value |
|---|---|
| **ID** | RIS-00N |
| **Description** | {{what_could_happen_and_why}} |
| **Source** | {{artifact_name_where_risk_was_identified}} |
| **Phase Identified** | {{ADM_phase}} |
| **Likelihood** | High / Medium / Low |
| **Impact** | High / Medium / Low |
| **Rating** | Critical / High / Medium / Low |
| **Affected Objectives** | OBJ-NNN, G-NNN |
| **Mitigation** | {{mitigation_action}} |
| **Contingency** | {{contingency_plan}} |
| **Owner** | {{name_and_role}} |
| **Status** | Open / Monitoring / Accepted / Closed |
| **Last Reviewed** | {{YYYY-MM-DD}} |
| **Details** | [[RIS-001\|→]] |

---

## Medium Risks

<details>
<summary>📋 Guidance</summary>

Medium risks should be tracked and assigned owners, but do not require escalation.
Review at phase boundaries or when related decisions are made.

</details>

---

### RIS-00N: {{risk_title}}

| Field | Value |
|---|---|
| **ID** | RIS-00N |
| **Description** | {{what_could_happen_and_why}} |
| **Source** | {{artifact_name_where_risk_was_identified}} |
| **Phase Identified** | {{ADM_phase}} |
| **Likelihood** | High / Medium / Low |
| **Impact** | High / Medium / Low |
| **Rating** | Critical / High / Medium / Low |
| **Affected Objectives** | OBJ-NNN, G-NNN |
| **Mitigation** | {{mitigation_action}} |
| **Contingency** | {{contingency_plan}} |
| **Owner** | {{name_and_role}} |
| **Status** | Open / Monitoring / Accepted / Closed |
| **Last Reviewed** | {{YYYY-MM-DD}} |

---

## Low Risks

<details>
<summary>📋 Guidance</summary>

Low risks are logged for awareness. No active mitigation is required unless likelihood
or impact changes. Review annually or at major phase transitions.

</details>

---

### RIS-00N: {{risk_title}}

| Field | Value |
|---|---|
| **ID** | RIS-00N |
| **Description** | {{what_could_happen_and_why}} |
| **Source** | {{artifact_name_where_risk_was_identified}} |
| **Phase Identified** | {{ADM_phase}} |
| **Likelihood** | High / Medium / Low |
| **Impact** | High / Medium / Low |
| **Rating** | Critical / High / Medium / Low |
| **Affected Objectives** | OBJ-NNN, G-NNN |
| **Mitigation** | {{mitigation_action}} |
| **Contingency** | {{contingency_plan}} |
| **Owner** | {{name_and_role}} |
| **Status** | Open / Monitoring / Accepted / Closed |
| **Last Reviewed** | {{YYYY-MM-DD}} |

---

## Closed / Accepted Risks

<details>
<summary>📋 Guidance</summary>

Closed risks are retained for audit and lessons-learned purposes.
Accepted risks are retained to provide governance evidence that the risk was known and
a conscious decision was made not to mitigate.

</details>

| ID | Description | Rating | Resolution | Closed Date |
|---|---|---|---|---|
| RIS-00N | {{description}} | Critical / High / Medium / Low | Mitigated / Expired / Accepted — {{reason}} | {{YYYY-MM-DD}} |

---

## Risk Heatmap Summary

| | **High Impact** | **Medium Impact** | **Low Impact** |
|---|---|---|---|
| **High Likelihood** | Critical | High | Medium |
| **Medium Likelihood** | High | Medium | Low |
| **Low Likelihood** | Medium | Low | Low |

*Current risks by cell — populated by `/ea-risks generate`:*

| Rating Cell | Risks |
|---|---|
| Critical (H×H) | {{list_of_RIS_ids}} |
| High (H×M, M×H) | {{list_of_RIS_ids}} |
| Medium (M×M, H×L, L×H) | {{list_of_RIS_ids}} |
| Low (M×L, L×M, L×L) | {{list_of_RIS_ids}} |

---

## Source Artifact Cross-Reference

*Generated dynamically from actual sources — one row per artifact that contributed risks.*

| Source Artifact | Risks Contributed |
|---|---|
| {{source_artifact}} | {{RIS_ids}} |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record decisions made in the context of this risk register — e.g., decisions to accept
a risk, decisions to close a risk without mitigation, or governance approvals for risk
tolerance thresholds. Use A3 rows for decisions with strategic or cross-artifact impact.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | | | | | | | | | | | |

---

*This document was generated using the EA Assistant plugin.*
*Run `/ea-risks` to refresh risk aggregation from all artifacts.*

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
