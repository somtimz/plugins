---
artifact: Operating Model
artifactId: operating-model
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.89
lastModified: {{YYYY-MM-DD}}
taxonomy:
  admPhases: [B]
  zachmanCell: "Enterprise/How"
  domain: Business
  category: Design
  audience: Business
  layer: Target
  sensitivity: Internal
  tags: [operating-model, organisation, processes, controls, sourcing, phase-b]
relatedArtifacts:
  - business-architecture
  - business-model-canvas
  - architecture-vision
  - statement-of-architecture-work
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
| Linked to Business Architecture | ⚠️ Pending | |
| Traces to Requirements Register | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Operating Model describes how the organisation will reliably operate its business to deliver value. It answers *"How will the organisation function?"* — the execution design to the Business Architecture's stable blueprint.

**What to include:** Organisation design; operating roles and decision rights; governance, controls, and SLAs; business process execution context; workforce, locations, and channels; sourcing and partnership model; information and technology enablement; performance management. Structured process detail lives in the Business Processes Register (`PROC-NNN`) and is linked from this artifact, not duplicated here.

**What NOT to include:**
- Business capabilities (CAP-NNN) — those belong in the **Business Architecture**.
- Value streams (VS-NNN) — authored in the **Business Architecture** and mastered in the Value Streams Register.
- Business services (SVC-NNN) — the service *definition* is BA; the *delivery model* is OM.
- Detailed process step tables — mastered in the **Business Processes Register** and linked from §5.

**Quality indicators:**
- The OM links back to the BA capability model and value streams — it is the operating expression of the blueprint, not a parallel design.
- Decision rights are explicit — who decides what, and what is escalated.
- Processes in §5 are summary-and-link references, not duplicated step tables.
- Performance management is tied to metrics (MET-NNN) that close the loop to goals/objectives.

**Common mistakes:**
- Repeating the org chart as the operating model — the OM is about how work flows across roles, not hierarchy.
- Duplicating process detail from the Business Processes Register — keep §5 as an index.
- Designing the OM without referencing the Business Architecture — this produces an operating model that does not deliver the target capabilities.

**TOGAF reference:** TOGAF 10 Part III, Phase B (§26) — Business Architecture; the Operating Model is the execution-oriented complement to the capability and value-stream views.

</details>

<details>
<summary>💡 Practitioner Tip — Operating Model</summary>

- **Design the OM after the capability model** — capabilities tell you *what* must be delivered; the OM designs *who, how, and where*.
- **Decision rights are more important than boxes** — a clean org chart with unclear authority is still a broken operating model.
- **Controls should be proportional** — not every process needs a committee; match governance to risk and materiality.
- **Sourcing is part of the OM** — make/buy/partner choices shape roles, processes, and technology enablement.
- **Performance management closes the loop** — define metrics that tell you whether the OM is delivering the BA intent.

</details>

# Operating Model

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Related Matrices

> **TOGAF relationship matrices for this domain** (manage with `/ea-matrix`; definitions in `matrix-catalogue.md`): Actor/Role (`actor-role`), Capability/Organization (`capability-organization`), Process/Value Stream (`process-value-stream`), Use Case/Process (`use-case-process`). Run `/ea-matrix list` for status.

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Overview of the target operating model: the key organisational, process, control, sourcing, and performance-management choices that will execute the Business Architecture.
Written for an executive or business sponsor audience.
Diagram: Operating Model overview (value chain + operating units + delivery channels)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Operating Model Context

<details>
<summary>📋 Guidance</summary>

Set the context for the operating model:
- Link to the Business Architecture and Architecture Vision — this OM executes that blueprint.
- State the scope of the OM (enterprise-wide, divisional, program-level).
- Note any significant business-model changes from the Business Model Canvas that drive the OM design.

</details>

{{operating_model_context}}

*Linked artifacts:*
- [[business-model-canvas\|Business Model Canvas]] — value model this OM must realise
- [[business-architecture\|Business Architecture]] — blueprint this OM executes
- [[architecture-vision\|Architecture Vision]]
- [[statement-of-architecture-work\|Statement of Architecture Work]]

---

## 2. Organisation Design

<details>
<summary>📋 Guidance</summary>

Describe the target organisational structure: operating units, teams, governance fora, and reporting relationships relevant to the architecture scope.
This is **not** the full enterprise org chart — it is the operating structure needed to deliver the target capabilities and value streams.
Include a diagram reference if available.

</details>

{{organisation_design}}

*Reference diagram:* `../../diagrams/{{org_design_diagram}}`

| Operating Unit | Role in OM | Capabilities Supported (CAP-NNN) | Value Streams Supported (VS-NNN) |
|---|---|---|---|
| {{unit_name}} | {{role}} | {{cap_ids}} | {{vs_ids}} |

---

## 3. Roles, Decision Rights & Accountability

<details>
<summary>📋 Guidance</summary>

Define the business **operating roles** (not EA engagement roles — those live in the Role Catalogue, `ROLE-NNN`).
For each key decision or accountability, state:
- **Decision / Accountability** — what is being decided or owned
- **Owner** — the operating role accountable for the decision
- **Consulted / Informed** — who else is involved
- **Escalation path** — where disputes or exceptions go

</details>

| Decision / Accountability | Owner (Operating Role) | Consulted | Informed | Escalation Path |
|---|---|---|---|---|
| {{decision}} | {{owner}} | {{consulted}} | {{informed}} | {{escalation}} |

> Note: EA engagement roles (`ROLE-NNN`) are managed via `/ea-roles`; business operating roles live in this artifact.

---

## 4. Governance, Controls & SLAs

<details>
<summary>📋 Guidance</summary>

Describe the governance mechanisms, business controls, and service-level expectations that keep the operating model on track.
Link to policies (POL-NNN), constraints (CST-NNN), and business rules (BR-NNN) where applicable.

</details>

| Control / SLA | Purpose | Owner | Frequency / Trigger | Linked Policy / Rule / Constraint |
|---|---|---|---|---|
| {{control}} | {{purpose}} | {{owner}} | {{frequency}} | {{POL/CST/BR-NNN}} |

---

## 5. Business Processes Execution Model

<details>
<summary>📋 Guidance</summary>

This section is a **summary-and-link index** into the authoritative Business Processes Register (`../../artifacts/cross-cutting/operations/business-processes-register.md`).
The Operating Model does **not** duplicate detailed step tables — it explains *how* the key processes are orchestrated to deliver value, and links to the register for process detail.

For each key process, note its place in the OM (which value stream it serves, which capability it operationalises, which controls apply).

</details>

| PROC-NNN | Process | OM Role | Owner | Linked Value Streams (VS-NNN) | Linked Capabilities (CAP-NNN) | Register | Details |
|---|---|---|---|---|---|---|---|
| [[PROC-001]] | {{process_name}} | {{om_role}} | {{owner}} | {{vs_ids}} | {{cap_ids}} | [Business Processes Register](../../artifacts/cross-cutting/operations/business-processes-register.md) | [[PROC-001\|→]] |

*Generate or refresh the register with `/ea-processes generate`. Add or edit processes with `/ea-processes add` or `/ea-processes update PROC-NNN`.*

---

## 6. Workforce, Locations & Channels

<details>
<summary>📋 Guidance</summary>

Describe the people, skills, geography, and delivery channels needed to operate the business.
Link workforce design back to capabilities and value streams.

</details>

| Element | Current State | Target State | Implications |
|---|---|---|---|
| Workforce / Skills | {{current}} | {{target}} | {{implications}} |
| Locations | {{current}} | {{target}} | {{implications}} |
| Channels | {{current}} | {{target}} | {{implications}} |

---

## 7. Sourcing & Partnership Model

<details>
<summary>📋 Guidance</summary>

Document make / buy / partner choices for key capabilities and services.
Identify strategic vendors, shared-service arrangements, outsourcing, or ecosystem partnerships.
Link to Vendor Landscape (VDR-NNN) entries where applicable.

</details>

| Capability / Service | Sourcing Model | Partner / Vendor (if any) | Rationale | Linked VDR-NNN |
|---|---|---|---|---|
| {{cap_or_service}} | Make / Buy / Partner | {{partner}} | {{rationale}} | {{vdr_id}} |

---

## 8. Information & Technology Enablement

<details>
<summary>📋 Guidance</summary>

Describe how data, applications, and technology enable the operating model.
Keep this at the business level — detailed data/application/technology design belongs in Phase C/D artifacts.
Link forward to Data Architecture, Application Architecture, and Technology Architecture as they are developed.

</details>

| OM Element | Enabling Information / Application / Technology | Linked Phase C/D Artifact |
|---|---|---|
| {{om_element}} | {{enabler}} | [[data-architecture\|Data Architecture]] / [[application-architecture\|Application Architecture]] / [[technology-architecture\|Technology Architecture]] |

---

## 9. Performance Management

<details>
<summary>📋 Guidance</summary>

Define how the operating model will be measured and improved.
Link metrics (MET-NNN) to goals/objectives, processes, and capabilities.
State review cadence and accountability.

</details>

| Metric (MET-NNN) | What it Measures | Target | Review Cadence | Owner |
|---|---|---|---|---|
| [[MET-001]] | {{measure}} | {{target}} | {{cadence}} | {{owner}} |

---

## 10. Gap Analysis

<details>
<summary>📋 Guidance</summary>

Identify gaps in the operating model relative to the target state.
Distinguish capability gaps (BA concern) from operating-model gaps (OM concern).
Link each OM gap to a GAP-NNN entry.

</details>

| Gap | OM Area | Current State | Target State | Linked GAP-NNN |
|---|---|---|---|---|
| {{gap}} | Organisation / Process / Control / Workforce / Sourcing / Enablement / Performance | {{current}} | {{target}} | [[GAP-001]] |

---

## 11. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

List requirements from the Requirements Register that this artifact addresses or generates.
Requirements may emerge from OM design decisions (e.g. new roles, controls, sourcing, technology enablement).

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

## 12. Traceability Summary

<details>
<summary>📋 Guidance</summary>

The Operating Model executes the Business Architecture. Use this summary to validate that the OM is grounded in the BA and feeds into requirements:

- **Every OM section** links back to at least one CAP-NNN capability or VS-NNN value stream from the Business Architecture.
- **Every process referenced in §5** is a summary-and-link to a PROC-NNN entry; detailed steps live in the register or a detail file.
- **Every decision in Appendix A3** with Authority = Strategic has a captured rationale block (#### A3.N).
- **Every sourcing choice in §7** with high cost/risk has a linked ADR-NNN in Appendix A5.
- **Every metric in §9** links to a MET-NNN that tracks a goal/objective or process performance.

Flag any orphan or gap in §10 Gap Analysis.

</details>

---

## 13. Diagrams

<details>
<summary>📋 Guidance</summary>

Standard diagrams for the Operating Model. Diagrams are stored in `diagrams/` relative to the engagement root and embedded in exported documents via `/ea-generate`. Use `/ea-diagram` to create or edit. See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

</details>

| Diagram | File | Status |
|---|---|---|
| Operating Model Overview | `../../diagrams/operating-model-overview.mmd` | ❌ Missing |
| Organisation Design | `../../diagrams/operating-model-org-design.mmd` | ❌ Missing |
| Process Execution Context | `../../diagrams/operating-model-process-context.mmd` | ❌ Missing |

*Use `/ea-diagram` to create. Run `/ea-generate png` to render for export.*

---

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
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

| # | Rule | Rationale | Approver | Date |
|---|---|---|---|---|
| — | — | — | — | — |
