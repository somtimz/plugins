# EA Concepts Reference

## How to Use This Reference

This file is the index for EA concepts that are frequently confused during interviews and artifact creation: **Vision**, **Mission**, **Business Context**, **Business Driver**, **Principle**, **Goal**, **Objective**, **Strategy**, **Plan**, **Risk**, **Issue**, **Problem**, **Opportunity**, **Capability Model**, **Value Stream**, **Business Process**, **Use Case**, **Business Model Canvas**, **Operating Model**, and **Metrics**. When the `ea-interviewer` agent detects concept confusion it cites this file. All commands and skills that capture direction, decisions, or risks should use these definitions — do not redefine them inline.

> 📎 Source: `references/ea-concepts-source.pdf` — *Enterprise Architecture Strategic Context: Terms, Concepts, and Relationship Models*. The definitions, relationships, and model diagrams in this file are grounded in that document.

---

## Motivation Framework

The engagement's strategic context is captured as a complete, linked chain from executive intent to practical execution:

```
Vision ──inspires──► Mission ──contextualizes──► Business Context (CTX)
                                                          │
                                                   informs / evidences
                                                          ▼
                                              Business Drivers (DRV)
                                                          │
                                                       drives
                                                          ▼
Issues (ISS) ──threatens──► Goals (G) ◄──achieves── Strategies (STR)
    │                           │                            │
   causes                 operationalizes          informed by / realised through
    ▼                           ▼                            ▼
Problems (PRB) ──blocks──► Objectives (OBJ)    Business Model Canvas (BMC)
                                │                            │
                             informs              ┌─────────┴─────────┐
                                ▼                  ▼                   ▼
                        Capability Model    Operating Model      Requirements Register
                       (What the org must be able to do)        (traces to ALL layers above)
                                │                                  │
                           exercises                        realised by
                                ▼                                  ▼
                         Value Streams                  Architecture Building Blocks (ABB)
                    (End-to-end value delivery)          (Logical, vendor-neutral components)
                                │                                  │
                            composed of                    implemented by
                                ▼                                  ▼
                         Business Processes                 Solution Building Blocks (SBB)
                                │                            (Concrete products and technologies)
                         enables / consumed by                       │
                                ▼                                    ▼
                          Use Cases                          User Stories (STY)
                    (Actor goals supported)                  (Actor-centred delivery items)
                                │                                    │
                           generates                          broken into
                                ▼                                    ▼
                     Requirements Register                       Tasks
                    (traces to ALL layers above)          (Atomic implementation steps)
```

For per-concept definitions, see the subfile referenced in the table below. For the relationship between business intent and EA enablement, see [`two-layers-of-intent.md`](two-layers-of-intent.md). For how motivation concepts flow through the ADM, see [`concept-families/motivation-across-adm.md`](concept-families/motivation-across-adm.md).

---

## Concept Definitions

Detailed definitions are split by concept family to keep lookups fast and to prevent loading unused definitions. The subfiles are the single source of truth for each concept's **What it IS**, **What it is NOT**, **Common confusions**, **TOGAF placement**, **ArchiMate element**, and **Practitioner Notes**.

| Family | Concepts | Reference |
|---|---|---|
| Motivation | Vision, Mission, Direction, Goal, Objective, Strategy, Plan, Risk, Issue, Problem, Opportunity, Metrics | [motivation-concepts.md](concept-families/motivation-concepts.md) |
| Business Context & Model | Business Context (CTX), Business Driver, Business Model Canvas (BMC) | [business-context-and-model-concepts.md](concept-families/business-context-and-model-concepts.md) |
| Governance & Rules | Principle, Policy, Business Rule, Constraint, Stakeholder Concern / Objection | [governance-concepts.md](concept-families/governance-concepts.md) |
| Business Layer | Capability Model, Operating Model, Value Stream, Business Process, Use Case, Business Scenario | [business-layer-concepts.md](concept-families/business-layer-concepts.md) |
| Architecture Products | Requirement, ABB, SBB, Reference Architecture, User Story, Service, Interface, Application/Technology Component, Capability Increment, Plateau/Transition Architecture, Deliverable, Architecture Partitioning, Enterprise Continuum | [architecture-products-concepts.md](concept-families/architecture-products-concepts.md) |
| Implementation | Work Package, Cost Entry (FIN), Architecture Decision Record, Capability Gap | [implementation-concepts.md](concept-families/implementation-concepts.md) |

---

## Quick Reference Table

The two columns below are the navigation aid. For TOGAF placement and ArchiMate element per concept, load the subfile — that data is canonical there and is not duplicated here.

| Concept | Core Question | One-Line Marker |
|---|---|---|
| **Vision** | *What do we aspire to become?* | Long-term aspirational destination — the North Star; all Drivers and Strategies must align |
| **Mission** | *Why do we exist today?* | Fundamental purpose and scope of activity — bounds which Drivers are relevant |
| **Business Context (CTX-NNN)** | *What is the environment telling us?* | Analysis discipline capturing external/internal conditions (PESTEL, SWOT, competitor, regulatory) — feeds Drivers, Issues, Opportunities, Policies, Constraints |
| **Business Driver** | *Why do we need to change now?* | External or internal force making the engagement necessary — must be evidenced and traceable to at least one Goal |
| **Principle** | *What must always be true?* | Normative rule — applies to every future decision in its domain |
| **Goal** | *Where do we want to be?* | Desired future state — qualitative, no deadline required |
| **Objective** | *How far, and by when?* | Measurable, time-bound result — must have a measure, target, and deadline |
| **Strategy** | *How will we get there?* | Chosen course of action — not an outcome, not a sequence |
| **Plan** | *What will we do, in what order, by when?* | Sequenced execution — who, what, when |
| **Risk** | *What could go wrong?* | Uncertain future event with potential negative effect on objectives |
| **Issue** | *What systemic concern is threatening a goal?* | Broad barrier or pattern of dysfunction — no single fix; threatens a Goal |
| **Problem** | *What specific symptom is blocking an objective?* | Observable, measurable, and fixable — blocks an Objective |
| **Capability Model** | *What must the organisation be able to do?* | Stable, hierarchical map of capabilities (people + process + info + tools) — independent of org structure or current systems |
| **Capability Gap** | *Which capabilities are missing or immature?* | Delta between required and current capability — prevents goals; feeds Gap Analysis |
| **Business Model Canvas (BMC-NNN)** | *How do we create, deliver, and capture value?* | Structured description of the business model — sits between Strategy and Business Architecture/Operating Model; nine blocks map to SVC/VS, CAP, FIN, Stakeholder Map |
| **Operating Model** | *How does the organisation function to deliver value?* | Execution design: how the organisation operates its business to deliver value |
| **Value Stream** | *What end-to-end result does the stakeholder receive?* | End-to-end chain of activities delivering value from trigger to outcome — composed of processes, exercises capabilities |
| **Business Process** | *How is value delivered step by step?* | Structured set of activities with defined actors, inputs, outputs, and decision points — component of a value stream |
| **Use Case** | *What does the actor need to accomplish?* | Discrete goal pursued by a specific actor — consumes processes, generates requirements |
| **Constraint** | *What boundaries must we respect?* | Non-negotiable restriction on implementation choices — certain, sourced, and owned |
| **Metrics** | *How do we know we are succeeding?* | Specific, quantifiable measures — leading (predictive) or lagging (outcome); validate strategies or surface new Issues and Problems |
| **ABB** | *What logical component do we need?* | Reusable, vendor-neutral architecture component at solution-independent level — names the capability to be implemented, not the product |
| **SBB** | *What product or system implements it?* | Concrete realisation of an ABB — specific product, vendor, or build choice; registered in the SBB Register |
| **User Story** | *What does the stakeholder want to be able to do?* | Stakeholder-perspective feature statement (As a… I want… so that…); links a business actor to a deliverable outcome; traced to REQ-NNN and ABB-NNN |
| **Service** | *What behaviour is offered to consumers?* | Externally visible unit of behaviour with a defined contract — what is offered, not how it is built |
| **Interface** | *Where and how do two things connect?* | Defined access point and contract between components or services (API, event, file exchange) |
| **Application / Technology Component** | *What structural element does the work?* | Modular structural unit (deployed application, node, device) — the thing that realises services via interfaces |
| **Capability Increment** | *How much of the capability does this step deliver?* | Discrete, valuable step in a capability's maturity, delivered by work packages and visible at a Plateau |
| **Plateau / Transition Architecture** | *What stable state exists between baseline and target?* | A relatively stable, operable architecture state at a point in time |
| **Deliverable** | *What work product is contractually handed over?* | Formally specified, reviewed, signed-off output of the engagement — contains artifacts |
| **Architecture Partitioning** | *How is the architecture landscape divided?* | Deliberate division of architectures by level, domain, and time so teams can work without collision |
| **Enterprise Continuum** | *How generic or specific is this asset?* | Classification of assets from generic (Foundation) to Organisation-Specific — governs reuse from the Architecture Repository |

---

## Disambiguation

For disambiguation between two concepts, check the **What it is NOT** and **Common confusions** sections in the relevant subfile under `concept-families/`. The single exception: the entry-level test of whether a subject belongs in **Business Architecture** or **EA / TOGAF** (the "Would this still exist without the EA team?" question) lives in [`two-layers-of-intent.md`](two-layers-of-intent.md).

---

## See Also

- [`two-layers-of-intent.md`](two-layers-of-intent.md) — Business Architecture vs EA / TOGAF distinction, naming conventions, quick test, AI example, and cross-layer mapping
- [`concept-families/motivation-across-adm.md`](concept-families/motivation-across-adm.md) — How motivation concepts flow through the ADM (EA's role, mental model, phase-by-phase, artifact distribution)
