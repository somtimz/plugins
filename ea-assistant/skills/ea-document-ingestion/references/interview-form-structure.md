# Interview Form Structure — Specification

This document defines the structure of the EA Assistant interview form as exported to and imported from Word (`.docx`) format. It covers the full specification of the format, examples of correctly and incorrectly formatted documents, and the rules governing how each answer state is parsed.

---

## Purpose and Context

The EA Assistant uses structured stakeholder interviews as a primary method for gathering architecture inputs. Interview questions are defined in interview templates (stored internally as YAML or Markdown). The interview form workflow is:

1. **Export:** The assistant exports an interview form to a `.docx` file. The document presents each question with a response area below it.
2. **Fill:** A stakeholder (or the architect facilitated by a stakeholder) fills in the form in Word. They may also mark questions as skipped or not applicable.
3. **Import:** The completed `.docx` is uploaded back to the assistant. The parser reads each answer, records the answer state, and stores the responses in the interview record.

---

## Document Structure Specification

### Overall Document Layout

The document is structured as follows:

```
[Cover Section]
  Title: Interview Form — <Engagement Name>
  Date: <ISO Date>
  Respondent: <Name / Role>
  Section: <Section Name>

[One or more Question Blocks]
```

The cover section uses a standard table or structured paragraph block. The Question Block structure is described below.

---

### Question Block Structure

Each question is represented by a **Question Block** consisting of three consecutive paragraphs or elements:

```
QUESTION BLOCK:

1. Question Header Paragraph
   Style: "Heading 3" or "Q-Header" custom style
   Text: "Q<number>. <Question text>"
   Example: "Q1. What are the primary business drivers for this programme?"

2. Guidance Paragraph (optional)
   Style: "Q-Guidance" custom style or italic Normal paragraph
   Text: Guidance text for the respondent
   Example: "(Consider regulatory, competitive, and operational drivers.)"

3. Answer Paragraph / Answer Table
   Style: "Q-Answer" custom style or Normal paragraph
   Text: The respondent's answer text, OR one of the answer state markers
```

The parser identifies a Question Block by finding a paragraph that matches the Question Header pattern: starts with `Q` followed by one or more digits, then a period, then a space.

---

### Answer State Markers

The following markers are the only valid answer state indicators. They must appear as the **complete and sole content** of the Answer Paragraph. They are case-insensitive but must otherwise be an exact match.

| Marker | Answer State | Meaning |
|---|---|---|
| *(substantive text)* | `answered` | The respondent has provided an answer |
| `SKIP` | `skipped` | The respondent intentionally skipped this question — they will answer later or it was not discussed |
| `N/A` | `not_applicable` | The question does not apply to this engagement or respondent |
| *(empty)* | `unanswered` | No content was entered — the answer paragraph exists but is blank |

---

### Answer State: `answered`

Any non-empty text in the Answer Paragraph that is not an exact match for `SKIP` or `N/A` is treated as an answer.

- Multi-paragraph answers are supported: if multiple consecutive paragraphs follow the Question Header before the next Question Header, all are collected as the answer body.
- The answer text is stored as plain text; formatting (bold, italic, bullet lists within the answer) is preserved as plain text with minimal markdown conversion (bullets become `- ` items).
- Answer tables: if the respondent completes an embedded table in the answer area, the table is extracted as a CSV-like structure (tab-separated rows) and stored as a structured answer.

**Correctly formatted answered example:**
```
Q3. What systems currently support the invoicing process?

The current invoicing process is supported by three systems:
- SAP ECC (primary billing engine)
- Salesforce (contract and quote data)
- SharePoint (manual invoice approvals via a workflow)

There is no direct integration between SAP and Salesforce; data is manually re-entered.
```

---

### Answer State: `skipped`

The word `SKIP` (case-insensitive) as the sole content of the Answer Paragraph marks the question as skipped.

Variations accepted:
- `SKIP`
- `skip`
- `Skip`
- `SKIP.` (trailing period is stripped)
- `[SKIP]` (square brackets are stripped)

**Correctly formatted skip example:**
```
Q7. What is the current DR/BCP testing frequency?

SKIP
```

**Incorrectly formatted — will be parsed as `answered` not `skipped`:**
```
Q7. What is the current DR/BCP testing frequency?

SKIP - will discuss in follow-up session
```
This is parsed as `answered` because the text extends beyond the marker word. The architect should use the `answered` state with "Will discuss in follow-up session" as the answer text instead.

---

### Answer State: `not_applicable`

The text `N/A` (case-insensitive) as the sole content of the Answer Paragraph marks the question as not applicable.

Variations accepted:
- `N/A`
- `n/a`
- `NA`
- `Not applicable`
- `Not Applicable`
- `[N/A]`

**Correctly formatted N/A example:**
```
Q12. Describe the organisation's current use of the Zachman Framework.

N/A
```

**Incorrectly formatted — will be parsed as `answered`:**
```
Q12. Describe the organisation's current use of the Zachman Framework.

N/A - we don't use it
```
To record non-applicability with a comment, the preferred approach is to use the `answered` state with text such as "Not applicable to this engagement. The organisation does not use Zachman."

---

### Answer State: `unanswered`

A completely empty Answer Paragraph (or a paragraph containing only whitespace or a non-breaking space) is parsed as `unanswered`.

Distinguishing `unanswered` from `skipped` is important:
- `unanswered` means the respondent may not have seen or considered the question.
- `skipped` means the respondent consciously deferred the question.

Both trigger a follow-up flag in the interview record, but `skipped` is treated with higher confidence that the respondent is aware of the outstanding item.

---

## Cover Section Parsing

The cover section is parsed to extract interview metadata. Expected field names (case-insensitive, colon-delimited):

| Field Label | Extracted As | Notes |
|---|---|---|
| `Engagement:` or `Project:` | `engagement_name` | Name of the architecture engagement |
| `Date:` | `interview_date` | Parsed as ISO date if possible; stored as string otherwise |
| `Respondent:` | `respondent_name` | Full name of the interviewee |
| `Role:` | `respondent_role` | Job title or role of the interviewee |
| `Interviewer:` | `interviewer_name` | Name of the architect conducting the interview |
| `Section:` | `section_name` | Which interview section this form covers |

If the cover section fields are not present or do not match expected labels, the metadata fields are set to `null` and a parsing warning is generated.

---

## Multi-Section Documents

A single `.docx` may contain multiple interview sections. Each section begins with a `Heading 1` or `Heading 2` paragraph whose text does not match the Question Header pattern (i.e., it is a section heading, not a question).

The parser assigns each question to the section heading that immediately precedes it. Section headings are extracted as `section_name` on each question record.

**Example structure:**
```
# Business Context                          ← Section heading (Heading 1)

Q1. What are the primary strategic goals?
[answer]

Q2. What are the key business risks?
[answer]

# Current Technology Landscape              ← Section heading (Heading 1)

Q3. What ERP system is in use?
[answer]
```

---

## Incorrect Formatting Examples and Diagnoses

### Problem: Questions not detected

**Symptom:** Parser returns zero questions.

**Cause:** The Question Header paragraphs do not use a Heading style. If normal paragraphs starting with "Q1." are used without the Heading 3 style, the parser may not detect them.

**Fix:** Apply the "Heading 3" style to all Question Header paragraphs. Alternatively, the parser has a fallback heuristic: if no Heading 3 paragraphs are found, it scans all paragraphs for the `Q\d+\.` pattern regardless of style. Enable this fallback mode explicitly if needed.

---

### Problem: Multi-paragraph answer captured incompletely

**Symptom:** Only the first paragraph of a multi-paragraph answer is captured.

**Cause:** The document uses a section break or page break between paragraphs of the same answer, which the parser treats as a block boundary.

**Fix:** Ensure that paragraphs within a single answer use standard paragraph breaks (Enter), not manual section breaks or page breaks.

---

### Problem: Answer state marker not recognised

**Symptom:** `SKIP - will follow up` is recorded as an answered question with text "SKIP - will follow up".

**Cause:** The marker must be the sole content of the Answer Paragraph. Any additional text causes the state to be `answered`.

**Fix:** Place the marker alone on its own paragraph. Use a separate guidance annotation in a comment or bracketed note that will be stripped on import, or simply accept the `answered` state and include the context in the answer text.

---

### Problem: Table answers not parsed correctly

**Symptom:** A table within the answer area returns garbled text.

**Cause:** The table contains merged cells or nested tables.

**Fix:** Avoid merged cells in answer tables. Nested tables are not supported — flatten to a single-level table.

---

## Import Validation Checks

The parser performs the following validation on import and reports warnings for each issue found:

| Check | Warning Triggered |
|---|---|
| Cover section metadata fields missing | "Interview metadata incomplete: [field names] not found" |
| Question numbers not sequential | "Question numbering gap: Q4 follows Q2" |
| No answers found (all unanswered) | "Warning: All questions are unanswered — verify document was completed" |
| Duplicate question numbers | "Duplicate question ID: Q5 appears twice in section [section name]" |
| Answer paragraph missing (no element after Question Header before next Header) | "Question Q[n] has no answer element — parsed as unanswered" |
