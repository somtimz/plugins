# TOGAF ADM Phase Inputs and Outputs Reference

Detailed input/output tables for every TOGAF ADM phase. Use this reference to validate deliverable completeness at each phase transition and to trace artefact lineage across the ADM cycle.

---

## Preliminary Phase

### Required Inputs

| Input | Source | Description |
|---|---|---|
| TOGAF and other framework descriptions | The Open Group / industry bodies | Standard reference material describing ADM phases, techniques, and artefacts |
| Board and business strategy | Executive leadership / board papers | High-level strategic direction, priorities, and investment themes |
| Business principles, goals, and drivers | Business leadership / strategy documents | Documented organisational values, measurable goals, and motivating forces |
| Existing governance frameworks | Corporate governance / legal / compliance | Current decision-making structures, policies, and accountability models |
| Existing IT strategy | CIO office / IT leadership | Current direction for technology investment, platforms, and capabilities |
| Existing organisational model for IT | HR / IT leadership | Current structure of IT functions, reporting lines, and operating model |
| Existing EA documentation (if any) | Architecture repository | Prior framework definitions, standards, or partial architecture artefacts |

### Key Activities

1. Determine the organisational scope and boundaries of the EA effort.
2. Identify and engage key stakeholders and establish sponsorship.
3. Confirm or select the architecture framework (e.g., TOGAF) and tailor it to the organisation.
4. Define and establish the Enterprise Architecture team and its operating model.
5. Identify and establish architecture principles.
6. Define the architecture governance framework and decision-making structures.
7. Select and configure the architecture tooling and repository.
8. Assess existing EA maturity and document baseline capabilities.
9. Develop and agree a governance and support strategy for the EA function.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Organisational model for EA | All ADM phases, governance bodies | Defines EA team structure, roles, responsibilities, and interfaces to the wider organisation |
| Tailored architecture framework | All ADM phases | TOGAF (or other framework) adapted with organisation-specific terminology, processes, and artefacts |
| Initial architecture repository | All ADM phases | Seeded repository with reference data, standards catalogue, and any existing architecture artefacts |
| Restatement of business principles, goals, and drivers | Phase A and all subsequent phases | Confirmed and documented set of business context statements that inform all architecture decisions |
| Governance and support strategy | Architecture governance bodies | Describes how architecture work will be governed, reviewed, and enforced across the enterprise |

### Quality Gates

- [ ] Executive sponsorship confirmed and documented
- [ ] Architecture framework tailoring decisions recorded and approved
- [ ] Architecture principles drafted and submitted for governance approval
- [ ] Repository tooling operational with initial content loaded
- [ ] Governance model agreed with relevant stakeholders

---

## Phase A — Architecture Vision

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Architecture reference materials | Architecture repository | Existing standards, patterns, and reference architectures relevant to the engagement |
| Request for Architecture Work | Sponsor / architecture board | Formal trigger document authorising the architecture engagement and defining scope |
| Business principles, goals, and drivers | Preliminary Phase output | Approved organisational context statements |
| Capability assessment | Business / IT leadership | Assessment of current organisational and IT capabilities relative to strategic needs |
| Communications plan | Stakeholder management | Plan for engaging and communicating with stakeholders throughout the cycle |
| Organisational model for EA | Preliminary Phase output | Defines team roles, responsibilities, and operating interfaces |
| Tailored architecture framework | Preliminary Phase output | Organisation-specific adaptation of the chosen architecture framework |
| Populated architecture repository | Preliminary Phase output / previous cycles | Artefacts, standards, and reference material from prior work |

### Key Activities

1. Establish the architecture project and confirm scope, constraints, and assumptions.
2. Identify and analyse stakeholders; develop or refine the stakeholder map.
3. Confirm and document business goals, drivers, and constraints.
4. Assess current capabilities and identify strategic gaps.
5. Develop the Architecture Vision as a high-level description of the target state.
6. Identify key risks and define initial mitigation approaches.
7. Develop the draft Statement of Architecture Work.
8. Obtain approval of the Statement of Architecture Work from the sponsoring organisation.
9. Publish the Architecture Vision to stakeholders.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Approved Statement of Architecture Work | Phases B–H, architecture board | Formally scoped and approved mandate for the architecture engagement |
| Refined business principles, goals, and drivers | Phases B–H | Updated context statements reflecting stakeholder input gathered during Phase A |
| Architecture principles | Phases B–H | Governing statements that guide architecture decisions throughout the engagement |
| Architecture Vision | Phases B–H, stakeholders | High-level description of the target architecture addressing key stakeholder concerns |
| Draft Architecture Definition Document (high-level) | Phases B–D | Skeleton document establishing structure for Business, Data, Application, and Technology chapters |
| Communications plan | Phases B–H | Updated plan for stakeholder engagement and communications throughout the ADM cycle |

### Quality Gates

- [ ] Statement of Architecture Work signed off by sponsor and architecture board
- [ ] Stakeholder map reviewed and accepted by engagement lead
- [ ] Architecture Vision communicates a coherent target state that addresses key concerns
- [ ] Architecture principles reviewed and provisionally approved
- [ ] Scope, constraints, and assumptions documented and agreed

---

## Phase B — Business Architecture

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase A outputs (all) | Phase A | Architecture Vision, Statement of Architecture Work, principles, communications plan |
| Architecture reference materials | Architecture repository | Business architecture patterns, industry reference models, and benchmarks |
| Request for Architecture Work | Sponsor | Original engagement mandate |
| Business principles, goals, and drivers | Phase A output | Refined context statements |
| Capability assessment | Business / IT leadership | Current capability baseline and strategic gap assessment |
| Organisational model for EA | Preliminary Phase output | Team roles and governance interfaces |
| Tailored architecture framework | Preliminary Phase output | Organisation-specific framework adaptation |
| Populated architecture repository | Repository | Prior business architecture artefacts and reference models |
| Business models and process documentation | Business units | Existing process maps, operating models, value chains, and organisational structures |

### Key Activities

1. Select applicable reference models, viewpoints, and tools for business architecture.
2. Develop the baseline business architecture description (as-is).
3. Develop the target business architecture description (to-be).
4. Perform a gap analysis between baseline and target business architectures.
5. Define candidate roadmap components arising from the gap analysis.
6. Resolve stakeholder concerns and conduct architecture review.
7. Finalise the business architecture and obtain formal sign-off.
8. Document the business architecture in the Architecture Definition Document.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Refined Phase A deliverables | Phases C–H | Updated Architecture Vision and Statement of Architecture Work reflecting business architecture findings |
| Draft Architecture Definition Document — Business sections | Phases C–D, Phase E | Documented baseline and target business architecture descriptions |
| Draft Architecture Requirements Specification — Business | Phases C–H | Measurable business requirements that architecture solutions must satisfy |
| Business architecture components of the roadmap | Phase E | Candidate work packages and initiatives identified from the business gap analysis |

### Quality Gates

- [ ] Baseline business architecture reflects current-state evidence (not assumptions)
- [ ] Target business architecture is traceable to Architecture Vision and business drivers
- [ ] Gap analysis is complete and reviewed by business stakeholders
- [ ] Business requirements specification has measurable acceptance criteria
- [ ] Architecture Definition Document business sections reviewed and accepted

---

## Phase C — Information Systems Architecture

### Phase C-Data: Data Architecture

#### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase B outputs (all) | Phase B | Business architecture deliverables and requirements |
| Data principles | Preliminary Phase / Phase A | Governing statements for data ownership, quality, and stewardship |
| Existing data portfolio | IT / Data management | Inventory of current data assets, data stores, and data flows |
| Existing data governance documentation | Data governance function | Current data policies, standards, and stewardship arrangements |
| Architecture repository | Repository | Prior data architecture artefacts and data reference models |

#### Key Activities

1. Select applicable data reference models and viewpoints.
2. Develop the baseline data architecture (logical and physical data models, data flow diagrams).
3. Develop the target data architecture aligned to business requirements.
4. Perform a data architecture gap analysis.
5. Identify data migration and data management implications.
6. Define candidate roadmap components for data architecture.
7. Conduct data architecture review with data stewards and business owners.

#### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Baseline data architecture description | Phase E, Phase G | Documented current-state logical and physical data architecture |
| Target data architecture description | Phase E, Phase G | Documented future-state data architecture aligned to business requirements |
| Data architecture gap analysis | Phase E | Identified gaps between baseline and target data architectures with impact assessment |

---

### Phase C-App: Application Architecture

#### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase B outputs (all) | Phase B | Business architecture deliverables and requirements |
| Application principles | Preliminary Phase / Phase A | Governing statements for application design, integration, and lifecycle |
| Existing application portfolio | IT / Application management | Inventory of current applications, interfaces, and integration patterns |
| Existing application governance documentation | IT governance | Current application standards, lifecycle policies, and vendor arrangements |
| Architecture repository | Repository | Prior application architecture artefacts and reference architectures |

#### Key Activities

1. Select applicable application reference models and viewpoints.
2. Develop the baseline application architecture (application inventory, interaction diagrams).
3. Develop the target application architecture aligned to business and data requirements.
4. Perform an application architecture gap analysis.
5. Identify application rationalisation and consolidation opportunities.
6. Define candidate roadmap components for application architecture.
7. Conduct application architecture review with application owners and IT management.

#### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Baseline application architecture description | Phase E, Phase G | Documented current-state application landscape including interfaces and integrations |
| Target application architecture description | Phase E, Phase G | Documented future-state application architecture aligned to business and data requirements |
| Application architecture gap analysis | Phase E | Identified gaps between baseline and target application architectures with impact assessment |

---

### Phase C — Combined Outputs

| Output | Consumer | Description |
|---|---|---|
| Draft Architecture Definition Document — Data and Application sections | Phase D, Phase E | Consolidated data and application architecture chapters of the Architecture Definition Document |
| Draft Architecture Requirements Specification — IS | Phases D–H | Measurable information systems requirements that architecture solutions must satisfy |
| IS components of the architecture roadmap | Phase E | Combined data and application candidate work packages from gap analyses |

### Phase C — Quality Gates

- [ ] Baseline data architecture validated against actual data asset inventory
- [ ] Baseline application architecture validated against actual application portfolio
- [ ] Target data architecture is traceable to business architecture requirements
- [ ] Target application architecture is traceable to business architecture requirements
- [ ] Data and application gap analyses reviewed and accepted by domain owners
- [ ] Integration points between data and application architectures are consistent
- [ ] Architecture Definition Document data and application sections reviewed and accepted

---

## Phase D — Technology Architecture

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase B and C outputs (all) | Phases B and C | Business, data, and application architecture deliverables and requirements |
| Technology principles | Preliminary Phase / Phase A | Governing statements for technology selection, standards, and lifecycle |
| Technology standards | IT / architecture board | Approved technology standards, preferred vendors, and reference platforms |
| Technology forecast | IT / vendor management | Emerging technology trends and planned platform changes relevant to the architecture horizon |
| Existing technology portfolio | IT / infrastructure management | Inventory of current infrastructure, platforms, and technology components |
| Architecture repository | Repository | Prior technology architecture artefacts and reference architectures |

### Key Activities

1. Select applicable technology reference models and viewpoints.
2. Develop the baseline technology architecture (infrastructure, platforms, deployment views).
3. Develop the target technology architecture aligned to IS and business requirements.
4. Perform a technology architecture gap analysis.
5. Identify technology refresh, rationalisation, and investment implications.
6. Define candidate roadmap components for technology architecture.
7. Conduct technology architecture review with infrastructure and operations teams.
8. Finalise technology architecture and obtain domain sign-off.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Baseline technology architecture description | Phase E, Phase G | Documented current-state infrastructure, platforms, and deployment topology |
| Target technology architecture description | Phase E, Phase G | Documented future-state technology architecture aligned to IS and business requirements |
| Technology architecture gap analysis | Phase E | Identified gaps between baseline and target technology architectures with impact assessment |
| Draft Architecture Definition Document — Technology section | Phase E | Technology architecture chapter of the Architecture Definition Document |
| Draft Architecture Requirements Specification — Technology | Phases E–H | Measurable technology requirements that solutions must satisfy |
| Technology components of the architecture roadmap | Phase E | Candidate technology work packages identified from the gap analysis |

### Quality Gates

- [ ] Baseline technology architecture validated against current infrastructure inventory
- [ ] Target technology architecture is traceable to IS and business architecture requirements
- [ ] Technology gap analysis reviewed and accepted by infrastructure and operations leads
- [ ] Technology standards compliance assessed for target architecture
- [ ] Architecture Definition Document technology section reviewed and accepted

---

## Phase E — Opportunities and Solutions

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase B, C, and D gap analyses | Phases B, C, D | All domain gap analyses (business, data, application, technology) |
| Architecture repository | Repository | Existing solution building blocks, reusable patterns, and reference implementations |
| Architecture Vision | Phase A | High-level target state and strategic intent |
| Draft Architecture Definition Documents (all sections) | Phases B, C, D | Complete draft architecture descriptions across all domains |
| Draft Architecture Requirements Specifications (all domains) | Phases B, C, D | Complete set of measurable architecture requirements |
| Change requests | Architecture governance / projects | Requests for change arising from projects, business change, or external drivers |
| Capability assessment | Business / IT leadership | Current capability assessment used to validate feasibility of proposed solutions |

### Key Activities

1. Determine and confirm key corporate change attributes (risk tolerance, change capacity, timescales).
2. Determine business constraints on implementation.
3. Review and consolidate gap analyses across all architecture domains.
4. Review requirements across all relevant architecture domains.
5. Consolidate and reconcile interoperability requirements.
6. Identify and group work packages that deliver the target architecture.
7. Identify transition architectures that represent intermediate states.
8. Define the architecture roadmap (initial version) showing the sequenced path to the target.
9. Assess and confirm the implementation and migration strategy.
10. Align the roadmap to business priorities and IT delivery capacity.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Refined Architecture Definition Document | Phase F, Phase G | Updated and internally consistent architecture descriptions across all domains |
| Refined Architecture Requirements Specification | Phase F, Phase G | Updated measurable requirements aligned to proposed solutions |
| Architecture roadmap (initial) | Phase F | Sequenced set of work packages showing the path from baseline to target architecture |
| Implementation and migration strategy | Phase F | Strategic approach for sequencing and delivering the transition from baseline to target |
| Transition architectures | Phase F, Phase G | Defined intermediate architecture states that represent viable stepping stones to the target |
| Work package definitions | Phase F | Scoped units of architecture-led change with dependencies and indicative resource requirements |

### Quality Gates

- [ ] All domain gap analyses reconciled and consolidated
- [ ] Work packages are non-overlapping, collectively exhaustive, and traceable to gap analysis findings
- [ ] Transition architectures represent coherent and viable intermediate states
- [ ] Architecture roadmap sequencing reviewed against business priorities and delivery capacity
- [ ] Implementation and migration strategy approved by sponsor and architecture board

---

## Phase F — Migration Planning

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Phase E outputs (all) | Phase E | Architecture roadmap, transition architectures, work packages, implementation strategy |
| Business priorities and constraints | Business leadership | Current and forecast business priorities, budget cycles, and change capacity |
| IT programmes and projects in flight | Programme management office | Existing IT delivery portfolio to assess dependencies and integration points |
| Cost and benefit analysis data | Finance / business case teams | Financial modelling data to support prioritisation and sequencing decisions |
| Capability assessment | Business / IT leadership | Updated assessment of organisational change capacity and delivery capability |

### Key Activities

1. Confirm management framework interactions for implementation and migration planning.
2. Assign a business value to each work package.
3. Estimate resource requirements, project timescales, and availability.
4. Prioritise migration projects through cost/benefit assessment and risk evaluation.
5. Confirm architecture roadmap and update for migration planning decisions.
6. Generate the Implementation and Migration Plan.
7. Complete the Architecture Definition Document and Architecture Requirements Specification.
8. Finalise the transition architectures.
9. Create the architecture contract for each work package.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Implementation and Migration Plan | Phase G, programme management | Detailed plan showing sequenced delivery of work packages with resource and timeline estimates |
| Finalised Architecture Definition Document | Phase G, Phase H | Complete and approved architecture descriptions across all domains |
| Finalised Architecture Requirements Specification | Phase G, Phase H | Complete and approved measurable requirements |
| Updated architecture roadmap | Phase G, Phase H | Roadmap updated to reflect migration planning decisions and confirmed sequencing |
| Updated transition architectures | Phase G | Revised intermediate architecture states aligned to the finalised migration plan |

### Quality Gates

- [ ] All work packages have assigned business value and priority scores
- [ ] Implementation and Migration Plan reviewed by programme management and finance
- [ ] Architecture Definition Document is complete, consistent, and formally approved
- [ ] Architecture Requirements Specification is complete, measurable, and formally approved
- [ ] Transition architectures are consistent with the migration plan sequencing

---

## Phase G — Implementation Governance

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Architecture Definition Document | Phase F | Finalised architecture descriptions across all domains |
| Architecture Requirements Specification | Phase F | Finalised measurable requirements |
| Architecture contract | Phase F | Agreed terms for architecture conformance during implementation |
| Project requests and project initiation documentation | Project management / PMO | Formal project charters and initiation documents for in-scope work packages |
| Capability assessment | Business / IT leadership | Assessment used to confirm project teams have required skills and governance structures |

### Key Activities

1. Confirm the scope and priorities for implementation with the sponsoring organisation.
2. Identify deployment resources and skills required.
3. Guide the development of solutions deployment (architecture oversight).
4. Perform enterprise architecture compliance reviews against the architecture contract.
5. Implement business and IT operations in accordance with the target architecture.
6. Perform post-implementation reviews and close the implementation.
7. Issue an architecture compliance assessment for each solution delivered.
8. Capture change requests arising from implementation activity.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Architecture contracts (signed) | Project teams, governance bodies | Formal agreements between the architecture function and project teams on conformance obligations |
| Compliance assessments | Architecture board, programme management | Documented results of architecture compliance reviews for each solution or work package |
| Change requests | Phase H | Requests for changes to architecture arising from implementation findings or deviations |
| Architecture-compliant solutions | Business / IT operations | Deployed solutions that have been verified against the architecture contract |

### Quality Gates

- [ ] Architecture contracts signed by project sponsors and lead architect
- [ ] At least one compliance review conducted per work package prior to deployment
- [ ] All change requests formally logged and assessed against architecture impact
- [ ] Post-implementation review completed and lessons learned captured
- [ ] Solutions signed off as architecture-compliant before operational handover

---

## Phase H — Architecture Change Management

### Required Inputs

| Input | Source | Description |
|---|---|---|
| Architecture Definition Documents (current cycle) | Phase G | Complete architecture descriptions from the current ADM cycle |
| Architecture Requirements Specification (current cycle) | Phase G | Complete requirements from the current ADM cycle |
| Architecture roadmap | Phase F / Phase G | Current roadmap showing remaining and planned work packages |
| Change requests | Phase G, business change, external drivers | Accumulated change requests arising from implementation, business change, or technology change |
| Monitoring results | Architecture governance / operations | Outputs of ongoing architecture compliance monitoring activities |
| Business priorities and drivers | Business leadership | Current business context that may trigger re-evaluation of the architecture |

### Key Activities

1. Establish value realisation process to measure architecture benefits.
2. Deploy monitoring tools and processes for architecture compliance.
3. Manage risk associated with ongoing change.
4. Provide analysis for architecture change management decisions.
5. Assess change requests for architecture impact and classify (dispensation, minor change, or new ADM cycle).
6. Implement minor changes through an established change control process.
7. Decide when a formal ADM cycle re-initiation is required for significant changes.
8. Activate the process to implement change where required.

### Required Outputs

| Output | Consumer | Description |
|---|---|---|
| Architecture updates | Architecture repository, stakeholders | Revised architecture documents reflecting approved minor changes and corrections |
| Changes to the architecture framework and principles | Preliminary Phase (next cycle) | Updates to governance structures, principles, or the tailored framework based on lessons learned |
| New Request for Architecture Work | Phase A (next cycle) | Formal trigger for a new ADM cycle where significant change is required |
| Statement of Architecture Work (updated or new) | Phase A (next cycle) | Updated or new scoping document for re-initiated architecture work |

### Quality Gates

- [ ] Change requests classified and dispositioned within agreed governance timescales
- [ ] Architecture updates peer-reviewed and approved before repository publication
- [ ] Monitoring results reviewed at defined governance cadence
- [ ] Lessons learned from the current cycle documented and fed into the Preliminary Phase of the next cycle
- [ ] Decision to initiate a new ADM cycle is formally approved and documented where applicable

---

## Artefact Lineage Summary

The table below summarises how key artefacts flow across phases.

| Artefact | Created | Refined | Finalised | Governed |
|---|---|---|---|---|
| Statement of Architecture Work | A | E, F | F | G, H |
| Architecture Vision | A | E | F | G, H |
| Architecture Definition Document | A (skeleton) | B, C, D, E | F | G, H |
| Architecture Requirements Specification | B | C, D, E | F | G, H |
| Architecture Roadmap | E | F | F | G, H |
| Transition Architectures | E | F | F | G |
| Implementation and Migration Plan | F | F | F | G |
| Architecture Contracts | F | — | G | G |
| Compliance Assessments | — | — | G | H |
| Change Requests | G | — | — | H |
