# TOGAF ADM Phase Reference Guide

This guide provides a concise but complete reference for each phase of the TOGAF 10 Architecture Development Method (ADM). For each phase, it covers the objectives, key inputs, major steps, key questions, and outputs (artefacts produced).

---

## Preliminary Phase

### Objectives
- Establish the Architecture Capability: governance, organisation, team, tools, and principles.
- Tailor the ADM for the organisation's context.
- Define the Architecture Principles that will govern future architecture work.

### Key Inputs
- TOGAF and other selected architecture frameworks
- Board strategies, business drivers, and constraints
- Existing organisational structures, governance models, and IT strategies
- Existing architecture frameworks, methods, and tools in use

### Major Steps
1. Determine the scope of the enterprise affected by the architecture capability.
2. Confirm governance and support frameworks.
3. Define and establish the Architecture Team.
4. Identify and establish Architecture Principles.
5. Select and implement architecture tooling.
6. Define the Architecture Repository structure.
7. **Link to shared Architecture Repository (if applicable):** If an organisation-wide Architecture Repository exists at `EA-Workspace/Architecture-Repository/`, run `/ea-repo link <slug>` to connect this engagement. The linked repository provides STD, VDR, and THR context during Phases B–D. If running `/ea-new` inside an EA-Workspace, this link is set automatically.
8. Finalise and publish the Architecture Governance framework.

### Key Questions
- What is the enterprise scope for architecture work?
- What governance structures are in place or needed?
- Who are the architecture stakeholders and what are their concerns?
- What principles will constrain future architecture decisions?
- What frameworks, methods, and notations will be used?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Principles Catalogue | Documented set of principles with rationale and implications |
| Architecture Governance Framework | Policies, procedures, and organisational structures for governance |
| Architecture Repository (initial) | Baseline structure for storing architecture outputs |
| Request for Architecture Work (template) | Template used to initiate architecture projects |
| Tailored ADM | Documented customisation of ADM phases and deliverables for the organisation |

### Deep Tactics
- Treat the Architecture Board as a **decision marketplace**, not a review committee.
- Define architecture services with **SLAs** — operate like a product team.
- **Fund architecture as a persistent capability**, not a project overhead.
- Build a **minimal but enforceable standards catalog** — start small, evolve fast.
- Align architecture **KPIs with enterprise OKRs** (e.g., reuse rate, time-to-decision).

### Decision Flow

**What to decide now:** Architecture Principles, governance model, standards catalog scope, team structure, engagement tailoring.

**What to defer:** Technology choices, vendor selections, specific patterns, detailed architecture designs.

**How to handle strong pressure:** If stakeholders insist on specific technology choices in Preliminary, convert to PAD-NNN with constraint boundaries: "We will evaluate cloud platforms in Phase D; constraint: data sovereignty requirements must be met."

**Evidence threshold:** Principles need evidence of organisational need (incidents, costs, regulatory requirements), not just aspiration.

### Decision Flow

**What to decide now:** Strategic direction, goals, objectives, scope boundaries, stakeholder map, high-level constraints.

**What to defer:** All technology, vendor, and pattern decisions. Any specific architecture style choice (microservices, event-driven, etc.) made in Phase A is premature and should be converted to a PAD-NNN with constraint boundaries.

**How to handle strong pressure:** When a sponsor or stakeholder insists on a technology in Phase A, document the constraint boundary, not the commitment. Example: "Sponsor insists on cloud-first → PAD-001: constraint boundary = all new workloads evaluate cloud; resolution path = Phase D Technology Architecture."

**Evidence threshold:** Goals and objectives need baseline metrics and business driver evidence. Strategies need at least one validation approach (pilot, reference case, expert review).

**Key rule:** Directional decisions only. If someone says "we're going microservices" in Phase A, challenge it immediately — that is a Phase C decision at the earliest.

### Decision Flow

**What to decide now:** Capability model, business process boundaries, org design implications, value stream definitions.

**What to defer:** Application boundaries (wait for Phase C), technology platforms (wait for Phase D), detailed data models (wait for Phase C).

**How to handle uncertainty:** Log business capability uncertainties as PAD-NNN entries. Example: "Uncertain whether customer onboarding should be centralised or federated → PAD-002 with resolution path to Phase E after org design workshop."

**Evidence threshold:** Capability gaps need baseline maturity assessment and target state definition. Business process changes need stakeholder validation.

### Decision Flow

**What to decide now:** Data domains and ownership, application boundaries and responsibilities, API contracts, integration patterns.

**What to defer:** Specific technology products and versions (wait for Phase D), detailed implementation designs (wait for Phase G).

**How to handle uncertainty:** POC or spike required before committing to patterns with low reversibility (event sourcing, CQRS, distributed transactions).

**Evidence threshold:** Application architecture needs interface definitions and data flow validation. Integration patterns need proof-of-concept for critical paths.

### Decision Flow

**What to decide now:** Technology platforms, standards, infrastructure topology, security mechanisms.

**What to defer:** Nothing — this is the primary technology decision phase. However, if a technology decision lacks evidence, it becomes a PAD-NNN blocking Phase E.

**Evidence threshold:** Technology decisions need benchmarks, vendor responses, or reference implementations. Vendor lock-in decisions need TCO analysis and exit strategy.

### Decision Flow

**What to decide now:** Work package definitions, transition architectures, benefits assessment.

**Critical action:** Convert all open PAD-NNN entries from Phases A–D into either committed decisions (A3/ADR) or work packages with evidence requirements.

**What to defer:** Nothing should remain deferred at Phase E. Any PAD still open after Phase E is a delivery risk.

**Evidence threshold:** Work packages need evidence-gated prioritisation. Low-evidence packages should be deferred until evidence is gathered.

### Decision Flow

**What to decide now:** Migration wave sequencing, resource allocation, rollout approach.

**How to prioritize:** Evidence-gate prioritisation — work packages with sufficient evidence and high reversibility should precede those with low reversibility and weak evidence.

**What to revisit:** Decisions from earlier phases that new delivery evidence contradicts.

### Decision Flow

**What to enforce now:** All committed architecture decisions (A3/ADR). Deviations require explicit acceptance with risk sign-off or remediation.

**What to create:** New PAD-NNN entries for uncertainties discovered during implementation.

**How to handle deviations:** Every deviation is either accepted (with documented risk) or remediated. No undocumented drift.

### Decision Flow

**What to adapt now:** Revisit decisions based on post-implementation evidence. Retire obsolete architectures and their associated ADRs.

**What to resolve:** Review all expired PAD-NNN entries — resolve or close them.

**Trigger:** New evidence that contradicts a previous decision should trigger a mini-ADM cycle, not a workaround.

### Decision Flow

**What to track:** Every requirement must link to at least one architecture decision or work package. Orphan requirements create hidden gaps.

**How to handle uncertainty:** Requirements with unclear implementation path become PAD-NNN entries with resolution paths.

**Evidence threshold:** Requirements need traceability to goals, objectives, or business drivers. Un traceable requirements are scope risks.

### Hidden Mechanics
- Architecture capability is the **platform** on which all future work runs. Under-invest here and everything downstream slows.
- The standards catalog is a **living product** with consumers, owners, and adoption metrics — not a static document.

### Maturity Indicators
- **L1:** Architecture team is a project overhead; governance is ad-hoc
- **L3:** Architecture team has defined services with SLAs; standards catalog is maintained
- **L5:** Architecture capability is self-funding; governance is automated; standards are continuously pruned

---

## Phase A — Architecture Vision

### Objectives
- Develop a high-level aspirational vision of the target architecture.
- Obtain approval to proceed with the full architecture development.
- Define the scope, constraints, and expectations for the engagement.

### Key Inputs
- Request for Architecture Work
- Architecture Principles
- Existing architecture (if any)
- Business strategy, goals, and drivers

### Major Steps
1. Establish the Architecture Project.
2. Identify and confirm stakeholders, concerns, and requirements.
3. Confirm and elaborate the business goals and strategic drivers.
4. Review and assess existing architecture.
5. Define the target architecture vision at a high level.
6. Define the Statement of Architecture Work and obtain approval.

### Key Questions
- What business problem are we solving?
- What is the scope (time, breadth of enterprise, depth of architecture)?
- Who are the key stakeholders and what are their concerns?
- What constraints are non-negotiable?
- What does success look like?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Vision | Narrative and/or diagram of the target state at a high level |
| Statement of Architecture Work | Agreed scope, schedule, resources, and success criteria |
| Stakeholder Map / Matrix | Who is affected, their concerns, and engagement approach |
| Value Chain Diagram | High-level view of business functions and value flow |
| Solution Concept Diagram | Sketch of the proposed solution |

### Deep Tactics
- Use **"strategic tension"** (current vs desired state) to drive urgency — quantify the gap.
- Build **multiple candidate visions** and force trade-off discussions early.
- Validate vision with **real delivery constraints** (skills, vendors, legacy).
- **Co-create the vision with business leaders** to secure ownership.
- Define **success metrics before moving to Phase B**.

### Hidden Mechanics
- Phase A is a **political and economic instrument**, not just a descriptive exercise. Its purpose is to secure alignment and funding.
- The Architecture Vision is a **negotiation tool**. Build it with stakeholders, not for them.

### Maturity Indicators
- **L1:** Vision is a static document produced by the architecture team
- **L3:** Vision is co-created with business; multiple options are evaluated; success metrics are defined
- **L5:** Vision is continuously updated; mini-ADM cycles validate assumptions before major investment

---

## Phase B — Business Architecture

### Objectives
- Develop the Baseline and Target Business Architecture to the agreed level of detail.
- Identify candidate Architecture Roadmap components from gaps.

### Key Inputs
- Architecture Vision and Statement of Architecture Work
- Architecture Principles
- Baseline Business Architecture (if any)
- Business strategy, process models, org charts

### Major Steps
1. Select reference models, viewpoints, and tools.
2. Develop the Baseline Business Architecture description.
3. Develop the Target Business Architecture description.
4. Perform a gap analysis between baseline and target.
5. Define candidate roadmap components.
6. Resolve impacts across the Architecture Landscape.

### Key Questions
- What business processes, functions, and capabilities are in scope?
- How does the organisation deliver value today?
- What changes are required to the business to achieve the vision?
- What are the business capability gaps?
- What organisational changes are implied?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Business Capability Map | Hierarchical map of enterprise business capabilities |
| Business Interaction Matrix | Which business units interact and how |
| Actor/Role Catalogue | Business actors, roles, and responsibilities |
| Business Process Catalogue | Documented business processes in scope |
| Organisation Map | Structure of business units and relationships |
| Business Gap Analysis | Gaps between baseline and target business architecture |

### Deep Tactics
- **Map capabilities to value streams** — don't model capabilities in isolation.
- Identify **differentiating vs commodity capabilities** — optimize investment accordingly.
- Use business architecture to **challenge org design**, not just reflect it.
- Link capabilities directly to **KPIs and revenue/cost drivers**.
- Focus on **"where to play" and "how to win"** — not just process diagrams.

### Hidden Mechanics
- Business architecture is a **compression function** — it compresses business ambiguity into coherent constraints.
- Capabilities are the **bridge** between strategy and execution. If they are not linked to value streams, the bridge is broken.

### Maturity Indicators
- **L1:** Business architecture reflects current org chart and processes
- **L3:** Capabilities are linked to value streams and KPIs; gap analysis prioritizes by business impact
- **L5:** Capability heatmaps directly drive investment prioritization; org design is challenged by architecture

---

## Phase C — Information Systems Architecture

### Objectives
- Develop the Baseline and Target Data Architecture and Application Architecture.
- This phase has two sub-phases: Data Architecture and Application Architecture (order may vary).

### Key Inputs
- Architecture Vision, Business Architecture outputs
- Baseline data and application assets
- Relevant standards and reference models (e.g., industry data models)

### Major Steps
1. Select reference models, viewpoints, and tools.
2. Develop Baseline Data Architecture.
3. Develop Target Data Architecture.
4. Develop Baseline Application Architecture.
5. Develop Target Application Architecture.
6. Perform gap analysis for data and applications.
7. Identify candidate roadmap components.

### Key Questions
- What data does the business depend on, and who owns it?
- What are the critical data quality and integrity concerns?
- What applications support which business capabilities?
- What systems are redundant, legacy, or to be decommissioned?
- How will data flow across the target application landscape?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Data Entity / Data Component Catalogue | Canonical list of data entities and their owners |
| Application Portfolio Catalogue | Inventory of applications with lifecycle status |
| Data Flow Diagram | How data moves between systems and actors |
| Application / Data Matrix | Which apps handle which data entities |
| Data Gap Analysis | Data capability gaps |
| Application Gap Analysis | Application capability gaps |
| Logical Data Model | Entity-relationship model at the logical level |
| Application Communication Diagram | Integration and interface map |

### Deep Tactics
- Treat **data as a product** — define clear ownership, quality SLAs, and lifecycle governance for every critical data entity.
- Design **interoperability early** — specify API contracts, event schemas, and integration patterns before selecting tools.
- **Rationalize applications with measurable criteria** — retirement decisions need cost, risk, and duplication metrics, not just age.
- Adopt **domain-oriented architectures** — align data and application boundaries with business domains to reduce coupling.
- Enforce **clear boundaries** between data domains; ambiguous ownership creates silent integration debt.

### Hidden Mechanics
- Phase C is where **future integration cost is locked in**. Poor boundary decisions here multiply across every downstream phase.
- Data architecture is a **power structure** — who owns what data determines who has authority in the organization.

### Maturity Indicators
- **L1:** Application inventory is a spreadsheet; data models are IT-owned
- **L3:** Data domains have owners and quality SLAs; APIs are contract-first; application rationalization uses cost/risk metrics
- **L5:** Data products are self-serve with automated quality checks; domain boundaries are continuously refined based on usage patterns

---

## Phase D — Technology Architecture

### Objectives
- Develop the Baseline and Target Technology Architecture.
- Map technology components to the application and data architecture.

### Key Inputs
- Outputs of Phases B and C
- Technology standards and constraints (e.g., approved platform list)
- Infrastructure inventory
- **Architecture Repository inputs (if `repoPath` set in `engagement.json`):**
  - Technology Horizon Register (THR): surface entries with ring = Adopt or Trial as candidate SBBs
  - Vendor Landscape Register (VDR): surface active vendors with linked ABBs as SBB mapping context
  - Standards Information Base (STD): surface mandatory standards with `applicableDomains` including Technology as compliance constraints

### Major Steps
1. Select reference models, viewpoints, and tools.
2. Develop Baseline Technology Architecture.
3. Develop Target Technology Architecture.
4. Perform gap analysis.
5. Identify candidate roadmap components.

### Key Questions
- What technology platforms currently support the application landscape?
- What cloud, on-premises, or hybrid strategy applies?
- What technology standards and constraints govern choices?
- What infrastructure changes are needed to support the target state?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Technology Standards Catalogue | Approved technology components and versions |
| Technology Portfolio Catalogue | Current technology inventory |
| Environments and Locations Diagram | Physical/logical deployment topology |
| Platform Decomposition Diagram | Technology stack layers |
| Technology Gap Analysis | Infrastructure and platform gaps |

### Deep Tactics
- **Standardize for leverage** — mandate core platforms only where they create economies of scale; allow flexibility at the edges.
- Create **golden paths** — pre-approved, well-documented technology stacks that teams can adopt without central review.
- Embed **observability and resilience** into technology standards from day one, not as afterthoughts.
- Design for **failure modes** — every critical technology component needs a documented degraded-mode behavior.
- Treat **cloud adoption as an operating model shift**, not just a hosting change — it changes team structures, funding, and decision rights.

### Hidden Mechanics
- Technology architecture is the **leverage layer** — good choices here multiply delivery capacity; bad choices create permanent drag.
- Standards are a **product** with consumers, owners, and adoption metrics — not a static document.

### Maturity Indicators
- **L1:** Technology choices are project-driven; standards exist but are ignored
- **L3:** Golden paths are documented and actively maintained; standards have owners and quarterly reviews
- **L5:** Technology choices are self-service within guardrails; fitness functions validate conformance automatically

---

## Phase E — Opportunities and Solutions

### Objectives
- Generate the initial version of the Architecture Roadmap.
- Determine whether an incremental or big-bang approach is preferred.
- Consolidate gap analyses from Phases B, C, D into work packages.

### Key Inputs
- Gap analyses from Phases B, C, D
- Architecture Vision
- Business transformation readiness results

### Major Steps
1. Determine key corporate change attributes.
2. Determine Business Transformation Readiness Assessment.
3. Identify and group major work packages.
4. Identify Transition Architectures.
5. Create the Architecture Roadmap (draft).

### Key Questions
- What is the organisation's appetite and capacity for change?
- Which gaps are the highest priority to address first?
- Are there logical groupings of change that form coherent work packages?
- What transition states are needed between baseline and target?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Roadmap (draft) | Sequenced plan of work packages to close gaps |
| Transition Architecture(s) | Intermediate states between baseline and target |
| Business Transformation Readiness Assessment | Assessment of change capacity |
| Implementation Factor Assessment | Risks and constraints on implementation |
| Work Package descriptions | Discrete units of architecture implementation work |

### Deep Tactics
- **Package work as value increments** — every work package must deliver measurable business value, not just close a technical gap.
- Prioritize by **impact × feasibility** — high-impact, low-effort quick wins build momentum and credibility.
- Design **transition architectures** deliberately — the path matters more than the ideal end state.
- **Expose trade-offs explicitly** — when sequencing work, state what is deferred and the risk of deferral.
- Align work packages to **funding cycles and capacity windows** — architecture that ignores budget reality is fantasy.

### Hidden Mechanics
- Phase E is where **architecture becomes an investment portfolio**. The quality of packaging and sequencing determines whether anything gets funded.
- Transition architectures are **strategic instruments**, not temporary compromises — they define how the enterprise survives change.

### Maturity Indicators
- **L1:** Roadmap is a wish-list of projects; no clear sequencing logic
- **L3:** Work packages are sized for value delivery; transition architectures are designed; quick wins are identified
- **L5:** Roadmap is treated as an investment portfolio with economic tracking; transition states are continuously refined

---

## Phase F — Migration Planning

### Objectives
- Finalise the Architecture Roadmap and Implementation and Migration Plan.
- Prioritise projects and ensure business value is delivered.

### Key Inputs
- Architecture Roadmap (draft from Phase E)
- Capability Assessment
- Communications Plan

### Major Steps
1. Confirm management framework interactions.
2. Assign business value to each work package.
3. Estimate resource requirements, project timings, and availability.
4. Prioritise migration projects.
5. Generate the Implementation and Migration Plan.

### Key Questions
- What is the sequencing logic and dependency chain?
- How are benefits realised over time?
- How will the migration plan be governed and tracked?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Implementation and Migration Plan | Fully detailed, costed, and sequenced roadmap |
| Prioritised Project List | Ranked list of implementation projects |
| Benefits Realisation Plan | How and when benefits will be measured |

### Deep Tactics
- **Optimize for value delivery** — sequence migration so that business benefits arrive early and compound over time.
- Quantify **risk exposure** per migration wave — know what breaks if a wave fails.
- Align to **funding cycles** — architecture that cannot fit into annual budget processes rarely gets executed.
- Define **exit criteria for legacy** — without clear retirement targets, old systems live forever.
- Maintain **flexibility** — build rollback paths and off-ramps into the plan; no migration survives first contact with reality unchanged.

### Hidden Mechanics
- Phase F is the **economic negotiation** — this is where architecture must speak the language of finance (cost, risk, return, TCO).
- The migration plan is a **contract between architecture and delivery** — it sets expectations that both sides must meet.

### Maturity Indicators
- **L1:** Migration plan is a Gantt chart with no economic justification
- **L3:** Benefits realization is tracked; risk exposure is quantified per wave; legacy retirement has exit criteria
- **L5:** Migration plan is continuously updated based on delivery feedback; economic tracking is automated

---

## Phase G — Implementation Governance

### Objectives
- Ensure conformance of implemented solutions with the Target Architecture.
- Perform architecture oversight of implementation projects.

### Key Inputs
- Implementation and Migration Plan
- Architecture Definition Documents from previous phases
- Architecture Contract

### Major Steps
1. Confirm scope and priorities with implementation teams.
2. Identify deployment resources and skills.
3. Guide development of deployment plans.
4. Perform architecture reviews of deliverables.
5. Update the Architecture Repository with as-built information.
6. Issue Architecture Compliance Certificates.

### Key Questions
- Are implementation projects conforming to the agreed architecture?
- What deviations have been requested and are they justified?
- What lessons are being learned for future ADM cycles?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Contract | Formal agreement between architecture and implementation teams |
| Compliance Assessment | Formal review of implementation against architecture |
| Architecture Compliance Certificate | Sign-off artefact for conformant deliverables |
| Updated Architecture Repository | As-built views and lessons learned |

### Deep Tactics
- Provide **embedded guidance**, not remote review — architects should sit with delivery teams, not gatekeep from a distance.
- Use **automated checks** in CI/CD to validate conformance — reduce governance latency and increase consistency.
- Focus governance effort on **high-risk, irreversible decisions** — don't review every line of code.
- **Track deviations explicitly** — every deviation should be accepted (with risk sign-off) or remediated, not just documented.
- **Measure governance by outcomes** — decision speed, delivery quality, and alignment, not checklist coverage.

### Hidden Mechanics
- Phase G is where **architecture intent meets delivery reality**. Without tight feedback loops, implementation drift is inevitable.
- Governance that is not tied to **funding or deployment consequences** is performative — it produces evidence of compliance without ensuring alignment.

### Maturity Indicators
- **L1:** Governance is checklist-based and centralized; deviations are documented but rarely remediated
- **L3:** Governance is selective and outcome-oriented; automated checks exist for core standards; deviations require explicit acceptance
- **L5:** Governance is largely automated; architects are embedded partners; metrics tie governance to delivery outcomes

---

## Phase H — Architecture Change Management

### Objectives
- Ensure that the architecture achieves its original target business value.
- Manage changes to the architecture in a controlled way.
- Trigger a new ADM cycle when significant change is required.

### Key Inputs
- Architecture Repository
- Architecture Contracts
- Change requests (technology changes, business events)

### Major Steps
1. Establish a value realization process.
2. Deploy monitoring tools.
3. Manage risks.
4. Assess change requests.
5. Determine whether changes require a new ADM cycle.

### Key Questions
- Is the architecture delivering the expected business value?
- What change requests have been raised and how significant are they?
- Do any changes require a full or partial ADM cycle re-run?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Updates | Revisions to architecture documents in the Repository |
| Change Request Log | Tracked register of all change requests |
| Architecture Compliance Assessments (updated) | Ongoing conformance tracking |

### Deep Tactics
- Treat architecture as a **living system** — update target states continuously, not annually.
- Monitor **leading indicators** (decision latency, technical debt velocity, pattern reuse rate) to trigger mini-ADM cycles before crises emerge.
- Run **mini-ADM cycles** for incremental changes — don't force every change through a full waterfall.
- **Retire obsolete architectures explicitly** — when a target is no longer relevant, kill it rather than letting it linger.
- Feed **implementation learnings back** into principles, standards, and reference architectures.

### Hidden Mechanics
- Phase H is the **adaptation loop** — the mechanism that prevents architecture from becoming static and irrelevant.
- Without Phase H discipline, the enterprise drifts into the **Static Target Architecture Illusion** — a fantasy future state that nobody believes.

### Maturity Indicators
- **L1:** Architecture is updated only during major projects; no systematic change management
- **L3:** Mini-ADM cycles are used for incremental change; leading indicators are tracked; obsolete targets are retired
- **L5:** Architecture is continuously adaptive; feedback loops are automated; the system optimizes for learning

---

## Requirements Management — The Central Hub

Requirements Management is not a phase but a continuous process that sits at the centre of the ADM wheel. It ensures that requirements identified in any phase are captured, stored, and fed into the relevant phases.

### Key Activities
- Capture emerging requirements as they arise in any phase.
- Assess the impact of requirements on current and target architectures.
- Prioritise requirements based on business value and strategic alignment.
- Maintain a Requirements Repository linked to the Architecture Repository.

### Artefacts
| Artefact | Description |
|---|---|
| Requirements Impact Assessment | Analysis of how a requirement affects the architecture |
| Architecture Requirements Specification | Detailed requirements for architecture components |
| Requirements Traceability Matrix | Linkage of requirements to architecture decisions and work packages |

### Deep Tactics
- Capture requirements **as they emerge** in any phase — don't wait for a formal requirements phase.
- Assess **impact before priority** — a high-priority requirement with low architectural impact should not block design.
- Link every requirement to **at least one architecture decision or work package** — orphan requirements create hidden gaps.
- Maintain a **living Requirements Repository** — update it continuously, not just at phase boundaries.
- Use requirements to **test the architecture** — if a requirement cannot be traced to a component, the architecture is incomplete.

### Hidden Mechanics
- Requirements Management is the **central nervous system** of the ADM — it coordinates signals across all phases.
- Poor requirement traceability is the **root cause of scope creep** — untraced requirements reappear as "surprises" in implementation.

### Maturity Indicators
- **L1:** Requirements are captured in documents and updated manually; traceability is weak
- **L3:** Requirements repository is linked to architecture repository; impact assessments are standard practice
- **L5:** Requirements flow is automated; traceability is validated by fitness functions; impact is predicted before approval
