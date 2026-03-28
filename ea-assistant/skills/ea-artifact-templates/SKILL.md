---
name: EA Artifact Templates
description: This skill should be used when the user asks to "create an artifact", "generate the architecture vision", "start a new artifact from a template", "what template should I use", "populate this artifact", or when any TOGAF artifact needs to be created or populated. Provides template selection, placeholder conventions, and guidance text marking standards for all EA artifacts.
version: 0.2.0
---

# EA Artifact Templates

All EA artifacts are created from templates stored in the plugin's `templates/` directory. Templates use a consistent structure with clearly marked guidance, placeholder tokens, and answer state markers.

## Template Conventions

### Placeholder Tokens

All unfilled fields use double-brace tokens:
```
{{field_name}}          — simple value
{{stakeholder_name}}    — named entity
{{YYYY-MM-DD}}          — date field
{{artifact_ref}}        — reference to another artifact
```

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
version: 0.1
lastModified: {{YYYY-MM-DD}}
---
```

## Artifact Catalogue

All TOGAF artifacts are in scope. Templates are stored in the plugin's `templates/` directory:

| Template File | Artifact | ADM Phase |
|---|---|---|
| `architecture-vision.md` | Architecture Vision | A |
| `statement-of-architecture-work.md` | Statement of Architecture Work | A |
| `architecture-principles.md` | Architecture Principles | Prelim / A |
| `stakeholder-map.md` | Stakeholder Map | Prelim / A |
| `business-model-canvas.md` | Business Model Canvas | B |
| `business-architecture.md` | Business Architecture | B |
| `data-architecture.md` | Data/Information Architecture | C |
| `application-architecture.md` | Application Architecture | C |
| `technology-architecture.md` | Technology Architecture | D |
| `gap-analysis.md` | Gap Analysis | B–D |
| `architecture-roadmap.md` | Architecture Roadmap | E / F |
| `migration-plan.md` | Migration Plan | F |
| `architecture-contract.md` | Architecture Contract | G |
| `compliance-assessment.md` | Compliance Assessment | G |
| `change-request.md` | Architecture Change Request | H |
| `requirements-register.md` | Architecture Requirements Register | Requirements |
| `traceability-matrix.md` | Requirements Traceability Matrix | Requirements |
| `decision-register.md` | Decision Register | All phases |
| `consolidated-report.md` | Consolidated Architecture Report | All phases |

## Creating an Artifact

1. Identify the artifact type and its template file
2. Copy the template to `EA-projects/{slug}/artifacts/{artifact-id}.md`
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

## Additional Resources

- **`references/artifact-descriptions.md`** — Purpose, audience, and contents of each TOGAF artifact
- **`references/template-authoring-guide.md`** — How to write and extend templates
- **`references/ea-concepts.md`** — Canonical definitions and TOGAF/ArchiMate alignment for Principle, Goal, Objective, Strategy, Plan, and Risk. Load this when concept confusion is detected during interviews or artifact population.
- **`references/compliance-check.md`** — Compliance rules (Tier 1/2/3), check procedure, remediation actions for Option 1 (achieve compliance) and Option 2 (accept as-is with defaults). Load this whenever an artifact is opened for interview, review, or viewing.
