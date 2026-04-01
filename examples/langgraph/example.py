"""
LangGraph integration example.

Prerequisites:
    cp .env.example .env
    pip install -r requirements.txt
"""

import asyncio
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

from metorial import Metorial, metorial_langgraph

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_langgraph(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )
  llm = ChatAnthropic(model="claude-sonnet-4-20250514")
  agent = create_agent(
    llm,
    tools=session.tools(),
    system_prompt="Use one tool then respond briefly.",
  )

  result = await agent.ainvoke(
    {
      "messages": [
        ("user", "Use the add tool to add 2 and 3. Reply with just the result.")
      ]
    }
  )
  print(result["messages"][-1].content)


if __name__ == "__main__":
  asyncio.run(main())
