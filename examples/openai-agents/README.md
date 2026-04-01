# Metorial + OpenAI Agents SDK

Uses the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) to run an AI agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `OPENAI_API_KEY` — from [platform.openai.com](https://platform.openai.com)

## Run

```bash
cp .env.example .env
pip install -r requirements.txt
python example.py
```

## How it works

This README snippet uses bare `await` for readability. For a runnable script, see [`example.py`](./example.py).

```python
import os

from agents import Agent, Runner

# Initialize the Metorial client
from metorial import Metorial, metorial_openai_agents

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Connect and resolve OpenAI Agents tools directly
session = await metorial.connect(
    adapter=metorial_openai_agents(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

# The agent and runner handle the tool call loop automatically
agent = Agent(
    name="Research Assistant",
    instructions="You are a helpful research assistant. Use the available tools to find information.",
    tools=session.tools(),
)

# Runner.run orchestrates the full conversation — when the agent
# wants to use a tool, the runner calls it via Metorial and feeds
# the result back until the agent produces a final answer
result = await Runner.run(
    agent, "Search the web for the latest news about AI agents and summarize the top 3 stories."
)
print(result.final_output)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
