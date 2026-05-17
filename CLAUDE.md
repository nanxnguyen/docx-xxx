# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A documentation-only workspace — engineering notes, frontend/backend knowledge maps, and trading-domain guides. There is no application code, no package manager, no test framework. Almost every file is Markdown. The only script is [convert-to-docx.sh](convert-to-docx.sh).

Content is bilingual (Vietnamese primary, English for technical terms). When editing, preserve existing language and terminology — do not translate one to the other unless asked.

## Directory layout (load-bearing)

- [Frontend/Topic/](Frontend/Topic/) — numbered learning topics, strict naming: `TopicNN-short-topic-name.md`. Hyphenated, lowercase, often with Vietnamese diacritics in the slug. When adding a topic, continue the numbering and pattern.
- [extend/](extend/) — extended question-style docs, naming: `QNN-topic-name.md`.
- [_Archive/](_Archive/) — older versions, grouped by theme (`01-JavaScript-Fundamentals/`, `04-React-Ecosystem/`, etc.). **Do not modify archived content** unless the task explicitly targets it.
- Root `*.md` — major standalone guides (uppercase descriptive names like [FRONTEND_INTERVIEW_QUESTIONS.md](FRONTEND_INTERVIEW_QUESTIONS.md), [TRADING_DOMAIN_KNOWLEDGE.md](TRADING_DOMAIN_KNOWLEDGE.md)).
- [Backend/](Backend/), [extend/](extend/), [promt/](promt/) — additional knowledge maps and prompt notes.
- [.codex/agents/](.codex/agents/) — Codex agent configs that define the doc-writing/reviewing style this repo expects. Read these before large rewrites (see "Doc style" below).

## Common commands

Lightweight checks only — there is no build or test step.

- Search before adding to avoid duplication: `rg "keyword" Frontend Backend extend`
- List all Markdown: `rg --files -g "*.md"`
- Validate shell script syntax: `bash -n convert-to-docx.sh`
- Export Markdown → DOCX/PDF: `./convert-to-docx.sh` (requires `pandoc`; PDF also needs `pdflatex`).
  - Note: the script's `INPUT_FILE` is hardcoded (currently `JavaScript_Core_Fundamentals.md`). To export a different doc, edit the script's variables — don't assume the script picks up arbitrary input. Only run when explicitly asked to produce DOCX/PDF.

## Doc style (the repo's voice)

The [.codex/agents/](.codex/agents/) configs are the source of truth for writing style. Key rules when rewriting or extending a Topic:

- **Audience**: senior/staff frontend engineer — production tradeoffs over textbook definitions.
- **Language**: Vietnamese prose; English in backticks for technical terms (`race condition`, `hydration`, `tree-shaking`, etc.).
- **Required section order for a rewritten topic**: Senior/Staff Summary → Key Mental Model → Main Concepts → Practical TS/JS Examples → Production Notes / React Implications → Common Pitfalls → Decision Guide/Checklist → Short Interview Answer.
- **Interview Answer** must sound conversational: "Em nghĩ...", "Theo em...", "Em thường..." — confident, concise, still senior-level.
- **Real-World Scenarios** (when added) live under `## 🌍 Real-World Scenarios` with structure: Context → User Flow → Technical Requirements → Edge Cases → Recommended Approach → Senior/Staff Tradeoffs → Testing Notes → Interview Answer → Vietnamese explanation.
- **Tables vs lists**: prefer compact tables for comparisons; switch to grouped bullets when cells get long or wrap poorly in terminal.
- **Highlight markers**: ✅ ⚠️ ❌ 💡 🔥 for scanning. Use them, don't over-decorate.
- Prefer TypeScript examples; "simple first, production second" when a concept is hard; use before/after for refactors.

## Editing rules

- **Scope discipline**: only edit the file the user requested. Do not touch unrelated topics, do not rewrite archived files, do not "improve" neighboring content opportunistically.
- **Preserve existing examples and bilingual explanations** unless they're wrong, duplicated, or clearly low-value. Fix incorrect technical statements when you spot them.
- **Add missing senior keys** for a topic (security, performance, SSR, a11y, testing, React implications) — but as a concise note/row/checklist item if the doc is already long, not a new long section.
- **No new files unless asked**. Prefer extending an existing topic.
- **Commit messages**: history is informal/short; nudge toward concise imperatives ("Update frontend caching notes", "Fix docx export script") rather than matching the existing one-letter style.

## Before finishing an edit

- Check heading hierarchy is consistent (no jumps from `##` to `####`).
- Check code fences are balanced.
- Run `git diff --check` on the edited file when practical.
- Report what changed and the key improvements — don't restate the diff.
