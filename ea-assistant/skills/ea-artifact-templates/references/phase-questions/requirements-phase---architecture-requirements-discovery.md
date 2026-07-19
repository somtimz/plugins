# Requirements Phase — Architecture Requirements Discovery


**Goal:** Discover and capture all architecture requirements — functional, non-functional, constraints, and assumptions. Run in phase mode (`/ea-interview start phase requirements`) before or alongside Phase A.

- Functional and non-functional requirements are written to the Requirements Register as `REQ-NNN` items.
- Constraints are written to the Constraints Register as `CST-NNN` items via `/ea-constraints add`.
- Legacy `category: Constraint` in the Requirements Register remains valid for backward compatibility but is deprecated for new capture.

**Before starting:** Ask for any existing requirements documents, standards registers, or service-level agreements. Start from what exists rather than from blank.

---

### Functional Requirements

1. What must the architecture enable that is not possible today? List the top 3–5 new business capabilities required.
2. Which existing capabilities must be preserved, enhanced, or replaced in the target state?
3. Are there specific integration or interoperability requirements — systems that must exchange data or trigger each other? For each boundary surfaced, apply `skills/ea-requirements-management/references/interoperability-requirements.md` — category (business/information/technical), degree (1–4), and capture conventions (REQ-NNN with measurable target; IFC-NNN for degree ≥ 3 boundaries).
4. Are there reporting or data access requirements — what information must be available to whom and when?
5. Are there workflow or process automation requirements that the architecture must support?

---

### Non-Functional Requirements — Ask one question per category

For each NFR category, ask the discovery question and, if answered, capture as REQ-NNN with `category: Non-Functional`, the appropriate `nfrSubType`, and a `measurableTarget`. If a category is not applicable to this engagement, mark it skipped.

| NFR Category | Discovery Question | Measurable Target Prompt |
|---|---|---|
| **Availability** | What is the minimum acceptable uptime? Are there critical periods (e.g. financial year-end, peak trading) where the system must never be unavailable? | Target: ___% availability measured monthly; planned maintenance window: ___ hours/month |
| **Reliability** | What failure rate is acceptable? Must the system continue operating in degraded mode if a component fails? What is the tolerated Mean Time Between Failures? | MTBF target: ___; tolerated failure rate: ___%; fault-tolerance model (active-active / active-passive / none) |
| **Performance** | What response times are expected under normal and peak load? How many concurrent users or transactions must be supported? | p95 response: ___ms; peak concurrent users: ___; throughput: ___ transactions/sec |
| **Security** | What authentication and authorisation model is required? Are there encryption, audit logging, or non-repudiation requirements? Which regulatory security frameworks apply? | Authentication method; data classification levels; encryption standards (AES-256, TLS 1.3+); compliance reference (ISO 27001, NIST CSF) |
| **Usability** | What accessibility standards apply? What is the target for task completion time, error rate, or user satisfaction? Are there specific user groups (e.g. assistive technology users) to support? | WCAG level (A / AA / AAA); task completion target; accessibility compliance date |
| **Maintainability** | How frequently must the system be updated or patched without downtime? What test coverage or code quality threshold is expected? What is the maximum acceptable time to diagnose and fix a production defect? | Deployment frequency; test coverage: ___%; MTTR target: ___ hours |
| **Portability** | Must the solution run on or be migrated to multiple platforms, cloud providers, or deployment models? Are there vendor lock-in constraints? | Target platforms / cloud providers; portability criteria; exit strategy requirement |
| **Compatibility** | What existing systems must the solution co-exist with and not disrupt? Are there API versioning or backward-compatibility requirements? | Existing systems to preserve; API backward-compat window: ___ months |
| **Recoverability** | What are the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for each critical component? What disaster recovery scenarios must be planned for? | RTO: ___ hours; RPO: ___ hours; DR scenario scope (single node / AZ / region / full DC) |

---

### Constraints

6. Are there mandated technology choices — cloud platforms, vendors, or infrastructure that must be used or must not be replaced?
7. Are there regulatory, legal, or contractual obligations that constrain the solution space (e.g. data residency, GDPR, financial regulation)?
8. Are there budget ceilings or timeline deadlines that are non-negotiable?
9. Are there organisational constraints — approved vendor panels, procurement rules, or internal policies that limit options?
10. Are there interoperability constraints — systems that must not be replaced or must be integrated without modification?

---

### Assumptions

11. What assumptions are you making about future business volumes, user growth, or technology capacity that underpin these requirements?
12. What assumptions are you making about the availability of skills, budget, or resources to implement the architecture?
13. What happens to the architecture if any of these assumptions prove false — what is the consequence and the mitigation?

---

### Process and Governance

14. How are requirements currently gathered and documented in your organisation? Who has authority to approve and prioritise?
15. How are conflicting requirements resolved? Who has the final word when two stakeholders disagree?
16. At what cadence will requirements be reviewed and updated during the engagement?

---

**Output Routing:**

| Captured Answer | Written To | ID Prefix | Fields Set |
|---|---|---|---|
| Functional requirement | Requirements Register — Enterprise or Program section | REQ-NNN | `category: Functional` |
| Non-functional requirement | Requirements Register — Enterprise or Program section | REQ-NNN | `category: Non-Functional`, `nfrSubType`, `measurableTarget` |
| Constraint | Requirements Register (Category: Constraint) | REQ-NNN | `category: Constraint` |
| Assumption | Requirements Register (Category: Assumption) | REQ-NNN | `category: Assumption` |
| Requirements governance process | Requirements Register executive summary | — | Prose context |

**NFR coverage check:** After all NFR questions, display the coverage status:
```
NFR Coverage: Availability ✅ | Reliability ⬜ | Performance ✅ | Security ✅ | Usability ⬜ | Maintainability ⬜ | Portability ➖ | Compatibility ✅ | Recoverability ✅
⬜ = not answered  ➖ = not applicable  ✅ = captured
```
Offer to skip remaining uncovered categories or continue.

**Facilitation Notes:**
- Run this session before Phase A interviews — requirements drive the Architecture Vision, not the reverse.
- NFR questions often surface unstated assumptions. When a stakeholder says "it must be fast", ask: "What does fast mean specifically — for whom, under what load, measured how?"
- Requirements without measurable targets cannot be tested. Refuse to mark an NFR as Approved until a measurable target is agreed.
- Ask for any existing SLAs, service management agreements, or IT policy documents — they contain implicit NFRs that would otherwise be missed.
- If no traceability process exists, recommend adopting the Traceability Matrix from the engagement start rather than retrofitting it.

---
