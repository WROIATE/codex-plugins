# Conventional Commits 1.0.0 Reference

Source: https://www.conventionalcommits.org/en/v1.0.0/

## Core Shape

```text
<type>[optional scope][optional !]: <description>

[optional body]

[optional footer(s)]
```

The convention adds machine-readable meaning to commit messages so tools can generate changelogs, infer SemVer release levels, and communicate change intent.

## Required Rules

- A commit must start with a type, optionally followed by a scope in parentheses, optionally followed by `!`, then a colon, one space, and a description.
- `feat` is required for commits that add a feature.
- `fix` is required for commits that fix a bug.
- Other types are allowed by the spec. Common conventional types include `build`, `chore`, `ci`, `docs`, `perf`, `refactor`, `revert`, `style`, and `test`.
- A scope is a noun describing the affected codebase area, written in parentheses after the type.
- A body is optional, free-form, and starts after one blank line.
- Footers are optional and start after one blank line following the body or subject.
- Footer tokens use a word token plus either `: ` or ` #` before the value.
- Footer tokens use hyphens instead of spaces, except `BREAKING CHANGE`.
- `BREAKING CHANGE: <description>` and `BREAKING-CHANGE: <description>` are synonymous footer tokens.
- A breaking change must be indicated either by `!` before the subject colon or by a breaking-change footer.
- If `!` is used, the subject description can serve as the breaking-change description.
- Implementors should treat units as case-insensitive except `BREAKING CHANGE`, which must be uppercase.

## SemVer Mapping

- `fix` maps to PATCH.
- `feat` maps to MINOR.
- Any breaking-change marker maps to MAJOR.
- Other types have no SemVer effect unless they mark a breaking change.

## Examples

```text
fix(parser): handle empty token streams
```

```text
feat(api)!: remove legacy response wrapper
```

```text
docs: correct changelog spelling
```

```text
fix: prevent request race

Track the latest request id and ignore stale responses.

Refs: #123
```

```text
feat(config): allow extending shared presets

BREAKING CHANGE: preset resolution now rejects relative parent traversal
```
