# Implementation — Concept Definitions



### Cost Entry (FIN-NNN)

**What it IS:**
A Cost Entry captures the **architecture-grade economic picture** of a single subject — a work package, an ADR option, a capability, or the whole engagement. It is the unit that makes architecture legible in financial terms: capital outlay, ongoing run cost, total cost of ownership, and projected value. Cost Entries answer *"What does this cost, over what horizon, and what is it worth?"*

**Architecture-grade, not finance-grade:** A Cost Entry exists to make trade-offs comparable and roadmaps fundable — not to replace the finance function's budgeting. Estimates are rough order-of-magnitude with an explicit confidence rating; they sharpen as evidence accrues (PADs resolve, vendors quote, POCs complete). Do not present them as committed budgets unless `status = Committed` or `Actual`.

**Structural parts** (Cost Model Register / `/ea-finance`):
- **ID** — `FIN-NNN`
- **Label** — what is being costed
- **Subject** — WorkPackage / ADR / Option / Capability / Engagement
- **Capex** — one-time build/transition cost
- **Opex (annual)** — recurring run cost once live
- **Horizon** — TCO horizon in years (default 3)
- **TCO** — *derived* = Capex + (Opex × Horizon)
- **Annual Benefit** — quantified annual value, if any
- **Benefit Narrative** — qualitative value when not fully quantified
- **Payback** — *derived* = Capex ÷ ((Annual Benefit − Opex) ÷ 12), in months; `—` if Annual Benefit does not exceed Opex (no payback); flagged as "beyond horizon" if it exceeds the TCO horizon
- **Confidence** + **Basis** — High / Medium / Low and why
- **Status** — Estimate / Budgeted / Committed / Actual
- **Links** — WP-NNN, ADR-NNN, G-NNN

**What it is NOT:**
- Not a Metric — a Cost Entry is a *projection* of cost and value; a `benefit`-type Metric *measures whether the projected value was realised*. Pair them: `FIN-003` projects €400k annual saving; `MET-012` (benefit) tracks the actual saving in production.
- Not a Business Case — a Business Case *argues* for an option using one or more Cost Entries as evidence; the Cost Entry is the costed building block, not the argument.
- Not a Work Package field — the roadmap WP cost fields are a *display projection* of the linked Cost Entry; `engagement.json → finance[]` is the source of truth.

**TOGAF placement:** Feeds the Business Case (Phase A funding instrument), the Architecture Roadmap budget roll-up (Phase E), and the Implementation & Migration Plan costing (Phase F); benefit realisation is checked in Phase G.

**Practitioner Notes:**
- **Speak the language of finance** — Phase F is an economic negotiation; cost, run-rate, TCO, and payback are the vocabulary that gets architecture funded.
- **Confidence beats false precision** — a Low-confidence ROM estimate that is honest about its basis is more useful than a spuriously exact figure.
- **Maturity marker (L1→L5):** L1 = no costing; L3 = strategic decisions and Wave-1 work carry TCO with confidence (T4-TCO); L5 = Cost Entries are tracked against actuals and trigger roadmap re-sequencing.

---

### Architecture Decision Record

**What it IS:**
An Architecture Decision Record (ADR) is a standalone document that captures the full context, options analysis, rationale, and consequences of a significant architecture decision. An ADR is written when a decision is hard to reverse, involves meaningful trade-offs, or requires documented rationale so that future architects understand why things are the way they are.

**ID scheme:** `ADR-NNN` (e.g., ADR-001, ADR-023). Assigned sequentially per engagement. Managed by `/ea-adrs`.

**ADR lifecycle:**
```
Candidate → In Progress → Completed
                                └──→ Superseded (by ADR-NNN)
          └──→ Deprecated (any time, with reason)
```
- **Candidate**: Decision identified; options analysis not yet started
- **In Progress**: Options analysis underway; decision not yet made
- **Completed**: Decision made and fully documented
- **Superseded**: Replaced by a newer ADR; `supersededBy: ADR-NNN` recorded
- **Deprecated**: No longer applicable; deprecation reason recorded

**When to create an ADR (not just an A3 Decision Log entry):**
- Technology or vendor selection (cloud platform, database engine, integration middleware)
- Architecture pattern or style choice (microservices, event-driven, CQRS, layered)
- Make-vs-buy or build-vs-configure decisions
- Data governance approach (ownership, sharing, sovereignty model)
- Security or compliance architecture approach
- Significant API or integration design choice
- Any decision that is hard to reverse or whose rationale may be questioned later

**ADR vs. A3 Decision Log:**
- The **A3 Decision Log** (within an artifact's appendix) tracks governance state — who decided what, at what authority level, and whether it has been verified. It is lightweight and lives inside the artifact.
- An **ADR** documents the full decision context: what situation triggered it, what options were considered, why one was chosen, and what the consequences are. It is a standalone artifact.
- They complement each other: log a high-level entry in A3; create an ADR for the full documentation. Link them via the ADR-NNN ID in the A3 `Notes` column.

**Structural parts** (architecture-decision-record.md):
- **§1 Status** — lifecycle history table (date/status/changed-by/note)
- **§2 Context** — situation that forces the decision; linked DRV/G-NNN; triggering artifact
- **§3 Decision Drivers** — evaluation criteria (must-have / should / nice-to-have)
- **§4 Options Considered** — at least two options with pros/cons and driver assessment
- **§5 Decision** — unambiguous statement; chosen option; governance reference
- **§6 Rationale** — why the chosen option was selected; accepted trade-offs
- **§7 Consequences** — positive, negative, risks introduced (RIS-NNN link), new decisions required
- **§8 Related Architecture Decisions** — ADR-to-ADR relationships
- **§9 Affected Artifacts** — artifacts materially affected by this decision

**TOGAF placement:** ADR is not a native TOGAF artifact, but maps closely to the Architecture Decision concept in TOGAF's Architecture Repository. ADRs are referenced via the A3 Decision Log in Architecture Vision, domain architecture artifacts, and the ADR Register.

**Commands:** Use `/ea-adrs` to manage ADRs, track the register, and surface ADR summaries. Use `/ea-adrs new` to create a new ADR. Use `/ea-adrs status` for a portfolio view.

---

### Capability Gap

**What it IS:**
A Capability Gap is a delta between the capabilities the organisation currently has and the capabilities it needs to achieve its Goals and Objectives. Capability Gaps are identified by comparing the Capability Model against the requirements of the Strategies and Objectives. A gap may be a **missing capability** (entirely absent) or an **immature capability** (present but not yet fit-for-purpose).

**Key relationships:**
- Capability Gaps **prevent Goals** from being achieved — if a required capability is absent or immature, the associated Goal cannot be reached
- Identified Capability Gaps **trigger work packages** in the Architecture Roadmap (Phase E)
- Capability Gaps are the primary output of the **Gap Analysis** artifact

**TOGAF placement:** Gap Analysis (Phases B, C, D) — one gap register per domain. Feeds into Architecture Roadmap work package definitions (Phase E).

---

### Work Package (WP-NNN)

**What it IS:**
A Work Package is a discrete, plannable unit of change that the organisation will resource and deliver to move from the baseline toward the target architecture. It is the **delivery vehicle**: capabilities and gaps define *what* must change; the work package is *how the change gets done and funded*. Every work package must deliver measurable business value — closing a technical gap is not a work package unless it enables a specific business outcome. Defined and sequenced in the Architecture Roadmap (Phase E) and finalised in the Migration Plan (Phase F).

**Structural parts** (Architecture Roadmap):
- **Description** and **Phase / Wave** — what it delivers and when, grouped into delivery increments
- **Advances Goals/Objectives** and **Executes Strategies** — the strategic alignment (a WP with neither is unjustified)
- **Closes Gaps** (GAP-NNN) and **Addresses Requirements** (REQ-NNN) — what it resolves
- **Effort**, **Capex / Opex / TCO** (via FIN-NNN), **Dependencies**, **Owner**, **Status**
- **Evidence Status**, **Decision Reversibility**, **Value Delivery** (Standalone / Cumulative / Enabling) — used for evidence-gated and risk-aware sequencing

**Key relationships:**
- **Closes** Capability Gaps and **delivers** Capabilities to their target maturity
- **Realises** the Transition Architectures (Plateaus) — work packages are the steps between plateaus
- **Costed by** Cost Entries (FIN-NNN); **depends on** other WPs (sequencing, captured in the WP/Dependency matrix)

**What it is NOT:**
- Not a **Gap** — a gap is the difference between current and target; the work package is the change that closes it
- Not a **Project** — a work package is an architecture-defined unit of change; a project is the delivery construct that may bundle several (program governance, not architecture governance)
- Not a **Plan** — a plan is the ordered set of actions; the roadmap *sequences* work packages into the plan
- Not a **Capability Increment** — an increment is a measurable step-up in a capability's maturity; a work package is the work that produces it

**TOGAF placement:** Architecture Roadmap (Phase E) — the primary home; refined and costed in the Migration Plan (Phase F); re-assessed in Phase H when change requests alter the migration sequence.

**Practitioner Notes:**
- **Package work as value increments** — every WP delivers measurable business value, not just a technical milestone.
- **Sequence by impact × feasibility** — quick wins early build delivery credibility; gate low-evidence packages out of Wave 1 (T4-WPEVID).
- **Align to funding cycles** — a roadmap that ignores budget reality is fantasy; carry capex/opex so waves roll up to a fundable budget (T4-TCO).
- **Maturity marker (L1→L5):** L1 = work packages are a project list with no traceability; L3 = each WP traces to gaps/goals and carries effort and evidence; L5 = the roadmap is an investment portfolio with economic tracking and continuous re-sequencing.

---
