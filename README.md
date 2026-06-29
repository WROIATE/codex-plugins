# Conventional Commits Codex Plugin

A local Codex plugin that packages the `conventional-commits` skill for creating,
reviewing, rewriting, and validating Git commit messages according to
Conventional Commits 1.0.0.

## Contents

- `.codex-plugin/plugin.json` - Codex plugin manifest.
- `skills/conventional-commits/SKILL.md` - Skill instructions.
- `skills/conventional-commits/references/conventional-commits-v1.md` - Condensed spec reference.
- `skills/conventional-commits/scripts/validate_commit_message.py` - Commit message validator.

## Install From A Local Marketplace

Add the plugin folder to a Codex marketplace entry, then install it:

```bash
codex plugin add conventional-commits@personal
```

After installation, start a new Codex thread and ask for `$conventional-commits`
when writing or reviewing commit messages.

## Validate

```bash
python3 skills/conventional-commits/scripts/validate_commit_message.py \
  "fix(api): handle empty responses"
```

Expected output:

```text
OK
```

## Source

This skill follows the Conventional Commits 1.0.0 specification:
https://www.conventionalcommits.org/en/v1.0.0/
