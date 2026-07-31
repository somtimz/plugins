# Phase C — Application Architecture


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
