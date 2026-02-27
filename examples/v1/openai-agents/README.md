# Metorial + OpenAI Agents SDK

Build OpenAI agents with MCP tools.

## Installation

```bash
pip install metorial openai-agents python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.openai_agents import create_openai_agent_tools
from agents import Agent, Runner

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    tools = create_openai_agent_tools(session)

    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
        tools=tools,
    )

    result = await Runner.run(agent, "Your query here")
```

## Examples

- [example.py](example.py) - Python script with research assistant agent
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `create_openai_agent_tools()` function converts MCP tools into OpenAI Agents SDK `FunctionTool` objects compatible with the official OpenAI Agents framework.

## Links

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- [Metorial Dashboard](https://app.metorial.com)
