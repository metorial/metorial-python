"""
Microsoft Autogen integration example.

Prerequisites:
    pip install metorial pyautogen python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from autogen import AssistantAgent, UserProxyAgent

from metorial import Metorial
from metorial.integrations.autogen import (
  create_autogen_tools,
  get_autogen_tool_executor,
)


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.v1.provider_session(
    provider="openai",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
  ) as session:
    tools = create_autogen_tools(session)
    tool_executor = get_autogen_tool_executor(session)

    llm_config = {
      "config_list": [{"model": "gpt-4o", "api_key": os.getenv("OPENAI_API_KEY")}],
      "tools": tools,
    }

    assistant = AssistantAgent(
      name="research_assistant",
      system_message="You are a helpful research assistant. Use the available tools to find information.",
      llm_config=llm_config,
    )

    user_proxy = UserProxyAgent(
      name="user",
      human_input_mode="NEVER",
      max_consecutive_auto_reply=5,
      function_map=tool_executor,
    )

    await user_proxy.a_initiate_chat(
      assistant,
      message="Search for the latest Python programming news",
    )


if __name__ == "__main__":
  asyncio.run(main())
