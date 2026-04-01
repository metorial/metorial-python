"""
LlamaIndex integration example.

Prerequisites:
    cp .env.example .env
    pip install -r requirements.txt
"""

import asyncio
import os

from dotenv import load_dotenv
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

from metorial import Metorial, metorial_llamaindex

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_llamaindex(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )

  agent = FunctionAgent(
    llm=OpenAI(model="gpt-4o-mini"),
    tools=session.tools(),
    system_prompt="Use one tool then respond briefly.",
  )

  result = await agent.run(
    "Use the add tool to add 2 and 3. Reply with just the result."
  )
  print(str(result))


if __name__ == "__main__":
  asyncio.run(main())
