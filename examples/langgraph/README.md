# Metorial + LangGraph

Uses [LangGraph](https://langchain-ai.github.io/langgraph/) with Anthropic Claude to run a streaming ReAct agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` — from [console.anthropic.com](https://console.anthropic.com)

## Run

```bash
pip install metorial langgraph langchain-anthropic python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial
from metorial.integrations.langgraph import create_langgraph_tools

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Open a provider session
async with metorial.provider_session(
    provider="anthropic",
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
) as session:
    # create_langgraph_tools converts MCP tools into LangGraph-compatible
    # tool definitions
    tools = create_langgraph_tools(session)

    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_react_agent(llm, tools)

    # The key difference from the LangChain example is streaming —
    # astream yields events as the agent works, letting you see
    # intermediate results
    async for event in agent.astream(
        {"messages": [("user", "Search the web for the latest news about AI agents and summarize the top 3 stories.")]}
    ):
        # Each event contains the agent's latest message. The agent will
        # call tools as needed — making search queries, reading results —
        # and stream partial answers as they become available
        if "agent" in event:
            print(event["agent"]["messages"][-1].content)

# The session is automatically closed when the async with block exits
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
