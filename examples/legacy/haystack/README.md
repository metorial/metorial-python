# Metorial + deepset Haystack

Build NLP pipelines with MCP tools.

## Installation

```bash
pip install metorial haystack-ai python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.haystack import create_haystack_tools, create_haystack_tool_invoker

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_haystack_tools(session)
    tool_invoker = create_haystack_tool_invoker(session)

    # Use with Haystack pipelines
```

## Examples

- [example.py](example.py) - Python script with Haystack pipeline
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The Haystack integration provides:

- `create_haystack_tools()` - Convert MCP tools to Haystack `Tool` objects
- `create_haystack_tool_invoker()` - Create a `ToolInvoker` component for pipelines

## Links

- [Haystack Documentation](https://docs.haystack.deepset.ai/)
- [Metorial Dashboard](https://app.metorial.com)
