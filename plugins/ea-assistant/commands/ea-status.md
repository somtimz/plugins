---
name: ea-status
description: Show a dashboard of all EA engagements and their progress
allowed-tools: Read, Bash
---

Display a comprehensive status dashboard for all EA engagements.

## Instructions

1. Scan for all `EA-projects/*/engagement.json` files.

2. For each engagement, read:
   - Name, status, currentPhase, lastModified
   - Count of artifacts by review status (Draft / In Review / Approved / Needs Revision)
   - Phase completion summary

3. Display a dashboard:

   ```
   ═══════════════════════════════════════════════════
   EA ENGAGEMENT DASHBOARD
   ═══════════════════════════════════════════════════

   📁 Acme Retail Transformation          [ACTIVE]
      Current Phase : Phase B — Business Architecture
      Artifacts     : 4 total (2 Draft, 1 In Review, 1 Approved)
      ADM Progress  : Prelim ✅ | Req ✅ | A ✅ | B 🔄 | C ⬜ | D ⬜ | E ⬜ | F ⬜ | G ⬜ | H ⬜
      Last Modified : 2026-03-10

   📁 Finance Modernisation 2026          [ON HOLD]
      Current Phase : Phase A — Architecture Vision
      Artifacts     : 1 total (1 Draft)
      ADM Progress  : Prelim ✅ | Req ⬜ | A 🔄 | ...
      Last Modified : 2026-02-28

   ═══════════════════════════════════════════════════
   Total engagements: 2 | Active: 1 | On Hold: 1
   ═══════════════════════════════════════════════════
   ```

   Legend: ✅ Complete | 🔄 In Progress | ⏸ On Hold | ⬜ Not Started

4. If a specific engagement is currently open (active in context), highlight it with ► marker.

5. Offer options:
   - Open an engagement (`/ea-open`)
   - Create a new one (`/ea-new`)
   - View artifacts for an engagement (`/ea-artifact`)
