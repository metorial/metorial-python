"""
Microsoft Semantic Kernel integration example.

Prerequisites:
    pip install metorial semantic-kernel python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

import semantic_kernel as sk
from semantic_kernel.connectors.ai.function_choice_behavior import (
  FunctionChoiceBehavior,
)
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory

from metorial import Metorial
from metorial.integrations.semantic_kernel import register_metorial_plugin


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="openai",
    server_deployments=[os.getenv("EXA_DEPLOYMENT_ID")],
  ) as session:
    kernel = sk.Kernel()

    service = OpenAIChatCompletion(
      service_id="chat",
      ai_model_id="gpt-4o",
    )
    kernel.add_service(service)

    register_metorial_plugin(kernel, session)

    settings = kernel.get_prompt_execution_settings_from_service_id("chat")
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    history = ChatHistory()
    history.add_user_message("Search for the latest Python programming news")

    result = await kernel.invoke_prompt(
      prompt="{{$history}}",
      history=history,
      settings=settings,
    )
    print(result)


if __name__ == "__main__":
  asyncio.run(main())
