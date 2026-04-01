# Metorial + LangChain

Uses [LangChain](https://python.langchain.com/) with Anthropic Claude and [LangGraph](https://langchain-ai.github.io/langgraph/) to run a ReAct agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` — from [console.anthropic.com](https://console.anthropic.com)

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

from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent

# Initialize the Metorial client
from metorial import Metorial, metorial_langchain

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Connect and resolve LangChain tools directly
session = await metorial.connect(
    adapter=metorial_langchain(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

# Pass tools to a LangGraph ReAct agent, which handles the tool call
# loop automatically
llm = ChatAnthropic(model="claude-sonnet-4-20250514")
agent = create_react_agent(llm, session.tools())

# The ReAct agent will call tools as needed — making search queries,
# reading results, and synthesizing a final answer
result = await agent.ainvoke(
    {"messages": [("user", "Search the web for the latest news about AI agents and summarize the top 3 stories.")]}
)
print(result["messages"][-1].content)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
