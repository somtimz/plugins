---
name: ea-new
description: Create a new EA engagement project
argument-hint: "[engagement-name]"
allowed-tools: Read, Write, Bash
---

Create a new EA engagement project under `EA-projects/`.

## Instructions

1. If an engagement name was provided as an argument, use it as the display name. Otherwise, ask the user for:
   - **Name** (required) — display name of the engagement
   - **Description** (required) — brief description of the engagement
   - **Sponsor / Owner** (required) — name of the executive sponsor
   - **Organisation** (required) — organisation or business unit
   - **Scope** (required) — brief scope statement
   - **Start Date** (required, default: today's date) — offer today's date as default
   - **Status** (default: `Active`) — Active / On Hold / Planning

2. Generate a slug from the name: lowercase, replace spaces with hyphens, remove special characters. Example: "Acme Retail Transformation 2026" → `acme-retail-transformation-2026`

3. Check that `EA-projects/{slug}/` does not already exist. If it does, inform the user and ask for a different name or whether to use the existing one.

4. Create the directory structure:
   ```
   EA-projects/{slug}/
   ├── requirements/
   ├── artifacts/
   ├── diagrams/
   ├── uploads/
   └── interviews/
   ```

5. Write `EA-projects/{slug}/engagement.json` with all fields populated and all ADM phases set to `Not Started`.

6. Read `.claude/ea-assistant.local.md` if it exists and extract `requirementsRepoPath`. Store in `engagement.json`. If the file does not exist, set `requirementsRepoPath` to `""`.

7. Confirm success to the user and display:
   - Engagement name and slug
   - Folder location: `EA-projects/{slug}/`
   - Offer to begin the **Preliminary phase** immediately or return to the main menu

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
  "status": "Active",
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
