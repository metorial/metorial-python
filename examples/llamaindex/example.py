"""
LlamaIndex integration example.

Prerequisites:
    pip install metorial llama-index llama-index-llms-anthropic python-dotenv
"""

import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

from metorial import Metorial
from metorial.integrations.llamaindex import create_llamaindex_tools


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
        tools = create_llamaindex_tools(session)

        print(f"Created {len(tools)} tools:")
        for t in tools:
            print(f"  - {t.metadata.name}")

        # Use with a LlamaIndex agent:
        # from llama_index.llms.anthropic import Anthropic
        # from llama_index.core.agent import FunctionCallingAgent
        #
        # llm = Anthropic(model="claude-sonnet-4-20250514")
        # agent = FunctionCallingAgent.from_tools(tools, llm=llm)
        # response = await agent.achat(
        #     "Use the add tool to add 2 and 3. Reply with just the result."
        # )
        # print(response)


if __name__ == "__main__":
    asyncio.run(main())
