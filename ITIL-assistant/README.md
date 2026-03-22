# ITIL Assistant

A Claude Code plugin for ITIL v4 Change Management — create, manage, and review IT Change Requests with a full CAB approval workflow.

## Overview

ITIL Assistant provides an interactive Change Request management system following ITIL v4 best practices. It supports the full change lifecycle from draft creation through CAB approval, with implementer checklists and Word document export.

## Features

- **Change Request management** — create, edit, and track RFCs with all ITIL v4 fields
- **CAB approval workflow** — submit CRs for review; approve or reject with notes
- **Implementer checklists** — track implementation steps, rollback plan, and validation items
- **Status dashboard** — filter and view CRs by status (Draft, Pending, Approved, Rejected)
- **Word document export** — generate formatted .docx for formal CAB submissions
- **Persistent storage** — all CR data persists between sessions

## Skills

| Skill | Description |
|---|---|
| `itil-change-request` | Interactive CR creation and management app |
| `cab-review` | CAB administrator review and approval tool |

## Commands

| Command | Description |
|---|---|
| `/itil-cr` | Open the Change Request management tool |
| `/cab-review` | Open the CAB Review tool |

## Status Flow

```
Draft → Pending CAB Approval → Approved by CAB
                             → Rejected
```

## Installation

```bash
/plugin install ITIL-assistant
```
