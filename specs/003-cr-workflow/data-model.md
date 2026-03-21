# Data Model: Change Request Workflow

**Feature**: 003-cr-workflow
**Date**: 2026-03-20

## Entities

### Change Request (CR)

The central entity. Stored as JSON in `window.storage` under key `cr_{id}`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | RFC identifier, format: `RFC-{YYYY}-{NNNN}` (e.g., `RFC-2026-0042`) |
| `title` | string | Yes* | Short description of the change |
| `changeType` | enum | Yes | `"Standard"` \| `"Normal"` \| `"Emergency"` |
| `priority` | enum | Yes | `"Low"` \| `"Medium"` \| `"High"` \| `"Critical"` |
| `requestedBy` | string | No | Name or team requesting the change |
| `changeOwner` | string | Yes* | Name or email of the implementer |
| `dateSubmitted` | string | Yes | ISO date `YYYY-MM-DD` |
| `affectedSystems` | string | No | Systems, servers, or services affected |
| `businessJustification` | string | No | Business need or risk being addressed |
| `changeDescription` | string | Yes* | What is being changed and why |
| `implSteps` | ChecklistStep[] | Yes | Implementation steps (min 1 entry) |
| `rollbackSteps` | ChecklistStep[] | Yes | Rollback plan steps (min 1 entry) |
| `validationItems` | ChecklistStep[] | Yes | Testing/validation criteria (min 1 entry) |
| `changeWindow` | ChangeWindow | No | Proposed timing for the change |
| `riskLevel` | enum | Yes | `"Low"` \| `"Medium"` \| `"High"` |
| `riskImpact` | string | No | Impact description if change fails |
| `riskUsers` | string | No | Affected users or services |
| `riskDeps` | string | No | Dependencies or prerequisites |
| `approverIds` | string[] | No | Array of approver IDs (e.g., `["a1", "a3"]`) |
| `status` | enum | Yes | See Status Flow below |
| `cabNotes` | string | No | Latest CAB decision notes |
| `cabHistory` | CabDecision[] | No | Append-only array of all CAB decisions |
| `retrospectiveReview` | boolean | No | `true` for emergency changes that skipped CAB |
| `createdAt` | string | Yes | ISO 8601 timestamp |
| `updatedAt` | string | Yes | ISO 8601 timestamp, refreshed on every save |

\* Required for CAB submission (validated by UI before enabling "Submit to CAB" button).

### ChecklistStep

Embedded within CR — not stored separately.

| Field | Type | Description |
|-------|------|-------------|
| `id` | number | Sequential ID within the list |
| `text` | string | Step description |
| `checked` | boolean | Completion state |

### ChangeWindow

Embedded within CR.

| Field | Type | Description |
|-------|------|-------------|
| `start` | string | Proposed start date/time (free text) |
| `duration` | string | Estimated duration (free text) |
| `maintenanceWindow` | string | Maintenance window description (free text) |

### CabDecision

Embedded within CR's `cabHistory` array. Append-only.

| Field | Type | Description |
|-------|------|-------------|
| `action` | enum | `"approve"` \| `"reject"` |
| `notes` | string | CAB administrator's notes |
| `timestamp` | string | ISO 8601 timestamp of the decision |

### Approver

Hardcoded in JSX artifacts. Not stored in `window.storage`.

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique ID (`a1` through `a8`) |
| `name` | string | Display name |
| `role` | string | Organizational role |

**Predefined values**:

| ID | Name | Role |
|----|------|------|
| a1 | Sarah Johnson | IT Director |
| a2 | Mark Chen | Application Owner |
| a3 | Lisa Patel | Security Lead |
| a4 | David Williams | Infrastructure Manager |
| a5 | Jennifer Torres | Change Manager |
| a6 | Robert Kim | Database Administrator |
| a7 | Amanda Foster | Network Lead |
| a8 | Michael Osei | CISO |

## Status Flow

```
                    ┌─────────────────────────────────────┐
                    │           Emergency bypass           │
                    │  (changeType === "Emergency")        │
                    v                                      │
Draft ──► Pending CAB Approval ──► Approved by CAB ◄──────┘
                    │                   ▲
                    │                   │ (resubmit)
                    v                   │
                 Rejected ──────► Draft (revert)
```

**Valid transitions**:

| From | To | Trigger | Conditions |
|------|----|---------|------------|
| Draft | Pending CAB Approval | "Submit to CAB" button | Title, Change Owner, Change Description required; changeType is Normal or Standard |
| Draft | Approved by CAB | "Submit to CAB" button | changeType is Emergency; sets `retrospectiveReview: true` |
| Pending CAB Approval | Approved by CAB | CAB admin clicks "Approve" | Appends to `cabHistory` |
| Pending CAB Approval | Rejected | CAB admin clicks "Reject" | Appends to `cabHistory` |
| Pending CAB Approval | Draft | "Revert to Draft" button | Requester pulls back for edits |
| Rejected | Draft | "Revert to Draft" button | Preserves `cabHistory` with rejection record |

**Invalid transitions** (enforced by UI): Draft → Approved (non-emergency), any → Deleted (except Draft), Approved → any.

## Storage Schema

### Keys

| Key | Value Type | Description |
|-----|-----------|-------------|
| `cr_index` | JSON string (string[]) | Array of RFC IDs in creation order |
| `cr_{id}` | JSON string (CR object) | Full CR record |

### Operations

| Operation | Read Keys | Write Keys | Notes |
|-----------|-----------|------------|-------|
| List all CRs | `cr_index`, then `cr_{id}` for each | — | Filter client-side by status |
| Create CR | `cr_index` | `cr_index`, `cr_{id}` | Append ID to index; write CR |
| Update CR | — | `cr_{id}` | Update `updatedAt`; do NOT modify index |
| Delete Draft CR | `cr_index` | `cr_index`, remove `cr_{id}` | Remove ID from index; delete record |
| CAB decision | — | `cr_{id}` | Append to `cabHistory`; update status, `cabNotes`, `updatedAt` |

### First-run behavior

If `cr_index` key does not exist or returns null, treat as empty array `[]`. Display empty dashboard with "New Change Request" button.
