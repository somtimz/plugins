# Skill Contract: SKILL.md Frontmatter

All skills MUST include valid YAML frontmatter with these required fields.

## itil-change-request

```yaml
---
name: itil-change-request
description: >
  Launch an interactive ITIL v4-compliant Change Request management app.
  Use this skill whenever the user wants to create, edit, or manage IT
  change requests for CAB approval. Triggers include: "change request",
  "CAB submission", "RFC", "request for change", "change management",
  upgrading servers/databases/applications, infrastructure changes,
  patch deployments, software rollouts, or any request where an IT team
  needs formal approval.
version: 0.1.0
---
```

**Behavior**: Read `references/cr-app.jsx` and present as React JSX artifact.

## cab-review

```yaml
---
name: cab-review
description: >
  Launch the CAB (Change Advisory Board) admin review tool. Use this
  skill when an administrator wants to review pending change requests,
  approve or reject them, or check what CRs are awaiting CAB decision.
  Triggers include: "cab review", "review change requests", "approve
  change requests", "pending approvals", "CAB admin".
version: 0.1.0
---
```

**Behavior**: Read `references/cab-review-app.jsx` and present as React JSX artifact.

## Command Contract

Commands are thin wrappers. Each `.md` file in `commands/` has frontmatter:

```yaml
---
name: <command-name>
description: <one-line description>
---
```

Body: Single instruction to launch the corresponding skill.
