"""
Google ADK integration example.

Prerequisites:
    cp .env.example .env
    pip install -r requirements.txt
"""

import asyncio
import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from metorial import Metorial, metorial_google_adk

load_dotenv()

APP_NAME = "metorial-google-adk"
USER_ID = "example-user"
SESSION_ID = "example-session"


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))

  # Create a deployment for Metorial Search — built-in web search, no auth needed
  deployment = metorial.provider_deployments.create(
    name="Metorial Search",
    provider_id="metorial-search",
  )

  session = await metorial.connect(
    adapter=metorial_google_adk(),
    providers=[
      {"provider_deployment_id": deployment.id},
      # (Optional) Add an OAuth provider like Slack or GitHub:
      # {"provider_deployment_id": "your-slack-deployment-id", "provider_auth_config_id": "auth-config-id"},
    ],
  )

  agent = Agent(
    model="gemini-2.0-flash",
    name="research_assistant",
    description="A helpful research assistant.",
    instruction="Use the available tools to answer the user's question.",
    tools=session.tools(),
  )

  session_service = InMemorySessionService()
  await session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
  )

  runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service,
  )
  message = types.Content(
    role="user",
    parts=[
      types.Part(text="Use the add tool to add 2 and 3. Reply with just the result.")
    ],
  )

  events = runner.run_async(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=message,
  )
  async for event in events:
    if event.is_final_response() and event.content and event.content.parts:
      print(event.content.parts[0].text)


if __name__ == "__main__":
  asyncio.run(main())
