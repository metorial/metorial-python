# Metorial + Haystack

Uses [deepset Haystack](https://haystack.deepset.ai/) with OpenAI GPT-4o to run a pipeline with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default — no dashboard setup needed.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `OPENAI_API_KEY` — from [platform.openai.com](https://platform.openai.com)

## Run

```bash
pip install metorial haystack-ai python-dotenv
python example.py
```

## How it works

```python
# Initialize the Metorial client
from metorial import Metorial, metorial_haystack

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

# Create a deployment for Metorial Search
deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

# Connect and resolve Haystack tools directly
session = await metorial.connect(
    adapter=metorial_haystack(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

# Tools are used by both the OpenAIChatGenerator (which tells the LLM
# about available tools) and the ToolInvoker (which executes tool calls)
tools = session.tools()
generator = OpenAIChatGenerator(model="gpt-4o", tools=tools)
tool_invoker = ToolInvoker(tools=tools)

# Build the pipeline — connect the generator's output to the tool
# invoker. When GPT-4o requests a tool call, Haystack routes it
# through the invoker which calls Metorial, and the results are
# returned.
pipeline = Pipeline()
pipeline.add_component("generator", generator)
pipeline.add_component("tool_invoker", tool_invoker)
pipeline.connect("generator.replies", "tool_invoker.messages")

# Run the pipeline
messages = [ChatMessage.from_user(
    "Search the web for the latest news about AI agents and summarize the top 3 stories."
)]
result = pipeline.run({"generator": {"messages": messages}})
print(result["tool_invoker"]["tool_messages"])
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
