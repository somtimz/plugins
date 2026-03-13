---
name: ea-open
description: Open or switch between EA engagements
argument-hint: "[engagement-name-or-slug]"
allowed-tools: Read, Write, Bash
---

Display a picklist of all EA engagements and allow the user to open one.

## Instructions

1. Scan for all `EA-projects/*/engagement.json` files. If no engagements exist, inform the user and offer to run `/ea-new`.

2. Build a picklist table from all found engagements:

   ```
   #  | Name                          | Phase   | Status    | Last Modified
   ---|-------------------------------|---------|-----------|---------------
   1  | Acme Retail Transformation    | Phase B | Active    | 2026-03-10
   2  | Finance Modernisation 2026    | Prelim  | On Hold   | 2026-02-28
   3  | Group IT Strategy             | Phase A | Active    | 2026-03-12
   ```

3. If an argument was provided, try to match it against engagement names or slugs directly. If a match is found, open it without showing the picklist.

4. Ask the user to select an engagement by number.

5. Load the selected engagement:
   - Read `engagement.json`
   - Display a summary:
     ```
     ✅ Opened: Acme Retail Transformation
     📁 Folder:  EA-projects/acme-retail-transformation-2026/
     📍 Phase:   Phase B — Business Architecture (In Progress)
     📋 Artifacts: 3 (2 Draft, 1 Approved)
     🕒 Last Modified: 2026-03-10
     ```
   - List any in-progress or pending artifacts
   - Offer next actions: continue current phase, view artifacts, start an interview, view status

6. Store the active engagement slug in the conversation context for subsequent commands.
