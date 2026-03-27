# Phase Interview Question Bank

Curated interview questions for each TOGAF ADM phase, with output routing tables mapping responses to ea-assistant artifact template fields.

---

## Preliminary Phase Interview

**Goal:** Establish architecture principles and governance model

**Key questions:**
1. What are the top three strategic goals for your organisation over the next three years?
2. What constraints apply to this engagement? (select all that apply)
   - [ ] Regulatory — compliance obligations, legal requirements, data residency rules
   - [ ] Financial — budget cap, cost reduction target, limited investment capacity
   - [ ] Technical — existing platform lock-in, skills gap, mandated standards
   - [ ] Organisational — headcount limits, change capacity, political constraints
   - [ ] Time — fixed deadline, regulatory timeline, or programme dependency
   - [ ] Other: ___
3. Who are the key decision-makers for IT investment in your organisation?
4. Does an existing architecture governance body or process exist? If so, how does it operate?
5. What does good architecture practice look like in your organisation?
6. What existing frameworks, standards, or methodologies does the organisation follow?
7. How would you describe your organisation's risk appetite for technology change?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Strategic goals | Architecture Principles | `{{strategic_goals}}` |
| Regulatory constraints | Architecture Principles | `{{regulatory_constraints}}` |
| Financial constraints | Architecture Principles | `{{financial_constraints}}` |
| Technical constraints | Architecture Principles | `{{technical_constraints}}` |
| IT decision-makers | Stakeholder Map | `{{key_decision_makers}}` |
| Governance body | Architecture Principles | `{{existing_governance}}` |
| Good architecture definition | Architecture Principles | `{{architecture_definition}}` |
| Existing frameworks/standards | Architecture Principles | `{{existing_frameworks}}` |
| Risk appetite | Architecture Principles | `{{risk_appetite}}` |

**Facilitation Notes:**
- Run this as a structured workshop with senior leadership, not a one-on-one interview; competing priorities surface quickly in a group setting.
- Ask for written documentation of existing principles or standards before the session — gaps between stated and documented practice are significant findings.
- If no governance body exists, note this as a gap and flag it as a Preliminary phase deliverable rather than leaving it unaddressed.
- Use the risk appetite question to calibrate how bold or conservative the architecture recommendations should be.

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
   - Assign each confirmed goal a G-NNN ID and note which driver(s) it responds to.

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

*§6 Problems — the specific, observable symptoms that block objectives:*
8. For each objective: what specific, measurable symptoms are actively blocking or undermining its delivery today? (e.g. "The monthly close process takes 15 days due to manual reconciliation", "Mobile checkout abandonment is 68% — 2× the industry benchmark")
   - Assign each confirmed problem a PRB-NNN ID and link it to the objective(s) it blocks.
   - If a response is too broad and unfixable directly ("we have poor data culture"), it is an **Issue** — move it up.

*§1 Executive Summary / §8 Scope / §9–§15 — scope, constraints, and risks:*
9. What does success look like at the end of this engagement? → §1 Executive Summary
10. Who are the key stakeholders and what are their primary concerns? → §9 Stakeholders + Stakeholder Map
11. What is explicitly in scope and out of scope for this engagement? → §8 Scope
12. What known constraints or assumptions should be documented upfront? → §11 Constraints + §12 Assumptions
13. What existing architecture assets, decisions, or documents are relevant? → Statement of Architecture Work §3
14. What is the desired timeline for completing this work? → §8 Scope (Time Horizon) + SoAW
15. What are the biggest risks that could derail this engagement? → §14 Key Risks

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| External business drivers | Architecture Vision | `§2 Business Drivers` (DRV-NNN rows) |
| Internal business drivers | Architecture Vision | `§2 Business Drivers` (DRV-NNN rows) |
| Goals | Architecture Vision + engagement.json | `§3 Goals` (G-NNN rows) + `direction.goals[]` |
| Objectives | Architecture Vision + engagement.json | `§4 Objectives` (OBJ-NNN rows) + `direction.objectives[]` |
| Systemic issues | Architecture Vision | `§5 Issues` (ISS-NNN rows) |
| Specific problems | Architecture Vision | `§6 Problems` (PRB-NNN rows) |
| Performance metrics | engagement.json | `metrics[]` linked to OBJ-NNN |
| Success criteria | Architecture Vision | `§1 Executive Summary` + `§3 Goals` |
| Key stakeholders | Stakeholder Map | `{{stakeholder_list}}` |
| Stakeholder concerns | Stakeholder Map | `{{stakeholder_concerns}}` |
| Strategies | Architecture Vision + engagement.json | `§7 Strategic Direction Summary` (STR-NNN rows) + `direction.strategies[]` |
| Metrics | engagement.json | `§7 Strategic Direction Summary` (MET-NNN rows) + `metrics[]` |
| In-scope items | Architecture Vision | `§8 Scope — {{scope_in}}` |
| Out-of-scope items | Architecture Vision | `§8 Scope — {{scope_out}}` |
| Constraints | Statement of Architecture Work | `{{constraints}}` |
| Assumptions | Statement of Architecture Work | `{{assumptions}}` |
| Existing architecture assets | Statement of Architecture Work | `§3 Approach` (reference existing assets as inputs) |
| Timeline | Statement of Architecture Work | `{{timeline}}` |
| Key risks | Architecture Vision | `§14 Key Risks` (table rows) |
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

---

## Phase B — Business Architecture Interview

**Goal:** Define business capabilities, processes, gaps, and business goals

**Key questions:**
1. What are the primary business functions performed by the organisation or the area in scope?
2. Walk me through the key end-to-end business processes — from customer/trigger to outcome.
3. Where are the biggest pain points or inefficiencies in current business operations?
4. What capabilities are missing that are needed to achieve the target state?
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

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Primary business functions | Business Architecture | `{{business_functions}}` |
| Key end-to-end processes | Business Architecture | `{{key_processes}}` |
| Pain points/inefficiencies | Gap Analysis | `{{current_state_gaps}}` |
| Missing capabilities | Business Architecture | `{{capability_gaps}}` |
| Gap Analysis | Gap Analysis | `{{business_gaps}}` |
| Organisation structure | Business Architecture | `{{org_structure}}` |
| Priority business outcomes | Business Architecture | `{{business_outcomes}}` |
| Future state description | Business Architecture | `{{future_state}}` |
| KPIs and metrics | Business Architecture | `{{performance_metrics}}` |
| Business direction (goals, objectives, strategies) | engagement.json + Business Capability Map | `direction.Business` + `{{business_direction}}` |
| Business metrics | engagement.json + Business Capability Map | `metrics.Business` + `{{business_metrics}}` |

**Facilitation Notes:**
- Run a capability mapping workshop using a whiteboard or collaborative tool — asking participants to place capabilities on a heat map (invest/maintain/retire) surfaces priorities faster than questions alone.
- Process walk-throughs are best done with operational staff, not just managers; the "how it actually works" often differs significantly from the "how it should work" described by leadership.
- When identifying gaps, ask "what would you do if you had no constraints?" to surface aspirational capabilities before applying reality checks.
- The KPIs question links business architecture to measurable outcomes — use answers to define gap analysis criteria.

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
9. *(If Data direction not yet defined)* Capture Data direction using the three-type model:
   - **Data goal** example: "Have a single source of truth for customer data" (qualitative, no deadline)
   - **Data objective** example: "Reduce duplicate customer records by 90% by June 2026" (measurable + deadline)
   - **Data strategy** example: "Implement a master data management platform" (approach, not outcome)

10. *(If Application direction not yet defined)* Capture Application direction using the three-type model:
    - **Application goal** example: "Operate a modern, composable application landscape"
    - **Application objective** example: "Decommission 3 legacy systems by Q2 2027"
    - **Application strategy** example: "Adopt SaaS-first for commodity capabilities"

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Key data domains | Data Architecture | `{{data_domains}}` |
| Applications per function | Application Architecture | `{{application_inventory}}` |
| Strategic applications | Application Architecture | `{{strategic_applications}}` |
| Replacement candidates | Application Architecture | `{{replacement_candidates}}` |
| Gap Analysis (application) | Gap Analysis | `{{application_gaps}}` |
| Data duplication issues | Data Architecture | `{{data_quality_issues}}` |
| Integration points | Application Architecture | `{{integration_points}}` |
| Regulatory data requirements | Requirements Register | `{{data_regulatory_requirements}}` |
| Data Architecture gaps | Gap Analysis | `{{data_gaps}}` |
| Application ownership | Application Architecture | `{{application_ownership}}` |
| Data domain ownership | Data Architecture | `{{data_ownership}}` |
| Key data/app challenge | Gap Analysis | `{{key_challenge}}` |
| Data direction (goals, objectives, strategies) | engagement.json + Logical Data Model | `direction.Data` + `{{data_direction}}` |
| Data metrics | engagement.json + Logical Data Model | `metrics.Data` + `{{data_metrics}}` |
| Application direction (goals, objectives, strategies) | engagement.json + Application Portfolio Catalogue | `direction.Application` + `{{application_direction}}` |
| Application metrics | engagement.json + Application Portfolio Catalogue | `metrics.Application` + `{{application_metrics}}` |

**Facilitation Notes:**
- Bring an application inventory template to the session pre-populated with known systems — asking people to add to a list is more productive than asking them to recall from memory.
- The "strategic vs replacement" question often surfaces political tensions; frame it as investment prioritisation rather than a performance critique of existing systems.
- Data ownership questions frequently reveal ungoverned domains — treat "no one owns it" as a gap finding, not an oversight to skip.
- Ask for data flow diagrams or integration documentation after the session; verbal descriptions of integration points are rarely complete.

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

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Current tech stack | Technology Architecture | `{{current_tech_stack}}` |
| Mandated standards | Technology Architecture | `{{mandated_standards}}` |
| Missing tech capabilities | Gap Analysis | `{{technology_gaps}}` |
| Technology Architecture gaps | Gap Analysis | `{{tech_capability_gaps}}` |
| Cloud strategy | Technology Architecture | `{{cloud_strategy}}` |
| Technology constraints | Technology Architecture | `{{tech_constraints}}` |
| Requirements Register (tech) | Requirements Register | `{{technology_requirements}}` |
| Future tech landscape | Technology Architecture | `{{future_tech_state}}` |
| Technology debt | Gap Analysis | `{{tech_debt}}` |
| Security/compliance requirements | Requirements Register | `{{security_requirements}}` |
| Technology direction (goals, objectives, strategies) | engagement.json + Technology Standards Catalogue | `direction.Technology` + `{{technology_direction}}` |

**Facilitation Notes:**
- Open with "what keeps you up at night about your current technology?" — this surfaces the real pain points faster than a structured inventory review.
- Technology debt questions are best answered by infrastructure and platform engineers, not just IT leadership; schedule a separate technical session if needed.
- Cloud strategy answers often reflect aspirations rather than funded plans; probe for budget commitment and timeline to distinguish strategy from wishful thinking.
- Capture mandated standards as constraints in both Technology Architecture and the Requirements Register — they frequently constrain solution options in phases E and F.

---

## Phase E — Opportunities and Solutions Interview

**Goal:** Prioritise work packages and build the initial architecture roadmap

**Key questions:**
1. Which capability gaps identified in earlier phases are the highest priority to close?
2. What projects are already in flight that this roadmap must align with or avoid conflicting with?
3. What is the available investment budget and target delivery timeline?
4. What sequencing dependencies exist — which changes must happen before others can begin?
5. What are acceptable transition states — what does "good enough for now" look like at each stage?
6. If the budget were halved, what would you deliver first?
7. What are the biggest risks to delivering this roadmap?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Priority capability gaps | Architecture Roadmap | `{{priority_gaps}}` |
| In-flight projects | Architecture Roadmap | `{{existing_projects}}` |
| Investment budget | Architecture Roadmap | `{{investment_budget}}` |
| Target timeline | Architecture Roadmap | `{{delivery_timeline}}` |
| Sequencing dependencies | Architecture Roadmap | `{{sequencing_dependencies}}` |
| Acceptable transition states | Architecture Roadmap | `{{transition_states}}` |
| Minimum viable delivery | Architecture Roadmap | `{{minimum_viable_scope}}` |
| Delivery risks | Architecture Roadmap | `{{delivery_risks}}` |

**Facilitation Notes:**
- The "halved budget" question is the most powerful prioritisation tool in this phase — it forces genuine trade-off decisions rather than keeping everything on the roadmap as "high priority."
- In-flight project alignment is frequently underestimated; request a project portfolio list before the session and map conflicts in advance.
- Sequencing questions work well as a group exercise where participants physically order work packages — disagreements in the room are better surfaced now than during delivery.
- Acceptable transition states define architecture checkpoints; if the organisation cannot articulate them, the roadmap will lack governance anchors.

---

## Phase F — Migration Planning Interview

**Goal:** Define the practical wave plan, resourcing, cut-over approach, and rollback strategy for delivering the architecture roadmap

**Key questions:**
1. How should the work packages be grouped into delivery waves — what natural groupings exist based on dependency, risk, or business value?
2. For each wave, what resources and skills are required, and are they available within the planned timeframe?
3. What is the organisation's capacity for change — how much disruption can be absorbed per wave without affecting business operations?
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

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Wave groupings | Migration Plan | `{{wave_1_name}}` / `{{wave_2_name}}` |
| Resource requirements per wave | Migration Plan | `{{migration_overview}}` |
| Organisational change capacity | Migration Plan | `{{migration_overview}}` |
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

---

## Requirements Management Interview

**Goal:** Establish requirements lifecycle management

**Key questions:**
1. How are requirements currently gathered and documented in your organisation?
2. Who has authority to approve and prioritise requirements?
3. How is traceability maintained from business need through to implementation?
4. How are conflicting requirements resolved when they arise?
5. At what cadence are requirements reviewed and updated during the engagement?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Requirements gathering approach | Requirements Register | `{{requirements_process}}` |
| Documentation standards | Requirements Register | `{{documentation_standards}}` |
| Approval/prioritisation authority | Requirements Register | `{{approval_authority}}` |
| Traceability approach | Traceability Matrix | `{{traceability_approach}}` |
| Traceability tools | Traceability Matrix | `{{traceability_tools}}` |
| Conflict resolution process | Requirements Register | `{{conflict_resolution}}` |
| Review and update cadence | Requirements Register | `{{review_cadence}}` |

**Facilitation Notes:**
- Requirements management interviews are often skipped under pressure to move to design; run this session early and treat its outputs as the foundation for all subsequent artifact population.
- Approval authority questions frequently surface competing stakeholders — documenting a single decision-maker or RACI upfront prevents delays later.
- If no traceability process exists, recommend adopting the Traceability Matrix from the start of the engagement rather than retrofitting it at the end.
- Ask for any existing requirements documents before the session; starting from what already exists is faster than starting from a blank page.
