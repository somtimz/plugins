---
name: ea-review
description: Open an artifact for review and assessment, track review state and comments
argument-hint: "[artifact-name]"
allowed-tools: [Read, Write, Bash]
---

Open an EA artifact for formal review and assessment.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

### Select Artifact

If no artifact name is provided, list all artifacts with their current review status:

```
Select artifact to review:
1. Architecture Vision          [Draft — Not Reviewed]
2. Architecture Principles      [Approved]
3. Requirements Register        [In Review — 2 open comments]
4. Business Architecture        [Needs Revision]
```

### Load Artifact for Review

1. Read the artifact file from `artifacts/{artifact-id}.md`
2. Read the review file `artifacts/{artifact-id}.review.md` if it exists
3. Display the artifact content with existing review comments inline (if any)

### Review Actions

Present the following options:

**a) Add a review comment**
- Ask: "Which section or field does your comment relate to?"
- Ask: "What is your comment or suggested change?"
- Ask: "Reviewer name (optional)"
- Append to `{artifact-id}.review.md`:
  ```markdown
  ## Comment — {YYYY-MM-DD} {Reviewer}
  **Section:** {section name}
  **Comment:** {comment text}
  **Status:** Open
  ```

**b) Resolve a comment**
- List open comments
- Mark selected comment as `Resolved` in the review file

**c) Update artifact review status**
- Options: `Draft` | `In Review` | `Approved` | `Needs Revision`
- Update `reviewStatus` in `engagement.json` artifacts entry
- Update the artifact frontmatter `reviewStatus` field

**d) View all open comments**
- List all unresolved comments across the review file

**e) Export review for offline**
- Export artifact + review comments as a single Markdown or Word document

### Review File Format

`artifacts/{artifact-id}.review.md`:

```markdown
# Review: {Artifact Name}
# Engagement: {Engagement Name}

---

## Comment — 2026-03-10 — Jane Smith
**Section:** Strategic Goals
**Comment:** The goals listed do not align with the board's priorities from Q1 2026.
**Status:** Open

## Comment — 2026-03-11 — John Doe
**Section:** Stakeholder Register
**Comment:** Missing the CTO and CFO from the stakeholder list.
**Status:** Resolved — 2026-03-12
```
