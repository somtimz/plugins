# Diagram Catalogue

Standard diagrams for each EA artifact type. Used by:
- `ea-interviewer` — to prompt for diagrams during and after Q&A sessions
- `ea-brainstorm.md` — to suggest visual capture at close of brainstorm
- `ea-grill.md` — to run Step 8 diagram coverage check
- `ea-diagram` agent — as the reference for standard naming and viewpoints

---

## How to Use This Catalogue

1. **During interview** — at the end of each phase session, present the relevant section and ask: "Which of these diagrams would you like to create now?"
2. **During brainstorm** — at close of session, surface the phase-relevant entries and offer to launch `/ea-diagram`
3. **During grill (Step 8)** — read the artifact's `diagrams:[]` frontmatter and inline refs, compare against the expected diagrams listed here, and report the coverage result
4. **During diagram creation** — use the Mermaid starters below as the initial skeleton; mark all AI-generated content with `%% 🤖 AI Draft — Review Required`

---

## Naming Convention

`{artifact-id}-{diagram-type}.{ext}`

| Ext | Format | When to Use |
|---|---|---|
| `.mmd` | Mermaid source | Primary authoring format; commit to `diagrams/` |
| `.png` / `.svg` | Rendered output | Embedded in exports via `/ea-generate`; regenerated from `.mmd` |
| `.drawio` | Draw.io XML | Complex free-form diagrams or when stakeholders edit in Draw.io |

---

## Preliminary Phase

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

## Phase A — Architecture Vision

### Motivation Map
**Artifact:** Architecture Vision  
**Viewpoint:** ArchiMate — Motivation viewpoint  
**Purpose:** Shows the full DRV → Goal → Strategy chain. Communicates *why* the engagement exists and *how* the organisation intends to respond.

**Filename:** `architecture-vision-motivation-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  DRV1["📌 DRV-001\n{{driver_1}}"]
  DRV2["📌 DRV-002\n{{driver_2}}"]
  G1["🎯 G-001\n{{goal_1}}"]
  G2["🎯 G-002\n{{goal_2}}"]
  STR1["🗺️ STR-001\n{{strategy_1}}"]
  STR2["🗺️ STR-002\n{{strategy_2}}"]
  ISS1["⚠️ ISS-001\n{{issue_1}}"]

  DRV1 --> G1
  DRV2 --> G1
  DRV2 --> G2
  G1 --> STR1
  G2 --> STR2
  ISS1 -. "threatens" .-> G1
```

---

### Stakeholder Power/Interest Grid
**Artifact:** Architecture Vision / Stakeholder Map  
**Viewpoint:** Custom — Stakeholder analysis  
**Purpose:** Positions stakeholders by influence and interest to guide engagement strategy.

**Filename:** `architecture-vision-stakeholder-grid.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Stakeholder Power / Interest Grid
  x-axis Low Interest --> High Interest
  y-axis Low Power --> High Power
  quadrant-1 Manage Closely
  quadrant-2 Keep Satisfied
  quadrant-3 Monitor
  quadrant-4 Keep Informed
  Sponsor: [0.8, 0.9]
  Programme Director: [0.7, 0.75]
  Lead Architect: [0.6, 0.6]
  End Users: [0.5, 0.3]
```

---

## Phase B — Business Architecture

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

## Phase C — Data Architecture

### Conceptual Data Model
**Artifact:** Data Architecture §2  
**Viewpoint:** ArchiMate / ER — Semantic layer  
**Purpose:** Business-readable view of major subject areas and their relationships. No technical attributes.

**Filename:** `data-architecture-conceptual-data-model.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ LINE_ITEM : contains
  PRODUCT ||--o{ LINE_ITEM : includes
  CUSTOMER {
    string name
    string id
  }
  ORDER {
    date orderDate
    string status
  }
```

---

### Data Flow Diagram
**Artifact:** Data Architecture §5  
**Viewpoint:** Custom — Information flow  
**Purpose:** Shows how data moves between systems, highlighting cross-boundary flows and transformation points.

**Filename:** `data-architecture-data-flow.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  SRC1["📦 Source System A"]
  SRC2["📦 Source System B"]
  INT["⚙️ Integration Layer / ETL"]
  TGT1["📦 Target / DWH"]
  TGT2["📦 Analytics Platform"]
  EXT["🌐 External Party"]

  SRC1 -- "batch / nightly" --> INT
  SRC2 -- "real-time" --> INT
  INT -- "cleansed" --> TGT1
  TGT1 -- "aggregated" --> TGT2
  TGT1 -- "regulated transfer" --> EXT
```

---

## Phase C — Application Architecture

### Application Cooperation View
**Artifact:** Application Architecture  
**Viewpoint:** ArchiMate — Application Cooperation viewpoint  
**Purpose:** Shows how applications interact — the integration topology.

**Filename:** `application-architecture-cooperation.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph LR
  APP1["📱 Application A"]
  APP2["📱 Application B"]
  APP3["📱 Application C"]
  ESB["⚙️ Integration Bus / API Gateway"]
  EXT["🌐 External System"]

  APP1 -- "REST API" --> ESB
  APP2 -- "event stream" --> ESB
  ESB -- "sync" --> APP3
  ESB -- "webhook" --> EXT
```

---

### Application Component Map
**Artifact:** Application Architecture  
**Viewpoint:** ArchiMate — Application Structure viewpoint  
**Purpose:** Decomposition of key applications into components and their dependencies.

**Filename:** `application-architecture-component-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph TD
  subgraph AppA["Application A"]
    UI["🖥️ UI Layer"]
    SVC["⚙️ Service Layer"]
    DB["🗄️ Data Layer"]
    UI --> SVC --> DB
  end
  subgraph AppB["Application B"]
    API["🔌 API"]
    CORE["⚙️ Core"]
    API --> CORE
  end
  SVC -- "calls" --> API
```

---

## Phase D — Technology Architecture

### Technology Stack View
**Artifact:** Technology Architecture  
**Viewpoint:** ArchiMate — Technology viewpoint  
**Purpose:** Layered view of the technology stack from infrastructure through to application.

**Filename:** `technology-architecture-stack.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph BT
  subgraph Infra["Infrastructure Layer"]
    HW["⚙️ Physical / Cloud IaaS"]
  end
  subgraph Platform["Platform Layer"]
    OS["🐧 OS / Container Platform"]
    DB["🗄️ Database Engine"]
  end
  subgraph App["Application Layer"]
    MW["📦 Middleware / ESB"]
    APP["📱 Application"]
  end
  HW --> OS
  HW --> DB
  OS --> MW
  DB --> APP
  MW --> APP
```

---

### Infrastructure Topology
**Artifact:** Technology Architecture  
**Viewpoint:** ArchiMate — Physical Infrastructure / Deployment viewpoint  
**Purpose:** Shows network zones, nodes, and deployment of key components. Highlights security boundaries and failure domains.

**Filename:** `technology-architecture-topology.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
graph LR
  subgraph Internet["🌐 Internet"]
    USR["👤 User"]
  end
  subgraph DMZ["DMZ"]
    WAF["🛡️ WAF / CDN"]
    LB["⚖️ Load Balancer"]
  end
  subgraph AppZone["Application Zone"]
    WEB["📱 Web / API Servers"]
    WORKER["⚙️ Workers"]
  end
  subgraph DataZone["Data Zone"]
    DB["🗄️ Primary DB"]
    REPLICA["🗄️ Read Replica"]
  end
  USR --> WAF --> LB --> WEB
  WEB --> WORKER
  WEB --> DB
  DB --> REPLICA
```

---

## Phase E — Opportunities & Solutions

### Gap Heat Map
**Artifact:** Gap Analysis  
**Viewpoint:** Custom — Capability/priority analysis  
**Purpose:** Visual prioritisation of gaps by strategic impact and closure effort.

**Filename:** `gap-analysis-heat-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Gap Priority Matrix
  x-axis Low Effort --> High Effort
  y-axis Low Impact --> High Impact
  quadrant-1 Quick Wins
  quadrant-2 Major Projects
  quadrant-3 Fill-ins
  quadrant-4 Thankless Tasks
  GAP-001: [0.2, 0.8]
  GAP-002: [0.7, 0.9]
  GAP-003: [0.3, 0.3]
```

---

### Architecture Roadmap (Gantt)
**Artifact:** Architecture Roadmap  
**Viewpoint:** Custom — Timeline / delivery  
**Purpose:** Delivery timeline showing work packages sequenced into waves.

**Filename:** `architecture-roadmap-gantt.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
gantt
  title Architecture Roadmap
  dateFormat  YYYY-MM-DD
  section Wave 1 — Foundation
    WP-001 Capability A   :wp1, 2025-01-01, 90d
    WP-002 Capability B   :wp2, after wp1, 60d
  section Wave 2 — Core Build
    WP-003 Capability C   :wp3, after wp1, 120d
    WP-004 Capability D   :wp4, after wp3, 90d
  section Wave 3 — Optimise
    WP-005 Capability E   :wp5, after wp4, 60d
```

---

## Phase F — Migration Planning

### Migration Wave Diagram
**Artifact:** Migration Plan  
**Viewpoint:** Custom — Transition sequence  
**Purpose:** Shows what moves in each wave and the transition state at each checkpoint.

**Filename:** `migration-plan-waves.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
gantt
  title Migration Waves
  dateFormat  YYYY-MM-DD
  section Wave 1
    Decommission System A   :done, w1a, 2025-01-01, 60d
    Deploy Replacement B    :w1b, 2025-01-01, 90d
  section Wave 2
    Migrate Data Domain X   :w2a, after w1b, 60d
    Cutover Users           :w2b, after w2a, 30d
  section Wave 3
    Decommission Legacy     :w3, after w2b, 45d
```

---

## Cross-Cutting Artifacts

### Risk Heat Map
**Artifact:** Risk Register  
**Viewpoint:** Custom — Risk analysis  
**Purpose:** Positions risks by likelihood and impact.

**Filename:** `risk-register-heat-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Risk Heat Map
  x-axis Low Likelihood --> High Likelihood
  y-axis Low Impact --> High Impact
  quadrant-1 Critical — Act Now
  quadrant-2 High — Mitigate
  quadrant-3 Low — Monitor
  quadrant-4 Medium — Watch
  RIS-001: [0.7, 0.8]
  RIS-002: [0.3, 0.9]
  RIS-003: [0.5, 0.4]
```

---

### Requirements Traceability Chain
**Artifact:** Requirements Register  
**Viewpoint:** Custom — Motivation traceability  
**Purpose:** Shows how requirements trace from drivers through goals, objectives, and strategies.

**Filename:** `requirements-register-traceability.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  DRV["📌 DRV-001\n{{driver}}"]
  G["🎯 G-001\n{{goal}}"]
  OBJ["🔢 OBJ-001\n{{objective}}"]
  REQ1["📋 REQ-001\n{{requirement}}"]
  REQ2["📋 REQ-002\n{{requirement}}"]
  DRV --> G --> OBJ --> REQ1
  OBJ --> REQ2
```

---

## Coverage Table (Quick Reference)

| Artifact | Expected Diagrams | Filenames |
|---|---|---|
| Engagement Charter | Context Diagram, Org Chart | `engagement-charter-context.mmd`, `engagement-charter-org-chart.mmd` |
| Architecture Vision | Motivation Map, Stakeholder Grid | `architecture-vision-motivation-map.mmd`, `architecture-vision-stakeholder-grid.mmd` |
| Business Architecture | Capability Map, Process Flow, Org Map | `business-architecture-capability-map.mmd`, `business-architecture-process-flow.mmd`, `business-architecture-org-map.mmd` |
| Data Architecture | Conceptual Data Model, Data Flow | `data-architecture-conceptual-data-model.mmd`, `data-architecture-data-flow.mmd` |
| Application Architecture | Application Cooperation, Component Map | `application-architecture-cooperation.mmd`, `application-architecture-component-map.mmd` |
| Technology Architecture | Technology Stack, Infrastructure Topology | `technology-architecture-stack.mmd`, `technology-architecture-topology.mmd` |
| Gap Analysis | Gap Heat Map | `gap-analysis-heat-map.mmd` |
| Architecture Roadmap | Gantt Roadmap | `architecture-roadmap-gantt.mmd` |
| Migration Plan | Wave Diagram | `migration-plan-waves.mmd` |
| Risk Register | Risk Heat Map | `risk-register-heat-map.mmd` |
| Requirements Register | Traceability Chain | `requirements-register-traceability.mmd` |
