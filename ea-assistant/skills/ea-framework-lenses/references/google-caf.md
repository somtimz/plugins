# Google Cloud Architecture Framework Lens

Maps the Google Cloud Architecture Framework pillars onto the TOGAF ADM. Shape is close to the AWS Well-Architected lens (workload-quality pillars) with one addition: **System Design** is a foundational pillar covering the structural choices the other pillars assume. Pillar questions are largely provider-agnostic; Google-specific service guidance belongs at the SBB level.

## Pillars

### System Design (foundational)
Make deliberate structural choices before optimising. Principles: design for the workload's actual requirements; choose regions/zones from latency, residency, and resilience needs; prefer managed services; design resource hierarchy (organisation/folders/projects) to mirror governance.

### Operational Excellence
Run, monitor, and improve systems efficiently. Principles: automate deployment and operations; monitor against SLOs with error budgets; plan for incident response and learn from incidents; manage capacity and quota proactively.

### Security, Privacy, and Compliance
Protect data and workloads and meet obligations. Principles: least privilege with centralised identity; defence in depth; encrypt by default; automate compliance controls; design for data residency and privacy obligations. *(Hand depth to the `ea-security` skill — keep this pillar's review at workload level.)*

### Reliability
Meet availability targets and recover from failure. Principles: define reliability via SLOs, not adjectives; eliminate single points of failure across zones/regions; test recovery and failure paths; degrade gracefully under overload.

### Cost Optimization
Maximise business value per unit of spend. Principles: attribute spend via resource hierarchy and labels; right-size and use committed-use/sustained-use economics deliberately; make cost a design requirement, not an afterthought.

### Performance Optimization
Meet performance targets efficiently. Principles: define measurable performance targets; match compute/storage classes to workload pattern; measure before and after optimising; scale elastically rather than over-provisioning.

## ADM Mapping

| Pillar | Primary ADM phase(s) | Target artifact(s) |
|---|---|---|
| System Design | C-App, D | Application Architecture (component/topology choices), Technology Architecture (resource hierarchy, regions) |
| Operational Excellence | D, G | Technology Architecture (operations sections), Implementation Governance Plan |
| Security, Privacy, Compliance | C-Data, C-App, D | Domain architecture security sections; defer depth to `ea-security` |
| Reliability | C-App, D | Application Architecture (resilience), Technology Architecture (zonal/regional topology, DR) |
| Cost Optimization | D, E, F | Technology Architecture (cost framing), Architecture Roadmap (T4-ECON), Migration Plan |
| Performance Optimization | C-App, D | Application Architecture (NFRs), Technology Architecture (service/class selection) |

## Review Checklist

### System Design
1. Does the resource hierarchy (org/folders/projects or equivalent) mirror the governance and cost-attribution model?
2. Are region/zone choices justified by stated latency, residency, and resilience requirements (REQ-NNN), not defaults?
3. Are managed services preferred, with self-managed exceptions justified?

### Operational Excellence
1. Are SLOs defined per service with error budgets, and is alerting tied to them rather than raw metrics?
2. Is deployment fully automated with a rollback path?
3. Is there a capacity/quota management approach for growth and burst?
4. Is incident response defined and exercised, with learnings fed back?

### Security, Privacy, and Compliance
1. Is identity centralised with least privilege and no long-lived keys?
2. Is encryption at rest/in transit specified per data classification, including key-management ownership?
3. Are compliance controls automated where possible? *(reinforces T4-FITNESS)*
4. Are data-residency and privacy obligations mapped to region and data-store choices?

### Reliability
1. Is each availability target an SLO (REQ-NNN with measurable target), and does the zonal/regional topology actually support it?
2. Are single points of failure identified, with blast radius bounded?
3. Are failover and restore procedures tested, not just documented?
4. Does the system degrade gracefully under overload (load shedding, backpressure)?

### Cost Optimization
1. Is spend attributable to capabilities/work packages via hierarchy and labels?
2. Are committed-use/sustained-use vs on-demand choices analysed per steady-state workload?
3. Do major architecture decisions carry cost framing? *(reinforces T4-ECON)*
4. Is there a post-deployment cost review loop with an owner?

### Performance Optimization
1. Are performance NFRs measurable (p95 latency, throughput) with a defined test approach?
2. Are compute/storage classes matched to workload patterns rather than defaulted?
3. Is elasticity preferred over static over-provisioning?

## Interview Questions

### Phase C-App
1. What SLOs (availability, latency) does each application service carry, and who owns them? → REQ-NNN (measurable targets); Application Architecture NFRs
2. Which components are candidates for managed or serverless services? → Application Architecture; PAD-NNN if premature

### Phase C-Data
1. What residency, privacy, or sovereignty obligations constrain where data may live? → REQ-NNN (`type: security`); CST-NNN if mandated
2. What is the data lifecycle (tiering, retention, deletion) per major store? → Data Architecture

### Phase D
1. How will the resource hierarchy mirror governance and cost attribution? → Technology Architecture; Govern linkage (POL/CST)
2. What region/zone topology is required by the stated SLOs, and what does it cost? → Technology Architecture; T4-ECON framing
3. What single points of failure remain, and what is each one's blast radius? → RIS-NNN
4. What is the committed-use strategy for steady-state workloads? → Technology Architecture (cost section)

### Phase E
1. Which work packages carry SLO or cost risk that should affect wave sequencing? → Architecture Roadmap (T4-WPEVID)
2. What operational capabilities (SLO monitoring, incident response, FinOps) must precede the first wave? → WP-NNN dependencies

## Tagging Conventions

| Finding type | Capture as | Convention |
|---|---|---|
| Missing/unmeasurable SLO or NFR | REQ-NNN | `source: GCP-AF / {pillar}`; `nfrSubType` + `measurableTarget` set |
| Resilience/cost exposure | RIS-NNN | Description names the pillar and checklist item |
| Baseline-vs-target shortfall | GAP-NNN | Statement cites the pillar |
| Premature service selection | PAD-NNN | Per T4-PREMAT — directional now, service later with expiry |
| Pillar explicitly deprioritised | A3 row | Decision with rationale in the owning artifact |
