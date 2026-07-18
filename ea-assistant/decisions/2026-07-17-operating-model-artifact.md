# Decision: First-Class Operating Model Artifact

**Date:** 2026-07-17

## Decision

The Operating Model is promoted to a **first-class Phase B authored artifact** (`templates/phase-b/operating-model.md`) with a dedicated slash command (`/ea-operatingmodel`). It is distinct from the Business Architecture artifact, which now focuses on the stable business blueprint (capabilities, value streams, services, information, rules, measures, use cases).

## Context

The Business Architecture template (`templates/phase-b/business-architecture.md`) had been conflating two different concerns:

1. **Business Architecture** — *what business the organisation needs to be* (stable blueprint).
2. **Operating Model** — *how the organisation will reliably operate that business* (execution design).

This made the Business Architecture artifact try to be both a capability/value blueprint and an org/process/controls design document, weakening both.

## Alternatives considered

1. **Keep OM as a section inside Business Architecture** — rejected because it perpetuates the conflation and makes the artifact too long and unfocused.
2. **Make OM a generated register** — rejected because OM content is primarily narrative/design (org design, decision rights, controls, sourcing, workforce) rather than a table of mastered items; processes already have the `PROC-NNN` register.
3. **Create a new top-level `operagement.json` array for OM** — rejected because most OM content is free-form artifact body; reuse existing `businessProcesses[]`, `services[]`, and the artifact registry.

## Reasoning

- First-class artifact status gives OM its own compliance checklist, scorecard, grill review, and export path.
- No new ID prefixes or top-level arrays are needed, minimising schema churn.
- The Business Architecture template can be refactored to focus on the blueprint, following the same summary-and-link pattern already used by the Architecture Vision.

## Trade-offs accepted

- Adds one more slash command to the surface area (`/ea-operatingmodel`).
- Legacy engagements with Organisation Model / Business Processes sections in BA will need a `/ea-migrate` split.
- The boundary between BA and OM requires explicit guidance (added to `ea-concepts.md`) and may need reinforcement during interviews.

## Supersedes

Nothing — this decision supplements `2026-07-17-business-architecture-layer-storage.md`, which covers `PROC-NNN` / `VS-NNN` / `UC-NNN` storage.
