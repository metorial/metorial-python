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
      from metorial import Metorial, metorial_haystack

      metorial = Metorial(api_key="...")

      session = await metorial.connect(
          adapter=metorial_haystack(),
          providers=[{"provider_deployment_id": deployment_id}],
      )
      generator = OpenAIChatGenerator(model="gpt-4o")
      messages = [ChatMessage.from_user("Search for Python news")]
      result = generator.run(messages=messages, tools=session.tools())
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
      input_schema = tool.get("inputSchema") or tool.get("input_schema") or {}

    from metorial.integrations import _sanitize_schema, _sanitize_tool_name

    # Preserve the original MCP tool name for execution; the sanitized name is
    # only the agent-facing identifier exposed to Haystack.
    original_name = tool_name
    tool_name = _sanitize_tool_name(tool_name)
    input_schema = _sanitize_schema(input_schema)

    # Create executor function for this tool
    tool_fn = _create_tool_function(session, original_name)

    haystack_tool = Tool(
      name=tool_name,
      description=tool_description,
      parameters=input_schema,
      function=tool_fn,
    )
    tools.append(haystack_tool)

  return tools


def _create_tool_function(session: "ProviderSession", tool_name: str):
  """Create a tool execution function for Haystack.

  ``tool_name`` is the original MCP tool name used for execution.

  Haystack's ToolInvoker calls tool functions synchronously (possibly from a
  worker thread). We capture the event loop that owns the MCP session at
  creation time and dispatch the async call back to it with
  run_coroutine_threadsafe so the MCP read loop can process the response.
  """
  import asyncio

  # Capture the loop that owns the MCP session while the session is active.
  _loop = asyncio.get_running_loop()

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

    # Dispatch to the session's event loop from whatever thread Haystack
    # calls us on, then block until the result is ready.
    future = asyncio.run_coroutine_threadsafe(call(), _loop)
    return future.result(timeout=120)

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

      session = ...
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
