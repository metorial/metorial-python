"""
PydanticAI integration example.

Prerequisites:
    pip install metorial pydantic-ai python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from pydantic_ai import Agent

from metorial import Metorial
from metorial.integrations.pydantic_ai import create_pydantic_ai_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="anthropic",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
  ) as session:
    tools = create_pydantic_ai_tools(session)

    agent = Agent(
      "anthropic:claude-sonnet-4-20250514",
      system_prompt="You are a helpful research assistant.",
      tools=tools,
    )

    result = await agent.run("Search for the latest Python programming news")
    # Handle different pydantic-ai versions
    output = getattr(result, "data", None) or getattr(result, "output", str(result))
    print(output)


if __name__ == "__main__":
  asyncio.run(main())
