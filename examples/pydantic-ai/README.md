# Metorial + PydanticAI

Uses [PydanticAI](https://ai.pydantic.dev/) with Anthropic Claude to run an AI agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` — from [console.anthropic.com](https://console.anthropic.com)

## Run

```bash
pip install metorial pydantic-ai python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial, metorial_pydantic_ai

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Connect and resolve PydanticAI tools directly
session = await metorial.connect(
    adapter=metorial_pydantic_ai(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

# Pass the tools directly to the agent
agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    system_prompt="You are a helpful research assistant.",
    tools=session.tools(),
)

# PydanticAI handles the tool call loop automatically — when Claude
# wants to use a tool, PydanticAI calls it via Metorial and feeds
# the result back
result = await agent.run(
    "Search the web for the latest news about AI agents and summarize the top 3 stories."
)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
