# Metorial + LlamaIndex

Uses [LlamaIndex](https://docs.llamaindex.ai/) to create MCP-powered tools via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `ANTHROPIC_API_KEY` — from [console.anthropic.com](https://console.anthropic.com) (if using the agent code)

## Run

```bash
pip install metorial llama-index llama-index-llms-anthropic python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial
from metorial.integrations.llamaindex import create_llamaindex_tools

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
    # create_llamaindex_tools converts MCP tools into LlamaIndex
    # FunctionTool objects. The example prints the available tools
    # to verify the integration works.
    tools = create_llamaindex_tools(session)

    # To use the tools with a LlamaIndex agent, uncomment the agent
    # code in the example. It creates a FunctionCallingAgent with
    # Anthropic Claude that handles tool calls automatically.
    from llama_index.llms.anthropic import Anthropic
    from llama_index.core.agent import FunctionCallingAgent

    llm = Anthropic(model="claude-sonnet-4-20250514")
    agent = FunctionCallingAgent.from_tools(tools, llm=llm)
    response = await agent.achat(
        "Search the web for the latest news about AI agents and summarize the top 3 stories."
    )

# The session is automatically closed when the async with block exits
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
