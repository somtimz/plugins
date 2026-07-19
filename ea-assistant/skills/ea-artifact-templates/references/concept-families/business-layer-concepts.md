# Business Layer — Concept Definitions



### Capability Model

**What it IS:**
A Capability Model is a stable, hierarchical map of what the organisation must be able to do to achieve its business outcomes — independent of current organisational structure, people, or systems. Capabilities represent bundles of people, processes, information, and tools working together to produce a defined outcome. The Capability Model answers *"What must the organisation be able to do?"*

**A single capability** is an *ability of the organisation to achieve an outcome*, independent of **who** performs it, **how** it is done, or **what** technology is used. It is a noun ("Customer Onboarding"), never a verb-noun process ("Process Order"). Manage individual capabilities with `/ea-capabilities`.

**The value a capability brings** — every capability should state the **business outcome it enables** and the goal/strategy it serves. A capability with no articulated value and no strategic anchor is a candidate for removal: it is either commodity overhead or "capability inflation". Make differentiating capabilities (where the org competes) strong; make commodity capabilities (table stakes) efficient, not gold-plated. Scoring, brainstorming, and interviewing all test for this value statement.

**Components — a capability is realised by** (the *what*, decomposed into the *how/who/with-what*):
- **People / Roles** — who executes
- **Processes** — how the work flows
- **Information / Data** — what is used and produced
- **Applications / Technology** — the enablers
- **Resources / Facilities** — assets it draws on

**Attributes (decision layer)** — meta-properties used to prioritise investment: **strategic importance** (differentiating vs commodity), **maturity**, **cost / investment**, **risk**, **performance**.

**Realization chain:** `Strategy → Capability → Process → Application → Technology`. The capability is the anchor that translates strategy into execution; processes operationalise it; applications and infrastructure enable the processes.

**Structural characteristics:**
- Organised as a hierarchy: Level 1 (domain) → Level 2 (capability) → Level 3 (sub-capability); the map is **box-in-box, not flow-based** (no arrows — that is a value stream)
- Each capability is assigned a **CAP-NNN** ID on creation during Phase B — IDs are sequential across the engagement
- Each capability has a name, brief description, **value / outcome**, and maturity level (Absent / Immature / Developing / Mature)
- Each capability includes a **Supports** field referencing the STR-NNN strategies or G-NNN goals it enables — the explicit strategy→capability traceability link; a capability with no strategic anchor should be flagged for removal or reclassification
- Independent of how the capability is currently delivered — what, not how or who
- Stable across reorganisations; changes only when business outcomes change. **Caveat:** "stable over time" holds at higher abstraction levels — digital-native and AI-driven organisations see faster capability evolution at lower levels.

**Key relationships:**
- **Objectives and Strategies inform** the Capability Model — the capabilities the org must develop are determined by where it is going and how it plans to get there
- **Capability Model shapes** the Operating Model — once you know what you must be able to do, you design how it will be done
- **Capability Gap** = a capability that is absent or immature relative to what the Strategies and Objectives require; capability gaps prevent Goals from being achieved
- Capabilities also relate to **value streams** (which stages they enable), **applications** (which IT supports them), and **data domains** (information ownership) — captured via `/ea-matrix` (capability×value-stream, capability×application, capability×organization)

**Capability Map vs Capability Knowledge Graph:** the **map** is a static, hierarchical *representation* (human-readable, hierarchy only). A **capability knowledge graph** is an *operational model* — capabilities as nodes with explicit typed relationships to processes, applications, data, goals, and value streams, enabling impact and path analysis. EA Assistant manages the **map** (and typed relationships via matrices); a full RDF/ontology knowledge graph is a future option, not built in — its ROI is still unproven in practice.

**What it is NOT:**
- Not an org chart — capabilities are outcome-based, not structure-based
- Not a process model — a capability is what can be done; a process is how it is done
- Not a system inventory — capabilities are business concepts; applications implement them
- Not a **value stream** — a capability is a stable "what"; a value stream is the end-to-end flow that delivers value by exercising capabilities

**Critical challenges (avoid):** *capability inflation / duplication* (no universal boundary for "a capability" — keep the model lean); *false completeness* (a map claims "full enterprise view" but omits informal work, shadow IT, and emergent capabilities — note known gaps); *maps hide dynamics* (no sequencing or causality — pair with value streams for transformation planning).

**TOGAF placement:** Business Architecture (Phase B) — the primary home. Referenced in Gap Analysis and Architecture Vision when summarising what the organisation must be able to do to achieve its Goals.

**Practitioner Notes:**
- **Map capabilities to value streams** — do not model capabilities in isolation. A capability without a value stream trace is unvalidated.
- Identify **differentiating vs commodity capabilities** — optimize investment accordingly.
- **Maturity marker (L1→L5):** L1 = capabilities reflect org chart; L3 = capabilities linked to value streams and KPIs; L5 = capability heatmaps directly drive investment prioritization
- Use business architecture to **challenge org design**, not just reflect it
- **Failure mode watch:** Centralized Bottleneck — if all capability decisions flow through a single authority, the model becomes a bottleneck rather than a tool

---

### Operating Model

**What it IS:**
The Operating Model is the **execution design** of the enterprise: it describes how the organisation will reliably operate its business to deliver value. It answers *"How will the organisation function to deliver value?"*

Where **Business Architecture** defines the stable business blueprint — what the organisation needs to be able to do — the **Operating Model** designs the operating system that makes that blueprint run day after day. The Operating Model is the "how" to the Capability Model's "what".

**Concept Home — Business Architecture vs Operating Model**

| Concept | Primary Home | Why |
|---|---|---|
| Capability Model (`CAP-NNN`) | **Business Architecture** | Stable "what the org must be able to do", independent of structure, process, or technology |
| Value Streams (`VS-NNN`) | **Business Architecture** | End-to-end value delivery chains that exercise capabilities |
| Business Services (`SVC-NNN`) | **Business Architecture** | Named business outcomes consumed by stakeholders; the service *definition* is part of the blueprint |
| Business Information / Measures | **Business Architecture** | What the business needs to know and measure to operate |
| Business Rules (`BR-NNN`) | **Business Architecture** | Decision logic that constrains or directs business behaviour |
| Use Cases (`UC-NNN`) | **Business Architecture** | Actor goals the business must support |
| Organisation Design | **Operating Model** | How operating units, teams, and governance fora are arranged |
| Business Operating Roles & Decision Rights | **Operating Model** | Who does the work, who decides, and who is accountable |
| Business Processes (`PROC-NNN`) | **Operating Model** | Structured activity flows that execute capabilities and value streams |
| Governance, Controls & SLAs | **Operating Model** | How decisions are made, how conformance is verified, and what levels of service are committed |
| Workforce, Locations & Channels | **Operating Model** | People, skills, geography, and delivery channels |
| Sourcing & Partnership Model | **Operating Model** | Make / buy / partner choices and vendor roles |
| Technology / Data Enablement | **Operating Model** (with detail in Phase C/D) | How applications, data, and infrastructure enable the operating design |
| Performance Management | **Operating Model** | KPIs, metrics, review cadence, and continuous improvement |
| Requirements (`REQ-NNN`) | **Both** | Trace from BA intent *and* OM execution design into solution delivery |
| Gaps (`GAP-NNN`) | **Both** | Capability gaps are BA concerns; operating-model gaps are OM concerns |

**Typical components:**
- **Process** — how work flows across the organisation to produce outcomes (mastered in the `PROC-NNN` Business Processes Register)
- **Information** — what data and knowledge is required, where it lives, and how it flows
- **Technology** — the platforms, systems, and tools that enable operations
- **Governance** — how decisions are made, who has authority, and how performance is managed
- **People & Organisation** — operating roles, skills, locations, and structural units
- **Sourcing** — which capabilities and services are built, bought, or partnered

**Key relationships:**
- **Capability Model shapes** the Operating Model — the design of processes, information flows, and technology choices follow from capability requirements
- **Value Streams are executed by** the Operating Model — processes, roles, and controls turn value-stream stages into operational reality
- **Operating Model performance is measured by** Metrics — the operating model is the source of most operational metrics
- Changes to the Operating Model are a primary driver of Business Architecture and Technology Architecture work

**What it is NOT:**
- Not a Capability Model — the Operating Model describes how work happens; the Capability Model describes what the org can do
- Not an org chart — an Operating Model includes process, information, and technology alongside people; org structure is only one input
- Not a system architecture — the Operating Model operates at the business level; the Technology Architecture is its technical expression
- Not a process repository — the `PROC-NNN` register owns process detail; the OM artifact *integrates* process, role, control, and sourcing choices into a coherent execution design

**TOGAF placement:** Business Architecture (Phase B) — particularly the Business Model Canvas and process views. Technology Architecture (Phase D) — the technical dimensions of the Operating Model.

**Practitioner Notes:**
- Keep the Business Architecture artifact focused on the stable blueprint; keep the Operating Model artifact focused on execution design. Mixing them produces a document that is neither a good blueprint nor a good operating design.
- Align ADM phases with **agile increments** (e.g., Vision with PI planning, Opportunities with backlog shaping).
- Treat **cloud adoption as an operating model shift**, not just a hosting change.
- **Maturity marker (L1→L5):** L1 = operating model reflects current state only; L3 = target operating model designed with delivery teams; L5 = operating model co-evolves with architecture and org design
- **Pattern:** Dual Operating System (Run vs Change) — separate stability-optimized and innovation-optimized operating models
- Use the Operating Model to **influence team structures**, not just system structures

---

### Value Stream (VS-NNN)

**What it IS:**
A Value Stream is an end-to-end sequence of activities that delivers a measurable outcome to a stakeholder, from initial trigger to final value realisation. It answers the question: *"What end-to-end result does the stakeholder receive?*" Value Streams exercise capabilities — each step in the stream requires one or more capabilities to be present and mature. They are composed of Business Processes and trace directly to Goals and Strategies.

**Distinguishing markers:**
- Stakeholder-centric — defined from the outside in (what the recipient gets), not from the inside out (what the org does)
- End-to-end — spans organisational boundaries, systems, and departments; no silo stops at a single team boundary
- Trigger-to-outcome — has a clear starting event and a clear value-delivered state
- Composed of Business Processes — a value stream is not a single process; it is a chain of processes
- Exercises Capabilities — every step needs a capability; a step with no covering capability is a capability gap

**What it is NOT:**
- Not a **Business Process** — a process is a structured activity flow; a value stream is the end-to-end chain that contains multiple processes
- Not a **Capability** — a capability is what the org *can* do; a value stream is how value is *delivered* using those capabilities
- Not a **Use Case** — a use case is an actor's discrete goal; a value stream is the organisation's end-to-end delivery chain
- Not a **Strategy** — a strategy is a chosen course of action; a value stream is the operational delivery mechanism

**Common confusions:**
- "Order-to-cash" — this is a **Value Stream** ✓ (end-to-end, stakeholder-centric, spans multiple processes)
- "Process customer invoice" — this is a **Business Process** (a single structured activity, not end-to-end)
- "Customer places an order" — this is a **Use Case** (an actor's discrete goal), not a value stream
- "We will digitise order-to-cash" — this is a **Strategy** (a chosen approach), not a value stream

**TOGAF placement:** Business Architecture (Phase B) — captured in the Value Stream Map. Each VS-NNN links to Goals (G-NNN) and Strategies (STR-NNN) via the Strategic Link column. VS-NNN entries trace to Capabilities (CAP-NNN) through the Capability Coverage column.

**Practitioner Notes:**
- A Value Stream with no linked Goal or Strategy is an **orphan** — flag it. Every value stream should trace to at least one strategic intent.
- Any step in a value stream with no covering capability is a **capability gap** — flag it for Gap Analysis.
- Value streams are the primary validation mechanism for Goals. A Goal without a value stream trace is unvalidated.
- **Maturity marker (L1→L5):** L1 = value streams named but not mapped to processes; L3 = value streams mapped to processes with capability coverage; L5 = value streams continuously measured with cycle-time and defect metrics
- Use value streams to find **process silos** — if a value stream crosses five organisational units and each has a different system, the integration pain is visible

---

### Business Process

**What it IS:**
A Business Process is a structured, repeatable set of activities with defined actors, inputs, outputs, decision points, and business rules that transforms inputs into outputs of value. It answers the question: *"How is value delivered step by step?*" Business Processes are components of Value Streams and exercise Capabilities.

**Distinguishing markers:**
- Structured and repeatable — not ad-hoc; follows a defined sequence
- Has defined actors — who does what at each step
- Has inputs and outputs — what goes in, what comes out
- Has decision points — where the flow branches based on business rules
- Component of a Value Stream — a single process does not deliver end-to-end value alone

**What it is NOT:**
- Not a **Value Stream** — a process is a single structured activity flow; a value stream is the end-to-end chain
- Not a **Capability** — a capability is the organisational ability; a process is how that ability is exercised
- Not a **Use Case** — a use case describes an actor's goal; a process describes the organisation's step-by-step activity
- Not a **Procedure** — a procedure is a low-level instruction ("click here, then there"); a process is a business-level flow

**Common confusions:**
- "Process the loan application" — this is a **Business Process** ✓ (structured, repeatable, has actors and decision points)
- "Customer applies for a loan" — this is a **Use Case** (actor's goal), not a process
- "From application to disbursement" — this is a **Value Stream** (end-to-end), not a single process
- "Click Submit, then verify identity" — this is a **Procedure** (low-level instruction), not a business process

**TOGAF placement:** Business Architecture (Phase B) — captured in Process Flow diagrams and the Business Architecture artifact. Each process links to its parent Value Stream (VS-NNN) and to the Capabilities (CAP-NNN) it exercises.

**Practitioner Notes:**
- A process with no parent Value Stream is an **orphan** — it may be a shadow process or a missed value-stream step. Flag it.
- Processes that duplicate steps across multiple value streams are a **consolidation opportunity**.
- Business rules buried in spreadsheets or tribal knowledge are a **process documentation gap** — they should be explicit decision points.
- **Maturity marker (L1→L5):** L1 = processes named but not documented; L3 = processes documented with actors, inputs, outputs, and decision points; L5 = processes automated with BPMN and measured with real-time metrics
- Use processes to find **actor-boundary violations** — when a single process step requires three different departments, the hand-off cost is visible

---

### Use Case (UC-NNN)

**What it IS:**
A Use Case is a discrete goal pursued by a specific actor (user, system, or external entity) that is supported by one or more Business Processes. It answers the question: *"What does the actor need to accomplish?*" Use Cases consume Business Processes and generate Requirements. They are the primary bridge from the business domain to the requirements domain.

**Distinguishing markers:**
- Actor-centric — defined from the perspective of who wants something
- Discrete and goal-oriented — has a clear start condition and a clear successful outcome
- Consumes Business Processes — a use case may trigger one or more processes
- Generates Requirements — every use case should produce at least one REQ-NNN
- Links to Capabilities — the use case reveals which capabilities the actor needs

**What it is NOT:**
- Not a **Business Process** — a process is the organisation's step-by-step flow; a use case is the actor's goal
- Not a **User Story** — a user story is a lightweight placeholder ("As a X, I want Y so that Z"); a use case is a structured analysis artifact with flows and exceptions
- Not a **Value Stream** — a value stream is end-to-end stakeholder delivery; a use case is a discrete actor goal
- Not a **Requirement** — a requirement is a formalised need ("the system must..."); a use case is the scenario that generates the requirement
- Not an **EA Capability Use Case** — a use case about "how we govern" or "how we standardize solutions" (e.g., "Define governance process for AI projects") belongs in the Governance Framework or Architecture Principles, not the Business Architecture. See **Two Layers of Intent**.

**Common confusions:**
- "Customer places an order" — this is a **Use Case** ✓ (actor goal, discrete, consumes processes)
- "Process customer order" — this is a **Business Process** (the org's flow), not a use case
- "As a customer, I want to place an order so that I can receive products" — this is a **User Story** (lightweight placeholder), not a full use case
- "The system must support order placement" — this is a **Requirement** (formalised need), not a use case

**TOGAF placement:** Business Architecture (Phase B) — captured in the Use Case Catalog. Each UC-NNN links to the Processes it consumes, the Capabilities (CAP-NNN) it exercises, and the Requirements (REQ-NNN) it generates.

**Practitioner Notes:**
- Every use case must generate at least one REQ-NNN requirement. A use case with no requirements is a **modeling gap** — flag it.
- Use cases that span multiple organisational silos reveal **integration pain** — the actor's goal is fragmented across systems.
- Use cases with no linked capability reveal **capability gaps** — the actor's goal cannot be supported.
- **Maturity marker (L1→L5):** L1 = use cases named but not documented; L3 = use cases documented with actors, preconditions, main flow, and exception flows; L5 = use cases traced to automated test scenarios and real user-journey analytics
- Use the Use Case Catalog to validate **Requirements completeness** — if a REQ-NNN cannot be traced to a UC-NNN, it may be an orphaned or implicit requirement
- **Two Layers check:** If the use case subject is "how we govern" or "how we standardize solutions" rather than "what the actor needs," it is an **EA Capability Use Case** — route it to the Governance Framework or Architecture Principles. See **Two Layers of Intent**.

---

### Business Scenario (BS-NNN)

**What it IS:**
A Business Scenario is a **TOGAF Phase A technique** — a narrative that frames an architecture need in business terms a stakeholder recognises, then derives the requirements needed to meet it. It bridges business stakeholders and architects by describing the problem in lived, concrete terms and working systematically to the technical and business requirements that resolve it. Its purpose is to **validate and justify the Architecture Vision** by grounding it in a real story rather than abstract driver/goal tables, and to **generate traceable requirements**. Managed via `/ea-scenarios`; stored as a full artifact in `artifacts/phase-a/` (one per scenario, `BS-NNN`) and indexed in `engagement.json → scenarios[]`.

**The six TOGAF elements** (every scenario captures these):
- **Problem Statement** — what is broken and why it matters, in the stakeholder's language
- **Objectives** — SMART goals the architecture must meet to resolve it
- **Environment** — the internal and external context (and current technology touchpoints)
- **Stakeholders & Concerns** — who is affected and what they care about
- **Actors** — the human and computing actors who act or are acted upon in the flow (distinct from stakeholders)
- **Requirements** — the specific capabilities the architecture must deliver (each registered as a REQ-NNN with `sourceScenario: BS-NNN`)

Plus **Current-State** and **Target-State** narratives and a **Change Delta** — because the value of a scenario is in *the change*: what happens today vs. what will happen in the target. Model the delta the architecture must enable, not the current state in exhaustive detail.

**Key relationships:**
- **Triggered by** Issues (ISS-NNN) and **addresses** Problems (PRB-NNN) — a scenario makes those concrete
- **Generates** Requirements (REQ-NNN) — the scenario is the narrative context that justifies each requirement
- **Justifies / tests** the Architecture Vision — one story that validates the agreed target state
- **Contains** Use Cases (UC-NNN) — a scenario is the broader business narrative; a use case is a discrete actor goal within it

**What it is NOT:**
- Not an **Issue** — an issue is a broad systemic concern; a scenario is a concrete narrative that an issue may trigger
- Not a **Problem** — a problem is a specific fixable symptom; a scenario may address several
- Not a **Requirement** — a scenario *generates* requirements; it is the context, not the formalised need
- Not the **Architecture Vision** — the Vision is the agreed target; a scenario is one story that justifies or tests it
- Not a **Use Case** — a use case is one actor's functional goal; a scenario is a business narrative that may contain several

**TOGAF placement:** Phase A (Architecture Vision) — optional but strongly recommended when stakeholder alignment is needed before Phase B, or when multiple distinct problem domains are in scope (each gets its own scenario). Source: TOGAF 10 Part III, §25.3.3.

**ArchiMate:** expressed through Motivation-aspect elements — `Driver`, `Assessment`, `Goal`, `Requirement` — linked to the `Stakeholders` and `Business Actors`/`Roles` that participate; the change delta maps to baseline vs target `Business Process`/`Application` elements.

**Practitioner Notes:**
- **Focus on the change.** A scenario that exhaustively models the current state but not the delta has missed its purpose — capture only what constrains or enables the target.
- **Use scenarios when tables fail.** When stakeholders can't engage with abstract driver/goal/objective tables, or when requirements are contested, a shared narrative everyone can verify breaks the deadlock.
- Every scenario should **generate at least one REQ-NNN** and **trace to at least one goal** — an ungrounded scenario is a story with no architectural consequence; flag it.
- **Maturity marker (L1→L5):** L1 = scenarios are anecdotes with no requirements; L3 = scenarios capture the six elements and generate traced requirements; L5 = scenarios drive the Vision and are revisited as the target state evolves.

---
