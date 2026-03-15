"""
OpenAI Agents SDK integration example.

Prerequisites:
    pip install metorial openai-agents python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from agents import Agent, Runner

from metorial import Metorial
from metorial.integrations.openai_agents import create_openai_agent_tools


async def main():
    metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

    # Create a deployment for Metorial Search — built-in web search, no auth needed
    deployment = metorial.provider_deployments.create(
        name="Metorial Search",
        provider_id="metorial-search",
    )

    async with metorial.provider_session(
        provider="openai",
        providers=[
            {"provider_deployment_id": deployment.id},
            # (Optional) Add an OAuth provider like Slack or GitHub:
            # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
        ],
    ) as session:
        tools = create_openai_agent_tools(session)

        agent = Agent(
            name="Research Assistant",
            instructions="You are a helpful research assistant. Use the available tools to find information.",
            tools=tools,
        )

        result = await Runner.run(
            agent, "Use the add tool to add 2 and 3. Reply with just the result."
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
