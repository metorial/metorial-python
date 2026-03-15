# Metorial + LangChain

Uses [LangChain](https://python.langchain.com/) with Anthropic Claude and [LangGraph](https://langchain-ai.github.io/langgraph/) to run a ReAct agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` — from [console.anthropic.com](https://console.anthropic.com)

## Run

```bash
pip install metorial langchain langchain-anthropic langgraph python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

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
    # create_langchain_tools converts MCP tools into LangChain-compatible
    # tool definitions
    tools = create_langchain_tools(session)

    # Pass tools to a LangGraph ReAct agent, which handles the tool call
    # loop automatically
    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_react_agent(llm, tools)

    # The ReAct agent will call tools as needed — making search queries,
    # reading results, and synthesizing a final answer
    result = await agent.ainvoke(
        {"messages": [("user", "Search the web for the latest news about AI agents and summarize the top 3 stories.")]}
    )
    print(result["messages"][-1].content)

# The session is automatically closed when the async with block exits
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
