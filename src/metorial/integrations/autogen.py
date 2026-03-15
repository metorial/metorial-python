"""Autogen integration for Metorial."""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from autogen_core.tools import FunctionTool
except ImportError:
  FunctionTool = None


def create_autogen_tools(session: "ProviderSession") -> list[Any]:
  """
  Convert Metorial session tools to Autogen FunctionTool objects.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      List of Autogen FunctionTool objects

  Example:
      ```python
      from autogen_agentchat.agents import AssistantAgent
      from autogen_ext.models.anthropic import AnthropicChatCompletionClient
      from metorial import Metorial
      from metorial.integrations.autogen import create_autogen_tools

      metorial = Metorial(api_key="...")

      async with metorial.provider_session(
          provider="anthropic",
          providers=[{"session_template_id": "deployment-id"}],
      ) as session:
          tools = create_autogen_tools(session)

          model_client = AnthropicChatCompletionClient(model="claude-sonnet-4-20250514")
          assistant = AssistantAgent(
              name="assistant",
              model_client=model_client,
              tools=tools,
          )
      ```
  """
  if FunctionTool is None:
    raise ImportError(
      "autogen-core is required for Autogen integration. "
      "Install it with: pip install autogen-agentchat autogen-ext"
    )

  tools = []
  tool_manager = session.tool_manager

  if tool_manager is None:
    return tools

  for tool in tool_manager.get_tools():
    tool_name = tool.name
    tool_description = tool.description or f"Tool: {tool_name}"

    schema = tool.get_parameters_as("json-schema") or {}
    properties = schema.get("properties", {})
    required_params = set(schema.get("required", []))

    # Build parameter list for the function signature
    type_map = {
      "string": str,
      "integer": int,
      "number": float,
      "boolean": bool,
      "array": list,
      "object": dict,
    }

    # Sort: required params first, optional params after
    required_props = [(n, s) for n, s in properties.items() if n in required_params]
    optional_props = [(n, s) for n, s in properties.items() if n not in required_params]

    params = []
    param_annotations = {}
    for prop_name, prop_schema in required_props + optional_props:
      json_type = prop_schema.get("type", "string")
      py_type = type_map.get(json_type, str)
      if prop_name not in required_params:
        py_type = py_type | None
      param_annotations[prop_name] = py_type
      if prop_name in required_params:
        params.append(f"{prop_name}: __annotations__['{prop_name}']")
      else:
        params.append(f"{prop_name}: __annotations__['{prop_name}'] = None")
    param_annotations["return"] = str

    func_name = tool_name.replace("-", "_")
    params_str = ", ".join(params) if params else ""

    # Dynamically create a function with explicit parameters
    # so autogen's FunctionTool can inspect the signature
    func_code = f"async def {func_name}({params_str}) -> str:\n"
    func_code += f"  '''{ tool_description }'''\n"
    func_code += f"  _kwargs = {{{', '.join(repr(p) + ': ' + p for p in properties)}}}\n"
    func_code += "  _kwargs = {k: v for k, v in _kwargs.items() if v is not None}\n"
    func_code += "  return await _executor(_tool_name, _kwargs)\n"

    async def _make_executor(name: str):
      async def _executor(tool_name_inner: str, kwargs: dict) -> str:
        try:
          result = await tool_manager.execute_tool(tool_name_inner, kwargs)
          if hasattr(result, "model_dump"):
            result = result.model_dump()
          return json.dumps(result, ensure_ascii=False, default=str)
        except Exception as e:
          return json.dumps({"error": str(e)}, ensure_ascii=False)
      return _executor

    import asyncio
    # We can't await here, so create the executor synchronously
    def _make_executor_sync(name: str):
      async def _executor(tool_name_inner: str, kwargs: dict) -> str:
        try:
          result = await tool_manager.execute_tool(tool_name_inner, kwargs)
          if hasattr(result, "model_dump"):
            result = result.model_dump()
          return json.dumps(result, ensure_ascii=False, default=str)
        except Exception as e:
          return json.dumps({"error": str(e)}, ensure_ascii=False)
      return _executor

    executor = _make_executor_sync(tool_name)
    local_ns: dict[str, Any] = {
      "_executor": executor,
      "_tool_name": tool_name,
      "__annotations__": param_annotations,
    }
    exec(func_code, local_ns)  # noqa: S102
    fn = local_ns[func_name]

    autogen_tool = FunctionTool(fn, description=tool_description, name=func_name)
    tools.append(autogen_tool)

  return tools


def get_autogen_tool_executor(session: "ProviderSession") -> dict[str, Callable]:
  """
  Get a function map for legacy Autogen tool execution.

  .. deprecated::
      Use create_autogen_tools() with the new Autogen API instead.

  Args:
      session: An active Metorial ProviderSession

  Returns:
      Dictionary mapping tool names to executor functions
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
