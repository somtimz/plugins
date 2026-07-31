# Two Layers of Intent: Business Change vs EA Enablement

This reference is split out from `ea-concepts.md` so the distinction, naming conventions, and quick test are available without loading the full concepts index. Subfile cross-references (e.g. "see Two Layers of Intent" in `concept-families/motivation-concepts.md`, `concept-families/business-layer-concepts.md`, `cross-topic-detection.md`, and `phase-questions/phase-a---architecture-vision-interview.md`) resolve here.

---

## The Core Distinction

| Layer | Subject | Question it answers |
|---|---|---|
| **Business Architecture** | Business capabilities and operations | *What does the business want to do?* |
| **EA / TOGAF Program** | Architecture capability and governance | *How do we structure, govern, and standardize change so it is done well?* |

> **Blunt framing:** Business architecture = **change** (what we want to transform). EA / TOGAF = **control** (how we ensure it is done right).

## Structural Model

Think in four layers. EA sits **across** the stack, not inside the business layer.

```
Layer 1 — Strategy
  Goals, Drivers

Layer 2 — Business Architecture
  Capabilities, Value Streams, Business Processes,
  Business Use Cases, Business Requirements

Layer 3 — Solution / Initiative
  Projects, Epics, Implementations

Layer 4 — EA / TOGAF (cross-cutting)
  Architecture Principles, Standards, Reference Architectures,
  EA Capability Use Cases, Architecture Requirements,
  Governance Processes, Architecture Decisions
```

- **Business artifacts** describe the organisation's desired future state and operational design.
- **EA artifacts** describe the rules, standards, and governance mechanisms that ensure solution initiatives conform to architecture direction.
- The two layers are **linked, not competing:** a Business Goal drives a solution initiative, which is then **governed by** an EA Use Case or Architecture Requirement.

## Visual Model

The diagram below shows the three domains (Business Architecture, Solution / Initiative, EA / TOGAF) and how they relate. Solid arrows show flow within a domain; dotted arrows show cross-cutting governance and enablement relationships.

![[Pasted image 20260508120316.png]]

Here's the Mermaid version.

```mermaid
flowchart TD
    subgraph L1["🔷 LAYER 1 — STRATEGY"]
        direction LR
        STR_D["📌 Strategic Driver"]:::strategy
        STR_G["🎯 Strategic Goal"]:::strategy
        STR_P["📐 Architecture Principle"]:::strategy
        STR_D --> STR_G --> STR_P
    end

    subgraph L2["🟢 LAYER 2 — BUSINESS ARCHITECTURE · Prefix: BIZ-"]
        direction LR
        BIZ_UC["Business Use Case"]:::biz
        BIZ_CAP["Business Capability"]:::biz
        BIZ_REQ["Business Requirement"]:::biz
        BIZ_PROC["Business Process"]:::biz
        BIZ_KPI["KPI / Metric"]:::biz
        BIZ_STK["Stakeholder Map"]:::biz
    end

    subgraph L3["🟠 LAYER 3 — EA / TOGAF PROGRAM · Prefix: EA-"]
        direction LR
        EA_UC["EA Use Case"]:::ea
        EA_REF["Reference Architecture"]:::ea
        EA_AREQ["Architecture Requirement"]:::ea
        EA_GOV["Governance Standard"]:::ea
        EA_ADR["ADR (Decision Record)"]:::ea
        EA_COMP["Compliance Checklist"]:::ea
    end

    subgraph L4["🟣 LAYER 4 — SOLUTION / INITIATIVE · Prefix: SOL-"]
        direction LR
        SOL_INIT["Initiative / Project"]:::sol
        SOL_ARCH["Solution Architecture"]:::sol
        SOL_GAP["Gap Analysis"]:::sol
        SOL_ROAD["Roadmap Item"]:::sol
    end

    subgraph TRACE["🔍 Traceability Example — AI Case Management"]
        direction LR
        T1["STR-001\nEfficiency"]:::strategy
        T2["BIZ-UC-01\nAutomate"]:::biz
        T3["SOL-001\nAI CMS"]:::sol
        T4["EA-GOV-03\nAI Gov"]:::ea
        T5["BIZ-REQ-07\nAccuracy"]:::biz
        T6["EA-STD-05\nModel Audit"]:::ea
        T7["SOL-001\nAI CMS"]:::sol
        T1 --> T2 --> T3 --> T4
        T5 --> T6 --> T7
    end

    L1 -->|"feeds"| L2
    L1 -->|"feeds"| L3
    L2 -. "governs" .-> L3
    L2 -->|"converges into"| L4
    L3 -->|"converges into"| L4
    L4 -->|"traced via"| TRACE

    classDef strategy fill:#dbeafe,stroke:#3b82f6,color:#1e3a8a,font-weight:bold
    classDef biz fill:#d1fae5,stroke:#10b981,color:#064e3b,font-weight:bold
    classDef ea fill:#ffedd5,stroke:#f97316,color:#7c2d12,font-weight:bold
    classDef sol fill:#ede9fe,stroke:#8b5cf6,color:#3b0764,font-weight:bold
```

## Naming Conventions

Use explicit prefixes to remove ambiguity. Both layers should still use the unified ID scheme (G-NNN, UC-NNN, REQ-NNN, etc.) — the prefix is for human readability in artifact titles and tables.

| Layer | Artifact | Naming pattern | Example |
|---|---|---|---|
| Business | Use Case | `Business Use Case: {actor goal}` | Business Use Case: Automate Case Management |
| Business | Requirement | `Business Requirement: {outcome}` | Business Requirement: Reduce handling time by 40% |
| Business | Goal | `Business Goal: {desired state}` | Business Goal: Automate case management with AI |
| EA / TOGAF | Use Case | `EA Capability Use Case: {capability}` | EA Capability Use Case: Govern AI Solutions |
| EA / TOGAF | Requirement | `Architecture Requirement: {rule}` | Architecture Requirement: All AI models must pass bias audit |
| EA / TOGAF | Goal | `EA Goal: {capability outcome}` | EA Goal: Establish AI architecture governance |

## Quick Test: "Would this still exist without the EA team?"

When an item feels ambiguous, apply this test:

- **If the item would still exist if the EA team were disbanded** → it is **Business Architecture**
  - Example: *Automating case management with AI* — the business still needs this.
- **If the item would disappear if the EA team were disbanded** → it is **EA / TOGAF**
  - Example: *Defining an AI governance process* — this is an EA capability, not a business operation.

## Example: AI in Case Management — Cleanly Separated

**Business Layer (running the business)**
- **Goal:** Automate case management with AI
- **Use Cases:**
  - Auto-triage cases
  - AI-assisted decisioning
  - Document classification
- **Requirements:**
  - Accuracy thresholds
  - Compliance constraints
  - Integration with CRM
- **Drivers:**
  - Reduce processing time
  - Improve service quality

**EA / TOGAF Layer (enabling controlled delivery)**
- **Use Case:** Define governance process for AI projects
- **Requirements:**
  - Model validation standards
  - Risk classification framework
  - Approval workflows
- **Outputs:**
  - Architecture principles
  - Reference architectures
  - Governance checkpoints

**Relationship map:**
```
Business Goal: Automate case management with AI
  ↓
Solution initiative: AI solution implementation
  ↓
Governed by → EA Capability Use Case: Govern AI Solutions
```

## When to Surface This Distinction

- During **Phase A interviews** when stakeholders describe "goals" that are actually about governance, standards, or EA team capabilities.
- During **Phase B Business Architecture** when business use cases are drafted — flag any whose subject is "governance," "standards," or "review" as likely EA-layer items.
- During **/ea-direction --quality** scans when a direction item's subject is ambiguous.
- During **/ea-grill** reviews when an artifact mixes business and EA intent without explicit labeling.

## Mapping Relationships Between the Two Layers

Do not keep the two layers separate in your head — connect them structurally:

| Business Layer | Relationship | EA / TOGAF Layer |
|---|---|---|
| Business Goal | drives | Solution initiative |
| Solution initiative | governed by | EA Capability Use Case |
| EA Governance | enforces | Architecture Requirements |
| Architecture Requirements | constrain | Solution design |
| Architecture Decisions | guide | Solution implementation |
