# Research: Change Request Workflow

**Feature**: 003-cr-workflow
**Date**: 2026-03-20

## R1: Claude Code Plugin Component Types

**Decision**: Use skills as the primary component, commands as thin wrappers, no agents needed.

**Rationale**: Skills auto-activate on natural language triggers, which matches how users will interact with change management ("I need to submit a change", "review pending CRs"). Commands provide explicit `/itil-cr` and `/cab-review` shortcuts. Agents would add complexity without value — the skills handle the full workflow via artifact rendering.

**Alternatives considered**:
- Agent-driven: An agent could orchestrate CR creation conversationally, but this duplicates what the JSX artifact already does interactively. Rejected for violating Principle V (Simplicity).
- Commands-only: Would require users to know exact command names. Rejected because skill auto-activation provides better discoverability.

## R2: React JSX Artifact Pattern

**Decision**: Store complete React JSX apps in `references/*.jsx` files. SKILL.md instructs the agent to read the file and present it as a React JSX artifact.

**Rationale**: This is the established pattern in Claude's artifact system. The JSX runs in a sandboxed React environment with access to `window.storage` for persistence. The existing `cr-app.jsx` (739 lines) and `cab-review-app.jsx` (410 lines) from the temp directory follow this pattern.

**Alternatives considered**:
- Inline JSX in SKILL.md: Would make SKILL.md unreadable at 700+ lines. Rejected.
- Multiple smaller JSX files composed together: Claude's artifact viewer renders a single JSX export. Rejected — each artifact must be self-contained.

## R3: Storage Schema Design

**Decision**: Use `window.storage` with `cr_index` (array of RFC IDs) and `cr_{id}` (full CR JSON) keys. Add `cabHistory` array to CR schema for audit trail.

**Rationale**: `window.storage` is the persistence mechanism available in Claude's artifact runtime. The index + individual record pattern allows efficient listing (read index) without loading all CR data, and individual CR reads/writes without rewriting the entire dataset.

**Alternatives considered**:
- Single key with all CRs: Would hit storage size limits with many CRs and require full rewrite on every change. Rejected.
- Separate storage per skill: Would break the shared data contract between `itil-change-request` and `cab-review`. Rejected per Constitution Principle IV.

## R4: Emergency Change Flow

**Decision**: Emergency CRs skip CAB approval. Submitting an Emergency CR transitions it directly from Draft to "Approved by CAB" with a `retrospectiveReview: true` flag. CAB reviews post-implementation.

**Rationale**: ITIL v4 explicitly distinguishes emergency changes as requiring expedited processing. The retrospective review flag ensures the CAB review tool can surface these for post-hoc review.

**Alternatives considered**:
- Same flow for all types: Would misrepresent ITIL v4 practices. Rejected per Constitution Principle III.
- Separate "Emergency Approved" status: Would add a 5th status to the flow, increasing UI complexity. Rejected — using the existing "Approved by CAB" status with a flag is simpler.

## R5: CR Schema Changes (from Clarifications)

**Decision**: Extend the existing CR schema with:
1. `cabHistory`: Array of `{ action, notes, timestamp }` objects — append-only audit trail
2. `retrospectiveReview`: Boolean flag for emergency changes
3. Deletion: Draft CRs only, removes from both `cr_index` and `cr_{id}`
4. Resubmission: Rejected CRs can revert to Draft; rejection notes preserved in `cabHistory`

**Rationale**: These extensions address the four clarifications from the spec session. `cabHistory` preserves audit trail across review cycles. The retrospective flag enables post-hoc CAB review of emergency changes.

## R6: Word Document Export

**Decision**: Use the `docx` npm package with the template structure defined in `references/docx-template.md`. The SKILL.md provides step-by-step instructions for the agent to generate the document.

**Rationale**: The docx template already exists and defines all sections (cover block, 7 content sections, footer). The agent generates a Node.js script at runtime, executes it, and presents the output file. No custom tooling needed.

**Alternatives considered**:
- Pandoc conversion from Markdown: Would require Pandoc as a dependency and produce less controlled formatting. Rejected.
- HTML-to-docx: Would add browser/puppeteer dependency. Rejected per Principle V.
