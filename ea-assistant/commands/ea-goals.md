---
name: ea-goals
description: Manage goals — list, add, update, trace to drivers and objectives, and generate a Goals Register
argument-hint: "[list|add|update|trace|generate] [G-NNN] [--domain Business|Technology|Data|Application|Cross-cutting] [--type Strategic|Operational|Capability|Compliance] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-goals` command. All mode mechanics (engagement resolution, ID assignment, list/add/update/trace/generate flows, common edge cases) follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Goal concept and its distinctions from Driver/Objective/Strategy, read `ea-concepts.md`; do not restate definitions here.

Goals sit in the middle of the motivation chain (DRV → **G** → OBJ → WP). Every goal must trace to at least one Business Driver; every goal should be operationalised by at least one Objective. Goals appear in Architecture Vision §3 — the register is the management interface; Architecture Vision is the primary display view.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `G-NNN` — Goal |
| Storage | `engagement.json → direction.goals[]` |
| Register file | `artifacts/cross-cutting/goals-register.md` (artifactId `goals-register`; relatedArtifacts `["architecture-vision"]`) |
| Display view | Architecture Vision `§3 Goals` — columns `ID \| Goal \| Business Driver(s) \| Linked Strategies \| Rationale \| Details` ← `id, statement, drivers, —, rationale` |
| Groupings | `list` and `generate` group by Domain; summary counts by Type, Priority, Status, plus "Orphans (no driver)" and "Not operationalised (no objective)" |
| Orphan rule | No linked drivers AND no linked objectives → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | Qualitative desired future state — no measures or deadlines (e.g. "Achieve highly resilient platform operations") | any string | ✓ |
| `domain` | Which architecture domain does this goal primarily belong to? | Business / Technology / Data / Application / Cross-cutting | ✓ |
| `type` | What kind of goal is this? | Strategic (organisational direction) / Operational (process/efficiency) / Capability (capability development) / Compliance (regulatory/governance) | ✓ |
| `priority` | Priority | High / Medium / Low | ✓ |
| `status` | Status | Active / Achieved / Superseded (default Active) | ✓ |
| `drivers` | Linked Drivers (list available DRV-NNN) | comma-separated DRV-NNN | opt |
| `rationale` | Why is this a goal for this engagement? What happens if not achieved? | any string | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `drivers` | `direction.drivers[]` | No drivers → orphan flag: "run `/ea-drivers add` to capture drivers first" |
| (derived) objectives | `direction.objectives[]` where `linkedGoal` = this ID | No objectives → "use `/ea-objectives add` to operationalise" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Business Drivers | `direction.drivers[]` where `linkedGoals` contains this G-NNN, plus this goal's `drivers` field |
| Lateral | Issues threatening this goal | `direction.issues[]` where `threatensGoals` contains this G-NNN |
| Downstream | Objectives (show Measure, Target, Deadline) | `direction.objectives[]` where `linkedGoal` = this G-NNN |
| Downstream | Strategies | `direction.strategies[]` where `supports` contains this G-NNN |
| Downstream | Work Packages | Architecture Roadmap WP rows where `Advances Goals/Objectives` references this G-NNN |

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Superseded` | "Superseded by which goal? (G-NNN or press Enter to skip)" |

## Register-Specific Checks

**Two-Layers check (post-prompt, add; also flag in `list` with `⚠️ EA-layer?`):** If the statement contains any of ("governance", "standards", "EA team", "architecture capability", "review process", "approval", "EA function"), warn:

```
⚠️  This statement may describe an EA-layer goal, not a business goal.
Quick test: Would this goal still exist if the EA team were disbanded?
- If yes → proceed (it is a business goal)
- If no → this belongs in the Governance Framework, not the Architecture Vision
Continue as a business goal? (y/n)
```

**Objective disambiguation (post-prompt, add):** If the statement contains a number or deadline, warn:

```
⚠️  Your statement contains what looks like a measure or deadline.
Goals are qualitative; Objectives are measurable. Consider:
- Goal: "{cleaned statement without measure}"
- Objective: "{statement}" (linked to this goal)
Proceed with the statement as-is? (y/n)
```

## Messages

- **Empty state:** "No goals found. Capture goals during Phase A interviews (`/ea-interview start phase A`) or `/ea-brainstorm`, then add them with `/ea-goals add`."
- **Add success:** "G-NNN added. Use '/ea-objectives add' to operationalise this goal with a measurable objective."
- **Orphan nudge:** "⚠️ No drivers linked. Run `/ea-drivers list` to see available drivers, then `/ea-goals update G-NNN drivers DRV-NNN`."
