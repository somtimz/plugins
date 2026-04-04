# Engagement Types and Architecture Domains

## Engagement Types

| Type | Description | ADM Focus |
|---|---|---|
| Greenfield | Building a new capability, business unit, or system from scratch. No baseline architecture. | Full ADM; emphasis on Phase A (Vision) and Phases B-D (target state) |
| Brownfield | Transforming existing systems, processes, or data while keeping the business running. | Full ADM; emphasis on baseline documentation in B-D and transition planning in E-F |
| Assessment-only | Current-state review of existing architecture without planning implementation changes. | Prelim, Requirements, A, and domain phases only; E-H are Not Applicable |
| Migration | Re-platforming or re-hosting workloads (e.g., cloud migration, data centre move). | Full ADM; emphasis on Phase D (Technology) and E-F (migration planning) |

See `references/engagement-patterns.md` for detailed tailoring guidance per type.

## Architecture Domains

Users select which architecture domains are in scope at engagement creation. At least one domain MUST be selected. Default: all four.

| Domain | ADM Phase | Description |
|---|---|---|
| Business | B | Business processes, capabilities, organisation, functions |
| Data | C-Data | Data entities, data components, data management |
| Application | C-App | Application components, interfaces, application services |
| Technology | D | Technology components, platforms, infrastructure |

Deselecting a domain sets its corresponding ADM phase to "Not Applicable" and excludes domain-specific artifacts from scaffolding.

## ADM Phase Map

| Phase | Name | Key Deliverables |
|---|---|---|
| Prelim | Preliminary | Architecture Principles, Org Model, Tailoring |
| Requirements | Architecture Requirements | Requirements Register, Traceability Matrix |
| A | Architecture Vision | Statement of Architecture Work, Architecture Vision |
| B | Business Architecture | Business Model Canvas, Business Architecture document |
| C-Data | Data Architecture | Data Architecture document |
| C-App | Application Architecture | Application Architecture document |
| D | Technology Architecture | Technology Architecture document |
| E | Opportunities & Solutions | Architecture Roadmap, Implementation Plan |
| F | Migration Planning | Migration Plan, Architecture Roadmap (updated) |
| G | Implementation Governance | Architecture Contracts, Compliance Assessments |
| H | Architecture Change Management | Change Requests, Updated Architecture |

Phases can be started, edited, or resumed in any order. Navigation is non-linear.
