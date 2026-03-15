"""
deepset Haystack integration example.

Prerequisites:
    pip install metorial haystack-ai python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from haystack import Pipeline
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.components.tools import ToolInvoker
from haystack.dataclasses import ChatMessage

from metorial import Metorial
from metorial.integrations.haystack import create_haystack_tools


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
        tools = create_haystack_tools(session)

        generator = OpenAIChatGenerator(model="gpt-4o", tools=tools)
        tool_invoker = ToolInvoker(tools=tools)

        pipeline = Pipeline()
        pipeline.add_component("generator", generator)
        pipeline.add_component("tool_invoker", tool_invoker)
        pipeline.connect("generator.replies", "tool_invoker.messages")

        messages = [ChatMessage.from_user(
            "Search the web for the latest news about AI agents and summarize the top 3 stories."
        )]
        result = pipeline.run({"generator": {"messages": messages}})

        print(result["tool_invoker"]["tool_messages"])


if __name__ == "__main__":
    asyncio.run(main())
