"""
LangGraph integration example.

Prerequisites:
    pip install metorial langgraph langchain-anthropic python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_react_agent

from metorial import Metorial
from metorial.integrations.langgraph import create_langgraph_tools


async def main():
    metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

    # Create a deployment for Metorial Search — built-in web search, no auth needed
    deployment = metorial.provider_deployments.create(
        name="Metorial Search",
        provider_id="metorial-search",
    )

    async with metorial.provider_session(
        provider="anthropic",
        providers=[
            {"provider_deployment_id": deployment.id},
            # (Optional) Add an OAuth provider like Slack or GitHub:
            # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
        ],
    ) as session:
        tools = create_langgraph_tools(session)

        llm = ChatAnthropic(model="claude-sonnet-4-20250514")
        agent = create_react_agent(llm, tools)

        async for event in agent.astream(
            {"messages": [("user", "Use the add tool to add 2 and 3. Reply with just the result.")]}
        ):
            if "agent" in event:
                print(event["agent"]["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
