# Cross-Cutting Classification and Decision Artefacts


### Zachman Diagram

**Purpose:** A cross-cutting classification artifact that maps the engagement's architecture content across the 6×6 Zachman Framework grid (rows: Contextual through Functioning; columns: What / How / Where / Who / When / Why). Serves three purposes: (1) coverage tracking — shows which cells are populated, partial, or empty; (2) stakeholder communication — each row targets a different audience; (3) traceability — each populated cell references its source artifact and section.

**Audience:** Architecture team, Lead Architect, Architecture Review Board, programme governance, and stakeholder-specific rows for executive (R1), business owner (R2), or technical (R3–R4) audiences.

**Contents:**
- Coverage summary table (6×6 grid with ✅/⚠️/❌ per cell)
- Row 1 — Contextual (Executive / Planner): scope, boundary, key players
- Row 2 — Conceptual (Business Owner): semantic model, business processes, organisation, strategy
- Row 3 — Logical (Architect / Designer): logical data, application functions, distribution, rules
- Row 4 — Physical (Builder / Developer): physical data, system design, infrastructure, rule implementation
- Row 5 — Detailed (Implementer): references to delivery artefacts (out of EA scope)
- Row 6 — Functioning Enterprise: observed reality (not modelled in advance)
- Gap Analysis table (empty cells with recommended remediation)
- Appendix A5 — Related Architecture Decisions

**When to Create:** After Phase A is complete (sufficient content for R1–R2 contextual and conceptual cells). Update at each phase gate as new architecture content is produced. Use `/ea-zachman generate` to auto-populate from existing artifacts, or `/ea-zachman interview` to fill cells via guided Q&A.

**Who Reviews:** Lead Architect (coverage completeness), Architecture Review Board (stakeholder-row alignment).

**Phase:** Cross-cutting — created incrementally from Phase A through Phase D.

**Template:** `zachman-diagram.md` — managed by `/ea-zachman`.

---
