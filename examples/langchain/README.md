# Metorial + LangChain

Build LangChain agents with access to any MCP server.

## Installation

```bash
pip install metorial langchain langchain-anthropic python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="anthropic",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_langchain_tools(session)
    # Use with any LangChain agent
```

## Examples

- [example.py](example.py) - Python script with tool-calling agent
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `create_langchain_tools()` function converts Metorial MCP tools into LangChain `BaseTool` objects that work with any LangChain agent:

- `AgentExecutor` with `create_tool_calling_agent`
- `create_openai_tools_agent`
- `create_react_agent`
- Any custom agent implementation

## Links

- [LangChain Documentation](https://python.langchain.com/)
- [Metorial Dashboard](https://app.metorial.com)
