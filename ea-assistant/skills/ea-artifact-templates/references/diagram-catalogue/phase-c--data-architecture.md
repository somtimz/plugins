# Phase C — Data Architecture


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
