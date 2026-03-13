# EA Engagement Patterns

This reference documents common engagement patterns for Enterprise Architecture work, how to recognise them, how to tailor the TOGAF ADM, and the anti-patterns to avoid in each context. The goal is to help architects select the right approach at the start of an engagement rather than defaulting to a single rigid process.

---

## Understanding Engagement Patterns

An engagement pattern is a recurring context that shapes how an EA engagement should be structured, which ADM phases deserve the most attention, and what stakeholder concerns will dominate. Recognising the pattern early prevents wasted effort and mis-scoped deliverables.

No engagement is a single pure pattern. Most are combinations; the value of this taxonomy is in identifying the dominant driver and tailoring accordingly.

---

## Pattern 1 — Greenfield (New Enterprise or New Domain)

### Description
The organisation is building a new capability, business unit, or system from scratch. There is little or no baseline architecture to document. The focus is entirely on the target state.

### Recognising It
- The engagement starts with "we need to build X from the ground up"
- There is no legacy constraint on the chosen technology or process
- Stakeholders want to know what best-in-class looks like
- The business case is investment-driven, not cost-reduction-driven

### ADM Tailoring
- Spend significant effort in Phase A establishing the vision and scope before anything else; the target is the whole story
- Phase B (Business) and Phase C (Information Systems) carry the most weight
- Baseline documentation in Phases B–D is either minimal or derived from market reference models (BIAN for banking, eTOM for telecoms, etc.)
- Phase E and F move quickly if the target is well-defined and there is no migration complexity
- Phase G may align tightly with an agile delivery model; use Architecture Contracts per sprint milestone rather than per phase

### Key Risks
- Scope creep: a greenfield invitation can expand indefinitely
- Stakeholder alignment is harder when no legacy anchors the discussion
- Perfectionism: architects may over-engineer a target that needs to be validated by building

### Useful Artefacts
- Capability Map (target-state only)
- Solution Concept Diagram
- Reference Architecture (adopted or adapted from an industry model)
- Architecture Principles (to constrain technology choices)

---

## Pattern 2 — Legacy Modernisation

### Description
The organisation has significant existing systems, processes, or data that need to be updated, replaced, or re-platformed, while keeping the business running throughout.

### Recognising It
- Systems described as "end of life," "tech debt," or "not supported"
- High maintenance cost as a percentage of IT spend
- Business change is slow because the legacy blocks it
- A specific trigger: vendor end-of-support, regulatory deadline, cloud mandate

### ADM Tailoring
- Invest heavily in baseline documentation in Phases B–D — you cannot plan a migration without knowing what you have
- Application Portfolio Catalogue and Technology Portfolio Catalogue are essential starting points
- Phase E is critical: the gap between a complex baseline and a clean target must be bridged by realistic transition architectures, not a single "lift and shift"
- Define at least two Transition Architectures (a coexistence state and a cutover state)
- Phase G must include decommission criteria, not just go-live criteria

### Key Risks
- Under-documenting the baseline: architects assume they know the estate and later discover undocumented integrations
- "Big bang" temptation: stakeholders want to cut over in one step to avoid running dual systems; this rarely succeeds for complex estates
- Data migration complexity is consistently underestimated; treat it as a first-class work stream

### Useful Artefacts
- Application Gap Analysis
- Technology Gap Analysis
- Application / Data Matrix
- Transition Architecture diagrams
- Data Migration Plan (as input to the Implementation Plan)

---

## Pattern 3 — Consolidation / Rationalisation

### Description
The organisation has accumulated redundant systems, often through mergers, acquisitions, or organic growth, and wants to reduce the number of platforms, vendors, or data stores.

### Recognising It
- Multiple systems doing the same job
- Post-merger integration mandate
- Cost reduction programme targeting application spend
- Vendor-count or licence-count reduction target

### ADM Tailoring
- Phase C (Application and Data Architecture) dominates: the portfolio must be fully catalogued before rationalisation decisions can be made
- Use an Application Portfolio Assessment framework (e.g., TIME model — Tolerate, Invest, Migrate, Eliminate) to classify each system
- Phase E decisions about which system "wins" are politically charged; architect must facilitate, not decide
- Phase F must account for the business disruption of migrating users from eliminated systems
- Organisational change management is a key dependency

### Key Risks
- Anchoring to the incumbent system of the dominant merger partner, ignoring a better alternative from the other entity
- Underestimating data quality issues in the system that "wins" — it may not be able to absorb all the data from eliminated systems
- Not decommissioning: applications are rationalised on paper but the old systems are never turned off

### Useful Artefacts
- Application Portfolio Catalogue with TIME classification
- Application / Function Matrix
- Rationalisation Decision Log
- Data Entity / Data Component Catalogue
- Transition Architecture (coexistence → consolidated)

---

## Pattern 4 — Compliance-Driven Architecture

### Description
An external regulatory or legal requirement forces architecture change. Examples include GDPR, PCI-DSS, DORA, SOX, HIPAA, or a sector-specific regulation.

### Recognising It
- A regulatory deadline or audit finding is the primary driver
- Stakeholders are from risk, compliance, or legal functions, not just IT
- The scope of change is defined externally; the architect's job is to find the most efficient path to compliance
- There is usually a hard deadline that cannot move

### ADM Tailoring
- Phase A must map the regulation's requirements to architecture concerns immediately; use a Regulation-to-Requirement Traceability Matrix from day one
- Requirements Management (the central ADM hub) is unusually prominent: regulatory requirements are non-negotiable constraints, not aspirations
- Baseline assessment in Phases B–D focuses on compliance gaps, not general improvement
- Phase E work packages must be sequenced by regulatory risk priority, not business value alone
- Phase G must produce Compliance Assessments that can be presented to auditors

### Key Risks
- Treating compliance as a checkbox exercise and missing systemic architecture improvements that would reduce future compliance cost
- Architecture becomes a "point solution" for each regulation rather than a coherent enterprise view
- Scope creep into adjacent improvements delays the compliance deliverable

### Useful Artefacts
- Regulation / Requirement Traceability Matrix
- Data Flow Diagram (especially for data residency and privacy regulations)
- Security Architecture View
- Compliance Assessment
- Architecture Requirements Specification (regulatory constraints)

---

## Pattern 5 — Cloud Migration / Adoption

### Description
The organisation is moving workloads from on-premises infrastructure to public, private, or hybrid cloud.

### Recognising It
- A "cloud first" or "cloud by default" policy has been adopted
- Infrastructure contracts are expiring and renewal is the trigger
- Cost optimisation through variable-cost infrastructure is the goal

### ADM Tailoring
- Phase D (Technology Architecture) carries the most weight
- Use a Cloud Migration Pattern (6 Rs: Rehost, Replatform, Repurchase, Refactor, Retire, Retain) to classify each workload
- Phase C must assess application cloud-readiness before Phase D defines the target
- Landing Zone design is a key Phase D output; it should precede workload migration
- Phase G governance must include cloud cost management and security posture monitoring

### Key Risks
- Lift-and-shift of poorly designed applications that will be more expensive in the cloud than on-premises
- Security and compliance gaps in the cloud landing zone discovered after migration begins
- Vendor lock-in through adoption of proprietary cloud services without an exit strategy

---

## ADM Tailoring Principles

Regardless of pattern, the following tailoring principles apply:

| Principle | Guidance |
|---|---|
| Scope before depth | Agree the breadth of the engagement before diving into any single domain |
| Phase prioritisation | Not all phases deserve equal effort; weight phases to the dominant driver |
| Iteration over perfection | Deliver useful architecture in iterations; a 70% complete architecture that guides decisions is better than a 100% complete one delivered after decisions have been made |
| Stakeholder alignment before artefact production | No amount of documentation compensates for misaligned stakeholders |
| Transition architectures are not optional | Any migration of real complexity needs explicit intermediate states |

---

## Common Anti-Patterns

### Anti-Pattern 1 — The Documentation Cemetery
Architecture work produces large volumes of documentation that are never read, never updated, and have no connection to delivery. Caused by treating phase completion as the goal rather than decision support.

**Counter:** Define a minimum viable artefact set for the engagement. Every artefact must have a named consumer and a decision it informs.

### Anti-Pattern 2 — Architecture as Approval Gateway
Every project must pass through an architecture review board that produces delays but no value. The board applies standards inconsistently and lacks the authority to enforce decisions.

**Counter:** Publish Architecture Principles and Standards that projects can self-assess against. Reserve board review for genuinely novel or high-risk decisions.

### Anti-Pattern 3 — Ivory Tower Architecture
Architects develop the target state without involving delivery teams, then hand over a document to be "implemented." The delivered system diverges significantly from the architecture.

**Counter:** Embed architecture engagement in Phase G. Use Architecture Contracts. Accept that the architecture will need to evolve as delivery learns.

### Anti-Pattern 4 — Perpetual Baseline
The engagement is consumed by documenting the current state, with no time remaining to define the target. Stakeholders lose patience and confidence.

**Counter:** Time-box baseline documentation. Accept known unknowns. Start target-state conversations in parallel with baseline discovery.

### Anti-Pattern 5 — Single-Framework Dogma
Forcing every engagement through all ADM phases in strict sequence regardless of context, or insisting on full Zachman coverage when a single viewpoint would suffice.

**Counter:** The ADM is a guide, not a prescription. TOGAF explicitly supports tailoring. Match the method to the problem.

### Anti-Pattern 6 — Ignoring Non-Functional Requirements
The architecture addresses functional capabilities but fails to specify performance, availability, security, or operability requirements. Delivery teams make ad hoc decisions that are hard to retrofit.

**Counter:** Include a dedicated Architecture Requirements Specification section for non-functional requirements, linked to technology and application architecture decisions.
