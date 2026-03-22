# Spec: Artifact Preview MCP Server

**ID**: 004-artifact-preview-mcp
**Status**: Future / Not Started
**Date**: 2026-03-21

---

## Problem

The `ea-interview-ui` skill delivers interactive React apps in two modes:
- **React artifact** — works natively in Claude Code and Claude Cowork
- **HTML file written to disk** — the fallback for OpenCode and other harnesses

The HTML-to-disk path works but is manual: Claude writes the file, tells the user the path, and the user opens it themselves. There is no live preview, no reload on update, and no way for the model to open the browser programmatically from within a non-Claude-Code harness.

An MCP server with a dedicated preview tool closes this gap. Any MCP-compatible harness (OpenCode, Codex CLI, custom agents) can call the tool to get an immediate browser preview of any HTML/JSX artifact — identical UX to Claude Code's native artifact pane.

---

## Proposed Solution

A lightweight local MCP server (`artifact-preview-mcp`) that exposes one primary tool: `preview_artifact`. The tool accepts an HTML string, writes it to a temp file, and either opens it directly in the default browser or serves it on `localhost:PORT` and opens that URL.

The server runs as a sidecar alongside whatever agentic harness the user is in. Once running, any model in any MCP-compatible tool can render artifacts natively.

---

## MCP Tool Design

### Tool: `preview_artifact`

```json
{
  "name": "preview_artifact",
  "description": "Render an HTML/JSX artifact in the user's default browser. Writes the content to a temp file and opens it, or serves it on localhost if a live-reload port is configured.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "html": {
        "type": "string",
        "description": "Complete self-contained HTML to render. Must be a full document (<!DOCTYPE html>...) or a JSX component string (shell wrapping applied automatically)."
      },
      "title": {
        "type": "string",
        "description": "Optional label shown in the browser tab and used as the temp filename."
      },
      "mode": {
        "type": "string",
        "enum": ["file", "serve"],
        "default": "file",
        "description": "file: write to temp dir and open. serve: write and serve on localhost for live-reload support."
      }
    },
    "required": ["html"]
  }
}
```

**Returns:** `{ url: "file:///tmp/ea-preview/interview-2026-03-21.html" }` or `{ url: "http://localhost:4321/preview" }`

### Optional tool: `close_preview`

Closes the currently served preview (kills the localhost server). Only relevant in `serve` mode.

---

## Architecture

```
Agent (OpenCode / Codex / custom)
    │
    │  MCP call: preview_artifact(html, title, mode)
    ▼
artifact-preview-mcp (Node.js sidecar)
    │
    ├── mode=file  →  write to /tmp/ea-preview/{title}.html
    │                 open with platform launcher (see below)
    │                 return { url: "file://..." }
    │
    └── mode=serve →  write to /tmp/ea-preview/{title}.html
                      if server not running: start http.createServer on PORT
                      return { url: "http://localhost:PORT/preview" }
```

### WSL2 detection and safe browser launch

Use `execFile` (not `exec`) to prevent shell injection — the file path is passed as a separate argument, never interpolated into a shell string:

```ts
import { execFile } from "node:child_process";
import { readFileSync, existsSync } from "node:fs";

function isWSL(): boolean {
  return existsSync("/proc/version") &&
    readFileSync("/proc/version", "utf8").toLowerCase().includes("microsoft");
}

function toWindowsPath(posixPath: string): string {
  // /mnt/c/foo → C:\foo
  return posixPath.replace(/^\/mnt\/([a-z])/, (_, d) => `${d.toUpperCase()}:`)
                  .replace(/\//g, "\\");
}

function openInBrowser(filePath: string): void {
  if (isWSL()) {
    // Pass windows path as a separate arg — no shell interpolation
    execFile("cmd.exe", ["/c", "start", "", toWindowsPath(filePath)]);
  } else if (process.platform === "darwin") {
    execFile("open", [filePath]);
  } else {
    execFile("xdg-open", [filePath]);
  }
}
```

### JSX auto-wrapping

If the model passes a JSX component string (detected by absence of `<!DOCTYPE`) rather than a full HTML document, the server wraps it automatically using the same shell pattern as `interview-app-shell.html`:

```ts
function wrapJsx(jsx: string, title = "Preview"): string {
  return `<!DOCTYPE html>
<html><head>
  <meta charset="UTF-8"/>
  <title>${title}</title>
  <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head><body>
  <div id="root"></div>
  <script type="text/babel" data-presets="react">
    const { useState, useEffect, useRef } = React;
    ${jsx}
  </script>
</body></html>`;
}
```

Note: the JSX component name must be the default export or the last function defined. The template does not auto-detect the component name — callers should ensure the component is self-mounting (calls `ReactDOM.createRoot` itself) or the SKILL.md instructions must append the mount call before passing to this tool.

---

## Implementation Notes

### Technology choice

| Option | Pros | Cons |
|---|---|---|
| **Node.js + TypeScript** | Same stack as existing `docx` export scripts; `@modelcontextprotocol/sdk` is the reference TS implementation | Requires Node |
| **Python** | `mcp` PyPI package; simpler for users who already have Python (RAG-assistant dependency) | Slightly more boilerplate |

Recommend **Node.js + TypeScript** — consistent with the existing tooling in this repo.

### Repo location

```
plugins/artifact-preview-mcp/
├── .claude-plugin/plugin.json
├── README.md
├── LICENSE
├── package.json
├── tsconfig.json
├── src/
│   └── index.ts          # MCP server entry point
└── install.sh            # registers server in .mcp.json / opencode config
```

### Registration

**Claude Code** (project `.mcp.json`):
```json
{
  "mcpServers": {
    "artifact-preview": {
      "command": "node",
      "args": ["./plugins/artifact-preview-mcp/dist/index.js"]
    }
  }
}
```

**OpenCode** (`~/.config/opencode/config.json`):
```json
{
  "mcp": {
    "artifact-preview": {
      "command": "node",
      "args": ["/path/to/plugins/artifact-preview-mcp/dist/index.js"]
    }
  }
}
```

### `install.sh` responsibilities

1. Run `npm install && npm run build` in the plugin directory
2. Detect whether the user is in a Claude Code project (`.mcp.json`) or OpenCode (`~/.config/opencode/config.json`) and write the registration block
3. Print the URL format so the user knows what to expect: `file:///tmp/ea-preview/` or `http://localhost:4321`

---

## Integration with `ea-interview-ui`

Once this server is running, SKILL.md gets a third delivery mode:

| Runtime | Delivery mode |
|---|---|
| Claude Code or Claude Cowork | React artifact (inline) |
| Any harness + `preview_artifact` MCP tool available | `preview_artifact` tool call |
| OpenCode / other, no MCP server | HTML file written to disk, user opens manually |

The SKILL.md runtime detection rule becomes:
1. If artifact viewer available → present as React artifact
2. Else if `preview_artifact` MCP tool is available → call `preview_artifact(html, title)`
3. Else → write HTML to `EA-projects/{slug}/ui/` and instruct user to open it

---

## Out of scope for v1

- Live reload / hot module replacement (`serve` mode provides localhost but no WebSocket HMR)
- PDF / screenshot export from the preview
- Auth or multi-user isolation (local dev tool only)
- Bundling React locally for offline use (CDN required for JSX auto-wrap; full HTML documents pass through as-is)
