# Metorial + Hugging Face smolagents

Build code-first agents with MCP tools.

## Installation

```bash
pip install metorial smolagents python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.smolagents import create_smolagents_tools
from smolagents import CodeAgent, HfApiModel

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_smolagents_tools(session)

    agent = CodeAgent(tools=tools, model=HfApiModel())
    result = agent.run("Your query here")
```

## Examples

- [example.py](example.py) - Python script with code agent
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `create_smolagents_tools()` function converts MCP tools into smolagents `Tool` objects that work with:

- `CodeAgent` - Generates and executes Python code
- `ToolCallingAgent` - Uses tool calling directly

## Links

- [smolagents Documentation](https://huggingface.co/docs/smolagents)
- [Metorial Dashboard](https://app.metorial.com)
