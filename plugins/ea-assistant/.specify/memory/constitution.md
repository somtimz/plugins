<!--
  Sync Impact Report
  ===================
  Version change: N/A (initial) → 1.0.0
  Modified principles: N/A (first ratification)
  Added sections:
    - Core Principles (5): Framework Fidelity, User-Sourced Content,
      Plugin Architecture, Engagement Isolation, Template-Driven Artifacts
    - Quality Standards
    - Development Workflow
    - Governance
  Removed sections: none
  Templates requiring updates:
    - .specify/templates/plan-template.md — ✅ compatible (Constitution Check
      section references constitution file generically)
    - .specify/templates/spec-template.md — ✅ compatible (no constitution
      references to update)
    - .specify/templates/tasks-template.md — ✅ compatible (no constitution
      references to update)
  Follow-up TODOs: none
-->

# EA Assistant Constitution

## Core Principles

### I. Framework Fidelity

All architecture artifacts, phases, and classifications MUST accurately
reflect the frameworks they claim to implement:

- **TOGAF 10**: ADM phases (Preliminary, A–H), deliverables, and
  terminology MUST match the standard. No invented phases or renamed
  deliverables.
- **Zachman Framework**: The full 6×6 matrix MUST be preserved. Cell
  descriptions MUST align with Zachman's published definitions.
- **ArchiMate 3.x**: Element names, relationships, and viewpoints MUST
  conform to the ArchiMate specification. No custom element types
  without explicit user request.

Rationale: Users rely on this plugin for professional EA work.
Misrepresenting standards erodes trust and produces non-compliant
deliverables.

### II. User-Sourced Content (NON-NEGOTIABLE)

Artifact content MUST originate from user interviews, uploaded
documents, or explicit user input — never from arbitrary AI generation.

- AI-suggested content MUST be marked with `🤖 AI Draft — Review required`.
- Unanswered fields MUST be marked with `⚠️ Not answered`.
- Not-applicable fields MUST be marked with `➖ Not applicable`.
- Placeholders MUST NOT be silently filled with plausible-sounding
  content.

Rationale: Enterprise Architecture artifacts inform real business
decisions. Fabricated content is worse than no content.

### III. Plugin Architecture

EA Assistant MUST conform to the Claude Code plugin structure defined
in the repository's `CLAUDE.md`:

- `plugin.json` with required fields (name, version, description, author).
- Agents in `agents/` with valid YAML frontmatter (name, description,
  model, color).
- Commands in `commands/` with valid YAML frontmatter (name,
  description).
- Skills in `skills/*/SKILL.md` with valid YAML frontmatter (name,
  description, version).
- Semantic versioning for all version fields.
- Conventional commit messages scoped to `ea-assistant`.

Rationale: CI validates plugin structure on every PR. Non-conforming
changes will be rejected.

### IV. Engagement Isolation

Each EA engagement MUST be fully self-contained within its own
directory under `EA-projects/<engagement-name>/`:

- All engagement state (metadata, artifacts, diagrams, interviews,
  uploads, requirements) MUST reside within the engagement directory.
- No engagement MAY read or modify another engagement's data without
  explicit user action (e.g., `/ea-merge` across engagements).
- `engagement.json` MUST be the single source of truth for engagement
  metadata, current ADM phase, and settings.

Rationale: Users run multiple concurrent engagements. Cross-contamination
of engagement data produces incorrect architecture deliverables.

### V. Template-Driven Artifacts

All TOGAF artifacts MUST be generated from templates in the `templates/`
directory:

- Templates define the canonical structure for each artifact type.
- New artifact types MUST have a corresponding template before
  generation is supported.
- Template modifications MUST be backward-compatible or accompanied by
  a migration path for existing engagements.
- Templates MUST use the standard field markers defined in
  Principle II (AI Draft, Not answered, Not applicable).

Rationale: Consistent artifact structure ensures cross-artifact
consistency checking works reliably and users get predictable output.

## Quality Standards

- **Diagram accuracy**: Diagrams (Mermaid, Graphviz, Draw.io) MUST use
  correct notation for the target framework (ArchiMate elements and
  relationships, TOGAF deliverable references).
- **Cross-artifact consistency**: The consistency checker agent MUST
  validate that entities, capabilities, and requirements referenced in
  one artifact exist and are correctly named in related artifacts.
- **Review workflow**: Every artifact MUST support the review lifecycle
  (draft → under review → approved/revision needed). Review status MUST
  be persisted in the engagement directory.
- **Interview integrity**: Stakeholder interview notes MUST be dated
  and versioned. Imported interview data (from Word) MUST preserve the
  original responses without modification.

## Development Workflow

- **Frontmatter validation**: All agent, command, and skill files MUST
  pass the CI frontmatter validation workflow before merge.
- **Scope discipline**: Changes MUST be scoped to the `ea-assistant`
  plugin directory. Cross-plugin changes require separate PRs.
- **Backward compatibility**: Changes to engagement storage format,
  template structure, or command interfaces MUST include migration
  guidance for existing engagements.
- **Testing**: New commands and agents SHOULD include usage examples
  in their description or README sections to enable manual verification.

## Governance

This constitution is the authoritative reference for EA Assistant
development decisions. When a proposed change conflicts with these
principles, the constitution takes precedence unless formally amended.

**Amendment procedure**:

1. Propose the change with rationale in a PR or conversation.
2. Document which principles are affected and why the change is needed.
3. Update this constitution via `/speckit.constitution` with the
   amendment details.
4. Propagate changes to affected templates and dependent artifacts.

**Versioning policy**: This constitution follows semantic versioning:

- MAJOR: Principle removal or backward-incompatible redefinition.
- MINOR: New principle or materially expanded guidance.
- PATCH: Clarifications, wording, or non-semantic refinements.

**Compliance review**: All feature specs and implementation plans MUST
include a Constitution Check verifying alignment with these principles.

**Version**: 1.0.0 | **Ratified**: 2026-03-19 | **Last Amended**: 2026-03-19
