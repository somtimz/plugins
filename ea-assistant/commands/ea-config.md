---
name: ea-config
description: Configure EA Assistant plugin settings and engagement rules
argument-hint: "[settings|rules|optouts|refresh]"
allowed-tools: [Read, Write, Bash]
---

Configure EA Assistant plugin settings, engagement rules, opt-outs, and refresh the engagement pointer doc.

## Instructions

## Engagement Resolution

Used by Sections 2, 3, and 4. Run this logic whenever a section requires an active engagement:

1. Check whether `EA-projects/` exists. If not, display:
   ```
   No EA-projects directory found. Run `/ea-new` to create your first engagement.
   ```
   Then stop.

2. Scan `EA-projects/*/engagement.json` for all files.

3. If exactly one engagement is found: use it silently and continue.

4. If multiple engagements are found: display a numbered list and ask the user to select:
   ```
   Multiple engagements found:
     1. acme-retail-transformation-2026
     2. finance-modernisation-2026
   Select engagement:
   ```
   Wait for selection; use the chosen slug for the remainder of the section.

5. If no engagements are found: display:
   ```
   No engagements found. Run `/ea-new` to create one.
   ```
   Then stop.
