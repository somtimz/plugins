---
name: ea-new
description: Create a new EA engagement project
argument-hint: "[engagement-name]"
allowed-tools: [Read, Write, Bash]
---

Create a new EA engagement project under `EA-projects/`.

## Instructions

### Workspace detection (pre-step)

Before creating the engagement, walk up from the current directory looking for `workspace.json` (check current dir, then parent, then grandparent, then great-grandparent — max 4 levels):

- **Workspace found:** Create the engagement at `<workspace-root>/EA-Projects/<slug>/`. Inform the user: "Creating engagement in EA-Workspace at `<workspace-root>`."
- **Workspace not found:** Ask the user:
  > "No EA-Workspace found. Options:
  > 1. Create a new EA-Workspace here (recommended)
  > 2. Continue without a workspace (engagement created at `./EA-Projects/<slug>/`)
  > 3. Enter an existing workspace path"

  If option 1: run `/ea-repo init` inline (prompt for org name, create workspace structure), then place engagement under it.
  If option 2: proceed with current behaviour — create at `./EA-Projects/<slug>/`.
  If option 3: validate the provided path contains `workspace.json`, then place engagement under it.

1. If an engagement name was provided as an argument, use it as the display name. Otherwise, ask the user for:
   - **Name** (required) — display name of the engagement
   - **Description** (required) — brief description of the engagement
   - **Sponsor / Owner** (required) — name of the executive sponsor
   - **Organisation** (required) — organisation or business unit
   - **Scope** (required) — brief scope statement
   - **Engagement Type** (required) — Greenfield / Brownfield / Assessment-only / Migration
   - **Architecture Level** (required) — the landscape level for this engagement:
     1. `Strategic`  — enterprise-wide direction, 5+ years (board/C-suite audience)
     2. `Segment`    — business domain/segment, 2–5 years (domain leadership audience)
     3. `Capability` — specific business capability, 1–3 years (capability owner audience)
     4. `Solution`   — specific project/initiative, immediate term (project/delivery audience)

     Not sure? Answer these: Is this sponsored by the board or C-suite? → Strategic. A single business unit or domain? → Segment. A specific capability or product area? → Capability. A specific project or system? → Solution. See `skills/ea-engagement-lifecycle/references/landscape-levels.md` for full guidance.
   - **Start Date** (required, default: today's date) — offer today's date as default
   - **Status** (default: `Active`) — Active / On Hold / Planning

2. Generate a slug from the name: lowercase, replace spaces with hyphens, remove special characters. Example: "Acme Retail Transformation 2026" → `acme-retail-transformation-2026`

3. Check that `EA-projects/{slug}/` does not already exist. If it does, inform the user and ask for a different name or whether to use the existing one.

3b. **ADM tailoring** — propose a phase set derived from the Architecture Level, then let the user adjust:

   | Level | Recommended phase set |
   |---|---|
   | Strategic | All phases (full ADM cycle) |
   | Segment | All phases |
   | Capability | All phases; offer to opt out of **Preliminary** when an Architecture Repository is linked (inherit enterprise principles/governance instead of re-establishing them) |
   | Solution | Offer to opt out of **Preliminary** (inherit from repository) and **Phase H** (change management handled at enterprise level); all other phases included but scoped to the solution |

   Present:
   ```
   Recommended phases for a {level} engagement: {list}
   Suggested opt-outs: {list with reasons, or "none"}
   Accept the recommendation, or adjust? (accept / toggle <phase> / full)
   ```
   - `accept` — apply the recommendation
   - `toggle <phase>` — flip a phase in/out (ask for a one-line reason when opting out)
   - `full` — include all phases regardless of level

   Requirements and the cross-cutting folder are always included — Requirements Management is the continuous center of the ADM and cannot be opted out.

4. Create the directory structure and seed files — **create `artifacts/{phase-folder}/` only for included phases** (plus `requirements/` and `cross-cutting/`, always):
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
   │       └── reference-architectures/
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
   - `.claude/rules/ea-local-config.md` ← `templates/seeds/ea-local-config.md` (user-editable; never overwritten)
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

5. Write `EA-projects/{slug}/engagement.json` using the template in `templates/seeds/engagement-json.md`, populated with all collected fields including `architectureLevel`. Set included ADM phases to `Not Started`; set opted-out phases to `Not Applicable` with an `optOutReason` field (from step 3b). Phases with `Not Applicable` status keep their entry in `phases[]` — they are excluded from picklists and progress counts (`/ea-status` already excludes them) but can be re-included later via `/ea-phase` (which restores `Not Started` and creates the folder). Read `.claude-plugin/plugin.json` and set `pluginVersion` and `lastMigratedVersion` to the `version` field value (new engagements start fully aligned); `schemaVersion` and `migrations` come from the seed (current schema, empty audit trail). Set `lastModified` to now (ISO 8601 timestamp). Set `adoptedRAs` to `[]` and `localRA` to `{ "nextId": 1 }`. See `skills/ea-engagement-lifecycle/references/engagement-schema.md` for the full annotated schema.

### Auto-link to Architecture Repository

After `engagement.json` is written, if a workspace was detected or created:
1. Set `engagement.json → repoPath: "../../Architecture-Repository"`
2. Append engagement to `workspace.json → projects[]`: `{ "slug": "<slug>", "name": "<name>", "path": "EA-Projects/<slug>", "status": "Active", "linkedDate": "<today>" }`
3. Append engagement to `Architecture-Repository/repo.json → linkedEngagements[]`: `{ "slug": "<slug>", "name": "<name>", "path": "EA-Projects/<slug>", "linkedDate": "<today>" }`
4. Update `lastModified` in both `workspace.json` and `repo.json`
5. Report: "✓ Linked to Architecture Repository at `<workspace>/Architecture-Repository`"

If no workspace: `repoPath` stays `null`. User can link later via `/ea-repo link <slug>`.

6. Read `.claude/ea-assistant.local.md` if it exists and extract `requirementsRepoPath`. Store in `engagement.json`. If the file does not exist, set `requirementsRepoPath` to `""`.

7. Write `EA-projects/{slug}/CLAUDE.md` from the template at `templates/seeds/engagement-claude-md.md`, substituting all `{field}` placeholders from `engagement.json`. This file is loaded automatically by Claude Code when a session is opened from inside the engagement folder.

   The `.claude/rules/ea-engagement.md` file (seeded in step 4) is loaded automatically alongside CLAUDE.md and enforces persistent session guardrails.

8. Confirm success to the user and display:
   - Engagement name and slug
   - Architecture Level: `{architectureLevel}`
   - Tailored phase set: `{included phases}`; opted out: `{phases with reasons, or "none"}`
   - Plugin Version: `{pluginVersion}` (ea-assistant version active at creation)
   - Folder location: `EA-projects/{slug}/`
   - Offer to begin the **Preliminary phase** immediately or return to the main menu
