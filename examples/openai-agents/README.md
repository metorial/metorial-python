# Metorial + OpenAI Agents SDK

Uses the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) to run an AI agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `OPENAI_API_KEY` — from [platform.openai.com](https://platform.openai.com)

## Run

```bash
pip install metorial openai-agents python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial
from metorial.integrations.openai_agents import create_openai_agent_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Open a provider session — note provider="openai" since the OpenAI
# Agents SDK uses OpenAI's tool format
async with metorial.provider_session(
    provider="openai",
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
) as session:
    # create_openai_agent_tools converts MCP tools into OpenAI Agents
    # SDK-compatible tool definitions
    tools = create_openai_agent_tools(session)

    # The agent and runner handle the tool call loop automatically
    agent = Agent(
        name="Research Assistant",
        instructions="You are a helpful research assistant. Use the available tools to find information.",
        tools=tools,
    )

    # Runner.run orchestrates the full conversation — when the agent
    # wants to use a tool, the runner calls it via Metorial and feeds
    # the result back until the agent produces a final answer
    result = await Runner.run(
        agent, "Search the web for the latest news about AI agents and summarize the top 3 stories."
    )
    print(result.final_output)

# The session is automatically closed when the async with block exits
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
