---
name: ea-merge
description: Merge all EA artifacts into a single consolidated architecture document
argument-hint: "[markdown|word|both]"
allowed-tools: Read, Write, Bash
---

Merge all artifacts for the active engagement into a single consolidated document.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

### Step 1: Select Artifacts

1. List all artifacts for the engagement with their status:
   ```
   Artifacts to include in consolidated report:
   ✅ Architecture Principles       (Approved)
   ✅ Requirements Register         (Approved)
   ✅ Architecture Vision           (Approved)
   🔄 Business Architecture         (Draft — include anyway?)
   ⬜ Application Architecture      (Not created — skip)
   ```

2. Ask: "Include Draft artifacts? (yes/no)"
3. Ask: "Exclude any specific artifacts? (enter numbers to exclude, or press Enter to include all)"

### Step 2: Determine Output Format

- If argument is `markdown` — Markdown only
- If argument is `word` — Word (.docx) only
- If argument is `both` or no argument — both formats
- If pandoc is not available and Word is requested, warn the user and offer Markdown only

### Step 3: Build Consolidated Document

Assemble artifacts in standard TOGAF order:
1. Cover page (engagement name, sponsor, date, version)
2. Table of Contents
3. Architecture Principles (Prelim)
4. Requirements Register (Requirements phase)
5. Architecture Vision (Phase A)
6. Stakeholder Map (Phase A)
7. Statement of Architecture Work (Phase A)
8. Business Architecture (Phase B)
9. Data/Information Architecture (Phase C)
10. Application Architecture (Phase C)
11. Technology Architecture (Phase D)
12. Gap Analysis (Phases B–D)
13. Architecture Roadmap (Phase E/F)
14. Migration Plan (Phase F)
15. Architecture Contracts (Phase G)
16. Appendices (uploaded source documents reference list)

For each included artifact:
- Add a section divider with the artifact name and phase
- Include the artifact content as-is
- Append any open review comments as a sub-section: "## Open Review Comments"
- Do NOT alter artifact content during merge

### Step 4: Add Cover Page

```markdown
# Consolidated Architecture Document
## {Engagement Name}

| Field | Value |
|---|---|
| Organisation | {organisation} |
| Sponsor | {sponsor} |
| Version | 1.0 |
| Date | {YYYY-MM-DD} |
| Status | Draft / For Review |

---
> ⚠️ This document contains sections in Draft status. Sections marked 🔄 have not been approved.
```

### Step 5: Write Output

- Markdown: `artifacts/consolidated-report-{YYYY-MM-DD}.md`
- Word: `artifacts/consolidated-report-{YYYY-MM-DD}.docx` (via pandoc)

```bash
pandoc artifacts/consolidated-report-{date}.md \
  -o artifacts/consolidated-report-{date}.docx
```

### Step 6: Confirm

Report output files and sizes. Offer to open or share the document.
