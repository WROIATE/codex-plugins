---
name: conventional-commits
description: Create, review, validate, or rewrite Git commit messages according to Conventional Commits 1.0.0. Use when Codex is asked to write a commit message, make a git commit, review commit history, fix a non-conforming commit subject, choose a commit type/scope, or enforce structured messages for changelog and SemVer automation.
---

# Conventional Commits

## Workflow

1. Inspect the actual change before proposing a message. Prefer `git diff --staged`; if nothing is staged and the user is asking for a commit message, inspect `git diff` and state whether the message is for unstaged changes.
2. Choose one primary intent. If the change mixes unrelated intents, recommend splitting the commit before writing a broad message.
3. Format the first line as `type(scope)!: description` or `type: description`.
4. Add a body only when the subject cannot explain the change clearly. Separate it from the subject with one blank line.
5. Add footers only for metadata such as `Refs: #123`, `Reviewed-by: Name`, or breaking changes. Separate footers from the body or subject with one blank line.
6. Validate the final message with `scripts/validate_commit_message.py` when writing or reviewing an exact commit message.

## Required Format

Use this structure:

```text
type(optional-scope)!: short imperative description

optional body

optional-footer: value
```

Rules to enforce:

- Require a type, optional parenthesized noun scope, optional `!`, then `: ` and a non-empty description.
- Use `feat` for new user-visible or API/library capability.
- Use `fix` for bug fixes.
- Allow other clear types when the repository does not define a stricter set: `build`, `chore`, `ci`, `docs`, `perf`, `refactor`, `revert`, `style`, `test`.
- Treat `!` before the colon as a breaking-change marker.
- Mark breaking changes either with `!` in the subject or a footer token `BREAKING CHANGE:` / `BREAKING-CHANGE:`.
- Keep `BREAKING CHANGE` uppercase when used as a footer token.
- Use footer tokens with hyphens instead of spaces, except for `BREAKING CHANGE`.
- Prefer lowercase types for consistency, even though the spec is case-insensitive except for `BREAKING CHANGE`.

## Type Selection

- `feat`: adds a feature or capability.
- `fix`: fixes incorrect behavior.
- `perf`: improves performance without changing intended behavior.
- `refactor`: changes internal structure without changing behavior or performance intent.
- `docs`: changes documentation or comments only.
- `test`: adds or updates tests without production behavior changes.
- `build`: changes build system, packaging, or dependencies.
- `ci`: changes CI configuration or automation.
- `style`: formatting-only changes that do not affect code behavior.
- `chore`: maintenance that does not fit a more specific type.
- `revert`: reverts previous commits; include a footer such as `Refs: <sha>`.

When more than one type seems plausible, choose the user-facing or release-impacting intent first: `fix`/`feat` before maintenance types, `perf` before `refactor`, and split the commit if separate changes deserve separate release notes.

## Message Style

- Write the subject in concise imperative English by default, matching the user's explicit language request if they ask otherwise.
- Do not end the subject with a period.
- Keep the subject specific enough to identify the changed behavior.
- Use a scope only when it adds useful context, such as a package, module, command, UI area, or service.
- For Git commit commands, quote multi-line messages safely with repeated `-m` flags or an editor/file path appropriate to the user's request.

## Validation Script

Run the bundled validator like this:

```bash
python3 /home/jarao/.codex/skills/conventional-commits/scripts/validate_commit_message.py "fix(api): handle empty responses"
```

For a file:

```bash
python3 /home/jarao/.codex/skills/conventional-commits/scripts/validate_commit_message.py --file COMMIT_EDITMSG
```

The script validates structure and common Conventional Commits 1.0.0 constraints. It does not replace repository-specific commitlint rules; if a repo has its own config, follow the stricter local rule.

## Reference

Read `references/conventional-commits-v1.md` when a task needs the condensed spec details, examples, or source URL.
