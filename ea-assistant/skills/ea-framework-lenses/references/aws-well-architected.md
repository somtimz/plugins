# AWS Well-Architected Framework Lens

Maps the six AWS Well-Architected pillars onto the TOGAF ADM. Use for engagements with AWS (or general cloud) workloads — the pillar questions are largely provider-agnostic; AWS-specific service guidance belongs at the SBB level.

## Pillars

### Operational Excellence
Run and monitor systems to deliver business value and continually improve processes. Principles: operations as code; small reversible changes; refine procedures frequently; anticipate failure; learn from operational events.

### Security
Protect data, systems, and assets through risk assessment and mitigation. Principles: strong identity foundation; traceability; security at all layers; automate security best practices; protect data in transit and at rest; keep people away from data; prepare for incidents. *(Overlaps with the deeper `ea-security` skill — use this pillar for cloud-workload review; use `/ea-security-review` for engagement-wide SABSA/ISO/NIST coverage.)*

### Reliability
Workloads perform their intended function correctly and consistently, and recover from failure. Principles: automatic recovery; test recovery procedures; scale horizontally; stop guessing capacity; manage change through automation.

### Performance Efficiency
Use computing resources efficiently as demand changes and technologies evolve. Principles: democratize advanced technologies; go global in minutes; use serverless architectures; experiment more often; consider mechanical sympathy (match technology to workload).

### Cost Optimization
Deliver business value at the lowest price point. Principles: implement cloud financial management; adopt a consumption model; measure overall efficiency; stop spending on undifferentiated heavy lifting; analyze and attribute expenditure.

### Sustainability
Minimize the environmental impact of running workloads. Principles: understand impact; establish sustainability goals; maximize utilization; adopt more efficient hardware/software; reduce downstream impact.

## ADM Mapping

| Pillar | Primary ADM phase(s) | Target artifact(s) |
|---|---|---|
| Operational Excellence | D, G | Technology Architecture (operations sections), Implementation Governance Plan |
| Security | C-Data, C-App, D | Data/Application/Technology Architecture security sections; defer depth to `ea-security` |
| Reliability | C-App, D | Application Architecture (resilience), Technology Architecture (topology, DR) |
| Performance Efficiency | C-App, D | Application Architecture (NFRs), Technology Architecture (sizing, services) |
| Cost Optimization | D, E, F | Technology Architecture (cost framing), Architecture Roadmap (T4-ECON), Migration Plan |
| Sustainability | D, E | Technology Architecture (efficiency targets), Architecture Roadmap |

## Review Checklist

### Operational Excellence
1. Is infrastructure and configuration defined as code, or are there manual provisioning steps?
2. Are deployment changes small and reversible, with a documented rollback path?
3. Are operational runbooks/playbooks specified for the workloads in scope?
4. Is there a defined process for learning from operational events (post-incident reviews feeding back into architecture)?
5. Are operational metrics and alerting thresholds specified for each major component?

### Security
1. Is identity centralised with least-privilege access and no long-lived credentials?
2. Is every layer (edge, VPC/network, compute, application, data) covered by a control, or are controls concentrated at the perimeter?
3. Is data classified, and is encryption specified in transit and at rest per classification?
4. Are security controls automated (policy-as-code, automated scanning) rather than manual review only? *(reinforces T4-FITNESS)*
5. Is there an incident response plan that has actually been exercised?

### Reliability
1. Are availability targets (REQ-NNN with measurable SLA) defined per workload, and does the topology support them?
2. Does recovery happen automatically (health checks, self-healing, failover), or does it depend on human intervention?
3. Are recovery procedures (backup restore, region/AZ failover) tested, not just documented?
4. Does the design scale horizontally to absorb load, or does it depend on vertical headroom guesses?
5. Are single points of failure identified, and is the blast radius of each failure mode bounded?

### Performance Efficiency
1. Are technology selections matched to the workload pattern (compute type, storage class, database model), or defaulted?
2. Are performance NFRs (p95 latency, throughput, concurrency) defined with measurable targets and a test approach?
3. Is there a mechanism to re-evaluate service choices as offerings evolve (links to Technology Horizon THR-NNN)?
4. Is caching/CDN/data-locality considered where latency targets demand it?
5. Are managed/serverless options preferred over self-managed infrastructure where they meet requirements?

### Cost Optimization
1. Is there cost attribution (tagging, account structure) mapping spend to capabilities or work packages?
2. Are consumption-model choices (on-demand vs reserved vs spot; serverless vs provisioned) justified per workload?
3. Are cost estimates attached to the major architecture decisions (reinforces T4-ECON on A3/ADR entries)?
4. Is undifferentiated heavy lifting (self-hosting what a managed service provides) identified and justified where retained?
5. Is there a defined process for reviewing and acting on cost anomalies post-deployment?

### Sustainability
1. Are utilization targets set so capacity matches demand (right-sizing, scale-to-zero where possible)?
2. Are region choices informed by efficiency/carbon considerations where latency and residency constraints allow?
3. Is data lifecycle management specified (tiering, expiry) to avoid indefinite storage growth?
4. Are efficiency improvements tracked as measurable objectives (OBJ-NNN/MET-NNN) rather than aspirations?

## Interview Questions

### Phase C-App
1. What availability and recovery expectations do the application workloads carry, and which are cloud-hosted? → Application Architecture NFRs; REQ-NNN (`nfrSubType: Availability/Recoverability`)
2. Which application components are candidates for managed or serverless services rather than self-managed? → Application Architecture; PAD-NNN if premature
3. How will application performance targets be validated under load? → REQ-NNN (`nfrSubType: Performance`, measurableTarget)

### Phase C-Data
1. How is data classified, and what encryption and residency rules follow from each class? → Data Architecture; REQ-NNN (`type: security`)
2. What is the data lifecycle — retention, tiering, expiry — for each major data store? → Data Architecture; Sustainability checklist item 3
3. What are RPO/RTO per critical data store, and how are restores tested? → REQ-NNN (`nfrSubType: Recoverability`)

### Phase D
1. Which Well-Architected pillars matter most for this engagement, and which are explicitly deprioritised? → Technology Architecture (lens scope note); A3 decision
2. Is infrastructure defined as code, and what is the deployment/rollback model? → Technology Architecture (Operational Excellence section)
3. How is the workload protected at each layer — edge, network, compute, data? → Technology Architecture security section; hand depth to `/ea-security-review`
4. What is the cost model per major workload (consumption vs reserved), and who owns cost review? → Technology Architecture; T4-ECON framing on related A3 rows
5. What single points of failure remain in the proposed topology, and what is the blast radius of each? → RIS-NNN; Technology Architecture resilience section

### Phase E
1. Which gaps or work packages carry cloud cost or operational-readiness risk that should affect wave sequencing? → Architecture Roadmap (Strategic Alignment, T4-WPEVID)
2. Are there quick-win optimisations (right-sizing, storage tiering, reserved capacity) that justify an early work package? → WP-NNN candidates; GAP-NNN
3. What operational capabilities (monitoring, incident response, FinOps) must exist before the first wave goes live? → Architecture Roadmap dependencies; CAP-NNN

## Tagging Conventions

| Finding type | Capture as | Convention |
|---|---|---|
| Missing/weak NFR | REQ-NNN | `source: AWS-WAF / {pillar}`; set `nfrSubType` and `measurableTarget` |
| Resilience/cost exposure | RIS-NNN | Description names the pillar and checklist item |
| Baseline-vs-target shortfall | GAP-NNN | `domain: Technology` (usually); statement cites the pillar |
| Premature service selection | PAD-NNN | Per T4-PREMAT — directional choice now, service choice deferred with expiry |
| Pillar explicitly deprioritised | A3 row | Decision with rationale in the owning architecture artifact |
