"""
LangGraph integration example.

Prerequisites:
    pip install metorial langgraph langchain-openai python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from metorial import Metorial
from metorial.integrations.langgraph import create_langgraph_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="openai",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
  ) as session:
    tools = create_langgraph_tools(session)

    llm = ChatOpenAI(model="gpt-4o")
    agent = create_react_agent(llm, tools)

    async for event in agent.astream(
      {"messages": [("user", "Search for the latest Python programming news")]}
    ):
      if "agent" in event:
        print(event["agent"]["messages"][-1].content)


if __name__ == "__main__":
  asyncio.run(main())
