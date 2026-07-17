# Decision: Storage model for first-class Business Architecture objects

**Date:** 2026-07-17

## Decision

Value Streams, Business Processes, and Use Cases are stored as **top-level arrays in `engagement.json`**: `valueStreams[]`, `businessProcesses[]`, `useCases[]`. The Business Process ID prefix is `PROC-NNN`.

## Context

The `ea-assistant` plugin is adding first-class register commands for Business Architecture objects drawn from three source decks. Existing first-class objects use two storage patterns:
- Motivation-chain items (`drivers`, `goals`, `objectives`, `strategies`, `issues`, `problems`, `opportunities`, `gaps`) live under `direction`.
- Cross-cutting governance/operational registers (`metrics`, `policies`, `finance`, `rules`, `services`) are top-level arrays.

## Alternatives considered

1. **Nested under `direction`**: rejected. Value streams, processes, and use cases are execution/business-layer objects, not motivation-chain items.
2. **Domain-prefixed IDs (e.g. `BP-PROC-NNN`)**: rejected. The ID scheme forbids domain-prefixed IDs except for the four architecture-principle prefixes (BP/DP/AP/TP).
3. **Reuse `BP-NNN` for Business Process**: rejected. `BP-NNN` is already allocated to Business Principles.

## Reasoning

- Top-level arrays match the recent `rules[]` / `services[]` pattern and keep the `direction` object focused on motivation.
- `PROC-NNN` is unique in the existing ID scheme and avoids collision with `BP-NNN` (Business Principle) and `PRB-NNN` (Problem).
- Stakeholder Goal Classification is treated as a classification lens, not a first-class object, so it needs no new ID prefix or register array.

## Trade-offs accepted

- Adds three more top-level arrays to `engagement.json`, increasing schema surface area. This is mitigated by `/ea-migrate` backfilling empty arrays for legacy engagements.
- Adds three new slash commands (`/ea-valuestreams`, `/ea-processes`, `/ea-usecases`), contributing to command-surface growth. Mitigated by keeping them thin and delegating mode mechanics to the register protocol and shared skills.

## Supersedes

None.
