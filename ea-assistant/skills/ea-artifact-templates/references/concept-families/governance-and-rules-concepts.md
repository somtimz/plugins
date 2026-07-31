# Governance & Rules — Concept Definitions



### Principle

**What it IS:**
A principle is a normative statement that governs all future architecture decisions. It acts as a decision filter: when choosing between design options, a principle tells you which option to select (or eliminate). Principles are durable — they change rarely and only through a formal governance process.

**Structural parts** (TOGAF standard):
- **Name** — short, memorable label (e.g. "Vendor Neutrality")
- **Statement** — one declarative sentence describing the rule (e.g. "Technology choices must not create dependency on a single vendor")
- **Rationale** — why this principle matters to the organisation
- **Implications** — what this means in practice for architects, developers, and the business
- **Owner** — who is accountable for upholding this principle
- **Status** — Proposed / Approved / Retired

**What it is NOT:**
- Not a **Goal** — a goal describes a desired state; a principle governs how decisions are made to reach any state
- Not a **Strategy** — a strategy selects an approach for a specific engagement or problem; a principle applies universally and indefinitely
- Not a **Requirement** — a requirement states a need ("the system must handle 10,000 concurrent users"); a principle states a rule ("all systems must be designed for scalability")
- Not a **Preference** — principles are binding within their governance scope; preferences are optional
- Not a **Policy** — a policy is an external governance document enacted by an authority (board, regulator); a principle is an internal normative rule created by the architecture board

**Common confusions:**
- "We should use cloud" — this is a **Strategy** (a chosen approach), not a principle. A principle would be: "Technology platforms must support elastic scalability" (applies to all technology choices, not just the cloud decision)
- "We want to be data-driven" — this is a **Goal**, not a principle
- "All APIs must use OAuth 2.0" — this is a **Standard** (a specific, enforceable technical rule), not a principle. The underlying principle is: "Security controls must be applied at every integration boundary"

**TOGAF placement:** Architecture Principles Catalogue, created in the Preliminary phase before Phase A begins. Governs Phases A–H.

**ArchiMate:** `Principle` element in the Motivation aspect. Motivates `Goals`, `Requirements`, and `Constraints`. May be aligned with or derived from `Policy`.

**Practitioner Notes:**
- Principles must be **enforceable constraints**, not aspirational statements. Each principle needs an enforcement mechanism.
- **Policy alignment:** Where a principle is derived from or aligned with an enterprise policy, record the POL-NNN in the principle's metadata. This strengthens traceability from external mandate to internal normative rule.
- Build a **minimal but enforceable standards catalog** — start small, evolve fast. Prune obsolete standards regularly.
- **Maturity marker (L1→L5):** L1 = principles are wall art; L3 = principles filter decisions with documented exceptions; L5 = principles are enforced automatically in pipelines
- **Failure mode watch:** Over-standardization (Failure Mode #5) — define core standards (mandatory) and flexible zones (experimental)
- Separate **principles** (universal, durable) from **standards** (contextual, evolving) and **preferences** (optional)

---

### Policy (POL-NNN)

**What it IS:**
A Policy is a **formal governance document or mandate** enacted by an authority (board, regulator, CISO, governance body) that creates binding boundaries on architecture and implementation choices. It is the **authorising source** for constraints — a policy does not directly restrict solution space, but it **generates** constraints (CST-NNN) that do. Policies answer *"What governance documents must we comply with?"* and capture the "why" and "who enacted it."

Every policy must have an **Issuing Authority** (who enacted it), an **Effective Date** (when it became binding), and a **Review Cycle** (when it expires or is reassessed). Policies have a **document lifecycle** distinct from the engagement: Draft → Enacted → Under Review → Superseded → Retired.

**ID scheme:** `POL-NNN` (e.g., POL-001, POL-002). Sequential within the engagement. Assigned by `/ea-policies add` when policies are captured in the Policies Register.

**Structural parts** (Policies Register row):
- **POL-NNN** — canonical policy ID
- **Title** — document title (e.g. "Cloud-First Procurement Policy v4.2")
- **Type** — Security / Procurement / Data Governance / Technology / Compliance / HR / Operational
- **Issuing Authority** — who enacted it (board, regulator, CISO, CFO, etc.)
- **Effective Date** — when the policy became binding
- **Review Cycle / Expiry** — when the policy is next reviewed or expires
- **Scope of Authority** — Enterprise / Divisional / Geographic
- **Statement** — summary of what the policy mandates
- **Document Reference / URL** — link to the actual policy document
- **Linked Constraints** — CST-NNN IDs generated by this policy
- **Linked Principles** — principles derived from or aligned with this policy
- **Status** — Draft / Enacted / Under Review / Superseded (by POL-NNN) / Retired

**What it is NOT:**
- Not a **Principle** — a principle is an internal normative decision filter created by the architecture board ("Technology choices must not create vendor dependency"); a policy is an external or governance-body mandate ("All vendor contracts >$100K require board approval")
- Not a **Constraint** — a constraint is the binding restriction *derived from* a policy ("Budget capped at $2M"); a policy is the *authorising document* that creates the constraint ("Capital Expenditure Policy v3.1")
- Not a **Requirement** — a requirement defines *what* the architecture must achieve with a measurable target ("API must respond within 200ms"); a policy does not have a measurable target — it authorises the rules that bound requirements
- Not a **Risk** — a policy is certain and enacted; a risk is uncertain and conditional

**Common confusions:**
- "We will not create dependency on a single vendor" — this is a **Principle** ✓ (internal normative rule). The **Policy** that authorises it is: "Vendor Diversification Policy, enacted by the Procurement Board, effective 2025-01-01." The **Constraint** derived from it is: "No single vendor may account for >60% of annual technology spend — CST-015"
- "All data at rest must be encrypted" — this is a **Policy** ✓ (governance mandate from CISO). The **Constraint** derived from it is: "Encryption must be AES-256-GCM or equivalent — CST-042"
- "The system must handle 10,000 concurrent users" — this is a **Requirement** (verifiable outcome), not a policy
- "Budget overrun is a risk" — this is a **Risk** (uncertain), not a policy. "The CFO has mandated a $2M budget cap" — that is a **Policy** ✓

**TOGAF placement:** Preliminary phase (capture existing enterprise policies); Architecture Vision (cite policies as constraint sources, §13); Governance Framework (list policies that govern architecture work). Policies are external inputs — the EA function does not create them, it discovers, catalogues, and traces them.

**ArchiMate:** `Contract` element (if the policy is a formal agreement) or `Business Object` element (if the policy is a governance document) in the Motivation aspect. Related to `Constraint` (policies generate constraints) and `Principle` (policies may motivate principles).

**Practitioner Notes:**
- Every policy must have a **named Issuing Authority**. Without an authority, a policy is unverifiable.
- Distinguish **Enterprise policies** (organisation-wide, read-only content) from **engagement-specific policy interpretations** (editable mappings to constraints). Enterprise policies are prefixed with 🔒 in the register.
- **Traceability check:** Every CST-NNN should trace to a POL-NNN, a regulation, a contract, or a stakeholder mandate. A constraint with Source = "Management decision" and no POL-NNN is a traceability gap.
- **Stale policy check:** A policy with Review Cycle past due and Status = Enacted may invalidate linked constraints. Run `/ea-policies trace` to flag stale policies.
- **Maturity marker (L1→L5):** L1 = policies mentioned only as free-text in constraint sources; L3 = policies catalogued with authority and review cycles; L5 = policies linked to automated compliance checks and validated at every architecture review
- **Cross-artifact consistency:** If a policy generates constraints in multiple artifacts, the Policies Register is the authoritative source — update the policy once, trace to all linked CST-NNN entries.

---

### Business Rule (BR-NNN)

**What it IS:**
A Business Rule is a **declarative governance statement that governs a specific business operation**, independent of how that operation is automated. It states *what* the business must, must not, should, or should not do under a defined condition, and *what outcome* follows. Business Rules are the operational source of truth for decisions that may be executed by people, applications, or both. They answer *"What operational rule must the business consistently enforce?"*

Every business rule has a **Subject** (the business entity or process it governs), a **Condition** (when it applies), a **Directive** (Must / Must Not / Should / Should Not), an **Outcome** (the result or action), and an **Authority** (who owns or enacted it). It is also linked to **Enforcement** (how compliance is verified) and to the **Business Service(s)** that operationalise it.

**ID scheme:** `BR-NNN` (e.g., BR-001, BR-002). Sequential within the engagement. Assigned by `/ea-rules add` when business rules are captured in the Business Rules Register.

**Structural parts (Business Rules Register row):**
- **BR-NNN** — canonical business rule ID
- **Subject** — the business entity, process, or decision the rule governs (e.g. "Customer eligibility for senior discount")
- **Condition** — the circumstance under which the rule applies (e.g. "Customer age is 65 or older AND purchase is made on a weekday")
- **Directive** — `Must` / `Must Not` / `Should` / `Should Not`
- **Outcome** — the business result or action produced when the condition is met (e.g. "Discount of 10% is applied")
- **Authority** — the role, policy, or body that owns the rule (preferred: link to POL-NNN or a named governance role)
- **Source** — Regulatory / Internal / Contractual / Market Practice / Policy-derived
- **Enforcement** — how compliance is verified: Manual review, Automated check, Workflow approval, Audit sample, System validation
- **Scope** — Enterprise 🔒 (organisation-wide) / Program (engagement-specific)
- **Status** — Active / Draft / Under Review / Superseded (by BR-NNN) / Retired
- **ADM Phase** — where the rule was identified or validated
- **Zachman Cell** — classification
- **Linked Business Services** — SVC-NNN IDs that operationalise this rule (Business-level services)
- **Linked Policies / Constraints** — POL-NNN and CST-NNN IDs derived from or enforcing this rule
- **Trace to Motivation** — DRV-NNN / G-NNN / OBJ-NNN / STR-NNN that the rule realises or constrains

**What it is NOT:**
- Not a **Policy** — a policy is the governance document or mandate that authorises rules; a business rule is the operational statement that operationalises the policy
- Not a **Constraint** — a constraint is a binding restriction on architecture or implementation choices; a business rule governs business behaviour and may *generate* constraints, but it is not itself an implementation boundary
- Not a **Requirement** — a requirement defines what the architecture must achieve with a measurable target ("API must respond within 200ms"); a business rule governs a business decision or condition
- Not a **Business Process** — a process is the step-by-step *how*; a rule is the declarative *what* that the process must satisfy
- Not an **Algorithm** — a rule states the business intent; the algorithm is an implementation choice for enforcing it

**Common confusions:**
- "A customer must be 18 or older to open an account" — this is a **Business Rule** ✓ (declarative operational rule with condition and directive)
- "All vendor contracts >$100K require board approval" — this is a **Policy** ✓ (governance mandate). The business rule derived from it is: "A vendor contract request with value >$100K must be routed to the board for approval — BR-021"
- "We must use AES-256-GCM encryption" — this is a **Constraint** ✓ (implementation restriction). The business rule behind it might be: "Customer data at rest must be protected against unauthorised disclosure — BR-042"
- "The claims system must settle 95% of claims within 24 hours" — this is a **Requirement** (measurable target), not a business rule
- "First verify identity, then check credit" — this is a **Business Process** (ordering of steps), not a business rule

**TOGAF placement:** Business Architecture (Phase B — business rules are discovered during capability and service modelling); Architecture Vision (cite high-level business rules as operational context); Requirements (business rules may generate or constrain REQ-NNN entries); Governance Framework (rules feed compliance and enforcement mechanisms). Business Rules are inputs from the business domain, not decisions made by the architecture function.

**ArchiMate:** Modelled as a `Business Object` or captured in a `Constraint` / `Business Process` relationship in the Business layer. A business rule is often realised by a `Business Service` and enforced by a `Business Process` or `Application Service`.

**Practitioner Notes:**
- Every business rule must have a **named Authority**. Without an authority, the rule is unenforceable and unverifiable.
- Keep rules **implementation-neutral**. A rule should not prescribe a system, API, or algorithm unless that restriction is itself a constraint.
- A single rule can generate **multiple constraints** (CST-NNN) and be operationalised by **multiple business services** (SVC-NNN). Maintain the traceability in both directions.
- **Traceability check:** Every BR-NNN should trace to at least one motivation element (driver, goal, objective, strategy) or policy. An orphan business rule is a governance gap.
- **Enforcement clarity:** "Manual review" is acceptable only if the review owner, frequency, and sample size are documented. Vague enforcement makes a rule ungovernable.
- **Maturity marker (L1→L5):** L1 = rules scattered as free-text in process documents; L3 = rules catalogued with condition/directive/outcome and linked to services; L5 = rules versioned, traced to automated decision services, and validated by conformance tests
- **Cross-artifact consistency:** If a business rule appears in both the Business Rules Register and a service or process artifact, the register version is authoritative. Update the rule once and propagate the BR-NNN reference.

---

### Constraint

**What it IS:**
A constraint is a non-negotiable restriction on the architecture or its implementation. It is **certain** — it will definitely apply regardless of decisions — and it limits the solution space by prohibiting or mandating specific choices. Every constraint must have a **Source** (the policy, regulation, contract, or mandate that created it) and an **Owner** (the person or role accountable for upholding it). Constraints answer *"What boundaries must we respect?"*

**ID scheme:** `CST-NNN` (e.g., CST-001, CST-002). Assigned by `/ea-constraints generate` when constraints are aggregated into the Constraints Register. Constraints may first appear as free-text in SBB "Constraints/Lock-in Risk" fields or as `category: Constraint` rows in the Requirements Register; these are re-mapped to `CST-NNN` on aggregation.

**Structural parts** (Constraints Register row):
- **CST-NNN** — canonical constraint ID assigned on aggregation
- **Type** — Technology / Regulatory / Budget / Timeline / Organisational / Interoperability
- **Statement** — the restriction, phrased as a binding rule (e.g. "Must deploy within existing AWS account")
- **Source** — the POL-NNN policy, regulation, contract, or stakeholder mandate that created this constraint. Preferred: link to a POL-NNN policy ID. Acceptable: free-text if the policy is not yet catalogued.
- **Owner** — who is accountable for upholding and verifying compliance with this constraint
- **Scope** — Enterprise 🔒 (organisation-wide) / Program (engagement-specific)
- **Priority** — High / Medium / Low
- **Status** — Active / Waived / Proposed
- **Waiver Justification** — required if Status is Waived; explains why the constraint is not enforced for this engagement
- **ADM Phase** — where identified
- **Zachman Cell** — classification
- **Linked Artifacts** — artifacts that must respect this constraint
- **Impact Assessment** — which capabilities, ABBs, SBBs, or work packages are bounded by this constraint

**What it is NOT:**
- Not a **Risk** — a constraint is certain and non-negotiable; a risk is uncertain and conditional
- Not a **Requirement** — a requirement defines *what* the architecture must achieve ("RTO < 4 hours"); a constraint restricts *how* it may be implemented ("Must use existing AWS account")
- Not a **Principle** — a principle is a normative decision filter ("Technology choices must not create vendor dependency"); a constraint is an externally imposed boundary ("Budget capped at $2M")
- Not an **Assumption** — an assumption is accepted as true for planning purposes but could be wrong; a constraint is binding regardless of belief
- Not a **Policy** — a policy is the governance document that *authorises* a constraint ("Capital Expenditure Policy v3.1"); a constraint is the binding restriction *derived from* it ("Budget capped at $2M")

**Common confusions:**
- "The project must complete by 31 December 2026" — this is a **Constraint** ✓ (certain, non-negotiable deadline)
- "We must handle 10,000 concurrent users" — this is a **Requirement** (verifiable outcome), not a constraint
- "We cannot use on-premise infrastructure" — this is a **Constraint** ✓ (restricts implementation choices)
- "Budget overrun is a risk" — this is a **Risk** (uncertain), not a constraint. "Budget is capped at $2M" — that is a **Constraint** (certain)

**TOGAF placement:** Architecture Vision (engagement constraints, §13); Architecture Principles (principles may generate constraints); Requirements Register (category: Constraint — legacy location, now deprecated in favour of standalone Constraints Register). The consolidated **Constraints Register** artifact aggregates all constraints into a single cross-cutting view — use `/ea-constraints` to generate it.

**ArchiMate:** `Constraint` element in the Motivation aspect. A restriction on implementation choices. Related to `Principle` (principles may motivate constraints), `Policy` (policies authorise constraints), and `Requirement` (constraints bound which requirements can be satisfied).

**Practitioner Notes:**
- Every constraint must have a **named Owner**. Without an owner, a constraint is unenforceable.
- Distinguish **Enterprise constraints** (organisation-wide, read-only content) from **Program constraints** (engagement-specific, fully editable). Enterprise constraints are prefixed with 🔒 in the register.
- **Traceability check:** Every SBB should reference the CST-NNN constraints that bound its selection. An SBB with vendor lock-in but no linked constraint is an orphan.
- **Policy linkage:** Every constraint's Source should ideally reference a POL-NNN policy ID. Constraints with free-text Source values ("Management decision") are traceability gaps — consider creating a POL-NNN for recurring sources.
- **Maturity marker (L1→L5):** L1 = constraints buried in free-text; L3 = constraints catalogued with owners and sources; L5 = constraints enforced automatically in pipelines and validated at every architecture review
- **Cross-artifact consistency:** If a constraint appears in both the Requirements Register (legacy) and the Constraints Register, the Constraints Register version is authoritative.

---

### Stakeholder Concern / Objection

**What it IS:**
A stakeholder concern or objection is a named challenge, question, or objection raised by a stakeholder or surfaced during a formal review (grill-me session, ARB review, executive challenge session). Unlike a Risk (which is an uncertain future event), a concern is a **present-tense challenge** to the architecture that requires either a documented response or a corrective action.

**ID scheme:** `CON-NNN` (e.g., CON-001). Assigned sequentially across the engagement; scoped to the artifact where the concern was raised. Aggregated by `/ea-concerns` into a cross-artifact Concerns Register.

**Structural parts** (Appendix A4 row):
- **ID** — CON-NNN
- **Concern** — the objection or question verbatim where possible
- **Raised By** — stakeholder name/role, or grill-me skill used
- **Category** — Scope / Goal / Approach / Feasibility / Risk / Stakeholder / Other
- **Status** — Addressed / Partially Addressed / Requires Attention
- **Response** — where in the artifact (or another) the concern is answered; blank if unresolved
- **Action / Owner** — what needs to happen and who is responsible (Requires Attention only)

**Distinction from Risk:** A concern becomes a Risk when it has a probability and a potential future impact on an objective. A concern that is "Requires Attention" and category "Risk" should be escalated to the Risk Register as a RIS-NNN entry.

**TOGAF placement:** Appendix A4 of every primary artifact. Aggregated via `/ea-concerns` into a cross-engagement Concerns Register.

---
