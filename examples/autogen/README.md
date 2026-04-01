# Metorial + AutoGen

Uses [AutoGen](https://microsoft.github.io/autogen/) with OpenAI to run an assistant with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default and requires no dashboard setup.

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

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

from metorial import Metorial, metorial_autogen

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

session = await metorial.connect(
    adapter=metorial_autogen(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

model_client = OpenAIChatCompletionClient(model="gpt-4o")
assistant = AssistantAgent(
    name="research_assistant",
    model_client=model_client,
    tools=session.tools(),
    system_message="You are a helpful research assistant.",
)

await Console(
    assistant.run_stream(
        task="Search the web for the latest news about AI agents and summarize the top 3 stories."
    )
)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
