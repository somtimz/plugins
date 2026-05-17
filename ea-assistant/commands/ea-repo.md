---
name: ea-repo
description: Initialise an EA-Workspace with a shared Architecture Repository, link engagements, and show repository status. The Architecture Repository holds Standards Information Base (SIB/STD-NNN), Vendor Landscape (VDR-NNN), and Technology Horizon (THR-NNN) registers shared across all EA engagements and IT projects.
---

# /ea-repo — Architecture Repository Management

Uses skill: `ea-architecture-repository`

---

## Mode: `init [workspace-path]`

Initialise a new EA-Workspace at `[workspace-path]` (default: `./EA-Workspace` relative to current directory).

### Steps

1. Confirm the target path with the user: "Initialise EA-Workspace at `<path>`?"
2. Prompt for organisation name (used in workspace.json and repo.json names)
3. Create directory structure:
   - `<path>/` (workspace root)
   - `<path>/EA-Projects/`
   - `<path>/Architecture-Repository/`
   - `<path>/Architecture-Repository/governance/`
   - `<path>/Architecture-Repository/sib/standards/`
   - `<path>/Architecture-Repository/vendor-landscape/entries/`
   - `<path>/Architecture-Repository/technology-horizon/entries/`
   - `<path>/Architecture-Repository/reference-library/`
4. Write `workspace.json` from seed `workspace-json.md` — substitute:
   - `{{organisation}}` → user-provided organisation name
   - `{{YYYY-MM-DD}}` → today's date
   - `{{YYYY-MM-DDTHH:MM:SSZ}}` → current UTC datetime
5. Write `repo.json` from seed `architecture-repo-json.md` with same substitutions
6. Write stub files:
   - `Architecture-Repository/governance/enterprise-principles.md` — heading: "# Enterprise Architecture Principles"
   - `Architecture-Repository/governance/enterprise-policies.md` — heading: "# Enterprise Architecture Policies"
   - `Architecture-Repository/governance/enterprise-constraints.md` — heading: "# Enterprise Architecture Constraints"
   - `Architecture-Repository/sib/sib-index.md` — heading: "# Standards Information Base Index"
   - `Architecture-Repository/vendor-landscape/vendor-index.md` — heading: "# Vendor Landscape Register Index"
   - `Architecture-Repository/technology-horizon/horizon-index.md` — heading: "# Technology Horizon Register Index"
7. Report:
   ```
   ✓ EA-Workspace initialised at <path>
   ✓ Architecture-Repository/ created (SIB, Vendor Landscape, Technology Horizon)
   ✓ EA-Projects/ ready for engagements

   Next steps:
     /ea-new              — create a new engagement (auto-links to this workspace)
     /ea-repo link <slug> — link an existing engagement
   ```

---

## Mode: `link <engagement-slug> [--workspace-path <path>]`

Link an existing EA engagement to this workspace's Architecture Repository.

### Steps

1. Resolve workspace root:
   - If `--workspace-path` provided: use that path and read `workspace.json`
   - Otherwise: walk up from current directory (max 4 levels) looking for `workspace.json`
   - If not found: error "No workspace.json found. Run /ea-repo init or provide --workspace-path."
2. Read `workspace.json` and `Architecture-Repository/repo.json` — confirm both exist and are valid JSON
3. Locate the engagement at `EA-Projects/<slug>/engagement.json`:
   - If not found: error "Engagement '<slug>' not found in EA-Projects/."
4. Update `engagement.json`:
   - Set `"repoPath": "../../Architecture-Repository"`
   - Update `"lastModified"` to now
5. Update `workspace.json`:
   - Append to `projects[]`: `{ "slug": "<slug>", "name": "<engagement.name>", "path": "EA-Projects/<slug>", "status": "Active", "linkedDate": "<today>" }`
   - Update `"lastModified"` to now
6. Update `Architecture-Repository/repo.json`:
   - Append to `linkedEngagements[]`: `{ "slug": "<slug>", "name": "<engagement.name>", "path": "EA-Projects/<slug>", "linkedDate": "<today>" }`
   - Update `"lastModified"` to now
7. Report:
   ```
   ✓ Engagement '<name>' linked to Architecture Repository
   ✓ engagement.json → repoPath: "../../Architecture-Repository"
   ✓ workspace.json → projects[] updated
   ✓ repo.json → linkedEngagements[] updated

   Now available:
     /ea-vendors    — manage Vendor Landscape Register (VDR-NNN)
     /ea-horizon    — manage Technology Horizon Register (THR-NNN)
     /ea-standards  — manage Standards Information Base (STD-NNN)
   ```

---

## Mode: `status [--workspace-path <path>]`

Show Architecture Repository health dashboard.

### Steps

1. Resolve workspace root (same walk-up logic as `link`)
2. Read `workspace.json` and `Architecture-Repository/repo.json`
3. Count entries:
   - VDR entries: count files in `Architecture-Repository/vendor-landscape/entries/`
   - THR entries: count files in `Architecture-Repository/technology-horizon/entries/`
   - STD entries: count files in `Architecture-Repository/sib/standards/`
4. Display:
   ```
   Architecture Repository: <repo.name>
   Organisation:            <repo.organisation>
   Owner:                   <repo.owner.name> (<repo.owner.email>)
   Last modified:           <repo.lastModified>

   Registers:
     Vendor Landscape:      <n> vendors (VDR-NNN)
     Technology Horizon:    <n> technologies (THR-NNN)
     Standards (SIB):       <n> standards (STD-NNN)

   Linked engagements (<count>):
     <slug>   <name>   <linkedDate>
     ...

   Warnings:
     [if owner.name is empty]: ⚠ No repository owner set — update repo.json → owner
     [if linkedEngagements is empty]: ⚠ No engagements linked — run /ea-repo link <slug>
   ```

---

## Mode: `open [workspace-path]`

Set the active Architecture Repository for the current session.

Store the resolved absolute path to `Architecture-Repository/` in session context so subsequent `/ea-vendors`, `/ea-horizon`, `/ea-standards` calls resolve it without needing `--workspace-path`.

If no path provided, walk up from current directory looking for `workspace.json`.

Report the active repository name and path.

---

## TOGAF Reference

TOGAF 10 §37 — Architecture Repository. Preliminary Phase output: "Populated Architecture Repository". Phase H input: "Existing Architecture Repository (for change assessment)".
