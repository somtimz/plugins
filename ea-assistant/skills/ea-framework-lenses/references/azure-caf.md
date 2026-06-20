# Azure Cloud Adoption Framework (CAF) Lens

Maps the Azure CAF methodologies onto the TOGAF ADM. CAF differs from the AWS Well-Architected lens in shape: it is an **adoption lifecycle** (strategy → plan → ready → adopt → govern → manage → secure), not a set of workload pillars — so this lens is strongest in Phases A, B, E, and F, where adoption sequencing and landing-zone readiness are decided. For workload-quality review on Azure, the Azure Well-Architected pillars largely mirror the AWS lens checklist — reuse `aws-well-architected.md` checklists with Azure service names at the SBB level.

## Pillars

*(CAF calls these methodologies; they serve as this lens's pillars.)*

### Strategy
Define business justification and expected outcomes of cloud adoption. Principles: document motivations (migration-triggered vs innovation-driven); define measurable business outcomes; build the business case on TCO honesty, not hope.

### Plan
Convert strategy into an actionable adoption plan. Principles: rationalise the digital estate using the five Rs (rehost, refactor, rearchitect, rebuild, replace); plan skilling/organisational readiness alongside workloads; sequence by business value and dependency.

### Ready
Prepare the cloud environment before workloads land. Principles: landing zones as the unit of environment readiness (identity, network, governance, billing scaffolding in place first); environment-as-code; design for scale-out of subscriptions/management groups.

### Adopt
Migrate and modernise workloads. Principles: migrate in waves with explicit promotion criteria; modernise only where rationalisation justified it; innovate on cloud-native services where differentiation matters.

### Govern
Establish guardrails that grow with adoption. Disciplines: cost management, security baseline, resource consistency, identity baseline, deployment acceleration. Principles: incremental governance (guardrails scale with risk); policy-as-code over manual review.

### Manage
Operate what was adopted. Principles: define operations baseline (inventory, visibility, compliance, protect/recover); set business commitments (criticality, SLA) per workload; expand operations only where commitments demand it.

### Secure
Continuous security posture across the lifecycle. Principles: risk-driven prioritisation; modernise security posture alongside workloads; treat security as ongoing, not a gate. *(Hand depth to the `ea-security` skill — this pillar's checklist stays at adoption-process level.)*

## ADM Mapping

| Pillar | Primary ADM phase(s) | Target artifact(s) |
|---|---|---|
| Strategy | A | Architecture Vision (drivers, goals, business case framing) |
| Plan | B, E, F | Business Architecture (capability/portfolio), Architecture Roadmap (five-Rs disposition per WP), Migration Plan |
| Ready | D | Technology Architecture (landing zone = environment ABBs/SBBs) |
| Adopt | F, G | Migration Plan (waves), Implementation Governance Plan |
| Govern | Prelim, G | Governance Framework, Architecture Principles, Implementation Governance Plan |
| Manage | G, H | Implementation Governance Plan (operations baseline), Change Request handling |
| Secure | Cross-cutting | Defer to `/ea-security-review` (SABSA/ISO/NIST) |

## Review Checklist

### Strategy (Phase A artifacts)
1. Are cloud-adoption motivations documented and classified (cost/exit pressure vs innovation), with evidence (DRV-NNN)?
2. Are business outcomes measurable (OBJ-NNN with target and deadline), not aspirations?
3. Does the business case account for dual-running and skilling costs, not just infrastructure deltas? *(reinforces T4-ECON)*

### Plan (Phase B/E artifacts)
1. Has the digital estate been rationalised — does every in-scope workload carry a five-Rs disposition with rationale?
2. Are dispositions recorded as decisions (A3/ADR) where hard to reverse (rebuild/replace), with rearchitect-vs-rehost trade-offs stated?
3. Is organisational readiness (skills, operating model) planned as work packages, not assumed?
4. Is wave sequencing driven by business value and dependency rather than technical convenience?

### Ready (Phase D artifacts)
1. Is a landing-zone design specified (identity, network topology, subscription/management-group structure, policy scaffolding) before workload architecture?
2. Is the environment defined as code with a repeatable vending process for new workload environments?
3. Are shared platform services (connectivity, DNS, key management, logging) ABBs with explicit SBB choices?

### Govern (Prelim/G artifacts)
1. Do the five governance disciplines each have an owner and a policy mechanism (POL-NNN → CST-NNN chain)?
2. Are guardrails automated (Azure Policy / policy-as-code equivalents) rather than review-board-only? *(reinforces T4-FITNESS)*
3. Is governance scaled to current risk — minimal viable guardrails now, with defined triggers to tighten?

### Manage (G/H artifacts)
1. Does every workload have a criticality classification and matching operations commitment (SLA, recovery)?
2. Is there an operations baseline (inventory, monitoring, backup) applied by default to everything adopted?
3. Do Phase H change triggers include cloud-spend and platform-deprecation signals (links to THR-NNN)?

## Interview Questions

### Phase A
1. What is driving cloud adoption — cost/datacentre exit, agility, or innovation — and what evidence supports it? → DRV-NNN; Architecture Vision §4
2. What measurable outcomes will prove adoption succeeded, by when? → OBJ-NNN
3. Who owns the cloud business case, and does it include skilling and dual-running costs? → Architecture Vision; A3 row

### Phase B
1. Which capabilities are differentiating (candidates for rebuild/innovate) vs commodity (rehost/replace)? → Capability Model; five-Rs input
2. What organisational/skills changes does adoption require, and who owns them? → Business Architecture (workforce); WP-NNN candidates

### Phase E
1. What is the five-Rs disposition of each major workload cluster, and which dispositions are still contested? → Architecture Roadmap (per-WP disposition); PAD-NNN for contested
2. What must the landing zone provide before Wave 1 can land? → WP-NNN (readiness work package), Roadmap dependencies

### Phase F
1. What are the wave promotion criteria — what must be true before each workload group moves? → Migration Plan (wave entry/exit criteria)
2. How long will dual-running last per wave, and is its cost in the plan? → Migration Plan; T4-ECON framing

## Tagging Conventions

| Finding type | Capture as | Convention |
|---|---|---|
| Missing/unevidenced motivation or outcome | DRV-NNN / OBJ-NNN | `evidence` populated; source `Azure-CAF / Strategy` |
| Undecided workload disposition | PAD-NNN | Five-Rs choice deferred with expiry (T4-PREMAT) |
| Hard-to-reverse disposition (rebuild/replace) | A3 row / ADR-NNN | Trade-offs and optionality noted (T4-OPTION) |
| Landing-zone / readiness gap | GAP-NNN + WP-NNN | `domain: Technology`; readiness WP sequenced before dependent waves |
| Governance discipline without mechanism | POL-NNN → CST-NNN | Automated enforcement noted per T4-FITNESS |
