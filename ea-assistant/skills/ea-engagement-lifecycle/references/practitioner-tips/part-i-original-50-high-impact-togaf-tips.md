# Part I: Original 50 High-Impact TOGAF Tips


### Strategic Framing & Positioning (Tips 1–10)

#### Tip 1 — Anchor ADM cycles to business outcomes, not architecture artifacts
**Why it matters:** Architecture that cannot demonstrate business value becomes overhead. Every phase must show measurable impact.  
**When to apply:** All phases. Every artifact should trace to a business outcome.  
**Related concept:** Business Driver, Goal, Objective, Metric.  
**How to incorporate:** In `architecture-vision.md` §4 Business Drivers, link every driver to a measurable outcome. In `statement-of-architecture-work.md` §6 Acceptance Criteria, define objective criteria.

#### Tip 2 — Position architecture as a decision-support function, not a documentation function
**Why it matters:** The real output of architecture is a managed constraint system (principles, standards, guardrails, patterns), not documents.  
**When to apply:** Preliminary, Phase A, Phase G. `governance-framework.md`, `architecture-principles.md`.  
**Related concept:** Principle, Governance Framework.  
**How to incorporate:** In `governance-framework.md` §1, frame governance as "decision support." In `architecture-principles.md`, ensure each principle is an enforceable constraint.

#### Tip 3 — Continuously align architecture work with portfolio management and funding cycles
**Why it matters:** Architecture that is not legible in financial terms will be bypassed by delivery and finance.  
**When to apply:** Phase E, F. `architecture-roadmap.md`, `migration-plan.md`.  
**Related concept:** Plan, Roadmap, Work Package.  
**How to incorporate:** In `architecture-roadmap.md` §4, show how each work package aligns to funding cycles. In `migration-plan.md` §3, reference budget constraints.

#### Tip 4 — Use capability-based planning to bridge strategy and execution
**Why it matters:** Capabilities are stable, hierarchical, and independent of org structure — they provide a durable bridge between "what we want to achieve" and "what we must be able to do."  
**When to apply:** Phase B. `business-architecture.md` §4 Business Capabilities.  
**Related concept:** Capability Model, Operating Model, Strategy.  
**How to incorporate:** Map every strategy (STR-NNN) to at least one capability (CAP-NNN). Ensure capabilities are linked to value streams.

#### Tip 5 — Treat the Architecture Vision as a negotiation tool, not a static deliverable
**Why it matters:** Phase A is where competing stakeholder interests are reconciled. The vision secures alignment, funding, and executive sponsorship.  
**When to apply:** Phase A. `architecture-vision.md` §1 Executive Summary, §2 Scope.  
**Related concept:** Vision, Mission.  
**How to incorporate:** Build multiple candidate visions and force trade-off discussions. Co-create with business leaders. Define success metrics before Phase B.

#### Tip 6 — Explicitly connect architecture work to strategic themes (growth, cost, risk, compliance)
**Why it matters:** Without explicit strategic theme linkage, architecture appears disconnected from enterprise priorities.  
**When to apply:** Phase A. `architecture-vision.md` §4 Business Drivers.  
**Related concept:** Business Driver, Strategy.  
**How to incorporate:** Tag each driver with its strategic theme. Validate that all major themes are represented.

#### Tip 7 — Build architecture narratives around business scenarios, not technical stacks
**Why it matters:** Executives and business stakeholders respond to scenarios, not technology descriptions.  
**When to apply:** Phase A, B. `architecture-vision.md` §1, `business-architecture.md` §2 Business Context.  
**Related concept:** Vision, Business Scenario.  
**How to incorporate:** Use business scenarios to validate the vision. Frame business architecture around "where to play" and "how to win."

#### Tip 8 — Use value streams to validate whether capabilities actually deliver outcomes
**Why it matters:** Capabilities in isolation do not prove value delivery. Value streams trace capabilities to customer and business outcomes.  
**When to apply:** Phase B. `business-architecture.md` §5 Value Streams.  
**Related concept:** Capability Model, Value Stream, Goal.  
**How to incorporate:** Ensure every capability is referenced by at least one value stream. Link value streams to goals (G-NNN).

#### Tip 9 — Avoid "framework worship" — TOGAF is a tool, not the goal
**Why it matters:** Rigid adherence to framework purity produces low-value artifacts. Tailor aggressively to context.  
**When to apply:** All phases. Especially Preliminary (tailoring) and Phase G (governance).  
**Related concept:** Tailored ADM, Governance.  
**How to incorporate:** In Preliminary, document the tailored ADM explicitly. In governance, measure by decision speed, not checklist completion.

#### Tip 10 — Periodically reassess whether architecture is solving the *right* problem
**Why it matters:** Architecture teams often solve elegantly the wrong problem. Regular reassessment prevents drift.  
**When to apply:** Phase A, H. `architecture-vision.md`, `change-request.md`.  
**Related concept:** Issue, Problem, Business Driver.  
**How to incorporate:** Add a "Problem Reassessment" checkpoint at the start of each ADM cycle. In Phase H, use leading indicators to trigger reassessment.

---

### ADM Execution Excellence (Tips 11–20)

#### Tip 11 — Don’t run ADM linearly — tailor and iterate aggressively based on context and maturity
**Why it matters:** Real enterprises do not transform in clean phases. Mini-cycles and dynamic adaptation are essential.  
**When to apply:** All phases.  
**Related concept:** Tailored ADM, Maturity Model.  
**How to incorporate:** Document the tailored ADM in Preliminary. Revisit tailoring at each phase gate.

#### Tip 12 — Timebox phases; avoid over-engineering early-phase artifacts
**Why it matters:** Over-documenting current state slows momentum and consumes resources that should go to target-state design.  
**When to apply:** All phases. Especially Phase B–D (baseline documentation).  
**Related concept:** Baseline Architecture, Target Architecture.  
**How to incorporate:** In `statement-of-architecture-work.md` §4 Schedule, set phase timeboxes. In `business-architecture.md`, document "just enough" baseline.

#### Tip 13 — Start with just-enough Baseline — over-documenting current state slows momentum
**Why it matters:** Baseline architecture should be sufficient to identify gaps, dependencies, constraints, and risks — no more.  
**When to apply:** Phases B, C, D. All baseline artifact sections.  
**Related concept:** Baseline Architecture, Gap Analysis.  
**How to incorporate:** In baseline sections, include a note: "Document only what is necessary to identify gaps and dependencies."

#### Tip 14 — Use Architecture Building Blocks (ABBs) to guide thinking; convert to Solution Building Blocks (SBBs) only when needed
**Why it matters:** Premature SBB specification constrains solution creativity and locks in vendor choices too early.  
**When to apply:** Phase C, D, E.  
**Related concept:** Architecture Building Block, Solution Building Block.  
**How to incorporate:** In `application-architecture.md` and `technology-architecture.md`, separate ABB and SBB discussions. Defer SBB selection to Phase E.

#### Tip 15 — Maintain a living Requirements Repository — don’t let requirements freeze too early
**Why it matters:** Requirements evolve as architecture work uncovers trade-offs, constraints, and market shifts.  
**When to apply:** Requirements phase, all phases. `requirements-register.md`.  
**Related concept:** Requirement, Traceability Matrix.  
**How to incorporate:** In `requirements-register.md`, include a "Last Reviewed" field. Review requirements at every phase gate.

#### Tip 16 — Reuse patterns and reference models instead of reinventing architectures
**Why it matters:** Reinventing standard patterns wastes effort and introduces unnecessary variation.  
**When to apply:** Phases C, D. `application-architecture.md`, `technology-architecture.md`.  
**Related concept:** Reference Architecture, Pattern.  
**How to incorporate:** In architecture documents, include a "Reference Models Used" section. Reference the architecture repository.

#### Tip 17 — Use hypothesis-driven architecture — test assumptions early
**Why it matters:** Architecture decisions made on unvalidated assumptions create downstream risk.  
**When to apply:** Phases B, C, D. `gap-analysis.md` §3 Hypothesis & Validation.  
**Related concept:** Gap Analysis, Assumption, Risk.  
**How to incorporate:** In `gap-analysis.md`, require a hypothesis and validation method for each gap. In `business-architecture.md`, test capability assumptions.

#### Tip 18 — Treat gaps as opportunities to simplify, not just deficits to fill
**Why it matters:** Gap analysis often defaults to "add more." Simplification is frequently the higher-value response.  
**When to apply:** Phases B, C, D, E. `gap-analysis.md`, `consolidated-gap-analysis.md`.  
**Related concept:** Gap, Capability Gap, Opportunity.  
**How to incorporate:** In gap analysis, include a "Simplify?" column. Ask: "Can we eliminate this capability rather than upgrade it?"

#### Tip 19 — Decompose large transformations into independently valuable increments
**Why it matters:** Big-bang transformations have high failure rates. Increments that deliver standalone value reduce risk and maintain momentum.  
**When to apply:** Phases E, F. `architecture-roadmap.md`, `migration-plan.md`.  
**Related concept:** Work Package, Plan, Transition Architecture.  
**How to incorporate:** In `architecture-roadmap.md` §2, ensure every work package advances at least one goal. In `migration-plan.md` §2, sequence for value delivery.

#### Tip 20 — Use architecture viewpoints deliberately — each view must answer a stakeholder concern
**Why it matters:** Viewpoints without a stakeholder concern become institutional clutter.  
**When to apply:** All phases. Diagram sections of all artifacts.  
**Related concept:** Viewpoint, Stakeholder Concern, ArchiMate.  
**How to incorporate:** In every artifact's Diagrams section, state the stakeholder concern each view answers. Use `/ea-diagram` with explicit viewpoint purpose.

---

### Governance & Decision-Making (Tips 21–30)

#### Tip 21 — Make Architecture Governance lightweight but unavoidable — embed it into delivery pipelines
**Why it matters:** Heavy governance creates bottlenecks. Lightweight governance embedded in pipelines scales.  
**When to apply:** Phase G. `governance-framework.md`, `implementation-governance-plan.md`.  
**Related concept:** Governance, Compliance, Fitness Function.  
**How to incorporate:** In `governance-framework.md`, define guardrails (approved paths) rather than gates (approvals). Reference automated checks.

#### Tip 22 — Use architecture principles as enforceable constraints, not aspirational statements
**Why it matters:** Principles that are not enforced are ignored. They must act as decision filters.  
**When to apply:** Preliminary, Phase G. `architecture-principles.md`, `governance-framework.md`.  
**Related concept:** Principle, Governance.  
**How to incorporate:** In `architecture-principles.md`, include implications and enforcement mechanism per principle. In governance, track deviations.

#### Tip 23 — Define clear decision rights between architects, product owners, and engineering leads
**Why it matters:** Ambiguous decision rights create deadlocks and shadow decision-making.  
**When to apply:** Preliminary, Phase G. `governance-framework.md` §2 Decision Rights.  
**Related concept:** Governance, Decision.  
**How to incorporate:** In `governance-framework.md`, use a RACI matrix for architecture decisions. Define escalation paths.

#### Tip 24 — Establish "guardrails over gates" — enable autonomy within boundaries
**Why it matters:** Teams innovate faster when they know the boundaries rather than waiting for approvals.  
**When to apply:** Preliminary, Phase G. `governance-framework.md`, `implementation-governance-plan.md`.  
**Related concept:** Governance, Standard.  
**How to incorporate:** In `governance-framework.md`, define "golden paths" (approved stacks) and "flexible zones" (experimental). In Phase G, use automated checks.

#### Tip 25 — Track architecture decisions (ADR-style) as first-class artifacts
**Why it matters:** Decisions without documented context are re-litigated. ADRs preserve rationale and reduce future ambiguity.  
**When to apply:** Any phase. All major artifacts with A3/A5 appendices.  
**Related concept:** Architecture Decision Record, Decision Log.  
**How to incorporate:** Use `/ea-adrs` for all technology/vendor/pattern decisions. Link A3 rows to ADR-NNN IDs.

#### Tip 26 — Shift governance left — review decisions earlier, not just at release checkpoints
**Why it matters:** Late-stage governance reviews are expensive and adversarial. Early engagement prevents divergence.  
**When to apply:** Phase G. `implementation-governance-plan.md`.  
**Related concept:** Governance, Compliance.  
**How to incorporate:** In `implementation-governance-plan.md`, define governance touchpoints at design time, not just deployment.

#### Tip 27 — Integrate governance with DevSecOps pipelines for continuous compliance
**Why it matters:** Manual compliance checks do not scale. Embedding standards in pipelines ensures consistency.  
**When to apply:** Phase G. `implementation-governance-plan.md`.  
**Related concept:** Governance, Fitness Function, Compliance.  
**How to incorporate:** In `implementation-governance-plan.md`, list pipeline-integrated checks (security, API conventions, dependency constraints).

#### Tip 28 — Measure governance effectiveness by decision speed, not control coverage
**Why it matters:** Slow architecture = delayed value. Decision latency is a leading indicator of architecture health.  
**When to apply:** Phase H. `governance-framework.md` §4 Metrics.  
**Related concept:** Governance, Metric, Decision.  
**How to incorporate:** In `governance-framework.md`, add a "Decision Latency" metric. Track time from decision request to resolution.

#### Tip 29 — Create escalation paths for architectural conflicts — avoid deadlocks
**Why it matters:** Unresolved conflicts between architecture and delivery degrade trust and create shadow IT.  
**When to apply:** All phases. `governance-framework.md` §2.  
**Related concept:** Governance, Decision, Risk.  
**How to incorporate:** In `governance-framework.md`, define explicit escalation paths with time limits. Reference the Architecture Board as final arbiter.

#### Tip 30 — Regularly prune obsolete standards and policies
**Why it matters:** Accumulated standards become constraints on innovation. Active pruning keeps the constraint system relevant.  
**When to apply:** Phase H. `governance-framework.md`, `architecture-principles.md`.  
**Related concept:** Principle, Standard, Governance.  
**How to incorporate:** In `governance-framework.md`, include a "Standards Review Cycle." In Phase H, feed implementation learnings back into standards.

---

### Stakeholder & Communication Mastery (Tips 31–40)

#### Tip 31 — Segment stakeholders and tailor viewpoints — don’t reuse the same views for executives and engineers
**Why it matters:** A single view cannot serve both strategic and technical concerns. Segmentation improves understanding and buy-in.  
**When to apply:** Phase A. `stakeholder-map.md`, `architecture-vision.md`.  
**Related concept:** Stakeholder, Viewpoint, Communication.  
**How to incorporate:** In `stakeholder-map.md` §2, segment by power/interest and information needs. In `architecture-vision.md` §3, map viewpoints to segments.

#### Tip 32 — Translate architecture into financial and risk language for senior stakeholders
**Why it matters:** Architecture that cannot be expressed in economic terms will lose to more financially legible initiatives.  
**When to apply:** Phase A, E, F. `architecture-vision.md`, `architecture-roadmap.md`, `migration-plan.md`.  
**Related concept:** Metric, Risk, Business Driver.  
**How to incorporate:** In `architecture-vision.md` §4, quantify driver impact where possible. In `architecture-roadmap.md`, show cost/benefit per work package.

#### Tip 33 — Use visuals (heatmaps, capability maps, roadmaps) instead of verbose documents
**Why it matters:** Visuals compress complexity and improve retention. They are more likely to be referenced than long documents.  
**When to apply:** All phases. All artifacts with diagram sections.  
**Related concept:** Diagram, Viewpoint, Capability Model.  
**How to incorporate:** In every artifact, prefer visual summaries. Use `/ea-diagram` to create heatmaps, capability maps, and roadmap views.

#### Tip 34 — Build coalitions early — architecture success depends on informal influence networks
**Why it matters:** Formal authority alone does not drive adoption. Informal networks accelerate buy-in and resolve resistance.  
**When to apply:** Phase A. `stakeholder-map.md`, `architecture-vision.md`.  
**Related concept:** Stakeholder, Influence, Communication.  
**How to incorporate:** In `stakeholder-map.md`, identify "champions" and "blockers." In `architecture-vision.md` §3, note coalition-building status.

#### Tip 35 — Treat resistance as signal — use it to refine assumptions and constraints
**Why it matters:** Resistance often surfaces valid concerns that the architecture has not adequately addressed.  
**When to apply:** All phases. `stakeholder-map.md` §5 Resistance & Concerns.  
**Related concept:** Stakeholder Concern, Constraint, Assumption.  
**How to incorporate:** In `stakeholder-map.md`, create a "Resistance Analysis" section. Map resistance to specific assumptions or constraints.

#### Tip 36 — Communicate trade-offs explicitly — avoid presenting "perfect" solutions
**Why it matters:** Stakeholders distrust architecture that appears to have no downsides. Explicit trade-offs build credibility.  &nbsp;**When to apply:** All phases. Every artifact with decision content.  
**Related concept:** Decision, Risk, Architecture Decision Record.  
**How to incorporate:** In A3 Decision Log entries, always include trade-offs. In `architecture-vision.md`, present multiple candidate visions with trade-offs.

#### Tip 37 — Use storytelling to explain transformation journeys
**Why it matters:** Narratives are more memorable and persuasive than frameworks. A transformation story creates emotional buy-in.  
**When to apply:** Phase A. `architecture-vision.md` §1 Executive Summary.  
**Related concept:** Vision, Communication.  
**How to incorporate:** In `architecture-vision.md` §1, frame the executive summary as a story: "From [current state] to [desired state] via [key choices]."

#### Tip 38 — Align terminology across business and IT to avoid semantic confusion
**Why it matters:** Misaligned terminology creates misunderstood requirements and duplicated effort.  
**When to apply:** All phases. `engagement-charter.md`, `ea-local-config.md`.  
**Related concept:** Concept, Requirement, Communication.  
**How to incorporate:** In `engagement-charter.md`, include a "Terminology Alignment" section. Maintain a glossary in `ea-local-config.md`.

#### Tip 39 — Validate stakeholder understanding — don’t assume alignment
**Why it matters:** Stakeholders may agree in meetings but have different interpretations. Validation prevents downstream rework.  
**When to apply:** Phase A, G. `stakeholder-map.md`, `compliance-assessment.md`.  
**Related concept:** Stakeholder, Communication, Compliance.  
**How to incorporate:** In `stakeholder-map.md`, add a "Understanding Validated" field. In Phase G, include comprehension checks in compliance reviews.

#### Tip 40 — Keep communication continuous, not phase-bound
**Why it matters:** Phase-bound communication creates information gaps and erodes trust. Continuous engagement maintains momentum.  
**When to apply:** All phases. `communications-plan.md`.  
**Related concept:** Communication, Governance, Stakeholder.  
**How to incorporate:** In `communications-plan.md`, define a cadence (weekly/biweekly) rather than phase-gate-only updates.

---

### Integration with Delivery & Agile (Tips 41–50)

#### Tip 41 — Embed architects in product teams — avoid centralized ivory tower models
**Why it matters:** Centralized architecture becomes a bottleneck. Embedded architects maintain coherence without creating delays.  
**When to apply:** Phase B, C, D, G. `governance-framework.md`, `implementation-governance-plan.md`.  
**Related concept:** Governance, Operating Model, Team.  
**How to incorporate:** In `governance-framework.md`, define "enterprise + domain architect" model. In `implementation-governance-plan.md`, specify embedded architect roles.

#### Tip 42 — Align ADM phases with agile increments (e.g., Vision with PI planning, Opportunities with backlog shaping)
**Why it matters:** Misaligned architecture and agile rhythms create friction. Synchronization improves flow.  
**When to apply:** All phases. `architecture-roadmap.md`, `migration-plan.md`.  
**Related concept:** Plan, Agile, Increment.  
**How to incorporate:** In `architecture-roadmap.md`, map work packages to agile increments (PIs, sprints). In `migration-plan.md`, align waves with release trains.

#### Tip 43 — Use reference architectures and patterns to accelerate teams instead of reviewing every design
**Why it matters:** Individual design reviews do not scale. Pre-approved patterns enable autonomous speed within guardrails.  
**When to apply:** Phases C, D, G. `technology-architecture.md`, `implementation-governance-plan.md`.  
**Related concept:** Reference Architecture, Pattern, Standard.  
**How to incorporate:** In `technology-architecture.md`, include a "Reference Patterns" section. In governance, promote pattern adoption over individual review.

#### Tip 44 — Continuously validate architecture through implementation feedback loops
**Why it matters:** Architecture assumptions are often wrong. Implementation feedback closes the loop and prevents drift.  
**When to apply:** Phase G, H. `compliance-assessment.md`, `change-request.md`.  
**Related concept:** Compliance, Feedback, Metric.  
**How to incorporate:** In `compliance-assessment.md`, include an "Architecture Validation" section. In Phase H, use metrics to surface issues.

#### Tip 45 — Treat migration planning as a product — prioritize increments that deliver standalone value
**Why it matters:** Migration plans that are purely technical sequences fail to secure business commitment. Value-centric sequencing maintains funding and morale.  
**When to apply:** Phase F. `migration-plan.md`.  
**Related concept:** Plan, Work Package, Value Stream.  
**How to incorporate:** In `migration-plan.md` §2, for each wave, define the standalone value delivered. Include a "Value Realization" checkpoint.

#### Tip 46 — Ensure architecture runway exists ahead of development demand
**Why it matters:** Development teams waiting for architecture decisions lose velocity. Runway ahead of demand prevents blocking.  
**When to apply:** Phase E, F. `architecture-roadmap.md`.  
**Related concept:** Roadmap, Plan, Work Package.  
**How to incorporate:** In `architecture-roadmap.md`, include a "Runway" section showing how far ahead architecture is vs. development demand.

#### Tip 47 — Co-create solutions with engineers to increase adoption
**Why it matters:** Architectures imposed on engineers are bypassed. Co-creation produces architectures that are understood and adopted.  
**When to apply:** Phases C, D, E, G. All domain architecture artifacts.  
**Related concept:** Governance, Solution, Team.  
**How to incorporate:** In architecture artifacts, include an "Engineer Review" section. In governance, require engineer sign-off on standards.

#### Tip 48 — Use fitness functions (automated checks) to enforce architectural intent
**Why it matters:** Manual governance does not scale. Automated fitness functions embed architectural constraints into delivery pipelines.  
**When to apply:** Phase G. `implementation-governance-plan.md`, `technology-architecture.md`.  
**Related concept:** Governance, Fitness Function, Standard.  
**How to incorporate:** In `technology-architecture.md`, define measurable fitness functions (latency thresholds, coupling limits, security constraints). In `implementation-governance-plan.md`, list pipeline-integrated checks.

#### Tip 49 — Balance intentional architecture with emergent design — don’t over-specify
**Why it matters:** Over-specification suppresses legitimate experimentation and domain-specific innovation. Intent + boundaries > prescriptions.  
**When to apply:** Phases C, D, E. All domain architecture artifacts.  
**Related concept:** Architecture, Design, Pattern.  
**How to incorporate:** In architecture artifacts, specify "intent + constraints" rather than exact implementations. Use pattern #3 (Intent-Based Architecture).

#### Tip 50 — Measure success through delivery outcomes (cycle time, quality, value), not artifact completeness
**Why it matters:** Artifact volume is a vanity metric. Delivery outcomes (speed, quality, value) are the real measure of architecture success.  
**When to apply:** Phase H. `governance-framework.md` §4 Metrics.  
**Related concept:** Metric, Governance, Delivery.  
**How to incorporate:** In `governance-framework.md`, replace "artifacts produced" metrics with "delivery outcomes" metrics (cycle time, defect rate, value realized).

#### Tip 51 — Apply the Decide vs Defer Matrix to every significant architecture choice
**Why it matters:** Premature decisions create rework and lock-in. Deferred decisions without resolution paths create delivery blockers. The five-factor matrix (Evidence, Reversibility, Impact, Urgency, Capability) forces disciplined timing.  
**When to apply:** Any phase. Every artifact containing A3 entries or ADR references.  
**Related concept:** Decision, Pending Architecture Decision, Architecture Decision Record.  
**How to incorporate:** In every artifact with A3 entries, add a "Phase Appropriateness" note. In ADRs, include a "Decision Timing" section. Convert premature or low-evidence decisions to PAD-NNN entries with constraint boundaries and expiry dates.

#### Tip 52 — Treat evidence as a first-class governance gate
**Why it matters:** Decisions made on assumptions rather than evidence are the primary source of architecture rework. MUST requirements should act as disqualifiers, not just evaluation criteria.  
**When to apply:** Phases A–E. ADR template, Gap Analysis, Architecture Roadmap.  
**Related concept:** Requirement, Decision, Evidence Assessment.  
**How to incorporate:** In ADR template §3b, require an Evidence Assessment table. In Gap Analysis, require Evidence Requirements per high-priority gap. In Architecture Roadmap, evidence-gate work packages.

#### Tip 53 — Document political alignment explicitly — don't hide stakeholder pressure
**Why it matters:** When decisions are driven by political pressure rather than architecture rationale, future architects cannot distinguish evidence-based choices from expedient ones. Documenting the political context preserves institutional memory.  
**When to apply:** Any phase. ADR template §5c, A3 Decision Log notes.  
**Related concept:** Stakeholder Concern, Governance, Decision.  
**How to incorporate:** In ADRs, include a "Political Alignment" section recording stakeholder pressure, governance forum review, and the defensible evidence-based position. In A3 entries, note if a decision was a fiat.

---
