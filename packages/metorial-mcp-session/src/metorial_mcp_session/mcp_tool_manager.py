from __future__ import annotations

import logging
from typing import Dict, List, Optional, Iterable, Any, TYPE_CHECKING

if TYPE_CHECKING:
  from .mcp_session import MetorialMcpSession

from .mcp_tool import MetorialMcpTool, Capability

logger = logging.getLogger(__name__)


class MetorialMcpToolManager:
  def __init__(
    self, session: MetorialMcpSession, tools: Iterable[MetorialMcpTool]
  ) -> None:
    self._session = session
    self._tools_by_key: Dict[str, MetorialMcpTool] = {}
    seen_names = set()
    seen_ids = set()
    duplicate_warnings = []

    for tool in tools:
      # Check for duplicate names
      if tool.name in seen_names:
        duplicate_warnings.append(
          f"Duplicate tool name: '{tool.name}' (last-wins behavior)"
        )
      else:
        seen_names.add(tool.name)

      # Check for duplicate IDs
      if tool.id in seen_ids:
        duplicate_warnings.append(
          f"Duplicate tool ID: '{tool.id}' (last-wins behavior)"
        )
      else:
        seen_ids.add(tool.id)

      # Prefer last-wins if duplicates collide
      self._tools_by_key[tool.id] = tool
      self._tools_by_key[tool.name] = tool

    # Log warnings for duplicates
    for warning in duplicate_warnings:
      logger.warning(f"⚠️ {warning}")

    if duplicate_warnings:
      logger.warning(
        f"⚠️ Found {len(duplicate_warnings)} duplicate tool(s). Using last-wins behavior."
      )

  @classmethod
  async def from_capabilities(
    cls,
    session: MetorialMcpSession,
    capabilities: List[Capability],
  ) -> "MetorialMcpToolManager":
    tools = [MetorialMcpTool.from_capability(session, cap) for cap in capabilities]
    return cls(session, tools)

  def get_tool(self, id_or_name: str) -> Optional[MetorialMcpTool]:
    return self._tools_by_key.get(id_or_name)

  def get_tools(self) -> List[MetorialMcpTool]:
    # unique instances (id and name point to same object)
    seen = set()
    out: List[MetorialMcpTool] = []
    for tool in self._tools_by_key.values():
      if id(tool) not in seen:
        seen.add(id(tool))
        out.append(tool)
    return out

  def get_duplicate_info(self) -> Dict[str, List[str]]:
    """Get information about duplicate tool names and IDs."""
    name_counts: dict[str, int] = {}
    id_counts: dict[str, int] = {}

    for tool in self._tools_by_key.values():
      name_counts[tool.name] = name_counts.get(tool.name, 0) + 1
      id_counts[tool.id] = id_counts.get(tool.id, 0) + 1

    duplicates = {
      "duplicate_names": [name for name, count in name_counts.items() if count > 1],
      "duplicate_ids": [tool_id for tool_id, count in id_counts.items() if count > 1],
    }

    return duplicates

  async def call_tool(self, id_or_name: str, args: Any) -> Any:
    tool = self.get_tool(id_or_name)
    if tool is None:
      raise KeyError(f"Tool not found: {id_or_name}")

    logger.debug(f"🔧 MCP Tool Manager: Calling tool '{id_or_name}' with args: {args}")
    call_result = tool.call(args)
    logger.debug(
      f"🔧 MCP Tool Manager: tool.call() returned: {call_result} (type: {type(call_result)})"
    )

    result = await call_result
    logger.debug(f"🔧 MCP Tool Manager: Tool execution completed: {result}")

    return result
