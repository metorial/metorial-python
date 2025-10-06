import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

from metorial import Metorial
from anthropic import AsyncAnthropic


async def main():
  metorial = Metorial(api_key=os.getenv("METORIAL_API_KEY"))
  anthropic = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

  google_cal_deployment_id = os.getenv("GOOGLE_CALENDAR_DEPLOYMENT_ID")

  print("🔗 Creating OAuth session...")
  oauth_session = metorial.oauth.sessions.create(
    server_deployment_id=google_cal_deployment_id
  )

  print("OAuth URLs for user authentication:")
  print(f"   Google Calendar: {oauth_session.url}")

  print("\n⏳ Waiting for OAuth completion...")
  await metorial.oauth.wait_for_completion([oauth_session])

  print("✅ OAuth session completed!")

  hackernews_deployment_id = os.getenv("HACKERNEWS_DEPLOYMENT_ID")

  result = await metorial.run(
    message="""Search Hackernews for the latest AI discussions using the available tools. Then create a
    calendar event using Google Calendar tools with my@email.address for tomorrow at 2pm to discuss AI trends.""",
    server_deployments=[
      { "serverDeploymentId": google_cal_deployment_id, "oauthSessionId": oauth_session.id },
      { "serverDeploymentId": hackernews_deployment_id },
    ],
    client=anthropic,
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    max_steps=25,
  )
  print(result["text"])

if __name__ == "__main__":
  asyncio.run(main())
