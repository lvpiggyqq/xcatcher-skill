# Install Xcatcher in Cline

Xcatcher is a hosted Streamable HTTP MCP server. Do not clone or execute server code, and do not ask the user for an API key just to verify the connection.

Add this entry to Cline's `cline_mcp_settings.json`, or enter the same URL in Cline's **MCP Servers → Remote Servers** interface:

```json
{
  "mcpServers": {
    "xcatcher": {
      "type": "streamableHttp",
      "url": "https://xcatcher.top/mcp/",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

After reconnecting, verify that `tools/list` succeeds and that the Xcatcher tools are visible. Then call, in order:

1. `get_service_info`
2. `preflight_crawl` with a harmless public handle such as `x`
3. `get_sample_result`

These checks are free and must not create a live crawl, quote, task, wallet signature, or payment. For a live crawl, read `skills/xcatcher/SKILL.md` and obtain explicit approval before any spend. Never request secrets or payment proofs in chat.
