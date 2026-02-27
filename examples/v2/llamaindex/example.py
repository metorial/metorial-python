"""
LlamaIndex integration example (Magnetar v2).

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

  async with metorial.provider_session(
    provider="anthropic",
    providers=[os.getenv("EXA_PROVIDER_DEPLOYMENT_ID")],
  ) as session:
    tools = create_llamaindex_tools(session)
    print(f"Created {len(tools)} tools:")
    for t in tools:
      print(f"  - {t.metadata.name}")

    print("Tools created successfully!")


if __name__ == "__main__":
  asyncio.run(main())
