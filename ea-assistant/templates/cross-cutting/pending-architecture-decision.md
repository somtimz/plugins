---
artifact: Pending Architecture Decision
artifactId: pad-{{NNN}}
padid: PAD-{{NNN}}
title: {{pending_decision_title}}
engagement: {{engagement_name}}
phase: {{phase_where_deferred}}
status: Open
expiryDate: {{YYYY-MM-DD}}
resolutionPhase: {{phase_to_resolve}}
linkedGap: {{GAP-NNN}}
linkedWorkPackage: {{WP-NNN}}
decisionOwner: {{owner}}
reviewedBy: {{reviewed_by}}
templateVersion: 0.9.55
reviewStatus: Not Reviewed
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [Preliminary, Requirements, A, B, C-Data, C-App, D, E, F, G, H]
  zachmanCell: ""
  domain: Cross-cutting
  category: Governance
  audience: Architecture
  layer: Governance
  sensitivity: Internal
  tags: [pad, pending, decision, deferral, evidence]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3: Appendix A3 — Decision Log present | ⚠️ Pending | Required |
| T4-PAD: Expiry date within 90 days of creation | ⚠️ Pending | Required for L4+ |
| T4-PAD: Resolution path defined | ⚠️ Pending | Required for L4+ |
| T4-PREMAT: Not a premature commitment disguised as a PAD | ⚠️ Pending | Verify this is genuinely deferred, not avoided |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

A **Pending Architecture Decision (PAD)** captures a decision that cannot be made now
because evidence is insufficient, the wrong phase has been reached, or stakeholder
alignment is incomplete. It replaces premature commitment with disciplined deferral.

**When to create a PAD instead of an ADR or A3 entry:**
- Evidence is insufficient to justify commitment (no benchmarks, POCs, or vendor responses)
- The decision is being made in the wrong ADM phase (e.g., technology choice in Phase A)
- Stakeholder pressure is forcing a decision before analysis is complete
- The decision is hard to reverse and the team lacks the capability to implement it
- A strong political mandate exists but the architecture team needs time to validate it

**PAD vs ADR vs A3:**
- **A3 Decision Log** — lightweight governance tracking inside an artifact (who decided what)
- **ADR** — full-context standalone document for decisions that are ready to commit
- **PAD** — deferred decision with constraint boundaries, evidence requirements, and resolution path.
  A PAD is converted to an ADR when evidence is sufficient. It is closed (not superseded) when resolved.

**PAD lifecycle:**
Open → In Progress (evidence gathering) → Resolved (converted to ADR or closed) → Expired

Use `/ea-decisions` or `/ea-adrs` to track PADs alongside other decision artifacts.
Run `/ea-status` to surface open PADs and their expiry dates.

**Key principle:** A PAD is not an excuse to avoid deciding. It is a commitment to decide
by a specific date with specific evidence. Every PAD must have an expiry date and a
resolution path. PADs without expiry dates are governance gaps, not governance discipline.

</details>

# {{padid}}: {{pending_decision_title}}

**Engagement:** {{engagement_name}}
**Phase Deferred From:** {{phase_where_deferred}}
**Status:** Open
**Decision Owner:** {{owner}}
**Expiry Date:** {{YYYY-MM-DD}}
**Resolution Phase:** {{phase_to_resolve}}

---

## 1. Decision Summary

<details>
<summary>📋 Guidance</summary>

State clearly what is being deferred and why. A reader should understand the decision
without reading the rest of the PAD. Include the specific question, the reason for deferral,
and the risk of deciding prematurely.

Example: "The choice of integration pattern (ESB vs event-driven vs API gateway) is deferred
from Phase A to Phase E because business capabilities, data domains, and transaction boundaries
have not yet been defined. Premature selection risks forcing artificial service boundaries
and creating a distributed monolith."

</details>

**Question being deferred:** {{deferred_question}}

**Reason for deferral:** {{deferral_reason}}

**Risk of premature decision:** {{premature_risk}}

**Phase where this decision should be made:** {{optimal_phase}}

---

## 2. Constraint Boundaries

<details>
<summary>📋 Guidance</summary>

Even though the specific decision is deferred, the solution space must be constrained.
Document the guardrails, MUST requirements, and principles that bound the eventual decision.
This allows delivery teams to design within constraints without knowing the final choice.

Example constraint boundary: "The eventual integration pattern must support real-time data
propagation, must not require a centralised message broker for all domains, and must
integrate with existing Salesforce and bespoke systems via REST or gRPC."

</details>

**Architecture principles that constrain this decision:**
- {{principle_constraint}}
- {{principle_constraint}}

**MUST requirements (disqualifiers if violated):**
| # | Requirement | Source |
|---|---|---|
| 1 | {{must_requirement}} | {{source_artifact_or_principle}} |
| 2 | {{must_requirement}} | {{source_artifact_or_principle}} |

**Guardrails (what the solution must respect):**
- {{guardrail}}
- {{guardrail}}

**What is fixed vs what remains open:**
| Fixed (non-negotiable) | Open (to be decided) |
|---|---|
| {{fixed_item}} | {{open_item}} |

---

## 3. Candidate Options

<details>
<summary>📋 Guidance</summary>

Document the options that have been preliminarily identified, with a preliminary assessment.
This is not a full options analysis (that belongs in the eventual ADR) — it is a shortlist
that frames the decision space and prevents "analysis paralysis" later.

For each option, note: why it is credible, why it might be eliminated, and what evidence
would confirm or disqualify it.

</details>

### Option 1: {{option_1_title}}

{{option_1_description}}

**Why credible:** {{credibility_reason}}
**Why might be eliminated:** {{elimination_risk}}
**Evidence needed to confirm:** {{confirmation_evidence}}

---

### Option 2: {{option_2_title}}

{{option_2_description}}

**Why credible:** {{credibility_reason}}
**Why might be eliminated:** {{elimination_risk}}
**Evidence needed to confirm:** {{confirmation_evidence}}

---

### Option 3: {{option_3_title}} *(add or remove as needed)*

{{option_3_description}}

**Why credible:** {{credibility_reason}}
**Why might be eliminated:** {{elimination_risk}}
**Evidence needed to confirm:** {{confirmation_evidence}}

---

## 4. Evidence Required

<details>
<summary>📋 Guidance</summary>

Define what evidence must be gathered before this decision can be made. Be specific:
"benchmark" is not enough — specify what metric, against what baseline, from what source.
If a POC is needed, define the success criteria, duration, and owner.

Evidence types: benchmarks, POC results, vendor responses, regulatory opinions,
production metrics, incident analysis, peer references, cost models, security reviews.

</details>

| Evidence Type | Description | Status | Gathering Method | Owner | Target Date |
|---|---|---|---|---|---|
| {{type}} | {{description}} | Missing / In Progress / Complete | {{method}} | {{owner}} | {{date}} |

**Overall evidence sufficiency target:** {{sufficient / partial / insufficient}}

**Evidence gaps that must close before decision:**
- {{gap}}
- {{gap}}

---

## 5. Resolution Path

<details>
<summary>📋 Guidance</summary>

Document exactly how and when this decision will be resolved. A PAD without a resolution
path is a governance gap. Specify: which phase or work package will close it, who is
accountable, what triggers reopening, and what happens if it expires unresolved.

</details>

**Resolved by:** {{phase_or_work_package}}

**Work package that resolves this PAD:** {{WP-NNN}}

**Resolution owner:** {{owner}}

**Resolution trigger:** {{trigger_event}}
*(e.g. "POC WP-003 completes and produces recommendation", "Phase E gap analysis confirms approach")*

**What happens if expired unresolved:** {{expiry_consequence}}

**Conditions for reopening:** {{reopening_conditions}}
*(e.g. "New stakeholder concern raised", "Business driver changes", "Evidence contradicts preliminary assessment")*

---

## 6. Expiry and Review Schedule

<details>
<summary>📋 Guidance</summary>

Every PAD must have an expiry date. Without one, deferred decisions drift indefinitely.
The expiry should be aggressive enough to create urgency but realistic enough to allow
evidence gathering. Schedule interim reviews to monitor progress.

</details>

| Review Date | Purpose | Owner | Status |
|---|---|---|---|
| {{date}} | Evidence progress check | {{owner}} | Scheduled |
| {{date}} | Pre-expiry decision checkpoint | {{owner}} | Scheduled |
| {{expiryDate}} | **Final expiry — decide or escalate** | {{owner}} | Scheduled |

**Expiry consequence:** {{expiry_consequence}}
*(What happens if the PAD expires without resolution? e.g. "Escalate to Architecture Board", "Default to safest option", "Extend with justification")*

---

## 7. Consequences of Premature Decision

<details>
<summary>📋 Guidance</summary>

Document the specific risks if this decision is made before evidence is available.
This section is the architect's defence against stakeholder pressure: it shows what
will break if the decision is forced early. Reference the microservices example or
other relevant failure modes from `failure-modes.md`.

</details>

**If decided now (prematurely):**

| Risk | Likelihood | Impact | Example / Scenario |
|---|---|---|---|
| {{risk}} | High / Med / Low | High / Med / Low | {{scenario}} |

**Historical reference:** {{failure_mode_reference}}
*(Link to a relevant failure mode from `failure-modes.md`, e.g. "Static Target Architecture Illusion — premature commitment to a pattern before domain analysis")*

**Cost of reversal if wrong:** {{reversal_cost}}

**Teams or systems affected if wrong:** {{blast_radius}}

---

## 8. Linked Artifacts

| Artifact | ID | Relationship | Status |
|---|---|---|---|
| Gap Analysis | {{GAP-NNN}} | This PAD resolves the gap | Open / Closed |
| Work Package | {{WP-NNN}} | This PAD will be resolved by WP | Proposed / Approved |
| Architecture Decision Record | {{ADR-NNN}} | Converts to ADR when resolved | Candidate / Proposed |
| A3 Decision Log | {{artifact}} | Logged as pending decision | Provisional |

---

## Appendix A3 — Decision Log

| Item | Value | State | Authority | Domain | Cost | Impact | Risk | Subject | Captured By | Owner | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Decision to defer {{subject}} | {{description}} | 🔄 Provisional | {{authority}} | {{domain}} | {{cost}} | {{impact}} | {{risk}} | {{subject}} | {{author}} | {{owner}} | {{YYYY-MM-DD}} |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record concerns about the deferral itself — stakeholders who believe the decision should
be made now, or who are concerned about the expiry date. Also record objections to the
constraint boundaries ("These guardrails are too restrictive / too loose").

Use `/ea-concerns` to generate a cross-artifact Concerns Register.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*Use `/ea-decisions` to track this PAD alongside other decisions. Use `/ea-concerns` to manage concerns. Run `/ea-status` to surface open PADs and expiry dates.*

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
