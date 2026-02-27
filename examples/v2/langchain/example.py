"""
LangChain integration example (Magnetar v2).

Prerequisites:
    pip install metorial langchain langchain-anthropic langgraph python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent

from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools

async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))
  
  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_langchain_tools(session)

    llm = ChatAnthropic(model="claude-sonnet-4-20250514")
    agent = create_agent(llm, tools)

    result = agent.invoke(
      {"messages": [("user", "Search for the latest Python programming news")]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
  asyncio.run(main())
