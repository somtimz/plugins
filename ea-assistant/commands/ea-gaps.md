---
name: ea-gaps
description: Manage architecture gaps — list, add, promote from raw gap text, update, trace to work packages, and generate a gap register
argument-hint: "[list|add|promote|update|trace|generate] [GAP-NNN] [--domain Business|Data|Application|Technology|Capability|Process] [--severity Critical|High|Medium|Low] [--status Open|Mitigated|Closed|Accepted] [--phase A|B|C|D|E|F|G|H]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-gaps` command. Load the `ea-gaps-management` skill for schema, lifecycle, and escalation detail. All mode mechanics follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Gap concept, read `ea-concepts.md`; do not restate definitions here.

This command manages formally promoted `GAP-NNN` entries. It complements `/ea-trace --gaps`, which aggregates raw gap prose from artifact text: discover gap statements there, then `/ea-gaps promote` to formalise the important ones.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `GAP-NNN` — Architecture Gap; `GAP-M-NNN` — Migration Gap. Series rule: active phase F or G → GAP-M series, otherwise GAP series |
| Storage | `engagement.json → direction.gaps[]` |
| Register file | `artifacts/cross-cutting/gap-register.md` (artifactId `gap-register`; frontmatter `phase: All`). Body has two sections — Architecture Gaps (GAP-NNN) and Migration Gaps (GAP-M-NNN, or "No migration gaps recorded.") — plus a Domain × Severity summary matrix and the hint: "Raw gap statements in artifact prose can be promoted with `/ea-gaps promote`." |
| Groupings | `list` groups by Severity (Critical first); summary counts by Status and Domain, plus "Unaddressed: {N} Critical/High gap(s) with no linked Work Packages" |
| Orphan rule | Severity Critical/High AND Status Open AND no linked WPs → `⚠️ Unaddressed` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | The gap — what is missing between baseline and target | any string | ✓ |
| `domain` | Domain | Business / Data / Application / Technology / Capability / Process | ✓ |
| `severity` | Severity | Critical / High / Medium / Low | ✓ |
| `baseline` | Current/as-is state description | any string | ✓ |
| `target` | Desired/to-be state description | any string | ✓ |
| `phase` | Which ADM phase this gap was identified in | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements | ✓ |
| `linkedWorkPackages` | Linked Work Packages | comma-separated WP-NNN | opt |
| `linkedArtifact` | Artifact ID where the gap appears | artifact ID string | opt |

New gaps get `status: Open`. Status values: Open / Mitigated / Closed / Accepted (lifecycle in `ea-gaps-management`).

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `linkedWorkPackages` | Architecture Roadmap WP rows | WP IDs not found in the roadmap → "⚠️ WP not found in Architecture Roadmap" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Source artifact + phase identified | `linkedArtifact`, `phase`; scan `direction` for REQ-NNN free-text matches on the statement |
| Downstream | Work Packages (show wave, priority, delivery status) | Architecture Roadmap rows for each `linkedWorkPackages` ID |

Close single-gap trace with: `⚠️ Unaddressed critical gap — no linked Work Packages` or `✅ Covered by {N} Work Package(s)`.

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Accepted` on a Critical gap | "Accepting a Critical gap without a linked Work Package means this gap is acknowledged but will not be addressed. Confirm? (y/n)" |
| `status: Closed` | Confirm the WP(s) have been delivered: "Mark as Closed only when the work package(s) addressing this gap have been implemented." |
| Emptying `linkedWorkPackages` on a Mitigated gap | "Removing all Work Packages will revert status to Open. Continue? (y/n)" — if yes, also set `status: Open` |

## Mode: `promote` (register-specific)

Promotes a raw gap statement into a formal GAP-NNN entry (typically after `/ea-trace --gaps`):

1. Ask: "Paste the raw gap statement to promote (or describe the gap):"
2. If multiple gaps are pasted: "I see {N} gap statements. Promote them one at a time? (y/n)" — if yes, loop.
3. For each, run the standard `add` flow with `statement` pre-filled from the pasted text.
4. Confirm: "GAP-NNN promoted from raw gap text. Run `/ea-gaps trace GAP-NNN` to link it to a Work Package."

## Register-Specific Checks

**Severity escalation (on add and update — see `ea-gaps-management` for the full rule):** if severity = Critical, status = Open, and no linked WPs, warn: "⚠️ This is a Critical gap with no linked Work Package. Add a WP with `/ea-gaps update GAP-NNN linkedWorkPackages WP-NNN` or accept the gap deliberately." Advisory — does not block the save.

## Messages

- **Empty state:** "No gaps recorded. Discover raw gap statements with `/ea-trace --gaps`, then formalise them with `/ea-gaps promote`, or add one directly with `/ea-gaps add`."
- **Add success:** "GAP-NNN added. Use `/ea-gaps trace GAP-NNN` to check work package linkage."
- **Unaddressed flag (`list`):** "⚠️ {N} unaddressed Critical/High gap(s) — no linked Work Packages. Run `/ea-gaps trace` to review."
