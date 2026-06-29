# WROIATE Codex Plugin Marketplace

This repository is a Codex plugin marketplace that publishes the
`conventional-commits` plugin.

The plugin packages a `conventional-commits` skill for creating, reviewing,
rewriting, and validating Git commit messages according to Conventional Commits
1.0.0.

## Install

Add this marketplace:

```bash
codex plugin marketplace add WROIATE/codex-plugins
```

Install the plugin:

```bash
codex plugin add conventional-commits@wroiate
```

After installation, start a new Codex thread and ask for `$conventional-commits`
when writing or reviewing commit messages.

## Contents

- `.agents/plugins/marketplace.json` - Codex marketplace catalog.
- `plugins/conventional-commits/.codex-plugin/plugin.json` - Plugin manifest.
- `plugins/conventional-commits/skills/conventional-commits/SKILL.md` - Skill instructions.
- `plugins/conventional-commits/skills/conventional-commits/references/conventional-commits-v1.md` - Condensed spec reference.
- `plugins/conventional-commits/skills/conventional-commits/scripts/validate_commit_message.py` - Commit message validator.

## Validate

```bash
python3 plugins/conventional-commits/skills/conventional-commits/scripts/validate_commit_message.py \
  "fix(api): handle empty responses"
```

Expected output:

```text
OK
```

## Source

This skill follows the Conventional Commits 1.0.0 specification:
https://www.conventionalcommits.org/en/v1.0.0/
