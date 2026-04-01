"""Google ADK integration for Metorial tools."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

from metorial.integrations import _sanitize_tool_name
from metorial.integrations._common import (
  apply_tool_signature,
  normalize_tool_result,
)

if TYPE_CHECKING:
  from metorial._client import ProviderSession


def create_google_adk_tools(session: ProviderSession) -> list[Any]:
  """Convert Metorial session tools to Google ADK-compatible async functions."""
  tool_manager = session.tool_manager
  if tool_manager is None:
    return []

  tools: list[Any] = []
  for tool in tool_manager.get_tools():
    tools.append(_create_google_adk_tool(tool, tool_manager))
  return tools


def _create_google_adk_tool(tool: Any, tool_manager: Any) -> Any:
  original_name = tool.name
  tool_name = _sanitize_tool_name(original_name)
  tool_description = tool.description or f"Tool: {tool_name}"
  schema = tool.get_parameters_as("json-schema") or {}
  required = set(schema.get("required", []))
  required_only_schema = {
    "type": "object",
    "properties": {
      name: prop_schema
      for name, prop_schema in schema.get("properties", {}).items()
      if name in required
    },
    "required": list(required),
  }

  async def tool_fn(**kwargs: Any) -> dict[str, Any]:
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    try:
      result = await tool_manager.execute_tool(original_name, filtered_kwargs)
    except Exception as e:
      return {"error": str(e)}

    normalized = normalize_tool_result(result)
    if isinstance(normalized, dict):
      return normalized
    if isinstance(normalized, list):
      return {"result": normalized}
    return {"result": json.loads(json.dumps(normalized, default=str))}

  apply_tool_signature(
    tool_fn,
    name=tool_name,
    description=tool_description,
    schema=required_only_schema,
    return_annotation=dict[str, Any],
    use_optional_union=False,
  )
  return tool_fn


__all__ = ["create_google_adk_tools"]
