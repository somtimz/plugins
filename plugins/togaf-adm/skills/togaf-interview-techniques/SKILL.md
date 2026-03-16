---
name: togaf-interview-techniques
description: This skill should be used when the user asks to "run a stakeholder interview", "interview a business owner", "elicit architecture requirements", "conduct an architecture workshop", "gather business drivers", "capture stakeholder concerns", "start a Phase A interview", "interview for business capabilities", or any request to conduct structured questioning for TOGAF artifact inputs.
version: 0.1.0
---

# TOGAF Architecture Interview Techniques

Structured interviews are the primary mechanism for eliciting architecture inputs from stakeholders. Each ADM phase has distinct questions aligned to its artifacts. This skill provides question sets, facilitation guidance, and output capture patterns.

## Interview Principles

- Ask one question at a time — avoid overwhelming stakeholders
- Probe responses with "Can you give an example?" or "What would success look like?"
- Capture verbatim responses before summarising
- Validate captured outputs with the stakeholder before proceeding
- Map all responses to the relevant artifact field

## Phase-by-Phase Interview Question Sets

### Preliminary Phase Interview
**Goal**: Establish architecture principles and governance model

Key questions:
1. What are the top 3 strategic goals of the organisation for the next 3 years?
2. What constraints (regulatory, financial, technical) must the architecture comply with?
3. Who are the key decision-makers for IT investment?
4. Is there an existing architecture governance body? How does it operate?
5. What does good architecture practice look like in your organisation?

**Outputs captured**: Architecture Principles draft, Governance Model inputs

---

### Phase A — Architecture Vision Interview
**Goal**: Define scope, concerns, and high-level target

Key questions:
1. What business problem or opportunity is driving this architecture engagement?
2. What does success look like at the end of this engagement?
3. Who are the key stakeholders and what are their primary concerns?
4. What is in scope and out of scope for this architecture?
5. Are there any known constraints or assumptions?
6. What existing architecture assets or documents should we consider?
7. What is the desired timeline for completion?

**Outputs captured**: Statement of Architecture Work inputs, Stakeholder Map entries, Architecture Vision narrative

---

### Phase B — Business Architecture Interview
**Goal**: Define business capabilities, processes, and gaps

Key questions:
1. What are the primary business functions this organisation performs?
2. Can you describe the key end-to-end business processes?
3. Where do you see pain points or inefficiencies today?
4. What capabilities do you wish the business had but currently lacks?
5. How is the organisation structured (divisions, teams, geography)?
6. What business outcomes are most important to improve?
7. What does the future state of the business look like in 3–5 years?

**Outputs captured**: Business Capability Map, Process Flow inputs, Gap Analysis (business)

---

### Phase C — Information Systems Interview
**Goal**: Understand data entities and application portfolio

Key questions:
1. What are the key data domains your organisation manages (customers, products, financials, etc.)?
2. What applications currently support each business function?
3. Which applications are considered strategic and which are candidates for replacement?
4. Where does data duplication or inconsistency occur?
5. What are the critical integration points between systems?
6. Are there regulatory requirements for data residency, retention, or privacy?

**Outputs captured**: Application Portfolio Catalog, Data Entity Catalog, App/Function Matrix

---

### Phase D — Technology Architecture Interview
**Goal**: Understand current and desired technology platform

Key questions:
1. What is the current technology stack (infrastructure, cloud, on-premise)?
2. What technology standards or approved products does the organisation mandate?
3. What technology capabilities are missing or insufficient?
4. What is the organisation's cloud strategy?
5. What are the key technology constraints (budget, skills, vendor lock-in)?
6. What does the technology landscape look like in 3 years?

**Outputs captured**: Technology Portfolio Catalog, Technology Standards, Gap Analysis (technology)

---

### Phase E/F — Opportunities and Roadmap Interview
**Goal**: Prioritise work packages and build the roadmap

Key questions:
1. Which capability gaps are highest priority to address?
2. What projects are already in flight that the architecture must align with?
3. What is the investment budget and timeline for transformation?
4. Are there sequencing dependencies between initiatives?
5. What transition states are acceptable (can the business tolerate multiple phases)?

**Outputs captured**: Work Package list, Roadmap priorities, Implementation and Migration Plan inputs

---

## Facilitation Patterns

### One-on-One Stakeholder Interview
- Duration: 45–60 minutes
- Format: Conversational, one question at a time
- Capture: Record responses in the plugin context; generate Requirements Register entries at the end
- Validate: Summarise and confirm with stakeholder before closing

### Workshop (Group)
- Duration: 2–4 hours
- Format: Present questions on screen, capture group responses collaboratively
- Use: Capability mapping workshops, gap analysis reviews, roadmap prioritisation
- Technique: Dot-voting for prioritisation, affinity grouping for capabilities

### Document Review Interview
- Trigger: When stakeholder provides a document instead of answering questions
- Action: Use `/togaf:load [file]` to ingest the document, then run `requirements-analyst` agent
- Follow-up: Generate specific gap questions based on what the document does not cover

## Capturing and Routing Interview Outputs

After each interview, route captured information to the appropriate artifact:

| Interview Response | Target Artifact |
|-------------------|-----------------|
| Business goals/drivers | Architecture Vision, Principles |
| Stakeholder names/roles/concerns | Stakeholder Map |
| Business capabilities mentioned | Business Capability Map |
| Process descriptions | Process Flow Diagram |
| Application names/owners | Application Portfolio Catalog |
| Pain points / gaps | Gap Analysis |
| Future state desires | Target Architecture |
| Regulatory/policy constraints | Requirements Register |
| Timeline preferences | Architecture Roadmap |

## Auto-Population Pattern

When an interview response maps to an artifact field:
1. Record the raw response
2. Flag it with the target artifact and field
3. Propose the mapped value to the user for confirmation
4. Add to the artifact automatically on confirmation

Use `/togaf:status` to see how many artifact fields have been populated from interviews.

