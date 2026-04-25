# Role Catalogue

Canonical reference for all roles involved in EA engagements. Each entry defines responsibilities, typical tasks, default RACI position, triggering events, meeting cadence, and escalation paths.

Use role IDs (ROLE-NNN) in the Stakeholder Map, Statement of Architecture Work §5, and the Role Catalogue engagement artifact to link named individuals to this reference.

---

## ROLE-001 — Stakeholder

**Description:** Owner of the architecture. The Stakeholder holds decision rights over the target architecture and any relief from or enforcement of it — including waivers, dispensations, and change approvals. Sets the risk appetite and strategic priorities that govern all architecture decisions.

**Responsibilities:**
- Provide strategic direction and priorities for the engagement
- Approve the Architecture Vision and Statement of Architecture Work
- Hold final decision authority on waivers, dispensations, and Architecture Change Requests
- Set risk appetite and constraint boundaries
- Sign off on Architecture Contract before implementation begins

**Typical Tasks:**
- Phase A: approve SAoW and Architecture Vision
- Phase F: review and approve Architecture Contract
- Phase G: approve dispensations and major ACRs
- Phase H: approve/reject Architecture Change Requests

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | A |
| Stakeholder Map | A |
| Implementation Governance Plan | A |
| Change Register | A |
| ADRs | C |

**Triggering Events:**
- Architecture Vision presented for approval
- Architecture Contract raised for sign-off
- ACR requiring waiver or dispensation
- Phase gate review requiring sponsor decision
- Escalation from Enterprise Architect

**Typical Cadence / Meetings:**
- Steering Committee: monthly (or as agreed)
- Phase gate reviews: at each ADM phase transition
- Emergency ACR reviews: as needed

**Escalation Path:**
- Escalates to: Board / C-suite (corporate governance layer)
- Receives escalations from: Enterprise Architect, Delivery Lead

---

## ROLE-002 — Stakeholder Agent

**Description:** Representative of the Stakeholder, acting on their behalf in governance forums and day-to-day architecture activities. Holds delegated authority for routine decisions; escalates non-routine matters to the Stakeholder.

**Responsibilities:**
- Represent stakeholder interests in architecture reviews and working groups
- Relay decisions when the Stakeholder is unavailable
- Validate that architecture artifacts align with stakeholder priorities
- Track stakeholder concerns and communicate resolutions back

**Typical Tasks:**
- Attend Architecture Working Group on behalf of Stakeholder
- Review artifacts and provide feedback during interviews
- Raise stakeholder concerns (CON-NNN) and track responses
- Brief Stakeholder ahead of phase gate reviews

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs | C |

**Triggering Events:**
- Stakeholder unavailable for a scheduled review
- Architecture review meeting or workshop scheduled
- ACR raised requiring stakeholder input
- Stakeholder concern (CON-NNN) logged

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly or fortnightly
- All phase gate reviews

**Escalation Path:**
- Escalates to: Stakeholder (non-routine decisions)
- Receives from: Enterprise Architect (briefings, review requests)

---

## ROLE-003 — Subject Matter Expert (SME)

**Description:** Possesses specialised knowledge about the enterprise, its systems, processes, or external environment. Provides knowledge, advice, and validation of architecture interpretations within their domain.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | I |
| Stakeholder Map | I |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs | C |

**Triggering Events:**
- Domain architecture interview or workshop scheduled
- Gap Analysis requiring domain validation
- Technical validation required for an ACR or ADR
- Architecture assumption challenged by delivery team

**Typical Cadence / Meetings:**
- Domain architecture working sessions (per active phase)
- Ad-hoc validation requests

**Escalation Path:**
- Escalates to: Domain Architect (decisions requiring architecture authority)
- Receives from: Enterprise Architect, Domain Architects (validation requests)

---

## ROLE-004 — Auditor

**Description:** Performs systematic reviews of both the target architecture and its implementation. Ensures architecture quality, standards compliance, and conformance to approved decisions. May operate within a formal Architecture Review Board (ARB) or as a peer reviewer.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | I |
| Implementation Governance Plan | C |
| Change Register | R |
| ADRs | C |

**Triggering Events:**
- Artifact reaches "In Review" status
- Delivery gate approaching
- ACR raised requiring conformance assessment
- Phase G initiated
- Non-conformance identified during implementation

**Typical Cadence / Meetings:**
- Architecture Review Board: monthly (or per governance calendar)
- Delivery gate reviews: per work package
- Compliance assessment cycle: per §4 of Implementation Governance Plan

**Escalation Path:**
- Escalates to: Enterprise Architect (non-conformances requiring architecture decisions)
- Receives from: Implementer (compliance review requests), Delivery Lead (gate preparation)

---

## ROLE-005 — Implementer

**Description:** Responsible for all change activity — from transformative capital projects to incremental operational changes. Holds decision rights about proposed implementation choices (design, product selection, change sequence) within the bounds set by the Architecture Contract.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | I |
| Stakeholder Map | I |
| Implementation Governance Plan | C |
| Change Register | R |
| ADRs | C |

**Triggering Events:**
- Architecture Contract signed (engagement authorised to start delivery)
- Delivery gate approaching
- Deviation from approved architecture required during build
- Implementation risk or issue identified

**Typical Cadence / Meetings:**
- Architecture Working Group: as required for status reporting
- Delivery gates: per work package schedule

**Escalation Path:**
- Escalates to: Delivery Lead (delivery issues), Enterprise Architect (architecture deviations)
- Receives from: Enterprise Architect (architecture direction), Auditor (compliance findings)

---

## ROLE-006 — Enterprise Architect

**Description:** Leads the development and governance of the target architecture across all domains. Accountable for the quality, coherence, and conformance of all architecture work throughout the ADM lifecycle.

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
- Phase E–F: consolidate Gap Analysis, Architecture Roadmap, and Migration Plan
- Phase G: oversee compliance programme; approve dispensations
- Phase H: assess ACRs for strategic impact; recommend ADM re-entry where warranted

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | R |
| Stakeholder Map | R |
| Implementation Governance Plan | R |
| Change Register | R |
| ADRs | R |

**Triggering Events:**
- New engagement initiated
- Phase gate reached
- ACR or ADR raised
- Architecture deviation detected
- Stakeholder escalation or governance issue
- Cross-domain conflict requiring resolution

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly (chair)
- Steering Committee: monthly (presenter)
- ARB: as chair or primary presenter
- All phase gate reviews

**Escalation Path:**
- Escalates to: Stakeholder (decisions requiring business authority or sponsor approval)
- Receives escalations from: Business Analyst, all Domain Architects, Delivery Lead, Auditor

---

## ROLE-007 — Business Architect

**Description:** Leads the development of the Business Architecture (Phase B), mapping business processes, capabilities, organisational structures, and business rules to the target state. Works closely with business stakeholders and the Business Analyst.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs (Business domain) | R |
| ADRs (Other domains) | C |

**Triggering Events:**
- Phase B initiated
- Business capability gap identified
- Phase B review or gate scheduled
- Business Architecture ACR raised

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly during Phase B
- Business stakeholder workshops: per phase schedule

**Escalation Path:**
- Escalates to: Enterprise Architect
- Receives from: Business Analyst (process and capability input), SMEs (business domain knowledge)

---

## ROLE-008 — Data Architect

**Description:** Leads the development of the Data Architecture (Phase C-Data), defining data models, data flows, data governance requirements, and the target data state. Works closely with the Data Owner.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs (Data domain) | R |
| ADRs (Other domains) | C |

**Triggering Events:**
- Phase C-Data initiated
- Data architecture review or gate scheduled
- Data quality or governance issue identified
- Data Architecture ACR raised

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly during Phase C-Data
- Data governance forum: if applicable (engagement-specific)

**Escalation Path:**
- Escalates to: Enterprise Architect
- Coordinates with: Data Owner (ROLE-014) on data policy and ownership decisions

---

## ROLE-009 — Application Architect

**Description:** Leads the development of the Application Architecture (Phase C-App), defining application components, integration patterns, and the target application landscape. Works closely with Application Owner(s).

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs (Application domain) | R |
| ADRs (Other domains) | C |

**Triggering Events:**
- Phase C-App initiated
- Application architecture review or gate scheduled
- Integration issue or make-vs-buy decision required
- Application Architecture ACR raised

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly during Phase C-App
- Application portfolio review: if applicable (engagement-specific)

**Escalation Path:**
- Escalates to: Enterprise Architect
- Coordinates with: Application Owner (ROLE-015) on portfolio and lifecycle decisions

---

## ROLE-010 — Technology Architect

**Description:** Leads the development of the Technology Architecture (Phase D), defining infrastructure, platforms, and technology standards for the target state. Ensures the technology layer supports security, resilience, and performance requirements.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs (Technology domain) | R |
| ADRs (Other domains) | C |

**Triggering Events:**
- Phase D initiated
- Technology architecture review or gate scheduled
- Platform selection or standard decision required
- Technology Architecture ACR raised

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly during Phase D
- Technology standards review: if applicable (engagement-specific)

**Escalation Path:**
- Escalates to: Enterprise Architect
- Receives from: SMEs (technical domain input), Implementer (technical constraints)

---

## ROLE-011 — Business Analyst

**Description:** Bridges business requirements and architecture. Translates business needs into structured requirements, validates architecture outputs against business intent, and supports stakeholder engagement throughout the ADM.

**Responsibilities:**
- Elicit, document, and maintain the Requirements Register
- Validate architecture artifacts against captured requirements
- Facilitate stakeholder workshops and requirements review sessions
- Produce and maintain the Traceability Matrix
- Flag requirement conflicts or gaps to the Enterprise Architect

**Typical Tasks:**
- Requirements phase: lead requirements elicitation; produce Requirements Register (REQ-NNN) and Traceability Matrix
- Phases B–D: validate domain architectures against requirements; flag gaps
- Phase G: support compliance assessments by verifying that delivered solutions meet stated requirements
- Phase H: assess change requests for requirements impact

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Requirements Register | R |
| Traceability Matrix | R |
| Implementation Governance Plan | C |
| Change Register | C |
| ADRs | C |

**Triggering Events:**
- New engagement initiated (requirements phase kick-off)
- Phase transition (requirements coverage review)
- Architecture artifact completed (requirements validation)
- Change request raised (requirements impact assessment)

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly
- Requirements review sessions: at each phase transition
- Stakeholder workshops: as required

**Escalation Path:**
- Escalates to: Enterprise Architect (requirement conflicts or ambiguity), Delivery Lead (scope issues)
- Receives from: Stakeholder / Stakeholder Agent (business direction), SMEs (domain requirements)

---

## ROLE-012 — Delivery Lead

**Description:** Accountable for the delivery of implementation work packages. Ensures that delivery activities conform to the Architecture Contract and are executed on schedule and within budget. The primary point of contact between the architecture team and the delivery organisation during Phase G.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | I |
| Implementation Governance Plan | R |
| Change Register | C |
| ADRs | I |

**Triggering Events:**
- Architecture Contract signed (delivery authorised)
- Work package initiated
- Delivery gate approaching
- Architecture deviation identified during delivery
- Implementation risk or issue escalated from Implementer

**Typical Cadence / Meetings:**
- Architecture Working Group: weekly (conformance status)
- Delivery status reviews: weekly
- Phase gate reviews: per work package

**Escalation Path:**
- Escalates to: Stakeholder (delivery risks), Enterprise Architect (architecture conformance issues)
- Receives escalations from: Implementer (delivery and deviation issues)

---

## ROLE-013 — Project Manager

**Description:** Responsible for the day-to-day management of the architecture engagement — schedule, resources, coordination, and communication. Works across all phases to keep the engagement on track without owning architecture content.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | C |
| Stakeholder Map | C |
| Implementation Governance Plan | C |
| Change Register | I |
| ADRs | I |

**Triggering Events:**
- Phase initiated (schedule planning required)
- Artifact approaching completion deadline
- Governance meeting scheduled (coordination needed)
- Engagement status report due

**Typical Cadence / Meetings:**
- Weekly status meetings (all phases)
- Steering Committee reporting: monthly
- Phase gate preparation: per phase

**Escalation Path:**
- Escalates to: Delivery Lead (delivery schedule risks), Stakeholder (engagement-level risks)
- Receives from: all roles (action items, schedule dependencies, resource requests)

---

## ROLE-014 — Data Owner

**Description:** Accountable for a specific data domain or dataset within the organisation. Defines data policies, quality standards, and access rules for their data domain. Participates in Data Architecture development to ensure governance requirements are captured.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | I |
| Stakeholder Map | I |
| Implementation Governance Plan | I |
| Change Register (data domain) | C |
| ADRs (data domain) | C |

**Triggering Events:**
- Data Architecture phase (C-Data) initiated
- Data model requiring ownership assignment
- Data governance policy decision required
- Data Architecture ACR or ADR raised affecting their domain

**Typical Cadence / Meetings:**
- Data Architecture working sessions: during Phase C-Data
- Data governance forum: if applicable (engagement-specific)

**Escalation Path:**
- Escalates to: Data Architect (technical data decisions), Stakeholder (data policy decisions with enterprise-wide impact)
- Coordinates with: Data Architect (ROLE-008)

---

## ROLE-015 — Application Owner

**Description:** Accountable for a specific application or application suite within the organisation. Responsible for its functional requirements, lifecycle, and fitness for purpose. Participates in Application Architecture development to ensure portfolio and capability decisions are well-informed.

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

**RACI Defaults:**

| Artifact | RACI |
|----------|------|
| Statement of Architecture Work | I |
| Stakeholder Map | I |
| Implementation Governance Plan | I |
| Change Register (application domain) | C |
| ADRs (application domain) | C |

**Triggering Events:**
- Application Architecture phase (C-App) initiated
- Application portfolio decision required (retire/replace/invest)
- Integration design requiring application owner input
- Application Architecture ACR or ADR raised affecting their application

**Typical Cadence / Meetings:**
- Application Architecture working sessions: during Phase C-App
- Application portfolio review: if applicable (engagement-specific)

**Escalation Path:**
- Escalates to: Application Architect (technical decisions), Stakeholder (strategic application portfolio decisions)
- Coordinates with: Application Architect (ROLE-009)
