---
artifact: Architecture Change Request
artifactId: acr-{{NNN}}
engagement: {{engagement_name}}
phase: H
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
  sensitivity: Confidential
  tags: [change, impact, disposition, phase-h]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Linked to Change Register | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** An Architecture Change Request (ACR) is the formal mechanism for proposing, assessing, and approving changes to the agreed architecture after the target state has been delivered or is under delivery. It prevents uncontrolled architectural drift by requiring every significant change to pass through an impact assessment and authority decision before implementation.

**What to include:** A change is significant enough to require an ACR when it: modifies the scope of an approved architecture domain; introduces or removes a technology platform; alters a key integration pattern; affects compliance posture; or creates new gaps against Architecture Principles. Minor implementation-level decisions that do not affect the baseline or target architecture descriptions do not require an ACR.

**Quality indicators:**
- The ACR reaches a disposition (Approved / Rejected / Deferred) — an ACR that circulates indefinitely is a governance gap
- All affected artifacts are listed in §6 Updated Artifacts with owners and target dates
- The change is logged in the Change Register (ACR-NNN) before or immediately after the ACR is raised

**Common mistakes:**
- Raising an ACR for changes that are within the authority of the delivery team — the ACR process should not create unnecessary governance friction
- Omitting the impact on architecture principles — this is the most commonly missed dimension of impact assessment
- Approving an ACR without updating the affected artifacts — approved changes that are not reflected in the architecture repository create drift

**TOGAF reference:** TOGAF 10 Part III, Phase H — Architecture Change Management. ACRs are the primary mechanism for maintaining the architecture repository in a current and consistent state post-delivery.

</details>

# Architecture Change Request

**Engagement:** {{engagement_name}}
**Change Request ID:** {{change_request_id}}
**Organisation:** {{organisation}}
**Raised By:** {{raised_by}}
**Date Raised:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** Draft / Under Review / Approved / Rejected / Deferred

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** A one-paragraph decision-maker summary of the change, the driver, and the impact. A governance board member who reads only this section should understand whether the change is routine, significant, or contentious.

**What to include:** What is changing (the architectural element), why it is being changed (the trigger), which domains are affected (a headline, not the full impact table), the decision recommended, and the key risk if the change is rejected. Include or reference the impact diagram if the change is structural.

**Quality indicators:**
- Can be read cold in 60 seconds — jargon-free, no unexplained acronyms
- States the recommended disposition (Approve / Reject / Defer) in the summary — the body sections support the recommendation
- Consistent with the body sections — if the body identifies High impact in Technology Architecture, the summary must not say "minimal impact"

**Common mistakes:**
- Restating the title of each body section rather than synthesising the change
- Writing the executive summary before the impact assessment and risk sections are complete — write it last
- Omitting the recommended disposition — governance authorities expect a recommendation, not just a description

**TOGAF reference:** TOGAF 10 Phase H — the ACR executive summary aligns with the briefing format used at Architecture Review Board meetings where change requests are adjudicated.

</details>

{{executive_summary}}

---

## 1. Change Description

<details>
<summary>📋 Guidance</summary>

**Purpose:** Precisely defines the scope of the change — what architectural element is affected, what is changing about it, and what the change type is. Precision here prevents scope creep in the approval process.

**What to include:** The specific architectural element (named application, integration, data domain, technology component, or principle — not a vague category). The nature of the change (add, modify, remove, substitute). The change type from the classification list above. The affected architecture domains. Keep justification out of this section — that belongs in §2.

**Quality indicators:**
- The change is described specifically enough that a reviewer can determine which artifacts need updating without reading further
- The affected domains are correctly classified — a database migration should flag Data Architecture, not just Technology
- The change type is selected from the controlled vocabulary (not "misc" or "other" unless genuinely novel)

**Common mistakes:**
- "We need to upgrade the CRM system" — too vague; name the system, the version change, and the architectural elements affected
- Mixing the change description with the justification — this conflates what is changing with why, making the impact assessment harder to verify independently
- Marking only one domain as affected when the change has obvious cross-domain implications (e.g. an application change that modifies data flows)

**TOGAF reference:** TOGAF 10 §33 — Change Description follows the standard architecture change categorisation (simplification, incremental improvement, re-architecting) which determines the level of governance scrutiny required.

</details>

**Type of Change:** New capability / Technology substitution / Process change / Correction / Decommission / Other

**Summary:** {{change_summary}}

**Detailed Description:**
{{change_description}}

**Affected Architecture Domains:** Business / Data / Application / Technology (select all that apply)

---

## 2. Justification

<details>
<summary>📋 Guidance</summary>

**Purpose:** Establishes why the change is necessary and what happens if it is rejected. The justification is the architect's case for the change — it must be strong enough to pass governance scrutiny independently of informal conversations.

**What to include:** The primary trigger (business driver DRV-NNN, regulatory requirement, technology end-of-life, implementation learning, or strategic direction change). Supporting evidence (vendor notice, regulatory publication date, metric trend, incident post-mortem). The consequence of rejection — framed in business terms (financial exposure, compliance risk, capability gap, operational disruption) not just technical terms.

**Quality indicators:**
- The trigger is traceable — a vendor EOL notice has a date and a document; a regulatory requirement has a citation; a business driver has a DRV-NNN reference
- "Consequence of Not Changing" is specific enough to quantify the risk — "we will be running unsupported software from [date]" or "we will be non-compliant with [regulation] by [date]"
- The justification does not beg the question — "we need to change because the current state is not good enough" is not a justification

**Common mistakes:**
- Justification that is only about technical preference ("the team wants to use the newer API") without a business-grounded driver
- Omitting the consequence of not changing — this is often the most persuasive element and is most frequently left blank
- Circular justification that refers back to the change description ("we need to upgrade because we need a newer version")

**TOGAF reference:** TOGAF 10 Phase H — change request justification must align with the Architecture Vision's business drivers to demonstrate that the change serves the engagement's strategic intent.

</details>

**Business Driver / Trigger:** {{business_driver}}

**Justification:**
{{justification}}

**Consequence of Not Changing:**
{{consequence_of_inaction}}

---

## 3. Impact Assessment

<details>
<summary>📋 Guidance</summary>

**Purpose:** Identifies all the ripple effects of the change — across domains, artifacts, and work in flight. The impact assessment is the technical core of the ACR; an incomplete assessment is the most common cause of change-related architectural drift.

**What to include:** Domain-level impact rated High/Medium/Low/None with a concrete description for each active domain. The list of artifacts requiring update if the change is approved (be specific — "the Application Architecture diagram on page 3" not just "the Application Architecture"). Any dependencies on in-flight work packages or other open change requests. An effort estimate to assess whether the change is proportionate to its justification.

**Quality indicators:**
- Every active domain in the engagement has an explicit impact assessment — "None" is a valid entry but must be consciously decided, not left blank
- The artifacts list is complete — if the impact assessment says Application Architecture is affected, the Application Architecture artifact must appear in the list
- Effort estimate is realistic — an estimate of "1 day" for a change that affects 5 artifacts across 3 domains is a red flag

**Common mistakes:**
- Only assessing the domain where the change originates — cross-domain ripple effects are missed more than 50% of the time in practice
- Listing artifact names without specifying the nature of the change required — "update the Technology Architecture" does not tell the architect what to update
- Omitting in-flight work package dependencies — a change approved without reference to open WPs can conflict with work already underway

**TOGAF reference:** TOGAF 10 §33 — Impact Assessment is the primary technical deliverable of the ACR process. The cross-domain impact table directly informs which artifacts must be updated in §6 to maintain repository consistency.

</details>

### Impact on Architecture Domains

| Domain | Impact | Description |
|---|---|---|
| Business Architecture | High / Med / Low / None | {{impact_description}} |
| Data Architecture | High / Med / Low / None | {{impact_description}} |
| Application Architecture | High / Med / Low / None | {{impact_description}} |
| Technology Architecture | High / Med / Low / None | {{impact_description}} |

### Artifacts Requiring Update
| Artifact | Nature of Change |
|---|---|
| {{artifact_name}} | {{change_description}} |

### Dependencies
{{dependencies}}

### Estimated Effort
{{estimated_effort}}

---

## 4. Risk Assessment

<details>
<summary>📋 Guidance</summary>

**Purpose:** Surfaces the risks of approving the change, so the governance authority can weigh them against the justification. A risk-free change request is almost certainly incomplete — every architecture change introduces some risk.

**What to include:** Architectural risks (the change creates technical debt, introduces a pattern inconsistent with Architecture Principles, or weakens a compliance or security control). Implementation risks (disruption to live systems, migration complexity, timing conflict with other work in flight). For each risk: a description, likelihood, impact, and a concrete mitigation. The overall risk level (High/Medium/Low) as a summary assessment.

**Quality indicators:**
- Architectural risks are distinguished from implementation risks — "the new pattern conflicts with AP-003 (loose coupling)" is an architectural risk; "the migration window falls during peak trading" is an implementation risk
- Mitigations are concrete, not generic — "follow best practices" is not a mitigation; "introduce the strangler pattern to route traffic gradually, with a rollback mechanism" is
- The overall risk level is consistent with the individual risk ratings — if any individual risk is High, the overall level should be at least Medium

**Common mistakes:**
- Listing only implementation risks and omitting architectural risks — the architecture authority cares most about the long-term architectural impact, not the deployment plan
- Risk mitigations that simply restate the risk ("risk: the change may fail; mitigation: make sure it doesn't fail")
- Marking overall risk as Low when the impact assessment identified High impact in multiple domains

**TOGAF reference:** TOGAF 10 §28 — Architecture Risk Management. Change request risks should be evaluated against the engagement Risk Register (RIS-NNN) to determine if new risks need to be added.

</details>

| Risk ID | Description | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| CR-R001 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} |
| CR-R002 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} |

**Overall Risk Level:** High / Medium / Low

---

## 5. Disposition

<details>
<summary>📋 Guidance</summary>

**Purpose:** Records the authoritative decision on the change request — what was decided, who decided it, why, and (if conditional) what must be met before implementation proceeds. The Disposition section is the governance artefact of record.

**What to include:** The decision (Approved / Rejected / Deferred / Approved with Conditions), the decision date, the named decision authority (individual or body), the rationale for the decision in 2–3 sentences, explicit conditions if conditional approval was granted, and the reconsideration trigger if deferred.

**Quality indicators:**
- The decision authority is named — "the ARB" is acceptable; "management" is not
- Conditions are specific and testable — "the implementation team must produce a rollback plan and have it reviewed by the Architecture Lead before go-live" not "follow best practices"
- Deferred decisions have a named reconsideration trigger — "defer until the Data Architecture artifact is approved" not "defer until more information is available"
- The rationale references the justification (§2) and risk assessment (§4) — the decision should be traceable to the evidence

**Common mistakes:**
- Conditions stated so vaguely that the implementing team cannot verify compliance — this leads to conditions being ignored
- Rejected ACRs with no rationale — without a rationale, the submitter cannot improve the request and resubmit
- Approved ACRs where §6 Updated Artifacts is not subsequently populated — an approval without an artifact update plan is incomplete

**TOGAF reference:** TOGAF 10 Phase H — the Disposition section corresponds to the Architecture Board's formal response to a change request, as described in the Architecture Governance framework (§38).

</details>

**Decision:** Approved / Rejected / Deferred / Approved with Conditions

**Decision Date:** {{decision_date}}
**Decision Authority:** {{decision_authority}}

**Rationale:**
{{decision_rationale}}

**Conditions (if Approved with Conditions):**
{{conditions}}

**Deferral Reason and Reconsideration Trigger (if Deferred):**
{{deferral_reason}}

---

## 6. Updated Artifacts

<details>
<summary>📋 Guidance</summary>

**Purpose:** Ensures the architecture repository is updated to reflect the approved change. An approved change that is not reflected in the artifacts creates drift between the documented architecture and the implemented state — the primary long-term risk of the ACR process.

**What to include:** Every artifact identified in the Impact Assessment (§3) as requiring update. For each: the nature of the update, the owner responsible for making it, and the target date. Update status should be tracked here through to completion.

**Quality indicators:**
- The artifact list is derived from §3 — every artifact listed as impacted in the Impact Assessment appears here; no artifacts appear here that were not mentioned in §3
- Every artifact has a named owner (a person, not a team or system)
- All updates are marked Complete before the ACR is closed — an ACR closed with pending updates is a governance gap

**Common mistakes:**
- Populating §6 with fewer artifacts than §3 identified — this is the most common cause of post-approval drift
- Listing "Architecture Repository" as a single artifact rather than the specific files to update
- Closing the ACR before confirming all artifact updates are complete — set up a follow-up review at the target date to verify

**TOGAF reference:** TOGAF 10 §33 — artifact updates following an approved change request are the primary mechanism for maintaining Architecture Repository currency in Phase H.

</details>

| Artifact | Update Required | Owner | Target Date | Status |
|---|---|---|---|---|
| {{artifact_name}} | {{update_description}} | {{owner}} | {{target_date}} | Pending / In Progress / Complete |

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
