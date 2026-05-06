# TOGAF Advanced Practitioner Maturity Model

A 5-level maturity model for assessing enterprise architecture practice maturity. Each level describes what teams do differently, typical indicators, common blockers, and how to advance.

This model is designed for self-assessment, team coaching, and engagement scoping. Use it to:
- Diagnose the current maturity of an architecture function
- Set realistic improvement targets
- Tailor ADM execution to the team's actual maturity (not aspirational maturity)
- Communicate maturity gaps to sponsors and executives

---

## Level 1 — Framework Compliance

### What It Looks Like
Architecture is treated as a compliance exercise. Teams follow TOGAF phases rigidly, produce heavy documentation, and view architecture as overhead imposed on delivery.

### Typical Indicators
- ADM followed phase-by-phase with minimal tailoring
- Artifact completeness measured by volume, not value
- Governance is review-heavy and approval-centric
- Architecture team is isolated from delivery
- Success measured by "artifacts produced" and "checklists passed"
- Stakeholders view architecture as a bottleneck
- Little to no economic traceability (cost, value, risk)

### What Teams Do Differently
- Produce architecture documents because they are required, not because they drive decisions
- Baseline documentation is exhaustive and often redundant
- Target architectures are static diagrams with no implementation pathway
- Gap analysis lists deficits without prioritization or economic framing
- Roadmaps are wish lists with no funding alignment
- Governance is a series of review meetings with go/no-go gates

### Typical Blockers
- Sponsors who equate architecture with documentation
- Delivery teams who bypass architecture to meet deadlines
- No clear linkage between architecture and funding
- Architecture team lacks decision rights or executive sponsorship

### How to Advance to Level 2
- Start measuring architecture by decision quality, not artifact volume
- Introduce tailoring: document which ADM phases are combined, skipped, or reordered
- Identify the top 5 decisions per engagement and focus architecture effort there
- Add economic framing to at least one artifact (e.g., Architecture Vision or Roadmap)
- Reduce artifact count by 30% — eliminate low-utility documents

---

## Level 2 — Tailored Execution

### What It Looks Like
TOGAF is adapted to the organization's context. Some business alignment exists. Governance is still review-heavy but beginning to show selectivity.

### Typical Indicators
- ADM phases are combined or reordered based on context
- Some artifacts trace to business outcomes
- Governance board reviews only high-impact items
- Architecture team engages with delivery on major decisions
- Success measured by "review items approved" and "standards compliance"
- Occasional economic justification in roadmap or business case

### What Teams Do Differently
- Tailor ADM based on engagement type (greenfield, modernization, compliance)
- Baseline documentation is "just enough" rather than exhaustive
- Target architectures include transition states
- Gap analysis prioritizes gaps by impact and feasibility
- Roadmaps show sequencing but limited funding alignment
- Governance is selective but still meeting-centric

### Typical Blockers
- Architecture still seen as "advisory" rather than "decision-support"
- Limited automated governance — manual reviews dominate
- Reference architectures exist but are rarely used
- Metrics focus on process compliance, not delivery outcomes
- Resistance from delivery teams who view architecture as "extra work"

### How to Advance to Level 3
- Embed architects in product/delivery teams for at least one pilot
- Create reusable reference architectures for the top 3 domains
- Shift governance from "gates" to "guardrails" for one phase
- Automate at least one compliance check in CI/CD
- Measure architecture by delivery outcomes (cycle time, defect rate, value realized)

---

## Level 3 — Integrated Delivery

### What It Looks Like
Architecture is embedded in agile delivery. Continuous feedback loops exist. Reference architectures are actively used. Governance is lighter and more automated.

### Typical Indicators
- Architects are embedded in product teams or squads
- ADM phases align with agile increments (PIs, sprints)
- Reference architectures and patterns accelerate delivery
- Automated checks enforce standards in pipelines
- Architecture decisions are tracked as first-class artifacts (ADRs)
- Success measured by "time-to-decision" and "pattern reuse rate"
- Economic framing is standard in roadmap and gap analysis

### What Teams Do Differently
- Architecture work is planned in the same backlogs as delivery
- Baseline and target states are updated continuously, not just at phase gates
- Gap analysis feeds directly into backlog items and work packages
- Roadmaps are living documents updated per quarter
- Governance is guardrail-based with automated enforcement
- Architecture repository is treated as a knowledge graph, not a document store

### Typical Blockers
- Scaling embedded architecture across all teams is expensive
- Legacy systems resist domain-oriented restructuring
- Finance and portfolio management are not yet aligned with architecture
- Architecture KPIs are not yet linked to enterprise OKRs
- Some teams still bypass architecture for speed

### How to Advance to Level 4
- Tie architecture decisions to funding and prioritization logic
- Introduce fitness functions (automated architectural checks) across all pipelines
- Use capability heatmaps to drive investment prioritization
- Federate architecture: enterprise architects set guardrails, domain architects make local decisions
- Measure governance effectiveness by decision speed, not control coverage

---

## Level 4 — Value-Driven Architecture

### What It Looks Like
Architecture consistently shapes investment, standards, and strategic sequencing. Economic reasoning is explicit. Governance is automated and lightweight.

### Typical Indicators
- Architecture influences funding allocation and portfolio prioritization
- Total cost of ownership (TCO) is standard in technology decisions
- Technical debt is visible in financial terms
- Fitness functions enforce architecture continuously
- Governance is automated with exception-only human review
- Success measured by "value realized per architecture decision" and "cost avoided"
- Architecture team operates as a product team with SLAs

### What Teams Do Differently
- Every significant architecture decision includes an economic analysis
- Roadmaps are sequenced by value delivery, not just technical dependency
- Legacy system retirement has explicit exit criteria and funding
- Architecture principles are enforceable constraints in pipelines
- Standards catalog is minimal, current, and actively pruned
- Architecture Board functions as a decision marketplace, not a review committee

### Typical Blockers
- Cultural resistance to "financializing" architecture
- Difficulty quantifying architecture value in hard dollars
- Organizational politics around funding reallocation
- Some executives still view architecture as "IT overhead"
- Metrics require cross-functional data that is hard to collect

### How to Advance to Level 5
- Treat architecture as a continuously evolving adaptive system
- Optimize for organizational learning and adaptability
- Architecture capability is self-improving based on feedback loops
- Mini-ADM cycles run continuously for incremental changes
- Architecture and organizational design are co-evolved

---

## Level 5 — Adaptive Enterprise System

### What It Looks Like
Architecture operates as a federated, continuously evolving system for managing complexity, risk, and change at scale. The organization optimizes for learning and adaptability.

### Typical Indicators
- Architecture evolves continuously, not just at major transformation points
- Federated model: enterprise architects set direction, domain architects adapt locally
- Mini-ADM cycles run for incremental changes without full phase overhead
- Architecture learnings feed back into principles and standards automatically
- Organization design and system architecture are co-evolved
- Success measured by "organizational adaptability" and "decision quality over time"
- Architecture is invisible — it is embedded in how the organization operates

### What Teams Do Differently
- Architecture principles are updated based on implementation learnings
- Standards catalog is pruned continuously; obsolete standards are retired
- Architecture repository is a knowledge graph with automated updates
- Internal enablement (training, communities of practice) is a core function
- Architecture team members are coaches and mentors, not gatekeepers
- The boundary between "architecture" and "delivery" has dissolved

### Typical Blockers
- Very few organizations reach Level 5. It requires:
  - Sustained executive sponsorship over multiple years
  - A culture that values learning over control
  - Technology that supports real-time architecture visibility
  - Organizational design that aligns with system boundaries

---

## Quick Assessment Questions

Use these questions to diagnose current maturity:

| Question | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| How do you measure architecture success? | Artifact volume | Process compliance | Delivery outcomes | Value realized | Organizational adaptability |
| How is governance enforced? | Meetings & approvals | Selective reviews | Guardrails + automation | Automated + exception review | Embedded in operations |
| Who makes architecture decisions? | Central EA team | EA + senior stakeholders | EA + delivery teams | Federated (enterprise + domain) | Distributed with alignment |
| How often do you update target architecture? | Once per engagement | At phase gates | Quarterly | Continuously | Continuously, automatically |
| How do you handle standards? | Accumulate | Maintain | Prune occasionally | Active pruning | Self-updating |
| What is the Architecture Board? | Review committee | Advisory body | Decision marketplace | Decision system | Invisible (embedded) |
| How is architecture funded? | Project overhead | Partially dedicated | Persistent capability | Product team | Core organizational function |

---

## Maturity-Based Compliance Expectations

| Level | Compliance Expectations |
|---|---|
| **L1** | All Tier 3 rules met; heavy documentation; checklist-driven |
| **L2** | Tier 3 rules met with tailoring justification; selective depth |
| **L3** | Tier 3 + economic traceability (cost/value/risk) in key artifacts |
| **L4** | Tier 3 + Tier 4 (automated enforcement, fitness functions) + value metrics |
| **L5** | Tier 3 + Tier 4 + self-updating compliance (architecture learns from implementation) |

---

*See also: `practitioner-tips.md` for the 50 tips and 70 deep tactics, `advanced-patterns.md` for implementation patterns, `failure-modes.md` for common maturity traps.*
