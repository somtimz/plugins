---
name: ea-roles
description: List, filter, and generate role catalogue entries for EA engagements
---

# /ea-roles

Provides access to the canonical role catalogue (`skills/ea-engagement-lifecycle/references/role-catalogue.md`) and generates per-engagement Role Catalogue artifacts.

## Usage

```
/ea-roles                              List all 15 roles (ID, name, one-line description)
/ea-roles <ROLE-ID>                    Full entry for that role (all extended attributes)
/ea-roles --domain <domain>            Filter by domain
/ea-roles --generate                   Generate role-catalogue artifact in active engagement
/ea-roles --update <ROLE-ID>           Assign a named individual and org to a role
```

## Sub-commands

### `/ea-roles` (no arguments)

Read `skills/ea-engagement-lifecycle/references/role-catalogue.md` and display a summary table:

| Role ID | Role | Domain | Description (one line) |
|---------|------|--------|----------------------|
| ROLE-001 | Stakeholder | Governance | Owner of the architecture; holds decision rights |
| … | … | … | … |

### `/ea-roles <ROLE-ID>`

Display the full entry for the specified role — all sections: description, responsibilities, typical tasks, RACI defaults, triggering events, cadence, and escalation path.

If the ROLE-ID is not found, list valid IDs and prompt the user to try again.

### `/ea-roles --domain <domain>`

Filter the role list to the specified domain. Valid domains:

| Domain | Roles included |
|--------|---------------|
| `governance` | ROLE-001, ROLE-002, ROLE-004, ROLE-006 |
| `architecture` | ROLE-006, ROLE-007, ROLE-008, ROLE-009, ROLE-010 |
| `business` | ROLE-001, ROLE-002, ROLE-003, ROLE-011 |
| `data` | ROLE-008, ROLE-014 |
| `application` | ROLE-009, ROLE-015 |
| `delivery` | ROLE-005, ROLE-012, ROLE-013 |

Display a filtered summary table. If the domain value is not recognised, list valid domains.

### `/ea-roles --generate`

Generate a Role Catalogue artifact in the active engagement:

1. Confirm the active engagement is loaded (if not, prompt `/ea-open` first)
2. Read `templates/role-catalogue.md`
3. Substitute `{{engagement_name}}`, `{{organisation}}`, and `{{YYYY-MM-DD}}`
4. Write to `EA-projects/{slug}/artifacts/phase-a/role-catalogue.md`
5. Register the artifact in `engagement.json` under `artifacts` with `status: Draft`
6. Confirm: "Role Catalogue created at `artifacts/phase-a/role-catalogue.md`. Use `/ea-roles --update ROLE-NNN` to assign named individuals, or open the file directly."

If a role-catalogue artifact already exists for this engagement, ask before overwriting.

### `/ea-roles --update <ROLE-ID>`

Interactively assign a named individual and organisation to a role in the active engagement's Role Catalogue:

1. Read `EA-projects/{slug}/artifacts/phase-a/role-catalogue.md`
2. Find the row for `<ROLE-ID>`
3. Prompt: "Who is assigned to [Role Name] (ROLE-NNN)? Enter name:"
4. Prompt: "Organisation unit:"
5. Update the row in the file; update `lastModified` in frontmatter
6. Confirm: "[Role Name] assigned to [Name] ([Org])."

If no Role Catalogue artifact exists, prompt to run `/ea-roles --generate` first.

## Domain Map Reference

Read the canonical role definitions from:
`skills/ea-engagement-lifecycle/references/role-catalogue.md`

Do not recite role descriptions from memory — always read the file.
