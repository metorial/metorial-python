"""CrewAI integration for Metorial tools."""

from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING, Any

from metorial.integrations import _sanitize_tool_name
from metorial.integrations._common import (
  apply_tool_signature,
  run_coro_on_loop,
  serialize_tool_result,
)

if TYPE_CHECKING:
  from metorial._client import ProviderSession

try:
  from crewai.tools import tool as crewai_tool
except ImportError:
  crewai_tool = None


def create_crewai_tools(session: ProviderSession) -> list[Any]:
  """Convert Metorial session tools to CrewAI BaseTool instances."""
  if crewai_tool is None:
    raise ImportError(
      "CrewAI is required for this integration. Install it with: pip install crewai"
    )

  tool_manager = session.tool_manager
  if tool_manager is None:
    return []

  owner_loop = asyncio.get_running_loop()
  tools: list[Any] = []
  for tool in tool_manager.get_tools():
    tools.append(_create_crewai_tool(tool, tool_manager, owner_loop))
  return tools


def _create_crewai_tool(
  tool: Any,
  tool_manager: Any,
  owner_loop: asyncio.AbstractEventLoop,
) -> Any:
  original_name = tool.name
  tool_name = _sanitize_tool_name(original_name)
  tool_description = tool.description or f"Tool: {tool_name}"
  schema = tool.get_parameters_as("json-schema") or {}

  async def execute_tool(**kwargs: Any) -> str:
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    try:
      result = await tool_manager.execute_tool(original_name, filtered_kwargs)
    except Exception as e:
      return json.dumps({"error": str(e)}, ensure_ascii=False)
    return serialize_tool_result(result)

  def sync_execute_tool(**kwargs: Any) -> str:
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    return run_coro_on_loop(
      owner_loop,
      lambda: execute_tool(**filtered_kwargs),
    )

  apply_tool_signature(
    sync_execute_tool,
    name=tool_name,
    description=tool_description,
    schema=schema,
    return_annotation=str,
  )
  return crewai_tool(tool_name)(sync_execute_tool)


__all__ = ["create_crewai_tools"]
