---
name: cab-review
description: >
  Launch the CAB (Change Advisory Board) admin review tool. Use this skill when an administrator wants to review pending change requests, approve or reject them, or check what CRs are awaiting CAB decision. Triggers include: "cab review", "review change requests", "approve change requests", "pending approvals", "CAB admin", or any request from someone acting as a CAB administrator. Use this even if the user just says "show me what needs CAB approval" or "I need to approve some CRs".
version: 0.1.0
---

# CAB Review Skill

Launches the CAB administrator review app. Reads from the same `window.storage` keys as the `itil-change-request` skill — no separate data store.

## Workflow

When this skill is triggered, read `references/cab-review-app.jsx` and present it as a React JSX artifact.

The app:
- Lists all CRs with status `Pending CAB Approval`
- Lets the CAB admin open each one and review full details
- Provides Approve / Reject buttons with optional notes
- Updates the CR status in `window.storage` immediately on decision

## Status transitions performed by this skill

| Action | From | To |
|---|---|---|
| Approve | Pending CAB Approval | Approved by CAB |
| Reject  | Pending CAB Approval | Rejected |

## Storage

Reads and writes the same keys as `itil-change-request`:
- `cr_index` — array of RFC IDs
- `cr_{id}` — individual CR records

Approved/Rejected CRs are updated in place; the index is unchanged.

## Word doc export after approval

If the admin wants to export an approved CR as a Word doc:
1. Read `/mnt/skills/public/docx/SKILL.md` and `references/docx-template.md` from the `itil-change-request` skill
2. Generate `.docx`
3. Save to `/mnt/user-data/outputs/Change Requests/Approved/{RFC_ID}.docx`
