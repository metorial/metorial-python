"""
LangGraph integration example (Magnetar v2).

Prerequisites:
    pip install metorial langgraph langchain-anthropic python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent

from metorial import Metorial
from metorial.integrations.langgraph import create_langgraph_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_langgraph_tools(session)

    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_agent(llm, tools)

    async for event in agent.astream(
      {"messages": [("user", "Search for the latest Python programming news")]}
    ):
      if "agent" in event:
        print(event["agent"]["messages"][-1].content)


if __name__ == "__main__":
  asyncio.run(main())
