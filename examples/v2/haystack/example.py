"""
deepset Haystack integration example (Magnetar v2).

Prerequisites:
    pip install metorial haystack-ai haystack-ai-provider-anthropic python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from haystack import Pipeline
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.tools import ToolInvoker
from haystack.dataclasses import ChatMessage

from metorial import Metorial
from metorial.integrations.haystack import create_haystack_tools


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_haystack_tools(session)

    generator = OpenAIChatGenerator(model="gpt-4o", tools=tools)
    tool_invoker = ToolInvoker(tools=tools)

    pipeline = Pipeline()
    pipeline.add_component("generator", generator)
    pipeline.add_component("tool_invoker", tool_invoker)
    pipeline.connect("generator.replies", "tool_invoker.messages")

    messages = [ChatMessage.from_user("Search for the latest Python programming news")]
    result = pipeline.run({"generator": {"messages": messages}})

    print(result["tool_invoker"]["tool_messages"])


if __name__ == "__main__":
  asyncio.run(main())
