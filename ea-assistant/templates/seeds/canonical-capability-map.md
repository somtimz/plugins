---
artifact: Canonical Capability Map
artifactId: canonical-capability-map
scope: repository
organisation: "{{organisation}}"
version: 1.0.0
lastModified: {{YYYY-MM-DD}}
---

# Canonical Capability Map — {{organisation}}

<!--
  The authoritative, reference business capability map for the enterprise. Engagements seed their
  Business Architecture capability model from this via `/ea-capabilities adopt`. Keep it
  technology- and organisation-neutral and stable — it is the enterprise's capability *taxonomy*,
  not a project deliverable. Maturity and strategic Supports are assessed per engagement, not here.
  Concept: the Capability Model definition in skills/ea-artifact-templates/references/ea-concepts.md.
-->

## How to use this map

- A capability is an **ability to achieve an outcome**, independent of who/how/what — a noun, not a process.
- IDs are stable canonical ids `CAP-C-NNN`. When an engagement adopts a branch, it allocates fresh engagement `CAP-NNN` ids and records `Source: canonical CAP-C-NNN`.
- The map is **box-in-box / hierarchical, not flow-based** (no arrows — that is a value stream).
- Replace the example domains below with the enterprise's actual L1 domains. Keep it lean — resist capability inflation and duplication.

## Capability Hierarchy

| CAP-C-NNN | Level | Domain | Capability | Value / Outcome | Description |
|---|---|---|---|---|---|
| CAP-C-001 | L1 | Strategy & Governance | Strategy & Governance | Sets direction and ensures the enterprise operates within its risk appetite | Strategic planning, enterprise governance, risk, compliance |
| CAP-C-002 | L2 | Strategy & Governance | Enterprise Architecture | Keeps change coherent and aligned to strategy | Architecture development, standards, conformance |
| CAP-C-010 | L1 | Customer Management | Customer Management | Wins, serves, and retains customers | The full customer relationship |
| CAP-C-011 | L2 | Customer Management | Customer Acquisition | Grows the customer base | Marketing, sales, onboarding |
| CAP-C-012 | L2 | Customer Management | Customer Service & Support | Retains customers by resolving their needs | Support, complaints, service requests |
| CAP-C-013 | L2 | Customer Management | Customer Insight | Improves decisions with customer understanding | Segmentation, analytics, voice-of-customer |
| CAP-C-020 | L1 | Product & Service | Product & Service Management | Brings the right offerings to market | Ideation through lifecycle management |
| CAP-C-021 | L2 | Product & Service | Product Development | Turns ideas into offerings | Design, build, launch |
| CAP-C-030 | L1 | Operations | Operations & Fulfilment | Delivers the product/service reliably | Core value-delivery operations |
| CAP-C-031 | L2 | Operations | Order Management | Converts demand into fulfilled value | Capture → fulfil → settle |
| CAP-C-032 | L2 | Operations | Supply & Logistics | Ensures inputs and delivery flow | Sourcing, inventory, distribution |
| CAP-C-040 | L1 | Finance | Financial Management | Funds, controls, and reports the enterprise | Planning, accounting, treasury |
| CAP-C-050 | L1 | People | Human Capital Management | Has the right people, capable and engaged | Hire, develop, reward, retain |
| CAP-C-060 | L1 | Technology | Information Technology | Provides and runs the digital backbone | Applications, infrastructure, data, security |
| CAP-C-061 | L2 | Technology | Information Security | Protects the enterprise's information assets | Identity, protection, monitoring, response |
| CAP-C-062 | L2 | Technology | Data Management | Makes trusted data available where needed | Governance, quality, master data, analytics platform |

## Coverage & Known Gaps

<!-- A capability map claims a "full enterprise view" but omits informal work, shadow IT, and
     emergent capabilities. Note known gaps here so the map does not give a false sense of completeness. -->

- {{known_gaps_or_None}}
