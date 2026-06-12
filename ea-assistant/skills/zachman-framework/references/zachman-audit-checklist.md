# Zachman Diagram Audit Checklist

Single source of truth for Zachman Diagram quality auditing. Consumed by:
- `/ea-zachman audit` — standalone audit mode
- `/ea-grill` — Zachman Diagram grilling block in `skills/ea-grill-skills/SKILL.md`

Neither entry point restates these checks — both execute this checklist by reference.

The audit targets the most recent `artifacts/cross-cutting/context/zachman-diagram-*.md`. It complements (does not replace) `/ea-zachman review` and `gap`, which measure cell *presence*; this checklist measures cell *quality* — honesty, coherence, currency, scope, and perspective purity.

Every check yields one of: ✅ pass · ⚠ fail · ❓ unverifiable (insufficient information to confirm or deny).

---

## Check Categories

### 1. Cell honesty

For every cell marked ✅ in the Coverage Summary:
- The cell section has at least 2 substantive bullets (a bullet restating the cell name or containing only an ID is not substantive).
- The cell cites at least one source reference (artifact name or path).
- Overstated coverage: a ✅ cell failing either test is flagged — "Coverage overstated: R{N},C{N} marked ✅ but {reason}."

For every cell marked ⚠️: the cell text states what is missing (not just partial content with no annotation).

For every non-❌ cell: no placeholder text — `TBD`, `TODO`, `⚠️ Not answered`, `⊘`.

### 2. Row refinement

For each column with two or more vertically adjacent populated cells, R(N) content must be a traceable refinement of R(N−1). Verify by opening the contributing source artifacts (per `references/cell-extraction-map.md`), not just the grid text:
- R3,C1 logical entities trace to R2,C1 conceptual entities (compare against Data Architecture conceptual vs logical model sections).
- R3,C2 application components/services trace to R2,C2 capabilities or processes (compare against Application Architecture and Business Architecture).
- R4,Cx technology content traces to R3,Cx logical content (compare against Technology Architecture vs Application/Data Architecture).
- Flag: "Refinement break: R{N},C{N} introduces {element} with no antecedent in R{N−1},C{N}."

### 3. Column consistency

- Every ID cited in any cell (CAP-NNN, REQ-NNN, ROLE-NNN, ABB-NNN, SBB-NNN, VS-NNN, G-NNN, …) exists in its register or source artifact. Dangling IDs are flagged High.
- The same element is named identically wherever it appears across cells (e.g. a capability named "Order Management" in R2,C2 must not appear as "Order Mgmt Service" in R3,C2 without an explicit mapping note).
- No two cells claim contradictory facts about the same element (e.g. an application listed as retired in one cell and as target-state in another).

### 4. Staleness

- Read the diagram's generation date (filename `zachman-diagram-{YYYY-MM-DD}.md` or frontmatter).
- For each contributing artifact in `references/cell-extraction-map.md`, compare its `lastModified` (frontmatter; file mtime as fallback) against the diagram date.
- Flag each cell whose sources changed after generation: "Stale: R{N},C{N} — {artifact} modified {date}, after diagram generation."
- If stale cells exceed one third of populated cells, the overall verdict becomes **Stale** and the primary recommendation is `/ea-zachman generate` before any cell-level fixes.

### 5. Scope honesty

- Every 🚫 cell must be justified by `engagement.json → architectureDomains` or a recorded scope decision (Engagement Charter scope section, or an A3 entry). Unjustified 🚫 in an in-scope domain is flagged High.
- An in-scope domain with an entire row or column marked 🚫 is flagged High: "Whole {row/column} excluded but domain {name} is in scope."

### 6. Perspective purity (primitive model fit)

One cell = one primitive model. For each populated cell, compare its content against the `Expected Model:` line for that cell in `references/zachman-cell-descriptions.md`:
- Content belonging to a lower row's perspective in an upper row is flagged (e.g. physical schema details in R2,C1; vendor product names in R2,C2).
- Content belonging to an upper row in a lower row is flagged (e.g. business goal prose in R4,C6).
- A bundle artifact (e.g. Architecture Definition Document) cited as a source is acceptable only if the cell's extracted content is the separable primitive model — citing the bundle with no extracted model content is flagged.
- Flag: "Perspective mix: R{N},C{N} contains {description} which belongs to R{M} ({expected model})."

---

## Severity Assignment

| Severity | Findings |
|---|---|
| High | Overstated ✅ cells; contradictory claims; dangling IDs; unjustified 🚫 in in-scope domains; whole in-scope row/column excluded |
| Medium | Missing source references; refinement breaks; stale cells; perspective mixing; bundle cited without separable model |
| Low | Naming drift without contradiction; thin ⚠️ annotations |

All findings in R5/R6 default to Low regardless of category — those rows describe implementation and operational reality usually outside documentation scope (consistent with `/ea-zachman gap` severity rules).

---

## Report Format

Both entry points render this structure (grill additionally feeds findings into its own scorecard and verdict):

```
ZACHMAN AUDIT — {engagement name}
Diagram: {filename} (generated {date})  |  Audited: {YYYY-MM-DD}
════════════════════════════════════════════════════

Category scorecard
──────────────────────────────────────────────────
1. Cell honesty          ✅ {n}  ⚠ {n}  ❓ {n}
2. Row refinement        ✅ {n}  ⚠ {n}  ❓ {n}
3. Column consistency    ✅ {n}  ⚠ {n}  ❓ {n}
4. Staleness             ✅ {n}  ⚠ {n}  ❓ {n}
5. Scope honesty         ✅ {n}  ⚠ {n}  ❓ {n}
6. Perspective purity    ✅ {n}  ⚠ {n}  ❓ {n}

Findings — High
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Findings — Medium
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Findings — Low
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Verdict: {Ready | Needs revision | Stale}
```

**Verdict rules:** **Ready** — no High findings. **Needs revision** — one or more High findings. **Stale** — stale cells exceed one third of populated cells (overrides the other two; fix currency first).
