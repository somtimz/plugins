# Register Snapshot Convention

Generated registers use a **stable, undated filename** — e.g. `goals-register.md`, `risk-register.md`. The current register is always the only register file at its folder level; superseded versions live in a `snapshots/` subfolder.

## Rule

When a register `generate` mode runs and the target register file already exists:

1. Read the existing file's `generated:` frontmatter date (fall back to the file's last-modified date).
2. Move it to a `snapshots/` subfolder **in the same directory**, renamed `{filename-stem}-{YYYY-MM-DD}.md`. If that snapshot name already exists, append `-v2`, `-v3`, etc. Create `snapshots/` if needed.
3. Write the new register to the stable filename.
4. `engagement.json → artifacts[]` keeps a **single entry** pointing at the stable path. Never register snapshot files; if a legacy dated entry exists for this register, update its `file` path to the stable filename instead of adding a new entry.

## Snapshot semantics

Snapshots are point-in-time archives: read-only, excluded from consistency checks, traceability walks, `/ea-publish`, and register `list`/`trace` modes.

## Example layout

```
artifacts/cross-cutting/operations/
├── risk-register.md                  ← current (only register at this level)
└── snapshots/
    ├── risk-register-2026-04-25.md
    └── risk-register-2026-05-03.md
```

## Scope

Applies to all generated registers (goals, drivers, issues, problems, gaps, scenarios, risks, concerns, decisions, ADR, change, ABB, SBB, story, policies, constraints, standards). Does **not** apply to inherently dated documents: ARB minutes, interview notes, grill reviews, briefs, and consolidated reports keep their dated filenames.
