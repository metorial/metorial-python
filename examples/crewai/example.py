"""
CrewAI integration example.

Prerequisites:
    cp .env.example .env
    pip install -r requirements.txt
"""

import asyncio
import os

from crewai import Agent, Crew, Task
from dotenv import load_dotenv

from metorial import Metorial, metorial_crewai

load_dotenv()


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_crewai(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )

  agent = Agent(
    role="Research Assistant",
    goal="Use the available tools to answer questions.",
    backstory="You are a helpful research assistant.",
    tools=session.tools(),
    llm="gpt-4o",
    verbose=True,
  )
  task = Task(
    description="Use the add tool to add 2 and 3. Reply with just the result.",
    expected_output="Just the result.",
    agent=agent,
  )

  crew = Crew(agents=[agent], tasks=[task], verbose=True)
  result = await crew.akickoff()
  print(result)


if __name__ == "__main__":
  asyncio.run(main())
