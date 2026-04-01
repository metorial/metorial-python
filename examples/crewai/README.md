# Metorial + CrewAI

Uses [CrewAI](https://www.crewai.com/) with OpenAI to run an agent with MCP tool calls via [Metorial](https://metorial.com). The example uses Metorial Search (built-in web search) by default and requires no dashboard setup.

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

from crewai import Agent, Crew, Task

from metorial import Metorial, metorial_crewai

metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
)

session = await metorial.connect(
    adapter=metorial_crewai(),
    providers=[
        {"provider_deployment_id": deployment.id},
    ],
)

agent = Agent(
    role="Research Assistant",
    goal="Use the available tools to answer questions.",
    backstory="You are a helpful research assistant.",
    tools=session.tools(),
    llm="gpt-4o",
)
task = Task(
    description="Search the web for the latest news about AI agents and summarize the top 3 stories.",
    expected_output="A concise summary of the top 3 stories.",
    agent=agent,
)

crew = Crew(agents=[agent], tasks=[task], verbose=True)
result = await crew.akickoff()
print(result)
```

## Adding OAuth providers

To add a provider that requires OAuth (like Slack or GitHub), uncomment the second entry in the `providers` list and provide your deployment and auth config IDs. See the [main README](../../README.md#authenticating-mcp-tool-providers) for details on setting up OAuth.
