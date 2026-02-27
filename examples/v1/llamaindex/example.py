"""
LlamaIndex integration example.

Prerequisites:
    pip install metorial llama-index llama-index-llms-openai python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from llama_index.llms.openai import OpenAI

from metorial import Metorial
from metorial.integrations.llamaindex import create_llamaindex_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.v1.provider_session(
    provider="openai",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
  ) as session:
    tools = create_llamaindex_tools(session)
    print(f"Created {len(tools)} tools:")
    for t in tools:
      print(f"  - {t.metadata.name}")

    # For a full agent example, use:
    # from llama_index.core.agent.workflow import FunctionAgent
    # agent = FunctionAgent(tools=tools, llm=OpenAI(model="gpt-4o"))
    # response = await agent.run("Search for news")
    print("Tools created successfully!")


if __name__ == "__main__":
  asyncio.run(main())
