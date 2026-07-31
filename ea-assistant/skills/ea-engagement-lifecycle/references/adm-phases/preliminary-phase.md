# Preliminary Phase


### Objectives
- Establish the Architecture Capability: governance, organisation, team, tools, and principles.
- Tailor the ADM for the organisation's context.
- Define the Architecture Principles that will govern future architecture work.

### Key Inputs
- TOGAF and other selected architecture frameworks
- Board strategies, business drivers, and constraints
- Existing organisational structures, governance models, and IT strategies
- Existing architecture frameworks, methods, and tools in use

### Major Steps
1. Determine the scope of the enterprise affected by the architecture capability.
2. Confirm governance and support frameworks.
3. Define and establish the Architecture Team.
4. Identify and establish Architecture Principles.
5. Select and implement architecture tooling.
6. Define the Architecture Repository structure.
7. **Link to shared Architecture Repository (if applicable):** If an organisation-wide Architecture Repository exists at `EA-Workspace/Architecture-Repository/`, run `/ea-repo link <slug>` to connect this engagement. The linked repository provides STD, VDR, and THR context during Phases B–D. If running `/ea-new` inside an EA-Workspace, this link is set automatically.
8. Finalise and publish the Architecture Governance framework.

### Key Questions
- What is the enterprise scope for architecture work?
- What governance structures are in place or needed?
- Who are the architecture stakeholders and what are their concerns?
- What principles will constrain future architecture decisions?
- What frameworks, methods, and notations will be used?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Principles Catalogue | Documented set of principles with rationale and implications |
| Architecture Governance Framework | Policies, procedures, and organisational structures for governance |
| Architecture Repository (initial) | Baseline structure for storing architecture outputs |
| Request for Architecture Work (template) | Template used to initiate architecture projects |
| Tailored ADM | Documented customisation of ADM phases and deliverables for the organisation |

### Deep Tactics
- Treat the Architecture Board as a **decision marketplace**, not a review committee.
- Define architecture services with **SLAs** — operate like a product team.
- **Fund architecture as a persistent capability**, not a project overhead.
- Build a **minimal but enforceable standards catalog** — start small, evolve fast.
- Align architecture **KPIs with enterprise OKRs** (e.g., reuse rate, time-to-decision).

### Decision Flow

**What to decide now:** Architecture Principles, governance model, standards catalog scope, team structure, engagement tailoring.

**What to defer:** Technology choices, vendor selections, specific patterns, detailed architecture designs.

**How to handle strong pressure:** If stakeholders insist on specific technology choices in Preliminary, convert to PAD-NNN with constraint boundaries: "We will evaluate cloud platforms in Phase D; constraint: data sovereignty requirements must be met."

**Evidence threshold:** Principles need evidence of organisational need (incidents, costs, regulatory requirements), not just aspiration.

### Decision Flow

**What to decide now:** Strategic direction, goals, objectives, scope boundaries, stakeholder map, high-level constraints.

**What to defer:** All technology, vendor, and pattern decisions. Any specific architecture style choice (microservices, event-driven, etc.) made in Phase A is premature and should be converted to a PAD-NNN with constraint boundaries.

**How to handle strong pressure:** When a sponsor or stakeholder insists on a technology in Phase A, document the constraint boundary, not the commitment. Example: "Sponsor insists on cloud-first → PAD-001: constraint boundary = all new workloads evaluate cloud; resolution path = Phase D Technology Architecture."

**Evidence threshold:** Goals and objectives need baseline metrics and business driver evidence. Strategies need at least one validation approach (pilot, reference case, expert review).

**Key rule:** Directional decisions only. If someone says "we're going microservices" in Phase A, challenge it immediately — that is a Phase C decision at the earliest.

### Decision Flow

**What to decide now:** Capability model, business process boundaries, org design implications, value stream definitions.

**What to defer:** Application boundaries (wait for Phase C), technology platforms (wait for Phase D), detailed data models (wait for Phase C).

**How to handle uncertainty:** Log business capability uncertainties as PAD-NNN entries. Example: "Uncertain whether customer onboarding should be centralised or federated → PAD-002 with resolution path to Phase E after org design workshop."

**Evidence threshold:** Capability gaps need baseline maturity assessment and target state definition. Business process changes need stakeholder validation.

### Decision Flow

**What to decide now:** Data domains and ownership, application boundaries and responsibilities, API contracts, integration patterns.

**What to defer:** Specific technology products and versions (wait for Phase D), detailed implementation designs (wait for Phase G).

**How to handle uncertainty:** POC or spike required before committing to patterns with low reversibility (event sourcing, CQRS, distributed transactions).

**Evidence threshold:** Application architecture needs interface definitions and data flow validation. Integration patterns need proof-of-concept for critical paths.

### Decision Flow

**What to decide now:** Technology platforms, standards, infrastructure topology, security mechanisms.

**What to defer:** Nothing — this is the primary technology decision phase. However, if a technology decision lacks evidence, it becomes a PAD-NNN blocking Phase E.

**Evidence threshold:** Technology decisions need benchmarks, vendor responses, or reference implementations. Vendor lock-in decisions need TCO analysis and exit strategy.

### Decision Flow

**What to decide now:** Work package definitions, transition architectures, benefits assessment.

**Critical action:** Convert all open PAD-NNN entries from Phases A–D into either committed decisions (A3/ADR) or work packages with evidence requirements.

**What to defer:** Nothing should remain deferred at Phase E. Any PAD still open after Phase E is a delivery risk.

**Evidence threshold:** Work packages need evidence-gated prioritisation. Low-evidence packages should be deferred until evidence is gathered.

### Decision Flow

**What to decide now:** Migration wave sequencing, resource allocation, rollout approach.

**How to prioritize:** Evidence-gate prioritisation — work packages with sufficient evidence and high reversibility should precede those with low reversibility and weak evidence.

**What to revisit:** Decisions from earlier phases that new delivery evidence contradicts.

### Decision Flow

**What to enforce now:** All committed architecture decisions (A3/ADR). Deviations require explicit acceptance with risk sign-off or remediation.

**What to create:** New PAD-NNN entries for uncertainties discovered during implementation.

**How to handle deviations:** Every deviation is either accepted (with documented risk) or remediated. No undocumented drift.

### Decision Flow

**What to adapt now:** Revisit decisions based on post-implementation evidence. Retire obsolete architectures and their associated ADRs.

**What to resolve:** Review all expired PAD-NNN entries — resolve or close them.

**Trigger:** New evidence that contradicts a previous decision should trigger a mini-ADM cycle, not a workaround.

### Decision Flow

**What to track:** Every requirement must link to at least one architecture decision or work package. Orphan requirements create hidden gaps.

**How to handle uncertainty:** Requirements with unclear implementation path become PAD-NNN entries with resolution paths.

**Evidence threshold:** Requirements need traceability to goals, objectives, or business drivers. Un traceable requirements are scope risks.

### Hidden Mechanics
- Architecture capability is the **platform** on which all future work runs. Under-invest here and everything downstream slows.
- The standards catalog is a **living product** with consumers, owners, and adoption metrics — not a static document.

### Maturity Indicators
- **L1:** Architecture team is a project overhead; governance is ad-hoc
- **L3:** Architecture team has defined services with SLAs; standards catalog is maintained
- **L5:** Architecture capability is self-funding; governance is automated; standards are continuously pruned

---
