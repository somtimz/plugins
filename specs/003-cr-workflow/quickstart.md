# Quickstart: ITIL-assistant Plugin

## Install

```bash
# From the plugins repository root
/plugin install ITIL-assistant
```

## Create a Change Request

Say any of:
- "I need to submit a change request"
- "Open the change request tool"
- `/itil-cr`

The interactive CR form will appear. Fill in:
1. **Title**, **Change Owner**, **Change Description** (required for submission)
2. Change type, priority, affected systems, business justification
3. Implementation steps, rollback plan, validation criteria
4. Change window and risk assessment
5. Select approvers from the predefined list

Click **Save Draft** to persist, or **Submit to CAB** when ready.

## Review & Approve Change Requests (CAB Admin)

Say any of:
- "Review change requests"
- "Show pending approvals"
- `/cab-review`

The CAB review dashboard shows all pending CRs. Click one to review full details, then **Approve** or **Reject** with optional notes.

## Track Implementation Progress

From the CR dashboard, click **Checklist** on any CR to open the implementation tracker. Check off steps as you complete them — progress saves automatically.

## Export to Word

Ask: "Export this change request as a Word document"

The plugin generates a formatted .docx with all CR sections and an approver signature table.

## Verify It Works

1. Create a CR with all fields → Save Draft → verify it appears on dashboard
2. Submit to CAB → verify status changes to "Pending CAB Approval"
3. Open CAB review → verify the CR appears → Approve it
4. Verify status is now "Approved by CAB"
5. Open checklist → check off some items → close and reopen → verify state persists
