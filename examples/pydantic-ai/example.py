"""
PydanticAI integration example.

Prerequisites:
    cp .env.example .env
    pip install -r requirements.txt
"""

import asyncio
import os

from dotenv import load_dotenv
from pydantic_ai import Agent

from metorial import Metorial, metorial_pydantic_ai

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_pydantic_ai(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )
  agent = Agent(
    "anthropic:claude-sonnet-4-20250514",
    system_prompt="You are a helpful research assistant.",
    tools=session.tools(),
  )

  result = await agent.run(
    "Use the add tool to add 2 and 3. Reply with just the result."
  )
  output = getattr(result, "data", None) or getattr(result, "output", str(result))
  print(output)


if __name__ == "__main__":
  asyncio.run(main())
