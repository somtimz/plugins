# EA Tool Format Guide

Parsing notes for structured export formats from EA modelling tools. These formats require specialized parsing distinct from document formats — they contain structured model data (elements, relationships, views) rather than prose.

---

## Sparx Enterprise Architect — XMI / UML Export

**File extensions:** `.xmi`, `.xml` (when containing XMI content)

**Detection heuristics:**
- Extension `.xmi` → treat as Sparx XMI
- Extension `.xml` + presence of `xmi:type` attributes or `<uml:Model>` root element → treat as XMI
- Extension `.xml` without these signals → treat as generic XML (use standard document processing)

**Format:** XMI 2.x wrapping UML 2.x metaclasses. Root element is `<XMI>` with nested `<uml:Model>`. All model elements are encoded as `<packagedElement>` nodes with `xmi:type` attributes indicating the UML type.

**Key elements to extract:**

| XMI element | `xmi:type` value | Maps to EA artifact |
|---|---|---|
| Component | `uml:Component` | Application Architecture — component |
| Class | `uml:Class` | Data Architecture (if data-focused) or Application Architecture |
| Interface | `uml:Interface` | Application Architecture — interface/API |
| Package | `uml:Package` | Structural grouping; maps to capability or domain |
| UseCase | `uml:UseCase` | Requirements Register — use case (UC-NNN) |
| Actor | `uml:Actor` | Stakeholder Map |
| AssociationClass, Dependency, Realization | association types | Relationship / integration |
| Stereotype (via `xmi:Extension`) | N/A | Domain-specific classification; read from `xmi:Extension` → `stereotype name` |

**Mapping strategy:**
1. Parse the `<uml:Model>` tree; group elements by `xmi:type`
2. For elements with stereotypes, classify by stereotype name:
   - `<<datatype>>`, `<<entity>>` → Data Architecture
   - `<<component>>`, `<<service>>`, `<<api>>` → Application Architecture
   - `<<node>>`, `<<device>>`, `<<executionEnvironment>>` → Technology Architecture
3. Present grouped element inventory (type + name + count) for user confirmation before mapping

**Known limitations:**
- Visual diagram layout is not encoded in XMI — only structural model data is available
- Custom stereotypes from Sparx MDG (Model Driven Generation) profiles require stereotype-name lookup against the deployed profile; names vary per organisation
- Selective export from Sparx may omit model elements; the export scope is set by the user in Sparx at export time — warn the user that the extract may be incomplete
- Associations between elements are encoded separately from elements; ensure the full XMI file is present

**Recommended handling:**
1. Skip `ea-document-converter` — parse XMI directly in `ea-document-analyst`
2. Group elements by mapped artifact type; present count summary: `"Found: 12 Components → Application Architecture, 8 DataTypes → Data Architecture, 3 UseCase → Requirements"`
3. Ask user which groups to import and to which artifact
4. Extract element names and any tagged values as structured lists
5. Attribute all content: `📎 Source: uploads/{filename}`

---

## Archi — `.archimate` Export

**File extensions:** `.archimate`

**Detection heuristics:** File extension `.archimate` → treat as Archi model file.

**Format:** Archi's proprietary XML format wrapping ArchiMate 3.x elements. Root element is `<archimate:model>`. Elements are direct children of the model or nested in `<folder>` elements. Views (diagrams) contain `<child>` elements that reference element IDs — they are structural, not visual.

**Key elements by ArchiMate layer:**

| Layer | Element types | Maps to EA artifact |
|---|---|---|
| Motivation | Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Constraint, Meaning, Value | Architecture Vision (motivation), Architecture Principles (principles), Requirements Register |
| Strategy | Resource, Capability, CourseOfAction | Architecture Vision (strategy), Business Architecture (capabilities) |
| Business | BusinessActor, BusinessRole, BusinessCollaboration, BusinessProcess, BusinessFunction, BusinessService, BusinessObject, Contract | Business Architecture |
| Application | ApplicationComponent, ApplicationFunction, ApplicationService, ApplicationInterface, ApplicationInteraction, DataObject | Application Architecture, Data Architecture |
| Technology | Node, Device, SystemSoftware, TechnologyCollaboration, TechnologyService, TechnologyInterface, Artifact, CommunicationNetwork, Path | Technology Architecture |
| Physical | EquipmentElement, Facility, DistributionNetwork, Material | Technology Architecture (physical) |
| Implementation & Migration | WorkPackage, Deliverable, ImplementationEvent, Plateau, Gap | Architecture Roadmap, Migration Plan |

**Mapping strategy:**
1. Parse all `<element>` nodes; group by ArchiMate type and map to the layer table above
2. For each layer with extracted elements: map to the corresponding EA artifact
3. Extract `name`, `documentation` (if present), and `property` tags from each element
4. Extract relationships between elements (source/target IDs → resolve names)
5. Views contain `<child archimateElement="...">` references — resolve IDs to element names to reconstruct diagram membership

**Known limitations:**
- Element layout, colours, and styling in Archi diagrams are stored in `<bounds>` and `<style>` attributes — these are tool-specific and are NOT extracted
- Custom properties (user-defined key-value pairs on elements) are extractable but may have non-standard names specific to the user's Archi model
- Archi models may contain elements from multiple layers with relationship cross-references — relationships are best extracted as a separate inventory rather than embedded in the element listing
- The `.archimate` format is the richest import for this plugin because ArchiMate types map directly to the plugin's artifact taxonomy

**Recommended handling:**
1. Skip `ea-document-converter` — parse XML directly in `ea-document-analyst`
2. Group elements by ArchiMate layer; present layer summary for confirmation: `"Found: 15 Business elements → Business Architecture, 22 Application elements → Application Architecture, 8 Motivation elements → Architecture Vision"`
3. Ask user which layers to import and to which artifact
4. For each confirmed layer: extract element names and documentation as a structured list; map to artifact sections (e.g. Business layer → Business Architecture §4 Capability Model)
5. Attribute all content: `📎 Source: uploads/{filename}`

---

## LeanIX — CSV / JSON Export

**File extensions:** `.csv`, `.json`

**Detection heuristics:**
- `.csv` with column headers `lxID`, `lxType`, or `factSheetType` → LeanIX Fact Sheet export
- `.json` with keys `data.allFactSheets` or `factSheets` containing items with `lxID` → LeanIX GraphQL export
- `.json` without these keys → treat as generic JSON (not LeanIX)

**Format:** LeanIX exports Fact Sheets — a structured record type with a `type` field (`Application`, `IT Component`, `Business Capability`, `Data Object`, `Interface`, `User Group`, `Process`, `Project`, `Epic`). Each Fact Sheet has standard fields plus lifecycle phases and custom fields.

**Key Fact Sheet types and mappings:**

| LeanIX Fact Sheet type | Maps to EA artifact | Key fields to extract |
|---|---|---|
| `Application` | Application Architecture — application portfolio | name, description, lifecycle, businessCriticality, technicalSuitability, tags |
| `IT Component` | Technology Architecture — component inventory | name, description, category, lifecycle |
| `Business Capability` | Business Architecture — capability model | name, description, level (parent/child hierarchy) |
| `Data Object` | Data Architecture — data entity inventory | name, description, hasPersonalData, classification |
| `Interface` | Application Architecture — integration map | name, description, interfaceType (REST/SOAP/File/etc.), sourceApplication, targetApplication |
| `User Group` | Stakeholder Map | name, description |
| `Process` | Business Architecture — process inventory | name, description |

**Lifecycle phase mapping:**

| LeanIX value | Interpretation |
|---|---|
| `plan` | Planned (future state) |
| `phaseIn` | Being introduced |
| `active` | Current (baseline) |
| `phaseOut` | Being decommissioned |
| `endOfLife` | Decommissioned / Target for removal |

**Relations file:** LeanIX exports relationships in a separate file (typically `relations.csv` or embedded in the GraphQL JSON). Relationships define which Applications use which IT Components, which Interfaces connect which Applications, etc. If only one file is provided, check whether it contains relationship data and if not, ask the user to provide the relations file.

**Known limitations:**
- LeanIX exports are point-in-time snapshots and may not reflect live model state
- Custom fields (user-defined in LeanIX) have non-standard names — present them as-is and ask the user how to classify them
- The LeanIX GraphQL export format varies by API version; column names in CSV exports can change with LeanIX releases — the detection heuristics above cover the most common cases
- LeanIX detection is the most fragile of the three formats — if a CSV file is ambiguous, ask the user to confirm it is a LeanIX export before proceeding

**Recommended handling:**
1. Skip `ea-document-converter` — parse CSV/JSON directly in `ea-document-analyst`
2. Group Fact Sheets by type; present type summary for confirmation: `"Found: 45 Applications → Application Architecture, 12 Business Capabilities → Business Architecture, 8 Interfaces → Application Architecture (integration map)"`
3. If relations file is absent: offer to proceed with fact sheets only or wait for user to provide the relations file
4. For each confirmed Fact Sheet type: extract names, descriptions, and lifecycle phase; map to artifact sections
5. Flag Fact Sheets with lifecycle `phaseOut` or `endOfLife` as current baseline candidates (gaps to be addressed)
6. Attribute all content: `📎 Source: uploads/{filename}`
