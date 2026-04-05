---
name: ea-next
description: Suggest the single most valuable next action for the active EA engagement based on current phase, artifact status, and engagement health
allowed-tools: [Read, Glob]
---

Suggest the best next action for the active EA engagement.

## Instructions

1. **Require active engagement.** Check for `engagement.json` in context. If none, prompt: "No engagement is active. Run `/ea-open` to open one first."

2. **Read engagement state.** From `engagement.json` extract: `currentPhase`, `artifacts[]` (id, phase, status, reviewStatus, file), `phases[]` (phase, status).

3. **Apply the Next Step Algorithm** — evaluate conditions in priority order and stop at the first match:

   | Priority | Condition | Recommendation |
   |---|---|---|
   | 1 | Any artifact in `currentPhase` has `reviewStatus: Needs Revision` | Run `/ea-grill {artifact-id}` to address review findings before proceeding |
   | 2 | `currentPhase` has blocking gate violations — read `skills/ea-engagement-lifecycle/references/phase-constraints.md` for the phase's Blocking Gates and check against artifact statuses | Run `/ea-consistency` — blocking issues found in {phase} must be resolved |
   | 3 | `currentPhase` has artifacts with `status: Draft` — read each draft artifact file and check for unanswered `{{placeholder}}` fields or `⚠️ Not answered` values | Run `/ea-interview {artifact-id}` to complete {N} unanswered fields |
   | 4 | `currentPhase` has no artifacts registered yet | Run `/ea-interview start phase {phase}` to start the phase interview, or `/ea-artifact create` to scaffold artifacts manually |
   | 5 | All artifacts in `currentPhase` have `status: Approved` or `reviewStatus: Approved` | Run `/ea-engage-review` to confirm phase health, then mark phase complete with `/ea-phase` |
   | 6 | No phase has status `In Progress` | Run `/ea-phase {next-phase}` to start the next recommended phase (use the phase order: Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H) |
   | 7 | Glob `artifacts/cross-cutting/zachman-diagram-*.md` returns no results | Run `/ea-zachman generate` to create the Zachman coverage diagram |
   | 8 | No issues found in any of the above | "Engagement looks healthy" |

4. **Output the recommendation:**

   ```
   ## What to do next

   **{one sentence explaining why this is the recommended next step}**

   → `{exact command to run}`

   Want to do something else? Run `/ea-status` for a full dashboard or `/ea-open` for the full next-actions menu.
   ```

   For priority 8 (no issues):
   ```
   ## What to do next

   **Engagement looks healthy — no outstanding gaps or blockers detected.**

   → `/ea-status` for a full dashboard

   Want to go deeper? Run `/ea-engage-review` for a full health check or `/ea-zachman review` for Zachman coverage.
   ```

## Next Step Algorithm Reference

This algorithm is also used by post-command prompts in `/ea-interview`, `/ea-grill`, `/ea-artifact`, and `/ea-zachman`. When those commands ask "Want a next step suggestion?", they apply this same priority order. Keeping the logic here ensures consistency — do not duplicate it inline in those commands; reference this file.
