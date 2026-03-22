---
artifact: Compliance Assessment
engagement: {{engagement_name}}
phase: G
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  A Compliance Assessment is a Phase G artifact that evaluates whether an implemented (or
  in-progress) solution conforms to the agreed architecture. Assessments are typically triggered
  by scheduled review gates defined in the Architecture Contract, or by a concern raised by
  the architecture team. The output is an objective record of conformance, non-conformances,
  and required remediation actions. Non-conformances must be tracked to closure.
-->

# Compliance Assessment

**Engagement:** {{engagement_name}}
**Assessment Reference:** {{assessment_reference}}
**Organisation:** {{organisation}}
**Assessor:** {{assessor}}
**Solution / Project Assessed:** {{solution_name}}
**Architecture Contract Reference:** {{contract_reference}}
**Assessment Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## 1. Assessment Purpose

<!-- GUIDANCE:
  State why this assessment is being conducted and what triggered it. Reference the Architecture
  Contract review schedule if this is a planned gate review, or describe the concern that
  triggered an ad-hoc assessment. State the expected outcome (confirm conformance, identify
  remediation actions, support go/no-go decision).
-->

{{assessment_purpose}}

**Assessment Type:** Scheduled gate / Ad-hoc / Pre-deployment / Post-implementation
**Go/No-Go Decision Required:** Yes / No

---

## 2. Scope

<!-- GUIDANCE:
  Define what is in scope for this assessment. List the solution components, architecture domains
  (business, data, application, technology), and Architecture Contract requirements being assessed.
  Be explicit about what is NOT being assessed to manage expectations.
-->

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Contract Requirements Assessed
{{requirements_assessed}}

---

## 3. Compliance Criteria

<!-- GUIDANCE:
  List the specific criteria against which the solution is being assessed. These should map
  directly to the Architecture Contract conformance requirements (ACR-xxx) and agreed standards.
  Each criterion must be objectively assessable — define what evidence will demonstrate compliance.
-->

| Criteria ID | Description | Source | Evidence Required |
|---|---|---|---|
| ACR-001 | {{description}} | Architecture Contract | {{evidence_required}} |
| ACR-002 | {{description}} | Architecture Contract | {{evidence_required}} |
| {{criteria_id}} | {{description}} | {{source}} | {{evidence_required}} |

---

## 4. Findings

<!-- GUIDANCE:
  Record the assessment findings for each criterion. Findings should be factual and evidence-based.
  Do not conflate observations with judgements. Reference specific evidence (document names,
  test results, code review observations) to support each finding.
-->

| Criteria ID | Finding | Evidence Reviewed | Compliance Status |
|---|---|---|---|
| ACR-001 | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |
| ACR-002 | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |
| {{criteria_id}} | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |

### Overall Compliance Summary
{{overall_compliance_summary}}

---

## 5. Non-conformances

<!-- GUIDANCE:
  Record each non-conformance identified. A non-conformance is a deviation from a mandatory
  requirement in the Architecture Contract. For each, assign a severity, identify the required
  remediation action, and set a target resolution date. Non-conformances must be tracked to
  closure — either by remediation or by a formal architecture waiver (documented change request).
-->

| NC ID | Description | Criteria ID | Severity | Required Action | Target Resolution | Owner |
|---|---|---|---|---|---|---|
| NC-001 | {{description}} | ACR-xxx | Critical / Major / Minor | {{action}} | {{date}} | {{owner}} |
| NC-002 | {{description}} | ACR-xxx | Critical / Major / Minor | {{action}} | {{date}} | {{owner}} |

**Total Non-conformances:** {{nc_count}}
**Critical:** {{critical_count}} | **Major:** {{major_count}} | **Minor:** {{minor_count}}

---

## 6. Recommendations

<!-- GUIDANCE:
  Provide recommendations beyond mandatory remediation — these address advisory guidance
  deviations or improvement opportunities identified during the assessment. Recommendations
  are not blocking but should be tracked. Include a recommendation for the go/no-go decision
  if this assessment feeds one.
-->

| Rec ID | Recommendation | Priority | Owner |
|---|---|---|---|
| REC-001 | {{recommendation}} | High / Med / Low | {{owner}} |

### Go / No-Go Recommendation
<!-- GUIDANCE:
  If this assessment feeds a deployment or phase-gate decision, state the recommendation clearly.
  If recommending conditional approval, list the conditions that must be met.
-->

**Recommendation:** Go / No-Go / Conditional Go

**Conditions (if Conditional Go):**
{{conditions}}

**Rationale:**
{{go_nogo_rationale}}

---

## 7. Sign-off

<!-- GUIDANCE:
  The assessor and the solution lead should both sign. The assessor confirms the assessment
  is accurate and objective. The solution lead acknowledges the findings and commits to
  remediation. For go/no-go decisions, the architecture authority must also sign.
-->

| Role | Name | Organisation | Signature | Date |
|---|---|---|---|---|
| Assessor | {{assessor}} | {{assessor_org}} | | |
| Solution Lead | {{solution_lead}} | {{solution_org}} | | |
| Architecture Authority | {{architecture_authority}} | {{arch_org}} | | |

---

*This document was created using the EA Assistant plugin.*
