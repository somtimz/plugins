# Motivation — Concept Definitions



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

**Practitioner Notes:**
- Treat the Vision as a **negotiation tool**, not a static deliverable. Build multiple candidate visions and force trade-off discussions early.
- Frame the vision as a **story**: "From [current state] to [desired state] via [key choices]." Stories create emotional buy-in.
- **Maturity marker (L1→L5):** L1 = single static vision; L3 = vision co-created with business; L5 = vision continuously updated based on implementation feedback
- Quantify the **strategic tension** (current vs desired state gap) to drive urgency
- Periodically reassess whether the vision is solving the *right* problem — if market conditions shift, the vision may need updating

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

**Practitioner Notes:**
- The Mission is a **scope boundary test**. If a Driver or Goal cannot be traced to the Mission, flag it as potential scope creep.
- Mission statements are stable across engagements. Do not rewrite the Mission for every architecture cycle.
- **Maturity marker (L1→L5):** L1 = Mission copied from corporate website; L3 = Mission validated with stakeholders; L5 = Mission co-evolved with architecture and org design
- Use the Mission to **filter noise**: stakeholder requests outside the Mission are politely redirected

---

### Direction

**What it IS:**
Direction is the **complete statement of intent** the organisation gives to architecture work — the *why*. It is the **superset** that is delivered through Goals, Objectives, and Strategies. At every level, direction consists of three things: a **performance expectation** (what outcome is required), a **constraint** (what limits apply), and a **risk appetite** (how much uncertainty is acceptable). Direction always comes from above — a chain runs shareholders → board → executive → management → teams — and in the **governance cascade**, the *execution* of one level becomes the *direction* for the level below. Held in `engagement.json → direction` (the parent object for vision, mission, drivers, goals, objectives, strategies, …).

**The three components of any direction:**
- **Performance expectation** — what outcome is required
- **Constraint** — what limits apply
- **Risk appetite** — how much uncertainty is acceptable

**Delivered through (Direction is the superset; these operationalise it):**
- **Goals** (where we want to be) → **Objectives** (how far, by when) → **Strategies** (how we get there)
- **Drivers** establish *why* the direction is needed; **Principles**, **Constraints**, and **Standards** bound *how* it is pursued

**What it is NOT:**
- Not a **Goal / Objective / Strategy** — those are the parts; Direction is the whole performance-expectation-and-constraint set they decompose
- Not a **Vision / Mission** — Vision/Mission are enduring identity statements; Direction is the specific intent for *this* change, carrying a performance expectation, constraint, and risk appetite
- Not a **Decision** — Direction *shapes* decisions (Four Elements: Direction → Decision); a decision is a specific commitment made within direction's bounds

**Governance role:** Direction is the first of the **Four Elements of Governance** (Direction → Decision → Execution, with Control wrapping all — see `governance-framework.md`). Every architecture decision should trace back to a clear source of direction; a decision with no direction anchor is ungoverned. Deviations from direction must be **escalated up the cascade**, never resolved silently.

**TOGAF placement:** established in the Preliminary Phase and Phase A; communicated through the Statement of Architecture Work, Architecture Principles, and Architecture Vision. The risk-appetite component frames the Risk Register's tolerance.

**Practitioner Notes:**
- Capture **all three components** — a direction with a performance expectation but no stated constraint or risk appetite invites scope creep and risk blindness.
- **Restate before decomposing** — when receiving direction, echo it back ("grow revenue with new products sold to existing customers") before breaking it into goals/objectives.
- **Maturity marker (L1→L5):** L1 = direction is implicit/assumed; L3 = direction is explicit (performance expectation + constraint + risk appetite) and traced to decisions; L5 = direction is continuously re-validated and the cascade is governed end to end.

---

### Goal

**What it IS:**
A goal is a qualitative statement of a desired future state. It describes *where* the organisation wants to be — aspirational and long-term. Goals do not require a specific measure or deadline to be valid; their function is to set direction and establish what "success" looks like.

**Structural parts** (engagement.json `direction.goals[]`):
- **Statement** — one declarative sentence describing the desired state
- **Priority** — High / Medium / Low
- **Rationale** — why this is a goal for this engagement (1–2 sentences; what happens if it is not achieved)
- **Linked Drivers** — DRV-NNN IDs that motivate this goal

**What it is NOT:**
- Not an **Objective** — an objective is the measurable, time-bound version of a goal ("achieve 99.9% uptime by Q3 2026"); a goal is its qualitative parent
- Not a **Strategy** — a strategy says how to pursue a goal, not what the goal is
- Not a **Principle** — a principle governs decisions; a goal defines a destination
- Not an **EA Goal** — an EA Goal describes architecture capability outcomes (e.g., "Establish AI governance" or "Define architecture standards"), not business outcomes. See **Two Layers of Intent**.

**Common confusions:**
- "We want 99.9% uptime" — the number makes this an **Objective**, not a goal. The goal is "Achieve highly reliable platform operations"; the objective is the measurable target
- "Adopt API-first integration" — this is a **Strategy** (a chosen approach), not a goal
- "Comply with GDPR" — this is a **Requirement** (a compliance obligation), not a goal. The related goal might be "Become a trusted custodian of customer data"

**TOGAF placement:** `direction.goals[]` in `engagement.json`; Goals Register (`/ea-goals`); Architecture Vision §5 summary; referenced in domain architecture documents.

**ArchiMate:** `Goal` element in the Motivation aspect. Realised by `Outcomes`, associated with `Requirements`.

**Practitioner Notes:**
- Use **value streams to validate** whether goals actually deliver outcomes. A Goal without a value stream trace is unvalidated.
- Link goals directly to **KPIs and revenue/cost drivers** where possible.
- **Maturity marker (L1→L5):** L1 = goals are generic and unmeasured; L3 = goals linked to metrics and value streams; L5 = goals continuously refined based on delivery feedback
- Focus on **"where to play" and "how to win"** — not just process diagrams
- **Economic framing:** Every Goal should have a "what happens if not achieved" statement that includes business impact
- **Two Layers check:** Apply the quick test — *Would this still exist if the EA team were disbanded?* If no, it is an **EA Goal** and belongs in the Governance Framework or Architecture Principles, not the Architecture Vision.

---

### Objective

**What it IS:**
An objective is the measurable, time-bound operationalisation of a goal. It answers *how far, and by when?* Every objective must have three parts: a **unit of measure** (what you will count or track), a **target value** (how much), and a **deadline** (by when). Objectives are the direct anchor for Problems — if a problem cannot be linked to an objective, it may be out of scope.

**Structural parts** (Architecture Vision §10 / `direction.objectives[]`):
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

**TOGAF placement:** Objectives Register (`/ea-objectives`); Architecture Vision §10 summary; domain artifacts; `direction.objectives[]` in `engagement.json`.

**ArchiMate:** `Outcome` element in the Motivation aspect. Associated with `Goal` (realisation relationship).

**Practitioner Notes:**
- Define **success metrics before moving to Phase B**. An Objective without a measure is just a Goal in disguise.
- **Timebox** phase completion against objectives. If an objective cannot be met within the timebox, escalate or descope.
- **Maturity marker (L1→L5):** L1 = objectives have measures but no baselines; L3 = objectives have baselines, targets, and deadlines; L5 = objectives are dynamically adjusted based on implementation learnings
- Objectives are the **primary anchor for Problems**. If a problem cannot be linked to an Objective, it may be out of scope.
- Track **decision latency** per objective — slow architecture = delayed value

---

### Issue

**What it IS:**
An issue is a broader, systemic concern that threatens the organisation's ability to achieve one or more goals. Issues are management-level problems — patterns of dysfunction, capability gaps, unresolved conflicts, or sustained exposure to a driver that has no single fix. An issue has multiple contributing causes, affects a domain or process broadly, and requires sustained organisational response rather than a technical patch.

**Structural parts** (Architecture Vision §7):
- **Statement** — one sentence naming the systemic concern
- **Area** — organisational, process, or technology domain most affected
- **Threatens Goal(s)** — G-NNN IDs of the goals this issue puts at risk
- **Evidence** — observable signal, event, or data point that confirms this issue exists (e.g. "incident log shows 12 P1 outages in 90 days")
- **Raised By** — stakeholder or source that surfaced this issue

**What it is NOT:**
- Not a **Problem** — a problem is a specific, observable symptom with a direct fix; an issue is broader and systemic
- Not a **Risk** — a risk is a future, uncertain event; an issue is a present, ongoing concern. When a risk materialises, it becomes an issue
- Not a **Driver** — a driver is an external or internal force; an issue is the organisational consequence of inadequately responding to a driver

**Common confusions:**
- "Our API is returning 500 errors" — this is a **Problem** (specific, observable, fixable)
- "We have poor data culture" — this is an **Issue** (systemic, no single fix)
- "Increasing regulatory pressure" — this is a **Driver** (external force)
- "The integration broke" — this is a **Problem** (specific, fixable). The related issue might be "Our integration architecture lacks resilience and monitoring"

**TOGAF placement:** Issues Register (`/ea-issues`); Architecture Vision §7 summary (Phase A). Issues captured here feed into Gap Analysis, Risk assessments, and Requirements.

**Practitioner Notes:**
- Treat gaps as **opportunities to simplify**, not just deficits to fill. The best architecture often removes rather than adds.
- Issues are **systemic concerns** — they have multiple contributing causes and no single fix.
- **Maturity marker (L1→L5):** L1 = issues are vague complaints; L3 = issues linked to goals and root causes; L5 = issues proactively identified via leading indicators before they become crises
- **Failure mode watch:** Documentation Trap — documenting issues without addressing systemic causes is waste

---

### Problem

**What it IS:**
A problem is a specific, observable, and fixable symptom that is actively blocking the achievement of one or more objectives. Problems have a clear cause-and-effect relationship: a root cause produces a visible symptom that degrades performance against a known objective. Because they are specific and measurable, problems can be prioritised, assigned, and resolved directly.

**Structural parts** (Architecture Vision §8):
- **Statement** — one sentence naming the specific problem
- **Observable Symptom** — what can be seen or measured today (ideally a number)
- **Blocks Objective(s)** — OBJ-NNN IDs of the objectives this problem is preventing
- **Evidence** — data point, incident, or measurement confirming the symptom is currently active
- **Raised By** — stakeholder or source that identified this problem

**What it is NOT:**
- Not an **Issue** — an issue is broad and systemic; a problem is specific and fixable. Multiple problems can contribute to a single issue
- Not a **Risk** — a risk is uncertain and future; a problem is certain and present
- Not a **Gap** — a gap is the difference between baseline and target state in a specific architecture domain (used in Gap Analysis); a problem is a current operational failure

**Common confusions:**
- "We have poor data quality" — this is an **Issue** (systemic). The problem is: "30% of customer records have duplicate entries, causing order processing errors 4× per week"
- "Our systems are slow" — this is an **Issue**. The problem is: "Mobile checkout page load time averages 8.2 seconds, causing 68% cart abandonment"
- "The vendor may not deliver" — this is a **Risk** (uncertain, future)

**TOGAF placement:** Problems Register (`/ea-problems`); Architecture Vision §8 summary (Phase A). Problems feed directly into Requirements — each problem should produce one or more architecture requirements.

**Practitioner Notes:**
- Problems are **specific, observable, and fixable** — if it is not fixable, it is an Issue, not a Problem.
- **Hypothesis-driven approach:** Test assumptions about root causes before committing to solutions.
- **Maturity marker (L1→L5):** L1 = problems described in vague terms; L3 = problems have measurable symptoms and linked objectives; L5 = problems are anticipated and prevented via fitness functions and automated checks
- **Economic framing:** Quantify the cost of each problem (revenue lost, inefficiency, risk exposure) to prioritize fixes

---

### Opportunity (OPP-NNN)

**What it IS:**
An Opportunity is an actionable possibility — a favourable opening the organisation could pursue to create or capture value, beyond simply fixing what is broken. Where Drivers, Issues, and Problems describe pressure and dysfunction, an Opportunity describes upside: a market gap, an emerging technology, a capability the org could newly exploit. It answers *"What could we gain if we acted?"* Captured in `engagement.json → direction.opportunities[]` and surfaced during brainstorming and Phase A.

**Types:**
- **Exploit** — capitalise on an existing advantage the org already holds
- **Enhance** — amplify a current capability to widen the lead
- **Emerge** — pursue something not previously in scope (new market, new technology, new model)

**Key relationships:**
- **Arises from** Drivers (a force can be a threat *and* an opening) and links to the Goals (G-NNN) it would advance
- **Distinct from a Problem** — a problem is a symptom to remove; an opportunity is value to capture. Resolving a problem may *reveal* an opportunity worth tracking separately.
- May justify new **Strategies**, **Capabilities**, or **Work Packages** when pursued

**What it is NOT:**
- Not a **Goal** — a goal is the desired future state; an opportunity is a possibility that, if taken, helps reach it
- Not a **Driver** — a driver is the underlying force; an opportunity is a specific actionable opening that force creates
- Not a **Requirement** — an opportunity is directional; it generates requirements only once a decision to pursue it is made

**TOGAF placement:** Architecture Vision (Phase A) — captured alongside Drivers/Issues/Problems as part of structuring corporate intent; an opportunity taken becomes input to Strategy and the Roadmap.

**Practitioner Notes:**
- Keep opportunities **honest** — an opportunity with no plausible value or no owner is wishful thinking; flag it.
- The best opportunities are often the **inverse of a problem** — when capturing problems, ask "if we fixed this, what would it open up?"
- **Maturity marker (L1→L5):** L1 = opportunities are a wish list; L3 = opportunities are typed, linked to drivers/goals, and triaged; L5 = opportunity pursuit is governed against strategy and revisited as the market shifts.

---

### Strategy

**What it IS:**
A strategy is a chosen course of action or approach that the organisation will take to pursue its goals and objectives. It answers *how* — selecting one path from among alternatives. A strategy does not describe steps or sequences; it names the approach.

**Structural parts** (engagement.json `direction.strategies[]`; managed via `/ea-strategies`):
- **Statement** — one declarative sentence naming the approach
- **Type** — the kind of approach: Build / Buy / Partner / Consolidate / Modernise / Defend / Other
- **Supports** — IDs of the goals or objectives this strategy serves
- **Horizon** — when the approach plays out: Near (0–12mo) / Mid (1–2yr) / Long (2yr+)
- **Priority** — High / Medium / Low
- **Status** — Active / Completed / Superseded
- **Rationale** — why this approach over the alternatives ("where to play / how to win")
- **Executing work packages** — *derived*, not stored: Architecture Roadmap WP rows whose `Executes Strategies` references this STR-NNN

**What it is NOT:**
- Not a **Plan** — a strategy says "we will take the API-first approach"; a plan says "in Q1 we will build the API gateway, in Q2 we will migrate service X, in Q3 we will retire the legacy integration layer"
- Not a **Goal** — a strategy is an approach to achieve a goal, not the goal itself
- Not a **Principle** — a strategy is chosen for this engagement; a principle applies universally

**Common confusions:**
- "Move to the cloud" — this is a strategy (the chosen approach). "Have 80% of workloads on cloud by Q4 2027" is the **Objective**. "Cloud-first" may be an architecture **Principle** if it's a permanent organisational rule
- "We will improve data quality" — this is a **Goal** (a desired state), not a strategy
- "We will adopt event-driven architecture" — this is a **Strategy** ✓

**TOGAF placement:** `direction.strategies[]` in `engagement.json`; Strategy Register (`/ea-strategies`); Architecture Vision §11 Direction Summary; Business Architecture (business strategy); Technology Architecture (technology strategy).

**ArchiMate:** `Course of Action` element in the Motivation aspect. Realises `Goals` and `Objectives`.

**Practitioner Notes:**
- Use **capability-based planning** to bridge strategy and execution. Every strategy should map to capabilities that must be developed or enhanced.
- Focus on **"where to play" and "how to win"** — strategies that do not answer these questions are not actionable.
- **Maturity marker (L1→L5):** L1 = strategies are wish lists; L3 = strategies linked to capabilities and gaps; L5 = strategies continuously validated against market shifts and delivery outcomes
- **Failure mode watch:** Static target architecture illusion — strategies that assume a fixed end-state will become obsolete

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

**Practitioner Notes:**
- Decompose large transformations into **independently valuable increments**. Each increment should deliver standalone value.
- Treat **migration planning as a product** — prioritize value delivery over technical dependency alone.
- **Maturity marker (L1→L5):** L1 = static wish-list roadmap; L3 = roadmap aligned with agile increments and funding cycles; L5 = roadmap continuously updated with quick wins and feedback loops
- Design for **optionality** — preserve future flexibility by abstracting vendor lock-in behind interfaces
- Include **exit criteria** for legacy systems to avoid indefinite coexistence

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

**TOGAF placement:** Architecture Vision (preliminary risks, §16); Statement of Architecture Work (risk register); Architecture Compliance Assessment (outstanding risks); Migration Plan (risk register per wave, §4). The consolidated **Risk Register** artifact aggregates all of the above into a single cross-cutting view — use `/ea-risks` to generate it. Risk likelihood and impact ratings also appear in the A3 Decision Log `Risk` column.

**ArchiMate:** `Risk` element in the Motivation aspect (Strategy layer, introduced in ArchiMate 3.0). Associated with `Goal` and `Outcome` via influence relationships.

**Practitioner Notes:**
- **Quantify uncertainty** — do not hide it behind diagrams. Express risks in financial terms where possible.
- Track architecture decisions (ADR-style) as first-class artifacts — risks often materialize when decision rationale is lost.
- **Maturity marker (L1→L5):** L1 = risks documented but not acted on; L3 = risks linked to mitigation plans and owners; L5 = risks actively managed via systemic architecture decisions (e.g., reducing integration points)
- Use architecture to **actively manage systemic risk**, not just document it
- **Design for graceful degradation**, not just peak performance

---

### Metrics

**What it IS:**
Metrics are specific, quantifiable measures used to track progress, performance, and outcomes. They provide evidence as to whether Strategies are working and whether Objectives and Goals are being achieved. Metrics answer *"How do we know we are succeeding?"*

**Governance role — metrics give Control its teeth:**
Metrics are the **instruments that give the Control element of governance its teeth**. Without metrics, governance is **opinion-based**; with metrics, it is **evidence-based**. Control is the governance element that verifies execution conforms to decisions and that decisions align with direction — and it can only do so observably through measurement. Each metric type tracks a specific element of direction, which is why a metric with no linked direction item is an orphan:

| Metric type | Tracks | Question it answers | Linked to |
|---|---|---|---|
| **Outcome** | A Goal | Is the desired state being approached? | G-NNN |
| **Performance** | An Objective | Is the measurable target on track? | OBJ-NNN |
| **Activity** | A Strategy | Is the chosen approach being executed? | STR-NNN |
| **Benefit** | A projected value (Cost Entry) | Did we realise the value? | FIN-NNN |

**Leading vs Lagging:**
- **Leading metrics** — predictive; indicate whether future performance is likely to improve or worsen (e.g. number of teams trained on new process before go-live)
- **Lagging metrics** — outcome-based; indicate whether desired results have already been achieved (e.g. NPS score after three months of operation)
- A robust measurement framework uses both: leading metrics to act early, lagging metrics to validate success

**Feedback loop role:**
Metrics close the loop between intention and evidence:
- If performance is on target → metrics **validate** the Strategy; Goals and Objectives are being achieved
- If performance is below threshold → metrics **surface new Problems** (observable symptoms) or **reveal deeper Issues** (systemic conditions)
- Metrics also **evaluate Capability Maturity** — when a capability is not performing, metrics identify which ones need investment

**Structural parts** (Architecture Vision §11 / Metrics Register):
- **ID** — MET-NNN
- **Description** — what is being measured
- **Type** — Leading / Lagging
- **Unit** — how it is measured
- **Baseline** — current value
- **Target** — desired value
- **Deadline** — when the target must be reached
- **Linked Objective(s)** — OBJ-NNN this metric tracks
- **Baseline Source** — where the current-state measurement comes from (report, system, stakeholder estimate)

**What it is NOT:**
- Not an Objective — an Objective defines the target; a Metric measures whether the target is being reached
- Not a KPI (necessarily) — all KPIs are metrics, but not all metrics are KPIs; KPIs are the most strategically significant metrics
- Not a requirement — a requirement specifies what must be done; a metric measures whether it has been done successfully

**TOGAF placement:** Architecture Vision §11 Strategic Direction Summary; referenced in Phase G (Implementation Governance) for compliance tracking; Phase H (Architecture Change Management) for performance feedback.

**Practitioner Notes:**
- **Measure success through delivery outcomes** (cycle time, quality, value), not artifact completeness.
- Metrics close the feedback loop: they either **validate** strategy or **surface new Issues/Problems**.
- **Maturity marker (L1→L5):** L1 = metrics are vanity metrics (artifact count); L3 = metrics linked to delivery outcomes and business KPIs; L5 = metrics automatically collected and trigger architecture adaptation
- Align architecture KPIs with **enterprise OKRs** (e.g., reuse rate, time-to-decision)
- Use **both leading and lagging metrics** — leading metrics for early action, lagging metrics for validation

---
