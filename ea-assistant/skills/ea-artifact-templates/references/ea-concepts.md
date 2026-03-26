# EA Concepts Reference

## How to Use This Reference

This file is the canonical source for eight EA concepts that are frequently confused during interviews and artifact creation: **Principle**, **Goal**, **Objective**, **Strategy**, **Plan**, **Risk**, **Issue**, and **Problem**. When the `ea-interviewer` agent detects concept confusion it cites this file. All commands and skills that capture direction, decisions, or risks should use these definitions — do not redefine them inline.

---

## Quick Reference Table

| Concept | Core Question | One-Line Marker | TOGAF Artifact Home | ArchiMate Element |
|---|---|---|---|---|
| **Principle** | *What must always be true?* | Normative rule — applies to every future decision in its domain | Architecture Principles Catalogue (Prelim) | Principle (Motivation) |
| **Goal** | *Where do we want to be?* | Desired future state — qualitative, no deadline required | Architecture Vision §3; domain artifacts | Goal (Motivation) |
| **Objective** | *How far, and by when?* | Measurable, time-bound result — must have a measure, target, and deadline | Architecture Vision §4; domain artifacts | Outcome (Motivation) |
| **Strategy** | *How will we get there?* | Chosen course of action — not an outcome, not a sequence | Architecture Vision; domain artifacts | Course of Action (Motivation) |
| **Plan** | *What will we do, in what order, by when?* | Sequenced execution — who, what, when | Architecture Roadmap (Phase E); Migration Plan (Phase F) | Implementation Event sequences (Impl. & Migration) |
| **Risk** | *What could go wrong?* | Uncertain future event with potential negative effect on objectives | Architecture Vision; Statement of Architecture Work; Migration Plan | Risk (Motivation, Strategy layer) |
| **Issue** | *What systemic concern is threatening a goal?* | Broad barrier or pattern of dysfunction — no single fix; threatens a Goal | Architecture Vision §5 (Phase A) | — |
| **Problem** | *What specific symptom is blocking an objective?* | Observable, measurable, and fixable — blocks an Objective | Architecture Vision §6 (Phase A) | — |

---

## Concept Definitions

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

**Structural parts** (risk register row):
- **Description** — what could happen
- **Likelihood** — High / Med / Low
- **Impact** — High / Med / Low
- **Risk Rating** — derived (High × High = High; Low × Low = Low; etc.)
- **Mitigation** — action taken to reduce likelihood or impact
- **Owner** — who is responsible for the mitigation

**What it is NOT:**
- Not a **Constraint** — a constraint is certain and non-negotiable (e.g., "the project must complete by 31 December 2026"); a risk is uncertain and conditional
- Not an **Issue** — an issue has already occurred and is being managed; a risk is future and hypothetical. When a risk materialises, it becomes an issue
- Not an **Assumption** — an assumption is something accepted as true for planning purposes (e.g., "the vendor will deliver on time"); a risk is what happens if the assumption is wrong

**Common confusions:**
- "Budget is limited" — this is a **Constraint** (a certainty), not a risk
- "The key architect may leave" — this is a **Risk** ✓ (uncertain; has likelihood and impact)
- "We assume stakeholder buy-in" — this is an **Assumption**. The associated risk is: "If stakeholder buy-in is not secured, adoption of the target architecture may fail"
- "The integration is broken" — this is an **Issue** (already occurred), not a risk

**TOGAF placement:** Architecture Vision (preliminary risks, Section 9); Statement of Architecture Work (risk register); Architecture Compliance Assessment (outstanding risks); Migration Plan (risk register per wave). Risk likelihood and impact ratings appear in the A3 Decision Log `Risk` column.

**ArchiMate:** `Risk` element in the Motivation aspect (Strategy layer, introduced in ArchiMate 3.0). Associated with `Goal` and `Outcome` via influence relationships.

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
