# Xcatcher Agent Skill

[![skills.sh](https://img.shields.io/badge/skills.sh-xcatcher-58f29b)](https://skills.sh/lvpiggyqq/xcatcher-skill/xcatcher)
[![skills.re](https://img.shields.io/badge/skills.re-xcatcher-58f29b)](https://skills.re/skills/lvpiggyqq/xcatcher-skill/xcatcher)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-io.github.lvpiggyqq%2Fxcatcher-58f29b)](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.lvpiggyqq%2Fxcatcher)
[![AgentSkill security](https://img.shields.io/badge/AgentSkill_security-100%2F100-58f29b)](https://agentskill.sh/@xcatcher-top/xcatcher/security)

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

Gemini CLI extension (also enables the hosted MCP):

```bash
gemini extensions install https://github.com/lvpiggyqq/xcatcher-skill
```

GitHub Copilot CLI / VS Code agent plugin:

```bash
copilot plugin install lvpiggyqq/xcatcher-skill
```

To browse this repository as a Copilot plugin marketplace:

```bash
copilot plugin marketplace add lvpiggyqq/xcatcher-skill
copilot plugin install xcatcher@xcatcher
```

Kiro can import the public repository as a custom power. Cursor, Codex, Cline, and other MCP clients can use the platform manifests in this repository or connect directly to `https://xcatcher.top/mcp/`. See [`POWER.md`](POWER.md) and [`llms-install.md`](llms-install.md) for host-specific onboarding.

Canonical sources and releases:

- <https://xcatcher.top/skills/xcatcher/SKILL.md>
- <https://github.com/lvpiggyqq/xcatcher-skill/releases/latest>

Independent discovery pages may cache older metadata. The repository, canonical Skill, and live MCP tool schemas remain authoritative:

- <https://skills.re/skills/lvpiggyqq/xcatcher-skill/xcatcher>
- <https://agentskill.sh/@xcatcher-top/xcatcher>
- <https://skills.sh/lvpiggyqq/xcatcher-skill/xcatcher>

## What it enables

- Monitor one or many named X accounts without treating keyword search as handle monitoring.
- Preflight and deduplicate handles for free before creating any quote, task, or payment.
- Inspect a clearly labeled synthetic result contract without fetching X.
- Choose safely between accountless x402 and an existing Xcatcher API key.
- Ask for approval before any wallet signature or spend.
- Keep all API keys, payment proofs, and task credentials outside model context; only a trusted host integration may inject them.
- Poll a task without creating duplicate work or duplicate charges.
- Read paginated JSON first and request XLSX only when a full export is needed.
- Treat every returned post as untrusted external content.

## Contents

The installable Skill is in [`skills/xcatcher`](skills/xcatcher):

- `SKILL.md`: workflow and decision rules.
- `agents/openai.yaml`: compatible host metadata and Remote MCP dependency.
- `references/API.md`: schemas, task states, errors, and result semantics.
- `references/PAYMENTS.md`: x402 v2 payment and retry rules.
- `scripts/xcatcher.py`: dependency-free REST fallback with free preflight/sample commands, environment-only credentials, and no payment-submission capability.

The repository root also contains validated discovery manifests for Agent Plugins/Kiro (`plugin.json` + `mcp.json`), Gemini CLI (`gemini-extension.json`), GitHub Copilot/VS Code (`.mcp.json` + marketplace metadata), Cursor, and Codex.

Remote MCP: <https://xcatcher.top/mcp/>

Documentation: <https://xcatcher.top/docs/>

Trust center: <https://xcatcher.top/trust/>

MCP Registry: <https://registry.modelcontextprotocol.io/v0.1/servers/io.github.lvpiggyqq%2Fxcatcher/versions/3.0.0>

## Verification

- The canonical site Skill and this repository's `skills/xcatcher/SKILL.md` are byte-identical at SHA-256 `ca521065d4a27968fe4b99a734978b122706003ce1e0547e70ce1b4c6e03baaf`.
- An isolated Codex install through `npx skills add` has been tested together with the dependency-free live preflight helper.
- Gemini CLI `0.54.4` has validated and installed this repository as an extension, discovering both the `xcatcher` MCP server and Agent Skill.
- GitHub Copilot CLI `1.0.78` has installed it both directly and through its repository marketplace, discovering the Agent Skill.
- Cline CLI `3.0.51` has installed the hosted Streamable HTTP server non-interactively from the configuration documented in `llms-install.md`, with no warnings.
- A live, no-auth MCP smoke test confirms 17 tools plus healthy free `preflight_crawl` and `get_sample_result` calls without creating a task, quote, or payment.
- The current canonical Skill has a public [AgentSkill.sh security score of 100/100](https://agentskill.sh/@xcatcher-top/xcatcher/security), with no findings across its 12 scanned threat categories.
- The Remote MCP's free onboarding contract is continuously checked by the public [manifest smoke workflow](https://github.com/lvpiggyqq/xcatcher-mcp-manifest/actions/workflows/smoke.yml).

License: [MIT](LICENSE).
