# Phase Status Reference

## Engagement Status Values

`Active` | `On Hold` | `Planning` | `Completed`

- **Active** — currently being worked on
- **On Hold** — paused; may resume later
- **Planning** — pre-kickoff preparation
- **Completed** — all planned work finished; all phases are either Complete or Not Applicable

Note: Engagement-level "Completed" is distinct from phase-level "Complete".

## Phase Status Values

`Not Started` | `In Progress` | `Complete` | `On Hold` | `Not Applicable`

`Not Applicable` is used when a phase is excluded based on engagement type and domain selection:
- Data domain deselected → C-Data = Not Applicable
- Assessment-only engagement → phases E-H = Not Applicable

## Phase Status State Transitions

All transitions below are valid. Timestamp management is automatic:

| From | To | Timestamp Effect |
|---|---|---|
| Not Started | In Progress | Sets `startedAt` to now |
| In Progress | Complete | Sets `completedAt` to now |
| In Progress | On Hold | No timestamp change |
| On Hold | In Progress | No timestamp change (preserves original `startedAt`) |
| Complete | In Progress | Clears `completedAt` (preserves `startedAt`) |
| Any | Not Started | Resets both `startedAt` and `completedAt` to null |
| Not Applicable | Any | Requires explicit user confirmation before override |

When a phase transitions to "In Progress" for the first time, `startedAt` is set. If the phase was previously started (has a `startedAt`), it is preserved on re-entry from On Hold.
