import asyncio

from openai import OpenAI

from metorial import MetorialMcpSession
from metorial_openai import MetorialOpenAISession

OPENAI_MODEL     = "gpt-4o"
METORIAL_API_KEY = "...metorial-api-key..."
OPENAI_API_KEY   = "...openai-api-key..."
DEPLOYMENTS      = ["...server-deployment-id..."]

async def run_chat(session, open_ai):
  messages = [{
    "role": "user",
    "content": ("Summarize the notion page with id page_id ...page-id... in my workspace."),
  }]

  for _ in range(10):
    resp = open_ai.chat.completions.create(
      model="gpt-4o",
      messages=messages,
      tools=session.tools,
    )
    msg = resp.choices[0].message
    tool_calls = msg.tool_calls

    if not tool_calls:  # final answer
      print(msg.content)
      return

    # Execute tool calls
    tool_msgs = await session.call_tools(tool_calls)

    # Add assistant tool_calls message
    messages.append({
      "role": "assistant",
      "tool_calls": msg.tool_calls,
    })
    
    # Add each tool result
    messages.extend(tool_msgs)

  # only reached if the loop never broke
  raise RuntimeError("No final response after 10 iterations")

async def main():
  mcp_session = MetorialMcpSession(
    api_key=METORIAL_API_KEY,
    server_deployment_ids=DEPLOYMENTS
  )
  tool_manager = await mcp_session.get_tool_manager()
  metorial_session = MetorialOpenAISession(tool_manager)

  open_ai = OpenAI(api_key=OPENAI_API_KEY)

  try:
    await run_chat(metorial_session, open_ai)
  finally:
    # swallow the anyio cancel-scope noise
    try:
      await mcp_session.close()
    except Exception:
      pass

if __name__ == "__main__":
  asyncio.run(main())