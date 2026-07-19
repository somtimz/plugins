# Phase G — Implementation Governance Interview


**Goal:** Establish governance and compliance monitoring

**Key questions:**
1. How will architecture compliance be monitored during implementation?
2. Who has the authority to approve change requests during delivery?
3. What is the expected reporting cadence for architecture status updates?
4. How will architecture requirements be enforced in contracts with delivery teams or vendors?
5. How will project deviations from the approved architecture be handled?
6. What tools or processes will be used to track compliance and issues?

### Decision Quality Questions
> Ask these after completing the standard Phase G questions. Governance is where decisions are enforced — deviations must be justified with evidence.

1. **[DECISION]** Are deviations from the approved architecture justified with evidence, or are they exceptions without rationale? Unjustified deviations erode decision quality.
2. **[DECISION]** Is governance effort focused on high-risk, irreversible decisions — or does it review everything equally? (Elite practice: guardrails for reversible, review for irreversible.)
3. **[DECISION]** Are conformance checks automated (CI/CD, policy-as-code) or manual? Manual-only governance scales poorly and creates bottlenecks.
4. **[DECISION]** How are PAD-NNN entries that expire during implementation handled? Are they escalated or silently ignored?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Compliance monitoring approach | Compliance Assessment | `{{compliance_monitoring}}` |
| Change approval authority | Architecture Contract | `{{change_approval_authority}}` |
| Reporting cadence | Compliance Assessment | `{{reporting_cadence}}` |
| Contract enforcement approach | Architecture Contract | `{{contract_enforcement}}` |
| Deviation handling process | Architecture Contract | `{{deviation_process}}` |
| Compliance Assessment process | Compliance Assessment | `{{assessment_process}}` |
| Tracking tools and processes | Compliance Assessment | `{{tracking_tools}}` |

**Facilitation Notes:**
- Governance interviews work best with both architecture leadership and project delivery leadership in the room — differences in expectation about compliance authority are common and must be resolved before delivery starts.
- Ask for examples of how past deviations were handled to understand the real governance culture rather than the stated policy.
- Reporting cadence questions should result in a concrete schedule, not a generic answer like "regularly" — pin down frequency and format.
- Contract enforcement is often overlooked in internal engagements; make it explicit even when no external vendor is involved.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase G? (y/n)"

**SABSA focus:** Operational — security operations model, compliance, and incident management

1. How will security compliance be assessed during implementation? Who performs the assessment?
2. Who is responsible for security operations once the architecture is live? (internal SOC, MSSP, hybrid)
3. What security monitoring and alerting is in place — or needs to be stood up — before go-live?
4. How are security incidents managed? Is there a tested incident response plan?
5. Is an ISO 27001 Statement of Applicability required? Who is responsible for maintaining it?
6. What are the security acceptance criteria for the Implementation Governance Plan — what must be true before sign-off?

**Output routing:**
| Answer | Output |
|---|---|
| Compliance assessment approach | Compliance Assessment (Phase G artifact) |
| Security operations model | Implementation Governance Plan (security operations section) |
| Incident response | Governance Framework (incident management), Implementation Governance Plan |
| Statement of Applicability | Compliance Assessment (SoA reference or draft) |

---
