# Metorial + PydanticAI

Build type-safe AI agents with MCP tools.

## Installation

```bash
pip install metorial pydantic-ai python-dotenv
```

## Quick Start

```python
from metorial import Metorial
from metorial.integrations.pydantic_ai import register_metorial_tools
from pydantic_ai import Agent

metorial = Metorial(api_key="your-metorial-api-key")

async with metorial.provider_session(
    provider="openai",
    server_deployments=["your-deployment-id"],
) as session:
    agent = Agent("openai:gpt-4o")
    register_metorial_tools(agent, session)

    result = await agent.run("Your query here")
```

## Examples

- [example.py](example.py) - Python script with PydanticAI agent
- [example.ipynb](example.ipynb) - Interactive Jupyter notebook tutorial

## Integration Details

The `register_metorial_tools()` function registers MCP tools directly onto a PydanticAI agent, providing:

- Type-safe tool definitions
- Automatic schema validation
- Seamless integration with PydanticAI's structured output

## Links

- [PydanticAI Documentation](https://ai.pydantic.dev/)
- [Metorial Dashboard](https://app.metorial.com)
