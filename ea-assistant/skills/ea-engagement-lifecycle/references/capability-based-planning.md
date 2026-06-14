# Capability-Based Planning

TOGAF technique for planning change in terms of **business capabilities** rather than projects or systems. The capability is the planning unit; projects (work packages) are merely the delivery vehicles. Use this method when building the Capability Model (Phase B) and the Architecture Roadmap (Phase E).

## Core Method

1. **Anchor on the Capability Model** (Phase B, CAP-NNN). Each capability is people + process + information + tools — all four dimensions, not just the system.
2. **Assess each in-scope capability**: current maturity → required maturity, with the gap recorded as a Capability Gap (feeding GAP-NNN). Rate the four dimensions separately — a capability is only as mature as its weakest dimension.
3. **Decompose the change into Capability Increments** — discrete, independently valuable maturity steps per capability (see the Capability Increment entry in `ea-concepts.md`). Each increment names the observable improvement, not the project that delivers it.
4. **Map increments to Work Packages** (Phase E): each WP-NNN delivers one or more increments; each increment is delivered by one or more WPs. Record the mapping in the Roadmap (the `Advances Goals/Objectives` linkage carries the motivation chain; the increment mapping carries the capability chain).
5. **Sequence by increment dependency and readiness**, not by system convenience: an increment that depends on another capability's increment constrains wave order; readiness ceilings (see Business Transformation Readiness Assessment) cap concurrent business-facing increments.
6. **Measure at the capability level**: define MET-NNN per capability increment (leading indicators where possible) so progress is reported as capability maturity gained, not work packages closed.

## Increment Quality Tests

| Test | Fail looks like |
|---|---|
| Independently valuable | "Increment 1: build the database" — that's a task, not a capability state |
| Observable | No one could tell from outside whether the increment is live |
| Four-dimensional | Only the tooling changed; process/people/information dimensions unaddressed |
| Plateau-aligned | The increment can't actually operate at any planned Transition Architecture |

## Wiring in This Plugin

| Step | Where |
|---|---|
| Capability Model / CAP-NNN | Business Architecture (Phase B); `ea-concepts.md` Capability Model entry |
| Capability gaps | `/ea-gaps` (domain: Capability) |
| Increments | Architecture Roadmap — per-capability increment list under each WP cluster ("CAP-007 Increment 2") |
| Readiness ceiling | `templates/phase-a/business-transformation-readiness.md` → Roadmap Implications |
| Measures | MET-NNN in `engagement.json → metrics`, linked to the capability's goals/objectives |

## Anti-patterns

- **Project-based planning wearing a capability costume** — WPs defined first, capabilities retrofitted. The tell: increments read like project phases ("Phase 1: foundation").
- **Tool-only increments** — buying the platform counts as an increment only if the process and people dimensions move with it.
- **Big-bang capability** — a capability with a single increment spanning the whole roadmap has not been decomposed; it cannot be governed.
