import { useState, useEffect, useRef } from "react";


// ─── Data injected by Claude before presenting this artifact ─────────────────
// Claude replaces INTERVIEW_DATA with the actual engagement/artifact context.
// Shape:
//   artifactName: string
//   engagementName: string
//   mode: "artifact" | "phase"          // artifact Q&A vs. phase question bank
//   questions: Array<{
//     id: string,
//     text: string,
//     context: string,                   // one-sentence "why it matters"
//     defaultAnswer: string | null,
//     existingAnswer: string | null,     // from previous session / imported doc
//     brainstormNote: string | null,     // relevant thought from brainstorm notes
//     options: Array<string> | null,     // if set, renders as a checklist/radio list
//     allowMultiple: boolean,            // true = checkboxes (default), false = radio (select one)
//   }>

const INTERVIEW_DATA = {
  artifactName: "Architecture Vision",
  engagementName: "My Engagement",
  mode: "artifact",
  questions: [
    {
      id: "q1",
      text: "What is the strategic intent of this engagement?",
      context: "This anchors all subsequent architecture decisions to a clear business purpose.",
      defaultAnswer: null,
      existingAnswer: null,
      brainstormNote: null,
      options: null,
      allowMultiple: true,
    },
  ],
};

// ─── Constants ────────────────────────────────────────────────────────────────

const ANSWER_STATE = {
  answered:         { label: "Answered",        bg: "#D1FAE5", text: "#065F46" },
  default_accepted: { label: "Default Accepted", bg: "#DBEAFE", text: "#1E40AF" },
  skipped:          { label: "Skipped",          bg: "#FEF9C3", text: "#854D0E" },
  na:               { label: "N/A",              bg: "#F3F4F6", text: "#4B5563" },
};


// ─── Components ───────────────────────────────────────────────────────────────

function Badge({ state }) {
  const s = ANSWER_STATE[state];
  if (!s) return null;
  return (
    <span style={{
      display: "inline-block", padding: "2px 10px", borderRadius: 999,
      fontSize: 11, fontWeight: 700, letterSpacing: "0.03em",
      background: s.bg, color: s.text,
    }}>
      {s.label}
    </span>
  );
}

function ProgressBar({ answered, total }) {
  const pct = total > 0 ? Math.round((answered / total) * 100) : 0;
  return (
    <div>
      <div style={{ height: 6, background: "#E5E7EB", borderRadius: 999, overflow: "hidden", marginBottom: 6 }}>
        <div style={{
          height: "100%", borderRadius: 999,
          background: "linear-gradient(90deg, #6366F1, #818CF8)",
          width: `${pct}%`, transition: "width 0.4s ease",
        }} />
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, color: "#9CA3AF" }}>
        <span>{answered} of {total} answered</span>
        <span>{pct}%</span>
      </div>
    </div>
  );
}

function OptionSelector({ options, allowMultiple, checked, onChange }) {
  function toggle(opt) {
    if (allowMultiple) {
      if (checked.includes(opt)) onChange(checked.filter(o => o !== opt));
      else onChange([...checked, opt]);
    } else {
      onChange(checked.includes(opt) ? [] : [opt]);
    }
  }
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 8, marginBottom: 14 }}>
      {options.map(opt => {
        const isChecked = checked.includes(opt);
        return (
          <label key={opt} style={{
            display: "flex", alignItems: "flex-start", gap: 10, cursor: "pointer",
            padding: "9px 12px", borderRadius: 8,
            border: `1.5px solid ${isChecked ? "#6366F1" : "#E5E7EB"}`,
            background: isChecked ? "#EEF2FF" : "#fff",
            transition: "border-color 0.15s, background 0.15s",
          }}>
            <input
              type={allowMultiple ? "checkbox" : "radio"}
              checked={isChecked}
              onChange={() => toggle(opt)}
              style={{ marginTop: 2, accentColor: "#6366F1", flexShrink: 0 }}
            />
            <span style={{ fontSize: 14, color: "#374151", lineHeight: 1.4 }}>{opt}</span>
          </label>
        );
      })}
    </div>
  );
}

function QuestionCard({ q, qNum, total, onAnswer, inputVal, setInputVal, checkedVals, onCheckChange, onBack, onJumpToReview }) {
  const textareaRef = useRef(null);
  const hasOptions = q.options && q.options.length > 0;

  useEffect(() => {
    if (!hasOptions) textareaRef.current?.focus();
  }, [qNum]);

  function buildAnswerValue() {
    if (hasOptions) {
      const parts = [];
      if (checkedVals.length > 0) parts.push(checkedVals.join(", "));
      if (inputVal.trim()) parts.push(`Notes: ${inputVal.trim()}`);
      return parts.join(" — ");
    }
    return inputVal.trim();
  }

  const canSubmit = hasOptions
    ? (checkedVals.length > 0 || inputVal.trim().length > 0)
    : inputVal.trim().length > 0;

  const submit = () => {
    const v = buildAnswerValue();
    if (v) onAnswer(v, "answered");
  };

  return (
    <div>
      {/* Question number + progress */}
      <div style={{ marginBottom: 20 }}>
        <div style={{ fontSize: 12, fontWeight: 700, color: "#6366F1", textTransform: "uppercase", letterSpacing: "0.06em", marginBottom: 4 }}>
          Question {qNum} of {total}
        </div>
        <ProgressBar answered={qNum - 1} total={total} />
      </div>

      {/* Card */}
      <div style={{
        background: "#fff", borderRadius: 14, padding: 28,
        boxShadow: "0 1px 4px rgba(0,0,0,0.08), 0 4px 16px rgba(0,0,0,0.04)",
        marginBottom: 16,
      }}>
        <h2 style={{ fontSize: 20, fontWeight: 700, color: "#111827", lineHeight: 1.35, margin: "0 0 8px" }}>
          {q.text}
        </h2>

        {q.context && (
          <p style={{ fontSize: 13, color: "#6B7280", lineHeight: 1.55, margin: "0 0 16px" }}>
            {q.context}
          </p>
        )}

        {q.brainstormNote && (
          <div style={{
            background: "#EFF6FF", border: "1px solid #BFDBFE",
            borderRadius: 8, padding: "10px 14px", marginBottom: 14,
            fontSize: 13, color: "#1D4ED8", lineHeight: 1.5,
          }}>
            💭 <strong>From your brainstorm:</strong> {q.brainstormNote}
          </div>
        )}

        {q.existingAnswer && (
          <div style={{
            background: "#FFF7ED", border: "1px solid #FED7AA",
            borderRadius: 8, padding: "10px 14px", marginBottom: 14,
            fontSize: 13, color: "#C2410C", lineHeight: 1.5,
          }}>
            📎 <strong>Previous answer:</strong> {q.existingAnswer}
          </div>
        )}

        {/* Checklist or free-text input */}
        {hasOptions ? (
          <>
            <OptionSelector
              options={q.options}
              allowMultiple={q.allowMultiple !== false}
              checked={checkedVals}
              onChange={onCheckChange}
            />
            <textarea
              ref={textareaRef}
              style={{
                width: "100%", minHeight: 60, padding: "10px 12px",
                border: "1.5px solid #E5E7EB", borderRadius: 8,
                fontSize: 14, fontFamily: "inherit", color: "#111827",
                resize: "vertical", outline: "none", boxSizing: "border-box",
                transition: "border-color 0.15s",
              }}
              placeholder="Additional notes (optional)"
              value={inputVal}
              onChange={e => setInputVal(e.target.value)}
              onFocus={e => { e.target.style.borderColor = "#6366F1"; }}
              onBlur={e => { e.target.style.borderColor = "#E5E7EB"; }}
              onKeyDown={e => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) submit(); }}
            />
          </>
        ) : (
          <textarea
            ref={textareaRef}
            style={{
              width: "100%", minHeight: 90, padding: "10px 12px",
              border: "1.5px solid #E5E7EB", borderRadius: 8,
              fontSize: 14, fontFamily: "inherit", color: "#111827",
              resize: "vertical", outline: "none", boxSizing: "border-box",
              transition: "border-color 0.15s",
            }}
            placeholder="Type your answer… (Ctrl+Enter to submit)"
            value={inputVal}
            onChange={e => setInputVal(e.target.value)}
            onFocus={e => { e.target.style.borderColor = "#6366F1"; }}
            onBlur={e => { e.target.style.borderColor = "#E5E7EB"; }}
            onKeyDown={e => { if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) submit(); }}
          />
        )}

        {/* Action buttons */}
        <div style={{ display: "flex", gap: 8, marginTop: 10, flexWrap: "wrap", alignItems: "center" }}>
          <button
            onClick={submit}
            disabled={!canSubmit}
            style={{
              padding: "9px 18px", borderRadius: 8, border: "none",
              background: canSubmit ? "#6366F1" : "#E5E7EB",
              color: canSubmit ? "#fff" : "#9CA3AF",
              fontSize: 14, fontWeight: 600, cursor: canSubmit ? "pointer" : "default",
              transition: "background 0.15s",
            }}
          >
            Submit ↵
          </button>

          {q.defaultAnswer && (
            <button
              onClick={() => onAnswer(`${q.defaultAnswer}`, "default_accepted")}
              style={{
                padding: "9px 16px", borderRadius: 8, border: "none",
                background: "#EEF2FF", color: "#4338CA",
                fontSize: 13, fontWeight: 500, cursor: "pointer",
              }}
            >
              💡 Accept default
            </button>
          )}

          {q.existingAnswer && (
            <button
              onClick={() => onAnswer(q.existingAnswer, "answered")}
              style={{
                padding: "9px 16px", borderRadius: 8, border: "none",
                background: "#FFF7ED", color: "#C2410C",
                fontSize: 13, fontWeight: 500, cursor: "pointer",
              }}
            >
              📎 Keep previous
            </button>
          )}

          <div style={{ marginLeft: "auto", display: "flex", gap: 8 }}>
            <button
              onClick={() => onAnswer("", "skipped")}
              style={{ padding: "9px 14px", borderRadius: 8, border: "1px solid #E5E7EB", background: "transparent", color: "#6B7280", fontSize: 13, cursor: "pointer" }}
            >
              Skip
            </button>
            <button
              onClick={() => onAnswer("", "na")}
              style={{ padding: "9px 14px", borderRadius: 8, border: "1px solid #E5E7EB", background: "transparent", color: "#6B7280", fontSize: 13, cursor: "pointer" }}
            >
              N/A
            </button>
          </div>
        </div>
      </div>

      {/* Nav row */}
      <div style={{ display: "flex", gap: 8 }}>
        {qNum > 1 && (
          <button onClick={onBack} style={{ padding: "7px 14px", borderRadius: 7, border: "1px solid #E5E7EB", background: "transparent", color: "#6B7280", fontSize: 13, cursor: "pointer" }}>
            ← Back
          </button>
        )}
        <button onClick={onJumpToReview} style={{ padding: "7px 14px", borderRadius: 7, border: "1px solid #E5E7EB", background: "transparent", color: "#6366F1", fontSize: 13, cursor: "pointer", marginLeft: "auto" }}>
          Review answers →
        </button>
      </div>
    </div>
  );
}

function ReviewScreen({ questions, answers, onEdit, onDone }) {
  const [copied, setCopied] = useState(false);

  function buildOutput() {
    const lines = [
      `INTERVIEW RESULTS — ${INTERVIEW_DATA.artifactName}`,
      `Engagement: ${INTERVIEW_DATA.engagementName}`,
      `Date: ${new Date().toISOString().split("T")[0]}`,
      "---",
    ];
    questions.forEach((q, i) => {
      const a = answers[q.id];
      const state = a?.state ?? "skipped";
      const stateLabel = ANSWER_STATE[state]?.label ?? "Skipped";
      lines.push(`\nQ${i + 1} [${stateLabel}]: ${q.text}`);
      if (a?.value) lines.push(`Answer: ${a.value}`);
    });
    return lines.join("\n");
  }

  function copy() {
    navigator.clipboard.writeText(buildOutput());
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  }

  const counts = {
    answered: 0, default_accepted: 0, skipped: 0, na: 0, not_reached: 0,
  };
  questions.forEach(q => {
    const state = answers[q.id]?.state;
    if (state) counts[state] = (counts[state] || 0) + 1;
    else counts.not_reached++;
  });

  return (
    <div>
      <h2 style={{ fontSize: 20, fontWeight: 700, color: "#111827", margin: "0 0 4px" }}>
        Interview Complete
      </h2>
      <p style={{ fontSize: 13, color: "#6B7280", margin: "0 0 20px" }}>
        {INTERVIEW_DATA.artifactName} — {INTERVIEW_DATA.engagementName}
      </p>

      {/* Summary row */}
      <div style={{ display: "flex", gap: 10, marginBottom: 24, flexWrap: "wrap" }}>
        {[
          { label: "Answered", count: (counts.answered || 0) + (counts.default_accepted || 0), color: "#065F46", bg: "#D1FAE5" },
          { label: "Skipped",  count: counts.skipped || 0,  color: "#854D0E", bg: "#FEF9C3" },
          { label: "N/A",      count: counts.na || 0,       color: "#4B5563", bg: "#F3F4F6" },
        ].map(s => (
          <div key={s.label} style={{ padding: "8px 16px", borderRadius: 8, background: s.bg }}>
            <span style={{ fontSize: 18, fontWeight: 700, color: s.color }}>{s.count}</span>
            <span style={{ fontSize: 12, color: s.color, marginLeft: 6 }}>{s.label}</span>
          </div>
        ))}
      </div>

      {/* Per-question review */}
      {questions.map((q, i) => {
        const a = answers[q.id];
        const state = a?.state ?? "skipped";
        return (
          <div key={q.id} style={{
            background: "#fff", borderRadius: 10, padding: "14px 18px",
            marginBottom: 10, boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
          }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 4 }}>
              <span style={{ fontSize: 12, color: "#9CA3AF" }}>Q{i + 1}</span>
              <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
                <Badge state={state} />
                <button onClick={() => onEdit(i)} style={{ padding: "2px 10px", borderRadius: 6, border: "1px solid #E5E7EB", background: "transparent", fontSize: 12, color: "#6B7280", cursor: "pointer" }}>
                  Edit
                </button>
              </div>
            </div>
            <p style={{ fontSize: 14, fontWeight: 500, color: "#374151", margin: "0 0 4px" }}>{q.text}</p>
            {a?.value && <p style={{ fontSize: 13, color: "#6B7280", margin: 0 }}>{a.value}</p>}
          </div>
        );
      })}

      {/* Copy button */}
      <button
        onClick={copy}
        style={{
          display: "block", width: "100%", marginTop: 24,
          padding: "14px 20px", borderRadius: 10, border: "none",
          background: copied ? "#059669" : "#6366F1", color: "#fff",
          fontSize: 15, fontWeight: 700, cursor: "pointer",
          transition: "background 0.3s",
        }}
      >
        {copied ? "✓ Copied!" : "Copy results to clipboard"}
      </button>
      <p style={{ textAlign: "center", fontSize: 12, color: "#9CA3AF", marginTop: 8 }}>
        Paste into the chat — Claude will write your answers to the artifact file.
      </p>
    </div>
  );
}

// ─── Main App ─────────────────────────────────────────────────────────────────

export default function InterviewApp() {
  const { questions, artifactName, engagementName } = INTERVIEW_DATA;
  const [answers, setAnswers] = useState({});
  const [idx, setIdx] = useState(0);
  const [inputVal, setInputVal] = useState("");
  const [checkedVals, setCheckedVals] = useState({}); // { [qId]: string[] }
  const [screen, setScreen] = useState("questions"); // "questions" | "review"

  // Sync input field when navigating
  useEffect(() => {
    const q = questions[idx];
    setInputVal(answers[q?.id]?.value ?? "");
  }, [idx]);

  function recordAnswer(value, state) {
    const q = questions[idx];
    const updated = { ...answers, [q.id]: { value, state } };
    setAnswers(updated);
    if (idx < questions.length - 1) {
      setIdx(i => i + 1);
      setInputVal("");
    } else {
      setScreen("review");
    }
  }

  const currentQ = questions[idx];
  const currentChecked = checkedVals[currentQ?.id] || [];

  function handleCheckChange(newChecked) {
    setCheckedVals(prev => ({ ...prev, [currentQ.id]: newChecked }));
  }

  const answeredCount = Object.keys(answers).length;

  return (
    <div style={{
      fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
      maxWidth: 680, margin: "0 auto", padding: "24px 20px",
      background: "#F9FAFB", minHeight: "100vh", boxSizing: "border-box",
    }}>
      {/* Header */}
      <div style={{ marginBottom: 28 }}>
        <div style={{ fontSize: 11, fontWeight: 700, color: "#6366F1", textTransform: "uppercase", letterSpacing: "0.08em", marginBottom: 4 }}>
          EA Interview
        </div>
        <h1 style={{ fontSize: 22, fontWeight: 800, color: "#111827", margin: "0 0 2px" }}>{artifactName}</h1>
        <p style={{ fontSize: 13, color: "#9CA3AF", margin: 0 }}>{engagementName}</p>
      </div>

      {screen === "questions" ? (
        <QuestionCard
          q={currentQ}
          qNum={idx + 1}
          total={questions.length}
          inputVal={inputVal}
          setInputVal={setInputVal}
          checkedVals={currentChecked}
          onCheckChange={handleCheckChange}
          onAnswer={recordAnswer}
          onBack={() => { setIdx(i => i - 1); }}
          onJumpToReview={() => setScreen("review")}
        />
      ) : (
        <ReviewScreen
          questions={questions}
          answers={answers}
          onEdit={i => { setIdx(i); setScreen("questions"); }}
          onDone={() => {}}
        />
      )}
    </div>
  );
}
