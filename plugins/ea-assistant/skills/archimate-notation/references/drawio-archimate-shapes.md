# Using ArchiMate Shapes in Draw.io

This guide covers how to set up, find, and use ArchiMate-compliant shape libraries in Draw.io (diagrams.net), including both the built-in shape set and community-maintained options. It also covers practical tips for producing ArchiMate-compliant diagrams and known limitations of the Draw.io implementation.

---

## Built-in ArchiMate Shape Library

### Enabling the Built-in Library

Draw.io ships with an ArchiMate shape library. To enable it:

1. Open Draw.io (desktop app or at https://app.diagrams.net).
2. Click **Extras** in the menu bar (or use the **More Shapes** option from the left panel).
3. In the **More Shapes** dialog, scroll to the **Other** or **Networking** section (the location varies by version).
4. Check the box next to **ArchiMate 3** (or **ArchiMate**).
5. Click **Apply**.

The ArchiMate shapes will appear as a new panel section in the left sidebar.

**Note:** In some Draw.io versions the ArchiMate library appears under **Search Shapes** by typing "archimate" before it is explicitly enabled. Enabling it via More Shapes makes it persistently available.

### Shape Panel Organisation

Once enabled, the ArchiMate shape panel is organised by section:

| Section | Contents |
|---|---|
| Motivation | Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Constraint, Meaning, Value |
| Strategy | Resource, Capability, Value Stream, Course of Action |
| Business | All Business layer active structure, behaviour, and passive structure elements |
| Application | All Application layer elements |
| Technology | All Technology layer elements |
| Physical | Equipment, Facility, Distribution Network, Material |
| Implementation | Work Package, Deliverable, Implementation Event, Gap, Plateau |
| Relationships | Specialisation, Association, Serving, Realisation, etc. |
| Junctions | AND junction, OR junction |

---

## Placing Elements

1. Drag any shape from the panel onto the canvas.
2. The shape renders with its standard ArchiMate badge icon and a default label.
3. Double-click the shape to edit its label (use the element name as the label).
4. Resize by dragging the corner handles — ArchiMate elements are typically rectangular.

### Recommended Sizing
ArchiMate does not mandate specific sizes, but for readability:
- Standard elements: approximately 120px wide × 60px tall.
- Nested compositions: the parent should be large enough to contain children visually.
- Keep sizes consistent within a viewpoint for visual clarity.

---

## Creating Relationships

ArchiMate relationships are directed connections between elements. In Draw.io:

1. Hover over a source element until the blue connection points appear on its edges.
2. Click and drag from a connection point to a target element.
3. A default arrow is created — this is a generic association.
4. To set the correct ArchiMate relationship type: right-click the connection → **Edit Connection** → or select the connection and use the **Format** panel to choose the correct line style.

Alternatively, use the ArchiMate relationship shapes from the shape panel and place them as connectors.

### Relationship Visual Properties

| Relationship | Line Style | Arrowhead |
|---|---|---|
| Association | Solid thin line | Open arrowhead or none (directional or bidirectional) |
| Composition | Solid line | Filled diamond at source |
| Aggregation | Solid line | Open diamond at source |
| Assignment | Solid line | Circle with line at source, filled arrow at target |
| Realisation | Dashed line | Open arrowhead |
| Serving | Solid line | Filled arrowhead at target |
| Access | Dashed line | Open arrowhead (R/W notation optional) |
| Influence | Dashed line | Open arrowhead (label with +/−/modifier optional) |
| Triggering | Solid line | Filled arrowhead (bold) |
| Flow | Dashed line | Filled arrowhead |
| Specialisation | Solid line | Open triangle arrowhead |

To apply these styles manually in Draw.io: select the connector → right panel → **Connection** tab → set **Start**, **End**, and **Line** properties.

---

## Colour Conventions

The ArchiMate standard does not mandate colours, but industry convention (used by tools such as Archi and BiZZdesign) is widely adopted:

| Layer / Aspect | Conventional Fill Colour |
|---|---|
| Motivation | Light purple / lilac (#E8D5F5 or similar) |
| Strategy | Light beige / sand (#F5F5DC or similar) |
| Business | Light yellow / gold (#FFFFCC or #FFE699) |
| Application | Light blue (#DDEEFF or #BDD7EE) |
| Technology | Light green (#E2EFDA or #C6EFCE) |
| Physical | Light orange (#FCE4D6 or similar) |
| Implementation | Light grey (#F2F2F2) |

To apply in Draw.io: select an element → **Format** panel → **Fill** → choose a colour or enter a hex code. You can set a default style for elements of each type to avoid repeating this step.

---

## Using Custom XML Styles for ArchiMate Elements

Draw.io stores element styles as XML style strings. You can paste a style string directly:

1. Right-click an element → **Edit Style** (or press Ctrl+E / Cmd+E).
2. Paste the style string and click OK.

Example style for an ArchiMate Application Component:
```
shape=mxgraph.archimate3.application;fillColor=#dae8fc;strokeColor=#6c8ebf;
```

Example style for an ArchiMate Business Process:
```
shape=mxgraph.archimate3.business;type=process;fillColor=#fffacd;strokeColor=#b8860b;
```

The shape name pattern is: `mxgraph.archimate3.<layer>` with a `type=<elementtype>` attribute.

**Discovering shape names:** In the shape panel, right-click any ArchiMate shape → **Edit Style** to see its style string. Use this to build a library of copy-paste style strings.

---

## Creating Viewpoints in Draw.io

Draw.io does not enforce viewpoint rules natively. It is the architect's responsibility to restrict element types per the viewpoint definition (see the Viewpoint Guide). Practical approaches:

### Layer-per-Tab Approach
- Use separate diagram pages (tabs) for each viewpoint.
- Name each page after the viewpoint (e.g., "Application Cooperation", "Layered View").
- Reuse element IDs when copying elements across pages to maintain visual consistency.

### Using Tags for Filtering
Draw.io supports **tags** on elements (Edit → Edit Tags). Assign tags such as `business`, `application`, `technology` to elements. Use **View → Filter** (or the tag panel) to show/hide elements by layer when working on complex models.

### Using Containers for Layers
Use Draw.io's container/swimlane shapes to visually separate layers in a Layered Viewpoint:
1. Insert a swimlane or container.
2. Label it "Business Layer", "Application Layer", "Technology Layer".
3. Place the appropriate elements inside each container.

---

## Exporting ArchiMate Diagrams

### For Documentation
- **Export as PNG:** File → Export As → PNG. Set scale to 150–200% for high-resolution output suitable for Word/PDF documents.
- **Export as SVG:** Preferred for documents where text must remain searchable. File → Export As → SVG.
- **Export as PDF:** File → Export As → PDF for direct inclusion in reports.

### For Sharing / Collaboration
- **Export as .drawio XML:** File → Export As → XML. This preserves the full diagram for others to edit.
- **Publish to Confluence/SharePoint:** Use the Draw.io Confluence plugin or embed the XML in a SharePoint page using the Draw.io web part.

---

## Known Limitations and Workarounds

### Limitation 1 — No Viewpoint Enforcement
Draw.io does not restrict which element types can be placed on a diagram. Any element can be added to any viewpoint. The architect must manually apply the correct viewpoint rules.

**Workaround:** Maintain a separate legend or checklist per viewpoint. Reference the Viewpoint Guide to self-check compliance before sharing diagrams.

### Limitation 2 — Relationship Direction Is Not Always Obvious
The visual styling of ArchiMate relationships in Draw.io is manually applied and can be inconsistently set. A mistyped style string produces an incorrect relationship type.

**Workaround:** Create a "style palette" diagram page containing one instance of each relationship type with the correct style applied. Copy-paste connectors from this palette page rather than styling from scratch.

### Limitation 3 — No Model-Level Semantics
Draw.io is a drawing tool, not a modelling tool. There is no underlying model that enforces element identity across diagrams (unlike tools such as Archi or BiZZdesign). The same logical element (e.g., "Order Management System") may be represented as multiple disconnected shapes across different diagram pages with no formal linkage.

**Workaround:** For complex enterprise models where traceability matters, use a dedicated ArchiMate modelling tool (Archi is free and open source; BiZZdesign is enterprise-grade). Use Draw.io for communication diagrams and presentation views, not as the system of record.

### Limitation 4 — Badge Icons May Differ from Standard
The Draw.io ArchiMate shape icons may not exactly match the reference icons in the ArchiMate specification published by The Open Group. In some versions, the icon rendering is approximate.

**Workaround:** For formal deliverables requiring strict compliance with the ArchiMate visual notation (e.g., for certification or audit purposes), verify against the ArchiMate 3 specification visual reference.

### Limitation 5 — Text Rendering in Nested Elements
When elements are nested inside containers (for composition relationships), the text label can overlap the container label or be clipped.

**Workaround:** Adjust label position to "Top" or "Bottom" for container elements. Use the Format panel to set label vertical alignment to top. For complex nested diagrams, consider using indentation/grouping approaches with explicit composition lines rather than visual nesting.

---

## Recommended Workflow for EA Deliverables

1. **Start in an ArchiMate modelling tool** (Archi or equivalent) for the architecture model — elements, relationships, and viewpoints with full semantic consistency.
2. **Export to Draw.io** for presentation and collaboration: either re-create views in Draw.io for client-facing diagrams, or export from Archi as image and embed.
3. **Use Draw.io natively** for quick conceptual diagrams, whiteboard-style views in workshops, and embedded diagrams in Confluence/SharePoint.
4. **Never treat Draw.io diagrams as the architecture model of record** unless the engagement scope does not require multi-view consistency.
