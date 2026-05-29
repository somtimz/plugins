---
artifact: Role Catalogue
artifactId: role-catalogue
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Reference
  sensitivity: Confidential
  tags: [roles, raci, governance, stakeholders, calendar, triggers]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Roles mapped to responsibilities | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Role Catalogue maps every governance role active in this engagement to a named individual, organisation, and RACI position. It provides the operational reference for who does what — supplementing the Stakeholder Map (which tracks interests and influence) with precise governance accountability assignments, triggering events, and meeting cadence.

**What to include:** Rows for every active governance role (ROLE-NNN), with named individual, organisation, RACI position (Responsible/Accountable/Consulted/Informed), triggering events for this role, and meeting cadence. Remove rows for roles not active in this engagement. Only add RACI Overrides when this engagement's governance structure explicitly differs from the canonical defaults in `skills/ea-engagement-lifecycle/references/role-catalogue.md`.

**Quality indicators:**
- Every role has exactly one Accountable owner — if a role has two Accountable entries, accountability is unclear; resolve to one
- Named individuals are current — a role catalogue with departed team members is a governance liability
- Triggering events are specific enough that the role holder knows when to act without being told

**Common mistakes:**
- Listing only formal governance roles (ARB Chair, Sponsor) and omitting operational roles (Lead Architect, Domain Architect, SME) — the catalogue should cover all roles that participate in architecture governance
- RACI assignments copied from the canonical without review — every engagement has governance nuances that may require overrides
- Role catalogue not updated when team composition changes — a stale role catalogue produces governance confusion at review time

**TOGAF reference:** TOGAF 10 Part III §23 — Architecture Capability Framework. Roles and responsibilities are defined in the Preliminary Phase as part of establishing the architecture practice capability.

</details>

# Role Catalogue

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Overview of the roles and governance bodies defined for this engagement and how they relate to architecture activities.
Diagram: RACI overview or stakeholder role diagram
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Active Roles

<details>
<summary>📋 Guidance</summary>

List all roles active in this engagement. Assign a named individual and their organisation unit. Use the RACI Override column only when the engagement-specific RACI differs from the canonical default in `role-catalogue.md`. Leave blank if the default applies.

Remove unused role rows. If a role is shared across multiple individuals (e.g., multiple Application Owners), duplicate the row and append a domain qualifier in the Notes column (e.g., "CRM domain").

</details>

| Role ID | Role | Named Individual | Organisation Unit | RACI Override | Notes |
|---------|------|-----------------|-------------------|---------------|-------|
| [ROLE-001](../details/ROLE-001.md) | Stakeholder | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-002](../details/ROLE-002.md) | Stakeholder Agent | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-003](../details/ROLE-003.md) | Subject Matter Expert (SME) | ⚠️ Not answered | ⚠️ Not answered | — | Multiple SMEs may be listed |
| [ROLE-004](../details/ROLE-004.md) | Auditor | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-005](../details/ROLE-005.md) | Implementer | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-006](../details/ROLE-006.md) | Enterprise Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-007](../details/ROLE-007.md) | Business Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-008](../details/ROLE-008.md) | Data Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-009](../details/ROLE-009.md) | Application Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-010](../details/ROLE-010.md) | Technology Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-011](../details/ROLE-011.md) | Business Analyst | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-012](../details/ROLE-012.md) | Delivery Lead | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-013](../details/ROLE-013.md) | Project Manager | ⚠️ Not answered | ⚠️ Not answered | — | |
| [ROLE-014](../details/ROLE-014.md) | Data Owner | ⚠️ Not answered | ⚠️ Not answered | — | Specify data domain in Notes |
| [ROLE-015](../details/ROLE-015.md) | Application Owner | ⚠️ Not answered | ⚠️ Not answered | — | Specify application in Notes |

---

## Triggering Events Summary

<details>
<summary>📋 Guidance</summary>

List the key events that activate role involvement in this engagement. Map each trigger to the roles it activates and the action required. Add engagement-specific triggers as needed.

</details>

| Trigger | Roles Activated | Action Required |
|---------|----------------|-----------------|
| New engagement initiated | ROLE-006, ROLE-013, ROLE-011 | Kick off interviews, schedule sessions, produce SAoW |
| Phase gate reached | ROLE-001, ROLE-006, ROLE-004 | Architecture review, compliance check, phase sign-off |
| Architecture Vision presented | ROLE-001, ROLE-002, ROLE-006 | Stakeholder review and approval |
| Architecture Contract raised | ROLE-001, ROLE-012, ROLE-006 | Review, negotiate, and sign |
| ACR raised (standard) | ROLE-006, ROLE-004, ROLE-001 | Impact assessment, governance decision, update Change Register |
| ACR raised (waiver required) | ROLE-001, ROLE-006, ROLE-004 | Waiver approval via IGP §6 process |
| Delivery gate approaching | ROLE-012, ROLE-004, ROLE-005 | Prepare compliance evidence, conduct gate review |
| Non-conformance identified | ROLE-004, ROLE-006, ROLE-005 | Raise non-conformance, agree remediation, track to closure |
| Data Architecture phase initiated | ROLE-008, ROLE-014, ROLE-003 | Data Architecture interviews, data model validation |
| Application Architecture phase initiated | ROLE-009, ROLE-015, ROLE-003 | Application Architecture interviews, portfolio review |
| ⚠️ Not answered | ⚠️ Not answered | ⚠️ Not answered |

---

## Engagement Calendar

<details>
<summary>📋 Guidance</summary>

Define the recurring meetings and governance activities for this engagement. Assign the roles expected to attend each. Add or remove rows to match the engagement's governance structure.

</details>

| Cadence | Meeting / Activity | Roles Present | Notes |
|---------|-------------------|---------------|-------|
| Weekly | Architecture Working Group | ROLE-006, ROLE-007, ROLE-008, ROLE-009, ROLE-010, ROLE-011 | Core architecture team |
| Weekly | Delivery Status Review | ROLE-012, ROLE-005, ROLE-006 | Phase G onwards |
| Fortnightly | Stakeholder Briefing | ROLE-001, ROLE-002, ROLE-006 | Progress update and decisions |
| Monthly | Steering Committee | ROLE-001, ROLE-006, ROLE-013 | Governance and escalations |
| Per phase | Phase Gate Review | ROLE-001, ROLE-004, ROLE-006, ROLE-012 | Phase sign-off |
| Per work package | Delivery Gate Review | ROLE-004, ROLE-005, ROLE-012 | Compliance assessment |
| Per ADR | ADR Review | ROLE-006, relevant Domain Architect, ROLE-001 | Decision capture |
| As needed | Emergency ACR Review | ROLE-001, ROLE-006, ROLE-004 | Waiver or dispensation |
| ⚠️ Not answered | ⚠️ Not answered | ⚠️ Not answered | |

---

## Escalation Paths

<details>
<summary>📋 Guidance</summary>

Summarise the escalation structure for this engagement. Confirm or override the canonical paths from `role-catalogue.md` based on the engagement's organisational context.

</details>

| Role | Escalates To | Receives From |
|------|-------------|---------------|
| ROLE-001 Stakeholder | Board / C-suite | Enterprise Architect (ROLE-006), Delivery Lead (ROLE-012) |
| ROLE-006 Enterprise Architect | Stakeholder (ROLE-001) | All Domain Architects, Business Analyst, Delivery Lead, Auditor |
| ROLE-012 Delivery Lead | Stakeholder (ROLE-001), Enterprise Architect (ROLE-006) | Implementer (ROLE-005) |
| ROLE-004 Auditor | Enterprise Architect (ROLE-006) | Implementer (ROLE-005), Delivery Lead (ROLE-012) |
| ROLE-011 Business Analyst | Enterprise Architect (ROLE-006), Delivery Lead (ROLE-012) | Stakeholder (ROLE-001), SMEs (ROLE-003) |
| ROLE-014 Data Owner | Data Architect (ROLE-008), Stakeholder (ROLE-001) | Data Architect (ROLE-008) |
| ROLE-015 Application Owner | Application Architect (ROLE-009), Stakeholder (ROLE-001) | Application Architect (ROLE-009) |

---

## Role Descriptions

<details>
<summary>📋 Guidance</summary>

Full responsibilities and typical tasks for each active role. Remove sections for roles not active in this engagement. The canonical definitions (including RACI defaults, triggering events, cadence, and escalation paths) are in `skills/ea-engagement-lifecycle/references/role-catalogue.md`.

</details>

### ROLE-001 — Stakeholder

**Responsibilities:**
- Provide strategic direction and priorities for the engagement
- Approve the Architecture Vision and Statement of Architecture Work
- Hold final decision authority on waivers, dispensations, and Architecture Change Requests
- Set risk appetite and constraint boundaries
- Sign off on the Architecture Contract before implementation begins

**Typical Tasks:**
- Phase A: approve SAoW and Architecture Vision
- Phase F: review and approve Architecture Contract
- Phase G: approve dispensations and major ACRs
- Phase H: approve or reject Architecture Change Requests

---

### ROLE-002 — Stakeholder Agent

**Responsibilities:**
- Represent stakeholder interests in architecture reviews and working groups
- Relay decisions when the Stakeholder is unavailable
- Validate that architecture artifacts align with stakeholder priorities
- Track stakeholder concerns and communicate resolutions back

**Typical Tasks:**
- Attend Architecture Working Group on behalf of Stakeholder
- Review artifacts and provide feedback during interviews
- Raise and track stakeholder concerns (CON-NNN)
- Brief Stakeholder ahead of phase gate reviews

---

### ROLE-003 — Subject Matter Expert (SME)

**Responsibilities:**
- Validate architecture assumptions in their domain of expertise
- Provide domain knowledge during interviews and workshops
- Review and challenge artifacts in their area
- Identify risks and constraints not visible to the architecture team

**Typical Tasks:**
- Phases B–D: participate in domain architecture interviews
- Validate Gap Analysis findings in their domain
- Review and sign off technical specifications
- Contribute to ADR option analysis when domain expertise is required

---

### ROLE-004 — Auditor

**Responsibilities:**
- Conduct T1/T2/T3 compliance reviews on all artifacts
- Participate in ARB reviews and governance forums
- Track open non-conformances and dispensations
- Produce Architecture Compliance Assessment reports
- Verify that implementation conforms to the approved architecture

**Typical Tasks:**
- All phases: T1/T2/T3 compliance checks on artifacts reaching "In Review"
- Phase G: lead Architecture Compliance Assessments; review delivery gate evidence
- Phase H: review ACRs for impact on approved architecture baseline
- ARB: prepare and present compliance findings

---

### ROLE-005 — Implementer

**Responsibilities:**
- Execute approved architecture within agreed constraints
- Raise Architecture Change Requests (ACRs) when deviations are needed
- Provide implementation progress reports at governance gates
- Participate in compliance reviews
- Deliver rollback and validation evidence at each gate

**Typical Tasks:**
- Phase G: report implementation progress; submit compliance evidence; raise ACRs for required deviations
- Phase H: track implementation of approved architecture changes
- All phases: flag emerging risks to the Delivery Lead

---

### ROLE-006 — Enterprise Architect

**Responsibilities:**
- Lead the ADM process end-to-end across all phases
- Approve Architecture Vision and domain architectures
- Chair or co-chair the Architecture Working Group and ARB
- Manage the Architecture Contract and compliance programme
- Mentor domain architects and maintain architecture standards
- Resolve cross-domain conflicts and alignment issues

**Typical Tasks:**
- All phases: lead interviews and artifact development; maintain engagement.json state
- Phase A: draft Architecture Vision and Statement of Architecture Work
- Phases B–D: coordinate domain architects; review domain architectures for coherence
- Phases E–F: consolidate Gap Analysis, Architecture Roadmap, and Migration Plan
- Phase G: oversee compliance programme; approve dispensations
- Phase H: assess ACRs for strategic impact; recommend ADM re-entry where warranted

---

### ROLE-007 — Business Architect

**Responsibilities:**
- Develop the Business Architecture artifact
- Facilitate business process and capability workshops
- Validate the business model, operating model, and capability map
- Identify business gaps and propose work packages
- Align business architecture to strategy and drivers

**Typical Tasks:**
- Phase B: lead Business Architecture interviews; develop process flows, capability model, and organisation charts; produce Gap Analysis (Business)
- Phase E: contribute business-domain work packages to the Architecture Roadmap
- Phase G: support compliance assessments for business-domain deliverables

---

### ROLE-008 — Data Architect

**Responsibilities:**
- Develop the Data Architecture artifact
- Define logical and physical data models
- Identify data governance, quality, and lineage requirements
- Assess data gaps and propose remediation work packages
- Coordinate data ownership assignments with Data Owner(s)

**Typical Tasks:**
- Phase C-Data: lead Data Architecture interviews; develop entity models, data flow diagrams, and data catalogue; produce Gap Analysis (Data)
- Phase E: contribute data-domain work packages to the Architecture Roadmap
- Phase G: support compliance assessments for data-domain deliverables

---

### ROLE-009 — Application Architect

**Responsibilities:**
- Develop the Application Architecture artifact
- Map application capabilities to business processes
- Define integration architecture and patterns
- Assess the current application portfolio and identify gaps
- Recommend make-vs-buy and retire/replace decisions

**Typical Tasks:**
- Phase C-App: lead Application Architecture interviews; develop application component diagrams, integration maps, and application catalogue; produce Gap Analysis (Application)
- Phase E: contribute application-domain work packages to the Architecture Roadmap
- Phase G: support compliance assessments for application-domain deliverables

---

### ROLE-010 — Technology Architect

**Responsibilities:**
- Develop the Technology Architecture artifact
- Define infrastructure components, platforms, and technology standards
- Assess technology gaps and propose work packages
- Ensure security, resilience, and performance requirements are addressed
- Maintain the technology radar and standards register

**Typical Tasks:**
- Phase D: lead Technology Architecture interviews; develop infrastructure diagrams, technology portfolio, and platform catalogue; produce Gap Analysis (Technology)
- Phase E: contribute technology-domain work packages to the Architecture Roadmap
- Phase G: support compliance assessments for technology-domain deliverables

---

### ROLE-011 — Business Analyst

**Responsibilities:**
- Elicit, document, and maintain the Requirements Register
- Validate architecture artifacts against captured requirements
- Facilitate stakeholder workshops and requirements review sessions
- Produce and maintain the Traceability Matrix
- Flag requirement conflicts or gaps to the Enterprise Architect

**Typical Tasks:**
- Requirements phase: lead requirements elicitation; produce Requirements Register (REQ-NNN) and Traceability Matrix
- Phases B–D: validate domain architectures against requirements; flag gaps
- Phase G: support compliance assessments by verifying delivered solutions meet stated requirements
- Phase H: assess change requests for requirements impact

---

### ROLE-012 — Delivery Lead

**Responsibilities:**
- Manage implementation teams and delivery schedule
- Report delivery progress at architecture governance gates
- Escalate delivery risks to Stakeholder and architecture risks to Enterprise Architect
- Coordinate with Enterprise Architect on conformance and ACR resolution
- Manage delivery scope and gate evidence

**Typical Tasks:**
- Phase F: contribute delivery constraints and schedule to the Migration Plan
- Phase G: attend compliance reviews; report work package status; co-ordinate ACR raising
- Phase H: review and endorse ACRs before submission to governance

---

### ROLE-013 — Project Manager

**Responsibilities:**
- Maintain the engagement schedule and track artifact completion milestones
- Coordinate stakeholder availability for interviews and reviews
- Manage engagement risks, issues, assumptions, and dependencies (RAID log)
- Produce engagement status reports
- Facilitate action item tracking from governance meetings

**Typical Tasks:**
- All phases: track phase completion against schedule; coordinate interview scheduling; circulate meeting notes and action items
- Phase A: manage SAoW sign-off process; track stakeholder engagement schedule
- Phase G: coordinate delivery gate scheduling; track outstanding compliance items

---

### ROLE-014 — Data Owner

**Responsibilities:**
- Define data quality requirements and standards for their domain
- Approve logical and physical data models for their domain
- Set data access, retention, and disposal policies
- Participate in data architecture reviews
- Validate data governance decisions and ownership assignments

**Typical Tasks:**
- Phase C-Data: participate in Data Architecture interviews; validate entity models and data flows; define governance requirements; review Gap Analysis (Data)
- Phase G: validate that implemented data solutions conform to governance policies
- Phase H: assess data-related ACRs for ownership impact

---

### ROLE-015 — Application Owner

**Responsibilities:**
- Define application capability requirements for their application
- Approve application architecture decisions affecting their application
- Participate in application portfolio reviews and lifecycle decisions
- Validate integration requirements and patterns
- Input to make-vs-buy and retire/replace decisions

**Typical Tasks:**
- Phase C-App: participate in Application Architecture interviews; validate application component design; approve or escalate make-vs-buy decisions; review Gap Analysis (Application)
- Phase G: validate that delivered application solutions conform to approved architecture
- Phase H: assess application-related ACRs for lifecycle impact

---

## Councils and Governance Bodies

<details>
<summary>📋 Guidance</summary>

Governance bodies are collective entities — they are not individual roles and have no ROLE-NNN ID. Populate chair and membership from the Active Roles table above. Remove any body not active in this engagement. Full duties and canonical definitions are in `skills/ea-engagement-lifecycle/references/role-catalogue.md`.

</details>

### Architecture Review Board (ARB)

**Chair:** {{arb_chair}} (typically ROLE-006 Enterprise Architect or a designated ARB Chair)
**Members:** {{arb_members}}
**Cadence:** {{arb_cadence}} (typically monthly + ad hoc for emergency ACRs and phase gates)

**Duties:**
- Review and approve, reject, or defer Strategic and Tactical architecture decisions
- Approve changes to Architecture Principles
- Grant or refuse dispensations and waivers raised under the Implementation Governance Plan
- Review and endorse Architecture Change Requests (ACRs) with engagement-wide impact
- Assess architecture compliance at phase gate reviews
- Resolve cross-domain conflicts escalated by the Enterprise Architect

**Typical Tasks:**
- Monthly: review open decisions, dispensation requests, and ACRs submitted for approval
- Per phase gate: assess artifact compliance; approve or withhold phase progression
- Per ADR (Strategic authority): receive notification; endorse or challenge the decision
- Per non-conformance: review remediation plans; approve or reject resolution approaches
- Emergency session: assess and decide ACRs requiring immediate architecture deviation

**Authority:** Approve / Reject / Defer / Escalate — per the Governance Framework §4 Terms of Reference
**Escalation:** Board / C-suite for decisions that exceed agreed ARB authority

---

### EA Working Group (AWG)

**Chair:** {{awg_chair}} (ROLE-006 Enterprise Architect)
**Members:** {{awg_members}} (typically ROLE-007 to ROLE-011 core; ROLE-002, ROLE-003, ROLE-013 as required)
**Cadence:** {{awg_cadence}} (typically weekly)

**Duties:**
- Coordinate architecture work across all active domains
- Peer-review artifacts in progress before formal "In Review" status
- Track open concerns (CON-NNN), in-progress ADRs, and open A3 decision items
- Align on cross-domain design choices; surface conflicts to the Enterprise Architect
- Maintain cadence on interview scheduling, artifact completion, and phase milestones
- Identify and escalate issues that require ARB authority or Stakeholder decision

**Typical Tasks:**
- Weekly: review artifact progress, outstanding decisions, and outputs from interviews in the prior week
- Per artifact: informal peer review before status changes to "In Review"
- Per interview completed: share outputs across domain architects for cross-domain alignment
- Per ADR in progress: discuss options analysis; align on recommendation before the ADR is finalised
- Per concern (CON-NNN): assess whether it warrants escalation or can be resolved at team level

**Authority:** Operational — within patterns and principles approved by the ARB
**Escalation:** Enterprise Architect escalates from AWG to ARB or Stakeholder as required

---

### Centre of Excellence (CoE)

**Lead:** {{coe_lead}} (Chief Architect or EA Practice Lead)
**Members:** {{coe_members}}
**Cadence:** Monthly (governance/standards review); quarterly (maturity reporting); continuous (knowledge base)

**Purpose:** The CoE is the custodian of EA standards, patterns, methods, and capability across the organisation. Where the ARB makes decisions and the AWG coordinates engagement work, the CoE builds the knowledge infrastructure that enables consistent, high-quality architecture practice across all engagements.

**Duties:**
- Establish, maintain, and publish architecture standards, patterns, and guidelines for use across engagements and delivery teams
- Govern the architecture repository — artifact templates, reference architectures, ADRs, and approved patterns
- Define and maintain EA tooling, methods, and the ADM tailoring guide for the organisation
- Measure and report architecture maturity across the portfolio (capability maturity, compliance rates, ADR coverage)
- Provide training, coaching, and onboarding for architects and delivery teams new to EA practice
- Facilitate architecture communities of practice; curate lessons learned across engagements
- Identify emerging patterns, technology shifts, and industry standards for consideration as future principles or standards

**Typical Tasks:**
- Per engagement kickoff: provide applicable standards, reference architectures, and pre-approved patterns to the engagement team
- Per phase: review new ADRs and patterns for promotion to the CoE knowledge base
- Per engagement close: conduct post-engagement lessons-learned review; update patterns, templates, or guidelines where warranted
- Quarterly: publish architecture maturity assessment; report compliance trends; update technology radar
- Annually: review and update Architecture Principles, EA method, and tailoring guides

**Authority:** Standard-setting — the CoE publishes standards that engagements must follow unless formally tailored via the ARB. The CoE does not hold decision authority over individual engagement decisions.

**Relationship to other bodies:**
- **ARB:** CoE proposes new standards and principles for ARB ratification
- **AWG:** CoE provides reference materials; AWG surfaces engagement learnings back to CoE
- **Engagements:** CoE provides the templates and standards all engagements consume

---

## Appendix A3 — Decision Log

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Owner | Date |
|----|----------|-------|-----------|--------|------|--------|------|---------|-------|------|
| — | | | | | | | | | | |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Relevance |
|--------|-------|--------|-----------|
| — | | | |

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
