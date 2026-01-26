"""Autogen integration for Metorial."""

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_autogen_tools(session: "ProviderSession") -> list[dict[str, Any]]:
  """
  Convert Metorial session tools to Autogen function definitions.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of Autogen tool definitions (function schemas)

  Example:
      ```python
      from autogen import AssistantAgent, UserProxyAgent
      from metorial import Metorial
      from metorial.integrations.autogen import create_autogen_tools, get_autogen_tool_executor

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          tools = create_autogen_tools(session)
          tool_executor = get_autogen_tool_executor(session)

          assistant = AssistantAgent(
              name="assistant",
              llm_config={"tools": tools},
          )

          user_proxy = UserProxyAgent(
              name="user",
              function_map=tool_executor,
          )

          user_proxy.initiate_chat(assistant, message="Search for Python news")
      ```
  """
  tools = []
  metorial_tools = session.get_tools()

  for tool in metorial_tools:
    # Handle OpenAI-style format (type: function, function: {name, ...})
    if "function" in tool:
      fn = tool["function"]
      tool_name = fn.get("name", "")
      tool_description = fn.get("description", "")
      input_schema = fn.get("parameters", {})
    else:
      # Handle direct format (name, description, inputSchema)
      tool_name = tool.get("name", "")
      tool_description = tool.get("description", "")
      input_schema = tool.get("inputSchema", {})

    tool_def = {
      "type": "function",
      "function": {
        "name": tool_name,
        "description": tool_description,
        "parameters": input_schema,
      },
    }
    tools.append(tool_def)

  return tools


def get_autogen_tool_executor(session: "ProviderSession") -> dict[str, Callable]:
  """
  Get a function map for Autogen tool execution.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      Dictionary mapping tool names to executor functions

  Example:
      ```python
      tool_executor = get_autogen_tool_executor(session)
      user_proxy = UserProxyAgent(name="user", function_map=tool_executor)
      ```
  """
  import asyncio

  metorial_tools = session.get_tools()
  function_map: dict[str, Callable] = {}

  for tool in metorial_tools:
    # Handle OpenAI-style format (type: function, function: {name, ...})
    if "function" in tool:
      tool_name = tool["function"].get("name", "")
    else:
      tool_name = tool.get("name", "")

    def make_executor(name: str) -> Callable:
      def executor(**kwargs: Any) -> str:
        async def call():
          result = await session.call_tool(name, kwargs)
          if isinstance(result, dict):
            content = result.get("content", [])
            if isinstance(content, list):
              texts = []
              for item in content:
                if isinstance(item, dict) and "text" in item:
                  texts.append(item["text"])
              return "\n".join(texts) if texts else str(result)
            return str(content)
          return str(result)

        try:
          asyncio.get_running_loop()
          import concurrent.futures

          with concurrent.futures.ThreadPoolExecutor() as pool:
            future = pool.submit(asyncio.run, call())
            return future.result()
        except RuntimeError:
          return asyncio.run(call())

      return executor

    function_map[tool_name] = make_executor(tool_name)

  return function_map
