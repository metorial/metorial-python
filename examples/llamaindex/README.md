# Metorial + LlamaIndex

Uses [LlamaIndex](https://www.llamaindex.ai/) with OpenAI to run a function-calling agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default and requires no dashboard setup.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `OPENAI_API_KEY` — from [platform.openai.com](https://platform.openai.com)

## Run

```bash
pip install metorial llama-index llama-index-llms-openai python-dotenv
python example.py
```

## How it works

This README snippet uses bare `await` for readability. For a runnable script, see [`example.py`](./example.py).

```python
import os

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

from metorial import Metorial, metorial_llamaindex

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

session = await metorial.connect(
    adapter=metorial_llamaindex(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

agent = FunctionAgent(
    llm=OpenAI(model="gpt-4o-mini"),
    tools=session.tools(),
    system_prompt="You are a helpful research assistant.",
)

result = await agent.run(
    "Search the web for the latest news about AI agents and summarize the top 3 stories."
)
print(str(result))
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
