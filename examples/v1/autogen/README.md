# Metorial + Microsoft Autogen

Build multi-agent conversations with MCP tools.

## Installation

```bash
pip install metorial pyautogen python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.autogen import create_autogen_tools, get_autogen_tool_executor

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_autogen_tools(session)
    executor = get_autogen_tool_executor(session)

    # Register tools with your Autogen agents
```

## Examples

- [example.py](example.py) - Python script with multi-agent conversation
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The Autogen integration provides:

- `create_autogen_tools()` - Convert MCP tools to Autogen function format
- `get_autogen_tool_executor()` - Get an executor function for tool calls

## Links

- [Autogen Documentation](https://microsoft.github.io/autogen/)
- [Metorial Dashboard](https://app.metorial.com)
