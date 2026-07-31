---
name: ea-objectives
description: Manage objectives — list, add, update, trace to goals, problems, and metrics, and generate an Objectives Register
argument-hint: "[list|add|update|trace|generate] [OBJ-NNN] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-objectives` command. All mode mechanics (engagement resolution, ID assignment, list/add/update/trace/generate flows, common edge cases) follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Objective concept and its distinctions from Goal/Metric/Problem, read `skills/ea-artifact-templates/references/concept-families/motivation-concepts.md` (**Objective**); do not restate definitions here.

Objectives operationalise goals (DRV → G → **OBJ**): each is a specific, measurable, time-bound result with a unit of measure, a target value, and a deadline. Every objective must link to exactly one goal; Problems block objectives; Metrics (MET-NNN) track them. The **Objectives Register** is the management interface; the Architecture Vision (§10) summarises and links to it rather than rendering a live table.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `OBJ-NNN` — Objective |
| Storage | `engagement.json → direction.objectives[]` |
| Register file | `artifacts/cross-cutting/objectives-register.md` (artifactId `objectives-register`; relatedArtifacts `["architecture-vision"]`) |
| Seed template | `templates/phase-a/objectives-register.md` (scored artifact; `generate` fills its Summary + per-goal item blocks) |
| Groupings | `list` and `generate` group by Linked Goal (orphans last); summary counts by Priority, plus "Orphans (no linked goal)" and "Not measurable (missing measure, target, or deadline)" |
| Orphan rule | No `linkedGoal` → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | The specific, measurable result (e.g. "Reduce mobile checkout page load time to under 2 seconds") | any string | ✓ |
| `measure` | Unit of measure — what is counted or measured? (e.g. "p95 page load time in seconds") | any string | ✓ |
| `target` | Target value the measure must reach (e.g. "< 2.0s") | any string | ✓ |
| `deadline` | When must the target be reached? | date or quarter (e.g. "2027-Q2") | ✓ |
| `priority` | Priority | High / Medium / Low | ✓ |
| `linkedGoal` | Which goal does this objective operationalise? (list available G-NNN) | single G-NNN | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `linkedGoal` | `direction.goals[]` | No goals exist → orphan flag: "run `/ea-goals add` to capture goals first" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Goal (show Priority) | `direction.goals[]` matching `linkedGoal` |
| Upstream | Drivers (contextual) | the linked goal's `drivers` field |
| Lateral | Problems blocking this objective | `direction.problems[]` where `blocksObjectives` contains this OBJ-NNN |
| Downstream | Metrics tracking this objective (show Baseline, Target, Status) | `metrics[]` where `linkedTo` contains this OBJ-NNN |
| Downstream | Work Packages | Architecture Roadmap WP rows where `Advances Goals/Objectives` references this OBJ-NNN |

Objectives have no status field — achievement is tracked through linked Metrics (MET-NNN status: On Track / At Risk / Behind / Achieved).

## Register-Specific Checks

**Goal disambiguation (post-prompt, add):** If the statement contains no number, percentage, or deadline, warn:

```
⚠️  Your statement looks qualitative.
Objectives are measurable; Goals are qualitative. Consider:
- Goal: "{statement}" (add with /ea-goals add)
- Objective: a measurable milestone under that goal, with measure, target, and deadline
Proceed with the statement as an objective? (y/n)
```

**Measurability flag (post-prompt, add; also flag in `list` with `⚠️ Not measurable`):** If `measure`, `target`, or `deadline` was skipped, warn:

```
⚠️  This objective is missing {measure / target / deadline}.
An objective without all three cannot be verified as achieved.
Capture it now, or proceed and complete later via /ea-objectives update? (capture/proceed)
```

## Messages

- **Empty state:** "No objectives found. Capture objectives during Phase A interviews (`/ea-interview start phase A`) or `/ea-brainstorm`, then add them with `/ea-objectives add`."
- **Add success:** "OBJ-NNN added to engagement.json. Run `/ea-objectives generate` to refresh the Objectives Register, use '/ea-objectives trace OBJ-NNN' to verify the goal linkage, and add a tracking metric in Architecture Vision §11 Key Metrics."
- **Orphan nudge:** "⚠️ No goal linked. Run `/ea-goals list` to see available goals, then `/ea-objectives update OBJ-NNN linkedGoal G-NNN`."
