"""
OpenAI Agents SDK integration for Metorial tools.

Example:
    from agents import Agent, Runner
    from metorial import Metorial
    from metorial.integrations.openai_agents import create_openai_agent_tools

    metorial = Metorial(api_key="...")

    async with metorial.provider_session(
        provider="openai",
        server_deployments=["deployment-id"],
    ) as session:
        tools = create_openai_agent_tools(session)

        agent = Agent(
            name="Assistant",
            instructions="You are a helpful assistant.",
            tools=tools,
        )

        result = await Runner.run(agent, "Search for news")
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from agents import FunctionTool
except ImportError:
  FunctionTool = None


def create_openai_agent_tools(session: ProviderSession) -> list[Any]:
  """Convert Metorial session tools to OpenAI Agents SDK tools.

  Args:
      session: Active Metorial ProviderSession

  Returns:
      List of OpenAI Agents SDK tool objects

  Raises:
      ImportError: If openai-agents is not installed
  """
  if FunctionTool is None:
    raise ImportError(
      "openai-agents is required for OpenAI Agents SDK integration. "
      "Install it with: pip install openai-agents"
    )

  tools = []
  tool_manager = session.tool_manager

  if tool_manager is None:
    return tools

  for tool in tool_manager.get_tools():
    openai_tool = _create_openai_agent_tool(tool, tool_manager)
    tools.append(openai_tool)

  return tools


def _create_openai_agent_tool(tool: Any, tool_manager: Any) -> Any:
  """Create an OpenAI Agents SDK FunctionTool from a Metorial tool."""
  tool_name = tool.name
  tool_description = tool.description or f"Tool: {tool_name}"
  schema = tool.get_parameters_as("json-schema") or {}

  # Build the parameters schema for OpenAI Agents
  properties = schema.get("properties", {})
  required = schema.get("required", [])

  # Create a clean parameters schema without additionalProperties
  params_schema = {
    "type": "object",
    "properties": properties,
    "required": required,
  }

  # Create the async function that will execute the tool
  async def tool_fn(**kwargs: Any) -> str:
    # Filter out None values
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    result = await tool_manager.execute_tool(tool_name, filtered_kwargs)
    if hasattr(result, "model_dump"):
      result = result.model_dump()
    return json.dumps(result, ensure_ascii=False, default=str)

  tool_fn.__name__ = tool_name
  tool_fn.__doc__ = tool_description

  # Create FunctionTool with explicit schema (bypass function introspection)
  return FunctionTool(
    name=tool_name,
    description=tool_description,
    params_json_schema=params_schema,
    on_invoke_tool=_make_invoke_handler(tool_name, tool_manager),
  )


def _make_invoke_handler(tool_name: str, tool_manager: Any):
  """Create an invoke handler for the FunctionTool."""

  async def invoke_handler(ctx: Any, input_json: str) -> str:
    kwargs = json.loads(input_json) if input_json else {}
    # Filter out None values
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    result = await tool_manager.execute_tool(tool_name, filtered_kwargs)
    if hasattr(result, "model_dump"):
      result = result.model_dump()
    return json.dumps(result, ensure_ascii=False, default=str)

  return invoke_handler


__all__ = ["create_openai_agent_tools"]
