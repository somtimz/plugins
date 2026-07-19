# Phase D — Technology Architecture Interview


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
