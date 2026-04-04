# Facilitator Configuration Reference

## Settings File

Read plugin settings from `.claude/ea-assistant.local.md`. All fields are optional — unset fields use the defaults shown.

```yaml
# Path to shared requirements folder (synced to engagement.json on /ea-new)
requirementsRepoPath: /path/to/shared/requirements-folder

# Overall tone and pacing for interviews and phase facilitation
# patient   — explain each question, offer examples, check understanding, probe gently on short answers
# direct    — ask, record, move on; minimal preamble or acknowledgement
# executive — outcome-framing, no TOGAF jargon, offer to skip detail, checkpoint every 5-7 questions
facilitatorStyle: patient

# Primary audience level — adjusts terminology and depth
# executive  — business outcomes only, no TOGAF terms unless user introduces them
# architect  — full TOGAF/ArchiMate vocabulary, technical depth expected
# technical  — system-level language, implementation focus
# mixed      — default; adapt language to the question context
audienceLevel: mixed

# Ask "Shall I record that?" before writing any answer to an artifact
requireConfirmBeforeRecord: false

# Show @research-agent reminder prompts when a driver, risk, or assumption could benefit from validation
researchPrompts: true

# Auto-summarise topics and themes at the end of every interview session
sessionSummary: true
```

All commands and agents that conduct interviews or facilitate phases MUST read this file at startup and apply the active style. If the file does not exist or `facilitatorStyle` is unset, default to `patient`.

## Style Behaviour Reference

| Behaviour | `patient` (default) | `direct` | `executive` |
|---|---|---|---|
| **Question preamble** | One sentence on why the question matters | Question only | Business-outcome framing; no TOGAF terms |
| **Answer acknowledgement** | Brief and warm ("Got it — that helps establish…") | None | None |
| **Short answer probe** | One gentle follow-up if answer is very brief | Accept as-is | Accept as-is |
| **Examples** | Offered proactively | On request only | On request only |
| **Section transitions** | "Anything else before we move on?" | None | None |
| **Checkpoints** | After each major section | None | Every 5–7 questions: "Pause here or continue?" |
| **Jargon** | TOGAF terms with plain-English gloss on first use | Full TOGAF vocabulary | Avoid TOGAF; use business language |
| **Session summary** | Full — counts, key themes, next step | Counts + next step | Key decisions + next step |

## Audience Level Reference

| Level | Adjustments |
|---|---|
| `executive` | Say "direction-setting" not "Phase A"; say "architecture document" not "Architecture Vision"; focus on outcomes and decisions |
| `architect` | Full TOGAF phase/artifact names; ArchiMate references; assume ADM familiarity |
| `technical` | System names, integration patterns, implementation detail expected; less business framing |
| `mixed` | Plain language by default; introduce TOGAF terms once with a brief gloss; adapt as conversation reveals expertise |

## Other Config Options

- **`requireConfirmBeforeRecord: true`** — after every answer, show: `"Record this? (y / edit / skip)"` before writing to the artifact
- **`researchPrompts: true`** — when a driver, risk, assumption, or technology claim is recorded, show: `💡 Consider validating with @research-agent before finalising.`
- **`sessionSummary: true`** — after session completion, display topics covered, answers recorded, and key themes. Set `false` to suppress (next step is always shown regardless)
