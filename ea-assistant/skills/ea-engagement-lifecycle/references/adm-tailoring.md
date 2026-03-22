# ADM Tailoring Guide

This guide provides structured guidance for adapting the TOGAF Architecture Development Method (ADM) to different delivery contexts and organisational constraints. Tailoring is not optional decoration — it is a professional responsibility. An ADM applied without contextual adjustment often produces artefacts that sit on shelves rather than driving change.

The core ADM cycle remains the reference point. Every tailoring pattern below preserves the intent of each phase while adjusting scope, sequence, formality, and artefact weight.

---

## When to Tailor

Tailor the ADM when one or more of the following conditions hold:

- The organisation delivers change through agile or iterative methods that cannot absorb the full ADM artefact set per cycle.
- Multiple projects share a common architecture umbrella and need coordinated governance rather than independent ADM cycles.
- The strategic driver is capability maturity rather than system replacement or technology refresh.
- Security, privacy, or regulatory requirements must be addressed as a first-class architecture concern rather than a downstream review.
- The organisation is small, has no dedicated EA function, and needs a minimum-viable architecture approach.

Tailoring does not mean skipping phases. It means combining phases, reducing artefact formality, adjusting sequencing, and fitting governance to what the organisation can actually absorb and act on.

---

## Agile Delivery

### Context

The organisation delivers change through time-boxed sprints or programme increments. Delivery teams work at velocity. Architecture must provide just-in-time guidance rather than upfront blueprints. Stakeholders expect architecture to be a collaborative, continuous activity rather than a gate-keeping function.

### Tailoring Table

| Standard ADM | Agile Adaptation |
|---|---|
| Preliminary — establish capability and framework | Run once per programme; standing architecture team owns outputs |
| Phase A — architecture vision | One-pager per PI or quarterly cycle; updated not rewritten |
| Phase B — business architecture | Lightweight capability/process canvas; updated per epic |
| Phase C — information systems architecture | Data and application views produced per feature cluster |
| Phase D — technology architecture | Thin technology baseline; updated when platform decisions arise |
| Phase E — opportunities and solutions | Translated into backlog epics and enabler stories |
| Phase F — migration planning | Rolling wave; 1–2 PIs planned, remainder indicative |
| Phase G — implementation governance | Architecture runway reviews embedded in PI planning |
| Phase H — architecture change management | Continuous; triggered by retrospectives or tech debt spikes |

### Artefact Adjustments

Replace heavy formal artefacts with lighter equivalents:

- Architecture Vision → Architecture One-Pager (1–2 pages, decision-focused)
- Business Architecture Document → Capability Canvas or Value Stream Map (visual, collaborative)
- Application Portfolio → Living Architecture Decision Records (ADRs) maintained in the repository
- Migration Plan → Programme Increment Roadmap with architecture runway items

### Phase Combinations

**B + C + D concurrent** — In agile contexts, business, data, and technology architecture decisions are often inseparable within a single feature or epic. Run B, C, and D as a single architecture sprint with cross-domain pairing rather than sequential gates.

**E + F collapse** — Opportunities identification and migration sequencing are the same conversation in a rolling-wave backlog. Combine into a single "Architecture Backlog Refinement" activity aligned to PI planning.

### Decision Tree: Agile Framework Alignment

```
Is the organisation using SAFe?
├── Yes → Align ADM phases to SAFe's architectural runway concept.
│         Phase A per ART; B/C/D per PI; E/F per PI planning; G embedded in system demo.
│         Architecture kanban replaces formal phase gates.
└── No → Is the organisation using Scrum at scale?
         ├── Yes → Architecture chapter or guild owns ADM phases across teams.
         │         Phase A per quarter; B/C/D per sprint cycle (2–4 sprints);
         │         E/F per quarterly planning; G via architecture review in sprint review.
         └── No (embedded architect model) →
                   Architect is embedded in delivery team.
                   ADM phases inform personal decision-making cadence.
                   Artefacts are ADRs and lightweight diagrams checked into the team repo.
                   Governance is async — architecture decisions shared via PR review.
```

---

## Programme-Level Architecture

### Context

Multiple projects or workstreams are executing under a single programme. Each project has its own scope and timeline, but they share infrastructure, data, integration layers, or business capabilities. Without coordinated architecture governance, projects make locally optimal decisions that create programme-level debt.

### Tailoring Table

| Standard ADM | Programme Adaptation |
|---|---|
| Preliminary | Programme architecture setup — standards, tools, team structure |
| Phase A | Programme Architecture Vision — once; refreshed at major milestone |
| Phase B | Programme Business Architecture — capability model shared across projects |
| Phase C | Programme Information Systems Architecture — shared data and integration standards |
| Phase D | Programme Technology Architecture — platform baseline; projects inherit |
| Phase E | Per-project opportunities within programme constraints |
| Phase F | Programme-level migration roadmap; project plans align to it |
| Phase G | Dual governance — programme board for cross-project; project architects for in-flight |
| Phase H | Change requests assessed at programme board; urgent changes fast-tracked |

### Governance Model

```
Programme Architecture Board
├── Owns: Architecture Principles, Standards Catalogue, Programme Roadmap
├── Reviews: Cross-project decisions, integration points, platform changes
├── Cadence: Monthly or per programme milestone
│
Project Architect (per project)
├── Owns: Project-scoped Architecture Definition Document
├── Reviews: In-project design decisions, deviations from programme standards
├── Escalates: Cross-project impacts, standard change requests
└── Cadence: Per sprint cycle or delivery gate
│
Change Flow:
  Project decision within standards → Project Architect approves → log to programme register
  Project decision deviating from standards → escalate to Programme Board → decision and record
  New programme standard required → Programme Board → update Standards Catalogue → notify projects
```

### Phase Combinations

**Programme level — Preliminary + A once, then G + H continuous**

Run Preliminary and Phase A as a programme inception activity. Establish the shared architecture vision, principles, and standards. Then operate G (governance) and H (change management) as a continuous programme service throughout delivery. Projects draw on the programme architecture baseline rather than running their own A through D.

**Project level — B through F per project**

Each project runs its own scoped B, C, D, E, F cycle, but within the constraints set at programme level. Project artefacts reference programme standards rather than redefining them. The programme architecture team reviews and approves project Architecture Definition Documents before project execution begins.

---

## Capability-Based Planning

### Context

The strategic intent is to evolve organisational capabilities incrementally. The architecture is not organised around systems or projects but around capabilities — discrete, measurable abilities the organisation needs to deliver its mission. Each increment improves one or more capabilities. Architecture governs the increments and ensures each builds on the last.

### Tailoring Table

| Standard ADM | Capability-Based Adaptation |
|---|---|
| Preliminary | Establish capability framework and heat map baseline |
| Phase A | Define capability target state and architecture roadmap across all increments |
| Phase B | Capability-centric business architecture — each increment maps to capability improvement |
| Phase C | Information architecture scoped to data and applications supporting target capabilities |
| Phase D | Technology required per capability increment |
| Phase E | Increment definition — scope, dependencies, enabling investments |
| Phase F | Increment sequencing — ordered by capability priority and dependency |
| Phase G | Govern each increment delivery; verify capability improvement is realised |
| Phase H | Review capability attainment; adjust roadmap based on actuals |

### Iteration Pattern

```
Phase A — Define full capability roadmap (all increments identified and sequenced)

For each increment:
  Phase B → Define business and process changes for this capability improvement
  Phase C → Define data and application changes required
  Phase D → Define technology changes required
  Phase E → Define increment scope, dependencies, risks
  Phase F → Confirm increment plan and resource alignment
  Phase G → Govern increment delivery; architecture compliance checks
  Phase H → Review: was the capability improvement achieved?
             Yes → proceed to next increment
             No  → adjust increment scope or roadmap; re-enter at B or E
```

### Artefact Adjustments

- Architecture Vision → Capability Roadmap (visual, increment-by-increment)
- Business Architecture Document → Capability Definition Sheet per increment (scope, measures, process delta)
- Application Portfolio → Capability-to-Application Mapping (which apps enable which capabilities)
- Migration Plan → Increment Plan (cost, timeline, dependencies, success measures)

---

## Security Architecture Overlay

### Context

Security, privacy, and regulatory compliance are first-class architectural concerns — not a late review. This applies to organisations in regulated industries (financial services, healthcare, government, critical infrastructure) or any context where a breach or compliance failure would be material. The security architecture overlay integrates security activities into every ADM phase rather than treating security as a separate stream.

### Tailoring Table

| Standard ADM | Security Architecture Overlay |
|---|---|
| Preliminary | Include security principles; establish CISO/DPO as architecture stakeholders |
| Phase A | Security vision — threat context, regulatory obligations, risk appetite |
| Phase B | Business security architecture — security-sensitive processes, access model, roles |
| Phase C | Data classification, privacy by design, secure application patterns |
| Phase D | Security technology architecture — controls, monitoring, identity infrastructure |
| Phase E | Security impact of each solution option; risk-adjusted option selection |
| Phase F | Security acceptance criteria in migration plan; security testing gates |
| Phase G | Security compliance checks in implementation governance; incident response integration |
| Phase H | Security posture review; threat landscape reassessment; control effectiveness |

### Additional Security Activities per Phase

- **Preliminary** — Conduct a regulatory mapping exercise. Identify applicable regulations (GDPR, ISO 27001, sector-specific). Document obligations as architecture constraints. Establish security architecture review as a mandatory gate in the governance framework.
- **Phase A** — Produce a Threat Context Statement alongside the Architecture Vision. Identify primary threat actors, attack surfaces, and regulatory red lines. Get explicit CISO sign-off on risk appetite before architecture work proceeds.
- **Phase B** — Map security-sensitive business processes. Identify where data classification decisions, access control boundaries, and fraud/abuse risk are highest. Document security roles (data owners, custodians, processors) in the business architecture.
- **Phase C** — Apply privacy by design principles to data architecture. Classify all major data entities. Define data residency and retention requirements. Produce a secure application pattern catalogue for use by development teams.
- **Phase D** — Design the security technology stack as an explicit architecture layer. Cover identity and access management, network segmentation, encryption at rest and in transit, security monitoring (SIEM/SOAR), and key management. Document security controls against each technology component.
- **Phase E** — Evaluate each solution option against a security risk matrix. Favour options that reduce attack surface or improve control coverage. Document residual risks for options selected.
- **Phase F** — Include security acceptance criteria in the migration plan. Define penetration testing, vulnerability assessment, and security review gates that must be passed before go-live. Assign security testing responsibilities.
- **Phase G** — Embed security compliance checks in implementation governance. Review security artefacts (pen test reports, DPIA outcomes, access control reviews) as part of architecture compliance assessments. Integrate with incident response processes so that security events trigger architecture review where needed.
- **Phase H** — Conduct a periodic security posture review. Reassess the threat landscape. Review control effectiveness metrics. Update the Threat Context Statement. Identify capability gaps introduced by change or by evolving threats.

### SABSA Integration Points

The Sherwood Applied Business Security Architecture (SABSA) framework provides a complementary layered model. Map SABSA layers to ADM phases as follows:

| SABSA Layer | SABSA Focus | ADM Phase |
|---|---|---|
| Contextual (Business) | Why — business risk and security drivers | Phase A — Architecture Vision |
| Conceptual (Architect) | What — security concepts and policies | Phase B — Business Architecture |
| Logical (Designer) | How — logical security services and controls | Phase C and D — Information Systems and Technology Architecture |
| Physical (Builder) | With what — physical security mechanisms | Phase D — Technology Architecture |
| Component (Tradesman) | Specific products and configurations | Phase G — Implementation Governance |

At each ADM phase, validate that the security architecture addresses the corresponding SABSA layer before proceeding. SABSA traceability ensures security decisions at lower layers remain traceable to business risk decisions made at the contextual layer.

---

## Small Organisation / Lightweight ADM

### Context

The organisation has fewer than 500 staff, no dedicated EA function, and limited capacity to produce or maintain formal architecture artefacts. Architecture must be done by someone with other responsibilities — a CTO, a lead architect who is also hands-on, or a senior business analyst. The value of architecture is real, but the method must fit within the available time and skill.

### Phase Combinations

| Lightweight ADM Stage | Constituent ADM Phases | Output |
|---|---|---|
| Kickoff | Preliminary + Phase A | Architecture context document (2–4 pages): principles, constraints, vision, stakeholders |
| Definition | Phase B + C + D | Architecture definition document (4–8 pages): capability model, key applications, technology baseline |
| Roadmap | Phase E + F | Architecture roadmap (1–2 pages or visual): prioritised initiatives, sequencing, rough costs |
| Periodic Review | Phase G | Architecture review meeting (quarterly): is delivery aligned to architecture? what has changed? |
| Annual Refresh | Phase H | Annual architecture update: refresh vision, update roadmap, retire completed initiatives |

### Artefact Minimums

Every artefact in the Lightweight ADM is a one-pager unless the organisation has a specific reason to go deeper.

- **Architecture Context (Kickoff)** — One page: 5–7 principles, top 3 constraints, one-paragraph vision, key stakeholders listed. Signed off by the most senior business owner available.
- **Architecture Definition (Definition)** — One page per domain: business capability map (hand-drawn or simple diagram is fine), application inventory (spreadsheet or table), technology baseline (list of key platforms, vendors, versions). Total: 3–5 pages.
- **Architecture Roadmap (Roadmap)** — Visual timeline or table: initiatives listed, rough sequencing, dependencies noted, indicative cost bands (small/medium/large). One page or one slide.
- **Architecture Review (Periodic Review)** — Meeting notes: what was delivered, what deviated from architecture, what decisions were made, what needs to change in the architecture. Maximum one page of notes per review.
- **Architecture Update (Annual Refresh)** — Revised versions of the above artefacts. Track changes. Archive the previous version. One meeting to agree the update with relevant stakeholders.

---

## Decision Matrix

Use this matrix to select one or more tailoring patterns for a given engagement. Patterns are not mutually exclusive — combine as needed.

| Factor | Agile Delivery | Programme-Level | Capability-Based | Security Overlay | Lightweight ADM |
|---|---|---|---|---|---|
| Large organisation (>500 staff) | Maybe | Yes | Maybe | Maybe | No |
| Small organisation (<500 staff) | Maybe | No | No | Maybe | Yes |
| Agile / sprint-based delivery | Yes | Maybe | No | Maybe | No |
| Multiple projects under one programme | No | Yes | No | Maybe | No |
| Regulatory or security pressure | No | No | No | Yes | No |
| No dedicated EA function | Maybe | No | No | No | Yes |
| Greenfield / new capability | Maybe | Maybe | Yes | Maybe | Maybe |
| Brownfield / legacy modernisation | Maybe | Yes | Yes | Yes | Maybe |
| Capability maturity as primary driver | No | No | Yes | No | No |
| Time-to-value pressure | Yes | No | No | No | Yes |

**Reading the matrix:**

- **Yes** — this factor strongly suggests this tailoring pattern applies.
- **Maybe** — this factor is compatible with the pattern but other factors determine fit.
- **No** — this factor suggests the pattern is unlikely to be the right choice; consider alternatives.

When multiple factors point to the same pattern, that pattern is the primary recommendation. When factors point to different patterns, combine them — for example, a large organisation with regulatory pressure running agile delivery should apply both the Agile Delivery and Security Architecture Overlay patterns simultaneously.
