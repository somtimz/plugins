import { useState, useEffect, useCallback } from "react";

// ─── Constants ───────────────────────────────────────────────────────────────

const APPROVERS = [
  { id: "a1", name: "Sarah Johnson",   role: "IT Director" },
  { id: "a2", name: "Mark Chen",       role: "Application Owner" },
  { id: "a3", name: "Lisa Patel",      role: "Security Lead" },
  { id: "a4", name: "David Williams",  role: "Infrastructure Manager" },
  { id: "a5", name: "Jennifer Torres", role: "Change Manager" },
  { id: "a6", name: "Robert Kim",      role: "Database Administrator" },
  { id: "a7", name: "Amanda Foster",   role: "Network Lead" },
  { id: "a8", name: "Michael Osei",    role: "CISO" },
];

const STATUS = {
  DRAFT:    "Draft",
  PENDING:  "Pending CAB Approval",
  APPROVED: "Approved by CAB",
  REJECTED: "Rejected",
};

const S_STYLE = {
  [STATUS.DRAFT]:    { bg: "#E5E7EB", text: "#374151", dot: "#9CA3AF" },
  [STATUS.PENDING]:  { bg: "#FEF3C7", text: "#92400E", dot: "#F59E0B" },
  [STATUS.APPROVED]: { bg: "#D1FAE5", text: "#065F46", dot: "#10B981" },
  [STATUS.REJECTED]: { bg: "#FEE2E2", text: "#991B1B", dot: "#EF4444" },
};

const P_STYLE = {
  Low:      { bg: "#ECFDF5", text: "#065F46" },
  Medium:   { bg: "#EFF6FF", text: "#1E40AF" },
  High:     { bg: "#FFF7ED", text: "#9A3412" },
  Critical: { bg: "#FEF2F2", text: "#991B1B" },
};

const RISK_COLOR = { Low: "#10B981", Medium: "#F59E0B", High: "#EF4444" };

// ─── Storage helpers ─────────────────────────────────────────────────────────

async function getCRs() {
  try {
    const idx = await window.storage.get("cr_index");
    if (!idx) return [];
    const ids = JSON.parse(idx.value);
    const out = [];
    for (const id of ids) {
      try {
        const r = await window.storage.get(`cr_${id}`);
        if (r) out.push(JSON.parse(r.value));
      } catch (_) {}
    }
    return out;
  } catch (_) { return []; }
}

async function putCR(cr) {
  const saved = { ...cr, updatedAt: new Date().toISOString() };
  let ids = [];
  try {
    const idx = await window.storage.get("cr_index");
    if (idx) ids = JSON.parse(idx.value);
  } catch (_) {}
  if (!ids.includes(cr.id)) ids.push(cr.id);
  await window.storage.set("cr_index", JSON.stringify(ids));
  await window.storage.set(`cr_${cr.id}`, JSON.stringify(saved));
  return saved;
}

// ─── Factory ─────────────────────────────────────────────────────────────────

function makeCR() {
  const year = new Date().getFullYear();
  const num  = String(Math.floor(Math.random() * 9000) + 1000);
  return {
    id: `RFC-${year}-${num}`,
    title: "", changeType: "Normal", priority: "Medium",
    requestedBy: "", changeOwner: "",
    dateSubmitted: new Date().toISOString().split("T")[0],
    affectedSystems: "", businessJustification: "", changeDescription: "",
    implSteps:        [{ id: 1, text: "", checked: false }],
    rollbackSteps:    [{ id: 1, text: "", checked: false }],
    validationItems:  [{ id: 1, text: "", checked: false }],
    changeWindow: { start: "", duration: "", maintenanceWindow: "" },
    riskLevel: "Medium", riskImpact: "", riskUsers: "", riskDeps: "",
    approverIds: [], status: STATUS.DRAFT, cabNotes: "",
    cabHistory: [], retrospectiveReview: false,
    createdAt: new Date().toISOString(), updatedAt: new Date().toISOString(),
  };
}

async function deleteCR(id) {
  try {
    const idx = await window.storage.get("cr_index");
    if (!idx) return;
    const ids = JSON.parse(idx.value).filter(x => x !== id);
    await window.storage.set("cr_index", JSON.stringify(ids));
    await window.storage.set(`cr_${id}`, JSON.stringify(null));
  } catch (_) {}
}

// ─── Small UI pieces ─────────────────────────────────────────────────────────

function StatusBadge({ status }) {
  const s = S_STYLE[status] || S_STYLE[STATUS.DRAFT];
  return (
    <span style={{ display:"inline-flex", alignItems:"center", gap:5,
      background:s.bg, color:s.text, padding:"3px 10px",
      borderRadius:20, fontSize:11, fontWeight:700, letterSpacing:"0.02em" }}>
      <span style={{ width:6, height:6, borderRadius:"50%", background:s.dot }} />
      {status}
    </span>
  );
}

function PriorityBadge({ priority }) {
  const s = P_STYLE[priority] || P_STYLE.Medium;
  return (
    <span style={{ background:s.bg, color:s.text,
      padding:"2px 7px", borderRadius:4, fontSize:11, fontWeight:700 }}>
      {priority.toUpperCase()}
    </span>
  );
}

function Card({ children, style }) {
  return (
    <div style={{ background:"#fff", borderRadius:10, boxShadow:"0 1px 4px rgba(0,0,0,0.07)",
      border:"1px solid #E8ECF4", ...style }}>
      {children}
    </div>
  );
}

function Btn({ children, onClick, variant="primary", small, disabled, style: sx }) {
  const base = { border:"none", borderRadius:7, cursor:disabled?"not-allowed":"pointer",
    fontWeight:600, fontSize:small?12:13, padding:small?"5px 12px":"8px 16px",
    opacity:disabled?0.5:1, transition:"opacity 0.15s", ...sx };
  const variants = {
    primary:  { background:"#1E3264", color:"#fff" },
    blue:     { background:"#3B82F6", color:"#fff" },
    green:    { background:"#10B981", color:"#fff" },
    red:      { background:"#EF4444", color:"#fff" },
    ghost:    { background:"#F3F4F6", color:"#374151" },
    outline:  { background:"transparent", color:"#1E3264", border:"1.5px solid #1E3264" },
  };
  return <button onClick={onClick} disabled={disabled} style={{ ...base, ...variants[variant] }}>{children}</button>;
}

function Input({ label, value, onChange, type="text", placeholder, required, rows, disabled }) {
  const [focused, setFocused] = useState(false);
  const style = {
    width:"100%", padding:"8px 10px", border:`1.5px solid ${focused?"#3B82F6":"#D1D5DB"}`,
    borderRadius:7, fontSize:13, outline:"none", transition:"border 0.15s",
    fontFamily:"inherit", resize:rows?"vertical":undefined,
    background:disabled?"#F9FAFB":"#fff", color:disabled?"#6B7280":"#111",
  };
  return (
    <div style={{ marginBottom:14 }}>
      {label && <label style={{ display:"block", fontSize:12, fontWeight:600,
        color:"#4B5563", marginBottom:4, letterSpacing:"0.03em" }}>
        {label}{required && <span style={{ color:"#EF4444" }}> *</span>}
      </label>}
      {rows
        ? <textarea value={value} onChange={e=>!disabled&&onChange(e.target.value)} placeholder={placeholder}
            rows={rows} style={style} disabled={disabled}
            onFocus={()=>setFocused(true)} onBlur={()=>setFocused(false)} />
        : <input type={type} value={value} onChange={e=>!disabled&&onChange(e.target.value)}
            placeholder={placeholder} style={style} disabled={disabled}
            onFocus={()=>setFocused(true)} onBlur={()=>setFocused(false)} />
      }
    </div>
  );
}

function Select({ label, value, onChange, options, disabled }) {
  return (
    <div style={{ marginBottom:14 }}>
      {label && <label style={{ display:"block", fontSize:12, fontWeight:600,
        color:"#4B5563", marginBottom:4 }}>{label}</label>}
      <select value={value} onChange={e=>onChange(e.target.value)} disabled={disabled}
        style={{ width:"100%", padding:"8px 10px", border:"1.5px solid #D1D5DB",
          borderRadius:7, fontSize:13, fontFamily:"inherit",
          background:disabled?"#F9FAFB":"#fff",
          color:disabled?"#6B7280":"#111", outline:"none" }}>
        {options.map(o => <option key={o.value||o} value={o.value||o}>{o.label||o}</option>)}
      </select>
    </div>
  );
}

function SectionHead({ title }) {
  return (
    <div style={{ fontSize:11, fontWeight:700, letterSpacing:"0.08em", color:"#6B7280",
      textTransform:"uppercase", marginBottom:14, paddingBottom:8,
      borderBottom:"2px solid #E8ECF4", marginTop:4 }}>
      {title}
    </div>
  );
}

// ─── Step list editor ─────────────────────────────────────────────────────────

function StepEditor({ label, steps, onChange }) {
  const update = (id, text) => onChange(steps.map(s => s.id===id ? {...s, text} : s));
  const add = () => {
    const maxId = steps.reduce((m,s) => Math.max(m,s.id), 0);
    onChange([...steps, { id: maxId+1, text:"", checked:false }]);
  };
  const remove = (id) => steps.length > 1 && onChange(steps.filter(s => s.id!==id));

  return (
    <div style={{ marginBottom:14 }}>
      <label style={{ display:"block", fontSize:12, fontWeight:600, color:"#4B5563", marginBottom:6 }}>{label}</label>
      {steps.map((s, i) => (
        <div key={s.id} style={{ display:"flex", gap:8, alignItems:"center", marginBottom:6 }}>
          <span style={{ fontSize:12, color:"#9CA3AF", width:20, textAlign:"right", flexShrink:0 }}>{i+1}.</span>
          <input value={s.text} onChange={e=>update(s.id, e.target.value)}
            placeholder={`Step ${i+1}`}
            style={{ flex:1, padding:"7px 9px", border:"1.5px solid #D1D5DB",
              borderRadius:6, fontSize:13, fontFamily:"inherit", background:"#fff" }} />
          <button onClick={()=>remove(s.id)} style={{ background:"none", border:"none",
            color:"#D1D5DB", cursor:"pointer", fontSize:16, padding:"0 4px", lineHeight:1 }}>×</button>
        </div>
      ))}
      <button onClick={add} style={{ fontSize:12, color:"#3B82F6", background:"none",
        border:"none", cursor:"pointer", padding:"4px 0", fontWeight:600 }}>+ Add step</button>
    </div>
  );
}

// ─── Approver picker ─────────────────────────────────────────────────────────

function ApproverPicker({ selected, onChange }) {
  const toggle = (id) => {
    onChange(selected.includes(id) ? selected.filter(x=>x!==id) : [...selected, id]);
  };
  return (
    <div style={{ marginBottom:14 }}>
      <label style={{ display:"block", fontSize:12, fontWeight:600, color:"#4B5563", marginBottom:6 }}>Approvers</label>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:6 }}>
        {APPROVERS.map(a => {
          const active = selected.includes(a.id);
          return (
            <div key={a.id} onClick={()=>toggle(a.id)}
              style={{ display:"flex", alignItems:"center", gap:8, padding:"8px 10px",
                border:`1.5px solid ${active?"#3B82F6":"#E5E7EB"}`,
                borderRadius:7, cursor:"pointer", background:active?"#EFF6FF":"#fff",
                transition:"all 0.12s" }}>
              <div style={{ width:16, height:16, borderRadius:4,
                border:`2px solid ${active?"#3B82F6":"#D1D5DB"}`,
                background:active?"#3B82F6":"transparent",
                display:"flex", alignItems:"center", justifyContent:"center", flexShrink:0 }}>
                {active && <span style={{ color:"#fff", fontSize:10, lineHeight:1 }}>✓</span>}
              </div>
              <div>
                <div style={{ fontSize:12, fontWeight:600, color:"#111" }}>{a.name}</div>
                <div style={{ fontSize:11, color:"#6B7280" }}>{a.role}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

// ─── Dashboard ────────────────────────────────────────────────────────────────

function Dashboard({ crs, allCRs, statusFilter, setStatusFilter, onEdit, onChecklist, onStatusChange, onDelete }) {
  const counts = {
    all:              allCRs.length,
    [STATUS.DRAFT]:   allCRs.filter(c=>c.status===STATUS.DRAFT).length,
    [STATUS.PENDING]: allCRs.filter(c=>c.status===STATUS.PENDING).length,
    [STATUS.APPROVED]:allCRs.filter(c=>c.status===STATUS.APPROVED).length,
    [STATUS.REJECTED]:allCRs.filter(c=>c.status===STATUS.REJECTED).length,
  };

  const filters = [
    { key:"all", label:"All", count:counts.all },
    { key:STATUS.DRAFT, label:"Draft", count:counts[STATUS.DRAFT] },
    { key:STATUS.PENDING, label:"Pending CAB", count:counts[STATUS.PENDING] },
    { key:STATUS.APPROVED, label:"Approved", count:counts[STATUS.APPROVED] },
    { key:STATUS.REJECTED, label:"Rejected", count:counts[STATUS.REJECTED] },
  ];

  return (
    <div>
      {/* Stat pills */}
      <div style={{ display:"flex", gap:8, marginBottom:20, flexWrap:"wrap" }}>
        {filters.map(f => {
          const active = statusFilter === f.key;
          const dotColor = f.key==="all" ? "#6B7280"
            : f.key===STATUS.DRAFT ? "#9CA3AF"
            : f.key===STATUS.PENDING ? "#F59E0B"
            : f.key===STATUS.APPROVED ? "#10B981" : "#EF4444";
          return (
            <button key={f.key} onClick={()=>setStatusFilter(f.key)}
              style={{ display:"flex", alignItems:"center", gap:6,
                padding:"6px 14px", borderRadius:20,
                border:`1.5px solid ${active?"#1E3264":"#E5E7EB"}`,
                background:active?"#1E3264":"#fff",
                color:active?"#fff":"#374151",
                cursor:"pointer", fontSize:12, fontWeight:600,
                fontFamily:"inherit" }}>
              <span style={{ width:7, height:7, borderRadius:"50%",
                background:active?"rgba(255,255,255,0.6)":dotColor }} />
              {f.label}
              <span style={{ background:active?"rgba(255,255,255,0.2)":"#F3F4F6",
                color:active?"#fff":"#6B7280", borderRadius:10,
                padding:"1px 7px", fontSize:11 }}>{f.count}</span>
            </button>
          );
        })}
      </div>

      {/* CR list */}
      {crs.length === 0 ? (
        <Card style={{ padding:40, textAlign:"center" }}>
          <div style={{ fontSize:32, marginBottom:8 }}>📋</div>
          <div style={{ fontSize:15, color:"#6B7280" }}>No change requests yet.</div>
        </Card>
      ) : (
        <div style={{ display:"flex", flexDirection:"column", gap:10 }}>
          {crs.map(cr => (
            <Card key={cr.id} style={{ padding:"16px 20px" }}>
              <div style={{ display:"flex", alignItems:"flex-start", justifyContent:"space-between", gap:12 }}>
                <div style={{ flex:1, minWidth:0 }}>
                  <div style={{ display:"flex", alignItems:"center", gap:8, marginBottom:5 }}>
                    <span style={{ fontSize:11, color:"#9CA3AF", fontFamily:"'IBM Plex Mono', monospace", fontWeight:600 }}>{cr.id}</span>
                    <StatusBadge status={cr.status} />
                    <PriorityBadge priority={cr.priority} />
                  </div>
                  <div style={{ fontSize:14, fontWeight:600, color:"#111", marginBottom:4 }}>
                    {cr.title || <span style={{ color:"#9CA3AF", fontStyle:"italic" }}>Untitled Change Request</span>}
                  </div>
                  <div style={{ fontSize:12, color:"#6B7280" }}>
                    {cr.changeType} · {cr.changeOwner || "No owner assigned"} · Updated {new Date(cr.updatedAt).toLocaleDateString()}
                  </div>
                  {cr.changeWindow?.start && (
                    <div style={{ fontSize:12, color:"#9CA3AF", marginTop:2 }}>
                      📅 {cr.changeWindow.start}
                    </div>
                  )}
                </div>
                <div style={{ display:"flex", gap:6, flexShrink:0 }}>
                  <Btn small variant="ghost" onClick={()=>onChecklist(cr)}>Checklist</Btn>
                  <Btn small variant="outline" onClick={()=>onEdit(cr)}>Edit</Btn>
                  {cr.status === STATUS.DRAFT && (
                    <Btn small variant="blue" onClick={()=>onStatusChange(cr, STATUS.PENDING)}>Submit to CAB</Btn>
                  )}
                  {cr.status === STATUS.DRAFT && (
                    <Btn small variant="red" onClick={()=>onDelete(cr)}>Delete</Btn>
                  )}
                </div>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}

// ─── CR Form ─────────────────────────────────────────────────────────────────

function CRForm({ cr: initialCR, onSave, onStatusChange, onChecklist }) {
  const [cr, setCR] = useState(initialCR);
  const [saving, setSaving] = useState(false);
  const [dirty, setDirty] = useState(false);

  const isReadOnly = cr.status === STATUS.APPROVED || cr.status === STATUS.REJECTED;

  const set = useCallback((field, val) => {
    setCR(prev => ({ ...prev, [field]: val }));
    setDirty(true);
  }, []);

  const setNested = useCallback((parent, field, val) => {
    setCR(prev => ({ ...prev, [parent]: { ...prev[parent], [field]: val } }));
    setDirty(true);
  }, []);

  const save = async (status) => {
    setSaving(true);
    let toSave = status ? { ...cr, status } : cr;
    // Emergency bypass: auto-approve without CAB
    if (status === STATUS.PENDING && cr.changeType === "Emergency") {
      const autoNote = "Auto-approved — Emergency change (retrospective CAB review required)";
      toSave = {
        ...toSave,
        status: STATUS.APPROVED,
        retrospectiveReview: true,
        cabNotes: autoNote,
        cabHistory: [...(cr.cabHistory || []), {
          action: "approved",
          notes: autoNote,
          timestamp: new Date().toISOString(),
        }],
      };
    }
    const saved = await onSave(toSave);
    setCR(saved);
    setSaving(false);
    setDirty(false);
  };

  const canSubmit = cr.title && cr.changeOwner && cr.changeDescription;

  return (
    <div style={{ maxWidth:800, margin:"0 auto" }}>
      {/* Top bar */}
      <div style={{ display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:18 }}>
        <div>
          <div style={{ fontSize:11, color:"#9CA3AF", fontFamily:"'IBM Plex Mono', monospace", marginBottom:2 }}>{cr.id}</div>
          <StatusBadge status={cr.status} />
        </div>
        <div style={{ display:"flex", gap:8, alignItems:"center" }}>
          {dirty && !isReadOnly && <span style={{ fontSize:11, color:"#F59E0B" }}>Unsaved changes</span>}
          <Btn variant="ghost" onClick={onChecklist}>View Checklist</Btn>
          {!isReadOnly && (
            <Btn variant="ghost" onClick={()=>save()} disabled={saving}>
              {saving ? "Saving..." : "Save Draft"}
            </Btn>
          )}
          {cr.status === STATUS.DRAFT && (
            <Btn variant="blue" onClick={()=>save(STATUS.PENDING)} disabled={!canSubmit || saving}>
              {cr.changeType === "Emergency" ? "Auto-Approve (Emergency)" : "Submit to CAB"}
            </Btn>
          )}
          {(cr.status === STATUS.PENDING || cr.status === STATUS.REJECTED) && (
            <Btn variant="ghost" onClick={()=>save(STATUS.DRAFT)}>Revert to Draft</Btn>
          )}
        </div>
      </div>

      {isReadOnly && (
        <div style={{ background: cr.status === STATUS.APPROVED ? "#D1FAE5" : "#FEE2E2",
          border:`1px solid ${cr.status === STATUS.APPROVED ? "#6EE7B7" : "#FCA5A5"}`,
          borderRadius:8, padding:"10px 14px", fontSize:12,
          color: cr.status === STATUS.APPROVED ? "#065F46" : "#991B1B", marginBottom:16 }}>
          This CR is <strong>{cr.status}</strong> — no further edits are permitted.
          {cr.status === STATUS.REJECTED && " Use \"Revert to Draft\" to edit and resubmit."}
          {cr.cabNotes && <div style={{ marginTop:4 }}>CAB notes: <em>{cr.cabNotes}</em></div>}
        </div>
      )}

      {!canSubmit && cr.status === STATUS.DRAFT && (
        <div style={{ background:"#FFF7ED", border:"1px solid #FED7AA", borderRadius:8,
          padding:"10px 14px", fontSize:12, color:"#92400E", marginBottom:16 }}>
          Complete <strong>Title</strong>, <strong>Change Owner</strong>, and <strong>Change Description</strong> before submitting to CAB.
        </div>
      )}

      {/* Form sections */}
      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="1 · Overview" />
        <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"0 16px" }}>
          <Input label="Change Title" required value={cr.title} onChange={v=>set("title",v)} placeholder="e.g. Upgrade MySQL to 8.0 on prod" disabled={isReadOnly} />
          <Input label="Change Owner / Implementer" required value={cr.changeOwner} onChange={v=>set("changeOwner",v)} placeholder="Name or email" disabled={isReadOnly} />
          <Input label="Requested By" value={cr.requestedBy} onChange={v=>set("requestedBy",v)} placeholder="Name or team" disabled={isReadOnly} />
          <Input label="Date Submitted" type="date" value={cr.dateSubmitted} onChange={v=>set("dateSubmitted",v)} disabled={isReadOnly} />
          <Select label="Change Type" value={cr.changeType} onChange={v=>set("changeType",v)}
            options={["Standard","Normal","Emergency"]} disabled={isReadOnly} />
          <Select label="Priority" value={cr.priority} onChange={v=>set("priority",v)}
            options={["Low","Medium","High","Critical"]} disabled={isReadOnly} />
        </div>
        <Input label="Change Description" required value={cr.changeDescription} onChange={v=>set("changeDescription",v)}
          placeholder="What is being changed and why?" rows={3} disabled={isReadOnly} />
        <Input label="Affected Systems" value={cr.affectedSystems} onChange={v=>set("affectedSystems",v)}
          placeholder="Which systems, servers, or services are affected?" rows={2} disabled={isReadOnly} />
        <Input label="Business Justification" value={cr.businessJustification} onChange={v=>set("businessJustification",v)}
          placeholder="What business need or risk does this address?" rows={2} disabled={isReadOnly} />
      </Card>

      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="2 · Implementation Steps" />
        <StepEditor label="" steps={cr.implSteps}
          onChange={v=>{ if(!isReadOnly){setCR(p=>({...p,implSteps:v})); setDirty(true);} }} />
      </Card>

      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="3 · Change Window" />
        <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"0 16px" }}>
          <Input label="Proposed Start Date/Time" value={cr.changeWindow.start}
            onChange={v=>setNested("changeWindow","start",v)} placeholder="e.g. March 18, 2026 at 5:00 PM EST" disabled={isReadOnly} />
          <Input label="Estimated Duration" value={cr.changeWindow.duration}
            onChange={v=>setNested("changeWindow","duration",v)} placeholder="e.g. 4 hours" disabled={isReadOnly} />
        </div>
        <Input label="Maintenance Window" value={cr.changeWindow.maintenanceWindow}
          onChange={v=>setNested("changeWindow","maintenanceWindow",v)} placeholder="e.g. 5:00 PM – 11:00 PM EST" disabled={isReadOnly} />
      </Card>

      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="4 · Risk & Impact" />
        <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"0 16px" }}>
          <Select label="Risk Level" value={cr.riskLevel} onChange={v=>set("riskLevel",v)}
            options={["Low","Medium","High"]} disabled={isReadOnly} />
          <Input label="Affected Users / Services" value={cr.riskUsers}
            onChange={v=>set("riskUsers",v)} placeholder="Who is impacted?" disabled={isReadOnly} />
        </div>
        <Input label="Impact if Change Fails" value={cr.riskImpact}
          onChange={v=>set("riskImpact",v)} placeholder="What happens if something goes wrong?" rows={2} disabled={isReadOnly} />
        <Input label="Dependencies / Prerequisites" value={cr.riskDeps}
          onChange={v=>set("riskDeps",v)} placeholder="Anything that must be in place first?" rows={2} disabled={isReadOnly} />
      </Card>

      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="5 · Rollback Plan" />
        <StepEditor label="" steps={cr.rollbackSteps}
          onChange={v=>{ if(!isReadOnly){setCR(p=>({...p,rollbackSteps:v})); setDirty(true);} }} />
      </Card>

      <Card style={{ padding:20, marginBottom:16 }}>
        <SectionHead title="6 · Testing & Validation" />
        <StepEditor label="" steps={cr.validationItems}
          onChange={v=>{ if(!isReadOnly){setCR(p=>({...p,validationItems:v})); setDirty(true);} }} />
      </Card>

      <Card style={{ padding:20, marginBottom:24 }}>
        <SectionHead title="7 · Approvers" />
        <ApproverPicker selected={cr.approverIds}
          onChange={v=>{ if(!isReadOnly){setCR(p=>({...p,approverIds:v})); setDirty(true);} }} />
      </Card>

      {/* Bottom save bar */}
      {!isReadOnly && (
        <div style={{ display:"flex", justifyContent:"flex-end", gap:8, paddingBottom:32 }}>
          {dirty && <span style={{ fontSize:12, color:"#F59E0B", alignSelf:"center" }}>Unsaved changes</span>}
          <Btn variant="ghost" onClick={()=>save()} disabled={saving}>
            {saving ? "Saving..." : "Save Draft"}
          </Btn>
          {cr.status === STATUS.DRAFT && (
            <Btn variant="blue" onClick={()=>save(STATUS.PENDING)} disabled={!canSubmit || saving}>
              {cr.changeType === "Emergency" ? "Auto-Approve (Emergency)" : "Submit to CAB"}
            </Btn>
          )}
        </div>
      )}
    </div>
  );
}

// ─── Checklist ────────────────────────────────────────────────────────────────

function ChecklistView({ cr: initialCR, onSave, onEdit, onStatusChange }) {
  const [cr, setCR] = useState(initialCR);
  const [saving, setSaving] = useState(false);

  const toggle = async (listKey, stepId) => {
    const updated = {
      ...cr,
      [listKey]: cr[listKey].map(s => s.id===stepId ? {...s, checked:!s.checked} : s)
    };
    setCR(updated);
    setSaving(true);
    const saved = await onSave(updated);
    setCR(saved);
    setSaving(false);
  };

  const pct = (list) => {
    if (!list.length) return 0;
    return Math.round(list.filter(s=>s.checked).length / list.length * 100);
  };

  const totalItems = cr.implSteps.length + cr.rollbackSteps.length + cr.validationItems.length;
  const totalDone  = [...cr.implSteps,...cr.rollbackSteps,...cr.validationItems].filter(s=>s.checked).length;
  const overallPct = totalItems ? Math.round(totalDone/totalItems*100) : 0;

  function ProgressBar({ pct }) {
    return (
      <div style={{ height:6, background:"#E5E7EB", borderRadius:3, overflow:"hidden" }}>
        <div style={{ height:"100%", width:`${pct}%`, background:pct===100?"#10B981":"#3B82F6",
          borderRadius:3, transition:"width 0.3s" }} />
      </div>
    );
  }

  function CheckSection({ title, listKey, steps }) {
    const p = pct(steps);
    return (
      <Card style={{ padding:20, marginBottom:14 }}>
        <div style={{ display:"flex", justifyContent:"space-between", alignItems:"center", marginBottom:10 }}>
          <SectionHead title={title} />
          <span style={{ fontSize:12, fontWeight:600, color:p===100?"#10B981":"#6B7280" }}>{p}%</span>
        </div>
        <ProgressBar pct={p} />
        <div style={{ marginTop:14 }}>
          {steps.filter(s=>s.text).map((s, i) => (
            <div key={s.id} onClick={()=>toggle(listKey, s.id)}
              style={{ display:"flex", alignItems:"flex-start", gap:10, padding:"9px 0",
                borderBottom:"1px solid #F3F4F6", cursor:"pointer",
                opacity:s.checked?0.5:1, transition:"opacity 0.15s" }}>
              <div style={{ width:20, height:20, borderRadius:5, flexShrink:0, marginTop:1,
                border:`2px solid ${s.checked?"#10B981":"#D1D5DB"}`,
                background:s.checked?"#10B981":"transparent",
                display:"flex", alignItems:"center", justifyContent:"center" }}>
                {s.checked && <span style={{ color:"#fff", fontSize:11 }}>✓</span>}
              </div>
              <div>
                <span style={{ fontSize:12, color:"#6B7280", marginRight:6 }}>{i+1}.</span>
                <span style={{ fontSize:13, color:"#111",
                  textDecoration:s.checked?"line-through":"none" }}>{s.text}</span>
              </div>
            </div>
          ))}
          {!steps.filter(s=>s.text).length && (
            <div style={{ fontSize:12, color:"#9CA3AF", padding:"8px 0" }}>No steps added yet.</div>
          )}
        </div>
      </Card>
    );
  }

  return (
    <div style={{ maxWidth:700, margin:"0 auto" }}>
      {/* Header */}
      <Card style={{ padding:"16px 20px", marginBottom:16 }}>
        <div style={{ display:"flex", alignItems:"center", justifyContent:"space-between" }}>
          <div>
            <div style={{ fontSize:11, color:"#9CA3AF", fontFamily:"'IBM Plex Mono', monospace", marginBottom:2 }}>{cr.id}</div>
            <div style={{ fontSize:14, fontWeight:600, color:"#111", marginBottom:5 }}>
              {cr.title || "Untitled Change Request"}
            </div>
            <div style={{ display:"flex", gap:6, alignItems:"center" }}>
              <StatusBadge status={cr.status} />
              <PriorityBadge priority={cr.priority} />
              {cr.changeWindow?.start && (
                <span style={{ fontSize:11, color:"#6B7280" }}>📅 {cr.changeWindow.start}</span>
              )}
            </div>
          </div>
          <div style={{ textAlign:"center" }}>
            <div style={{ fontSize:28, fontWeight:700, color:overallPct===100?"#10B981":"#1E3264" }}>{overallPct}%</div>
            <div style={{ fontSize:11, color:"#6B7280" }}>complete</div>
          </div>
        </div>
        <div style={{ marginTop:12 }}>
          <ProgressBar pct={overallPct} />
        </div>
      </Card>

      {/* Saving indicator */}
      {saving && <div style={{ fontSize:11, color:"#6B7280", textAlign:"center", marginBottom:8 }}>Saving...</div>}

      <CheckSection title="Implementation Steps" listKey="implSteps" steps={cr.implSteps} />
      <CheckSection title="Rollback Steps" listKey="rollbackSteps" steps={cr.rollbackSteps} />
      <CheckSection title="Validation & Testing" listKey="validationItems" steps={cr.validationItems} />

      <div style={{ display:"flex", justifyContent:"flex-end", gap:8, paddingBottom:32 }}>
        <Btn variant="ghost" onClick={onEdit}>Edit CR</Btn>
        {cr.status === STATUS.DRAFT && (
          <Btn variant="blue" onClick={()=>onStatusChange(STATUS.PENDING)}>Submit to CAB</Btn>
        )}
      </div>
    </div>
  );
}

// ─── Root ─────────────────────────────────────────────────────────────────────

export default function App() {
  const [crs, setCRs]           = useState([]);
  const [loading, setLoading]   = useState(true);
  const [view, setView]         = useState("dashboard");
  const [activeCR, setActiveCR] = useState(null);
  const [filter, setFilter]     = useState("all");
  const [toast, setToast]       = useState(null);

  useEffect(() => {
    const link = document.createElement("link");
    link.rel  = "stylesheet";
    link.href = "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@600&display=swap";
    document.head.appendChild(link);
    getCRs().then(data => {
      setCRs(data.sort((a,b) => new Date(b.updatedAt)-new Date(a.updatedAt)));
      setLoading(false);
    });
  }, []);

  const showToast = (msg, type="success") => {
    setToast({ msg, type });
    setTimeout(() => setToast(null), 2500);
  };

  const handleSave = async (cr) => {
    const saved = await putCR(cr);
    setCRs(prev => {
      const i = prev.findIndex(c=>c.id===saved.id);
      const next = i>=0 ? [...prev.slice(0,i), saved, ...prev.slice(i+1)] : [saved,...prev];
      return next.sort((a,b) => new Date(b.updatedAt)-new Date(a.updatedAt));
    });
    showToast("Saved");
    return saved;
  };

  const handleStatusChange = async (cr, newStatus) => {
    let toSave = { ...cr, status: newStatus };
    // Emergency bypass: auto-approve without CAB (regardless of trigger source)
    if (newStatus === STATUS.PENDING && cr.changeType === "Emergency") {
      const autoNote = "Auto-approved — Emergency change (retrospective CAB review required)";
      toSave = {
        ...toSave,
        status: STATUS.APPROVED,
        retrospectiveReview: true,
        cabNotes: autoNote,
        cabHistory: [...(cr.cabHistory || []), {
          action: "approved",
          notes: autoNote,
          timestamp: new Date().toISOString(),
        }],
      };
    }
    const saved = await handleSave(toSave);
    if (activeCR?.id === saved.id) setActiveCR(saved);
    const labels = {
      [STATUS.PENDING]:  "Submitted to CAB for approval",
      [STATUS.DRAFT]:    "Reverted to Draft",
      [STATUS.APPROVED]: "Approved by CAB",
      [STATUS.REJECTED]: "Rejected",
    };
    showToast(labels[newStatus] || "Status updated");
  };

  const handleDelete = async (cr) => {
    if (!window.confirm(`Delete ${cr.id}? This cannot be undone.`)) return;
    await deleteCR(cr.id);
    setCRs(prev => prev.filter(c => c.id !== cr.id));
    showToast(`${cr.id} deleted`);
  };

  const goBack = () => { setActiveCR(null); setView("dashboard"); };

  const filtered = filter==="all" ? crs : crs.filter(c=>c.status===filter);

  if (loading) return (
    <div style={{ fontFamily:"system-ui", display:"flex", alignItems:"center",
      justifyContent:"center", height:"100vh", background:"#F0F2F8", color:"#6B7280" }}>
      Loading change requests...
    </div>
  );

  return (
    <div style={{ fontFamily:"'IBM Plex Sans', system-ui, sans-serif",
      minHeight:"100vh", background:"#F0F2F8" }}>

      {/* Header */}
      <div style={{ background:"#1E3264", padding:"0 24px", height:56,
        display:"flex", alignItems:"center", justifyContent:"space-between",
        boxShadow:"0 2px 8px rgba(0,0,0,0.15)" }}>
        <div style={{ display:"flex", alignItems:"center", gap:10 }}>
          {view !== "dashboard" && (
            <button onClick={goBack} style={{ background:"rgba(255,255,255,0.12)", border:"none",
              color:"rgba(255,255,255,0.9)", borderRadius:6, padding:"4px 10px",
              cursor:"pointer", fontSize:12, fontFamily:"inherit", fontWeight:500 }}>
              ← All CRs
            </button>
          )}
          <span style={{ color:"#fff", fontWeight:600, fontSize:14, letterSpacing:"-0.01em" }}>
            Change Request Management
          </span>
          {activeCR && (
            <span style={{ color:"rgba(255,255,255,0.4)", fontSize:12,
              fontFamily:"'IBM Plex Mono', monospace" }}>
              / {activeCR.id}
            </span>
          )}
        </div>
        {view === "dashboard" && (
          <Btn variant="blue" onClick={()=>{ setActiveCR(makeCR()); setView("form"); }}>
            + New Change Request
          </Btn>
        )}
      </div>

      {/* Body */}
      <div style={{ padding:20 }}>
        {view === "dashboard" && (
          <Dashboard crs={filtered} allCRs={crs} statusFilter={filter}
            setStatusFilter={setFilter}
            onEdit={cr=>{ setActiveCR(cr); setView("form"); }}
            onChecklist={cr=>{ setActiveCR(cr); setView("checklist"); }}
            onStatusChange={handleStatusChange}
            onDelete={handleDelete} />
        )}
        {view === "form" && activeCR && (
          <CRForm cr={activeCR} onSave={handleSave}
            onStatusChange={(status)=>handleStatusChange(activeCR, status)}
            onChecklist={()=>setView("checklist")} />
        )}
        {view === "checklist" && activeCR && (
          <ChecklistView cr={activeCR} onSave={async(cr)=>{ const s=await handleSave(cr); setActiveCR(s); return s; }}
            onEdit={()=>setView("form")}
            onStatusChange={(status)=>handleStatusChange(activeCR, status)} />
        )}
      </div>

      {/* Toast */}
      {toast && (
        <div style={{ position:"fixed", bottom:24, right:24,
          background:toast.type==="error"?"#EF4444":"#10B981",
          color:"#fff", padding:"10px 18px", borderRadius:8,
          fontSize:13, fontWeight:600, boxShadow:"0 4px 12px rgba(0,0,0,0.15)",
          animation:"fadeIn 0.2s ease" }}>
          {toast.msg}
        </div>
      )}
    </div>
  );
}
