# Preliminary Phase


### Context Diagram
**Artifact:** Engagement Charter  
**Viewpoint:** ArchiMate — Organisation viewpoint  
**Purpose:** Shows the engagement boundary, affected organisations, and key external relationships.

**Filename:** `engagement-charter-context.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph LR
  subgraph Scope["Engagement Scope"]
    ORG["🏢 Organisation"]
  end
  EXT1["🏢 Partner / Customer"]
  EXT2["⚖️ Regulator"]
  EXT3["🏢 Supplier"]
  EXT1 -- "dependency" --> ORG
  ORG -- "compliance" --> EXT2
  ORG -- "contracts" --> EXT3
```

---

### Organisation Chart
**Artifact:** Engagement Charter  
**Viewpoint:** ArchiMate — Organisation viewpoint  
**Purpose:** Shows the organisational structure and units in scope.

**Filename:** `engagement-charter-org-chart.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph TD
  CEO["👤 CEO / Sponsor"]
  CIO["👤 CIO"]
  BU1["🏢 Business Unit A"]
  BU2["🏢 Business Unit B"]
  EA["👤 Lead Architect"]
  CEO --> CIO
  CEO --> BU1
  CEO --> BU2
  CIO --> EA
```

---
