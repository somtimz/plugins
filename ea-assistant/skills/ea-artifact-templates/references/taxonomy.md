# EA Artifact Taxonomy — Reference

Every EA artifact template includes a `taxonomy:` block in its YAML frontmatter. This reference defines all valid values for each dimension and the rules for assigning them.

---

## Frontmatter Schema

```yaml
taxonomy:
  domain: Cross-cutting          # Architecture domain
  category: Strategy             # Functional category
  audience: Executive            # Primary reader
  layer: Motivation              # Architectural layer
  sensitivity: Internal          # Information classification
  tags: [vision, goals, phase-a] # Free-form searchable keywords
```

All six fields are required on every artifact. Tags are a list of 3–6 lowercase kebab-case keywords.

---

## Dimension Definitions

### `domain` — Architecture Domain

Which architecture domain this artifact primarily covers.

| Value | Definition |
|---|---|
| `Business` | Business processes, capabilities, organisation structure, operating model |
| `Data` | Information architecture, data models, data flows, data governance |
| `Application` | Application portfolio, system integrations, APIs, software capabilities |
| `Technology` | Infrastructure, platforms, networks, cloud, security, operations |
| `Cross-cutting` | Spans multiple domains, or applies to the engagement as a whole |

**Rule:** Use `Cross-cutting` whenever an artifact addresses concerns across two or more domains, or when it is engagement-wide (e.g., Architecture Vision, Roadmap, Governance artifacts).

---

### `category` — Functional Category

What the artifact *does* in the EA process.

| Value | Definition | Examples |
|---|---|---|
| `Strategy` | Sets direction — defines why and what at the highest level | Architecture Vision, Architecture Principles, Governance Framework, Business Model Canvas |
| `Analysis` | Assesses current state, requirements, or stakeholder landscape | Gap Analysis, Requirements Register, Stakeholder Map, Traceability Matrix |
| `Design` | Defines the target architecture in a specific domain | Business Architecture, Data Architecture, Application Architecture, Technology Architecture |
| `Planning` | Coordinates delivery — sequences work and manages transitions | Architecture Roadmap, Migration Plan, Statement of Architecture Work, Consolidated Report |
| `Governance` | Controls conformance, change, and decision-making | Compliance Assessment, Architecture Contract, Implementation Governance Plan, Change Request |
| `Register` | Aggregated cross-artifact views — generated on demand | Decision Register, Risk Register, Change Register |

---

### `audience` — Primary Audience

Who primarily reads and acts on this artifact.

| Value | Definition |
|---|---|
| `Executive` | C-suite, board members, programme sponsors, business leadership |
| `Business` | Business owners, process owners, subject matter experts, product owners |
| `Architecture` | Enterprise architects, domain architects, solution architects, ARB members |
| `Delivery` | Project managers, developers, testers, delivery leads, integration teams |
| `Governance` | Architecture Review Board, risk officers, compliance teams, audit |
| `All` | Consumed meaningfully by multiple distinct audiences (e.g., Requirements Register) |

**Rule:** Choose the *primary* audience — who will act on this artifact most directly. A document read by executives but authored for architects is `Architecture`.

---

### `layer` — Architectural Layer

Which architectural layer the artifact primarily operates at. Based on TOGAF's motivation, baseline, target, and transition layers.

| Value | Definition |
|---|---|
| `Motivation` | Captures *why*: business drivers, goals, objectives, strategies, issues, problems |
| `Baseline` | Documents the *as-is* current state architecture |
| `Target` | Defines the *to-be* future state architecture |
| `Transition` | Bridges baseline to target: gaps, roadmaps, migration plans |
| `Governance` | Controls the architecture process: decisions, risks, compliance, contracts, changes |
| `Reference` | Cross-cutting reference material: principles, traceability, stakeholder maps |

---

### `sensitivity` — Information Classification

Controls who outside the EA team can access the artifact.

| Value | Definition | Handling |
|---|---|---|
| `Internal` | Standard internal document — appropriate for all staff | Default; no special handling |
| `Confidential` | Contains sensitive business, stakeholder, or commercial information — restricted to named stakeholders | Label clearly; limit distribution |
| `Restricted` | Highest sensitivity — board-level, regulatory, or personal data | Named-individual access only; do not export without approval |

**Default:** `Internal`. Upgrade to `Confidential` when the artifact contains:
- Named individual stakeholder assessments (Stakeholder Map)
- Commercial sensitivities (Business Model Canvas, Statement of Architecture Work)
- Contractual obligations (Architecture Contract, Change Request)
- Risk or vulnerability details (Risk Register)

---

### `tags` — Searchable Keywords

Free-form list of 3–6 lowercase kebab-case keywords. Tags should include:
- The primary ADM phase (`phase-a`, `phase-b`, `phase-g`, `preliminary`, `cross-cutting`)
- 2–4 content keywords drawn from the artifact's major sections

**Convention:**
- Use kebab-case: `data-model` not `data model` or `dataModel`
- Include the phase tag: `phase-a`, `phase-b`, `phase-c`, ..., `phase-h`, `preliminary`
- For cross-cutting registers: use `cross-cutting` as the phase tag

---

## Canonical Taxonomy Map

| Template | domain | category | audience | layer | sensitivity |
|---|---|---|---|---|---|
| architecture-vision | Cross-cutting | Strategy | Executive | Motivation | Internal |
| architecture-principles | Cross-cutting | Strategy | Architecture | Reference | Internal |
| governance-framework | Cross-cutting | Strategy | Governance | Governance | Internal |
| business-model-canvas | Business | Strategy | Executive | Motivation | Confidential |
| statement-of-architecture-work | Cross-cutting | Planning | Governance | Governance | Confidential |
| stakeholder-map | Cross-cutting | Analysis | Architecture | Reference | Confidential |
| requirements-register | Cross-cutting | Analysis | All | Reference | Internal |
| gap-analysis | Cross-cutting | Analysis | Architecture | Transition | Internal |
| traceability-matrix | Cross-cutting | Analysis | Architecture | Reference | Internal |
| business-architecture | Business | Design | Business | Target | Internal |
| data-architecture | Data | Design | Architecture | Target | Internal |
| application-architecture | Application | Design | Architecture | Target | Internal |
| technology-architecture | Technology | Design | Architecture | Target | Internal |
| architecture-roadmap | Cross-cutting | Planning | All | Transition | Internal |
| migration-plan | Cross-cutting | Planning | Delivery | Transition | Internal |
| consolidated-report | Cross-cutting | Planning | Executive | Reference | Internal |
| architecture-contract | Cross-cutting | Governance | Governance | Governance | Confidential |
| compliance-assessment | Cross-cutting | Governance | Governance | Governance | Internal |
| implementation-governance-plan | Cross-cutting | Governance | Governance | Governance | Internal |
| change-request | Cross-cutting | Governance | Governance | Governance | Confidential |
| decision-register | Cross-cutting | Register | Governance | Governance | Internal |
| risk-register | Cross-cutting | Register | Governance | Governance | Confidential |
| change-register | Cross-cutting | Register | Governance | Governance | Internal |
| adr-register | Cross-cutting | Register | Governance | Governance | Internal |
| architecture-decision-record | Cross-cutting | Governance | Architecture | Governance | Internal |
| zachman-diagram | Cross-cutting | Analysis | Architecture | Reference | Internal |
| engagement-charter | Cross-cutting | Strategy | Executive | Motivation | Confidential |

---

## Using the Taxonomy

**In `/ea-artifact list`:** group and filter by `category`, `domain`, or `audience`.

**In `/ea-engage-review`:** filter artifact inventory by `layer` (e.g. show all `Target` artifacts to check design completeness, or all `Governance` artifacts for governance scan).

**In `/ea-publish`:** flag any artifact with `sensitivity: Confidential` or `Restricted` before export — prompt for distribution list confirmation.

**In `ea-generate.md`:** extract `taxonomy` block into the `meta` JSON alongside other frontmatter fields, so Word/PPTX outputs can include classification headers.

**When creating a non-standard artifact:** assign taxonomy values using this reference. If no existing `category` fits, use the closest match and note the deviation in Appendix A4.
