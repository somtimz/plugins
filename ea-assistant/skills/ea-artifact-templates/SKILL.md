---
name: ea-artifact-templates
description: This skill should be used when the user asks to "create an artifact", "generate the architecture vision", "start a new artifact from a template", "what template should I use", "populate this artifact", or when any TOGAF artifact needs to be created or populated. Provides template selection, placeholder conventions, and guidance text marking standards for all EA artifacts.
version: 0.9.86
---

# EA Artifact Templates

All EA artifacts are created from templates stored in the plugin's `templates/` directory. Templates use a consistent structure with clearly marked guidance, placeholder tokens, and answer state markers.

## Template Organisation

Templates are filed into ADM-phase subfolders that mirror the engagement `artifacts/` layout: `templates/{preliminary,phase-a,phase-b,phase-c-data,phase-c-app,phase-d,phase-e,phase-f,phase-g,phase-h,requirements}/`. Multi-phase and `phase: All` templates live in `templates/cross-cutting/` and are governed by their `admPhases` tag; `templates/seeds/` holds engagement scaffolding (not artifacts). Look up templates by globbing recursively (`templates/**/*.md`). The source subfolder is organisational only — an artifact's **storage** folder is always derived from the template's `phase:` value (see the Phase Folder Mapping in `commands/ea-artifact.md`).

Every template also carries two classification tags in its `taxonomy:` block: `admPhases` (the ADM phase(s) it applies to) and `zachmanCell` (optional best-effort primary Zachman cell, e.g. `Scope/Why`; blank where ambiguous — cell vocabulary in `skills/zachman-framework/references/zachman-cell-descriptions.md`).

## Artifact Taxonomy

Every artifact template includes a `taxonomy:` block in its YAML frontmatter. Use `references/taxonomy.md` as the canonical reference for all valid values and assignment rules.

```yaml
taxonomy:
  admPhases: [A]               # one or more of Preliminary|Requirements|A|B|C-Data|C-App|D|E|F|G|H
  zachmanCell: "Scope/Why"     # optional best-effort primary Zachman cell; "" where ambiguous
  domain: Cross-cutting        # Business | Data | Application | Technology | Cross-cutting
  category: Strategy           # Strategy | Analysis | Design | Planning | Governance | Register
  audience: Executive          # Executive | Business | Architecture | Delivery | Governance | All
  layer: Motivation            # Motivation | Baseline | Target | Transition | Governance | Reference
  sensitivity: Internal        # Internal | Confidential | Restricted
  tags: [vision, goals, phase-a]
```

When creating a non-standard artifact, assign taxonomy values using `references/taxonomy.md`. The `taxonomy` block is a T1-10 compliance requirement — all artifacts must have it.

---

## Template Conventions

### Placeholder Tokens

All unfilled fields use double-brace tokens:
```
{{field_name}}          — simple value
{{stakeholder_name}}    — named entity
{{YYYY-MM-DD}}          — date-only field (startDate, decisionDate, file names)
{{YYYY-MM-DDTHH:MM:SSZ}} — timestamp field (lastModified, createdAt, lastUpdated)
{{artifact_ref}}        — reference to another artifact
```

### Internal Links

Internal links (detail files, cross-artifact, diagrams, uploads, research) follow the engagement's `linkStyle` — `wikilink` (Obsidian `[[..]]`, default for new engagements) or `markdown` (relative paths). Templates ship with wikilink-form example rows. Full rules, both-style table, parsing and export handling: `references/link-conventions.md`; do not restate inline.

### Guidance Text

Guidance explaining what a section means is marked with HTML comments so it is invisible in rendered output but visible in source:

```markdown
<!-- GUIDANCE:
  Describe the high-level intent and scope of this section.
  This text is for the author and should NOT appear in the final deliverable.
  Remove or leave as-is — it will not render in Word or HTML exports.
-->
```

### Answer State Markers

| State | Marker |
|---|---|
| Answered | Value written directly |
| Not answered | `⚠️ Not answered` |
| Not applicable | `➖ Not applicable` |
| Opted out | `⊘ Opted out` or `⊘ Opted out — {reason}` |
| AI-suggested draft | `> 🤖 **AI Draft — Review Required**` blockquote |
| Default accepted | value + ` ✓ Default accepted` |
| Source document | value + ` 📎 Source: uploads/{filename}` |

**Opted out vs. Not answered:** `⊘ Opted out` is an explicit, deliberate choice — the user decided this question or artifact is out of scope for their needs. The reason is recorded in `engagement.json` under `optOuts[]` and surfaced in status reports. `⚠️ Not answered` is a temporary skip — the field may still be filled in later.

### Governance State Markers (Appendix A3 — Decision Log)

Used exclusively in Appendix A3 decision rows to track the governance state of each decision:

| State | Marker | Meaning |
|---|---|---|
| Provisional | `🔄 Provisional` | Recorded but not yet reviewed or owned |
| Awaiting Verification | `⏳ Awaiting Verification` | Assigned to an owner; pending their confirmation |
| Verified | `✓ Verified` | Owner has confirmed the decision is correct |
| Under Vote | `🗳️ Under Vote` | Submitted to stakeholders for a formal vote |
| Voted | `✅ Voted` | Decision carried by stakeholder vote |
| Fiat | `👑 Fiat` | Decided by a senior decision maker without vote |
| Returned | `↩️ Returned` | Sent back for rework by approver or facilitator |

### Appendix Schema — A3 Decision Log

Every artifact that supports a Decision Log uses this standard table in `## Appendix A3 — Decision Log`:

```markdown
### Appendix A3 — Decision Log

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| {{item}} | {{value}} | 🔄 Provisional | {{facilitator}} | {{owner}} | Strategic / Tactical / Operational | Business / Data / Application / Technology / Cross | High / Med / Low / TBD | High / Med / Low / TBD | High / Med / Low / TBD | {{subject_tag}} | {{date}} |
```

**Field definitions:**

| Field | Values | Meaning |
|---|---|---|
| **Authority** | Strategic / Tactical / Operational | Strategic = enterprise-wide long-term commitment; Tactical = engagement-scoped medium-term; Operational = implementation detail short-term |
| **Domain** | Business / Data / Application / Technology / Cross | Which architecture domain this decision primarily affects |
| **Cost** | High / Med / Low / TBD | Resource or time commitment required to execute this decision |
| **Impact** | High / Med / Low / TBD | Business or architecture impact if this decision stands or changes |
| **Risk** | High / Med / Low / TBD | Risk of making this decision incorrectly or reversing it later |
| **Subject** | Free text | Short tag (e.g. "Cloud strategy", "Data governance", "API design") for topic-based filtering |

A3 rows are the source data for `/ea-decisions`.

### A3.N Decision Rationale Blocks

Each A3 decision row may have an accompanying rationale block written directly below the A3 table. These blocks capture the reasoning behind a decision and are expected for all Strategic-authority decisions.

**Format:** One block per decision, anchored by the `Item` field value (case-insensitive match):

```markdown
#### A3.N — {Item value}
- **Rationale:** Why this decision was made
- **Alternatives:** Other options considered and why they were rejected
- **Tradeoffs accepted:** What was sacrificed by choosing this option
- **Implications:** Downstream effects to monitor or act on
```

**Rules:**
- All four fields are optional — a partial block with only Rationale or Tradeoffs is valid; omit empty bullet lines
- Anchor header must be exactly `#### A3.N — {Item}` with the Item value matching the A3 row (case-insensitive)
- When a user explicitly skips rationale capture, write a sentinel block instead of a full block:
  ```
  #### A3.N — {Item value}
  *(rationale not captured)*
  ```
- Sentinel blocks are excluded from `/ea-decisions` Decision Detail output and from the T3-RATIONALE compliance warning
- All A3.N blocks for a given artifact are written below the A3 table, before the next `##`-level heading

**Created by:** `/ea-interview` (immediately after `a: {text}` capture); `/ea-decisions rationale` (catch-up pass for existing A3 entries)
**Consumed by:** `/ea-decisions generate` (Decision Detail section); compliance rule T3-RATIONALE

### Appendix Schema — A4 Stakeholder Concerns & Objections

Every primary artifact (Architecture Vision, all domain architectures, Gap Analysis, Architecture Roadmap, Statement of Architecture Work, and Migration Plan) includes this appendix in `## Appendix A4 — Stakeholder Concerns & Objections`:

```markdown
### Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |
```

**Field definitions:**

| Field | Values | Meaning |
|---|---|---|
| **ID** | CON-NNN | Concern identifier — sequential within the engagement across all artifacts |
| **Concern** | Free text | The objection, question, or challenge as it was raised — verbatim where possible |
| **Raised By** | Free text | Source: stakeholder name/role (e.g. "CIO"), "grill-me-boardroom", "Architecture Review Board", "Sponsor workshop", etc. |
| **Category** | Scope / Goal / Approach / Feasibility / Risk / Stakeholder / Other | The type of concern |
| **Status** | Addressed / Partially Addressed / Requires Attention | Whether the concern has been resolved |
| **Response** | Free text or artifact/section reference | Where in this artifact (or another) the concern is answered (e.g. "§3 Goals — G-001 scoped to exclude retail domain"). Leave blank if Requires Attention |
| **Action / Owner** | Free text | What needs to happen and who is responsible — only for Requires Attention items. Leave `—` for Addressed items |

**Status rules:**
- **Addressed** — a clear, documented response exists; record where. Set `Action / Owner` to `—`
- **Partially Addressed** — a response exists but with acknowledged gaps; note both the response and remaining gap
- **Requires Attention** — no adequate response exists; must have an Action and Owner. These rows are flagged by `/ea-concerns` and may be escalated to the Risk Register as RIS-NNN entries

A4 rows are the source data for `/ea-concerns`.

### Review State Header

Every artifact includes a status block at the top:

```markdown
---
artifact: Architecture Vision
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.9.86
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
---
```

## Artifact Catalogue

Artifact depth (section detail, length, governance formality) is calibrated to the engagement's `architectureLevel`. At the start of any artifact creation or population session, load `skills/ea-engagement-lifecycle/references/landscape-levels.md` and apply the Depth Expectation Matrix:
- **Strategic** — full population of all sections; all governance appendices (A3, A4, A5) required; all A3 Strategic-authority decisions require A3.N rationale blocks
- **Segment** — full population; same governance requirements as Strategic
- **Capability** — key sections; A3/A4/A5 required; abbreviated sections noted in the matrix
- **Solution** — key sections; A3/A4/A5 required; may abbreviate governance appendices as noted

All TOGAF artifacts are in scope. Templates are stored in the plugin's `templates/` directory:

| Template File | Artifact | ADM Phase |
|---|---|---|
| `engagement-charter.md` | Engagement Charter | Prelim |
| `governance-framework.md` | Governance Framework | Prelim |
| `architecture-principles.md` | Architecture Principles | Prelim / A |
| `stakeholder-map.md` | Stakeholder Map | Prelim / A |
| `architecture-vision.md` | Architecture Vision | A |
| `statement-of-architecture-work.md` | Statement of Architecture Work | A |
| `target-state-declaration.md` | Target State Declaration | A |
| `communications-plan.md` | Communications Plan | A |
| `architecture-definition-document.md` | Architecture Definition Document | A (skeleton) → F (final) |
| `business-model-canvas.md` | Business Model Canvas | B |
| `business-architecture.md` | Business Architecture | B |
| `data-architecture.md` | Data/Information Architecture | C |
| `application-architecture.md` | Application Architecture | C |
| `technology-architecture.md` | Technology Architecture | D |
| `gap-analysis.md` | Gap Analysis (domain) | B, C-Data, C-App, D |
| `consolidated-gap-analysis.md` | Consolidated Gap Analysis | E |
| `transition-architectures.md` | Transition Architectures | E / F |
| `architecture-roadmap.md` | Architecture Roadmap | E / F |
| `migration-plan.md` | Migration Plan | F |
| `implementation-governance-plan.md` | Implementation Governance Plan | G |
| `architecture-contract.md` | Architecture Contract | G |
| `compliance-assessment.md` | Compliance Assessment | G |
| `change-request.md` | Architecture Change Request | H |
| `change-register.md` | Change Register | H (generated by /ea-changes) |
| `requirements-register.md` | Architecture Requirements Register | Requirements |
| `traceability-matrix.md` | Requirements Traceability Matrix | Requirements |
| `architecture-decision-record.md` | Architecture Decision Record | All phases |
| `stakeholder-action-plan.md` | Stakeholder Action Plan | cross-cutting/governance/ (generated by /ea-actions) |
| `adr-register.md` | ADR Register | cross-cutting/governance/ (generated by /ea-adrs) |
| `abb-register.md` | ABB Register | C / D (generated by /ea-abbs) |
| `sbb-register.md` | SBB Register | D (generated by /ea-sbbs) |
| `story-register.md` | Story Register | E / F (generated by /ea-stories) |
| `risk-register.md` | Risk Register | cross-cutting/operations/ (generated by /ea-risks) |
| `zachman-diagram.md` | Zachman Diagram | cross-cutting/context/ (generated by /ea-zachman) |
| `decision-register.md` | Decision Register | cross-cutting/governance/ (generated by /ea-decisions) |
| `consolidated-report.md` | Consolidated Architecture Report | All phases |
| `workshop-minutes.md` | Workshop Minutes | All phases (generated by /ea-workshop) |
| `arb-minutes.md` | ARB Meeting Minutes | All phases (generated by /ea-arb) |
| `cross-cutting-index.md` | Cross-cutting Index | artifacts/cross-cutting/ (navigation hub, auto-updated) |

## Creating an Artifact

1. Identify the artifact type and its template file
2. Copy the template to `EA-projects/{slug}/artifacts/{phase-folder}/{artifact-id}.md` — derive `{phase-folder}` from the Phase Folder Mapping table in `ea-artifact.md`
3. Pre-populate fields with any available data from:
   - `engagement.json` (name, sponsor, organisation)
   - Requirements register (relevant requirements)
   - Uploaded documents (via `ea-document-ingestion`)
   - Previous interview notes
4. Leave unpopulated fields as `{{field_name}}` placeholders
5. Add the artifact entry to `engagement.json` under `artifacts[]`
6. Do NOT fill placeholder sections with AI-generated content unless clearly marked as a draft

## Interview-Driven Population

When populating an artifact via interview:
1. Extract the questions from the template (fields marked `{{...}}`)
2. Load them into the `ea-interviewer` agent
3. For each question, offer:
   - A default answer where one is reasonable (clearly marked)
   - Option to skip (`⚠️ Not answered`)
   - Option to mark N/A (`➖ Not applicable`)
4. Write confirmed answers directly into the artifact
5. Save dated interview notes to `interviews/`

## Guidance Text Policy

Guidance text in templates serves two purposes:
1. **Authoring guide** — explains what the section should contain
2. **Quality check** — reminds the author of TOGAF standards

Guidance text is ALWAYS wrapped in `<!-- GUIDANCE: ... -->` HTML comments.
It must NEVER be removed automatically — the author decides whether to keep or remove it.
It does NOT appear in Word or HTML exports (HTML comments are not rendered).

## Readability Guidelines

Apply these rules when creating, populating, or reviewing artifact content:

- **Tables are for summary/index only.** Keep tables to ≤ 8 columns. If a table would need more than 8 columns to capture all relevant fields, move the overflow to a detail file (see below).
- **Narrative before tables.** Every table-heavy section should be preceded by 1–3 sentences of prose that summarise what the reader is about to see — the top finding, the dominant pattern, or the key implication. Avoid leading with a table and no context.
- **Split large tables.** For sections with more than 10 rows, split by a natural dimension (e.g. High / Medium / Low priority, In Scope / Out of Scope, Business / Technical) to aid scanning.
- **Avoid redundant columns.** Do not repeat information that is already expressed by the ID, the section heading, or the row label. Each column should add unique information.
- **Detail on demand.** For items that require extended narrative, rationale, risks, costs, issues, concerns, impact, or alternatives, link to a detail file rather than expanding the table inline.

## Item Detail Files

Table rows in EA artifacts may optionally link to a companion detail file containing extended content. This keeps tables scannable while providing depth on demand.

**Convention:**
- Detail files live at `artifacts/details/{ID}.md` — one engagement-wide directory
- Link from table: add a `Details` column with `[→](../details/{ID}.md)` when a detail file exists, or `—` when it does not
- Create with: `/ea-detail new {ID} [{artifact-id}]`
- Full convention: `references/detail-file-convention.md`

**When to create a detail file:**
- Item was contested, challenged in a grill, or raised stakeholder concerns
- Item has non-trivial cost, risk, or dependency implications
- Stakeholder asks "why?" or "what about X?" about a specific row
- Item has alternatives that were considered but rejected

**Context loading:** Skills that use Scope A (ea-grill, ea-review, ea-interview) automatically load linked detail files and cite them as `[detail: {ID}]`. See `skills/ea-engagement-lifecycle/references/context-loading.md`.

## Additional Resources

- **`references/artifact-descriptions.md`** — Purpose, audience, and contents of each TOGAF artifact
- **`references/template-authoring-guide.md`** — How to write and extend templates
- **`references/ea-concepts.md`** — Canonical definitions and TOGAF/ArchiMate alignment for Principle, Goal, Objective, Strategy, Plan, and Risk. Load this when concept confusion is detected during interviews or artifact population.
- **`references/compliance-check.md`** — Compliance rules (Tier 1/2/3), check procedure, remediation actions for Option 1 (achieve compliance) and Option 2 (accept as-is with defaults). Load this whenever an artifact is opened for interview, review, or viewing.
- **`references/detail-file-convention.md`** — Detail file pattern: location, frontmatter, sections, linking rules, and how skills load and cite detail files.
- **`references/link-conventions.md`** — Internal link styles: the `linkStyle` setting (wikilink | markdown), link forms per target, wikilink rules, parsing rule (recognise both forms), and export resolution for `/ea-generate` and `/ea-publish`.
