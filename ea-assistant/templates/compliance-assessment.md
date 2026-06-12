---
artifact: Compliance Assessment
artifactId: compliance-assessment
engagement: {{engagement_name}}
phase: G
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Internal
  tags: [compliance, conformance, assessment, phase-g]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-ADR | ⚠️ Pending | |
| Linked to Architecture Contract | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** A Compliance Assessment records whether an implemented or in-progress solution conforms to the agreed architecture. It is the mechanism that transforms architecture governance from aspiration into evidence — a completed assessment is the architect's formal statement that a solution has been reviewed against the Architecture Contract and Architecture Principles.

**What to include:** The assessment scope (which work packages and solution components were reviewed), the conformance criteria (which Architecture Contract clauses and Architecture Principles were assessed), the findings (conformant items, non-conformances with severity and remediation actions), and the overall conformance status. Non-conformances must be tracked to closure.

**Quality indicators:**
- Each finding references a specific criterion from the Architecture Contract or an Architecture Principle (BP/DP/AP/TP-NNN) — findings without a criterion cannot be challenged or defended
- Non-conformance severity is assigned consistently — define the severity taxonomy in the Implementation Governance Plan and apply it here
- Remediation actions have named owners and target dates — an unowned action is an unmanaged action

**Common mistakes:**
- Assessments conducted too late (post-deployment) — by then, non-conformances are expensive to fix; schedule assessments at design, pre-build, and pre-deployment gates
- Non-conformances marked as "accepted" without a formal dispensation decision from the architecture authority
- Overall conformance status of "Compliant" when there are open non-conformances — status must reflect actual state, not the desired state

**TOGAF reference:** TOGAF 10 Part III, Phase G (§31) — Architecture Compliance Review. Compliance Assessments are the primary Phase G mechanism for maintaining architecture integrity during implementation.

</details>

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

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the architecture compliance position: what is compliant, what has approved dispensations, and what requires attention.
Diagram: Compliance scorecard by domain/principle
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Assessment Purpose

<details>
<summary>📋 Guidance</summary>

State why this assessment is being conducted and what triggered it. Reference the Architecture
Contract review schedule if this is a planned gate review, or describe the concern that
triggered an ad-hoc assessment. State the expected outcome (confirm conformance, identify
remediation actions, support go/no-go decision).

</details>

{{assessment_purpose}}

**Assessment Type:** Scheduled gate / Ad-hoc / Pre-deployment / Post-implementation
**Go/No-Go Decision Required:** Yes / No

---

## 2. Scope

<details>
<summary>📋 Guidance</summary>

Define what is in scope for this assessment. List the solution components, architecture domains
(business, data, application, technology), and Architecture Contract requirements being assessed.
Be explicit about what is NOT being assessed to manage expectations.

</details>

### In Scope
{{scope_in}}

### Out of Scope
{{scope_out}}

### Contract Requirements Assessed
{{requirements_assessed}}

---

## 3. Compliance Criteria

<details>
<summary>📋 Guidance</summary>

List the specific criteria against which the solution is being assessed. These should map
directly to the Architecture Contract conformance requirements (ACR-xxx) and agreed standards.
Each criterion must be objectively assessable — define what evidence will demonstrate compliance.

</details>

| Criteria ID | Description | Source | Evidence Required |
|---|---|---|---|
| [[ACR-001]] | {{description}} | Architecture Contract | {{evidence_required}} |
| [[ACR-002]] | {{description}} | Architecture Contract | {{evidence_required}} |
| {{criteria_id}} | {{description}} | {{source}} | {{evidence_required}} |

---

## 4. Findings

<details>
<summary>📋 Guidance</summary>

Record the assessment findings for each criterion. Findings should be factual and evidence-based.
Do not conflate observations with judgements. Reference specific evidence (document names,
test results, code review observations) to support each finding.

</details>

| Criteria ID | Finding | Evidence Reviewed | Compliance Status |
|---|---|---|---|
| [[ACR-001]] | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |
| [[ACR-002]] | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |
| {{criteria_id}} | {{finding}} | {{evidence}} | Compliant / Partially Compliant / Non-Compliant / Not Assessed |

### Overall Compliance Summary
{{overall_compliance_summary}}

---

## 5. Non-conformances

<details>
<summary>📋 Guidance</summary>

Record each non-conformance identified. A non-conformance is a deviation from a mandatory
requirement in the Architecture Contract. For each, assign a severity, identify the required
remediation action, and set a target resolution date. Non-conformances must be tracked to
closure — either by remediation or by a formal architecture waiver (documented change request).

</details>

| NC ID | Description | Criteria ID | Severity | Required Action | Target Resolution | Owner |
|---|---|---|---|---|---|---|
| [[NC-001]] | {{description}} | ACR-xxx | Critical / Major / Minor | {{action}} | {{date}} | {{owner}} |
| [[NC-002]] | {{description}} | ACR-xxx | Critical / Major / Minor | {{action}} | {{date}} | {{owner}} |

**Total Non-conformances:** {{nc_count}}
**Critical:** {{critical_count}} | **Major:** {{major_count}} | **Minor:** {{minor_count}}

---

## 6. Recommendations

<details>
<summary>📋 Guidance</summary>

Provide recommendations beyond mandatory remediation — these address advisory guidance
deviations or improvement opportunities identified during the assessment. Recommendations
are not blocking but should be tracked. Include a recommendation for the go/no-go decision
if this assessment feeds one.

</details>

| Rec ID | Recommendation | Priority | Owner |
|---|---|---|---|
| [[REC-001]] | {{recommendation}} | High / Med / Low | {{owner}} |

### Go / No-Go Recommendation
<details>
<summary>📋 Guidance</summary>

If this assessment feeds a deployment or phase-gate decision, state the recommendation clearly.
If recommending conditional approval, list the conditions that must be met.

</details>

**Recommendation:** Go / No-Go / Conditional Go

**Conditions (if Conditional Go):**
{{conditions}}

**Rationale:**
{{go_nogo_rationale}}

---

## 7. Sign-off

<details>
<summary>📋 Guidance</summary>

The assessor and the solution lead should both sign. The assessor confirms the assessment
is accurate and objective. The solution lead acknowledges the findings and commits to
remediation. For go/no-go decisions, the architecture authority must also sign.

</details>

| Role | Name | Organisation | Signature | Date |
|---|---|---|---|---|
| Assessor | {{assessor}} | {{assessor_org}} | | |
| Solution Lead | {{solution_lead}} | {{solution_org}} | | |
| Architecture Authority | {{architecture_authority}} | {{arch_org}} | | |

---
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
