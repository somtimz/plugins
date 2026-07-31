Decision: Add Business Context (CTX-NNN) and Business Model Canvas (BMC-NNN) as first-class EA concepts and update the unified ID scheme, templates, commands, and README to align with a four-concept business-layer model (Business Context / Business Model Canvas / Business Architecture / Operating Model).

Context: The plugin previously treated Operating Model as a first-class Phase B artifact and split Business Architecture from Operating Model, but Business Context and Business Model Canvas were implicit or subsumed under Business Architecture. Stakeholder confusion about where external-analysis findings and value-model content belong was surfacing. The user asked for a full conceptual alignment across `ea-concepts.md`, README, grill/review commands, other commands, agents, and skills.

Alternatives considered:
- Absorb Business Context into the Drivers Register and Business Model Canvas into the Business Architecture artifact only. Rejected because it loses traceability from raw analysis (PESTEL/SWOT) to derived direction and governance items, and it hides the value-model layer between strategy and capability design.
- Introduce domain-prefixed IDs (e.g., BG- for business goal). Rejected: the ID scheme is deliberately unified and domain-agnostic, and the CLAUDE.md explicitly forbids domain-prefixed IDs.
- Keep BMC elements in existing registers only (SVC, VS, CAP, FIN) without a BMC-NNN detail prefix. Rejected because the Business Model Canvas is a coherent authored artifact; BMC-NNN detail files capture canvas-specific elements, assumptions, and pivot hypotheses that do not cleanly belong in other registers.

Reasoning:
- Business Context is an analysis discipline, not a motivation item. It produces findings that become drivers, issues, opportunities, policies, and constraints. A dedicated CTX-NNN prefix makes traceability explicit.
- Business Model Canvas sits between strategy and business architecture/operating model. It describes value creation, delivery, and capture; its nine blocks map cleanly to existing registers (SVC/VS, CAP, FIN, Stakeholder Map). BMC-NNN detail files hold canvas-specific elements and assumptions.
- The four-concept split (Context / Value Model / Blueprint / Operating Model) gives Phase B a clear conceptual home for ambiguous content and matches how senior stakeholders think.
- Updating the source of truth (`ea-concepts.md`) first, then cascading to ID scheme, commands, templates, and README, keeps the plugin internally consistent.

Trade-offs accepted:
- BMC-NNN and CTX-NNN add two new ID families to manage. To keep the bar low, they are optional detail-file prefixes; the core registers (drivers, issues, opportunities, etc.) remain the primary motivation/governance IDs.
- `engagement.json` does not gain new top-level arrays for `businessContext` or `businessModelCanvas` in this pass; CTX/BMC detail files live in `artifacts/details/` and are linked from artifact sections. A future decision can add arrays if register-protocol automation requires it.
- README and `ea-help.md` counts increase from 33 to 35 concepts, which may require readers to relearn the summary number.

Supersedes: None.
