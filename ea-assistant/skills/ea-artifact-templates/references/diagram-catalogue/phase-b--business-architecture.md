# Phase B — Business Architecture


### Capability Map
**Artifact:** Business Architecture  
**Viewpoint:** ArchiMate — Capability viewpoint  
**Purpose:** Hierarchical map of business capabilities with maturity heat-map colouring.

**Filename:** `business-architecture-capability-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph TD
  L0["🏢 Organisation Name"]
  CAP1["📦 CAP-001\nCapability Domain A"]
  CAP2["📦 CAP-002\nCapability Domain B"]
  CAP3["📦 CAP-003\nCapability Domain C"]
  CAP1A["📦 CAP-004\nSub-Capability A1"]
  CAP1B["📦 CAP-005\nSub-Capability A2"]
  CAP2A["📦 CAP-006\nSub-Capability B1"]
  L0 --> CAP1
  L0 --> CAP2
  L0 --> CAP3
  CAP1 --> CAP1A
  CAP1 --> CAP1B
  CAP2 --> CAP2A
  style CAP1A fill:#ff9999
  style CAP2A fill:#ff9933
  style CAP1B fill:#ffcc66
  style CAP1 fill:#99cc99
```

> Colour guide: 🔴 `#ff9999` = Absent &nbsp; 🟠 `#ff9933` = Immature &nbsp; 🟡 `#ffcc66` = Developing &nbsp; 🟢 `#99cc99` = Mature

---

### Business Process Flow
**Artifact:** Business Architecture  
**Viewpoint:** ArchiMate — Business Process viewpoint  
**Purpose:** End-to-end swimlane for a key business process.

**Filename:** `business-architecture-process-flow.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  subgraph Actor1["Actor / Role A"]
    A1["Start: Trigger"]
    A3["Step 3"]
    A5["End: Outcome"]
  end
  subgraph Actor2["Actor / Role B"]
    A2["Step 2"]
    A4["Step 4"]
  end
  A1 --> A2 --> A3 --> A4 --> A5
```

---

### Organisation Map
**Artifact:** Business Architecture  
**Viewpoint:** ArchiMate — Organisation viewpoint  
**Purpose:** Structural view of teams and roles relevant to the architecture scope.

**Filename:** `business-architecture-org-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph TD
  ORG["🏢 Organisation"]
  DIV1["🏢 Division A"]
  DIV2["🏢 Division B"]
  TEAM1["👥 Team A1"]
  ROLE1["👤 Role A1a"]
  ORG --> DIV1 --> TEAM1 --> ROLE1
  ORG --> DIV2
```

---
