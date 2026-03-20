# Command Interface Contract: EA Project Management

**Feature**: 002-ea-project-management
**Date**: 2026-03-20

## `/ea-status` Enhanced Dashboard

### Input
- No arguments required
- Scans `EA-projects/*/engagement.json` for active engagements
- Optionally scans `EA-projects/.archive/*/engagement.json` when "show archived" requested

### Output Format

```
═══════════════════════════════════════════════════════════════
EA ENGAGEMENT DASHBOARD
═══════════════════════════════════════════════════════════════

📁 Acme Retail Transformation          [ACTIVE]     Greenfield
   Domains       : Business, Data, Application, Technology
   Current Phase : Phase B — Business Architecture
   Artifacts     : 4 total (2 Draft, 1 In Review, 1 Approved)
   ADM Progress  : Prelim ✅ | Req ✅ | A ✅ | B 🔄 | C-Data ⬜ | C-App ⬜ | D ⬜ | E ⬜ | F ⬜ | G ⬜ | H ⬜
   Dates         : 2026-03-01 → 2026-09-30
   Last Modified : 2026-03-10

📁 Finance Modernisation 2026          [ON HOLD]    Assessment-only
   Domains       : Business, Data
   Current Phase : Phase A — Architecture Vision
   Artifacts     : 1 total (1 Draft)
   ADM Progress  : Prelim ✅ | Req ⬜ | A 🔄 | B ⬜ | C-Data ⬜ | C-App ➖ | D ➖ | E ➖ | F ➖ | G ➖ | H ➖
   Dates         : 2026-02-15 → —
   Last Modified : 2026-02-28

═══════════════════════════════════════════════════════════════
Total: 2 | Active: 1 | On Hold: 1 | Planning: 0 | Completed: 0
═══════════════════════════════════════════════════════════════

Legend: ✅ Complete | 🔄 In Progress | ⏸ On Hold | ⬜ Not Started | ➖ Not Applicable

Options:
1. Open an engagement (`/ea-open`)
2. Create a new engagement (`/ea-new`)
3. Show archived engagements
```

### Archived Section (when requested)

```
───────────────────────────────────────────────────────────────
ARCHIVED ENGAGEMENTS
───────────────────────────────────────────────────────────────

📦 Old Project Alpha                    [COMPLETED]  Brownfield
   Archived      : 2026-01-15
   Last Modified : 2026-01-10

Options:
1. Restore an archived engagement
2. Delete an archived engagement
3. Return to active dashboard
```

### Empty State

```
No EA engagements found.

Get started by creating your first engagement: /ea-new
```

### Legacy Engagement Display

When `engagementType`, `architectureDomains`, or `targetEndDate` are missing:
- Type column shows "—"
- Domains line shows "Business, Data, Application, Technology" (default)
- Dates show start date only with "→ —" for missing target end date

---

## `/ea-open` Enhanced Command

### Input
- Optional argument: engagement name or slug
- Scans `EA-projects/*/engagement.json`

### Picklist Format

```
#  | Name                          | Type           | Domains | Phase   | Status    | Last Modified
---|-------------------------------|----------------|---------|---------|-----------|---------------
1  | Acme Retail Transformation    | Greenfield     | 4       | Phase B | Active    | 2026-03-10
2  | Finance Modernisation 2026    | Assessment-only| 2       | Phase A | On Hold   | 2026-02-28
3  | Group IT Strategy             | Migration      | 4       | Phase A | Active    | 2026-03-12
```

### Opened Engagement Summary

```
✅ Opened: Acme Retail Transformation
📁 Folder:  EA-projects/acme-retail-transformation-2026/

## Engagement Details

| Field | Value |
|-------|-------|
| Name | Acme Retail Transformation |
| Slug | acme-retail-transformation-2026 |
| Type | Greenfield |
| Domains | Business, Data, Application, Technology |
| Sponsor | Jane Smith |
| Organisation | Acme Corp |
| Scope | End-to-end retail platform transformation |
| Start Date | 2026-03-01 |
| Target End Date | 2026-09-30 |
| Status | Active |

## ADM Phase Progress

| Phase | Name | Status |
|-------|------|--------|
| Prelim | Preliminary | ✅ Complete |
| Requirements | Architecture Requirements | ✅ Complete |
| A | Architecture Vision | ✅ Complete |
| B | Business Architecture | 🔄 In Progress |
| C-Data | Data Architecture | ⬜ Not Started |
| C-App | Application Architecture | ⬜ Not Started |
| D | Technology Architecture | ⬜ Not Started |
| E | Opportunities & Solutions | ⬜ Not Started |
| F | Migration Planning | ⬜ Not Started |
| G | Implementation Governance | ⬜ Not Started |
| H | Architecture Change Management | ⬜ Not Started |

## Artifacts (4 total)

| Artifact | Phase | Status | Review |
|----------|-------|--------|--------|
| Architecture Principles | Prelim | Approved | Approved |
| Stakeholder Map | Prelim | Draft | Not Reviewed |
| Architecture Vision | A | In Review | In Review |
| Business Architecture | B | Draft | Not Reviewed |

## Next Actions

1. Continue current phase (Phase B — Business Architecture)
2. View artifacts (`/ea-artifact`)
3. Start an interview (`/ea-interview`)
4. View detailed status
5. Edit engagement metadata
6. Edit phase status
7. Edit artifact status
8. Archive engagement
9. Delete engagement
```

### Edit Metadata Flow

```
Which field would you like to edit?

1. Name (display only — slug unchanged)
2. Description
3. Sponsor
4. Organisation
5. Scope
6. Status (Active / On Hold / Planning / Completed)
7. Start Date
8. Target End Date

> [user selects field]

Current value: Active
New value: On Hold

✅ Updated: status → "On Hold"
   engagement.json saved (lastModified: 2026-03-20T14:30:00Z)
```

### Edit Phase Status Flow

```
Select a phase to update:

| # | Phase | Current Status |
|---|-------|---------------|
| 1 | Prelim | Complete |
| 2 | Requirements | Complete |
| 3 | A | Complete |
| 4 | B | In Progress |
| 5 | C-Data | Not Started |
| ...

> [user selects phase]

Phase B — Business Architecture
Current status: In Progress
New status: Not Started / In Progress / Complete / On Hold

> [user selects status]

✅ Updated: Phase B → "Complete"
   completedAt: 2026-03-20T14:35:00Z
   engagement.json saved

💡 Suggestion: Advance current phase to C-Data (Data Architecture)?
```

### Edit Artifact Status Flow

```
Select an artifact to update:

| # | Artifact | Phase | Status | Review |
|---|----------|-------|--------|--------|
| 1 | Architecture Principles | Prelim | Approved | Approved |
| 2 | Stakeholder Map | Prelim | Draft | Not Reviewed |
| ...

> [user selects artifact]

Stakeholder Map
What would you like to update?
1. Status (Draft / In Review / Approved / Needs Revision)
2. Review Status (Not Reviewed / In Review / Approved / Needs Revision)

> [user selects field and value]

✅ Updated: Stakeholder Map status → "In Review"
   engagement.json saved (lastModified: 2026-03-20T14:40:00Z)
```

### Archive Flow

```
⚠️ Archive "Acme Retail Transformation"?

This will move the engagement to EA-projects/.archive/acme-retail-transformation-2026/
It will no longer appear in /ea-status or /ea-open.
You can restore it later.

Confirm? (yes/no)

> yes

✅ Archived: Acme Retail Transformation
   Moved to: EA-projects/.archive/acme-retail-transformation-2026/
```

### Delete Flow

```
⚠️ DELETE "Acme Retail Transformation"?

This will PERMANENTLY remove:
  EA-projects/acme-retail-transformation-2026/
  Including all artifacts, interviews, diagrams, and engagement data.

This action cannot be undone.

Type the engagement slug to confirm: acme-retail-transformation-2026

> acme-retail-transformation-2026

✅ Deleted: Acme Retail Transformation
   Directory removed: EA-projects/acme-retail-transformation-2026/
```

### Restore Flow (from /ea-status archived section)

```
Select an archived engagement to restore:

| # | Name | Status | Archived |
|---|------|--------|----------|
| 1 | Old Project Alpha | Completed | 2026-01-15 |

> 1

✅ Restored: Old Project Alpha
   Moved to: EA-projects/old-project-alpha/
   Now visible in /ea-status and /ea-open.
```
