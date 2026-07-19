# Phase C — Information Systems Interview


**Goal:** Understand data entities, application portfolio, and data/application goals

**Key questions:**
1. What are the key data domains in your organisation — the major categories of information you manage?
2. Which applications support each of the business functions we identified?
3. Which applications are considered strategic investments, and which are candidates for replacement?
4. Where do you have data duplication or inconsistency problems across systems?
5. What are the critical integration points between applications?
6. Are there regulatory requirements governing specific data? (select all that apply)
   - [ ] Privacy — GDPR, CCPA, LGPD, or equivalent
   - [ ] Data retention — legal hold, archiving, or disposal obligations
   - [ ] Data classification — sensitivity labels and handling requirements
   - [ ] Data sovereignty / residency — data must remain in-country or in-region
   - [ ] Sector-specific — HIPAA, PCI-DSS, SOX, ISO 27001, or similar
   - [ ] None identified
   - [ ] Other: ___
7. Who owns each application and each major data domain?
8. What is the single biggest challenge you face with your data and application landscape today?

**Application Architecture Design Questions:**

9. For each target application component: what is its primary responsibility? And equally important — what is NOT its responsibility? Where is its boundary with adjacent components?

10. What architecture pattern best describes the target application landscape?
    - [ ] Modular Monolith — single deployable unit with well-defined internal modules
    - [ ] Microservices — independently deployable services per bounded context
    - [ ] Event-driven — services communicate primarily via events / message bus
    - [ ] Serverless — functions-as-a-service with no persistent application tier
    - [ ] COTS / SaaS-led — mostly packaged software; custom code only at the edges
    - [ ] Hybrid — combination of above; describe which pattern applies where
    Why was this pattern chosen? What constraints (cost, skills, timeline, regulatory) drove the decision?

11. For each significant application component: describe its internal structure.
    - What are the major internal modules or layers? (e.g. Presentation, Business Logic, Data Access, Integration Adapter)
    - Which modules are most likely to change frequently — and should therefore be isolated from stable modules?
    - Which modules need to be independently scalable?

12. What services or APIs does each component expose to other components or external consumers?
    - For each service: what does it do, what are the exact consumers, and what is the protocol (REST / GraphQL / gRPC / event)?
    - What authentication and authorisation model applies to each API?
    - Is there an SLA (max response time, availability target) that consumers depend on?

13. Walk me through the user journey for the most business-critical use case (reference UC-NNN from Business Architecture). Which application components are touched in sequence?
    - What is the user interaction model — web UI, mobile app, API call, or batch?
    - Where are the key latency or reliability sensitivity points in this journey?
    - What happens to the user journey if any one component is unavailable?

14. For each architecturally significant component: what are the non-functional requirements?
    - **Performance:** max acceptable response time; throughput (requests/sec or records/hr)
    - **Availability:** uptime target (e.g. 99.9%); acceptable maintenance window
    - **Scalability:** horizontal or vertical; what triggers a scale event?
    - **Data volume:** current record counts and 3-year projected growth

15. How are events or state changes communicated between components?
    - Is the primary integration pattern synchronous (request/response) or asynchronous (event/message)?
    - If asynchronous: what is the message broker or event bus? (e.g. Kafka, Azure Service Bus, AWS SQS)
    - How are event schemas defined, documented, and versioned? Who is responsible for schema governance?

16. What COTS or SaaS products are being adopted for commodity capabilities?
    - For each: which business capability (CAP-NNN) does it replace or augment?
    - What customisation or extension points will be used — and is customisation within the vendor's supported model?
    - What is the integration pattern for connecting this COTS product to the broader application landscape?

9. *(If Data direction not yet defined)* Capture Data direction using the three-type model:
   - **Data goal** example: "Have a single source of truth for customer data" (qualitative, no deadline)
   - **Data objective** example: "Reduce duplicate customer records by 90% by June 2026" (measurable + deadline)
   - **Data strategy** example: "Implement a master data management platform" (approach, not outcome)

10. *(If Application direction not yet defined)* Capture Application direction using the three-type model:
    - **Application goal** example: "Operate a modern, composable application landscape"
    - **Application objective** example: "Decommission 3 legacy systems by Q2 2027"
    - **Application strategy** example: "Adopt SaaS-first for commodity capabilities"

**Architecture Building Block (ABB) questions:**
> Ask these when defining the target application/data landscape. ABBs are logical, vendor-neutral components — do not name specific products here.

11. For each significant application component identified: what is the logical function it provides — described without naming a vendor or product? (e.g. "Immutable Log Store", not "AWS CloudTrail"; use a noun phrase, not an action: "Database Backup Service", not "Back up the database")
    - What requirement(s) (REQ-NNN) does this ABB satisfy?
    - What is its architecture domain — Application or Data?
    - Assign an ABB-NNN ID and capture in the ABB Register.

12. For each ABB: is it reusable across multiple capabilities or is it single-purpose?
    - Reusable ABBs should have a generic name and broad description.
    - Single-purpose ABBs should trace to a specific capability (CAP-NNN) and requirement (REQ-NNN).

### Decision Quality Questions
> Ask these after completing the standard Phase C questions. Data and application decisions are high-impact and often hard to reverse — evidence and optionality matter most here.

1. **[DECISION]** For each technology or vendor selection proposed: what POC, benchmark, or reference implementation is required before commitment? Has it been scheduled?
2. **[DECISION]** What is the reversibility of each chosen data model or application pattern? If wrong, how many downstream systems are affected?
3. **[DECISION]** What optionality is preserved? (e.g., API-first design allows vendor swap; domain-driven boundaries allow technology change without consumer impact.)
4. **[DECISION]** Are there MUST requirements that should disqualify any candidate option? Has a weighted scorecard been applied?
5. **[DECISION]** Is there strong stakeholder pressure for a specific vendor or platform? What is the defensible evidence-based position?
6. **[DECISION]** Which unresolved data or application decisions should be logged as PAD-NNN rather than committed now?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Key data domains | Data Architecture | `{{data_domains}}` |
| Applications per function | Application Architecture | `§2 Current Application Portfolio` |
| Strategic applications | Application Architecture | `§3 Target Application Landscape` |
| Replacement candidates | Application Architecture | `§3 Target Application Landscape — Status: Replace / Retire` |
| Gap Analysis (application) | Gap Analysis | `{{application_gaps}}` |
| Data duplication issues | Data Architecture | `{{data_quality_issues}}` |
| Integration points | Application Architecture | `§5 Integration Architecture` |
| Regulatory data requirements | Requirements Register | `{{data_regulatory_requirements}}` |
| Data Architecture gaps | Gap Analysis | `{{data_gaps}}` |
| Application ownership | Application Architecture | `§2 Current Application Portfolio` |
| Data domain ownership | Data Architecture | `{{data_ownership}}` |
| Key data/app challenge | Gap Analysis | `{{key_challenge}}` |
| Component responsibilities and boundaries | Application Architecture | `§4 Application Components — Responsibility` |
| Architecture pattern selection | Application Architecture | `§4 Application Components — Architecture Pattern` |
| Component internal modules / layers | Application Architecture | `§4 Application Components — Internal Modules/Layers table` |
| Service / API contracts | Application Architecture | `§4 Application Components — Service Contracts table` + `§5 API Catalog` |
| User journeys through applications (UC-NNN) | Application Architecture | `§1a User Journeys & Use Cases` |
| NFRs per component | Requirements Register | `REQ-NNN` type:non-functional, scope:application |
| Integration pattern (sync / async) | Application Architecture | `§5 Integration Architecture — Integration Pattern` |
| Event schema governance | Application Architecture | `§5 Integration Architecture — Integration Pattern` |
| COTS / SaaS adoption decisions | Application Architecture | `§3 Target Application Landscape — Rationale` |
| Data direction (goals, objectives, strategies) | engagement.json + Logical Data Model | `direction.Data` + `{{data_direction}}` |
| Data metrics | engagement.json + Logical Data Model | `metrics.Data` + `{{data_metrics}}` |
| Application direction (goals, objectives, strategies) | engagement.json + Application Portfolio Catalogue | `direction.Application` + `{{application_direction}}` |
| Application metrics | engagement.json + Application Portfolio Catalogue | `metrics.Application` + `{{application_metrics}}` |

**Facilitation Notes:**
- Bring an application inventory template to the session pre-populated with known systems — asking people to add to a list is more productive than asking them to recall from memory.
- The "strategic vs replacement" question often surfaces political tensions; frame it as investment prioritisation rather than a performance critique of existing systems.
- Data ownership questions frequently reveal ungoverned domains — treat "no one owns it" as a gap finding, not an oversight to skip.
- Ask for data flow diagrams or integration documentation after the session; verbal descriptions of integration points are rarely complete.
- Run architecture pattern selection (Q10) as an explicit decision — it should go through the A3 Decision Log. Patterns chosen by default rather than by design are a significant governance gap.
- Component boundary questions (Q9) are most productive with technical leads, not just architects — the people who implement components know where the real boundaries are.
- Use case tracing (Q13) should be done for at least the top 3 critical use cases from the Business Architecture — single use case coverage is insufficient for system-of-systems design.
- NFR elicitation (Q14) should be captured per component, not for the whole system — aggregate NFRs hide where the real engineering constraints are.
- Event schema governance (Q15) is frequently neglected until integration breaks — establish ownership and versioning policy during Phase C, not during implementation.

**§D Diagrams — ask at close of session:**
> "Five diagrams are standard for Phase C. Which would you like to create or describe now?"
- **Conceptual Data Model** — business-readable subject areas and their relationships (`data-architecture-conceptual-data-model.mmd`)
- **Data Flow Diagram** — how data moves between systems and across boundaries (`data-architecture-data-flow.mmd`)
- **Application Cooperation View** — integration topology showing how applications interact (`application-architecture-cooperation.mmd`)
- **Application Component Map** — internal decomposition of key applications (`application-architecture-component-map.mmd`)
- **User Journey Trace** — sequence diagram showing which components are touched for a critical use case (`application-architecture-journey-trace.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to the relevant artifact frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions — C-Data (optional)
> Offer this section after completing the standard Phase C data questions. Ask: "Would you like to address security concerns for Phase C Data Architecture? (y/n)"

**SABSA focus:** Logical — data classification, protection services, and privacy obligations

1. What data classification levels apply? (e.g., Public / Internal / Confidential / Restricted — or organisation-specific scheme)
2. What data is most sensitive or regulated? (personal data, payment data, health data, IP, classified)
3. What are the encryption requirements — at rest and in transit? Are there approved algorithms or key lengths?
4. What data retention and deletion obligations exist? What triggers deletion?
5. What privacy requirements apply? Is GDPR Article 25 (privacy by design and by default) a relevant obligation?
6. Where does data reside — jurisdiction constraints, cross-border transfer restrictions?

**Output routing:**
| Answer | Output |
|---|---|
| Data classification scheme | Data Architecture (classification table) |
| Encryption at rest and in transit | Data Architecture (encryption specification), REQ-NNN type:security, category:data-protection |
| Retention and deletion | Data Architecture (retention policy), REQ-NNN type:security, source:ISO27001, control:A.8.10 |
| Privacy requirements | Data Architecture (privacy notes), REQ-NNN type:security, category:privacy |

### Security Questions — C-App (optional)
> Offer this section after completing the standard Phase C application questions. Ask: "Would you like to address security concerns for Phase C Application Architecture? (y/n)"

**SABSA focus:** Logical — identity, access, audit, and secure development

1. What authentication model is required? (SSO, MFA, federated identity, protocol: SAML / OIDC / Kerberos)
2. What authorisation model applies? (RBAC, ABAC, policy-based — what granularity of access control is needed?)
3. What audit logging is required? Who needs to see logs, for how long, and in what format?
4. How are APIs secured? (OAuth 2.0, mTLS, API gateway, rate limiting)
5. What are the secure coding standards for this application? (OWASP, SSDLC, code review requirements)
6. What is the approach to vulnerability management — SAST, DAST, penetration testing frequency?

**Output routing:**
| Answer | Output |
|---|---|
| Authentication model | Application Architecture (auth model section), REQ-NNN type:security, category:access-control |
| Authorisation model | Application Architecture (authz model), REQ-NNN type:security, source:ISO27001, control:A.5.15 |
| Audit logging | Application Architecture (logging requirements), REQ-NNN type:security, source:ISO27001, control:A.8.15 |
| API security | Application Architecture (API security section) |

---
