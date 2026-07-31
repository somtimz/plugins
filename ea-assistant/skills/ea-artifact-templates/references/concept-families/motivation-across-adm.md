# Motivation Concepts Across the ADM Lifecycle

How motivation concepts (Vision, Mission, Business Context, Drivers, Goals, Objectives, Strategies, Issues, Problems, Opportunities, Metrics) flow through the ADM. Extracted from `ea-concepts.md` so the lifecycle view is available without loading the full concepts index.

---

## EA's Role — Interpret and Operationalize, Not Create

TOGAF does not assume EA creates mission, vision, or strategy. These come from corporate leadership. EA's role is to:

- **Receive** them as inputs
- **Interpret** what they mean for architecture scope and direction
- **Operationalize** them into drivers, goals, objectives, issues, and problems that architecture can act on
- **Trace** them through every subsequent phase so all architecture decisions remain anchored to strategic intent

This is the fundamental distinction between strategic planning (which owns mission/vision/strategy) and enterprise architecture (which translates them into architecture-ready intent).

---

## Conceptual Mental Model

| Layer | Answers | Concepts |
|---|---|---|
| **WHY** | Why does the enterprise exist and where is it going? | Mission, Vision |
| **CONTEXT** | What is the environment telling us? | Business Context (CTX) |
| **WHAT** | What does it want to achieve? | Goals, Objectives |
| **HOW** | How does it plan to achieve it? | Strategies |
| **VALUE MODEL** | How does it create, deliver, and capture value? | Business Model Canvas (BMC) |
| **WHAT BLOCKS** | What is in the way? | Issues, Problems, Risks |
| **STRUCTURAL RESPONSE** | How does architecture enable the change? | Architecture (B–D) → Plan (E–F) → Governance (G) → Adapt (H) |

---

## Phase-by-Phase Lifecycle

| ADM Phase | What happens to motivation concepts | Key deliverables |
|---|---|---|
| **Preliminary** | Receive and understand existing mission, vision, high-level goals, and enterprise strategies from corporate strategy. Align the architecture capability to them. Embed them in Architecture Principles. EA does not create them here — it absorbs them. | Architecture Principles, Governance Framework |
| **Phase A — Architecture Vision** | Primary translation phase. Structure corporate intent into architecture-ready form: scope and confirm goals and objectives; identify business drivers; capture issues and problems via business scenarios; translate strategies into architecture direction; identify constraints and opportunities. This is where strategy becomes architecture intent. | Architecture Vision, Statement of Architecture Work, Stakeholder Map |
| **Phases B–D — Architecture Definition** | Refine goals into requirements; translate strategies into architectural building blocks; ensure every design choice traces to a goal, objective, or strategy. Issues and problems from Phase A become the gap drivers for baseline-to-target analysis. | Baseline & Target Architectures, Gap Analysis |
| **Phase E — Opportunities & Solutions** | Strategy becomes implementation-oriented. Identify solution approaches; group into work packages; align each work package to a goal, objective, or strategy. Benefits assessment validates that planned solutions address the identified issues and problems. | Solution Concept, Initial Roadmap, Benefits Assessment |
| **Phase F — Migration Planning** | Objectives and strategies meet execution reality. Prioritise initiatives based on goals; resolve constraints and trade-offs; sequence work packages into a deliverable roadmap. | Implementation & Migration Plan, Architecture Roadmap |
| **Phase G — Implementation Governance** | Governance ensures implementation conforms to the architecture that was derived from the motivation framework. Compliance reviews validate that delivered solutions still address the original drivers, goals, and objectives. | Compliance Assessments, Architecture Contracts |
| **Phase H — Change Management** | New problems, issues, or changes to strategy and goals trigger new ADM cycles. Metrics close the feedback loop — they either confirm success or surface new issues and capability gaps that re-enter the motivation framework. | Architecture Updates, Change Requests |

---

## Artifact Distribution

Not every motivation concept gets its own document. They are distributed across artifacts:

| Artifact | Motivation concepts hosted |
|---|---|
| **Architecture Vision** | Mission, Vision, Business Context (CTX), Business Drivers (DRV), Goals (G), Objectives (OBJ), Strategies (STR), Issues (ISS), Problems (PRB), Opportunities (OPP), Metrics (MET), Risks |
| **Architecture Principles** | Derived from Mission, Vision, Business Context, and Strategies — normative rules that operationalize strategic intent |
| **Engagement Charter** | Mission, Vision, Business Context, high-level goals, constraints, scope boundaries — the mandate frame |
| **Statement of Architecture Work** | Scope, constraints, objectives, success criteria — the delivery commitment |
| **Stakeholder Map** | Stakeholder concerns mapped to goals and issues |
| **Business Model Canvas** | Nine blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure |
| **Business Architecture** | Business Context (CTX) narrative, Capabilities (CAP), Value Streams (VS), Business Services (SVC), Business Processes (PROC), Business Rules (BR), Use Cases (UC), Requirements (REQ) |
| **Operating Model** | Execution design derived from Business Architecture and Business Model Canvas: org design, roles/decision rights, controls, processes, workforce, sourcing, enablement, performance management |
| **Requirements Register** | Formalized goals, issues, and needs — the formal bridge from motivation to execution; every REQ traces to a DRV, G, OBJ, ISS, PRB, CAP, VS, UC, Process, OM element, or Metric |
| **Gap Analysis** | Issues and problems expressed as baseline-to-target gaps; capability gaps may surface as Opportunities |
| **Architecture Roadmap** | Goals, objectives, strategies, and business-model choices realized as sequenced work packages; Opportunities (OPP) elaborated into WPs |
