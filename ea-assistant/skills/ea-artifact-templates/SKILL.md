---
name: EA Artifact Templates
description: This skill should be used when the user asks to "create an artifact", "generate the architecture vision", "start a new artifact from a template", "what template should I use", "populate this artifact", or when any TOGAF artifact needs to be created or populated. Provides template selection, placeholder conventions, and guidance text marking standards for all EA artifacts.
version: 0.1.0
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
| AI-suggested draft | `> 🤖 **AI Draft — Review Required**` blockquote |
| Default accepted | value + ` ✓ Default accepted` |
| Source document | value + ` 📎 Source: uploads/{filename}` |

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
