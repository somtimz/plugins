---
name: ea-new
description: Create a new EA engagement project
argument-hint: "[engagement-name]"
allowed-tools: [Read, Write, Bash]
---

Create a new EA engagement project under `EA-projects/`.

## Instructions

1. If an engagement name was provided as an argument, use it as the display name. Otherwise, ask the user for:
   - **Name** (required) — display name of the engagement
   - **Description** (required) — brief description of the engagement
   - **Sponsor / Owner** (required) — name of the executive sponsor
   - **Organisation** (required) — organisation or business unit
   - **Scope** (required) — brief scope statement
   - **Engagement Type** (required) — Greenfield / Brownfield / Assessment-only / Migration
   - **Start Date** (required, default: today's date) — offer today's date as default
   - **Status** (default: `Active`) — Active / On Hold / Planning

2. Generate a slug from the name: lowercase, replace spaces with hyphens, remove special characters. Example: "Acme Retail Transformation 2026" → `acme-retail-transformation-2026`

3. Check that `EA-projects/{slug}/` does not already exist. If it does, inform the user and ask for a different name or whether to use the existing one.

4. Create the directory structure and seed files:
   ```
   EA-projects/{slug}/
   ├── .claude/
   │   └── rules/
   │       └── ea-engagement.md    ← seed from templates/seeds/engagement-rules.md
   ├── requirements/
   ├── artifacts/
   │   ├── preliminary/
   │   ├── requirements/
   │   ├── phase-a/
   │   ├── phase-b/
   │   ├── phase-c-data/
   │   ├── phase-c-app/
   │   ├── phase-d/
   │   ├── phase-e/
   │   ├── phase-f/
   │   ├── phase-g/
   │   ├── phase-h/
   │   └── cross-cutting/
   ├── diagrams/
   ├── uploads/
   ├── interviews/
   ├── reviews/
   ├── ResearchAndReferences/
   │   └── research-index.md    ← seed from templates/seeds/research-index.md
   └── brainstorm/
       └── brainstorm-notes.md  ← seed with heading and instructions
   ```

   Seed files by reading from the `templates/seeds/` directory and substituting `{name}`, `{slug}`, and today's date:
   - `.claude/rules/ea-engagement.md` ← `templates/seeds/engagement-rules.md`
   - `ResearchAndReferences/research-index.md` ← `templates/seeds/research-index.md`

   Seed `brainstorm/brainstorm-notes.md` with:
   ```markdown
   # Brainstorm Notes — {name}

   Use this file for freeform background, constraints, political context,
   stakeholder dynamics, and anything else that informs the engagement but
   doesn't belong in a structured artifact.

   This file is **never overwritten** by EA Assistant — it is yours to maintain.
   The EA interviewer surfaces relevant content from here during interviews.
   ```

5. Write `EA-projects/{slug}/engagement.json` using the template in `templates/seeds/engagement-json.md`, populated with all collected fields. Set all ADM phases to `Not Started`. See `skills/ea-engagement-lifecycle/references/engagement-schema.md` for the full annotated schema.

6. Read `.claude/ea-assistant.local.md` if it exists and extract `requirementsRepoPath`. Store in `engagement.json`. If the file does not exist, set `requirementsRepoPath` to `""`.

7. Write `EA-projects/{slug}/CLAUDE.md` from the template at `templates/seeds/engagement-claude-md.md`, substituting all `{field}` placeholders from `engagement.json`. This file is loaded automatically by Claude Code when a session is opened from inside the engagement folder.

   The `.claude/rules/ea-engagement.md` file (seeded in step 4) is loaded automatically alongside CLAUDE.md and enforces persistent session guardrails.

8. Confirm success to the user and display:
   - Engagement name and slug
   - Folder location: `EA-projects/{slug}/`
   - Offer to begin the **Preliminary phase** immediately or return to the main menu
