---
name: ea-problems
description: Manage architecture problems — list, add, update, trace to objectives and requirements, and generate a Problems Register
argument-hint: "[list|add|update|trace|generate] [PRB-NNN] [--domain Business|Technology|Data|Application|Engagement] [--type Operational|Technical|Data|Engagement|Compliance] [--severity Critical|High|Medium|Low] [--status Open|In Progress|Resolved]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-problems` command. All mode mechanics follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Problem concept and its distinctions from Issue/Risk/Gap/Constraint, read `ea-concepts.md`; do not restate definitions here.

Problems are specific, observable, fixable symptoms actively blocking objectives — certain and present, with a measurable symptom. They appear in Architecture Vision §6 — the register is the management interface; Architecture Vision is the primary display view. The **Engagement** domain covers problems with the EA engagement itself (methodology, governance, team, tooling).

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `PRB-NNN` — Problem |
| Storage | `engagement.json → direction.problems[]` |
| Register file | `artifacts/cross-cutting/problems-register.md` (artifactId `problems-register`; relatedArtifacts `["architecture-vision"]`) |
| Display view | Architecture Vision `§6 Problems` — columns `ID \| Problem \| Observable Symptom \| Blocks Objective(s) \| Evidence \| Raised By \| Details` ← `id, statement, symptom, blocksObjectives, evidence, raisedBy` |
| Groupings | `list` and `generate` group by Domain (Engagement first, then Business, Technology, Data, Application); summary counts by Severity, Status, plus "No evidence" and "No objectives" |
| Orphan rule | No linked objectives → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | Name the specific problem — observable and fixable (e.g. "Mobile checkout page load time averages 8.2 seconds") | any string | ✓ |
| `symptom` | Observable Symptom — what can be seen or measured today, ideally a number (e.g. "68% cart abandonment on mobile due to slow load") | any string | ✓ |
| `domain` | Which area is primarily affected? | Business / Technology / Data / Application / Engagement | ✓ |
| `type` | Category | Operational / Technical / Data / Engagement / Compliance | ✓ |
| `severity` | Severity | Critical / High / Medium / Low | ✓ |
| `status` | Status | Open / In Progress / Resolved (default Open) | ✓ |
| `blocksObjectives` | Which objectives is this problem preventing? (list available OBJ-NNN; if none exist: "No objectives captured yet — add objectives with '/ea-objectives add' after this step") | comma-separated OBJ-NNN | ✓ (recommended) |
| `evidence` | Data point, incident, or measurement confirming the symptom is currently active | any string | ✓ (recommended) |
| `raisedBy` | Stakeholder or source that identified this problem | any string | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `blocksObjectives` | `direction.objectives[]` | No objectives → "if it cannot be linked to an objective, it may be out of scope"; emptying via update warns "makes this problem out-of-scope" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Related Issues (systemic patterns this problem contributes to) | `direction.issues[]` sharing threatened goals with this problem's blocked objectives |
| Blocks | Objectives (show Target, Deadline, parent Goal) | `direction.objectives[]` matching `blocksObjectives` |
| Upstream (via objectives) | Goals at risk | parent goals of the blocked objectives |
| Downstream | Architecture Requirements derived from this problem | `artifacts/**/requirements*.md` REQ rows referencing PRB-NNN; if none: "⚠️ No requirements — consider creating REQ-NNN entries to address this problem" |

Chain status labels: `✅ Addressed | ⚠️ Partial | 🔴 Orphan`.

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Resolved` | "Resolution summary (optional):" |

## Register-Specific Checks

**Problem vs Issue disambiguation (pre-add):**

```
Is this concern specific, observable, and directly fixable?
Or is it a broader, systemic pattern with multiple contributing causes?

(p) Problem — specific, observable, fixable, blocks a particular objective
(i) Issue — systemic, broad, multiple causes, sustained response needed
```

If (i): "Routing to `/ea-issues add` — use Issues for systemic, broad concerns that threaten goals." Stop.

**Systemic check (post-prompt, add):** If the statement uses plural broad terms ("architecture", "culture", "all systems", "consistently", "always"), warn:

```
⚠️  Your statement sounds systemic — it may describe a pattern rather than a specific event.
Problems are specific and fixable. Issues are systemic and broad.
Example of a Problem: "Payment API returns HTTP 500 errors 3× per week on average"
Example of an Issue: "Integration architecture lacks resilience and monitoring"
Proceed as a Problem? (y/n)
```

**Escalation flag (`list`):** "🔴 {N} critical/high problem(s) are unresolved — consider creating architecture requirements to address them."

## Messages

- **Empty state:** "No problems found. Capture problems during interviews or `/ea-brainstorm`, then add them with `/ea-problems add`."
- **Add success:** "PRB-NNN added. Consider creating a REQ-NNN requirement to address this problem: '/ea-requirements add'."
- **Orphan nudge (no objectives exist yet):** "⚠️ No objectives captured yet. Problems should block specific objectives. After capturing objectives with '/ea-objectives add', link this problem: /ea-problems update PRB-NNN blocksObjectives OBJ-NNN"
- **No-evidence flag:** "⚠️ {N} problem(s) have no evidence — problems without a measurable symptom cannot be prioritised."
