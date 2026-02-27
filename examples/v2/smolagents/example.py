"""
Hugging Face smolagents integration example (Magnetar v2).

Prerequisites:
    pip install metorial smolagents python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from smolagents import CodeAgent, LiteLLMModel

from metorial import Metorial
from metorial.integrations.smolagents import create_smolagents_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_smolagents_tools(session)

    model = LiteLLMModel(model_id="anthropic/claude-sonnet-4-20250514")
    agent = CodeAgent(tools=tools, model=model)

    result = agent.run("Search for the latest Python programming news")
    print(result)


if __name__ == "__main__":
  asyncio.run(main())
