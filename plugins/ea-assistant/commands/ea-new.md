---
name: ea-new
description: Create a new EA engagement project
argument-hint: "[engagement-name]"
allowed-tools: [Read, Write, Bash]
---

Create a new EA engagement project under `EA-projects/`.

## Instructions

1. **Collect engagement metadata.** If an engagement name was provided as an argument, use it as the display name and skip the Name prompt. Otherwise, ask the user for each field in order. For fields with defaults, offer the default and accept Enter to confirm it.

   | Order | Field | Required | Default | Format |
   |-------|-------|----------|---------|--------|
   | 1 | **Name** | Yes | — | Free text |
   | 2 | **Description** | Yes | — | Free text |
   | 3 | **Sponsor / Owner** | Yes | — | Free text |
   | 4 | **Organisation** | Yes | — | Free text |
   | 5 | **Scope** | Yes | — | Brief scope statement |
   | 6 | **Engagement Type** | Yes | — | Select one: Greenfield, Brownfield, Assessment-only, Migration |
   | 7 | **Architecture Domains** | Yes | All four | Multi-select: Business, Data, Application, Technology |
   | 8 | **Start Date** | Yes | Today | ISO 8601 date (YYYY-MM-DD) |
   | 9 | **Target End Date** | No | None | ISO 8601 date (YYYY-MM-DD) |
   | 10 | **Status** | Yes | Active | Select one: Active, On Hold, Planning |

   **Validation rules:**
   - Name must not be empty. If empty, re-prompt.
   - At least one architecture domain must be selected. If none selected, re-prompt.
   - Engagement type must be one of the four listed values.

2. **Generate a slug** from the name: lowercase, replace spaces with hyphens, remove special characters (keep only `a-z`, `0-9`, `-`), collapse consecutive hyphens, truncate to maximum 60 characters. Example: "Acme Retail Transformation 2026" → `acme-retail-transformation-2026`. Example: "Acme & Partners (2026)" → `acme-partners-2026`.

3. **Check for duplicates.** If `EA-projects/{slug}/` already exists, inform the user:

   ```
   An engagement with slug "{slug}" already exists.

   Options:
   1. Open the existing engagement
   2. Choose a different name
   ```

   If the user chooses to open the existing engagement, hand off to the `/ea-open` command. If they choose a different name, return to step 1 (Name prompt only).

4. **Display confirmation summary.** Show all collected values in a table for the user to review:

   ```markdown
   ## New Engagement Summary

   | Field | Value |
   |-------|-------|
   | Name | {name} |
   | Slug | {slug} |
   | Description | {description} |
   | Sponsor | {sponsor} |
   | Organisation | {organisation} |
   | Scope | {scope} |
   | Engagement Type | {engagementType} |
   | Architecture Domains | {comma-separated domains} |
   | Start Date | {startDate} |
   | Target End Date | {targetEndDate or "None"} |
   | Status | {status} |

   **Actions**: Confirm / Edit [field name] / Cancel
   ```

   - **Confirm**: Proceed to step 5.
   - **Edit [field name]**: Re-prompt for the named field only, update the value, regenerate the slug if Name was edited, and redisplay the summary. Loop until the user confirms or cancels.
   - **Cancel**: Abandon creation. Display "Engagement creation cancelled. No files were created." and stop.

5. **Create the directory structure.** If `EA-projects/` does not exist, create it first.

   ```
   EA-projects/{slug}/
   ├── requirements/
   ├── artifacts/
   ├── diagrams/
   ├── uploads/
   └── interviews/
   ```

6. **Determine phase applicability.** Based on the engagement type and selected architecture domains, set each ADM phase status using the rules from `references/scaffolding-map.md`:

   **Always applicable phases** (set to "Not Started"):
   - All types: Prelim, Requirements, A
   - Greenfield, Brownfield, Migration: also E, F, G, H
   - Assessment-only: E, F, G, H are "Not Applicable"

   **Domain-dependent phases:**
   - Business selected → B = "Not Started"; Business deselected → B = "Not Applicable"
   - Data selected → C-Data = "Not Started"; Data deselected → C-Data = "Not Applicable"
   - Application selected → C-App = "Not Started"; Application deselected → C-App = "Not Applicable"
   - Technology selected → D = "Not Started"; Technology deselected → D = "Not Applicable"

7. **Read plugin settings.** If `.claude/ea-assistant.local.md` exists, extract `requirementsRepoPath` and store it in `engagement.json`. If the file does not exist, set `requirementsRepoPath` to `""`.

8. **Write `engagement.json`** with all fields populated per the template below.

9. **Scaffold Preliminary phase artifacts.** For each artifact defined in `references/scaffolding-map.md`:
   - Check that the engagement type and domain selection match the artifact's applicability rules.
   - Copy the template file from `templates/` to `EA-projects/{slug}/artifacts/{artifact-id}.md`.
   - Replace template variables with engagement metadata:
     - `{{engagement_name}}` → name
     - `{{organisation}}` → organisation
     - `{{sponsor}}` → sponsor
     - `{{YYYY-MM-DD}}` → today's date
   - Mark all content sections that are not pre-populated with `⚠️ Not answered`.
   - Add the artifact to the `artifacts` array in `engagement.json` with status "Draft" and reviewStatus "Not Reviewed".
   - If a template file is missing, skip that artifact, warn the user, and continue with remaining artifacts.

10. **Confirm success** and display:

    ```markdown
    ## Engagement Created

    **Name**: {name}
    **Slug**: {slug}
    **Location**: EA-projects/{slug}/

    ### Scaffolded Artifacts
    - artifacts/architecture-principles.md (Draft)
    - artifacts/stakeholder-map.md (Draft)

    **Next**: Begin Preliminary phase (`/ea-phase Prelim`) or return to menu?
    ```

    If any artifacts were skipped due to missing templates, note them here.

## engagement.json Template

```json
{
  "name": "",
  "slug": "",
  "description": "",
  "sponsor": "",
  "organisation": "",
  "scope": "",
  "startDate": "",
  "targetEndDate": null,
  "status": "Active",
  "engagementType": "",
  "architectureDomains": [],
  "currentPhase": "Prelim",
  "requirementsRepoPath": "",
  "lastModified": "",
  "phases": {
    "Prelim": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "Requirements": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "A": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "B": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-Data": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "C-App": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "D": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "E": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "F": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "G": { "status": "Not Started", "startedAt": null, "completedAt": null },
    "H": { "status": "Not Started", "startedAt": null, "completedAt": null }
  },
  "artifacts": []
}
```

**Note:** Phase statuses in the template above are defaults. Step 6 overrides them based on engagement type and domain selection. The actual `engagement.json` written will have the correct applicability-adjusted statuses.
