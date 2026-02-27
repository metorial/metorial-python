"""
OpenAI Agents SDK integration example (Magnetar v2).

Prerequisites:
    pip install metorial openai-agents python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from agents import Agent, Runner

from metorial import Metorial
from metorial.integrations.openai_agents import create_openai_agent_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="openai",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_openai_agent_tools(session)

    agent = Agent(
      name="Research Assistant",
      instructions="You are a helpful research assistant. Use the available tools to find information.",
      tools=tools,
    )

    result = await Runner.run(agent, "Search for the latest Python programming news")
    print(result.final_output)


if __name__ == "__main__":
  asyncio.run(main())
