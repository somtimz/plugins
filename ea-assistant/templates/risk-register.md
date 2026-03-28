---
artifact: Risk Register
artifactId: risk-register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<details>
<summary>📋 Guidance</summary>

The Risk Register is a cross-cutting artifact that aggregates and tracks all architecture risks
across the engagement — from initial identification in the Architecture Vision through to
delivery in the Migration Plan. Use `/ea-risks` to generate or update this register; it will
scan all artifacts for risk content and compile them here.

A risk is an uncertain future event or condition that, if it occurs, will have a negative effect
on one or more objectives. Every risk must have a likelihood, impact, and mitigation strategy.

Risk rating is derived from likelihood × impact:
  Critical: High likelihood + High impact
  High:     High likelihood + Medium impact, OR Medium likelihood + High impact
  Medium:   Medium likelihood + Medium impact, OR High/Low likelihood + Low/High impact
  Low:      Low likelihood + Low/Medium impact

Statuses:
  Open:       Active risk — mitigation planned or in progress
  Monitoring: Risk is being watched; likelihood has reduced but not closed
  Accepted:   Risk acknowledged with no mitigation (owner accepts consequence)
  Closed:     Risk no longer applies (resolved, expired, or fully mitigated)

</details>

# Risk Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Generated:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Risk Summary

| Total | Critical | High | Medium | Low | Open | Monitoring | Accepted | Closed |
|---|---|---|---|---|---|---|---|---|
| {{total}} | {{critical}} | {{high}} | {{medium}} | {{low}} | {{open}} | {{monitoring}} | {{accepted}} | {{closed}} |

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
| **ID** | RIS-001 |
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

| Source Artifact | Risks Contributed |
|---|---|
| Architecture Vision | {{RIS_ids}} |
| Statement of Architecture Work | {{RIS_ids}} |
| Migration Plan | {{RIS_ids}} |
| Architecture Compliance Assessment | {{RIS_ids}} |
| Other | {{RIS_ids}} |

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
