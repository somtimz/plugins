# Reference Architecture Schema

A reference architecture is a **governed, reusable blueprint** for a class of solutions — see the **Reference Architecture (RA-NNN)** concept in `skills/ea-artifact-templates/references/ea-concepts.md` for the definition, boundary conditions, failure modes, and stress test. This file defines the entry's structure; the authored template is `templates/seeds/ra-entry-template.md` (guidance-driven, so RAs are interview-able / scorable / grillable).

## RA-NNN Entry Frontmatter

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `RA-NNN` (3-digit zero-padded) | Allocated from `repo.json → referenceArchitecture.nextId` (repo-level) or `engagement.json → localRA.nextId` (local) |
| `name` | string | any | Short descriptive name of the pattern |
| `domain` | enum | `Business \| Data \| Application \| Technology \| Cross-cutting` | Primary architecture domain |
| `status` | enum | `Draft \| Approved \| Deprecated` | Lifecycle state |
| `version` | string | semver `MAJOR.MINOR.PATCH` | Start at `1.0.0` |
| `source` | enum | `internal \| industry` | `industry` = derived from a named standard or body (e.g. BIAN, AWS WAF, Azure CAF) |
| `industryBody` | string | any | If `source: industry`, name the issuing body (e.g. "BIAN", "AWS") |
| `linkedCAPs` | array | `CAP-NNN` strings | Business capabilities this RA serves (capability→technology traceability) |
| `linkedSTDs` | array | `STD-NNN` strings | Standards this RA is derived from or aligns to |
| `linkedADRs` | array | `ADR-NNN` strings | ADRs ratified against this RA (populated during engagement adoption) |
| `linkedSBBs` | array | `SBB-NNN` strings | Approved solution building blocks referenced by this RA (technology-neutral RA still references approved products) |
| `reviewCadence` | string | any | How often the RA is reviewed/versioned (RAs age quickly and need active lifecycle management) |
| `createdDate` | ISO date | `YYYY-MM-DD` | |
| `lastModified` | ISO date | `YYYY-MM-DD` | Updated on every edit |

## Markdown Sections

Each section carries a `<details>📋 Guidance</details>` block. Required sections must be populated for an RA to have governance value; the boundary sections (Mandatory vs Optional Components, Integration, Security Trust Boundaries, Data Ownership & Sovereignty, Governance Checkpoints) are what separate a governed RA from "architecture by PowerPoint".

| Section | Required | Content |
|---|---|---|
| `## Overview` | yes | 1–3 paragraphs: the solution class it governs and the consistency goal |
| `## Scope & Domain` | yes | In-scope / out-of-scope boundary of the solution class |
| `## Capability Alignment` | yes | Table: CAP-NNN \| Capability \| How this RA enables it |
| `## Architecture Layers` | yes | Logical service decomposition. Table: Layer \| ABB-NNN \| ABB Name \| Role in Pattern |
| `## Mandatory vs Optional Components` | yes | Table: Component (ABB-NNN) \| Mandatory/Optional \| Conformance note |
| `## Integration Patterns & Mechanisms` | yes | Table: Interaction \| Approved pattern/mechanism \| Mandatory? |
| `## Information Flows` | no | Table: Flow \| From \| To \| Mechanism \| Notes |
| `## Security Architecture & Trust Boundaries` | yes | Table: Trust boundary \| Crossing \| Required control/pattern |
| `## Data Ownership & Sovereignty` | yes | Table: Data domain \| Authoritative source \| Ownership boundary \| Residency requirement |
| `## Technology Standards` | yes | Table: STD-NNN \| Standard \| Mandatory? (technology-neutral) |
| `## Non-Functional Requirements` | no | Table: NFR category \| Target/envelope \| Conformance check |
| `## Key Decisions` | yes | Table: Decision \| Rationale Summary \| Candidate ADR Title |
| `## Constraints` | yes | Table: Description \| Candidate CST Title \| Flexibility (Mandatory \| Recommended) |
| `## Implied Principles` | yes | Bullet list of BP/DP/AP/TP IDs or free-text principle statements |
| `## Governance Checkpoints & Conformance` | yes | Table: Checkpoint \| Measurable conformance criterion \| Checked at (phase) + adoption metric |
| `## Operational Responsibilities` | no | Table: Component/service \| Operated by \| Consumed as shared service? |
| `## Adoption Notes` | yes | What is mandatory vs. flexible; known adaptations |
| `## Stress Test` | no | The three-teams consistency-vs-freedom verdict |
| `## Grill Checklist` | yes | Numbered testable statements used by `/ea-grill` when this RA is adopted |

### Grill Checklist format

Each item is a single testable statement in present tense, e.g.:

```
1. All inter-service communication uses the event bus — no direct synchronous DB calls across service boundaries.
2. Each service owns exactly one bounded context — no shared schema between services.
3. Events are named in past tense (OrderPlaced, PaymentReceived) — no imperative commands (ProcessOrder).
```

The grill check passes if the engagement's artifacts are consistent with the statement; it fails (and is reported as a finding) if they contradict it or cannot be verified.

## Scope Labels

`(local)` — displayed in list output when the RA lives in `artifacts/cross-cutting/reference-architectures/` rather than the Architecture Repository. Local RAs are scoped to one engagement and are not shared. If a local and repo RA share the same ID, `/ea-refarch show` resolves the repo entry first; use `/ea-refarch show RA-NNN --local` to force local resolution.

## Storage Paths

| Scope | Path |
|---|---|
| Repo-level | `Architecture-Repository/reference-library/entries/RA-NNN.md` |
| Per-engagement | `artifacts/cross-cutting/reference-architectures/RA-NNN.md` |
| Repo index | `Architecture-Repository/reference-library/reference-architecture-index.md` |
| Engagement index | `artifacts/cross-cutting/reference-architectures/reference-architecture-index.md` |
