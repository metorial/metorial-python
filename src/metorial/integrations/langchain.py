"""
LangChain integration for Metorial tools.

Example:
    from langchain_anthropic import ChatAnthropic
    from langchain.agents import create_tool_calling_agent, AgentExecutor
    from metorial import Metorial
    from metorial.integrations.langchain import create_langchain_tools

    metorial = Metorial(api_key="...")

    async with metorial.provider_session(
        provider="anthropic",
        server_deployments=["deployment-id"],
    ) as session:
        tools = create_langchain_tools(session)

        agent = create_tool_calling_agent(ChatAnthropic(), tools, prompt)
        executor = AgentExecutor(agent=agent, tools=tools)

        result = await executor.ainvoke({"input": "Search for news"})
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from langchain_core.tools import StructuredTool
except ImportError:
  StructuredTool = None


def create_langchain_tools(session: ProviderSession) -> list[Any]:
  """Convert Metorial session tools to LangChain tools.

  Args:
      session: Active Metorial ProviderSession

  Returns:
      List of LangChain StructuredTool objects

  Raises:
      ImportError: If langchain-core is not installed
  """
  if StructuredTool is None:
    raise ImportError(
      "langchain-core is required for LangChain integration. "
      "Install it with: pip install langchain-core"
    )

  tools = []
  tool_manager = session.tool_manager

  if tool_manager is None:
    return tools

  for tool in tool_manager.get_tools():
    # Get the tool's parameters schema
    schema = tool.get_parameters_as("json-schema") or {}

    # Capture tool_name in closure to avoid late binding issues
    def make_tool_fn(tool_name: str):
      async def tool_fn(**kwargs: Any) -> str:
        # Filter out None values - LangChain includes these for optional params
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        result = await tool_manager.execute_tool(tool_name, filtered_kwargs)
        if hasattr(result, "model_dump"):
          result = result.model_dump()
        return json.dumps(result, ensure_ascii=False, default=str)

      return tool_fn

    # Create the LangChain tool
    lc_tool = StructuredTool.from_function(
      coroutine=make_tool_fn(tool.name),
      name=tool.name,
      description=tool.description or f"Tool: {tool.name}",
      args_schema=_schema_to_pydantic(tool.name, schema),
    )
    tools.append(lc_tool)

  return tools


def _schema_to_pydantic(name: str, schema: dict[str, Any]) -> Any:
  """Convert JSON schema to Pydantic model for LangChain."""
  try:
    from pydantic import Field, create_model
  except ImportError:
    return None

  properties = schema.get("properties", {})
  required = set(schema.get("required", []))

  fields = {}
  for prop_name, prop_schema in properties.items():
    prop_type = _json_type_to_python(prop_schema.get("type", "string"))
    description = prop_schema.get("description", "")
    default = ... if prop_name in required else None

    fields[prop_name] = (prop_type, Field(default=default, description=description))

  return create_model(f"{name}Input", **fields)


def _json_type_to_python(json_type: str) -> type:
  """Convert JSON schema type to Python type."""
  type_map = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
    "object": dict,
  }
  return type_map.get(json_type, str)


__all__ = ["create_langchain_tools"]
