# Phase Interview Question Bank

Curated interview questions for each TOGAF ADM phase, with output routing tables mapping responses to ea-assistant artifact template fields.

---

## Preliminary Phase Interview

**Goal:** Establish the Engagement Charter, Architecture Principles, and Governance Framework

**Deliverables:** Engagement Charter, Architecture Principles, Governance Framework

---

### Preliminary — Part 1: Organisation & Engagement Context

*Routes to: Engagement Charter §1 (Organisation Background), §2 (Purpose & Mandate), §3 (Scope)*

1. Describe the organisation: industry, operating model, scale, and the key aspects of the current technology landscape that are relevant to this engagement.
2. What has changed recently — strategically, competitively, or operationally — that is making this engagement necessary now?
3. Who has authorised this engagement and what is the formal mandate? (Board resolution, executive decision, regulatory directive, programme board approval)
4. How would you classify this engagement type?
   - [ ] Greenfield implementation — building new capability where none exists
   - [ ] Legacy modernisation — replacing or upgrading existing systems
   - [ ] Cloud migration — moving workloads to cloud platforms
   - [ ] Capability assessment — understanding current state before committing to direction
   - [ ] Regulatory compliance — mandated by a regulation or external body
   - [ ] Merger / acquisition integration — consolidating organisations or systems
   - [ ] Post-acquisition rationalisation — reducing duplication after a merger
   - [ ] Other: ___
5. What is explicitly in scope for this engagement? What is explicitly out of scope?
6. What assumptions are you making that, if wrong, would significantly change the scope or approach?
7. What constraints apply to this engagement? (select all that apply)
   - [ ] Regulatory — compliance obligations, legal requirements, data residency rules
   - [ ] Financial — budget cap or envelope
   - [ ] Technical — existing platform lock-in, skills gap, mandated standards
   - [ ] Organisational — headcount limits, change capacity, political constraints
   - [ ] Time — fixed deadline, regulatory timeline, or programme dependency
   - [ ] Other: ___

---

### Preliminary — Part 2: Relationships & Affected Organisations

*Routes to: Engagement Charter §4 (Related Engagements), §5 (Organisations Affected)*

8. What other programmes or projects is this engagement related to — as a predecessor, successor, or peer? What does this engagement depend on from them, and what do they depend on from this engagement?
9. Which internal divisions or business units will be significantly affected by this engagement?
10. Which external organisations — customers, partners, suppliers, regulators — are affected?
11. Are there regulatory or compliance bodies whose requirements this engagement must satisfy?

---

### Preliminary — Part 3: Motivation Framework

*Routes to: Engagement Charter §6, engagement.json → direction (rendered in the motivation registers), Architecture Vision §4–§5/§7–§8/§10 summaries*

12. What external forces (market shifts, regulatory changes, competitive pressure, technology change) are creating pressure to act now? Assign each a DRV-NNN ID.
13. What internal forces (cost pressure, strategic mandate, leadership change, capability gap) are pushing this engagement forward? Assign each a DRV-NNN ID.
   - For each driver: what evidence, event, or data point confirms this is real pressure on the organisation right now? Note the source (report, incident, regulatory instrument, stakeholder statement). A driver without a verifiable source is an assumption — flag it.
14. Given those drivers, what are the high-level outcomes this engagement must achieve? Capture each as a goal (G-NNN) — a qualitative statement of a desired future state.
15. For each goal: what specific, measurable result would prove this goal is being achieved, and by when? Capture each as an objective (OBJ-NNN) with a measure and deadline.
16. How does the organisation intend to achieve its goals? Capture the key approaches as strategies (STR-NNN), each linked to the goals it supports.
17. What is currently getting in the way? Capture strategic threats as issues (ISS-NNN, linked to goals) and operational blockers as problems (PRB-NNN, linked to objectives).

---

### Preliminary — Part 4: Programme Structure

*Routes to: Engagement Charter §7 (Programme Structure)*

18. How is this engagement structured as a programme? What major phases of delivery do you anticipate?
   - Common phase types: Planning, Preparation, Procurement, Pilot, Implementation (one or more waves), Post-Implementation / Benefits Realisation
   - Not all types are required — phases may be merged or omitted
19. For each programme phase: what are the key deliverables, linked goals, estimated duration, and prerequisites?
20. What is driving the phasing decision? (e.g. regulatory deadline, risk management, change capacity, budget approval cycles, technology dependencies)

---

### Preliminary — Part 5: Outcomes, Benefits, Costs & Risks

*Routes to: Engagement Charter §8 (Outcomes), §9 (Benefits), §10 (Costs), §11 (Risk Profile)*

21. When this engagement is complete, what will be different? Describe the outputs (what will be delivered), outcomes (how the organisation will operate differently), and impacts (strategic effects).
22. What financial benefits do you expect? (cost reduction, cost avoidance, revenue growth, efficiency gains — quantify where possible)
23. What non-financial benefits do you expect? (risk reduction, compliance, capability, resilience, customer experience)
24. What is the budget envelope for this engagement? What are the major cost categories?
25. What are the top risks to this engagement succeeding? For each: what is the likelihood, impact, and proposed mitigation?
26. What level of residual risk is the sponsor willing to accept? Under what circumstances would the engagement be paused or stopped?

---

### Preliminary — Part 6: Governance & Principles

*Routes to: Architecture Principles, Governance Framework*

27. Who are the key decision-makers for IT investment in your organisation?
28. Does an existing architecture governance body or process exist? If so, how does it operate?
29. What are the top three strategic goals for your organisation over the next three years?
30. What does good architecture practice look like in your organisation?
31. What existing frameworks, standards, or methodologies does the organisation follow?
32. How would you describe your organisation's risk appetite for technology change?

---

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Organisation profile | Engagement Charter | `§1.1 Organisation Profile` |
| History & context | Engagement Charter | `§1.2 Relevant History & Context` |
| Engagement purpose & mandate | Engagement Charter | `§2 Purpose & Mandate` |
| Engagement type | Engagement Charter | `§2.2 Mandate` + `engagement.json → engagementType` |
| Scope in/out | Engagement Charter | `§3 Scope & Boundaries` |
| Assumptions | Engagement Charter | `§3.4 Assumptions` |
| Constraints | Engagement Charter / Constraints Register | `§3.5 Constraints` + `CST-NNN` entries via `/ea-constraints` |
| Related engagements | Engagement Charter | `§4` |
| Organisations affected | Engagement Charter | `§5` |
| Business drivers (DRV-NNN) | Engagement Charter `§6.2` + Architecture Vision `§4` + `engagement.json → direction.drivers` | — |
| Goals (G-NNN) | Engagement Charter `§6.3` + Architecture Vision `§5` + `engagement.json → direction.goals` | — |
| Objectives (OBJ-NNN) | Engagement Charter `§6.4` + Architecture Vision `§10` + `engagement.json → direction.objectives` | — |
| Strategies (STR-NNN) | Engagement Charter `§6.5` + Architecture Vision `§11` + `engagement.json → direction.strategies` | — |
| Issues / Problems | Engagement Charter `§6.6` + Architecture Vision `§7` + `§8` | — |
| Programme structure | Engagement Charter | `§7 Programme Structure` |
| Expected outcomes | Engagement Charter | `§8` |
| Benefits | Engagement Charter | `§9` |
| Costs | Engagement Charter | `§10` |
| Risk profile | Engagement Charter `§11` + Risk Register (via `/ea-risks`) | — |
| Key stakeholders | Engagement Charter `§12` + Stakeholder Map `{{stakeholder_table}}` | — |
| IT decision-makers | Architecture Principles | `{{existing_governance}}` |
| Strategic goals (principles context) | Architecture Principles | `{{strategic_goals}}` |
| Good architecture definition | Architecture Principles | `{{architecture_definition}}` |
| Existing frameworks/standards | Architecture Principles | `{{existing_frameworks}}` |
| Risk appetite | Architecture Principles | `{{risk_appetite}}` |
| Governance body | Governance Framework | `§3 Governance Structure` |

**Facilitation Notes:**
- Run the context and motivation questions (Parts 1–3) as a structured workshop with senior leadership and the sponsor — competing priorities and scope disagreements surface quickly in a group setting.
- Run the programme structure and risk questions (Parts 4–5) with the programme director and key delivery leads.
- Run the governance and principles questions (Part 6) with the EA team, CTO/CIO, and ARB members.
- Ask for written documentation of existing principles, strategies, or standards before the session — gaps between stated and documented practice are significant findings.
- If no governance body exists, note this as a gap and flag it as a deliverable (Governance Framework) rather than leaving it unaddressed.
- The motivation framework (Part 3) produces IDs used in all subsequent artifacts — agree them in this session and record in engagement.json before moving to Phase A.
- Dual-route all DRV/G/OBJ/STR/ISS/PRB responses: write to the Engagement Charter AND to engagement.json → direction simultaneously.

**§D Diagrams — ask at close of session:**
> "Two standard diagrams help communicate the engagement scope and structure. Would you like to create either of these now, or describe what they should show?"
- **Context Diagram** — engagement boundary, key external organisations and relationships (`engagement-charter-context.mmd`)
- **Organisation Chart** — structure and units in scope (`engagement-charter-org-chart.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filename added to Engagement Charter frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for the Preliminary Phase? (y/n)"

**SABSA focus:** Contextual — governance, obligations, and existing security posture

1. What security governance model applies to this organisation? (e.g., CISO-led, committee-based, outsourced)
2. Who holds security decision authority — who can approve exceptions, set policy, and sign off on architecture security sections?
3. What security policies already exist? Are they current and enforced?
4. What compliance obligations apply? (e.g., GDPR, PCI-DSS, ISO 27001, HIPAA, sector regulation)
5. Is there an existing ISMS or security programme this engagement must align with?
6. What is the current security maturity tier? (NIST CSF: Partial / Risk Informed / Repeatable / Adaptive)

**Output routing:**
| Answer | Output |
|---|---|
| Governance model and decision authority | Architecture Principles (security governance section) |
| Existing policies and compliance obligations | Governance Framework (security notes), DRV-NNN type:security |
| Current maturity tier | Architecture Vision (security baseline section) |

### Decision Quality Questions
> Ask these after completing the standard Preliminary Phase questions. They probe whether decisions are being made at the right time with sufficient evidence.

1. **[DECISION]** Which decisions must be made in the Preliminary Phase, and which should be deferred to later phases? (Principles should be decided now; technology choices should not.)
2. **[DECISION]** Are the architecture principles evidence-based — grounded in known constraints, regulatory requirements, or proven practice — or are they aspirational statements?
3. **[DECISION]** Is there strong pressure to make specific technology or vendor commitments before Phase A? If so, how will you handle it? (Convert to PAD-NNN with constraint boundaries.)
4. **[DECISION]** What evidence would change the principles you've defined? If none, the principles are assumptions — flag them.

---

## Phase A — Architecture Vision Interview

**Goal:** Define scope, concerns, high-level target, and cross-domain goals

**ID Scheme Reference:**

| Prefix | Concept | Example | Linked To |
|---|---|---|---|
| DRV-NNN | Business Driver | DRV-001 | — (root cause of engagement) |
| G-NNN | Goal | G-001 | DRV-NNN (responds to driver) |
| OBJ-NNN | Objective | OBJ-001 | G-NNN (operationalises goal) |
| ISS-NNN | Issue | ISS-001 | G-NNN (threatens goal) |
| PRB-NNN | Problem | PRB-001 | OBJ-NNN (blocks objective) |
| STR-NNN | Strategy | STR-001 | G-NNN (approach to achieve goal) |
| MET-NNN | Metric | MET-001 | OBJ-NNN (measures objective) |
| OPP-NNN | Opportunity | OPP-001 | DRV-NNN + G-NNN (specific possibility to exploit) |

Assign IDs sequentially within each prefix as responses are confirmed. Record IDs in the Architecture Vision template and in `engagement.json` where applicable.

**Key questions:**

*§2 Business Drivers — the forces making this engagement necessary:*
1. What external forces (market shifts, regulatory changes, competitive pressure, technology change) are creating pressure to act now?
2. What internal forces (cost pressure, strategic mandate, leadership change, capability gap) are pushing this engagement forward?
3. For each driver: is it an opportunity to exploit, a threat to respond to, or a mandate to comply with?

*§3 Goals — the broad outcomes the strategy must achieve:*
4. Given those drivers, what are the high-level outcomes this engagement must achieve? Capture each as a goal: a qualitative statement of a desired future state — no numbers or deadlines required at this level. (e.g. "Become a trusted custodian of customer data", "Achieve highly reliable platform operations")
   - If a response includes a specific number or deadline, it is an **Objective** — note it and handle in the next step.
   - If it describes an approach ("adopt cloud-first"), it is a **Strategy** — note it and record separately.
   - **Layer test:** If the stated goal is about governance, standards, or EA capability (e.g., "Establish AI governance", "Define architecture review process"), it is likely an **EA Goal** — capture it separately for the Governance Framework or Architecture Principles, not as a Business Goal in the Architecture Vision. See `ea-concepts.md` → **Two Layers of Intent**.
   - Assign each confirmed goal a G-NNN ID and note which driver(s) it responds to.
   - For each goal: in one sentence, why is achieving it important for this engagement specifically? What happens if it is not achieved? (This is the goal's Rationale — captures the consequence of failure.)

*§4 Objectives — the measurable, time-bound results that operationalise each goal:*
5. For each goal captured: what is the specific, measurable result that would prove this goal is being achieved — and by when? (e.g. for "Achieve highly reliable platform operations" → "Reduce unplanned downtime to under 4 hours per quarter by Q4 2026")
   - Each objective must have: a unit of measure, a target value, and a deadline. Push back on any that lack all three.
   - Assign each confirmed objective an OBJ-NNN ID and link it to its parent goal.
6. For each objective: how will you measure progress? What is the current baseline, and where does the data come from? Capture as a performance metric linked to the objective.
   - For goals without a single measure, ask for a leading indicator — capture as an outcome metric.

*§5 Issues — the systemic barriers that threaten goals:*
7. For each goal: what broader, systemic concerns are currently preventing or threatening its achievement? (Patterns of dysfunction, capability gaps, unresolved conflicts — not single broken things.) (e.g. "Weak stakeholder alignment across business units", "Inconsistent data quality across operational systems")
   - Assign each confirmed issue an ISS-NNN ID and link it to the goal(s) it threatens.
   - If a response is too specific and fixable ("error rate is 30%"), it is a **Problem** — note it and handle in the next step.
   - For each issue: what observable signal or event confirms this issue exists? Who raised or first identified it? (Evidence and source — an issue without evidence is an assumption.)

*§6 Problems — the specific, observable symptoms that block objectives:*
8. For each objective: what specific, measurable symptoms are actively blocking or undermining its delivery today? (e.g. "The monthly close process takes 15 days due to manual reconciliation", "Mobile checkout abandonment is 68% — 2× the industry benchmark")
   - Assign each confirmed problem a PRB-NNN ID and link it to the objective(s) it blocks.
   - If a response is too broad and unfixable directly ("we have poor data culture"), it is an **Issue** — move it up.
   - For each problem: what data point, incident, or measurement confirms this symptom is currently active? Who raised or first identified it? (Evidence and source — a problem without evidence cannot be prioritised or verified later.)

*Inter-element connections — run after Issues and Problems are captured:*
> **After Issues:** "Do any of these issues, if resolved, unlock something the organisation could not do before — beyond just removing the barrier? If so, that's an Opportunity — capture it as OPP-NNN."
> **After Problems:** "Does each problem link clearly to an objective it's blocking? Could resolving any of them create a new capability or market possibility worth tracking as an Opportunity?"

*§7 Opportunities — specific, actionable possibilities to exploit:*
9. Given the drivers, goals, and gaps identified: what specific things could this engagement make possible that the organisation cannot currently do? (e.g. "Real-time personalisation using our existing data platform", "Self-service supplier onboarding — currently takes 3 weeks manually")
   - Classify each as: **Exploit** (capitalise on existing advantage), **Enhance** (amplify current capability), or **Emerge** (something not previously in scope).
   - Assign each confirmed opportunity an OPP-NNN ID and link it to the driver(s) and goal(s) it advances.
   - An opportunity must advance at least one goal. If it advances no goal, either a goal is missing or the item is not architecture-relevant.

*Inter-element connections — run after Risks are captured (§15 Key Risks):*
> **After Risks:** "For each Critical or High risk — which goal does it threaten? Link it now (G-NNN). And: does this risk also suggest a defensive opportunity worth capturing as OPP-NNN?"
> **After Metrics:** "For each metric — what is the current baseline? If unknown, flag it as a data gap. An unmeasured baseline is itself a benefits realisation risk."

*§1 Executive Summary / §9 Scope / §10–§16 — scope, constraints, and risks:*
10. What does success look like at the end of this engagement? → §1 Executive Summary
11. Who are the key stakeholders and what are their primary concerns? → §10 Stakeholders + Stakeholder Map
12. What is explicitly in scope and out of scope for this engagement? → §9 Scope
13. What known constraints or assumptions should be documented upfront? → §12 Constraints + §13 Assumptions
14. What existing architecture assets, decisions, or documents are relevant? → Statement of Architecture Work §3
15. What is the desired timeline for completing this work? → §9 Scope (Time Horizon) + SoAW
16. What are the biggest risks that could derail this engagement? → §15 Key Risks

### Decision Quality Questions
> Ask these after completing the standard Phase A questions. Phase A is for directional choices only — any specific technology or pattern commitment is premature.

1. **[DECISION]** Have any specific technology choices, vendor selections, or implementation patterns been proposed in this phase? If yes, flag as premature and convert to PAD-NNN with constraint boundaries.
2. **[DECISION]** For each strategy (STR-NNN): what evidence would be required before it can be treated as a committed decision rather than a directional hypothesis?
3. **[DECISION]** Is there stakeholder pressure to make specific technology commitments now? What is the defensible governance position if challenged?
4. **[DECISION]** Which decisions made in Phase A should be revisited after Phase B–D analysis? (All technology-specific choices; directional strategies with weak evidence.)

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| External business drivers | Drivers Register (+ engagement.json) | `direction.drivers[]`; Vision §4 summary |
| Internal business drivers | Drivers Register (+ engagement.json) | `direction.drivers[]`; Vision §4 summary |
| Goals | Goals Register + engagement.json | `direction.goals[]`; Vision §5 summary |
| Objectives | Objectives Register + engagement.json | `direction.objectives[]`; Vision §10 summary |
| Systemic issues | Issues Register (+ engagement.json) | `direction.issues[]`; Vision §7 summary |
| Specific problems | Problems Register (+ engagement.json) | `direction.problems[]`; Vision §8 summary |
| Opportunities | Architecture Vision | `§9 Opportunities` (OPP-NNN rows) |
| Performance metrics | engagement.json | `metrics[]` linked to OBJ-NNN |
| Success criteria | Architecture Vision | `§1 Executive Summary` + `§5 Goals` |
| Key stakeholders | Stakeholder Map | `{{stakeholder_list}}` |
| Stakeholder concerns | Stakeholder Map | `{{stakeholder_concerns}}` |
| Strategies | Strategy Register + engagement.json | `direction.strategies[]`; Vision §11 summary |
| Metrics | engagement.json | `§11 Strategic Direction Summary` (MET-NNN rows) + `metrics[]` |
| In-scope items | Architecture Vision | `§2 Scope — {{scope_in}}` |
| Out-of-scope items | Architecture Vision | `§2 Scope — {{scope_out}}` |
| Constraints | Statement of Architecture Work / Constraints Register | `{{constraints}}` + `CST-NNN` via `/ea-constraints` |
| Assumptions | Statement of Architecture Work | `{{assumptions}}` |
| Existing architecture assets | Statement of Architecture Work | `§3 Approach` (reference existing assets as inputs) |
| Timeline | Statement of Architecture Work | `{{timeline}}` |
| Key risks | Architecture Vision | `§16 Key Risks` (summary; full detail in Risk Register) |
| Strategies | engagement.json | `direction.strategies[]` |

**Facilitation Notes:**
- Follow the sequence: Drivers → Goals → Objectives → Issues → Problems. Each layer is easier to articulate once the layer above is established.
- Goals come before objectives. Do not ask for measures until you have a confirmed, classified goal — premature measurement pressure collapses goals into objectives and loses the qualitative anchor.
- When classifying responses: numbers or deadlines → Objective; approaches or choices → Strategy; broad dysfunction → Issue; specific observable symptom → Problem. Reclassify explicitly and confirm with the stakeholder before recording.
- For every Issue, ask "which goal does this threaten?" — if it threatens no goal, either the goal list is incomplete or the issue is not architecture-relevant.
- For every Problem, ask "which objective does this block?" — if it blocks no objective, either the objectives list is incomplete or the problem is out of scope.
- Scope boundary questions often generate the most debate; document disagreements explicitly rather than forcing premature consensus.
- A brief stakeholder RACI draft during this session prevents scope and accountability conflicts later.
- If a driver, issue, or problem needs external validation or deeper investigation, pause and invoke `@research-agent` before recording it as fact. Example: "I'll check the regulatory landscape on that before we lock in DRV-002." Research findings can be pasted directly into brainstorm notes or artifact fields.

**§D Diagrams — ask at close of session:**
> "Two diagrams can make the Architecture Vision immediately clearer for executive stakeholders. Would you like to create either now, or describe what they should show?"
- **Motivation Map** — shows the full DRV → Goal → Strategy chain in one visual (`architecture-vision-motivation-map.mmd`)
- **Stakeholder Power/Interest Grid** — positions each stakeholder by influence and engagement level (`architecture-vision-stakeholder-grid.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Architecture Vision frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase A? (y/n)"

**SABSA focus:** Contextual — security vision, drivers, and top-level risk

1. What are the primary security drivers for this engagement? Are they regulatory, contractual, or risk-driven?
2. Who are the security stakeholders? (CISO, DPO, compliance officer, risk committee, board audit committee)
3. What are the top 3 security risks at the engagement level? What keeps the CISO awake at night?
4. What security principles should constrain all downstream architecture decisions?
5. Is there an existing security architecture or security reference model that this engagement must align with?
6. Are there any known security incidents or breaches in this organisation's recent history that should inform the architecture?

**Output routing:**
| Answer | Output |
|---|---|
| Security drivers | DRV-NNN type:security in Requirements Register |
| Security stakeholders | Stakeholder Map (security authority roles) |
| Top-level security risks | RIS-NNN type:security, category:security in Risk Register |
| Security principles | Architecture Principles (security section) |

---

## Phase B — Business Architecture Interview

**Goal:** Define business capabilities, processes, gaps, and business goals

**Key questions:**
1. What are the primary business functions performed by the organisation or the area in scope?
2. Walk me through the key end-to-end business processes — from customer/trigger to outcome.

   *2a. For each key process: walk me through the steps.*
   - Who performs each step (actor / role / system)?
   - Which application or system is used at each step?
   - Where are the key decision points or business rules applied?
   - What are the named exception paths — what can go wrong, and what happens next?
   - Is there an SLA or performance expectation for this process end-to-end?

   *2b. For each process: which value stream (from Q3a) is it part of, and which capabilities does it exercise?*
   (This builds the capability-to-process cross-reference that links §4 Processes to §3 Capabilities.)

3. Where are the biggest pain points or inefficiencies in current business operations?

3a. What are the end-to-end chains of activity that deliver value to your key stakeholders or customers?
   - For each value stream: what is the trigger that starts it, what is the end outcome the stakeholder receives, and who benefits?
   - Which value streams are most critical to the organisation's strategic goals (G-NNN)?
   - Assign each a VS-NNN ID.

   *3b. For each value stream: which business capabilities are exercised along the path?*
   - Are there steps in the value stream where no existing capability covers the need?
   - Flag any uncovered steps as capability gaps — these will become GAP-NNN entries.

4. Let's build the capability model systematically — this is the core Phase B deliverable. Capabilities are mastered in the Business Architecture capability table and managed with **`/ea-capabilities`** (which can also seed from the Architecture Repository's canonical capability map via `adopt`). A capability is an *ability to achieve an outcome* — a noun ("Order Management"), not a process ("Process Orders").

   a. **Level 1 — Domains:** What are the major capability domains relevant to this engagement?
      (e.g. Customer Management, Operations, Finance, Technology, Compliance — agree 4–8 domains)
      Assign each a CAP-NNN ID starting at CAP-001.

   b. **Level 2 — Capabilities:** For each domain, what specific capabilities must the organisation have to deliver value in that domain?
      Assign sequential CAP-NNN IDs continuing from the L1 IDs.

   c. **Level 3 — Sub-capabilities:** For any L2 capability where detail matters for gap analysis, what sub-capabilities exist beneath it?
      Only elicit L3 where there is a known gap or a Phase B deliverable that requires it.

   c2. **Value / Outcome:** For each capability, what business outcome does it enable — the value of being able to do it? ("What do we gain by being able to do this?") A capability with no articulated value and no strategic anchor is **capability inflation** — flag it for removal or as commodity overhead. Distinguish **differentiating** capabilities (where you compete — invest) from **commodity** ones (table stakes — make efficient). Recorded in the Value / Outcome column.

   d. **Maturity Assessment:** For each L2 and L3 capability, rate the current maturity:
      - **Absent** — this capability does not exist today
      - **Immature** — exists but ad hoc, inconsistent, or person-dependent
      - **Developing** — repeatable and documented but not optimised
      - **Mature** — optimised, governed, and performing well

   e. **Target Maturity:** What maturity level does each capability need to reach to support the engagement's strategies and goals?

   f. **Strategic Alignment:** Which STR-NNN or G-NNN does each capability support?
      Any capability with no strategic anchor should be flagged for removal or reclassification.

4a. Who are the primary actors that interact with this business domain?
    (Actors are roles, not individuals — examples: Customer, Supplier, Finance Officer, External Regulator, Internal System)

4b. For each actor: what are the 3–5 most important things they need to accomplish in this domain?
    - Capture each as a use case: "{Actor} needs to {goal}" — e.g. "Customer needs to submit a warranty claim"
    - **Layer test:** If the use case subject is "how we govern" or "how we standardize" (e.g., "Define governance process for AI projects") rather than "what the actor needs" (e.g., "Auto-triage cases with AI"), it is an **EA Capability Use Case** — route it to the Governance Framework or Architecture Principles, not the Business Architecture Use Case Catalog.
    - Assign each a UC-NNN ID sequentially.

4c. For each use case: what triggers it, what must be true before it starts (preconditions), and what does success look like for the actor?
    - Summarise the main success scenario in one sentence — the normal path from trigger to outcome.
    - Are there named alternate paths or exception scenarios worth noting at architecture level?

4d. For each use case: which capabilities (CAP-NNN) must the business have to support it?
    - Any use case where no existing capability covers the need is a capability gap — flag it in §7 Gap Analysis.
    - Link each UC-NNN to the value stream (VS-NNN) it contributes to.

5. How is the organisation structured — what divisions, teams, or geographies are involved?
6. What are the priority business outcomes this architecture must support?
7. What does the business need to look like in three to five years?
8. How is performance measured today — what KPIs or metrics matter most?
9. *(If Business direction not yet defined or needs refinement)* Let's capture Business direction. Remind the user of the distinction:
   - **Goal** = where the business wants to be (qualitative; no number required)
   - **Objective** = how far and by when (must have a measure, a target, and a deadline)
   - **Strategy** = how you'll get there (a chosen approach, not an outcome)

   Ask for goals first, then objectives for each goal, then strategies. If a response has a target number or deadline, classify it as an objective. If it describes an approach (e.g. "use agile delivery"), classify it as a strategy.
10. For each Business objective captured, ask: "How will you measure this — what is the unit of measure, and where does the data come from? What is the current baseline?" Capture as a `performance` metric (`BM-`) linked to the objective. For goals, ask for a leading indicator — capture as an `outcome` metric. For strategies, ask for an activity measure — capture as an `activity` metric.

### Decision Quality Questions
> Ask these after completing the standard Phase B questions. Phase B is where capability gaps are identified — decisions on how to close them should be evidence-based.

1. **[DECISION]** For each capability gap identified: what POC, benchmark, or reference implementation is required before committing to a closure approach?
2. **[DECISION]** When a make-vs-buy or build-vs-configure choice is proposed, what evidence supports each option? Has a weighted scorecard been applied?
3. **[DECISION]** What optionality is preserved in the target capability model? If a vendor or pattern is chosen, how hard is it to reverse or swap later?
4. **[DECISION]** Are any decisions being made under strong stakeholder pressure? What is the defensible evidence-based position?
5. **[DECISION]** Which capability gaps should be logged as PAD-NNN rather than committed decisions? (Gaps with weak evidence, high reversibility cost, or unclear impact.)

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Primary business functions | Business Architecture | `{{business_functions}}` |
| Key end-to-end processes | Business Architecture | `§4 Business Processes` |
| Process steps, actors, systems, decisions | Business Architecture | `§4 Business Processes — Steps table` |
| Process exceptions | Business Architecture | `§4 Business Processes — Exceptions` |
| Process SLA / performance | Business Architecture | `§4 Business Processes — SLA / Performance` |
| Pain points/inefficiencies | Gap Analysis | `{{current_state_gaps}}` |
| Value streams (VS-NNN) | Business Architecture | `§3a Value Streams` |
| Capability-to-value-stream linkage | Business Architecture | `§3a Key Capabilities column` + `§3 Supports column` |
| Capability domains (L1, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L1) |
| Capabilities (L2, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L2) |
| Sub-capabilities (L3, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L3) |
| Capability maturity assessments | Business Architecture + Gap Analysis | `§3` maturity columns + `§7 Gap Analysis` |
| Capability-to-strategy links | Business Architecture | `Supports (STR-NNN / G-NNN)` column |
| Actors | Business Architecture | `§4a Use Case Catalog — Primary Actor` |
| Use cases (UC-NNN) | Business Architecture | `§4a Use Case Catalog` |
| Use case capability linkage | Business Architecture | `§4a Capabilities Used (CAP-NNN)` |
| Use case value stream linkage | Business Architecture | `§4a` → `§3a VS-NNN` cross-reference |
| Gap Analysis | Gap Analysis | `{{business_gaps}}` |
| Organisation structure | Business Architecture | `{{org_structure}}` |
| Priority business outcomes | Business Architecture | `{{business_outcomes}}` |
| Future state description | Business Architecture | `{{future_state}}` |
| KPIs and metrics | Business Architecture | `{{performance_metrics}}` |
| Business direction (goals, objectives, strategies) | engagement.json + Business Capability Map | `direction.Business` + `{{business_direction}}` |
| Business metrics | engagement.json + Business Capability Map | `metrics.Business` + `{{business_metrics}}` |

**Facilitation Notes:**
- Recommended sequence: value streams (Q3a) → capability model (Q4) → process decomposition (Q2a) → use cases (Q4a). Value streams provide the organising context before drilling into capability and process detail.
- Work top-down on capabilities: agree L1 domains first (with the group), then populate L2 capabilities for the domains most relevant to the engagement scope. Don't attempt to enumerate all L3 sub-capabilities — only go to L3 where there is a known gap or a Phase B deliverable that requires it.
- Run a capability mapping workshop using a whiteboard or collaborative tool — asking participants to place capabilities on a heat map (invest/maintain/retire) surfaces priorities faster than questions alone.
- Process walk-throughs are best done with operational staff, not just managers; the "how it actually works" often differs significantly from the "how it should work" described by leadership. The Steps table in §4 is most accurately populated in a session with process owners, not IT leadership.
- Decision / business rule capture (Q2a) frequently surfaces where compliance, exception handling, and system complexity live — these become inputs to application architecture component design.
- Use case elicitation (Q4a) works well after the capability model is agreed — actors often emerge naturally from capability discussions ("who uses this capability?").
- When identifying gaps, ask "what would you do if you had no constraints?" to surface aspirational capabilities before applying reality checks.
- Every L2/L3 capability where Current Maturity < Target Maturity is a Capability Gap — ensure it appears in the Gap Analysis Capability Gap Register with a Prevents (G-NNN/OBJ-NNN) link.
- Every use case with no covering capability is also a Capability Gap — flag it immediately in §7.
- The KPIs question links business architecture to measurable outcomes — use answers to define gap analysis criteria.

**§D Diagrams — ask at close of session:**
> "Four diagrams are standard for the Business Architecture. Which would you like to create or describe now?"
- **Capability Map** — hierarchical heat map of business capabilities with maturity colouring (`business-architecture-capability-map.mmd`)
- **Value Stream Map** — end-to-end chains of activity with capability overlays (`business-architecture-value-stream.mmd`)
- **Business Process Flow** — swimlane for the most critical end-to-end process (`business-architecture-process-flow.mmd`)
- **Organisation Map** — structure and roles in scope (`business-architecture-org-map.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Business Architecture frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase B? (y/n)"

**SABSA focus:** Conceptual — security policies, business security attributes, organisational model

1. What are the business security attributes required? (confidentiality, integrity, availability, auditability, accountability, non-repudiation — which matter most and why?)
2. What security policies govern this business domain? Are they documented and enforced?
3. How are security roles and responsibilities organised? Is there a clear RACI for security decisions?
4. What are the security-sensitive business processes — processes where a failure would cause regulatory, financial, or reputational harm?
5. What third-party or supply chain relationships introduce security risk?

**Output routing:**
| Answer | Output |
|---|---|
| Business security attributes | Business Architecture (security section), REQ-NNN type:security, source:business policy |
| Security roles and RACI | Business Architecture (security RACI), Governance Framework |
| Security-sensitive processes | Business Architecture (process security notes), RIS-NNN |

---

## Phase B — Operating Model Interview

**Goal:** Design the execution system that will run the Business Architecture day after day — organisation, roles, decision rights, controls, processes, workforce, sourcing, technology enablement, and performance management.

**When to run:** Run this interview after the Business Architecture capability/value-stream model is at least draft-stable. The OM executes the blueprint; designing it before the BA is stable risks an operating model that does not deliver the target capabilities.

**Key questions:**

### Operating Model Context
*Routes to: Operating Model §1*

1. What is the scope of this Operating Model — enterprise-wide, divisional, programme-level, or for a specific value stream?
2. Which Business Architecture capabilities (CAP-NNN) and value streams (VS-NNN) does this OM need to operationalise? Link each OM section back to at least one CAP-NNN or VS-NNN.
3. What Business Model Canvas changes (new segments, channels, revenue streams, partnerships) drive changes in how the organisation must operate?

### Organisation Design
*Routes to: Operating Model §2*

4. What operating units, teams, or forums are needed to deliver the target capabilities? Do not reproduce the whole enterprise org chart — focus on the operating structure required by this architecture.
5. For each operating unit: what capabilities (CAP-NNN) and value streams (VS-NNN) does it support?
6. How does the target operating structure differ from today's organisation? What units are new, merged, or retired?

### Roles, Decision Rights & Accountability
*Routes to: Operating Model §3*

7. For the key decisions this OM must make (e.g. pricing exceptions, capacity allocation, vendor selection, risk acceptance, hiring): who is accountable, who is consulted, who is informed, and what is the escalation path?
8. Which business operating roles are required that do not exist today? How do they differ from EA engagement roles (ROLE-NNN, managed via `/ea-roles`)?
9. Where are decision rights unclear or contested today? How will the OM resolve them?

### Governance, Controls & SLAs
*Routes to: Operating Model §4*

10. What business controls, checkpoints, or service-level expectations keep the operating model on track? (e.g. monthly capacity review, fraud control, customer complaint SLA)
11. Which policies (POL-NNN), constraints (CST-NNN), or business rules (BR-NNN) apply to each control?
12. Which controls are proportionate to risk, and which are overhead that should be challenged or removed?

### Business Processes Execution Model
*Routes to: Operating Model §5 + Business Processes Register*

13. Which end-to-end business processes are critical to this OM? For each: what value stream (VS-NNN) and capabilities (CAP-NNN) does it serve?
14. For each critical process: what is its OM role — core, supporting, exception handling, governance? Which operating role owns it?
15. Are the detailed process steps already captured as PROC-NNN entries, or do they need to be created via `/ea-processes add`?
16. Where do processes hand off across operating units, channels, or partners? What integration or orchestration is required?

### Workforce, Locations & Channels
*Routes to: Operating Model §6*

17. What skills, headcount, or workforce mix changes are needed to operate the target model?
18. Which locations, regions, or sites are in scope? Will the target state centralise, distribute, or regionalise work?
19. What delivery channels (digital, physical, partner, self-service) does this OM use? Link each to the relevant business service (SVC-NNN) and value stream (VS-NNN).
20. What are the implications of workforce/location/channel choices for capabilities and processes?

### Sourcing & Partnership Model
*Routes to: Operating Model §7*

21. For each capability or service in scope: is it made internally, bought via COTS/SaaS, or delivered through a partner/shared-service arrangement?
22. Who are the strategic vendors, outsourcers, or ecosystem partners? Link to Vendor Landscape (VDR-NNN) entries where applicable.
23. What make-vs-buy or partner decisions are hard to reverse, high cost, or contested? Flag these for ADR-NNN capture.

### Information & Technology Enablement
*Routes to: Operating Model §8*

24. At a business level, what data, applications, or technology are essential to enable this OM? Do not design Phase C/D detail here — just identify the enabling dependencies.
25. For each enabling dependency: which Phase C/D artifact will contain the detailed design (Data Architecture, Application Architecture, Technology Architecture)?
26. What technology constraints (existing platforms, mandated standards, skills gaps) shape the OM design?

### Performance Management
*Routes to: Operating Model §9 + engagement.json → metrics*

27. How will the OM be measured? Identify metrics (MET-NNN) for capability performance, process performance, customer outcomes, and financial impact.
28. For each metric: what is the target, the review cadence, and the accountable owner?
29. How do these metrics close the loop back to goals (G-NNN), objectives (OBJ-NNN), and strategies (STR-NNN)?

### Gap Analysis
*Routes to: Operating Model §10 + Gap Analysis*

30. What gaps exist in the target operating model relative to current operations? (organisation, process, control, workforce, sourcing, enablement, performance)
31. Which of these are OM gaps (how work is run) versus capability gaps (what the business can do)? Route capability gaps to the Business Architecture / Gap Analysis; keep OM gaps here.
32. Link each OM gap to a GAP-NNN entry.

### Decision Quality Questions
> Ask these after completing the standard Operating Model questions. Operating Model decisions are often organisationally and politically charged — evidence and accountability matter.

1. **[DECISION]** For each new operating unit or role: what evidence supports the design — volume, capability coverage, decision load, or risk exposure?
2. **[DECISION]** For each sourcing choice (make/buy/partner): what evidence supports the option, and what would change the decision?
3. **[DECISION]** Which decisions in this OM are hard to reverse (org design, outsourcing, location strategy)? Have they been captured as ADR-NNN or PAD-NNN?
4. **[DECISION]** Where decision rights are contested, what is the defensible, governance-backed position?
5. **[DECISION]** How will the OM be validated before full rollout — pilot, simulation, staged cutover, or other test?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| OM scope and context | Operating Model | `§1 Operating Model Context — {{operating_model_context}}` |
| BA links (CAP-NNN / VS-NNN) | Operating Model | §1–§7 traceability fields |
| Business-model drivers | Operating Model | `§1` + Business Model Canvas link |
| Operating units / forums | Operating Model | `§2 Organisation Design — {{organisation_design}}` |
| Unit-to-capability/value-stream links | Operating Model | `§2` table |
| Target org changes | Operating Model / Gap Analysis | `§2` + GAP-NNN entries |
| Decision / accountability matrix | Operating Model | `§3 Roles, Decision Rights & Accountability` |
| New business operating roles | Operating Model | `§3` + Role Catalogue note |
| Governance controls / SLAs | Operating Model | `§4 Governance, Controls & SLAs` |
| Linked policies / rules / constraints | Operating Model / registers | `§4` + POL/CST/BR-NNN |
| Critical process list and OM role | Operating Model | `§5 Business Processes Execution Model` |
| Process ownership and handoffs | Operating Model + Business Processes Register | `§5` + PROC-NNN owner/scope |
| Workforce / skills changes | Operating Model | `§6 Workforce, Locations & Channels` |
| Locations / channels | Operating Model + Business Services Register | `§6` + `deliveryChannel` on SVC-NNN |
| Sourcing choices | Operating Model | `§7 Sourcing & Partnership Model` |
| Strategic vendors / partners | Operating Model + Vendor Landscape | `§7` + VDR-NNN |
| Hard-to-reverse sourcing decisions | ADR Register | ADR-NNN via `/ea-adrs new` |
| Information / tech enablement dependencies | Operating Model | `§8 Information & Technology Enablement` |
| Performance metrics | Operating Model + engagement.json | `§9 Performance Management` + `metrics[]` |
| OM gaps | Gap Analysis + Operating Model | `§10 Gap Analysis` + GAP-NNN |
| Requirements emerging from OM | Requirements Register | REQ-NNN via `/ea-requirements add` |

**Facilitation Notes:**
- Run the Business Architecture interview and confirm the capability/value-stream model before this interview. If the BA is unstable, spend the first half of this session validating BA links rather than designing new org structures.
- Use the Business Architecture capability map as the organising anchor — every OM element should trace to a capability or value stream; otherwise it is untethered design.
- Distinguish **business operating roles** (owned by the OM) from **EA engagement roles** (ROLE-NNN in the Role Catalogue). Confusing the two is a common Phase B error.
- Decision-rights questions often surface political tension; document the defensible position and escalate unresolved disputes to the Architecture Review Board.
- Sourcing and location decisions are frequently hard to reverse — convert them to ADR-NNN at the point the choice is ratified, not afterwards.
- Keep process detail in the Business Processes Register; this interview should produce a summary-and-link index in OM §5, not duplicated step tables.
- Workforce/channel questions should surface delivery-model implications for business services — update `deliveryChannel` and `operatingModelNote` on SVC-NNN entries via `/ea-services update`.

**§D Diagrams — ask at close of session:**
> "Three diagrams are standard for the Operating Model. Which would you like to create or describe now?"
- **Operating Model Overview** — value chain + operating units + delivery channels (`operating-model-overview.mmd`)
- **Organisation Design** — target operating structure and decision fora (`operating-model-org-design.mmd`)
- **Process Execution Context** — critical processes mapped to operating units and capabilities (`operating-model-process-context.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Operating Model frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard Operating Model questions. Ask: "Would you like to address security concerns for the Operating Model? (y/n)"

**SABSA focus:** Operational — security roles, controls, and supply-chain assurance

1. Which business operating roles own security decisions for this domain?
2. What security controls are embedded in the operating processes (e.g. segregation of duties, access recertification, fraud checks)?
3. What SLAs or assurance requirements apply to outsourced or partner-delivered capabilities?
4. Which third parties introduce material security or compliance risk, and how are they governed?

**Output routing:**
| Answer | Output |
|---|---|
| Security roles and accountabilities | Operating Model §3 + Governance Framework |
| Process-embedded security controls | Operating Model §4 + RIS-NNN |
| Supplier security SLAs / assurance | Operating Model §7 + Constraints Register |
| High-risk third parties | Vendor Landscape (VDR-NNN) + Risk Register (RIS-NNN) |

---

## Phase B — Business Model Canvas Interview

**Goal:** Capture the nine building blocks of the business model before detailing capabilities and processes

**When to run:** Run this interview at the start of Phase B, before or alongside the Business Architecture interview. It is especially valuable for Greenfield and Brownfield engagements. For Assessment-only engagements, use it to baseline the current operating model.

**Key questions:**

### Customer Segments
1. Who are your most important customers or users? How would you group them into distinct segments?
2. For each segment: how large is it (volume, revenue contribution, strategic importance)?
3. Are there segments you serve today that you want to exit, grow, or enter in the future?

### Value Propositions
4. For each customer segment, what problem do you solve or what need do you satisfy?
5. What makes your offering different or better than alternatives available to that segment?
6. Which value proposition is most important to the organisation's long-term success?

### Channels
7. How do customers find out about what you offer today? What channels do you use to reach them?
8. How do customers purchase, access, or receive the product or service?
9. Are any channels underperforming or missing that you plan to add?

### Customer Relationships
10. What type of relationship do you maintain with each customer segment — personal, self-service, community, automated?
11. Is the primary goal of the relationship to acquire new customers, retain existing ones, or grow revenue per customer?
12. How do customers prefer to interact with you (in-person, digital, hybrid)?

### Revenue Streams
13. For what value do customers pay? What are all the ways the organisation generates revenue?
14. For each revenue stream, how is pricing determined (fixed, volume-based, negotiated, market-rate)?
15. Which revenue streams are most significant? Are any growing, declining, or at risk?

### Key Resources
16. What physical, intellectual, human, or financial assets are essential to delivering the Value Proposition?
17. Which of these resources are owned by the organisation, and which are leased or sourced from partners?
18. What would happen to the business model if you lost access to the most critical resource?

### Key Activities
19. What are the most important things the organisation must do well to make the business model work?
20. Are these activities production (making/delivering), problem-solving (consulting/knowledge), or platform-based (running a marketplace or network)?
21. Which activities are core and must stay internal, and which are candidates for outsourcing?

### Key Partnerships
22. Who are the most important external partners or suppliers the business model depends on?
23. For each partner: what do they provide, and what do you provide to them in return?
24. Are there partnerships that don't exist today that the target state will require?

### Cost Structure
25. What are the largest costs in operating the current business model?
26. Are costs primarily fixed (remain the same regardless of volume) or variable (scale with activity)?
27. Is the business model more cost-driven (minimise cost) or value-driven (justify premium pricing)?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Customer segments (who they are, size) | Business Model Canvas | `{{customer_segments}}` |
| Value propositions per segment | Business Model Canvas | `{{value_propositions}}` |
| Channels (awareness, delivery) | Business Model Canvas | `{{channels}}` |
| Customer relationship type and goal | Business Model Canvas | `{{customer_relationships}}` |
| Revenue streams and pricing | Business Model Canvas | `{{revenue_streams}}` |
| Key resources (type, owned vs. sourced) | Business Model Canvas | `{{key_resources}}` |
| Key activities (type, core vs. outsourced) | Business Model Canvas | `{{key_activities}}` |
| Key partnerships and what is exchanged | Business Model Canvas | `{{key_partnerships}}` |
| Cost structure (largest costs, fixed/variable) | Business Model Canvas | `{{cost_structure}}` |
| Business model narrative | Business Model Canvas | `{{business_model_summary}}` |
| Segment-to-service linkage | Business Architecture | `{{business_services}}`, `{{business_context}}` |
| Capability requirements from key activities | Business Architecture | `{{business_capabilities}}` |
| Process candidates from key activities | Business Architecture | `{{business_processes}}` |

**Facilitation Notes:**
- Run the BMC interview before the detailed Business Architecture questions — it creates a shared mental model of the business before diving into capability and process detail.
- The nine blocks are interdependent; if an answer changes one block, ask what it implies for related blocks (e.g., "If you add that channel, does it change your cost structure?").
- For Brownfield engagements, capture both current state and target state for each block — the differences are the transformation scope.
- The Value Proposition question is the most important anchor: capabilities, processes, and resources should all trace back to supporting at least one Value Proposition.
- If the organisation has multiple business units with different models, complete a separate canvas for each unit or product line.
- Use the BMC linkage table (Section 11 of the template) to connect each block to the corresponding Business Architecture element — this prevents the Business Architecture from drifting away from commercial reality.

---

## Phase C — Information Systems Interview

**Goal:** Understand data entities, application portfolio, and data/application goals

**Key questions:**
1. What are the key data domains in your organisation — the major categories of information you manage?
2. Which applications support each of the business functions we identified?
3. Which applications are considered strategic investments, and which are candidates for replacement?
4. Where do you have data duplication or inconsistency problems across systems?
5. What are the critical integration points between applications?
6. Are there regulatory requirements governing specific data? (select all that apply)
   - [ ] Privacy — GDPR, CCPA, LGPD, or equivalent
   - [ ] Data retention — legal hold, archiving, or disposal obligations
   - [ ] Data classification — sensitivity labels and handling requirements
   - [ ] Data sovereignty / residency — data must remain in-country or in-region
   - [ ] Sector-specific — HIPAA, PCI-DSS, SOX, ISO 27001, or similar
   - [ ] None identified
   - [ ] Other: ___
7. Who owns each application and each major data domain?
8. What is the single biggest challenge you face with your data and application landscape today?

**Application Architecture Design Questions:**

9. For each target application component: what is its primary responsibility? And equally important — what is NOT its responsibility? Where is its boundary with adjacent components?

10. What architecture pattern best describes the target application landscape?
    - [ ] Modular Monolith — single deployable unit with well-defined internal modules
    - [ ] Microservices — independently deployable services per bounded context
    - [ ] Event-driven — services communicate primarily via events / message bus
    - [ ] Serverless — functions-as-a-service with no persistent application tier
    - [ ] COTS / SaaS-led — mostly packaged software; custom code only at the edges
    - [ ] Hybrid — combination of above; describe which pattern applies where
    Why was this pattern chosen? What constraints (cost, skills, timeline, regulatory) drove the decision?

11. For each significant application component: describe its internal structure.
    - What are the major internal modules or layers? (e.g. Presentation, Business Logic, Data Access, Integration Adapter)
    - Which modules are most likely to change frequently — and should therefore be isolated from stable modules?
    - Which modules need to be independently scalable?

12. What services or APIs does each component expose to other components or external consumers?
    - For each service: what does it do, what are the exact consumers, and what is the protocol (REST / GraphQL / gRPC / event)?
    - What authentication and authorisation model applies to each API?
    - Is there an SLA (max response time, availability target) that consumers depend on?

13. Walk me through the user journey for the most business-critical use case (reference UC-NNN from Business Architecture). Which application components are touched in sequence?
    - What is the user interaction model — web UI, mobile app, API call, or batch?
    - Where are the key latency or reliability sensitivity points in this journey?
    - What happens to the user journey if any one component is unavailable?

14. For each architecturally significant component: what are the non-functional requirements?
    - **Performance:** max acceptable response time; throughput (requests/sec or records/hr)
    - **Availability:** uptime target (e.g. 99.9%); acceptable maintenance window
    - **Scalability:** horizontal or vertical; what triggers a scale event?
    - **Data volume:** current record counts and 3-year projected growth

15. How are events or state changes communicated between components?
    - Is the primary integration pattern synchronous (request/response) or asynchronous (event/message)?
    - If asynchronous: what is the message broker or event bus? (e.g. Kafka, Azure Service Bus, AWS SQS)
    - How are event schemas defined, documented, and versioned? Who is responsible for schema governance?

16. What COTS or SaaS products are being adopted for commodity capabilities?
    - For each: which business capability (CAP-NNN) does it replace or augment?
    - What customisation or extension points will be used — and is customisation within the vendor's supported model?
    - What is the integration pattern for connecting this COTS product to the broader application landscape?

9. *(If Data direction not yet defined)* Capture Data direction using the three-type model:
   - **Data goal** example: "Have a single source of truth for customer data" (qualitative, no deadline)
   - **Data objective** example: "Reduce duplicate customer records by 90% by June 2026" (measurable + deadline)
   - **Data strategy** example: "Implement a master data management platform" (approach, not outcome)

10. *(If Application direction not yet defined)* Capture Application direction using the three-type model:
    - **Application goal** example: "Operate a modern, composable application landscape"
    - **Application objective** example: "Decommission 3 legacy systems by Q2 2027"
    - **Application strategy** example: "Adopt SaaS-first for commodity capabilities"

**Architecture Building Block (ABB) questions:**
> Ask these when defining the target application/data landscape. ABBs are logical, vendor-neutral components — do not name specific products here.

11. For each significant application component identified: what is the logical function it provides — described without naming a vendor or product? (e.g. "Immutable Log Store", not "AWS CloudTrail"; use a noun phrase, not an action: "Database Backup Service", not "Back up the database")
    - What requirement(s) (REQ-NNN) does this ABB satisfy?
    - What is its architecture domain — Application or Data?
    - Assign an ABB-NNN ID and capture in the ABB Register.

12. For each ABB: is it reusable across multiple capabilities or is it single-purpose?
    - Reusable ABBs should have a generic name and broad description.
    - Single-purpose ABBs should trace to a specific capability (CAP-NNN) and requirement (REQ-NNN).

### Decision Quality Questions
> Ask these after completing the standard Phase C questions. Data and application decisions are high-impact and often hard to reverse — evidence and optionality matter most here.

1. **[DECISION]** For each technology or vendor selection proposed: what POC, benchmark, or reference implementation is required before commitment? Has it been scheduled?
2. **[DECISION]** What is the reversibility of each chosen data model or application pattern? If wrong, how many downstream systems are affected?
3. **[DECISION]** What optionality is preserved? (e.g., API-first design allows vendor swap; domain-driven boundaries allow technology change without consumer impact.)
4. **[DECISION]** Are there MUST requirements that should disqualify any candidate option? Has a weighted scorecard been applied?
5. **[DECISION]** Is there strong stakeholder pressure for a specific vendor or platform? What is the defensible evidence-based position?
6. **[DECISION]** Which unresolved data or application decisions should be logged as PAD-NNN rather than committed now?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Key data domains | Data Architecture | `{{data_domains}}` |
| Applications per function | Application Architecture | `§2 Current Application Portfolio` |
| Strategic applications | Application Architecture | `§3 Target Application Landscape` |
| Replacement candidates | Application Architecture | `§3 Target Application Landscape — Status: Replace / Retire` |
| Gap Analysis (application) | Gap Analysis | `{{application_gaps}}` |
| Data duplication issues | Data Architecture | `{{data_quality_issues}}` |
| Integration points | Application Architecture | `§5 Integration Architecture` |
| Regulatory data requirements | Requirements Register | `{{data_regulatory_requirements}}` |
| Data Architecture gaps | Gap Analysis | `{{data_gaps}}` |
| Application ownership | Application Architecture | `§2 Current Application Portfolio` |
| Data domain ownership | Data Architecture | `{{data_ownership}}` |
| Key data/app challenge | Gap Analysis | `{{key_challenge}}` |
| Component responsibilities and boundaries | Application Architecture | `§4 Application Components — Responsibility` |
| Architecture pattern selection | Application Architecture | `§4 Application Components — Architecture Pattern` |
| Component internal modules / layers | Application Architecture | `§4 Application Components — Internal Modules/Layers table` |
| Service / API contracts | Application Architecture | `§4 Application Components — Service Contracts table` + `§5 API Catalog` |
| User journeys through applications (UC-NNN) | Application Architecture | `§1a User Journeys & Use Cases` |
| NFRs per component | Requirements Register | `REQ-NNN` type:non-functional, scope:application |
| Integration pattern (sync / async) | Application Architecture | `§5 Integration Architecture — Integration Pattern` |
| Event schema governance | Application Architecture | `§5 Integration Architecture — Integration Pattern` |
| COTS / SaaS adoption decisions | Application Architecture | `§3 Target Application Landscape — Rationale` |
| Data direction (goals, objectives, strategies) | engagement.json + Logical Data Model | `direction.Data` + `{{data_direction}}` |
| Data metrics | engagement.json + Logical Data Model | `metrics.Data` + `{{data_metrics}}` |
| Application direction (goals, objectives, strategies) | engagement.json + Application Portfolio Catalogue | `direction.Application` + `{{application_direction}}` |
| Application metrics | engagement.json + Application Portfolio Catalogue | `metrics.Application` + `{{application_metrics}}` |

**Facilitation Notes:**
- Bring an application inventory template to the session pre-populated with known systems — asking people to add to a list is more productive than asking them to recall from memory.
- The "strategic vs replacement" question often surfaces political tensions; frame it as investment prioritisation rather than a performance critique of existing systems.
- Data ownership questions frequently reveal ungoverned domains — treat "no one owns it" as a gap finding, not an oversight to skip.
- Ask for data flow diagrams or integration documentation after the session; verbal descriptions of integration points are rarely complete.
- Run architecture pattern selection (Q10) as an explicit decision — it should go through the A3 Decision Log. Patterns chosen by default rather than by design are a significant governance gap.
- Component boundary questions (Q9) are most productive with technical leads, not just architects — the people who implement components know where the real boundaries are.
- Use case tracing (Q13) should be done for at least the top 3 critical use cases from the Business Architecture — single use case coverage is insufficient for system-of-systems design.
- NFR elicitation (Q14) should be captured per component, not for the whole system — aggregate NFRs hide where the real engineering constraints are.
- Event schema governance (Q15) is frequently neglected until integration breaks — establish ownership and versioning policy during Phase C, not during implementation.

**§D Diagrams — ask at close of session:**
> "Five diagrams are standard for Phase C. Which would you like to create or describe now?"
- **Conceptual Data Model** — business-readable subject areas and their relationships (`data-architecture-conceptual-data-model.mmd`)
- **Data Flow Diagram** — how data moves between systems and across boundaries (`data-architecture-data-flow.mmd`)
- **Application Cooperation View** — integration topology showing how applications interact (`application-architecture-cooperation.mmd`)
- **Application Component Map** — internal decomposition of key applications (`application-architecture-component-map.mmd`)
- **User Journey Trace** — sequence diagram showing which components are touched for a critical use case (`application-architecture-journey-trace.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to the relevant artifact frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions — C-Data (optional)
> Offer this section after completing the standard Phase C data questions. Ask: "Would you like to address security concerns for Phase C Data Architecture? (y/n)"

**SABSA focus:** Logical — data classification, protection services, and privacy obligations

1. What data classification levels apply? (e.g., Public / Internal / Confidential / Restricted — or organisation-specific scheme)
2. What data is most sensitive or regulated? (personal data, payment data, health data, IP, classified)
3. What are the encryption requirements — at rest and in transit? Are there approved algorithms or key lengths?
4. What data retention and deletion obligations exist? What triggers deletion?
5. What privacy requirements apply? Is GDPR Article 25 (privacy by design and by default) a relevant obligation?
6. Where does data reside — jurisdiction constraints, cross-border transfer restrictions?

**Output routing:**
| Answer | Output |
|---|---|
| Data classification scheme | Data Architecture (classification table) |
| Encryption at rest and in transit | Data Architecture (encryption specification), REQ-NNN type:security, category:data-protection |
| Retention and deletion | Data Architecture (retention policy), REQ-NNN type:security, source:ISO27001, control:A.8.10 |
| Privacy requirements | Data Architecture (privacy notes), REQ-NNN type:security, category:privacy |

### Security Questions — C-App (optional)
> Offer this section after completing the standard Phase C application questions. Ask: "Would you like to address security concerns for Phase C Application Architecture? (y/n)"

**SABSA focus:** Logical — identity, access, audit, and secure development

1. What authentication model is required? (SSO, MFA, federated identity, protocol: SAML / OIDC / Kerberos)
2. What authorisation model applies? (RBAC, ABAC, policy-based — what granularity of access control is needed?)
3. What audit logging is required? Who needs to see logs, for how long, and in what format?
4. How are APIs secured? (OAuth 2.0, mTLS, API gateway, rate limiting)
5. What are the secure coding standards for this application? (OWASP, SSDLC, code review requirements)
6. What is the approach to vulnerability management — SAST, DAST, penetration testing frequency?

**Output routing:**
| Answer | Output |
|---|---|
| Authentication model | Application Architecture (auth model section), REQ-NNN type:security, category:access-control |
| Authorisation model | Application Architecture (authz model), REQ-NNN type:security, source:ISO27001, control:A.5.15 |
| Audit logging | Application Architecture (logging requirements), REQ-NNN type:security, source:ISO27001, control:A.8.15 |
| API security | Application Architecture (API security section) |

---

## Phase D — Technology Architecture Interview

**Goal:** Understand current and desired technology platform, and technology goals

**Key questions:**
1. What is your current technology stack — key platforms, infrastructure, and tooling?
2. What technology standards are mandated within the organisation or by your industry?
3. What technology capabilities are missing from the current platform?
4. What is your organisation's cloud strategy — where do you want to be in three years?
5. What technology constraints must the architecture respect (vendor lock-in, existing contracts, skills)?
6. What does your technology landscape need to look like in three years?
7. Where is your technology debt concentrated — which parts of the platform are most at risk?
8. What security or compliance requirements directly affect technology decisions?
9. *(If Technology direction not yet defined)* Capture Technology direction using the three-type model:
   - **Technology goal** example: "Operate a cloud-native, zero-trust platform" (qualitative state)
   - **Technology objective** example: "Achieve 99.9% availability for all Tier-1 systems by Q3 2026" (measurable + deadline)
   - **Technology strategy** example: "Containerise all new workloads using Kubernetes" (chosen approach)

   Watch for common confusion: "move to the cloud" is a strategy if cloud is the approach to achieve availability or cost goals; it becomes a goal if the cloud-native state is itself the aspiration.
10. For each Technology objective, ask: "How will you measure this — what is the unit, the baseline, and where does data come from?" Capture as a `performance` metric (`TM-`). For Technology strategies, ask for an activity measure (e.g., "% of workloads containerised") — capture as an `activity` metric.

**Solution Building Block (SBB) questions:**
> Ask these when selecting concrete technologies. SBBs are vendor-specific implementations of ABBs.

11. For each ABB-NNN defined in Phase C: what concrete product, service, or technology will implement it?
    - What is the vendor or source? (commercial, open source, internal build)
    - What version or release channel? (specific version, LTS, managed service)
    - What lock-in constraints exist? (proprietary APIs, egress costs, licensing, data residency)
    - Assign an SBB-NNN ID and capture in the SBB Register.
    - **Anti-pattern check:** If an SBB is selected before its ABB is defined, flag as "vendor-first selection" and require the ABB to be backfilled.

12. For each SBB: what is the exit cost and timeline if this vendor relationship fails?
    - Is there an alternative SBB that could implement the same ABB?
    - Capture alternatives as "backup SBB" references for risk planning.

### Decision Quality Questions
> Ask these after completing the standard Phase D questions. Technology choices are often the hardest to reverse — treat evidence and optionality as first-class concerns.

1. **[DECISION]** For each technology standard or platform selected: what fitness function or automated conformance check will validate adoption?
2. **[DECISION]** What is the reversibility of each technology commitment? (e.g., containerised workloads are more reversible than mainframe migrations.)
3. **[DECISION]** What optionality is preserved? (e.g., multi-cloud abstraction, API-first design, domain-aligned data stores.)
4. **[DECISION]** Are golden paths defined so teams can adopt standards without central review? What is the boundary between pre-approved and review-required choices?
5. **[DECISION]** Is there vendor lock-in risk? What is the exit cost and timeline if the vendor relationship fails?
6. **[DECISION]** Which technology decisions lack sufficient evidence and should be deferred as PAD-NNN?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Current tech stack | Technology Architecture | `{{current_tech_stack}}` |
| Mandated standards | Technology Architecture | `{{mandated_standards}}` |
| Missing tech capabilities | Gap Analysis | `{{technology_gaps}}` |
| Technology Architecture gaps | Gap Analysis | `{{tech_capability_gaps}}` |
| Cloud strategy | Technology Architecture | `{{cloud_strategy}}` |
| Technology constraints | Technology Architecture / Constraints Register | `{{tech_constraints}}` + `CST-NNN` via `/ea-constraints` |
| Requirements Register (tech) | Requirements Register | `{{technology_requirements}}` |
| Future tech landscape | Technology Architecture | `{{future_tech_state}}` |
| Technology debt | Gap Analysis | `{{tech_debt}}` |
| Security/compliance requirements | Requirements Register | `{{security_requirements}}` |
| Technology direction (goals, objectives, strategies) | engagement.json + Technology Standards Catalogue | `direction.Technology` + `{{technology_direction}}` |

**Facilitation Notes:**
- Open with "what keeps you up at night about your current technology?" — this surfaces the real pain points faster than a structured inventory review.
- Technology debt questions are best answered by infrastructure and platform engineers, not just IT leadership; schedule a separate technical session if needed.
- Cloud strategy answers often reflect aspirations rather than funded plans; probe for budget commitment and timeline to distinguish strategy from wishful thinking.
- Capture mandated standards as constraints in the Constraints Register (`CST-NNN`) and reference them in Technology Architecture SBB records — they frequently constrain solution options in phases E and F. Legacy `category: Constraint` in the Requirements Register is deprecated.

**§D Diagrams — ask at close of session:**
> "Two diagrams are standard for the Technology Architecture. Which would you like to create or describe now?"
- **Technology Stack View** — layered view from infrastructure through platform to application (`technology-architecture-stack.mmd`)
- **Infrastructure Topology** — network zones, nodes, and security boundaries (`technology-architecture-topology.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Technology Architecture frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase D? (y/n)"

**SABSA focus:** Physical — security mechanisms, network controls, monitoring, and infrastructure

1. What network segmentation model is required? (zones, DMZ, micro-segmentation, air-gapped segments)
2. What PKI and certificate management approach is used? (internal CA, public CA, certificate lifecycle)
3. What endpoint hardening standards apply? (CIS Benchmarks, vendor hardening guides, mobile device management)
4. What security monitoring and SIEM tools are in scope? What log sources are required?
5. What physical security controls apply to infrastructure? (data centre, co-location, cloud physical security)
6. What backup and recovery controls are required? (RTO, RPO, backup encryption, offsite storage)

**Output routing:**
| Answer | Output |
|---|---|
| Network segmentation | Technology Architecture (network security section) |
| PKI and certificate management | Technology Architecture (PKI section), REQ-NNN type:security, source:ISO27001, control:A.8.24 |
| SIEM and monitoring | Technology Architecture (monitoring section), RIS-NNN (infrastructure security risks) |
| Backup and recovery | Technology Architecture (resilience section), REQ-NNN type:security, source:NIST-CSF, control:RC.RP |

---

## Phase E — Opportunities and Solutions Interview

**Goal:** Prioritise work packages and build the initial architecture roadmap, grounded in the Goals, Objectives, and Strategies established in Phase A.

**Pre-session preparation:** Load the Architecture Vision and read §5 Goals (G-NNN), §10 Objectives (OBJ-NNN), §9 Opportunities (OPP-NNN), and §11 Strategic Direction Summary (STR-NNN) before starting. Present this list to participants so work package prioritisation is anchored to stated intent.

**Key questions:**

*Strategic alignment (ask first — establishes the anchor for all prioritisation)*
1. Looking at the Goals and Strategies defined in Phase A, which are the most critical to advance in the next 12 months? (Reference G-NNN and STR-NNN IDs by name.)
2. For each proposed work package, which Goal, Objective, or Strategy does it directly advance? Are there Goals or Strategies that no work package addresses — and is that intentional?

*Opportunity and gap coverage*
3. Which capability gaps identified in earlier phases are the highest priority to close?
4. For each high-priority gap — does it represent an Opportunity (OPP-NNN) to capture, not just a problem to fix? Assign an OPP-NNN if so, and link it to the work package it will be addressed by.
   - If an OPP-NNN was already recorded in Phase A, link the WP to it now.
   - If no OPP-NNN exists yet, create one and add it to Architecture Vision §9.
5. What projects are already in flight that this roadmap must align with or avoid conflicting with?

*Resources and capacity*
6. For each proposed work package: what roles and skills are needed to deliver it? Estimate FTE required and identify any skill gaps or vendor/partner dependencies.
   - Record: Roles, FTE estimate, skill dependencies, vendor/partner — in the WP's `Resources Required` field in the Architecture Roadmap.
   - Flag any WP where required resources are not confirmed as a delivery risk.

*Constraints and sequencing*
7. What is the available investment budget and target delivery timeline?
6. What sequencing dependencies exist — which changes must happen before others can begin?
8. What sequencing dependencies exist — which changes must happen before others can begin?
9. What are acceptable transition states — what does "good enough for now" look like at each stage?
10. If the budget were halved, which Goals and work packages would you protect, and which would you defer?

*Risk*
11. What are the biggest risks to delivering this roadmap — and do any of those risks directly threaten a Goal or Strategy?

**User Story (STY-NNN) questions:**
> Ask these when decomposing work packages into delivery items. Stories translate SBBs into actor-centred work.

12. For each SBB-NNN selected in Phase D: what user stories are needed to implement it?
    - Who is the actor? (user, operator, customer, system)
    - What does the actor want to accomplish? (goal)
    - Why does it matter? (benefit)
    - Format: "As a {actor}, I want {goal} so that {benefit}."
    - Assign a STY-NNN ID and capture in the Requirements Register Stories subsection or Architecture Roadmap.

13. For each story: what acceptance criteria confirm it is done?
    - Measurable outcomes: "Given X, when Y, then Z"
    - Link each criterion to a REQ-NNN measurable target where possible.

14. Are there enabler stories — infrastructure, security, compliance scaffolding — with no direct user-facing outcome?
    - Tag as `[Enabler]` and link to the SBB they support.
    - Ensure enabler stories still trace to at least one REQ-NNN (e.g. a security requirement).

15. For each story: what are the atomic implementation tasks?
    - Tasks have no IDs; they are bullet points under the story.
    - Example tasks: "Configure backup schedule", "Test restore procedure", "Write runbook"
    - **Anti-pattern check:** If a story reads like a task ("Configure X", "Run Y"), it is not a story — rewrite as actor-goal-benefit or move to Tasks.

### Decision Quality Questions
> Ask these after completing the standard Phase E questions. Phase E converts gaps and decisions into work packages — evidence-gating and PAD resolution are critical here.

1. **[DECISION]** Are all PAD-NNN entries from earlier phases either resolved or linked to a work package? List any open PADs with expired target dates.
2. **[DECISION]** For each work package: what evidence must be gathered before it starts? Is the evidence status sufficient, partial, or insufficient?
3. **[DECISION]** Are work packages with insufficient evidence scheduled in Wave 1? If yes, flag as high-risk and require executive sign-off or guardrails.
4. **[DECISION]** What is the decision reversibility of each work package? (High = can reverse with minimal cost; Low = irreversible or expensive.)
5. **[DECISION]** Does every work package advance at least one goal or execute at least one strategy? Orphan work packages create delivery risk — flag them.
6. **[DECISION]** Which transition architectures are deliberate value increments vs. temporary compromises? Document the value delivery mode for each.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Goals/strategies addressed by the roadmap | Architecture Roadmap | Strategic Alignment table (G-NNN / OBJ-NNN / STR-NNN / OPP-NNN column) |
| Goals/strategies with no covering WP | Architecture Roadmap | `{{unaddressed_items}}` |
| Goals/strategies per work package | Architecture Roadmap | WP table `{{g_obj_ids}}` / `{{str_ids}}` per WP |
| Opportunities per work package | Architecture Roadmap | WP table Strategic Alignment (OPP-NNN) |
| Priority capability gaps | Architecture Roadmap | `{{priority_gaps}}` |
| WP resource requirements | Architecture Roadmap | WP `Resources Required` + `Capacity note` fields |
| In-flight projects | Architecture Roadmap | `{{existing_projects}}` |
| Investment budget | Architecture Roadmap | `{{investment_budget}}` |
| Target timeline | Architecture Roadmap | `{{delivery_timeline}}` |
| Sequencing dependencies | Architecture Roadmap | `{{sequencing_dependencies}}` |
| Acceptable transition states | Architecture Roadmap | `{{transition_states}}` |
| Minimum viable delivery | Architecture Roadmap | `{{minimum_viable_scope}}` |
| Delivery risks | Architecture Roadmap | `{{delivery_risks}}` |

**Facilitation Notes:**
- **Always anchor to Phase A Goals first.** Without this, prioritisation defaults to loudest voice or easiest wins rather than strategic intent. If the Architecture Vision is incomplete or has no Goals defined, flag this as a blocker and recommend completing §5–§10 before proceeding.
- The Strategic Alignment table in the roadmap must have every G-NNN and STR-NNN from Phase A appear at least once. Anything missing is an explicit coverage gap.
- The "halved budget" question is the most powerful prioritisation tool — framing it as "which Goals do we protect?" makes the trade-off explicit and strategic rather than tactical.
- In-flight project alignment is frequently underestimated; request a project portfolio list before the session and map conflicts in advance.
- Sequencing questions work well as a group exercise where participants physically order work packages — disagreements in the room are better surfaced now than during delivery.
- Acceptable transition states define architecture checkpoints; if the organisation cannot articulate them, the roadmap will lack governance anchors.

**§D Diagrams — ask at close of session:**
> "One diagram is essential for Phase E. Would you like to create it now?"
- **Architecture Roadmap (Gantt)** — work packages sequenced into delivery waves with timeline (`architecture-roadmap-gantt.mmd`)
- **Gap Heat Map** *(optional)* — visual prioritisation of gaps by impact and effort (`gap-analysis-heat-map.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Architecture Roadmap frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase E? (y/n)"

**SABSA focus:** Component — security gap analysis and work package sequencing

1. What security gaps have been identified against the target architecture?
2. Which security work packages are highest priority — what cannot go live without being addressed?
3. Are there security dependencies that constrain the roadmap sequence? (e.g., IAM must be in place before application migration)
4. What security products or tools are being selected to implement the Physical layer controls?
5. Are any security capabilities being deferred to a later iteration, and is that risk-accepted?

**Output routing:**
| Answer | Output |
|---|---|
| Security gaps | Gap Analysis (security gaps section) |
| Security work packages | Architecture Roadmap (WP-NNN type:security) |
| Security dependencies | Architecture Roadmap (sequencing notes) |

---

## Phase F — Migration Planning Interview

**Goal:** Define the practical wave plan, resourcing, cut-over approach, and rollback strategy for delivering the architecture roadmap

**Key questions:**
1. How should the work packages be grouped into delivery waves — what natural groupings exist based on dependency, risk, or business value?
2. For each wave, what resources and skills are required, and are they available within the planned timeframe?
   - For each role: what is required vs. what is confirmed? Record gaps in the Wave Resource Summary table.
   - Are vendor or partner commitments in place for this wave? If not, flag as a delivery risk.
3. What is the organisation's capacity for change — how much disruption can be absorbed per wave without affecting business operations?

*Resource validation — run after all waves are defined:*
> "Looking across all waves: where are the resource peaks? Are there any waves where multiple high-FTE work packages overlap? Flag overlapping peaks as scheduling risks in the Risk Register."
4. How will data be migrated for each wave? (select all that apply)
   - [ ] ETL — batch extract, transform, and load jobs
   - [ ] Replication — continuous sync from source to target system
   - [ ] Dual-write — application writes to both old and new systems simultaneously
   - [ ] API-based migration — programmatic data transfer via APIs
   - [ ] Manual — human-led data entry or copy
   - [ ] Other: ___
5. What is the cut-over approach? (select one)
   - [ ] Hard cut-over — all users switch at once on a fixed date
   - [ ] Phased rollout — groups of users migrated in waves
   - [ ] Parallel running — old and new systems operate simultaneously for a period
   - [ ] Feature flags — gradual activation controlled by configuration
   - [ ] Strangler fig — new functionality incrementally replaces old
   - [ ] Other: ___
6. What are the rollback triggers and procedures for each wave — if something goes wrong, how quickly can you revert and who makes that call?
7. How will legacy systems be decommissioned once replacement capabilities are live?
8. What are the entry and exit criteria for each wave — what must be true before a wave begins and before the next one starts?
9. How will user transition and change management be handled across each wave?
10. What dependencies exist with third-party vendors, regulators, or external systems that constrain the migration sequence?

### Decision Quality Questions
> Ask these after completing the standard Phase F questions. Migration decisions are often irreversible and expensive — timing and evidence quality matter.

1. **[DECISION]** Are migration waves prioritised by evidence quality, not just impact? (Work packages with weak evidence should be deferred or given guardrails.)
2. **[DECISION]** For each wave: what is the rollback cost and timeline? Is the decision reversible within the wave's budget?
3. **[DECISION]** What is the minimum viable evidence required before each wave starts? Has it been gathered?
4. **[DECISION]** Are there legacy exit criteria defined for every system being replaced? Without exit criteria, legacy systems live forever.
5. **[DECISION]** Which migration decisions are being made under time pressure that may compromise evidence quality? Flag as risky commits.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Wave groupings | Migration Plan | `{{wave_1_name}}` / `{{wave_2_name}}` |
| Resource requirements per wave | Migration Plan | Wave Resource Summary table (role / required / available / gap) |
| Organisational change capacity | Migration Plan | `{{migration_overview}}` |
| Resource peak conflicts across waves | Risk Register (via `/ea-risks add`) | New RIS-NNN — delivery risk |
| Data migration approach | Migration Plan | `{{data_migration_approach}}` |
| Cut-over approach | Migration Plan | `{{cutover_approach}}` |
| Rollback triggers | Migration Plan | `{{trigger_1}}` / `{{trigger_2}}` |
| Rollback procedures | Migration Plan | `{{procedure_1}}` / `{{procedure_2}}` |
| Decommissioning approach | Migration Plan | `{{decommissioning_approach}}` |
| Wave entry/exit criteria | Migration Plan | `{{wave_1_entry_criteria}}` / `{{wave_1_exit_criteria}}` |
| User transition approach | Migration Plan | `{{user_transition_approach}}` |
| External dependencies | Migration Plan | `{{wave_1_dependencies}}` / `{{wave_2_dependencies}}` |
| Migration risks | Migration Plan | `{{description}}` / `{{mitigation}}` (risk register rows) |

**Facilitation Notes:**
- Run wave planning as a visual exercise — use sticky notes or a whiteboard to group work packages; verbal discussion alone rarely produces a coherent wave structure.
- Change capacity is frequently overestimated by leadership; ask operational managers separately to get a realistic picture of how much disruption the organisation can absorb.
- Rollback planning is often skipped under time pressure — treat it as mandatory; a rollback that has not been rehearsed is not a rollback.
- Data migration approach must be agreed with data owners and the DBA/data engineering team before the Migration Plan is finalised; late surprises here cause the most delivery delays.
- External dependencies (regulatory approvals, vendor upgrade windows, third-party API changes) are frequently on the critical path; surface them early and track them explicitly.

**§D Diagrams — ask at close of session:**
> "One diagram makes the Migration Plan immediately clearer for delivery teams. Would you like to create it now?"
- **Migration Wave Diagram** — Gantt showing what moves in each wave and key transition checkpoints (`migration-plan-waves.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram file → `diagrams/`, filename added to Migration Plan frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for a Mermaid starter.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase F? (y/n)"

Load the **Phase F — Migration Planning** section of `skills/ea-security/references/security-interview-questions.md` and ask its questions, routing answers per its output routing table (migration data protection, coexistence/cutover risks, secrets rotation, secure decommissioning, third-party access, per-wave security go/no-go).

---

## Phase G — Implementation Governance Interview

**Goal:** Establish governance and compliance monitoring

**Key questions:**
1. How will architecture compliance be monitored during implementation?
2. Who has the authority to approve change requests during delivery?
3. What is the expected reporting cadence for architecture status updates?
4. How will architecture requirements be enforced in contracts with delivery teams or vendors?
5. How will project deviations from the approved architecture be handled?
6. What tools or processes will be used to track compliance and issues?

### Decision Quality Questions
> Ask these after completing the standard Phase G questions. Governance is where decisions are enforced — deviations must be justified with evidence.

1. **[DECISION]** Are deviations from the approved architecture justified with evidence, or are they exceptions without rationale? Unjustified deviations erode decision quality.
2. **[DECISION]** Is governance effort focused on high-risk, irreversible decisions — or does it review everything equally? (Elite practice: guardrails for reversible, review for irreversible.)
3. **[DECISION]** Are conformance checks automated (CI/CD, policy-as-code) or manual? Manual-only governance scales poorly and creates bottlenecks.
4. **[DECISION]** How are PAD-NNN entries that expire during implementation handled? Are they escalated or silently ignored?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Compliance monitoring approach | Compliance Assessment | `{{compliance_monitoring}}` |
| Change approval authority | Architecture Contract | `{{change_approval_authority}}` |
| Reporting cadence | Compliance Assessment | `{{reporting_cadence}}` |
| Contract enforcement approach | Architecture Contract | `{{contract_enforcement}}` |
| Deviation handling process | Architecture Contract | `{{deviation_process}}` |
| Compliance Assessment process | Compliance Assessment | `{{assessment_process}}` |
| Tracking tools and processes | Compliance Assessment | `{{tracking_tools}}` |

**Facilitation Notes:**
- Governance interviews work best with both architecture leadership and project delivery leadership in the room — differences in expectation about compliance authority are common and must be resolved before delivery starts.
- Ask for examples of how past deviations were handled to understand the real governance culture rather than the stated policy.
- Reporting cadence questions should result in a concrete schedule, not a generic answer like "regularly" — pin down frequency and format.
- Contract enforcement is often overlooked in internal engagements; make it explicit even when no external vendor is involved.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase G? (y/n)"

**SABSA focus:** Operational — security operations model, compliance, and incident management

1. How will security compliance be assessed during implementation? Who performs the assessment?
2. Who is responsible for security operations once the architecture is live? (internal SOC, MSSP, hybrid)
3. What security monitoring and alerting is in place — or needs to be stood up — before go-live?
4. How are security incidents managed? Is there a tested incident response plan?
5. Is an ISO 27001 Statement of Applicability required? Who is responsible for maintaining it?
6. What are the security acceptance criteria for the Implementation Governance Plan — what must be true before sign-off?

**Output routing:**
| Answer | Output |
|---|---|
| Compliance assessment approach | Compliance Assessment (Phase G artifact) |
| Security operations model | Implementation Governance Plan (security operations section) |
| Incident response | Governance Framework (incident management), Implementation Governance Plan |
| Statement of Applicability | Compliance Assessment (SoA reference or draft) |

---

## Phase H — Architecture Change Management Interview

**Goal:** Establish change management and architecture refresh

**Key questions:**
1. How are change requests to the architecture currently submitted and tracked?
2. What triggers a new ADM cycle versus a minor update or waiver?
3. How will the architecture be monitored for continued relevance over time?
4. Who is responsible for maintaining the architecture after this engagement concludes?
5. What is the planned cadence for architecture reviews after delivery?
6. How will lessons learned from this engagement be captured and used?

### Decision Quality Questions
> Ask these after completing the standard Phase H questions. Phase H is where decisions are revisited based on post-implementation evidence — adaptive governance depends on honest reassessment.

1. **[DECISION]** Which decisions made earlier in the engagement should be revisited based on post-implementation evidence? (e.g., technology choices that underperformed, assumptions that proved wrong.)
2. **[DECISION]** Are expired PAD-NNN entries reviewed and either resolved or formally closed? Orphan PADs create hidden delivery risk.
3. **[DECISION]** What is the process for converting post-implementation learnings into updated principles, standards, or reference architectures?
4. **[DECISION]** Are architecture decisions periodically stress-tested against new evidence? If not, the architecture becomes static and drifts from reality.
5. **[DECISION]** Which decisions from this engagement would you make differently with hindsight? Capture as lessons learned and feed back into the engagement charter for future work.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Change request submission process | Change Request | `{{change_submission_process}}` |
| Change tracking approach | Change Request | `{{change_tracking}}` |
| ADM trigger criteria | Change Request | `{{adm_trigger_criteria}}` |
| Architecture monitoring approach | Change Request | `{{monitoring_approach}}` |
| Post-engagement ownership | Change Request | `{{architecture_owner}}` |
| Review cadence | Change Request | `{{review_cadence}}` |
| Lessons learned process | Change Request | `{{lessons_learned_process}}` |

**Facilitation Notes:**
- Phase H interviews often reveal that no one has thought about post-delivery ownership; treat this as a risk to flag immediately rather than leaving it for the client to resolve later.
- The ADM trigger criteria question prevents scope creep being managed as minor changes — agree on clear thresholds upfront.
- Ask for examples of how previous architecture changes were handled to calibrate the maturity of the change management process.
- Lessons learned capture is frequently skipped under delivery pressure; recommend a brief retrospective as a scheduled deliverable rather than an ad hoc activity.
- For ACR triage, classification thresholds, and re-entry mapping, use `skills/ea-engagement-lifecycle/references/phase-h-change-guide.md`.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase H? (y/n)"

Load the **Phase H — Architecture Change Management** section of `skills/ea-security/references/security-interview-questions.md` and ask its questions, routing answers per its output routing table (ACR security impact assessment, re-assessment triggers, control drift, policy/constraint review cycles, incident-learning feedback).

---

## Requirements Phase — Architecture Requirements Discovery

**Goal:** Discover and capture all architecture requirements — functional, non-functional, constraints, and assumptions. Run in phase mode (`/ea-interview start phase requirements`) before or alongside Phase A.

- Functional and non-functional requirements are written to the Requirements Register as `REQ-NNN` items.
- Constraints are written to the Constraints Register as `CST-NNN` items via `/ea-constraints add`.
- Legacy `category: Constraint` in the Requirements Register remains valid for backward compatibility but is deprecated for new capture.

**Before starting:** Ask for any existing requirements documents, standards registers, or service-level agreements. Start from what exists rather than from blank.

---

### Functional Requirements

1. What must the architecture enable that is not possible today? List the top 3–5 new business capabilities required.
2. Which existing capabilities must be preserved, enhanced, or replaced in the target state?
3. Are there specific integration or interoperability requirements — systems that must exchange data or trigger each other? For each boundary surfaced, apply `skills/ea-requirements-management/references/interoperability-requirements.md` — category (business/information/technical), degree (1–4), and capture conventions (REQ-NNN with measurable target; IFC-NNN for degree ≥ 3 boundaries).
4. Are there reporting or data access requirements — what information must be available to whom and when?
5. Are there workflow or process automation requirements that the architecture must support?

---

### Non-Functional Requirements — Ask one question per category

For each NFR category, ask the discovery question and, if answered, capture as REQ-NNN with `category: Non-Functional`, the appropriate `nfrSubType`, and a `measurableTarget`. If a category is not applicable to this engagement, mark it skipped.

| NFR Category | Discovery Question | Measurable Target Prompt |
|---|---|---|
| **Availability** | What is the minimum acceptable uptime? Are there critical periods (e.g. financial year-end, peak trading) where the system must never be unavailable? | Target: ___% availability measured monthly; planned maintenance window: ___ hours/month |
| **Reliability** | What failure rate is acceptable? Must the system continue operating in degraded mode if a component fails? What is the tolerated Mean Time Between Failures? | MTBF target: ___; tolerated failure rate: ___%; fault-tolerance model (active-active / active-passive / none) |
| **Performance** | What response times are expected under normal and peak load? How many concurrent users or transactions must be supported? | p95 response: ___ms; peak concurrent users: ___; throughput: ___ transactions/sec |
| **Security** | What authentication and authorisation model is required? Are there encryption, audit logging, or non-repudiation requirements? Which regulatory security frameworks apply? | Authentication method; data classification levels; encryption standards (AES-256, TLS 1.3+); compliance reference (ISO 27001, NIST CSF) |
| **Usability** | What accessibility standards apply? What is the target for task completion time, error rate, or user satisfaction? Are there specific user groups (e.g. assistive technology users) to support? | WCAG level (A / AA / AAA); task completion target; accessibility compliance date |
| **Maintainability** | How frequently must the system be updated or patched without downtime? What test coverage or code quality threshold is expected? What is the maximum acceptable time to diagnose and fix a production defect? | Deployment frequency; test coverage: ___%; MTTR target: ___ hours |
| **Portability** | Must the solution run on or be migrated to multiple platforms, cloud providers, or deployment models? Are there vendor lock-in constraints? | Target platforms / cloud providers; portability criteria; exit strategy requirement |
| **Compatibility** | What existing systems must the solution co-exist with and not disrupt? Are there API versioning or backward-compatibility requirements? | Existing systems to preserve; API backward-compat window: ___ months |
| **Recoverability** | What are the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for each critical component? What disaster recovery scenarios must be planned for? | RTO: ___ hours; RPO: ___ hours; DR scenario scope (single node / AZ / region / full DC) |

---

### Constraints

6. Are there mandated technology choices — cloud platforms, vendors, or infrastructure that must be used or must not be replaced?
7. Are there regulatory, legal, or contractual obligations that constrain the solution space (e.g. data residency, GDPR, financial regulation)?
8. Are there budget ceilings or timeline deadlines that are non-negotiable?
9. Are there organisational constraints — approved vendor panels, procurement rules, or internal policies that limit options?
10. Are there interoperability constraints — systems that must not be replaced or must be integrated without modification?

---

### Assumptions

11. What assumptions are you making about future business volumes, user growth, or technology capacity that underpin these requirements?
12. What assumptions are you making about the availability of skills, budget, or resources to implement the architecture?
13. What happens to the architecture if any of these assumptions prove false — what is the consequence and the mitigation?

---

### Process and Governance

14. How are requirements currently gathered and documented in your organisation? Who has authority to approve and prioritise?
15. How are conflicting requirements resolved? Who has the final word when two stakeholders disagree?
16. At what cadence will requirements be reviewed and updated during the engagement?

---

**Output Routing:**

| Captured Answer | Written To | ID Prefix | Fields Set |
|---|---|---|---|
| Functional requirement | Requirements Register — Enterprise or Program section | REQ-NNN | `category: Functional` |
| Non-functional requirement | Requirements Register — Enterprise or Program section | REQ-NNN | `category: Non-Functional`, `nfrSubType`, `measurableTarget` |
| Constraint | Requirements Register (Category: Constraint) | REQ-NNN | `category: Constraint` |
| Assumption | Requirements Register (Category: Assumption) | REQ-NNN | `category: Assumption` |
| Requirements governance process | Requirements Register executive summary | — | Prose context |

**NFR coverage check:** After all NFR questions, display the coverage status:
```
NFR Coverage: Availability ✅ | Reliability ⬜ | Performance ✅ | Security ✅ | Usability ⬜ | Maintainability ⬜ | Portability ➖ | Compatibility ✅ | Recoverability ✅
⬜ = not answered  ➖ = not applicable  ✅ = captured
```
Offer to skip remaining uncovered categories or continue.

**Facilitation Notes:**
- Run this session before Phase A interviews — requirements drive the Architecture Vision, not the reverse.
- NFR questions often surface unstated assumptions. When a stakeholder says "it must be fast", ask: "What does fast mean specifically — for whom, under what load, measured how?"
- Requirements without measurable targets cannot be tested. Refuse to mark an NFR as Approved until a measurable target is agreed.
- Ask for any existing SLAs, service management agreements, or IT policy documents — they contain implicit NFRs that would otherwise be missed.
- If no traceability process exists, recommend adopting the Traceability Matrix from the engagement start rather than retrofitting it.

---

## Advanced Practitioner Questions by Phase

These questions probe economic reasoning, decision quality, failure mode symptoms, and maturity level. Use them when the engagement is at L3+ or when the stakeholder is a senior practitioner. Mark each as `[ADVANCED]` when presenting.

### Preliminary Phase — Advanced
1. **[ADVANCED]** How is the architecture capability funded — as a persistent operating cost or as project overhead? (Tests Failure Mode 2: Centralized Bottleneck)
2. **[ADVANCED]** What percentage of architecture team time is spent on conversations vs. document production? (Elite habit: 70/30 rule)
3. **[ADVANCED]** What is the average decision latency for architecture questions — and what is the target? (Tests maturity L3+ indicator)
4. **[ADVANCED]** How are architecture standards maintained — as a static document or as a product with owners, consumers, and adoption metrics? (Tests advanced pattern: Architecture as Product)
5. **[ADVANCED]** What happens to a project that does not comply with architecture standards? (Tests Failure Mode 3: Fake Governance)

### Phase A — Advanced
1. **[ADVANCED]** Can you quantify the gap between current and desired state in economic terms (cost, risk, revenue)? (Deep tactic: strategic tension)
2. **[ADVANCED]** Have you built multiple candidate visions and evaluated trade-offs between them? (Deep tactic: multiple visions)
3. **[ADVANCED]** What are the success metrics that must be met before this vision is approved to proceed to Phase B? (Deep tactic: success metrics before B)
4. **[ADVANCED]** Who has co-created this vision with business leaders — and who has not been consulted? (Hidden mechanic: vision as negotiation tool)
5. **[ADVANCED]** If the full vision cannot be delivered, what is the minimum viable vision that still justifies the investment? (Pattern: Option Architecture)

### Phase B — Advanced
1. **[ADVANCED]** For each capability: is it differentiating (competitive advantage) or commodity (should be standardized)? (Deep tactic: differentiate vs commodity)
2. **[ADVANCED]** How is each capability linked to a value stream and a KPI or revenue/cost driver? (Deep tactic: capability-value stream-KPI linkage)
3. **[ADVANCED]** Does the current org design support the target capability model — or does the org need to change? (Deep tactic: challenge org design)
4. **[ADVANCED]** Where is the business ambiguous — and how does this architecture compress that ambiguity into coherent constraints? (Hidden mechanic: compression function)
5. **[ADVANCED]** Have you identified "where to play" and "how to win" — or only mapped processes? (Deep tactic: strategic focus)

### Phase C — Advanced
1. **[ADVANCED]** Is data treated as a product with ownership, quality SLAs, and lifecycle governance? (Deep tactic: data as product)
2. **[ADVANCED]** Are API contracts and event schemas defined before tools are selected? (Deep tactic: interoperability early)
3. **[ADVANCED]** What measurable criteria will be used to rationalize applications — cost, risk, duplication, or just age? (Deep tactic: rationalize with metrics)
4. **[ADVANCED]** Do data and application boundaries align with business domains? (Pattern: Fracture Planes)
5. **[ADVANCED]** Who owns each critical data domain — and what happens when ownership is ambiguous? (Hidden mechanic: data as power structure)
6. **[ADVANCED]** Are ABBs defined before any vendor or product is named? (Tests vendor-first anti-pattern)
7. **[ADVANCED]** Can every ABB trace to at least one REQ-NNN and one CAP-NNN? (Tests ABB validation)

### Phase D — Advanced
1. **[ADVANCED]** Are technology standards core (mandatory enterprise-wide) or flexible (domain-specific)? Is there a defined flexible zone? (Deep tactic: standardize for leverage)
2. **[ADVANCED]** Are there pre-approved golden paths that teams can adopt without central review? (Deep tactic: golden paths)
3. **[ADVANCED]** Is observability and resilience embedded in technology standards from day one? (Deep tactic: design for failure)
4. **[ADVANCED]** How is cloud adoption changing team structures, funding, and decision rights — not just hosting? (Deep tactic: cloud as operating model)
5. **[ADVANCED]** Do standards have consumers, owners, and adoption metrics — or are they static documents? (Hidden mechanic: standards as product)
6. **[ADVANCED]** Is every SBB selected against a defined ABB, or are products chosen before logical components are named? (Tests vendor-first anti-pattern)
7. **[ADVANCED]** For each SBB: what is the exit cost and timeline if the vendor relationship fails? (Tests lock-in awareness)
8. **[ADVANCED]** Are fitness functions or conformance tests defined for each SBB before procurement? (Tests T4-FITNESS compliance)

### Phase E — Advanced
1. **[ADVANCED]** Does every work package deliver measurable business value, not just close a technical gap? (Deep tactic: value increments)
2. **[ADVANCED]** How are work packages prioritized — by impact, by feasibility, or by loudest voice? (Deep tactic: impact × feasibility)
3. **[ADVANCED]** What are the realistic transition architectures between baseline and target — not just the ideal end state? (Deep tactic: transition architectures)
4. **[ADVANCED]** What trade-offs are explicit in the roadmap — what is deferred and what is the risk of deferral? (Deep tactic: expose trade-offs)
5. **[ADVANCED]** If the budget were halved, which goals and work packages would you protect? (Tests economic reasoning)
6. **[ADVANCED]** Does every story trace to at least one REQ-NNN and one SBB-NNN? (Tests story traceability)
7. **[ADVANCED]** Are enabler stories explicitly tagged and linked to architectural runway requirements? (Tests architectural runway visibility)
8. **[ADVANCED]** Is each story decomposable into 2–5 tasks, or are stories too large (epic-sized) or too small (task-level)? (Tests story sizing)

### Phase F — Advanced
1. **[ADVANCED]** Is benefits realization tracked per wave — and how is it measured? (Deep tactic: optimize for value delivery)
2. **[ADVANCED]** What is the risk exposure per migration wave — what breaks if a wave fails? (Deep tactic: risk exposure)
3. **[ADVANCED]** Are there clear exit criteria for legacy systems — without which they will live forever? (Deep tactic: legacy exit criteria)
4. **[ADVANCED]** Does the plan include rollback paths and off-ramps — or is it all-or-nothing? (Deep tactic: maintain flexibility)
5. **[ADVANCED]** Can the migration plan articulate value in financial terms (TCO, cost of change, risk reduction) to finance? (Tests Failure Mode 4: Misalignment with Finance)

### Phase G — Advanced
1. **[ADVANCED]** Is governance provided through embedded guidance or remote review? (Deep tactic: embedded guidance)
2. **[ADVANCED]** Are conformance checks automated in CI/CD, or does every deployment wait for manual approval? (Deep tactic: automated checks)
3. **[ADVANCED]** Is governance effort focused on high-risk, irreversible decisions — or does it review everything? (Deep tactic: focus on high-risk)
4. **[ADVANCED]** Are deviations accepted (with risk sign-off) or remediated — not just documented? (Deep tactic: track deviations)
5. **[ADVANCED]** How is governance measured — by decision speed and delivery outcomes, or by checklist coverage? (Deep tactic: measure by outcomes)

### Phase H — Advanced
1. **[ADVANCED]** Is the target architecture updated continuously, or only during major projects? (Deep tactic: living system)
2. **[ADVANCED]** What leading indicators are tracked to trigger mini-ADM cycles before crises emerge? (Deep tactic: leading indicators)
3. **[ADVANCED]** Are obsolete architectures retired explicitly, or do they linger indefinitely? (Deep tactic: retire obsolete)
4. **[ADVANCED]** Are implementation learnings fed back into principles, standards, and reference architectures? (Deep tactic: feed learnings back)
5. **[ADVANCED]** How often does the architecture team run mini-ADM cycles for incremental change? (Tests maturity L5 indicator)
