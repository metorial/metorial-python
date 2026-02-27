"""
Microsoft Semantic Kernel integration example (Magnetar v2).

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
from semantic_kernel.connectors.ai.anthropic import AnthropicChatCompletion
from semantic_kernel.contents.chat_history import ChatHistory

from metorial import Metorial
from metorial.integrations.semantic_kernel import register_metorial_plugin


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    kernel = sk.Kernel()

    service = AnthropicChatCompletion(
      service_id="chat",
      ai_model_id="claude-sonnet-4-20250514",
    )
    kernel.add_service(service)

    register_metorial_plugin(kernel, session)

    settings = kernel.get_prompt_execution_settings_from_service_id("chat")
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    history = ChatHistory()
    history.add_user_message("Search for the latest Python programming news")

    result = await service.get_chat_message_contents(
      chat_history=history,
      settings=settings,
      kernel=kernel,
    )
    print(result[0] if result else "No response")


if __name__ == "__main__":
  asyncio.run(main())
