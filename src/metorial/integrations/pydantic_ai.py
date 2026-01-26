"""
PydanticAI integration for Metorial tools.

Example:
    from pydantic_ai import Agent
    from metorial import Metorial
    from metorial.integrations.pydantic_ai import create_pydantic_ai_tools

    metorial = Metorial(api_key="...")

    async with metorial.provider_session(
        provider="openai",
        server_deployments=["deployment-id"],
    ) as session:
        tools = create_pydantic_ai_tools(session)

        agent = Agent("openai:gpt-4o", tools=tools)

        result = await agent.run("Search for news")
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from pydantic_ai import Agent, RunContext, Tool
except ImportError:
  Agent = None
  RunContext = None
  Tool = None


def register_metorial_tools(agent: Any, session: ProviderSession) -> None:
  """Register Metorial tools with a PydanticAI agent.

  Args:
      agent: PydanticAI Agent instance
      session: Active Metorial ProviderSession

  Raises:
      ImportError: If pydantic-ai is not installed
  """
  if Agent is None:
    raise ImportError(
      "pydantic-ai is required for PydanticAI integration. "
      "Install it with: pip install pydantic-ai"
    )

  tool_manager = session.tool_manager

  if tool_manager is None:
    return

  for tool in tool_manager.get_tools():
    _register_single_tool(agent, tool, tool_manager)


def _register_single_tool(agent: Any, tool: Any, tool_manager: Any) -> None:
  """Register a single Metorial tool with the agent."""
  tool_name = tool.name
  tool_description = tool.description or f"Tool: {tool_name}"

  # Create tool function without ctx parameter (PydanticAI v2 doesn't require it)
  async def metorial_tool(**kwargs: Any) -> str:
    """Dynamic Metorial tool wrapper."""
    # Filter out None values
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    result = await tool_manager.execute_tool(tool_name, filtered_kwargs)
    if hasattr(result, "model_dump"):
      result = result.model_dump()
    return json.dumps(result, ensure_ascii=False, default=str)

  # Override the function metadata
  metorial_tool.__name__ = tool_name
  metorial_tool.__doc__ = tool_description

  # Register with agent
  agent.tool(metorial_tool, name=tool_name)


def create_pydantic_ai_tools(session: ProviderSession) -> list[Any]:
  """Create PydanticAI Tool objects from Metorial session.

  For advanced usage where you want to manually add tools.

  Args:
      session: Active Metorial ProviderSession

  Returns:
      List of PydanticAI Tool objects

  Raises:
      ImportError: If pydantic-ai is not installed
  """
  if Tool is None:
    raise ImportError(
      "pydantic-ai is required for PydanticAI integration. "
      "Install it with: pip install pydantic-ai"
    )

  tools = []
  tool_manager = session.tool_manager

  if tool_manager is None:
    return tools

  for tool in tool_manager.get_tools():
    pydantic_tool = _create_pydantic_tool(tool, tool_manager)
    tools.append(pydantic_tool)

  return tools


def _create_pydantic_tool(tool: Any, tool_manager: Any) -> Any:
  """Create a PydanticAI Tool from a Metorial tool."""
  from pydantic import Field, create_model

  tool_name = tool.name
  tool_description = tool.description or f"Tool: {tool_name}"
  schema = tool.get_parameters_as("json-schema") or {}

  # Build a Pydantic model for the tool parameters
  properties = schema.get("properties", {})
  required = set(schema.get("required", []))

  fields: dict[str, Any] = {}
  for prop_name, prop_schema in properties.items():
    prop_type = _json_type_to_python(prop_schema.get("type", "string"))
    description = prop_schema.get("description", "")

    if prop_name in required:
      fields[prop_name] = (prop_type, Field(description=description))
    else:
      fields[prop_name] = (
        prop_type | None,
        Field(default=None, description=description),
      )

  # Create the parameter model
  ParamModel = create_model(f"{tool_name}Params", **fields) if fields else None

  # Create a wrapper class to hold the tool function with proper closure
  def make_tool_fn(name: str, param_model: Any, mgr: Any):
    if param_model:

      async def tool_fn(**kwargs: Any) -> str:
        # Filter out None values
        filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        result = await mgr.execute_tool(name, filtered_kwargs)
        if hasattr(result, "model_dump"):
          result = result.model_dump()
        return json.dumps(result, ensure_ascii=False, default=str)

      # Set annotations for PydanticAI to discover parameters
      tool_fn.__annotations__ = {
        k: v[0]
        for k, v in fields.items()  # Get the type from (type, Field) tuple
      }
      tool_fn.__annotations__["return"] = str

    else:

      async def tool_fn() -> str:
        result = await mgr.execute_tool(name, {})
        if hasattr(result, "model_dump"):
          result = result.model_dump()
        return json.dumps(result, ensure_ascii=False, default=str)

    tool_fn.__name__ = name
    tool_fn.__doc__ = tool_description
    return tool_fn

  fn = make_tool_fn(tool_name, ParamModel, tool_manager)

  # Create PydanticAI Tool
  return Tool(fn, name=tool_name, description=tool_description)


def _json_type_to_python(json_type: str) -> type:
  """Convert JSON schema type to Python type."""
  type_map: dict[str, type] = {
    "string": str,
    "integer": int,
    "number": float,
    "boolean": bool,
    "array": list,
    "object": dict,
  }
  return type_map.get(json_type, str)


__all__ = ["create_pydantic_ai_tools"]
