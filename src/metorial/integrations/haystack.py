"""Haystack (deepset) integration for Metorial."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_haystack_tools(session: "ProviderSession") -> list[Any]:
  """
  Convert Metorial session tools to Haystack Tool objects.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of Haystack Tool objects

  Example:
      ```python
      from haystack.components.generators.chat import OpenAIChatGenerator
      from haystack.dataclasses import ChatMessage
      from metorial import Metorial
      from metorial.integrations.haystack import create_haystack_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="openai",
          server_deployments=[deployment_id],
      ) as session:
          tools = create_haystack_tools(session)

          generator = OpenAIChatGenerator(model="gpt-4o")
          messages = [ChatMessage.from_user("Search for Python news")]
          result = generator.run(messages=messages, tools=tools)
      ```
  """
  try:
    from haystack.tools import Tool
  except ImportError as e:
    raise ImportError(
      "Haystack is required for this integration. "
      "Install it with: pip install haystack-ai"
    ) from e

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

    # Create executor function for this tool
    tool_fn = _create_tool_function(session, tool_name)

    haystack_tool = Tool(
      name=tool_name,
      description=tool_description,
      parameters=input_schema,
      function=tool_fn,
    )
    tools.append(haystack_tool)

  return tools


def _create_tool_function(session: "ProviderSession", tool_name: str):
  """Create a tool execution function for Haystack."""
  import asyncio

  def tool_fn(**kwargs: Any) -> str:
    async def call():
      result = await session.call_tool(tool_name, kwargs)
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

  return tool_fn


def create_haystack_tool_invoker(session: "ProviderSession") -> Any:
  """
  Create a Haystack ToolInvoker component with Metorial tools.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      A Haystack ToolInvoker component

  Example:
      ```python
      from haystack import Pipeline
      from haystack.components.generators.chat import OpenAIChatGenerator
      from metorial.integrations.haystack import create_haystack_tools, create_haystack_tool_invoker

      async with metorial.provider_session(...) as session:
          tools = create_haystack_tools(session)
          tool_invoker = create_haystack_tool_invoker(session)

          pipeline = Pipeline()
          pipeline.add_component("generator", OpenAIChatGenerator(tools=tools))
          pipeline.add_component("tool_invoker", tool_invoker)
          pipeline.connect("generator.replies", "tool_invoker.messages")
      ```
  """
  try:
    from haystack.components.tools import ToolInvoker
  except ImportError as e:
    raise ImportError(
      "Haystack is required for this integration. "
      "Install it with: pip install haystack-ai"
    ) from e

  tools = create_haystack_tools(session)
  return ToolInvoker(tools=tools)
