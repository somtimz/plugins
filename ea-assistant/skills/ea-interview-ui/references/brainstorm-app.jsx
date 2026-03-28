import { useState, useRef, useEffect } from "react";

// ─── Brainstorm Data (injected at runtime — null fields = generic defaults) ────
//
// Shape injected by ea-brainstorm.md at render time:
//
//   const BRAINSTORM_DATA = {
//     phase: "Phase D — Technology Architecture",   // null = no phase badge
//     subtitle: "Focus on platform, infrastructure, and technical decisions.",  // null = generic
//     categories: [                                 // null = use all defaults
//       { id: "concerns",      hint: "Platform lock-in, security posture, technical debt, skills gaps",
//         suggestions: ["Legacy platform creates vendor lock-in with no viable migration path",
//                       "Security posture is immature — no zero-trust controls in place"] },
//       { id: "goals",         hint: "Target platform, infrastructure principles, cloud/hybrid strategy",
//         suggestions: ["Cloud-native platform with container-first deployment",
//                       "Hybrid cloud balancing on-prem for regulated data and public cloud for scale"] },
//       // ... other categories — suggestions is optional, null if omitted
//     ],
//   };

const BRAINSTORM_DATA = {
  phase: null,
  subtitle: null,
  categories: null,
};


// ─── Default Categories ────────────────────────────────────────────────────────

const DEFAULT_CATEGORIES = [
  { id: "concerns",      label: "Concerns",        emoji: "⚠️", hint: "Risks, worries, unknowns" },
  { id: "goals",         label: "Goals & Vision",   emoji: "🎯", hint: "Desired outcomes, strategic intent" },
  { id: "constraints",   label: "Constraints",      emoji: "🔒", hint: "Budget, time, tech, or organisational limits" },
  { id: "opportunities", label: "Opportunities",    emoji: "💡", hint: "Potential wins, improvements, innovations" },
  { id: "assumptions",   label: "Assumptions",      emoji: "🔮", hint: "Things taken as true without confirmation" },
  { id: "other",         label: "Other",            emoji: "📝", hint: "Anything that doesn't fit above" },
];

// Merge phase-specific hint and suggestion overrides into the default category list
const _catOverrides = BRAINSTORM_DATA.categories
  ? Object.fromEntries(BRAINSTORM_DATA.categories.map(c => [c.id, c]))
  : {};
const CATEGORIES = DEFAULT_CATEGORIES.map(c => {
  const ov = _catOverrides[c.id];
  if (!ov) return c;
  return { ...c, hint: ov.hint ?? c.hint, suggestions: ov.suggestions ?? null };
});


// ─── CategoryCard ─────────────────────────────────────────────────────────────

function ThoughtStarters({ suggestions, onAdd }) {
  const [open, setOpen] = useState(false);
  if (!suggestions || suggestions.length === 0) return null;
  return (
    <div style={{ marginBottom: 10 }}>
      <button
        onClick={() => setOpen(o => !o)}
        style={{
          padding: "4px 10px", borderRadius: 6, border: "1px dashed #C7D2FE",
          background: "transparent", color: "#6366F1", fontSize: 12, cursor: "pointer",
          fontFamily: "inherit",
        }}
      >
        💡 Thought starters {open ? "▴" : "▾"}
      </button>
      {open && (
        <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginTop: 8 }}>
          {suggestions.map((s, i) => (
            <button
              key={i}
              onClick={() => onAdd(s)}
              title="Click to add as a thought"
              style={{
                padding: "5px 12px", borderRadius: 999,
                border: "1.5px solid #C7D2FE",
                background: "#EEF2FF", color: "#4338CA",
                fontSize: 12, cursor: "pointer", fontFamily: "inherit",
              }}
            >
              + {s}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function CategoryCard({ cat, thoughts, onUpdate, onAdd, onRemove, autoFocusLast }) {
  const lastRef = useRef(null);
  const [collapsed, setCollapsed] = useState(false);

  useEffect(() => {
    if (autoFocusLast && lastRef.current) {
      lastRef.current.focus();
    }
  }, [thoughts.length, autoFocusLast]);

  const filledCount = thoughts.filter(t => t.trim()).length;

  return (
    <div style={{
      background: "#fff", borderRadius: 12, marginBottom: 12,
      boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      overflow: "hidden",
    }}>
      {/* Header row */}
      <button
        onClick={() => setCollapsed(c => !c)}
        style={{
          display: "flex", alignItems: "center", gap: 10, width: "100%",
          padding: "14px 18px", background: "transparent", border: "none",
          cursor: "pointer", textAlign: "left",
        }}
      >
        <span style={{ fontSize: 18 }}>{cat.emoji}</span>
        <div style={{ flex: 1 }}>
          <div style={{ fontSize: 14, fontWeight: 700, color: "#111827" }}>{cat.label}</div>
          <div style={{ fontSize: 12, color: "#9CA3AF" }}>{cat.hint}</div>
        </div>
        {filledCount > 0 && (
          <span style={{
            padding: "2px 10px", borderRadius: 999,
            background: "#EEF2FF", color: "#4338CA",
            fontSize: 12, fontWeight: 700,
          }}>
            {filledCount}
          </span>
        )}
        <span style={{ fontSize: 12, color: "#9CA3AF", marginLeft: 4 }}>
          {collapsed ? "▸" : "▾"}
        </span>
      </button>

      {/* Inputs */}
      {!collapsed && (
        <div style={{ padding: "0 18px 16px" }}>
          <ThoughtStarters suggestions={cat.suggestions} onAdd={v => onAdd(v)} />
          {thoughts.map((thought, i) => (
            <div key={i} style={{ display: "flex", gap: 8, marginBottom: 8, alignItems: "flex-start" }}>
              <textarea
                ref={i === thoughts.length - 1 ? lastRef : null}
                style={{
                  flex: 1, padding: "8px 10px", minHeight: 60,
                  border: "1.5px solid #E5E7EB", borderRadius: 8,
                  fontSize: 13, fontFamily: "inherit", color: "#111827",
                  resize: "vertical", outline: "none",
                  transition: "border-color 0.15s",
                }}
                placeholder={`Add a ${cat.label.toLowerCase()} thought…`}
                value={thought}
                onChange={e => onUpdate(i, e.target.value)}
                onFocus={e => { e.target.style.borderColor = "#6366F1"; }}
                onBlur={e => { e.target.style.borderColor = "#E5E7EB"; }}
                onKeyDown={e => {
                  if (e.key === "Enter" && !e.shiftKey) {
                    e.preventDefault();
                    if (thought.trim() && i === thoughts.length - 1) onAdd();
                  }
                }}
              />
              {thoughts.length > 1 && (
                <button
                  onClick={() => onRemove(i)}
                  style={{
                    padding: "6px 8px", marginTop: 2, borderRadius: 6,
                    border: "1px solid #E5E7EB", background: "transparent",
                    color: "#9CA3AF", fontSize: 14, cursor: "pointer",
                    lineHeight: 1,
                  }}
                >
                  ×
                </button>
              )}
            </div>
          ))}
          <button
            onClick={onAdd}
            style={{
              padding: "6px 14px", borderRadius: 7,
              border: "1px dashed #D1D5DB", background: "transparent",
              color: "#9CA3AF", fontSize: 12, cursor: "pointer",
              marginTop: 2,
            }}
          >
            + Add thought
          </button>
        </div>
      )}
    </div>
  );
}

// ─── Result Screen ─────────────────────────────────────────────────────────────

function ResultScreen({ thoughts, onBack }) {
  const [copied, setCopied] = useState(false);

  function buildOutput() {
    const lines = ["BRAINSTORM NOTES", "---"];
    if (BRAINSTORM_DATA.phase) lines.push(`Phase: ${BRAINSTORM_DATA.phase}`);
    for (const cat of CATEGORIES) {
      const filled = thoughts[cat.id].filter(t => t.trim());
      if (filled.length) {
        lines.push(`\n### ${cat.label}`);
        filled.forEach(t => lines.push(`- ${t.trim()}`));
      }
    }
    return lines.join("\n");
  }

  const output = buildOutput();

  function copy() {
    navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  }

  return (
    <div>
      <h2 style={{ fontSize: 20, fontWeight: 700, color: "#111827", margin: "0 0 6px" }}>
        Notes ready
      </h2>
      <p style={{ fontSize: 13, color: "#6B7280", margin: "0 0 20px" }}>
        Copy and paste into the chat — Claude will organise and save them.
      </p>

      <pre style={{
        background: "#F3F4F6", borderRadius: 10, padding: "16px 18px",
        fontSize: 13, color: "#374151", lineHeight: 1.65,
        whiteSpace: "pre-wrap", wordBreak: "break-word",
        fontFamily: "'Fira Code', 'Menlo', monospace",
        marginBottom: 16,
      }}>
        {output}
      </pre>

      <button
        onClick={copy}
        style={{
          display: "block", width: "100%", padding: "13px 20px",
          borderRadius: 10, border: "none",
          background: copied ? "#059669" : "#6366F1", color: "#fff",
          fontSize: 15, fontWeight: 700, cursor: "pointer",
          transition: "background 0.3s", marginBottom: 12,
        }}
      >
        {copied ? "✓ Copied!" : "Copy to clipboard"}
      </button>

      <button
        onClick={onBack}
        style={{
          display: "block", width: "100%", padding: "11px 20px",
          borderRadius: 10, border: "1px solid #E5E7EB", background: "transparent",
          color: "#6B7280", fontSize: 14, cursor: "pointer",
        }}
      >
        ← Back to edit
      </button>
    </div>
  );
}

// ─── Main App ─────────────────────────────────────────────────────────────────

export default function BrainstormPad() {
  const empty = () => Object.fromEntries(CATEGORIES.map(c => [c.id, [""]]));

  const [thoughts, setThoughts] = useState(empty);
  const [screen, setScreen] = useState("input"); // "input" | "result"
  const [lastAddedCat, setLastAddedCat] = useState(null);

  function updateThought(catId, idx, val) {
    setThoughts(t => {
      const arr = [...t[catId]];
      arr[idx] = val;
      return { ...t, [catId]: arr };
    });
  }

  function addThought(catId, prefill = "") {
    setThoughts(t => ({ ...t, [catId]: [...t[catId], prefill] }));
    setLastAddedCat(catId);
  }

  function removeThought(catId, idx) {
    setThoughts(t => {
      const arr = t[catId].filter((_, i) => i !== idx);
      return { ...t, [catId]: arr.length ? arr : [""] };
    });
  }

  const hasContent = CATEGORIES.some(c => thoughts[c.id].some(t => t.trim()));

  return (
    <div style={{
      fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      maxWidth: 640, margin: "0 auto", padding: "24px 20px",
      background: "#F9FAFB", minHeight: "100vh", boxSizing: "border-box",
    }}>
      {/* Header */}
      <div style={{ marginBottom: 24 }}>
        <div style={{ fontSize: 11, fontWeight: 700, color: "#6366F1", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: 4 }}>
          EA Brainstorm{BRAINSTORM_DATA.phase ? ` · ${BRAINSTORM_DATA.phase}` : ""}
        </div>
        <h1 style={{ fontSize: 22, fontWeight: 800, color: "#111827", margin: "0 0 4px" }}>
          What's on your mind?
        </h1>
        <p style={{ fontSize: 13, color: "#9CA3AF", margin: 0 }}>
          {BRAINSTORM_DATA.subtitle || "Capture thoughts freely — no wrong answers. Press Enter to add another thought."}
        </p>
      </div>

      {screen === "input" ? (
        <>
          {CATEGORIES.map(cat => (
            <CategoryCard
              key={cat.id}
              cat={cat}
              thoughts={thoughts[cat.id]}
              onUpdate={(i, v) => updateThought(cat.id, i, v)}
              onAdd={(v) => addThought(cat.id, v)}
              onRemove={i => removeThought(cat.id, i)}
              autoFocusLast={lastAddedCat === cat.id}
            />
          ))}

          <div style={{ display: "flex", gap: 10, marginTop: 8 }}>
            <button
              onClick={() => setThoughts(empty())}
              style={{
                padding: "10px 18px", borderRadius: 8, border: "1px solid #E5E7EB",
                background: "transparent", color: "#9CA3AF", fontSize: 13, cursor: "pointer",
              }}
            >
              Clear all
            </button>
            <button
              onClick={() => setScreen("result")}
              disabled={!hasContent}
              style={{
                flex: 1, padding: "12px 20px", borderRadius: 8, border: "none",
                background: hasContent ? "#6366F1" : "#E5E7EB",
                color: hasContent ? "#fff" : "#9CA3AF",
                fontSize: 14, fontWeight: 700,
                cursor: hasContent ? "pointer" : "default",
                transition: "background 0.15s",
              }}
            >
              Done — show notes →
            </button>
          </div>
        </>
      ) : (
        <ResultScreen thoughts={thoughts} onBack={() => setScreen("input")} />
      )}
    </div>
  );
}
