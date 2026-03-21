---
name: itil-change-request
description: >
  Launch an interactive ITIL v4-compliant Change Request management app. Use this skill whenever the user wants to create, edit, or manage IT change requests for CAB approval. Triggers include: "change request", "CAB submission", "RFC", "request for change", "change management", upgrading servers/databases/applications, infrastructure changes, patch deployments, software rollouts, or any request where an IT team needs formal approval. Use this skill even if the user just says "I need to submit a change" or "open the change request tool".
version: 0.1.0
---

# ITIL Change Request Skill

Launches an interactive Change Request management app. All CR data persists between sessions via `window.storage`.

## Workflow

When this skill is triggered, read `references/cr-app.jsx` and present it as a React JSX artifact. Do not collect information inline — the app handles everything.

The app supports:
- Creating and editing CRs (all ITIL v4 fields)
- Selecting approvers from a predefined list
- Implementer checklist (check off impl/rollback/validation steps)
- Status management: Draft → Pending CAB Approval
- Dashboard with filter by status

## Word doc export

If the user asks to export a CR as a Word doc:
1. Read `/mnt/skills/public/docx/SKILL.md`
2. Read `references/docx-template.md` for structure
3. Generate `.docx` using `docx` npm package
4. Save to: `/mnt/user-data/outputs/Change Requests/{RFC_ID}.docx`
   - Approved CRs: `/mnt/user-data/outputs/Change Requests/Approved/{RFC_ID}.docx`
5. Validate: `python scripts/office/validate.py`
6. Present with `present_files`

## Storage layout

| Key | Value |
|---|---|
| `cr_index` | JSON array of RFC IDs |
| `cr_{id}` | JSON — full CR record |

## CR schema

```json
{
  "id": "RFC-2026-0042",
  "title": "", "changeType": "Normal", "priority": "Medium",
  "requestedBy": "", "changeOwner": "",
  "dateSubmitted": "2026-03-05",
  "affectedSystems": "", "businessJustification": "", "changeDescription": "",
  "implSteps":       [{ "id": 1, "text": "", "checked": false }],
  "rollbackSteps":   [{ "id": 1, "text": "", "checked": false }],
  "validationItems": [{ "id": 1, "text": "", "checked": false }],
  "changeWindow": { "start": "", "duration": "", "maintenanceWindow": "" },
  "riskLevel": "Medium", "riskImpact": "", "riskUsers": "", "riskDeps": "",
  "approverIds": ["a1"],
  "status": "Draft", "cabNotes": "",
  "cabHistory": [],
  "retrospectiveReview": false,
  "createdAt": "2026-03-05T12:00:00Z", "updatedAt": "2026-03-05T12:00:00Z"
}
```

## Status flow

```
Draft → Pending CAB Approval → Approved by CAB
                             → Rejected

Emergency (changeType === "Emergency"):
Draft → Approved by CAB (auto-approved, retrospectiveReview: true)
```

- Pending → Approved/Rejected is handled by the `/cab-review` skill.
- Emergency CRs skip CAB — the app auto-approves and sets `retrospectiveReview: true`.
- Rejected CRs can be reverted to Draft for editing and resubmission.
- Approved and Rejected CRs are read-only — no edits permitted.

## Predefined approvers

| ID | Name | Role |
|---|---|---|
| a1 | Sarah Johnson | IT Director |
| a2 | Mark Chen | Application Owner |
| a3 | Lisa Patel | Security Lead |
| a4 | David Williams | Infrastructure Manager |
| a5 | Jennifer Torres | Change Manager |
| a6 | Robert Kim | Database Administrator |
| a7 | Amanda Foster | Network Lead |
| a8 | Michael Osei | CISO |
