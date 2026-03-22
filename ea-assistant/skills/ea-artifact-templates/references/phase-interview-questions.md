# Phase Interview Question Bank

Curated interview questions for each TOGAF ADM phase, with output routing tables mapping responses to ea-assistant artifact template fields.

---

## Preliminary Phase Interview

**Goal:** Establish architecture principles and governance model

**Key questions:**
1. What are the top three strategic goals for your organisation over the next three years?
2. What constraints apply to this engagement — regulatory, financial, or technical?
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

**Goal:** Define scope, concerns, and high-level target

**Key questions:**
1. What is the business problem or opportunity driving this engagement?
2. What does success look like at the end of this engagement?
3. Who are the key stakeholders and what are their primary concerns?
4. What is explicitly in scope and out of scope for this engagement?
5. What known constraints or assumptions should be documented upfront?
6. What existing architecture assets, decisions, or documents are relevant?
7. What is the desired timeline for completing this work?
8. What are the biggest risks that could derail this engagement?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Business problem/opportunity | Architecture Vision | `{{business_problem}}` |
| Success criteria | Architecture Vision | `{{success_criteria}}` |
| Statement of Architecture Work | Statement of Architecture Work | `{{engagement_justification}}` |
| Key stakeholders | Stakeholder Map | `{{stakeholder_list}}` |
| Stakeholder concerns | Stakeholder Map | `{{stakeholder_concerns}}` |
| In-scope items | Architecture Vision | `{{scope_inclusions}}` |
| Out-of-scope items | Architecture Vision | `{{scope_exclusions}}` |
| Constraints | Statement of Architecture Work | `{{constraints}}` |
| Assumptions | Statement of Architecture Work | `{{assumptions}}` |
| Existing architecture assets | Architecture Vision | `{{existing_assets}}` |
| Timeline | Statement of Architecture Work | `{{timeline}}` |
| Key risks | Architecture Vision | `{{key_risks}}` |

**Facilitation Notes:**
- The "what does success look like" question is the most important in this phase — get a concrete, measurable answer rather than accepting vague aspirations.
- Scope boundary questions often generate the most debate; document disagreements explicitly rather than forcing premature consensus.
- Ask stakeholders to describe their concerns in terms of consequences: "what happens if this is not addressed?" reveals priority more reliably than a ranking exercise.
- A brief stakeholder RACI draft during this session prevents scope and accountability conflicts later.

---

## Phase B — Business Architecture Interview

**Goal:** Define business capabilities, processes, and gaps

**Key questions:**
1. What are the primary business functions performed by the organisation or the area in scope?
2. Walk me through the key end-to-end business processes — from customer/trigger to outcome.
3. Where are the biggest pain points or inefficiencies in current business operations?
4. What capabilities are missing that are needed to achieve the target state?
5. How is the organisation structured — what divisions, teams, or geographies are involved?
6. What are the priority business outcomes this architecture must support?
7. What does the business need to look like in three to five years?
8. How is performance measured today — what KPIs or metrics matter most?

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

**Facilitation Notes:**
- Run a capability mapping workshop using a whiteboard or collaborative tool — asking participants to place capabilities on a heat map (invest/maintain/retire) surfaces priorities faster than questions alone.
- Process walk-throughs are best done with operational staff, not just managers; the "how it actually works" often differs significantly from the "how it should work" described by leadership.
- When identifying gaps, ask "what would you do if you had no constraints?" to surface aspirational capabilities before applying reality checks.
- The KPIs question links business architecture to measurable outcomes — use answers to define gap analysis criteria.

---

## Phase C — Information Systems Interview

**Goal:** Understand data entities and application portfolio

**Key questions:**
1. What are the key data domains in your organisation — the major categories of information you manage?
2. Which applications support each of the business functions we identified?
3. Which applications are considered strategic investments, and which are candidates for replacement?
4. Where do you have data duplication or inconsistency problems across systems?
5. What are the critical integration points between applications?
6. Are there regulatory requirements governing specific data (e.g., privacy, retention, classification)?
7. Who owns each application and each major data domain?
8. What is the single biggest challenge you face with your data and application landscape today?

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

**Facilitation Notes:**
- Bring an application inventory template to the session pre-populated with known systems — asking people to add to a list is more productive than asking them to recall from memory.
- The "strategic vs replacement" question often surfaces political tensions; frame it as investment prioritisation rather than a performance critique of existing systems.
- Data ownership questions frequently reveal ungoverned domains — treat "no one owns it" as a gap finding, not an oversight to skip.
- Ask for data flow diagrams or integration documentation after the session; verbal descriptions of integration points are rarely complete.

---

## Phase D — Technology Architecture Interview

**Goal:** Understand current and desired technology platform

**Key questions:**
1. What is your current technology stack — key platforms, infrastructure, and tooling?
2. What technology standards are mandated within the organisation or by your industry?
3. What technology capabilities are missing from the current platform?
4. What is your organisation's cloud strategy — where do you want to be in three years?
5. What technology constraints must the architecture respect (vendor lock-in, existing contracts, skills)?
6. What does your technology landscape need to look like in three years?
7. Where is your technology debt concentrated — which parts of the platform are most at risk?
8. What security or compliance requirements directly affect technology decisions?

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

**Facilitation Notes:**
- Open with "what keeps you up at night about your current technology?" — this surfaces the real pain points faster than a structured inventory review.
- Technology debt questions are best answered by infrastructure and platform engineers, not just IT leadership; schedule a separate technical session if needed.
- Cloud strategy answers often reflect aspirations rather than funded plans; probe for budget commitment and timeline to distinguish strategy from wishful thinking.
- Capture mandated standards as constraints in both Technology Architecture and the Requirements Register — they frequently constrain solution options in phases E and F.

---

## Phase E/F — Opportunities and Roadmap Interview

**Goal:** Prioritise work packages and build the roadmap

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
| Investment budget | Migration Plan | `{{investment_budget}}` |
| Target timeline | Architecture Roadmap | `{{delivery_timeline}}` |
| Sequencing dependencies | Architecture Roadmap | `{{sequencing_dependencies}}` |
| Migration Plan dependencies | Migration Plan | `{{migration_dependencies}}` |
| Acceptable transition states | Migration Plan | `{{transition_states}}` |
| Minimum viable delivery | Architecture Roadmap | `{{minimum_viable_scope}}` |
| Delivery risks | Architecture Roadmap | `{{delivery_risks}}` |
| Migration Plan risks | Migration Plan | `{{migration_risks}}` |

**Facilitation Notes:**
- The "halved budget" question is the most powerful prioritisation tool in this phase — it forces genuine trade-off decisions rather than keeping everything on the roadmap as "high priority."
- In-flight project alignment is frequently underestimated; request a project portfolio list before the session and map conflicts in advance.
- Sequencing questions work well as a group exercise where participants physically order work packages — disagreements in the room are better surfaced now than during delivery.
- Acceptable transition states define architecture checkpoints; if the organisation cannot articulate them, the roadmap will lack governance anchors.

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
