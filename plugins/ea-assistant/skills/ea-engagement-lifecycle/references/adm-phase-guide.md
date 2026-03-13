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
7. Finalise and publish the Architecture Governance framework.

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

---

## Phase D — Technology Architecture

### Objectives
- Develop the Baseline and Target Technology Architecture.
- Map technology components to the application and data architecture.

### Key Inputs
- Outputs of Phases B and C
- Technology standards and constraints (e.g., approved platform list)
- Infrastructure inventory

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
