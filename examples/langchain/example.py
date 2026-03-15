"""
LangChain integration example.

Prerequisites:
    pip install metorial langchain langchain-anthropic langgraph python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain.agents import create_react_agent

from metorial import Metorial
from metorial.integrations.langchain import create_langchain_tools


async def main():
    metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

    # Create a deployment for Metorial Search — built-in web search, no auth needed
    deployment = metorial.provider_deployments.create(
        name="Example Search",
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
        tools = create_langchain_tools(session)

        llm = ChatAnthropic(model="claude-sonnet-4-20250514")
        agent = create_react_agent(llm, tools)

        result = await agent.ainvoke(
            {"messages": [("user", "Use the add tool to add 2 and 3. Reply with just the result.")]}
        )
        print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
