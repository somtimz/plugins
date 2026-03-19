# Scaffolding Map

This reference defines which artifacts are automatically scaffolded when a new engagement is created via `/ea-new`. The scaffolding engine uses this map to determine which templates to copy based on the selected engagement type and architecture domains.

## Engagement Type to ADM Phase Applicability

Each engagement type determines which ADM phases are applicable. Phases not listed as "Always" or mapped by a selected domain are set to "Not Applicable".

| Engagement Type  | Always Applicable           | Domain-Dependent (if selected)       | Skipped                |
|------------------|-----------------------------|--------------------------------------|------------------------|
| Greenfield       | Prelim, Requirements, A, E, F, G, H | B (Business), C-Data (Data), C-App (Application), D (Technology) | None |
| Brownfield       | Prelim, Requirements, A, E, F, G, H | B, C-Data, C-App, D                  | None                   |
| Assessment-only  | Prelim, Requirements, A     | B, C-Data, C-App, D                  | E, F, G, H             |
| Migration        | Prelim, Requirements, A, E, F, G, H | B, C-Data, C-App, D                  | None                   |

### Domain to Phase Mapping

| Domain       | ADM Phase |
|--------------|-----------|
| Business     | B         |
| Data         | C-Data    |
| Application  | C-App     |
| Technology   | D         |

### Phase Applicability Rules

1. Phases in "Always Applicable" are set to "Not Started" regardless of domain selection.
2. For each selected domain, set the corresponding phase to "Not Started".
3. For each deselected domain, set the corresponding phase to "Not Applicable".
4. Phases in "Skipped" (by engagement type) are set to "Not Applicable" regardless of domain selection.

## Preliminary Phase Artifacts

The following artifacts are scaffolded during engagement creation. All are applicable to the Preliminary phase.

| Artifact ID              | Display Name              | Template Path                          | Applicable Types | Applicable Domains |
|--------------------------|---------------------------|----------------------------------------|------------------|--------------------|
| architecture-principles  | Architecture Principles   | templates/architecture-principles.md   | All              | All                |
| stakeholder-map          | Stakeholder Map           | templates/stakeholder-map.md           | All              | All                |

### Scaffolding Rules

For each artifact in the table above:

1. **Type check**: If the engagement type is not in "Applicable Types", skip the artifact.
2. **Domain check**: If "Applicable Domains" specifies a domain list, skip the artifact if none of the listed domains are selected. "All" means scaffold regardless of domain selection.
3. **Copy template**: Copy the template file to `EA-projects/{slug}/artifacts/{artifact-id}.md`.
4. **Replace variables**: Substitute template variables with engagement metadata:
   - `{{engagement_name}}` → engagement name
   - `{{organisation}}` → organisation
   - `{{sponsor}}` → sponsor name
   - `{{YYYY-MM-DD}}` → today's date
5. **Mark content**: All content sections that are not pre-populated from metadata MUST be marked with `⚠️ Not answered`.
6. **Register artifact**: Add an entry to the `artifacts` array in `engagement.json`:
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
7. **Missing template**: If the template file does not exist, skip the artifact, log a warning to the user, and continue with remaining artifacts. Note the skipped artifact in the creation confirmation.
