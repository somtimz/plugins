import { useState, useEffect } from "react";

const STATUS = {
  DRAFT:    "Draft",
  PENDING:  "Pending CAB Approval",
  APPROVED: "Approved by CAB",
  REJECTED: "Rejected",
};

const P_STYLE = {
  Low:      { bg:"#ECFDF5", text:"#065F46" },
  Medium:   { bg:"#EFF6FF", text:"#1E40AF" },
  High:     { bg:"#FFF7ED", text:"#9A3412" },
  Critical: { bg:"#FEF2F2", text:"#991B1B" },
};

const RISK_COLOR = { Low:"#10B981", Medium:"#F59E0B", High:"#EF4444" };

const APPROVERS_MAP = {
  a1:{ name:"Sarah Johnson",   role:"IT Director" },
  a2:{ name:"Mark Chen",       role:"Application Owner" },
  a3:{ name:"Lisa Patel",      role:"Security Lead" },
  a4:{ name:"David Williams",  role:"Infrastructure Manager" },
  a5:{ name:"Jennifer Torres", role:"Change Manager" },
  a6:{ name:"Robert Kim",      role:"Database Administrator" },
  a7:{ name:"Amanda Foster",   role:"Network Lead" },
  a8:{ name:"Michael Osei",    role:"CISO" },
};

// ─── Storage ─────────────────────────────────────────────────────────────────

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

// ─── UI primitives ────────────────────────────────────────────────────────────

function Card({ children, style }) {
  return (
    <div style={{ background:"#fff", borderRadius:10,
      boxShadow:"0 1px 4px rgba(0,0,0,0.07)", border:"1px solid #E8ECF4", ...style }}>
      {children}
    </div>
  );
}

function Btn({ children, onClick, variant="primary", disabled }) {
  const variants = {
    primary: { background:"#1E3264", color:"#fff" },
    green:   { background:"#10B981", color:"#fff" },
    red:     { background:"#EF4444", color:"#fff" },
    ghost:   { background:"#F3F4F6", color:"#374151" },
    amber:   { background:"#F59E0B", color:"#fff" },
  };
  return (
    <button onClick={onClick} disabled={disabled}
      style={{ border:"none", borderRadius:7, cursor:disabled?"not-allowed":"pointer",
        fontWeight:600, fontSize:13, padding:"8px 16px", fontFamily:"inherit",
        opacity:disabled?0.5:1, ...variants[variant] }}>
      {children}
    </button>
  );
}

function SectionHead({ title }) {
  return (
    <div style={{ fontSize:11, fontWeight:700, letterSpacing:"0.08em", color:"#6B7280",
      textTransform:"uppercase", marginBottom:12, paddingBottom:8,
      borderBottom:"2px solid #E8ECF4" }}>
      {title}
    </div>
  );
}

function Field({ label, value, mono }) {
  if (!value) return null;
  return (
    <div style={{ marginBottom:10 }}>
      <div style={{ fontSize:11, fontWeight:700, color:"#9CA3AF",
        letterSpacing:"0.05em", textTransform:"uppercase", marginBottom:3 }}>{label}</div>
      <div style={{ fontSize:13, color:"#111",
        fontFamily: mono ? "'IBM Plex Mono', monospace" : "inherit",
        lineHeight:1.5 }}>{value}</div>
    </div>
  );
}

// ─── CR Detail panel ─────────────────────────────────────────────────────────

function CRDetail({ cr, onDecision, deciding }) {
  return (
    <div style={{ maxWidth:760, margin:"0 auto" }}>

      {/* Header card */}
      <Card style={{ padding:20, marginBottom:14 }}>
        <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-start" }}>
          <div>
            <span style={{ fontSize:11, color:"#9CA3AF",
              fontFamily:"'IBM Plex Mono',monospace", fontWeight:600 }}>{cr.id}</span>
            <h2 style={{ fontSize:18, fontWeight:700, color:"#111", margin:"4px 0 8px" }}>
              {cr.title || "Untitled"}
            </h2>
            <div style={{ display:"flex", gap:8, flexWrap:"wrap" }}>
              <span style={{ background:"#FEF3C7", color:"#92400E",
                padding:"3px 10px", borderRadius:20, fontSize:11, fontWeight:700 }}>
                ⏳ PENDING CAB APPROVAL
              </span>
              <span style={{ background: P_STYLE[cr.priority]?.bg, color:P_STYLE[cr.priority]?.text,
                padding:"3px 8px", borderRadius:4, fontSize:11, fontWeight:700 }}>
                {cr.priority?.toUpperCase()}
              </span>
              <span style={{ background:"#F3F4F6", color:"#374151",
                padding:"3px 8px", borderRadius:4, fontSize:11 }}>
                {cr.changeType}
              </span>
            </div>
          </div>
          <div style={{ textAlign:"right", fontSize:12, color:"#6B7280" }}>
            <div>Submitted {new Date(cr.updatedAt).toLocaleDateString()}</div>
            <div style={{ marginTop:2 }}>Owner: <strong>{cr.changeOwner || "—"}</strong></div>
          </div>
        </div>
      </Card>

      {/* Content grid */}
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:14, marginBottom:14 }}>
        <Card style={{ padding:18 }}>
          <SectionHead title="Overview" />
          <Field label="Change Description" value={cr.changeDescription} />
          <Field label="Business Justification" value={cr.businessJustification} />
          <Field label="Affected Systems" value={cr.affectedSystems} />
          <Field label="Requested By" value={cr.requestedBy} />
        </Card>

        <Card style={{ padding:18 }}>
          <SectionHead title="Change Window" />
          <Field label="Proposed Start" value={cr.changeWindow?.start} />
          <Field label="Duration" value={cr.changeWindow?.duration} />
          <Field label="Maintenance Window" value={cr.changeWindow?.maintenanceWindow} />
          <div style={{ marginTop:14 }}>
            <SectionHead title="Risk Assessment" />
            <div style={{ display:"flex", alignItems:"center", gap:8, marginBottom:8 }}>
              <span style={{ fontSize:12, fontWeight:700, color:"#4B5563" }}>Risk Level:</span>
              <span style={{ fontWeight:700, fontSize:14,
                color:RISK_COLOR[cr.riskLevel]||"#6B7280" }}>{cr.riskLevel}</span>
            </div>
            <Field label="Impact if Change Fails" value={cr.riskImpact} />
            <Field label="Affected Users" value={cr.riskUsers} />
            <Field label="Dependencies" value={cr.riskDeps} />
          </div>
        </Card>
      </div>

      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:14, marginBottom:14 }}>
        <Card style={{ padding:18 }}>
          <SectionHead title="Implementation Steps" />
          {(cr.implSteps||[]).filter(s=>s.text).map((s,i)=>(
            <div key={s.id} style={{ display:"flex", gap:8, marginBottom:6, fontSize:13, color:"#111" }}>
              <span style={{ color:"#9CA3AF", flexShrink:0 }}>{i+1}.</span>
              <span>{s.text}</span>
            </div>
          ))}
        </Card>
        <Card style={{ padding:18 }}>
          <SectionHead title="Rollback Plan" />
          {(cr.rollbackSteps||[]).filter(s=>s.text).map((s,i)=>(
            <div key={s.id} style={{ display:"flex", gap:8, marginBottom:6, fontSize:13, color:"#111" }}>
              <span style={{ color:"#9CA3AF", flexShrink:0 }}>{i+1}.</span>
              <span>{s.text}</span>
            </div>
          ))}
          <div style={{ marginTop:14 }}>
            <SectionHead title="Validation" />
            {(cr.validationItems||[]).filter(s=>s.text).map((s,i)=>(
              <div key={s.id} style={{ display:"flex", gap:8, marginBottom:6, fontSize:13, color:"#111" }}>
                <span style={{ color:"#9CA3AF" }}>•</span>
                <span>{s.text}</span>
              </div>
            ))}
          </div>
        </Card>
      </div>

      {/* Approvers */}
      {cr.approverIds?.length > 0 && (
        <Card style={{ padding:18, marginBottom:14 }}>
          <SectionHead title="Requested Approvers" />
          <div style={{ display:"flex", gap:8, flexWrap:"wrap" }}>
            {cr.approverIds.map(id => {
              const a = APPROVERS_MAP[id];
              return a ? (
                <div key={id} style={{ background:"#F8FAFF", border:"1px solid #E0E7FF",
                  borderRadius:7, padding:"6px 12px" }}>
                  <div style={{ fontSize:12, fontWeight:600 }}>{a.name}</div>
                  <div style={{ fontSize:11, color:"#6B7280" }}>{a.role}</div>
                </div>
              ) : null;
            })}
          </div>
        </Card>
      )}

      {/* Decision box */}
      <Card style={{ padding:20, border:"2px solid #E0E7FF", marginBottom:24 }}>
        <SectionHead title="CAB Decision" />
        <div style={{ marginBottom:14 }}>
          <label style={{ display:"block", fontSize:12, fontWeight:600,
            color:"#4B5563", marginBottom:6 }}>Notes (optional)</label>
          <textarea
            value={cr._cabDraft || ""}
            onChange={e => onDecision("_note", e.target.value)}
            rows={3}
            placeholder="Add conditions, concerns, or approval notes..."
            style={{ width:"100%", padding:"8px 10px", border:"1.5px solid #D1D5DB",
              borderRadius:7, fontSize:13, fontFamily:"inherit", resize:"vertical",
              background:"#fff", outline:"none" }}
          />
        </div>
        <div style={{ display:"flex", gap:10 }}>
          <Btn variant="green" onClick={()=>onDecision("approve")} disabled={deciding}>
            ✓ Approve
          </Btn>
          <Btn variant="red" onClick={()=>onDecision("reject")} disabled={deciding}>
            ✗ Reject
          </Btn>
          <Btn variant="ghost" onClick={()=>onDecision("back")}>Back to list</Btn>
        </div>
      </Card>
    </div>
  );
}

// ─── Root ─────────────────────────────────────────────────────────────────────

export default function CABReview() {
  const [crs, setCRs]         = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);
  const [deciding, setDeciding] = useState(false);
  const [toast, setToast]     = useState(null);
  const [noteVal, setNoteVal] = useState("");

  useEffect(() => {
    const link = document.createElement("link");
    link.rel  = "stylesheet";
    link.href = "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@600&display=swap";
    document.head.appendChild(link);
    getCRs().then(all => {
      const pending = all.filter(c => c.status === STATUS.PENDING)
        .sort((a,b)=>new Date(b.updatedAt)-new Date(a.updatedAt));
      setCRs(pending);
      setLoading(false);
    });
  }, []);

  const showToast = (msg, type="success") => {
    setToast({ msg, type });
    setTimeout(() => setToast(null), 3000);
  };

  const handleDecision = async (action, noteText) => {
    if (action === "back") { setSelected(null); setNoteVal(""); return; }
    if (action === "_note") { setNoteVal(noteText); return; }

    setDeciding(true);
    const newStatus = action === "approve" ? STATUS.APPROVED : STATUS.REJECTED;
    const historyEntry = {
      action,
      notes: noteVal,
      timestamp: new Date().toISOString(),
    };
    const updated = {
      ...selected,
      status: newStatus,
      cabNotes: noteVal,
      cabHistory: [...(selected.cabHistory || []), historyEntry],
    };
    const saved = await putCR(updated);

    setCRs(prev => prev.filter(c => c.id !== saved.id));
    setSelected(null);
    setNoteVal("");
    setDeciding(false);
    showToast(action === "approve" ? `${saved.id} approved ✓` : `${saved.id} rejected`, action === "approve" ? "success" : "error");
  };

  if (loading) return (
    <div style={{ fontFamily:"system-ui", display:"flex", alignItems:"center",
      justifyContent:"center", height:"100vh", background:"#F0F2F8", color:"#6B7280" }}>
      Loading...
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
          {selected && (
            <button onClick={()=>{ setSelected(null); setNoteVal(""); }}
              style={{ background:"rgba(255,255,255,0.12)", border:"none",
                color:"rgba(255,255,255,0.9)", borderRadius:6, padding:"4px 10px",
                cursor:"pointer", fontSize:12, fontFamily:"inherit" }}>
              ← Pending List
            </button>
          )}
          <span style={{ color:"#fff", fontWeight:600, fontSize:14 }}>
            CAB Review
          </span>
          {selected && (
            <span style={{ color:"rgba(255,255,255,0.4)", fontSize:12,
              fontFamily:"'IBM Plex Mono',monospace" }}>
              / {selected.id}
            </span>
          )}
        </div>
        <span style={{ background:"#F59E0B", color:"#fff", borderRadius:20,
          padding:"3px 12px", fontSize:12, fontWeight:700 }}>
          {crs.length} Pending
        </span>
      </div>

      <div style={{ padding:20 }}>
        {!selected ? (
          /* Pending list */
          <div style={{ maxWidth:760, margin:"0 auto" }}>
            {crs.length === 0 ? (
              <Card style={{ padding:48, textAlign:"center" }}>
                <div style={{ fontSize:36, marginBottom:10 }}>✅</div>
                <div style={{ fontSize:16, fontWeight:600, color:"#374151", marginBottom:4 }}>
                  All clear — no pending CRs
                </div>
                <div style={{ fontSize:13, color:"#9CA3AF" }}>
                  Change requests submitted for CAB approval will appear here.
                </div>
              </Card>
            ) : (
              <>
                <div style={{ fontSize:13, color:"#6B7280", marginBottom:14 }}>
                  {crs.length} change request{crs.length>1?"s":""} awaiting your decision. Click one to review.
                </div>
                <div style={{ display:"flex", flexDirection:"column", gap:10 }}>
                  {crs.map(cr => (
                    <Card key={cr.id} style={{ padding:"16px 20px", cursor:"pointer",
                      transition:"box-shadow 0.15s" }}
                      onClick={()=>{ setSelected(cr); setNoteVal(""); }}>
                      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"flex-start" }}>
                        <div>
                          <div style={{ display:"flex", gap:8, alignItems:"center", marginBottom:5 }}>
                            <span style={{ fontSize:11, color:"#9CA3AF",
                              fontFamily:"'IBM Plex Mono',monospace", fontWeight:600 }}>{cr.id}</span>
                            <span style={{ background:P_STYLE[cr.priority]?.bg,
                              color:P_STYLE[cr.priority]?.text,
                              padding:"2px 7px", borderRadius:4, fontSize:11, fontWeight:700 }}>
                              {cr.priority?.toUpperCase()}
                            </span>
                            <span style={{ background:"#FFF7ED", color:"#9A3412",
                              padding:"2px 7px", borderRadius:4, fontSize:11, fontWeight:600 }}>
                              Risk: <strong style={{ color:RISK_COLOR[cr.riskLevel] }}>{cr.riskLevel}</strong>
                            </span>
                          </div>
                          <div style={{ fontSize:14, fontWeight:600, color:"#111", marginBottom:3 }}>
                            {cr.title || "Untitled"}
                          </div>
                          <div style={{ fontSize:12, color:"#6B7280" }}>
                            {cr.changeType} · Owner: {cr.changeOwner||"—"} · {cr.changeWindow?.start || "No window set"}
                          </div>
                        </div>
                        <span style={{ fontSize:12, color:"#3B82F6", fontWeight:600, flexShrink:0 }}>
                          Review →
                        </span>
                      </div>
                    </Card>
                  ))}
                </div>
              </>
            )}
          </div>
        ) : (
          <CRDetail
            cr={{ ...selected, _cabDraft: noteVal }}
            onDecision={handleDecision}
            deciding={deciding}
          />
        )}
      </div>

      {toast && (
        <div style={{ position:"fixed", bottom:24, right:24,
          background:toast.type==="error"?"#EF4444":"#10B981",
          color:"#fff", padding:"10px 18px", borderRadius:8,
          fontSize:13, fontWeight:600, boxShadow:"0 4px 12px rgba(0,0,0,0.15)" }}>
          {toast.msg}
        </div>
      )}
    </div>
  );
}
