---
name: ea-gaps-management
description: This skill should be used when the user asks to "manage architecture gaps", "add a gap", "promote a gap", "view gaps", "trace a gap to work packages", "update the gap register", or "generate the gap register". Handles the full gap lifecycle from identification through formal promotion, status tracking, and linkage to work packages.
version: 0.9.57
---

# EA Gaps Management

Architecture Gaps Management captures, classifies, traces, and tracks the formal resolution of differences between the as-is (baseline) state and the to-be (target) state across architecture domains. Gaps are identified in Phase B–D artifact gap analysis sections, consolidated in Gap Analysis (Phase E), and addressed through Work Packages in the Architecture Roadmap.

## Relationship with `/ea-trace --gaps`

Two complementary mechanisms exist for working with gaps:

| Mechanism | Purpose | Source |
|---|---|---|
| `/ea-trace --gaps` | Aggregates raw gap prose from artifact text | Artifact files (e.g., "Gap: No API gateway in current state") |
| `/ea-gaps` | Manages formally promoted GAP-NNN entries | `engagement.json → direction.gaps[]` |

Typical workflow: run `/ea-trace --gaps` → identify the most important gaps in artifact prose → `/ea-gaps promote` to formalise them with structured metadata. Both coexist — not all raw gap statements need to be promoted to GAP-NNN entries, only those requiring formal tracking and Work Package linkage.

## Gaps Storage

Formally promoted gaps are stored in `engagement.json → direction.gaps[]`:

```
engagement.json
└── direction
    └── gaps[]          # formally promoted GAP-NNN entries (source of truth)
```

The gap register file (`artifacts/cross-cutting/gap-register.md`) is generated output only — never edited directly. Superseded versions are archived to `snapshots/` per the register snapshot convention.

## Gap Schema

```json
{
  "id": "GAP-NNN",
  "statement": "",
  "domain": "Business | Data | Application | Technology | Capability | Process",
  "severity": "Critical | High | Medium | Low",
  "baseline": "",
  "target": "",
  "phase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
  "linkedWorkPackages": ["WP-NNN"],
  "linkedArtifact": "",
  "status": "Open | Mitigated | Closed | Accepted"
}
```

**Field definitions:**
- `statement` — the gap as a clear statement of what is missing between baseline and target
- `domain` — the architecture domain where the gap exists
- `severity` — Critical (blocks delivery or creates major business risk) / High (significant impact on target state) / Medium (notable but manageable) / Low (minor or cosmetic)
- `baseline` — the current/as-is state description
- `target` — the desired/to-be state description
- `phase` — the ADM phase in which this gap was identified
- `linkedWorkPackages` — WP-NNN IDs from the Architecture Roadmap that address this gap
- `linkedArtifact` — artifact ID of the source artifact where the gap was documented
- `status` — lifecycle status (see below)

## ID Assignment Algorithm

Two ID series are maintained:
- **GAP-NNN** — standard architecture gaps (all phases except F and G)
- **GAP-M-NNN** — migration gaps (Phase F: Migration Planning; Phase G: Implementation Governance)

**Assignment steps:**
1. Read current `direction.gaps[]`.
2. Filter to the applicable series (GAP-NNN or GAP-M-NNN based on the gap's phase).
3. Find the maximum numeric suffix N in that series.
4. Assign N+1, zero-padded to 3 digits (e.g., next after GAP-003 is GAP-004; next after GAP-M-001 is GAP-M-002).
5. If the series is empty, start at GAP-001 or GAP-M-001.

IDs are assigned once and never reused. If a gap is removed or superseded, its ID remains as a placeholder with `status: Closed` and a note in `statement`.

## Gap Status Lifecycle

```
Open → Mitigated → Closed
     ↘ Accepted (deliberate)
```

| Status | Meaning | Transition condition |
|---|---|---|
| Open | Gap identified; no linked Work Package yet | Initial state on `add` or `promote` |
| Mitigated | Linked to at least one WP in the Architecture Roadmap | Set when `linkedWorkPackages` is populated |
| Closed | WP(s) addressing this gap have been implemented | Set manually when delivery is confirmed |
| Accepted | Deliberately not addressed; risk accepted | Set when organisation decides not to close the gap |

Auto-transition: when `linkedWorkPackages` is populated via `update`, suggest setting `status: Mitigated` if current status is Open.

## Severity Escalation Rule

When saving or updating a gap, apply this check:

```
IF severity = Critical
AND status = Open
AND linkedWorkPackages is empty
THEN surface warning:
"⚠️ GAP-NNN: Critical gap with no linked Work Packages.
 Add a WP: /ea-gaps update GAP-NNN linkedWorkPackages WP-NNN
 Or accept deliberately: /ea-gaps update GAP-NNN status Accepted"
```

The warning is advisory — it does not block the save.

## Gap Register Format

`artifacts/cross-cutting/gap-register.md` uses this structure:

```markdown
---
artifact: Gap Register
artifactId: gap-register
engagement: {name}
phase: All
status: Draft
generated: {YYYY-MM-DD}
---

# Gap Register — {engagement name}

**Generated:** {YYYY-MM-DD}  |  **Total Gaps:** {N}  |  **Unaddressed:** {N}

---

## Architecture Gaps (GAP-NNN)

### GAP-NNN: {first 60 chars of statement}

| Field | Value |
|---|---|
| **ID** | GAP-NNN |
| **Statement** | {statement} |
| **Domain** | {domain} |
| **Severity** | {severity} |
| **Baseline** | {baseline} |
| **Target** | {target} |
| **Phase Identified** | {phase} |
| **Linked Work Packages** | {WP-NNN list or "—"} |
| **Linked Artifact** | {linkedArtifact or "—"} |
| **Status** | {status} |

---

## Migration Gaps (GAP-M-NNN)

{Same H3 structure per GAP-M-NNN, or "No migration gaps recorded." if empty}

---

## Summary

| Domain | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| Business | {N} | {N} | {N} | {N} | {N} |
| Data | {N} | {N} | {N} | {N} | {N} |
| Application | {N} | {N} | {N} | {N} | {N} |
| Technology | {N} | {N} | {N} | {N} | {N} |
| Capability | {N} | {N} | {N} | {N} | {N} |
| Process | {N} | {N} | {N} | {N} | {N} |

> Raw gap statements in artifact prose can be promoted to formal GAP-NNN entries using `/ea-gaps promote`.
```

## Traceability

Gaps trace:
- **Upstream** — to the artifact that identified the gap (`linkedArtifact`) and the ADM phase
- **Downstream** — to Work Packages (`linkedWorkPackages`) that address the gap in the Architecture Roadmap

The `/ea-engage-review` command checks for Critical/High gaps with no linked Work Packages and flags them in the Alignment dimension report.
