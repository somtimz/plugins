# EA Concepts Reference

## How to Use This Reference

This file is the canonical source for EA concepts that are frequently confused during interviews and artifact creation: **Vision**, **Mission**, **Principle**, **Goal**, **Objective**, **Strategy**, **Plan**, **Risk**, **Issue**, **Problem**, **Capability Model**, **Operating Model**, and **Metrics**. When the `ea-interviewer` agent detects concept confusion it cites this file. All commands and skills that capture direction, decisions, or risks should use these definitions — do not redefine them inline.

> 📎 Source: `references/ea-concepts-source.pdf` — *Enterprise Architecture Strategic Context: Terms, Concepts, and Relationship Models*. The definitions, relationships, and model diagrams in this file are grounded in that document.

---

## Motivation Framework

The engagement's strategic context is captured as a complete, linked chain from executive intent to practical execution:

```
Vision ──inspires──► Mission ──contextualizes──► Business Drivers (DRV)
                                                          │
                                                       drives
                                                          ▼
Issues (ISS) ──threatens──► Goals (G) ◄──achieves── Strategies (STR)
    │                           │
   causes                 operationalizes
    ▼                           ▼
Problems (PRB) ──blocks──► Objectives (OBJ)
                                │
                             informs
                                ▼
                        Capability Model          ◄── Capability Gap (prevents Goals)
                       (What the org does)
                                │
                            shapes
                                ▼
                         Operating Model
                       (How the org functions)
                                │
                           measured by
                                ▼
                      Metrics (Leading & Lagging)
                       /          |          \
                 surfaces    identifies    evaluates
                     ▼            ▼             ▼
                New Issues   New Problems   Cap. Maturity
                                │
                             defines
                                ▼
                     Requirements Register
                    (traces to ALL layers above)
```

Key relationships:
- **Vision** inspires Mission; **Mission** contextualizes Business Drivers
- **Business Drivers** drive Goals; **Issues** threaten Goals; **Strategies** achieve Goals
- **Goals** are operationalized through Objectives; **Problems** block Objectives
- **Objectives and Strategies** inform the Capability Model — what the org must be able to do
- **Capability Model** shapes the Operating Model — how capabilities are organized and delivered
- **Operating Model** performance is measured through Metrics
- **Metrics** close the feedback loop: they validate success or surface new Issues, Problems, and Capability Maturity gaps
- **Capability Gaps** (missing or immature capabilities) prevent Goals from being achieved — they are identified through the Capability Model and feed into the Gap Analysis
- **Requirements Register** is the formal bridge from the strategic layer to execution; every requirement traces back to a Driver, Goal, Objective, Issue, Problem, Capability, Operating Model element, or Metric

---

## Quick Reference Table

| Concept | Core Question | One-Line Marker | TOGAF Artifact Home | ArchiMate Element |
|---|---|---|---|---|
| **Vision** | *What do we aspire to become?* | Long-term aspirational destination — the North Star; all Drivers and Strategies must align | Architecture Vision §1; Stakeholder Map | — |
| **Mission** | *Why do we exist today?* | Fundamental purpose and scope of activity — bounds which Drivers are relevant | Architecture Vision §1; Stakeholder Map | — |
| **Principle** | *What must always be true?* | Normative rule — applies to every future decision in its domain | Architecture Principles Catalogue (Prelim) | Principle (Motivation) |
| **Goal** | *Where do we want to be?* | Desired future state — qualitative, no deadline required | Architecture Vision §3; domain artifacts | Goal (Motivation) |
| **Objective** | *How far, and by when?* | Measurable, time-bound result — must have a measure, target, and deadline | Architecture Vision §4; domain artifacts | Outcome (Motivation) |
| **Strategy** | *How will we get there?* | Chosen course of action — not an outcome, not a sequence | Architecture Vision; domain artifacts | Course of Action (Motivation) |
| **Plan** | *What will we do, in what order, by when?* | Sequenced execution — who, what, when | Architecture Roadmap (Phase E); Migration Plan (Phase F) | Implementation Event sequences (Impl. & Migration) |
| **Risk** | *What could go wrong?* | Uncertain future event with potential negative effect on objectives | Architecture Vision; Statement of Architecture Work; Migration Plan | Risk (Motivation, Strategy layer) |
| **Issue** | *What systemic concern is threatening a goal?* | Broad barrier or pattern of dysfunction — no single fix; threatens a Goal | Architecture Vision §5 (Phase A) | — |
| **Problem** | *What specific symptom is blocking an objective?* | Observable, measurable, and fixable — blocks an Objective | Architecture Vision §6 (Phase A) | — |
| **Capability Model** | *What must the organisation be able to do?* | Stable, hierarchical map of capabilities (people + process + info + tools) — independent of org structure or current systems | Business Architecture (Phase B); Capability Map | Resource (Active Structure) |
| **Capability Gap** | *Which capabilities are missing or immature?* | Delta between required and current capability — prevents goals; feeds Gap Analysis | Gap Analysis (Phase B/C/D) | — |
| **Operating Model** | *How does the organisation function to deliver value?* | Describes how process, information, technology, and governance are organized and coordinated | Business Architecture (Phase B); Technology Architecture (Phase D) | — |
| **Metrics** | *How do we know we are succeeding?* | Specific, quantifiable measures — leading (predictive) or lagging (outcome); validate strategies or surface new Issues and Problems | Architecture Vision §7; domain artifacts | — |

---

## Concept Definitions

---

### Vision

**What it IS:**
A Vision is a forward-looking, aspirational description of what the organisation intends to become or achieve in the long term — typically a 3–5 year horizon. It serves as the "North Star": all Business Drivers, Goals, and Strategies must align with the Vision to ensure cohesive transformation. The Vision answers *"What are we becoming?"* — not what the organisation does today, but what it is striving towards.

**Distinguishing markers:**
- Aspirational and inspirational — not a plan or a set of tasks
- Long-horizon (3–5 years) — not a near-term target
- Describes an end state, not a method
- Provides the alignment test for all strategic choices made during the engagement

**What it is NOT:**
- Not a **Mission** — a Vision describes the future destination; a Mission describes today's purpose
- Not a **Goal** — a Vision is the overarching aspiration; Goals are the specific desired outcomes that contribute to realising it
- Not a **Strategy** — a Vision says *where*; a Strategy says *how*
- Not a **Principle** — a Vision is a directional statement, not a governance rule

**Common confusions:**
- "Become the leading digital insurer in Southeast Asia by 2030" — this is a **Vision** ✓ (aspirational, long-term, end-state)
- "Deliver outstanding customer service" — this could be a **Mission** (present-day purpose) or a **Goal** (desired state), not a Vision unless it describes a multi-year transformation
- "Adopt cloud-first architecture" — this is a **Strategy** (a chosen approach), not a Vision

**TOGAF placement:** Architecture Vision §1 Executive Summary; Stakeholder Map (as organisational context). Captured during Phase A as the strategic frame for the entire engagement. All Business Drivers should be validated against the Vision — Drivers that do not contribute to the Vision should be flagged.

---

### Mission

**What it IS:**
A Mission is a concise statement defining the organisation's fundamental purpose, its core activities, and the primary stakeholders it serves. It answers *"Why do we exist today?"* — not where the organisation is going, but what it is for right now. The Mission provides the boundary for all Business Drivers and Goals: Drivers and Goals that fall outside the Mission may indicate scope creep or a need to update the Mission itself.

**Distinguishing markers:**
- Present-tense, enduring — describes current purpose, not future aspiration
- Names what the organisation does, for whom, and why
- Provides the scope boundary test for Drivers and Goals
- Stable across engagements (unlike Goals and Objectives which are engagement-specific)

**What it is NOT:**
- Not a **Vision** — a Mission describes today's purpose; a Vision describes tomorrow's aspiration
- Not a **Goal** — a Mission is a standing statement of purpose; a Goal is a time-bound desired outcome
- Not a **Principle** — a Mission explains what the organisation is for; a Principle governs how decisions are made
- Not a **Strategy** — a Mission is a declaration of purpose, not a chosen approach

**Common confusions:**
- "We exist to connect people with affordable financial services" — this is a **Mission** ✓ (defines purpose, beneficiaries, and core activity)
- "Become the most trusted financial services provider in the region" — this is a **Vision** (aspirational, future state)
- "We will adopt API-first integration" — this is a **Strategy** (approach), not a Mission

**TOGAF placement:** Architecture Vision §1 Executive Summary; Stakeholder Map. Captured as organisational context in Phase A. Used to validate that Business Drivers are within scope — a Driver that cannot be traced to the Mission is out of scope for this engagement unless the Mission is being updated.

---

### Principle

**What it IS:**
A principle is a normative statement that governs all future architecture decisions. It acts as a decision filter: when choosing between design options, a principle tells you which option to select (or eliminate). Principles are durable — they change rarely and only through a formal governance process.

**Structural parts** (TOGAF standard):
- **Name** — short, memorable label (e.g. "Vendor Neutrality")
- **Statement** — one declarative sentence describing the rule (e.g. "Technology choices must not create dependency on a single vendor")
- **Rationale** — why this principle matters to the organisation
- **Implications** — what this means in practice for architects, developers, and the business
- **Owner** — who is accountable for upholding this principle
- **Status** — Proposed / Approved / Retired

**What it is NOT:**
- Not a **Goal** — a goal describes a desired state; a principle governs how decisions are made to reach any state
- Not a **Strategy** — a strategy selects an approach for a specific engagement or problem; a principle applies universally and indefinitely
- Not a **Requirement** — a requirement states a need ("the system must handle 10,000 concurrent users"); a principle states a rule ("all systems must be designed for scalability")
- Not a **Preference** — principles are binding within their governance scope; preferences are optional

**Common confusions:**
- "We should use cloud" — this is a **Strategy** (a chosen approach), not a principle. A principle would be: "Technology platforms must support elastic scalability" (applies to all technology choices, not just the cloud decision)
- "We want to be data-driven" — this is a **Goal**, not a principle
- "All APIs must use OAuth 2.0" — this is a **Standard** (a specific, enforceable technical rule), not a principle. The underlying principle is: "Security controls must be applied at every integration boundary"

**TOGAF placement:** Architecture Principles Catalogue, created in the Preliminary phase before Phase A begins. Governs Phases A–H.

**ArchiMate:** `Principle` element in the Motivation aspect. Motivates `Goals`, `Requirements`, and `Constraints`.

---

### Goal

**What it IS:**
A goal is a qualitative statement of a desired future state. It describes *where* the organisation wants to be — aspirational and long-term. Goals do not require a specific measure or deadline to be valid; their function is to set direction and establish what "success" looks like.

**Structural parts** (engagement.json `direction.goals[]`):
- **Statement** — one declarative sentence describing the desired state
- **Priority** — High / Medium / Low

**What it is NOT:**
- Not an **Objective** — an objective is the measurable, time-bound version of a goal ("achieve 99.9% uptime by Q3 2026"); a goal is its qualitative parent
- Not a **Strategy** — a strategy says how to pursue a goal, not what the goal is
- Not a **Principle** — a principle governs decisions; a goal defines a destination

**Common confusions:**
- "We want 99.9% uptime" — the number makes this an **Objective**, not a goal. The goal is "Achieve highly reliable platform operations"; the objective is the measurable target
- "Adopt API-first integration" — this is a **Strategy** (a chosen approach), not a goal
- "Comply with GDPR" — this is a **Requirement** (a compliance obligation), not a goal. The related goal might be "Become a trusted custodian of customer data"

**TOGAF placement:** `direction.goals[]` in `engagement.json`; Architecture Vision §3; referenced in domain architecture documents.

**ArchiMate:** `Goal` element in the Motivation aspect. Realised by `Outcomes`, associated with `Requirements`.

---

### Objective

**What it IS:**
An objective is the measurable, time-bound operationalisation of a goal. It answers *how far, and by when?* Every objective must have three parts: a **unit of measure** (what you will count or track), a **target value** (how much), and a **deadline** (by when). Objectives are the direct anchor for Problems — if a problem cannot be linked to an objective, it may be out of scope.

**Structural parts** (Architecture Vision §4 / `direction.objectives[]`):
- **Statement** — one declarative sentence specifying the outcome
- **Measure** — unit of measure (e.g. "unplanned downtime hours per quarter")
- **Target** — target value (e.g. "< 4 hours")
- **Deadline** — date by which the target must be reached
- **Baseline** — current measured value (e.g. "currently 22 hours/quarter")
- **Linked Goal** — G-NNN of the parent goal

**What it is NOT:**
- Not a **Goal** — a goal is the qualitative parent; the objective is the measurable child
- Not a **Strategy** — an objective describes what you will achieve; a strategy describes how
- Not a **KPI** — a KPI is an ongoing performance measure; an objective is a one-time target with a deadline

**Common confusions:**
- "We want to improve customer satisfaction" — this is a **Goal** (no measure or deadline). The objective is: "Increase NPS from 32 to 50 by Q3 2026"
- "Reduce costs" — this is a **Goal**. "Reduce operational cost by 15% by end of FY27" is the **Objective**
- "We want 99.9% uptime" — has a measure and implicit target; add a deadline to make it a complete Objective

**TOGAF placement:** Architecture Vision §4; domain artifacts; `direction.objectives[]` in `engagement.json`.

**ArchiMate:** `Outcome` element in the Motivation aspect. Associated with `Goal` (realisation relationship).

---

### Issue

**What it IS:**
An issue is a broader, systemic concern that threatens the organisation's ability to achieve one or more goals. Issues are management-level problems — patterns of dysfunction, capability gaps, unresolved conflicts, or sustained exposure to a driver that has no single fix. An issue has multiple contributing causes, affects a domain or process broadly, and requires sustained organisational response rather than a technical patch.

**Structural parts** (Architecture Vision §5):
- **Statement** — one sentence naming the systemic concern
- **Area** — organisational, process, or technology domain most affected
- **Threatens Goal(s)** — G-NNN IDs of the goals this issue puts at risk

**What it is NOT:**
- Not a **Problem** — a problem is a specific, observable symptom with a direct fix; an issue is broader and systemic
- Not a **Risk** — a risk is a future, uncertain event; an issue is a present, ongoing concern. When a risk materialises, it becomes an issue
- Not a **Driver** — a driver is an external or internal force; an issue is the organisational consequence of inadequately responding to a driver

**Common confusions:**
- "Our API is returning 500 errors" — this is a **Problem** (specific, observable, fixable)
- "We have poor data culture" — this is an **Issue** (systemic, no single fix)
- "Increasing regulatory pressure" — this is a **Driver** (external force)
- "The integration broke" — this is a **Problem** (specific, fixable). The related issue might be "Our integration architecture lacks resilience and monitoring"

**TOGAF placement:** Architecture Vision §5 (Phase A). Issues captured here feed into Gap Analysis, Risk assessments, and Requirements.

---

### Problem

**What it IS:**
A problem is a specific, observable, and fixable symptom that is actively blocking the achievement of one or more objectives. Problems have a clear cause-and-effect relationship: a root cause produces a visible symptom that degrades performance against a known objective. Because they are specific and measurable, problems can be prioritised, assigned, and resolved directly.

**Structural parts** (Architecture Vision §6):
- **Statement** — one sentence naming the specific problem
- **Observable Symptom** — what can be seen or measured today (ideally a number)
- **Blocks Objective(s)** — OBJ-NNN IDs of the objectives this problem is preventing

**What it is NOT:**
- Not an **Issue** — an issue is broad and systemic; a problem is specific and fixable. Multiple problems can contribute to a single issue
- Not a **Risk** — a risk is uncertain and future; a problem is certain and present
- Not a **Gap** — a gap is the difference between baseline and target state in a specific architecture domain (used in Gap Analysis); a problem is a current operational failure

**Common confusions:**
- "We have poor data quality" — this is an **Issue** (systemic). The problem is: "30% of customer records have duplicate entries, causing order processing errors 4× per week"
- "Our systems are slow" — this is an **Issue**. The problem is: "Mobile checkout page load time averages 8.2 seconds, causing 68% cart abandonment"
- "The vendor may not deliver" — this is a **Risk** (uncertain, future)

**TOGAF placement:** Architecture Vision §6 (Phase A). Problems feed directly into Requirements — each problem should produce one or more architecture requirements.

---

### Strategy

**What it IS:**
A strategy is a chosen course of action or approach that the organisation will take to pursue its goals and objectives. It answers *how* — selecting one path from among alternatives. A strategy does not describe steps or sequences; it names the approach.

**Structural parts** (engagement.json `direction.strategies[]`):
- **Statement** — one declarative sentence naming the approach
- **Supports** — IDs of the goals or objectives this strategy serves
- **Priority** — High / Medium / Low

**What it is NOT:**
- Not a **Plan** — a strategy says "we will take the API-first approach"; a plan says "in Q1 we will build the API gateway, in Q2 we will migrate service X, in Q3 we will retire the legacy integration layer"
- Not a **Goal** — a strategy is an approach to achieve a goal, not the goal itself
- Not a **Principle** — a strategy is chosen for this engagement; a principle applies universally

**Common confusions:**
- "Move to the cloud" — this is a strategy (the chosen approach). "Have 80% of workloads on cloud by Q4 2027" is the **Objective**. "Cloud-first" may be an architecture **Principle** if it's a permanent organisational rule
- "We will improve data quality" — this is a **Goal** (a desired state), not a strategy
- "We will adopt event-driven architecture" — this is a **Strategy** ✓

**TOGAF placement:** `direction.strategies[]` in `engagement.json`; Architecture Vision Direction Summary; Business Architecture (business strategy); Technology Architecture (technology strategy).

**ArchiMate:** `Course of Action` element in the Motivation aspect. Realises `Goals` and `Objectives`.

---

### Plan

**What it IS:**
A plan is a sequenced description of how a strategy will be executed. It specifies who does what, in what order, and by when. Plans operate at the execution level and are time-bound by definition. They translate strategy into coordinated work.

**Distinguishing marker:** a plan has a sequence, resources (or work packages), owners, and dates. A strategy has none of these.

**TOGAF artifact homes:**
- **Architecture Roadmap** (Phase E/F) — the architecture-level plan: work packages, initiatives, and their sequencing across delivery waves
- **Migration Plan** (Phase F) — the detailed plan for migrating from baseline to target state; includes wave planning, dependencies, rollback procedures
- Work packages within a Roadmap are the smallest plan units

**What it is NOT:**
- Not a **Strategy** — a strategy says "adopt API-first"; a plan says "in Wave 1, build the API gateway; in Wave 2, migrate payment services; in Wave 3, decommission legacy ESB"
- Not a **Goal** — a plan is an execution sequence; a goal is a destination
- Not a **Principle** — a plan is temporary and engagement-specific; principles are permanent

**Common confusions:**
- "Our plan is to become cloud-native" — this is a **Goal** (desired future state), not a plan
- "We plan to adopt Kubernetes" — this is a **Strategy** (chosen approach), not a plan. The plan would specify the migration waves, owners, and dates

**ArchiMate:** No single dedicated element; plans are expressed through sequences of `Implementation Event`, `Work Package`, and `Deliverable` elements in the Implementation & Migration aspect.

---

### Risk

**What it IS:**
A risk is an uncertain future event or condition that, if it occurs, will have a negative effect on one or more objectives. Every risk has two dimensions: **likelihood** (probability it will occur) and **impact** (severity of effect if it does). The combination of the two determines risk rating.

**ID scheme:** `RIS-NNN` (e.g., RIS-001, RIS-002). Assigned by `/ea-risks generate` when risks are aggregated into the Risk Register. Source artifacts may use local IDs (e.g., `MIG-R001` in Migration Plan); these are re-mapped to `RIS-NNN` on aggregation.

**Structural parts** (risk register row):
- **RIS-NNN** — canonical risk ID assigned on aggregation
- **Description** — what could happen and why
- **Likelihood** — High / Medium / Low
- **Impact** — High / Medium / Low
- **Rating** — derived: Critical (H×H) / High (H×M, M×H) / Medium (M×M, H×L, L×H) / Low (M×L, L×M, L×L)
- **Mitigation** — action taken to reduce likelihood or impact
- **Contingency** — what to do if the risk materialises despite mitigation
- **Owner** — who is responsible for the mitigation
- **Status** — Open / Monitoring / Accepted / Closed
- **Source** — which artifact the risk was identified in

**What it is NOT:**
- Not a **Constraint** — a constraint is certain and non-negotiable (e.g., "the project must complete by 31 December 2026"); a risk is uncertain and conditional
- Not an **Issue** — an issue has already occurred and is being managed; a risk is future and hypothetical. When a risk materialises, it becomes an issue
- Not an **Assumption** — an assumption is something accepted as true for planning purposes (e.g., "the vendor will deliver on time"); a risk is what happens if the assumption is wrong

**Common confusions:**
- "Budget is limited" — this is a **Constraint** (a certainty), not a risk
- "The key architect may leave" — this is a **Risk** ✓ (uncertain; has likelihood and impact)
- "We assume stakeholder buy-in" — this is an **Assumption**. The associated risk is: "If stakeholder buy-in is not secured, adoption of the target architecture may fail"
- "The integration is broken" — this is an **Issue** (already occurred), not a risk

**TOGAF placement:** Architecture Vision (preliminary risks, §14); Statement of Architecture Work (risk register); Architecture Compliance Assessment (outstanding risks); Migration Plan (risk register per wave, §4). The consolidated **Risk Register** artifact aggregates all of the above into a single cross-cutting view — use `/ea-risks` to generate it. Risk likelihood and impact ratings also appear in the A3 Decision Log `Risk` column.

**ArchiMate:** `Risk` element in the Motivation aspect (Strategy layer, introduced in ArchiMate 3.0). Associated with `Goal` and `Outcome` via influence relationships.

---

### Stakeholder Concern / Objection

**What it IS:**
A stakeholder concern or objection is a named challenge, question, or objection raised by a stakeholder or surfaced during a formal review (grill-me session, ARB review, executive challenge session). Unlike a Risk (which is an uncertain future event), a concern is a **present-tense challenge** to the architecture that requires either a documented response or a corrective action.

**ID scheme:** `CON-NNN` (e.g., CON-001). Assigned sequentially across the engagement; scoped to the artifact where the concern was raised. Aggregated by `/ea-concerns` into a cross-artifact Concerns Register.

**Structural parts** (Appendix A4 row):
- **ID** — CON-NNN
- **Concern** — the objection or question verbatim where possible
- **Raised By** — stakeholder name/role, or grill-me skill used
- **Category** — Scope / Goal / Approach / Feasibility / Risk / Stakeholder / Other
- **Status** — Addressed / Partially Addressed / Requires Attention
- **Response** — where in the artifact (or another) the concern is answered; blank if unresolved
- **Action / Owner** — what needs to happen and who is responsible (Requires Attention only)

**Distinction from Risk:** A concern becomes a Risk when it has a probability and a potential future impact on an objective. A concern that is "Requires Attention" and category "Risk" should be escalated to the Risk Register as a RIS-NNN entry.

**TOGAF placement:** Appendix A4 of every primary artifact. Aggregated via `/ea-concerns` into a cross-engagement Concerns Register.

---

### Capability Model

**What it IS:**
A Capability Model is a stable, hierarchical map of what the organisation must be able to do to achieve its business outcomes — independent of current organisational structure, people, or systems. Capabilities represent bundles of people, processes, information, and tools working together to produce a defined outcome. The Capability Model answers *"What must the organisation be able to do?"*

**Structural characteristics:**
- Organised as a hierarchy: Level 1 (domain) → Level 2 (capability) → Level 3 (sub-capability)
- Each capability has a name, brief description, and maturity level (Absent / Immature / Developing / Mature)
- Independent of how the capability is currently delivered — what, not how or who
- Stable across reorganisations; changes only when business outcomes change

**Key relationships:**
- **Objectives and Strategies inform** the Capability Model — the capabilities the org must develop are determined by where it is going and how it plans to get there
- **Capability Model shapes** the Operating Model — once you know what you must be able to do, you design how it will be done
- **Capability Gap** = a capability that is absent or immature relative to what the Strategies and Objectives require; capability gaps prevent Goals from being achieved

**What it is NOT:**
- Not an org chart — capabilities are outcome-based, not structure-based
- Not a process model — a capability is what can be done; a process is how it is done
- Not a system inventory — capabilities are business concepts; applications implement them

**TOGAF placement:** Business Architecture (Phase B) — the primary home. Referenced in Gap Analysis and Architecture Vision when summarising what the organisation must be able to do to achieve its Goals.

---

### Operating Model

**What it IS:**
The Operating Model is a high-level description of how the organisation functions in order to deliver value. It describes how process, information, technology, and governance are organised and coordinated — the "how" to the Capability Model's "what". The Operating Model answers *"How does the organisation function to deliver value?"*

**Typical components:**
- **Process** — how work flows across the organisation to produce outcomes
- **Information** — what data and knowledge is required, where it lives, and how it flows
- **Technology** — the platforms, systems, and tools that enable operations
- **Governance** — how decisions are made, who has authority, and how performance is managed

**Key relationships:**
- **Capability Model shapes** the Operating Model — the design of processes, information flows, and technology choices follow from capability requirements
- **Operating Model performance is measured by** Metrics — the operating model is the source of most operational metrics
- Changes to the Operating Model are the primary driver of Business Architecture and Technology Architecture work

**What it is NOT:**
- Not a Capability Model — the Operating Model describes how work happens; the Capability Model describes what the org can do
- Not an org chart — an Operating Model includes process, information, and technology alongside people
- Not a system architecture — the Operating Model operates at the business level; the Technology Architecture is its technical expression

**TOGAF placement:** Business Architecture (Phase B) — particularly the Business Model Canvas and process views. Technology Architecture (Phase D) — the technical dimensions of the Operating Model.

---

### Metrics

**What it IS:**
Metrics are specific, quantifiable measures used to track progress, performance, and outcomes. They provide evidence as to whether Strategies are working and whether Objectives and Goals are being achieved. Metrics answer *"How do we know we are succeeding?"*

**Leading vs Lagging:**
- **Leading metrics** — predictive; indicate whether future performance is likely to improve or worsen (e.g. number of teams trained on new process before go-live)
- **Lagging metrics** — outcome-based; indicate whether desired results have already been achieved (e.g. NPS score after three months of operation)
- A robust measurement framework uses both: leading metrics to act early, lagging metrics to validate success

**Feedback loop role:**
Metrics close the loop between intention and evidence:
- If performance is on target → metrics **validate** the Strategy; Goals and Objectives are being achieved
- If performance is below threshold → metrics **surface new Problems** (observable symptoms) or **reveal deeper Issues** (systemic conditions)
- Metrics also **evaluate Capability Maturity** — when a capability is not performing, metrics identify which ones need investment

**Structural parts** (Architecture Vision §7 / Metrics Register):
- **ID** — MET-NNN
- **Description** — what is being measured
- **Type** — Leading / Lagging
- **Unit** — how it is measured
- **Baseline** — current value
- **Target** — desired value
- **Deadline** — when the target must be reached
- **Linked Objective(s)** — OBJ-NNN this metric tracks

**What it is NOT:**
- Not an Objective — an Objective defines the target; a Metric measures whether the target is being reached
- Not a KPI (necessarily) — all KPIs are metrics, but not all metrics are KPIs; KPIs are the most strategically significant metrics
- Not a requirement — a requirement specifies what must be done; a metric measures whether it has been done successfully

**TOGAF placement:** Architecture Vision §7 Strategic Direction Summary; referenced in Phase G (Implementation Governance) for compliance tracking; Phase H (Architecture Change Management) for performance feedback.

---

### Architecture Decision Record

**What it IS:**
An Architecture Decision Record (ADR) is a standalone document that captures the full context, options analysis, rationale, and consequences of a significant architecture decision. An ADR is written when a decision is hard to reverse, involves meaningful trade-offs, or requires documented rationale so that future architects understand why things are the way they are.

**ID scheme:** `ADR-NNN` (e.g., ADR-001, ADR-023). Assigned sequentially per engagement. Managed by `/ea-adrs`.

**ADR lifecycle:**
```
Candidate → In Progress → Completed
                                └──→ Superseded (by ADR-NNN)
          └──→ Deprecated (any time, with reason)
```
- **Candidate**: Decision identified; options analysis not yet started
- **In Progress**: Options analysis underway; decision not yet made
- **Completed**: Decision made and fully documented
- **Superseded**: Replaced by a newer ADR; `supersededBy: ADR-NNN` recorded
- **Deprecated**: No longer applicable; deprecation reason recorded

**When to create an ADR (not just an A3 Decision Log entry):**
- Technology or vendor selection (cloud platform, database engine, integration middleware)
- Architecture pattern or style choice (microservices, event-driven, CQRS, layered)
- Make-vs-buy or build-vs-configure decisions
- Data governance approach (ownership, sharing, sovereignty model)
- Security or compliance architecture approach
- Significant API or integration design choice
- Any decision that is hard to reverse or whose rationale may be questioned later

**ADR vs. A3 Decision Log:**
- The **A3 Decision Log** (within an artifact's appendix) tracks governance state — who decided what, at what authority level, and whether it has been verified. It is lightweight and lives inside the artifact.
- An **ADR** documents the full decision context: what situation triggered it, what options were considered, why one was chosen, and what the consequences are. It is a standalone artifact.
- They complement each other: log a high-level entry in A3; create an ADR for the full documentation. Link them via the ADR-NNN ID in the A3 `Notes` column.

**Structural parts** (architecture-decision-record.md):
- **§1 Status** — lifecycle history table (date/status/changed-by/note)
- **§2 Context** — situation that forces the decision; linked DRV/G-NNN; triggering artifact
- **§3 Decision Drivers** — evaluation criteria (must-have / should / nice-to-have)
- **§4 Options Considered** — at least two options with pros/cons and driver assessment
- **§5 Decision** — unambiguous statement; chosen option; governance reference
- **§6 Rationale** — why the chosen option was selected; accepted trade-offs
- **§7 Consequences** — positive, negative, risks introduced (RIS-NNN link), new decisions required
- **§8 Related Architecture Decisions** — ADR-to-ADR relationships
- **§9 Affected Artifacts** — artifacts materially affected by this decision

**TOGAF placement:** ADR is not a native TOGAF artifact, but maps closely to the Architecture Decision concept in TOGAF's Architecture Repository. ADRs are referenced via the A3 Decision Log in Architecture Vision, domain architecture artifacts, and the ADR Register.

**Commands:** Use `/ea-adrs` to manage ADRs, track the register, and surface ADR summaries. Use `/ea-adrs new` to create a new ADR. Use `/ea-adrs status` for a portfolio view.

---

### Capability Gap

**What it IS:**
A Capability Gap is a delta between the capabilities the organisation currently has and the capabilities it needs to achieve its Goals and Objectives. Capability Gaps are identified by comparing the Capability Model against the requirements of the Strategies and Objectives. A gap may be a **missing capability** (entirely absent) or an **immature capability** (present but not yet fit-for-purpose).

**Key relationships:**
- Capability Gaps **prevent Goals** from being achieved — if a required capability is absent or immature, the associated Goal cannot be reached
- Identified Capability Gaps **trigger work packages** in the Architecture Roadmap (Phase E)
- Capability Gaps are the primary output of the **Gap Analysis** artifact

**TOGAF placement:** Gap Analysis (Phases B, C, D) — one gap register per domain. Feeds into Architecture Roadmap work package definitions (Phase E).

---

## Disambiguation Checklist

Apply these tests in order. The first test that matches identifies the concept:

1. **Does it contain a deadline or a measurable target?** → likely an **Objective**, not a Goal
2. **Does it describe how to achieve something (an approach or choice), rather than what to achieve?** → likely a **Strategy**, not a Goal or Plan
3. **Does it include a sequence, phases, waves, or work packages with dates?** → likely a **Plan** (Roadmap or Migration Plan), not a Strategy
4. **Does it apply universally to all future decisions in its domain, not just this engagement?** → likely a **Principle**, not a Strategy or Goal
5. **Is it uncertain — could it either happen or not happen?** → likely a **Risk**, not a Constraint
6. **Is it a current, ongoing concern — already affecting the organisation?** → it is an **Issue** (if broad and systemic) or a **Problem** (if specific and fixable), not a Risk
7. **Is it specific, observable, and directly fixable — does it block a particular objective?** → it is a **Problem**, not an Issue
8. **Is it broad, systemic, and without a single fix — does it threaten a goal?** → it is an **Issue**, not a Problem
9. **Is it non-negotiable — it will definitely apply regardless of decisions?** → it is a **Constraint**, not a Risk
10. **Does it describe a desired future state without specifying how to get there?** → likely a **Goal**, not a Strategy
11. **Is it a binding rule that governs architecture decisions — not a description of what the organisation wants or how it will get there?** → it is a **Principle**
12. **Does it require a Rationale, Implications, and Owner to be complete?** → it is a **Principle** (TOGAF standard structure)

---

## Common Confusions — Quick Reference

| What someone said | What they probably meant | Why |
|---|---|---|
| "Our principle is to use cloud-first" | **Strategy** (or Principle if permanent org rule) | States a technology approach, not a universal decision rule — unless it is a permanent board-approved policy |
| "Our goal is to migrate to Azure" | **Strategy** | Describes an approach, not a destination state |
| "We want 99.9% uptime" | **Objective** | Has an implicit measurable target; needs a deadline to be complete |
| "We plan to adopt microservices" | **Strategy** | No sequence, phases, or dates — just a chosen approach |
| "Budget overrun is a problem" | **Issue** (if ongoing) or **Risk** (if future) | Use "issue" if it has occurred; "risk" if it might occur |
| "We must finish by December" | **Constraint** | Certain, non-negotiable — not a risk |
| "The system must handle 10,000 concurrent users" | **Requirement** | Specific, testable, scoped to this system — not a principle |
| "We should document all APIs" | **Standard** or **Principle** | A standard if prescriptive and auditable; a principle if it's a governance rule ("All integration surfaces must be documented and versioned") |

---

## TOGAF and ArchiMate Alignment Summary

| Concept | TOGAF Artefact Home | ADM Phase First Used | ArchiMate Aspect | ArchiMate Element |
|---|---|---|---|---|
| Vision | Architecture Vision §1; Stakeholder Map | A | Motivation | — |
| Mission | Architecture Vision §1; Stakeholder Map | A | Motivation | — |
| Principle | Architecture Principles Catalogue | Preliminary | Motivation | Principle |
| Goal | Architecture Vision §3; Domain Artifacts | A | Motivation | Goal |
| Objective | Architecture Vision §4; Domain Artifacts | A | Motivation | Outcome |
| Strategy | Architecture Vision; Domain Artifacts | A | Motivation | Course of Action |
| Plan | Architecture Roadmap; Migration Plan | E / F | Implementation & Migration | Work Package, Implementation Event |
| Risk | Architecture Vision; Statement of Architecture Work; Migration Plan | A | Motivation (Strategy layer) | Risk |
| Constraint | Architecture Vision; Principles; Requirements Register | Preliminary / A | Motivation | Constraint |
| Requirement | Requirements Register; Traceability Matrix | Requirements | Motivation | Requirement |
| Issue | Architecture Vision §5; Gap Analysis | A | — | — |
| Problem | Architecture Vision §6; Requirements Register (Motivation field) | A | — | — |
| Capability Model | Business Architecture; Capability Map | B | Business | Resource (Active Structure) |
| Capability Gap | Gap Analysis (B/C/D); Architecture Roadmap (E) | B | Business | — |
| Operating Model | Business Architecture; Technology Architecture | B / D | Business | — |
| Metrics | Architecture Vision §7; Phase G/H governance | A / G / H | Motivation | — |
| Architecture Decision Record | ADR Register; individual ADR-NNN files; cross-referenced in artifact `## Related Architecture Decisions` sections | Any | — | — |
