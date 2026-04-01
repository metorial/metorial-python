"""
AutoGen integration example.

Prerequisites:
    pip install metorial autogen-agentchat autogen-ext python-dotenv
"""

import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

from metorial import Metorial, metorial_autogen

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_autogen(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )

  model_client = OpenAIChatCompletionClient(model="gpt-4o")
  assistant = AssistantAgent(
    name="assistant",
    model_client=model_client,
    tools=session.tools(),
    system_message="You are a helpful research assistant.",
  )

  await Console(
    assistant.run_stream(task="Use the add tool to add 2 and 3. Reply with just the result.")
  )


if __name__ == "__main__":
  asyncio.run(main())
