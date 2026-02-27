# Metorial + LangGraph

Build graph-based agent workflows with MCP tools.

## Installation

```bash
pip install metorial langgraph langchain-openai python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.langgraph import create_langgraph_tools, create_langgraph_tool_node

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_langgraph_tools(session)
    tool_node = create_langgraph_tool_node(session)  # For custom graphs
```

## Examples

- [example.py](example.py) - Python script with LangGraph workflow
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The LangGraph integration provides:

- `create_langgraph_tools()` - Convert MCP tools to LangGraph format
- `create_langgraph_tool_node()` - Create a pre-built tool execution node for your graph

## Links

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Metorial Dashboard](https://app.metorial.com)
