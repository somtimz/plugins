---
name: togaf-adm-phases
description: This skill should be used when the user asks about "TOGAF ADM phases", "start a phase", "what happens in Phase A", "Architecture Vision", "Business Architecture", "Technology Architecture", "ADM cycle", "architecture governance", "requirements management", "phase inputs and outputs", "ADM activities", or any question about progressing through the TOGAF 10 Architecture Development Method.
version: 0.1.0
---

# TOGAF 10 Architecture Development Method (ADM)

The ADM is the core process of TOGAF 10 — a repeatable cycle of phases for developing and managing enterprise architectures. Each phase has defined inputs, steps, and outputs. Requirements Management sits at the centre and applies to all phases continuously.

## ADM Phase Map

```
                    ┌─────────────────────┐
                    │    Preliminary       │
                    └──────────┬──────────┘
                               │
              ┌────────────────▼───────────────┐
              │        Requirements             │
              │         Management              │
              └────────────────┬───────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   ┌────▼────┐           ┌─────▼─────┐          ┌────▼────┐
   │  Phase A │           │  Phase B  │          │ Phase C │
   │  Vision  │           │ Business  │          │  Info.  │
   └────┬────┘           └─────┬─────┘          └────┬────┘
        │                      │                      │
   ┌────▼────┐           ┌─────▼─────┐          ┌────▼────┐
   │  Phase H │           │  Phase D  │          │ Phase E │
   │  Change  │           │Technology │          │ Opport. │
   └────┬────┘           └─────┬─────┘          └────┬────┘
        │                      │                      │
   ┌────▼────┐           ┌─────▼─────┐
   │  Phase G │           │  Phase F  │
   │  Impl.  │           │ Migration │
   └─────────┘           └───────────┘
```

## Phase Reference

### Preliminary Phase
- **Purpose**: Prepare the organisation for TOGAF adoption
- **Key activities**: Define architecture capability, establish governance, tailor the ADM, identify stakeholders
- **Inputs**: Board strategy, business principles, existing frameworks
- **Outputs**: Architecture principles, tailored ADM, governance model, architecture repository baseline
- **Key artifacts**: Architecture Principles Catalog, Governance Model

### Phase A — Architecture Vision
- **Purpose**: Define the scope, stakeholders, and high-level vision for the architecture engagement
- **Key activities**: Identify stakeholders and concerns, create Architecture Vision, obtain approval
- **Inputs**: Architecture principles, business strategy, request for architecture work
- **Outputs**: Statement of Architecture Work, Architecture Vision, approved stakeholder map
- **Key artifacts**: Stakeholder Map, Architecture Vision Document, Business Scenario

### Phase B — Business Architecture
- **Purpose**: Develop the baseline and target Business Architecture
- **Key activities**: Develop business capability map, process flows, organisational model, gap analysis
- **Inputs**: Phase A outputs, business principles, business models
- **Outputs**: Baseline and Target Business Architecture, gap analysis, candidate roadmap
- **Key artifacts**: Business Capability Map, Process Flow Diagram, Organisation/Actor Catalog, Business Interaction Matrix

### Phase C — Information Systems Architecture
- **Purpose**: Develop Data and Application Architectures
- **Key activities**: Identify data entities, define application portfolio, map applications to business functions
- **Sub-phases**: Data Architecture, Application Architecture
- **Inputs**: Phase B outputs, data and application principles
- **Outputs**: Data and Application Architectures, gap analyses
- **Key artifacts**: Data Entity Catalog, Application Portfolio Catalog, Application/Function Matrix, Data Flow Diagram

### Phase D — Technology Architecture
- **Purpose**: Define the technology platform supporting data and applications
- **Key activities**: Identify technology components, map to applications, define standards
- **Inputs**: Phase C outputs, technology principles, current technology landscape
- **Outputs**: Technology Architecture, gap analysis, updated roadmap
- **Key artifacts**: Technology Portfolio Catalog, Technology Standards Catalog, System/Technology Matrix

### Phase E — Opportunities and Solutions
- **Purpose**: Identify major implementation projects and work packages
- **Key activities**: Review gap analyses, generate work packages, identify transition architectures
- **Inputs**: Phases B, C, D gap analyses, business requirements
- **Outputs**: Implementation and Migration Strategy, Work Package list, Transition Architecture(s)
- **Key artifacts**: Project Context Diagram, Benefits Diagram, Implementation Factor Assessment

### Phase F — Migration Planning
- **Purpose**: Develop a detailed Implementation and Migration Plan
- **Key activities**: Prioritise projects, estimate costs/benefits, create roadmap, update Architecture Repository
- **Inputs**: Phase E outputs, business priorities, constraints
- **Outputs**: Implementation and Migration Plan, Architecture Roadmap, updated Architecture Repository
- **Key artifacts**: Architecture Roadmap (Gantt), Transition Architecture descriptions, Migration Plan

### Phase G — Implementation Governance
- **Purpose**: Ensure architecture conformance during implementation
- **Key activities**: Oversee projects, handle implementation contracts, resolve issues
- **Inputs**: Architecture Repository, approved Architecture, project requests
- **Outputs**: Architecture Contracts, Compliance Assessments, change requests
- **Key artifacts**: Architecture Contract, Compliance Assessment, Implementation Governance Model

### Phase H — Architecture Change Management
- **Purpose**: Monitor architecture performance and manage change requests
- **Key activities**: Assess change requests, determine impact, initiate new ADM cycle if needed
- **Inputs**: Deployed architecture, change requests, monitoring data
- **Outputs**: Architecture updates, revised requirements, ADM cycle initiation decision
- **Key artifacts**: Architecture Change Request, Change Impact Assessment

### Requirements Management (Central)
- **Purpose**: Continuously identify, store, and manage architecture requirements
- **Key activities**: Receive requirements, prioritise, assign to phases, manage changes
- **Scope**: Active across all phases simultaneously
- **Key artifacts**: Requirements Repository, Requirements Impact Assessment

## ADM Iteration Patterns

TOGAF 10 supports four iteration modes:
1. **Architecture Context** — Preliminary + A, establish governance before each cycle
2. **Architecture Definition** — B through D, develop domain architectures iteratively
3. **Transition Planning** — E and F, plan implementation incrementally
4. **Architecture Governance** — G and H, oversee change continuously

## Using This Plugin for ADM

To start an ADM engagement, use `/togaf:phase [phase-name]` to enter a phase interactively.

To check current progress across all phases, use `/togaf:status`.

For phase-specific inputs and outputs detail, consult:
- **`references/phase-inputs-outputs.md`** — Complete input/output tables for every phase

## TOGAF 10 vs TOGAF 9 Key Differences

- Restructured into **Part I (Introduction & Core), Part II (ADM), Part III (ADM Guidelines & Techniques), Part IV (Architecture Content), Part V (Enterprise Architecture Capability & Governance)**
- Updated **Content Metamodel** with clearer class hierarchy
- Strengthened guidance on **agile integration** and **team-based architecture**
- New emphasis on **Enterprise Architecture as a practice**, not just a process
- Updated **Architecture Repository** structure with improved classification

## Quick Phase Selector

| Goal | Start with |
|------|-----------|
| New EA programme | Preliminary |
| Architecture engagement request | Phase A |
| Define business capabilities | Phase B |
| Map applications to business | Phase C |
| Define technology platform | Phase D |
| Plan implementation projects | Phase E |
| Build a roadmap | Phase F |
| Govern ongoing projects | Phase G |
| Manage architecture change | Phase H |

## Additional Resources

- **`references/phase-inputs-outputs.md`** — Detailed input/output tables per phase
- **`references/adm-tailoring.md`** — Tailoring guides for agile, programme, and capability-based ADM
