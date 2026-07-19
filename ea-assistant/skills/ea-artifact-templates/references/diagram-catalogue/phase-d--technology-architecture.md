# Phase D — Technology Architecture


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
