# Repository Guidelines

## Project Structure & Module Organization

This repository is a documentation workspace for engineering notes, interview material, and domain guides. Most content is Markdown.

- Root `*.md` files contain major standalone guides, such as `FRONTEND_INTERVIEW_QUESTIONS.md`, `React_Fundamentals.md`, and trading notes.
- `Frontend/Topic/` contains numbered frontend learning topics. Keep the `TopicNN-...md` naming pattern when adding related material.
- `Backend/` contains backend knowledge maps and summaries.
- `extend/` contains additional question-style or extended topic documents.
- `_Archive/` stores older material. Do not move or rewrite archived content unless the task explicitly targets it.
- `promt/` contains prompt-related notes.
- `convert-to-docx.sh` is the only project script and is used for Pandoc-based exports.

## Build, Test, and Development Commands

There is no application build or package manager configured. Use lightweight documentation checks:

- `rg "keyword" Frontend Backend extend` searches existing notes before adding duplicate content.
- `rg --files -g "*.md"` lists Markdown documents.
- `bash -n convert-to-docx.sh` checks shell syntax when editing the export script.
- `./convert-to-docx.sh` exports Markdown to DOCX/PDF with Pandoc; verify `pandoc` and optional `pdflatex` are installed first.

## Coding Style & Naming Conventions

For Markdown, use clear heading hierarchy, concise sections, tables, and bullet lists where they improve scanning. Preserve existing Vietnamese and English terminology in nearby content. Avoid broad rewrites of unrelated sections.

For filenames, follow existing patterns:

- Frontend topics: `Topic01-short-topic-name.md`
- Extended questions: `Q50-topic-name.md`
- Standalone guides: uppercase descriptive names, for example `KEYCLOAK_SUMMARY.md`

For shell scripts, keep Bash syntax consistent with the existing script, quote paths and variables, and check optional tools before using them.

## Testing Guidelines

There is no test framework or coverage requirement. For documentation-only changes, review rendered Markdown structure, heading levels, tables, and changed links. For script changes, run `bash -n convert-to-docx.sh` and, when dependencies are available, run the script on the intended input.

## Commit & Pull Request Guidelines

Recent Git history uses very short informal commit messages, so prefer improving clarity going forward. Use concise imperative messages such as `Update frontend caching notes` or `Fix docx export script`.

Pull requests should include a short summary, changed files or topic areas, verification performed, and screenshots only when rendered output or exported documents changed.

## Agent-Specific Instructions

Read relevant files before editing. Keep changes scoped to the requested document or script. Do not remove existing examples, notes, or bilingual explanations unless requested. Convert Markdown to DOCX only when explicitly asked.
