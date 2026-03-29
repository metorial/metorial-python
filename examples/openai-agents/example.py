"""
OpenAI Agents SDK integration example.

Prerequisites:
    pip install metorial openai-agents python-dotenv
"""

import asyncio
import os

from agents import Agent, Runner
from dotenv import load_dotenv

from metorial import Metorial, metorial_openai_agents

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_openai_agents(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )
  agent = Agent(
    name="Research Assistant",
    instructions="You are a helpful research assistant. Use the available tools to find information.",
    tools=session.tools(),
  )

  result = await Runner.run(
    agent, "Use the add tool to add 2 and 3. Reply with just the result."
  )
  print(result.final_output)


if __name__ == "__main__":
  asyncio.run(main())
