# Scaffolding Map

This reference defines which artifacts are automatically scaffolded when a new engagement is created via `/ea-new`, and which templates are available per ADM phase. The scaffolding engine uses this map to determine phase applicability and which templates to copy based on the selected engagement type and architecture domains.

---

## Engagement Type to ADM Phase Applicability

Each engagement type determines which ADM phases are applicable. Phases not covered by "Always Applicable" or the selected domains are set to `Not Applicable`.

| Engagement Type | Always Applicable | Domain-Dependent (if selected) | Not Applicable |
|---|---|---|---|
| Greenfield | Prelim, Requirements, A, E, F, G, H | B (Business), C-Data (Data), C-App (Application), D (Technology) | — |
| Brownfield | Prelim, Requirements, A, E, F, G, H | B, C-Data, C-App, D | — |
| Assessment-only | Prelim, Requirements, A | B, C-Data, C-App, D | E, F, G, H |
| Migration | Prelim, Requirements, A, E, F, G, H | B, C-Data, C-App, D | — |

### Domain to Phase Mapping

| Domain | ADM Phase |
|---|---|
| Business | B |
| Data | C-Data |
| Application | C-App |
| Technology | D |

### Phase Applicability Rules

1. Phases in **Always Applicable** are set to `Not Started` regardless of domain selection.
2. For each **selected domain**, set the corresponding phase to `Not Started`.
3. For each **deselected domain**, set the corresponding phase to `Not Applicable`.
4. Phases in **Not Applicable** (by engagement type) are set to `Not Applicable` regardless of domain selection.

---

## Artifact Scaffolding at Engagement Creation

These artifacts are automatically scaffolded when `/ea-new` completes. All are Preliminary phase artifacts.

| Artifact ID | Display Name | Template | Applicable Types | Applicable Domains |
|---|---|---|---|---|
| `architecture-principles` | Architecture Principles | `templates/architecture-principles.md` | All | All |
| `stakeholder-map` | Stakeholder Map | `templates/stakeholder-map.md` | All | All |

### Scaffolding Rules

For each artifact in the table above:

1. **Type check** — If the engagement type is not in Applicable Types, skip.
2. **Domain check** — If Applicable Domains specifies a domain list, skip if none of the listed domains are selected. `All` means scaffold regardless of selection.
3. **Copy template** — Copy the template to `EA-projects/{slug}/artifacts/{artifact-id}.md`.
4. **Replace variables** — Substitute tokens with engagement metadata:
   - `{{engagement_name}}` → engagement name
   - `{{organisation}}` → organisation
   - `{{sponsor}}` → sponsor name
   - `{{YYYY-MM-DD}}` → today's date
5. **Mark unpopulated content** — All sections not pre-populated from metadata MUST be marked `⚠️ Not answered`.
6. **Register artifact** — Add an entry to `artifacts[]` in `engagement.json`:
   ```json
   {
     "id": "{artifact-id}",
     "name": "{display-name}",
     "phase": "Prelim",
     "file": "artifacts/{artifact-id}.md",
     "reviewFile": "artifacts/{artifact-id}.review.md",
     "status": "Draft",
     "createdAt": "{ISO 8601 timestamp}",
     "lastModified": "{ISO 8601 timestamp}",
     "reviewStatus": "Not Reviewed"
   }
   ```
7. **Missing template** — If the template file does not exist, skip, log a warning, and continue. Note the skipped artifact in the creation confirmation.

---

## Full Artifact Catalogue by Phase

All available templates and the phase they belong to. These are not all scaffolded at creation — they are created on demand via `/ea-artifact create` or `/ea-phase` as the engagement progresses.

| Template File | Artifact Name | Phase | Domain | Engagement Types |
|---|---|---|---|---|
| `architecture-principles.md` | Architecture Principles | Prelim | All | All |
| `stakeholder-map.md` | Stakeholder Map | Prelim / A | All | All |
| `statement-of-architecture-work.md` | Statement of Architecture Work | A | All | All |
| `architecture-vision.md` | Architecture Vision | A | All | All |
| `requirements-register.md` | Architecture Requirements Register | Requirements | All | All |
| `traceability-matrix.md` | Requirements Traceability Matrix | Requirements | All | All |
| `business-model-canvas.md` | Business Model Canvas | B | Business | Greenfield, Brownfield, Migration |
| `business-architecture.md` | Business Architecture | B | Business | All |
| `data-architecture.md` | Data / Information Architecture | C-Data | Data | All |
| `application-architecture.md` | Application Architecture | C-App | Application | All |
| `gap-analysis.md` | Gap Analysis | B–D | All | All |
| `technology-architecture.md` | Technology Architecture | D | Technology | All |
| `architecture-roadmap.md` | Architecture Roadmap | E / F | All | Greenfield, Brownfield, Migration |
| `migration-plan.md` | Migration Plan | F | All | Brownfield, Migration |
| `architecture-contract.md` | Architecture Contract | G | All | Greenfield, Brownfield, Migration |
| `compliance-assessment.md` | Compliance Assessment | G | All | Greenfield, Brownfield, Migration |
| `change-request.md` | Architecture Change Request | H | All | Greenfield, Brownfield, Migration |
| `decision-register.md` | Decision Register | All phases | All | All |
| `consolidated-report.md` | Consolidated Architecture Report | All phases | All | All |

### Domain Column Key

- **All** — scaffold for any domain selection
- **Business** — only when Business domain is selected
- **Data** — only when Data domain is selected
- **Application** — only when Application domain is selected
- **Technology** — only when Technology domain is selected

### Engagement Type Notes

- **Assessment-only**: Gap analysis is included (current-state gaps still identified); roadmap, migration plan, contracts, and change requests are excluded (E–H are Not Applicable).
- **Business Model Canvas**: Not applicable to Assessment-only engagements — the BMC documents the business model for transformation planning, not current-state assessment.
- **Migration**: Migration Plan is primary; Architecture Roadmap is also created to sequence the migration waves.
