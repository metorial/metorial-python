# Metorial + Google ADK

Uses [Google ADK](https://google.github.io/adk-docs/) with Gemini to run an agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default and requires no dashboard setup.

## Environment variables

- `METORIAL_API_KEY` — get one at [platform.metorial.com](https://platform.metorial.com)
- `GOOGLE_API_KEY` — from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Run

```bash
pip install metorial google-adk google-genai python-dotenv
python example.py
```

## How it works

This README snippet uses bare `await` for readability. For a runnable script, see [`example.py`](./example.py).

```python
import os

from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from metorial import Metorial, metorial_google_adk

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

session = await metorial.connect(
    adapter=metorial_google_adk(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

agent = Agent(
    model="gemini-2.0-flash",
    name="research_assistant",
    description="A helpful research assistant.",
    instruction="Use the available tools to answer the user's question.",
    tools=session.tools(),
)

session_service = InMemorySessionService()
await session_service.create_session(
    app_name="metorial-google-adk",
    user_id="example-user",
    session_id="session-1",
)
runner = Runner(
    agent=agent,
    app_name="metorial-google-adk",
    session_service=session_service,
)
message = types.Content(
    role="user",
    parts=[types.Part(text="Search the web for the latest news about AI agents and summarize the top 3 stories.")],
)

events = runner.run_async(
    user_id="example-user",
    session_id="session-1",
    new_message=message,
)
async for event in events:
    if event.is_final_response():
        print(event.content.parts[0].text)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
