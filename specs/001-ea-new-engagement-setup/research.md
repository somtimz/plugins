# Research: EA New Engagement Setup

## R1: Engagement Type to ADM Phase Applicability Mapping

**Decision**: Map each engagement type to a set of applicable ADM phases,
while allowing user override via domain selection.

**Rationale**: The existing `engagement-patterns.md` reference already
documents which phases are emphasized per pattern. This mapping codifies
that guidance into a default configuration that `/ea-new` can apply
automatically.

**Mapping**:

| Engagement Type  | Always Applicable          | Applicable if Domain Selected        | Typically Skipped |
|------------------|----------------------------|--------------------------------------|-------------------|
| Greenfield       | Prelim, Req, A, E, F, G, H | B (Business), C-Data (Data), C-App (Application), D (Technology) | None |
| Brownfield       | Prelim, Req, A, E, F, G, H | B, C-Data, C-App, D                  | None |
| Assessment-only  | Prelim, Req, A             | B, C-Data, C-App, D                  | E, F, G, H |
| Migration        | Prelim, Req, A, E, F, G, H | B, C-Data, C-App, D                  | None |

**Domain → Phase mapping**:
- Business → Phase B
- Data → Phase C-Data
- Application → Phase C-App
- Technology → Phase D

Phases not in "Always Applicable" and not mapped by any selected domain
are set to "Not Applicable" in `engagement.json`.

**Alternatives considered**:
- Fully manual phase selection: rejected because it adds cognitive load
  and users would need TOGAF knowledge to make correct selections.
- Hardcoded per-type with no domain override: rejected because real
  engagements often scope out specific domains.

## R2: Preliminary Phase Scaffolding Artifact Set

**Decision**: Scaffold two artifacts for all engagement types:
Architecture Principles and Stakeholder Map. These are universally
applicable to the Preliminary phase regardless of type or domain.

**Rationale**: The ADM Phase Guide lists 5 Preliminary artefacts:
Architecture Principles Catalogue, Architecture Governance Framework,
Architecture Repository (initial), Request for Architecture Work
(template), and Tailored ADM. Of these, only Architecture Principles
and Stakeholder Map have existing templates in the plugin. The others
(Governance Framework, Repository, Tailored ADM) are organizational
outputs that are better created through interview-driven workflows
than scaffolding.

**Alternatives considered**:
- Scaffold all 5 Preliminary artifacts: rejected because 3 of 5 don't
  have templates yet. Creating new templates is out of scope for this
  feature.
- Scaffold no artifacts (leave to `/ea-artifact`): rejected because the
  spec explicitly requires scaffolding as a core enhancement.

## R3: Confirmation Summary UX Pattern

**Decision**: After collecting all fields, display a formatted Markdown
summary table showing each field name and value. Offer three actions:
confirm (create the engagement), edit (re-prompt for a specific field),
or cancel (abandon creation).

**Rationale**: Claude Code commands interact via conversational prompts.
A summary table is the clearest way to present all fields at once in a
terminal environment. The edit action re-prompts for the selected field
only, preserving all other values.

**Alternatives considered**:
- Numbered list with "type a number to edit": rejected because it adds
  an extra indirection step.
- No edit capability (confirm or cancel only): rejected because the spec
  explicitly requires edit-before-save.

## R4: Backward Compatibility with Existing Engagements

**Decision**: New fields (`engagementType`, `architectureDomains`,
`targetEndDate`) are optional in `engagement.json`. Commands that read
engagement data MUST handle missing fields gracefully by applying
defaults: `engagementType` defaults to `null` (unclassified),
`architectureDomains` defaults to all four, `targetEndDate` defaults
to `null`.

**Rationale**: Constitution Principle IV (Engagement Isolation) and
Development Workflow (backward compatibility) require that existing
engagements continue to work. No migration script is needed; the schema
is additive.

**Alternatives considered**:
- Require migration of existing engagements: rejected because it adds
  unnecessary complexity and risk for a CLI plugin.
- Store new fields separately from `engagement.json`: rejected because
  it violates the single-source-of-truth principle for engagement
  metadata.

## R5: Slug Generation Rules

**Decision**: Use the existing algorithm (lowercase, replace spaces with
hyphens, remove non-alphanumeric characters except hyphens, collapse
consecutive hyphens, truncate to 60 characters) as already defined in
the current `ea-new.md` command.

**Rationale**: The existing rules are sufficient and well-tested. No
changes needed.
