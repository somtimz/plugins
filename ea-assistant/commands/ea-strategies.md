---
name: ea-strategies
description: Manage strategies — list, add, update, trace the Goals→Strategies→Work Packages map, and generate a Strategy Register. Strategies are the chosen approaches ("how") that execute goals and objectives.
argument-hint: "[list|add|update|trace|generate] [STR-NNN] [--type Build|Buy|Partner|Consolidate|Modernise|Defend|Other] [--horizon Near|Mid|Long] [--priority High|Medium|Low] [--status Active|Completed|Superseded]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-strategies` command. All mode mechanics (engagement resolution, ID assignment, list/add/update/trace/generate flows, common edge cases) follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Strategy concept and its distinctions from Goal / Objective / Plan / Principle, read `ea-concepts.md`; do not restate definitions here.

Strategy is the **"how"** in the motivation chain (DRV → G → OBJ → **STR** → WP) — the chosen approach for pursuing goals and objectives. Until now it was the only motivation concept without a register command, so strategies were buried in the direction data. This command surfaces them: every strategy should support at least one goal or objective, and be executed by at least one work package. The **Strategy Register** is the management interface; the Architecture Vision (§11) summarises and links to it rather than rendering a live table. **`trace` (no ID) renders the Strategy Map** — one row per strategy showing the goals it serves and the work packages that execute it.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `STR-NNN` — Strategy |
| Storage | `engagement.json → direction.strategies[]` |
| Register file | `artifacts/cross-cutting/strategy-register.md` (artifactId `strategy-register`; relatedArtifacts `["architecture-vision"]`) |
| Seed template | `templates/phase-a/strategy-register.md` (scored artifact; `generate` fills its Summary + per-type item blocks) |
| Groupings | `list` and `generate` group by Type; summary counts by Horizon, Priority, Status, plus "Orphans (no supported goal/objective)" and "Not executed (no work package)" |
| Orphan rule | No `supports` AND no executing work package → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | The chosen approach — names a path, not an outcome or a sequence of steps (e.g. "Adopt API-first integration across all channels") | any string | ✓ |
| `type` | What kind of approach is this? | Build / Buy / Partner / Consolidate / Modernise / Defend / Other | ✓ |
| `supports` | Goals or objectives this strategy serves (list available G-NNN and OBJ-NNN) | comma-separated G-NNN / OBJ-NNN | opt |
| `horizon` | Over what timeframe does this approach play out? | Near (0–12mo) / Mid (1–2yr) / Long (2yr+) | ✓ |
| `priority` | Priority | High / Medium / Low | ✓ |
| `status` | Status | Active / Completed / Superseded (default Active) | ✓ |
| `rationale` | Why this approach over the alternatives? What "where to play / how to win" choice does it make? | any string | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `supports` | `direction.goals[]` and `direction.objectives[]` | No supported goal/objective → orphan flag: "run `/ea-goals list` / `/ea-objectives list`, then `/ea-strategies update STR-NNN supports G-NNN`" |
| (derived) work packages | Architecture Roadmap WP rows where `Executes Strategies` references this STR-NNN | No executing WP → "not executed by any work package; add it to a WP's `Executes Strategies` in the roadmap" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Goals supported | `direction.goals[]` referenced in this strategy's `supports` |
| Upstream | Objectives supported (show Measure, Target, Deadline) | `direction.objectives[]` referenced in `supports` |
| Lateral | Sibling strategies for the same goal | other `direction.strategies[]` whose `supports` overlaps this one's |
| Downstream | Work Packages executing this strategy (show Wave, Status) | Architecture Roadmap WP rows where `Executes Strategies` references this STR-NNN |

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Superseded` | "Superseded by which strategy? (STR-NNN or press Enter to skip)" |

## Register-Specific Checks

**Goal disambiguation (post-prompt, add; also flag in `list` with `⚠️ goal?`):** If the statement reads as a desired state rather than an approach (starts with or contains "achieve", "become", "improve", "increase", "reduce", "ensure" as the main verb), warn:

```
⚠️  This statement reads like a desired outcome (a Goal), not an approach (a Strategy).
Quick test: does it name a PATH ("adopt X", "consolidate onto Y") or a DESTINATION ("become the most trusted...")?
- Path → Strategy ✓
- Destination → this belongs in /ea-goals
Proceed as a strategy? (y/n)
```

**Objective disambiguation (post-prompt, add):** If the statement contains a number or a deadline, warn it may be an Objective (measurable target), and offer to split: the qualitative approach stays here; the measurable target goes to `/ea-objectives`.

**Plan disambiguation (post-prompt, add):** If the statement describes a sequence ("first", "then", "in Q1/Q2", "phase 1") , warn:

```
⚠️  This describes a sequence of steps (a Plan), not an approach (a Strategy).
A strategy names the approach ("API-first integration"); a plan names the ordered steps to deliver it.
Capture the approach here and let the Architecture Roadmap sequence the work. Proceed? (y/n)
```

## Messages

- **Empty state:** "No strategies found. Capture strategies during Phase A interviews (`/ea-interview start phase A`) or `/ea-brainstorm`, then add them with `/ea-strategies add`. A strategy is the chosen *approach* for achieving a goal — the 'how'."
- **Add success:** "STR-NNN added to engagement.json. Run `/ea-strategies generate` to refresh the Strategy Register, link it to the work packages that execute it via the roadmap's `Executes Strategies` field (`/ea-matrix` or edit the Architecture Roadmap), and confirm it supports a goal with `/ea-strategies trace STR-NNN`."
- **Orphan nudge:** "⚠️ No supported goal/objective. Run `/ea-goals list` (or `/ea-objectives list`) to see what's available, then `/ea-strategies update STR-NNN supports G-NNN`."
