# metorial-mcp-session

MCP (Model Context Protocol) session management for Metorial. Provides session handling and tool management functionality.

## Installation

```bash
pip install metorial-mcp-session
# or
uv add metorial-mcp-session
# or
poetry add metorial-mcp-session
```

## Features

- 🔧 **Session Management**: Handle MCP sessions and lifecycle
- 🛠️ **Tool Management**: Manage and execute tools through MCP
- 📡 **Protocol Handling**: MCP protocol implementation
- ⚡ **Async Support**: Full async/await support

## Usage

This package is typically used internally by other Metorial packages and not directly by end users.

### Internal Usage

```python
from metorial_mcp_session import MetorialMcpSession

# Used internally by Metorial packages
session = MetorialMcpSession()
```

## License

MIT License - see [LICENSE](../../LICENSE) file for details.
