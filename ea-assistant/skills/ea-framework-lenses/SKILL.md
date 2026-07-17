---
name: ea-framework-lenses
description: This skill should be used when the user asks to "apply a framework lens", "review against AWS Well-Architected", "well-architected review", "review against Azure CAF", "cloud adoption framework review", "review against the Google Cloud Architecture Framework", "apply cloud framework", "check pillar coverage", or when /ea-grill --skill waf|caf|gcaf is invoked or a phase interview offers framework lens questions. Provides a pluggable mechanism for reviewing EA artifacts and phases against external prescriptive frameworks.
version: 0.9.86
---

# EA Framework Lenses

A **framework lens** maps an external prescriptive framework (pillars, design principles, best practices) onto the TOGAF ADM so its guidance can be applied at the right phase, in the right artifact, without making the framework a parallel methodology. TOGAF remains the process backbone; a lens is an overlay.

## Lens Registry

| Lens | Short name | Reference file | Status |
|---|---|---|---|
| AWS Well-Architected Framework | `waf` | `references/aws-well-architected.md` | Available |
| Azure Cloud Adoption Framework | `caf` | `references/azure-caf.md` | Available — adoption-lifecycle shape: strongest in Phases A/B/E/F |
| Google Cloud Architecture Framework | `gcaf` | `references/google-caf.md` | Available |

The security frameworks (SABSA, ISO 27001, NIST CSF) are **not** lenses — they have their own deeper integration via the `ea-security` skill and `/ea-security-review`.

## Lens File Contract

Every lens reference file must contain these sections, in order:

1. **`## Pillars`** — the framework's top-level structure, one `###` per pillar: definition (1–2 sentences) and condensed design principles.
2. **`## ADM Mapping`** — table: pillar → primary ADM phase(s) → target artifact(s). This is what makes the lens consumable.
3. **`## Review Checklist`** — per pillar, 4–8 checkable items phrased as questions a reviewer answers against an artifact. Used by `/ea-grill --skill {short-name}`.
4. **`## Interview Questions`** — per relevant ADM phase, 3–6 questions to inject into phase interviews, each with output routing (target artifact/register).
5. **`## Tagging Conventions`** — how findings become engagement items: REQ-NNN (`source: {framework}`, pillar reference), RIS-NNN, GAP-NNN, or PAD-NNN.

## Consumption Points

**1. `/ea-grill --skill {short-name}` (artifact review):** load the lens reference; for each pillar whose ADM Mapping includes the artifact's phase, walk the Review Checklist against the artifact. Report per pillar: `✅ Addressed / ⚠️ Partial / 🔴 Not addressed / ➖ Not applicable`, with findings and suggested REQ/RIS/GAP captures per the Tagging Conventions. Same session flow as other grill skills (one area at a time; offer to apply findings).

**2. Phase interview injection (`/ea-interview start phase`):** after the question bank's optional Security Questions, offer: *"Apply a framework lens to this phase? Available: {lenses from the registry whose Interview Questions cover the current phase}. (lens name / n)"* If accepted, load the lens reference and ask its Interview Questions for the current phase, routing answers per the lens's routing tables. Offer in phases C-Data, C-App, D, E for workload-pillar lenses (`waf`, `gcaf`) and additionally A, B, F for adoption-lifecycle lenses (`caf`). Skip the offer silently if the engagement has no cloud or infrastructure scope signals (no cloud-related drivers, constraints, SBBs, or technology choices).

**3. Direct consultation:** when the user asks "what does {framework} say about X", load the lens reference and answer from it, citing the pillar.

## Adding a New Lens

1. Author `references/{lens-name}.md` following the Lens File Contract.
2. Add a row to the Lens Registry above.
3. Add a row to the `/ea-grill` skill table (`commands/ea-grill.md`) pointing at the reference file.
4. No other wiring needed — interview injection and direct consultation read the registry.

## Boundaries

- A lens never overrides TOGAF artifacts or the ID scheme — findings land in existing registers (REQ/RIS/GAP/PAD), never in framework-specific stores.
- Lens checklists are review aids, not compliance tiers — they do not participate in T1–T4 compliance rules.
- Vendor-specific guidance belongs at the SBB level; ABBs stay vendor-neutral even under a cloud lens.
