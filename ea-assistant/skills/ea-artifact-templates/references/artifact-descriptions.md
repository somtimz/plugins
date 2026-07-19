# EA Artifact Descriptions — Reference

This reference describes each TOGAF-aligned architecture artefact supported by the EA Assistant. For each artefact it provides: purpose, intended audience, contents, when to create it, who reviews it, and which ADM phase it primarily belongs to.

---

| Phase | Artifact | Purpose | Template / Command | Details |
|---|---|---|---|---|
| Preliminary | Engagement Charter | The foundational Preliminary Phase artifact. Establishes the authoritative record of why the engagement exists, what it covers, who it affects, how it is structured, and what it is expected to deliver. | `engagement-charter.md` — `/ea-artifact create engagement-charter` | [details](artifact-descriptions/preliminary-phase-artefacts.md) |
| Preliminary | Architecture Principles Catalogue | Documents the set of normative statements that govern all future architecture decisions for the enterprise. | — | [details](artifact-descriptions/preliminary-phase-artefacts.md) |
| Preliminary | Architecture Governance Framework | Defines how architecture decisions are made, communicated, and enforced. | `governance-framework.md` — `/ea-artifact create governance-framework` | [details](artifact-descriptions/preliminary-phase-artefacts.md) |
| A | Architecture Vision | Provides a high-level, stakeholder-oriented description of the target architecture and the value it will deliver. | — | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Statement of Architecture Work | A formal agreement between the architecture team and the commissioning organisation that defines scope, schedule, deliverables, resources, and acceptance criteria. | — | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Stakeholder Map and Matrix | Identifies all stakeholders relevant to the architecture engagement, their concerns, interest, and influence. | — | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Business Case | The economic and political instrument that secures the mandate and funding for the architecture engagement. | `business-case.md` — `/ea-artifact create business-case` | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Communications Plan | Defines how architecture information will be communicated to each stakeholder group throughout the ADM cycle. | `communications-plan.md` — `/ea-artifact create communications-plan` | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Business Transformation Readiness Assessment | Rates the organisation's readiness to absorb the transformation across twelve TOGAF dimensions. | `business-transformation-readiness.md` — `/ea-artifact create business-transformation-readiness` | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| A | Architecture Definition Document | The primary container for all architecture descriptions produced across the ADM lifecycle. | `architecture-definition-document.md` — `/ea-artifact create architecture-definition-document` | [details](artifact-descriptions/phase-a--architecture-vision-artefacts.md) |
| B | Business Capability Map | Provides a hierarchical view of what the enterprise can do (capabilities), independent of organisation, process, or technology. | — | [details](artifact-descriptions/phase-b--business-architecture-artefacts.md) |
| B | Business Process Catalogue | An inventory of the business processes in scope. | — | [details](artifact-descriptions/phase-b--business-architecture-artefacts.md) |
| B | Organisation Map | Shows the organisational structure of the enterprise as relevant to the architecture. | — | [details](artifact-descriptions/phase-b--business-architecture-artefacts.md) |
| C | Application Portfolio Catalogue | A complete inventory of the application systems in scope. | — | [details](artifact-descriptions/phase-c--information-systems-architecture-artefacts.md) |
| C | Logical Data Model | Documents the enterprise's key data entities, their attributes, and relationships. | — | [details](artifact-descriptions/phase-c--information-systems-architecture-artefacts.md) |
| C | Data Flow Diagram | Shows how data moves between systems, processes, and actors. | — | [details](artifact-descriptions/phase-c--information-systems-architecture-artefacts.md) |
| D | Technology Standards Catalogue | Documents the approved technology standards, products, and versions that all architecture must conform to. | — | [details](artifact-descriptions/phase-d--technology-architecture-artefacts.md) |
| D | Environments and Locations Diagram | Shows the physical and logical deployment topology of the architecture. | — | [details](artifact-descriptions/phase-d--technology-architecture-artefacts.md) |
| E/F | Consolidated Gap Analysis | Aggregates and reconciles the domain-level gap analyses produced in Phases B, C-Data, C-App, and D. | `consolidated-gap-analysis.md` — `/ea-artifact create consolidated-gap-analysis` | [details](artifact-descriptions/phase-e--f--roadmap-and-transition-artefacts.md) |
| E/F | Transition Architectures | Defines the intermediate architecture states between the Baseline and Target Architectures. | `transition-architectures.md` — `/ea-artifact create transition-architectures` | [details](artifact-descriptions/phase-e--f--roadmap-and-transition-artefacts.md) |
| E/F | Architecture Roadmap | A sequenced, prioritised plan that shows how the architecture will evolve from its baseline to its target state. | — | [details](artifact-descriptions/phase-e--f--roadmap-and-transition-artefacts.md) |
| E/F | Motivation Registers | Six dedicated Phase-A registers — Drivers, Goals, Objectives, Strategy, Issues, Problems. | — | [details](artifact-descriptions/phase-e--f--roadmap-and-transition-artefacts.md) |
| E/F | Risk Register | A cross-cutting artifact that aggregates and tracks all architecture risks across the engagement. | — | [details](artifact-descriptions/phase-e--f--roadmap-and-transition-artefacts.md) |
| G | Architecture Compliance Assessment | A formal review of a project's deliverables or a solution design against the approved architecture. | — | [details](artifact-descriptions/phase-g--governance-artefacts.md) |
| G | Implementation Governance Plan | Translates the Architecture Governance Framework into a concrete, engagement-specific operating plan. | `implementation-governance-plan.md` — `/ea-artifact create implementation-governance-plan` | [details](artifact-descriptions/phase-g--governance-artefacts.md) |
| G | Architecture Requirements Specification | The definitive, consolidated specification of all architecture requirements for the engagement. | — | [details](artifact-descriptions/phase-g--governance-artefacts.md) |
| H | Architecture Change Request | A formal request to deviate from, or update, the agreed target architecture. | `change-request.md` — `/ea-artifact create change-request` | [details](artifact-descriptions/phase-h--architecture-change-management-artefacts.md) |
| H | Change Register | Aggregates all Architecture Change Request artifacts for the engagement into a single governance view. | `change-register.md` — generated by `/ea-changes` | [details](artifact-descriptions/phase-h--architecture-change-management-artefacts.md) |
| Cross-cutting | Zachman Diagram | A cross-cutting classification artifact that maps the engagement's architecture content against the Zachman framework. | `zachman-diagram.md` — `/ea-zachman` | [details](artifact-descriptions/cross-cutting-classification-and-decision-artefacts.md) |
| Cross-cutting ADR | Architecture Decision Record (ADR) | A standalone document capturing a significant architecture decision. | `architecture-decision-record.md` — `/ea-adrs new` | [details](artifact-descriptions/cross-cutting-architecture-decision-artefacts.md) |
| Cross-cutting ADR | ADR Register | Cross-cutting aggregate artifact listing all Architecture Decision Records for the engagement. | `adr-register.md` — generated by `/ea-adrs generate` | [details](artifact-descriptions/cross-cutting-architecture-decision-artefacts.md) |

---

Cross-cutting artifacts are also documented in the per-phase files linked in the table above.
