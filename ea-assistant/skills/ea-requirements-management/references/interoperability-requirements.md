# Interoperability Requirements

TOGAF technique for identifying and refining the requirements that govern how systems, organisations, and partners work together. Use during the Requirements phase discovery interview and refine in Phase C-App (integration views) and Phase D. Interoperability requirements attach to **Interfaces** (IFC-NNN) wherever one exists.

## Categories

| Category | Concerns | Typical owner |
|---|---|---|
| **Business / Operational** | Shared processes across org boundaries, aligned SLAs, escalation paths, operating-hours alignment, regulatory data-sharing agreements | Business / service owners |
| **Information** | Shared semantics (canonical models, code sets), data quality obligations at the boundary, master-data ownership, classification compatibility | Data owners / stewards |
| **Technical** | Protocols, formats, API standards, versioning, security token compatibility, network reachability, throughput at the boundary | Application / technology architects |

## Degrees of Interoperability

Rate each required interaction — the degree drives how much architecture work the boundary needs:

| Degree | Meaning | Architecture implication |
|---|---|---|
| 1 — Unstructured exchange | Humans exchange documents/files | Minimal — define format and channel |
| 2 — Structured exchange | Data exchanged in agreed structures, manually processed | Canonical format + validation rules |
| 3 — Seamless data sharing | Automated exchange under a shared model | IFC-NNN with full contract; master-data ownership decided |
| 4 — Seamless information sharing | Shared understanding — data interpreted identically everywhere | Canonical semantic model; governance over change to it |

## Discovery Checklist (Requirements phase / C-App)

1. Which external organisations, partners, or regulators must this architecture exchange data with? Under what agreements?
2. Which internal systems must interoperate across domain or vendor boundaries in the target state?
3. For each interaction: required degree (1–4), direction, volume, latency, and availability expectations?
4. Are there mandated standards at any boundary (industry formats, government schemas, STD-NNN entries)?
5. Who owns the canonical definition of shared entities (customer, product, account) — and is that ownership accepted by both sides?
6. What happens at the boundary when the other side changes — what backward-compatibility window is required?
7. Are there security/classification constraints on what may cross each boundary?

## Capture Conventions

- Each confirmed interoperability need → **REQ-NNN** with `category: Non-Functional`, `nfrSubType: Compatibility` (or `Security` for boundary-control requirements), a `measurableTarget` (degree, latency, compat window), and source.
- Each boundary with degree ≥ 3 → an **IFC-NNN** interface catalogue entry (see `ea-concepts.md`); link the REQ to it.
- Mandated standards → link the REQ to the **STD-NNN** entry (`/ea-standards`); conflicts become CST-NNN constraints.
- Unresolvable ownership disputes over shared data → CON-NNN (stakeholder concern) and, if blocking, ISS-NNN.

## Anti-patterns

- "Integrate with X" captured as a functional requirement with no degree, volume, or contract — untestable; always force a measurable target.
- Treating interoperability as purely technical — degree 3–4 interactions fail on semantics and ownership, not protocols.
- Designing point-to-point contracts where a mandated industry standard (STD-NNN) already exists.
