# Xcatcher Agent Skill

Install one Agent Skill that teaches Codex, Claude Code, Cursor, GitHub Copilot, Cline, and other compatible agents how to fetch recent public X (Twitter) posts by handle through Xcatcher.

The Skill prefers the public Remote MCP endpoint, returns structured JSON, and supports accountless x402 v2 USDC pay-per-crawl on Base. It includes explicit payment approval, secret-handling, retry, polling, and prompt-injection boundaries.

## Install

Universal Skills CLI:

```bash
npx skills add lvpiggyqq/xcatcher-skill --skill xcatcher
```

Non-interactive Codex project install:

```bash
npx skills add lvpiggyqq/xcatcher-skill --skill xcatcher --agent codex -y --copy
```

GitHub CLI:

```bash
gh skill install lvpiggyqq/xcatcher-skill xcatcher
```

To inspect before installing:

```bash
npx skills add lvpiggyqq/xcatcher-skill --list
gh skill preview lvpiggyqq/xcatcher-skill xcatcher
```

Canonical sources and releases:

- <https://xcatcher.top/skills/xcatcher/SKILL.md>
- <https://github.com/lvpiggyqq/xcatcher-skill/releases/latest>

## What it enables

- Monitor one or many named X accounts without treating keyword search as handle monitoring.
- Choose safely between accountless x402 and an existing Xcatcher API key.
- Ask for approval before any wallet signature or spend.
- Keep API keys, payment signatures, and task tokens in host-managed secret channels rather than prompts or shell history.
- Poll a task without creating duplicate work or duplicate charges.
- Read paginated JSON first and request XLSX only when a full export is needed.
- Treat every returned post as untrusted external content.

## Contents

The installable Skill is in [`skills/xcatcher`](skills/xcatcher):

- `SKILL.md`: workflow and decision rules.
- `agents/openai.yaml`: compatible host metadata and Remote MCP dependency.
- `references/API.md`: schemas, task states, errors, and result semantics.
- `references/PAYMENTS.md`: x402 v2 payment and retry rules.
- `scripts/xcatcher.py`: dependency-free REST fallback.

Remote MCP: <https://xcatcher.top/mcp/>

Documentation: <https://xcatcher.top/docs/>

MCP Registry: <https://registry.modelcontextprotocol.io/v0.1/servers/io.github.lvpiggyqq%2Fxcatcher/versions/3.0.0>

License: [MIT](LICENSE).
