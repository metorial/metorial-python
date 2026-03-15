from __future__ import annotations

import logging
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._protocols import McpSessionProtocol

from .mcp_tool import Capability, MetorialMcpTool

logger = logging.getLogger(__name__)


class MetorialMcpToolManager:
  def __init__(
    self, session: McpSessionProtocol, tools: Iterable[MetorialMcpTool]
  ) -> None:
    self._session = session
    self._tools_by_key: dict[str, MetorialMcpTool] = {}

    for tool in tools:
      if tool.name in self._tools_by_key:
        logger.warning(
          f"Duplicate tool name: '{tool.name}'. "
          "The API should return unique tool names — this may indicate a bug."
        )
      if tool.id in self._tools_by_key:
        logger.warning(
          f"Duplicate tool ID: '{tool.id}' (from tool '{tool.name}'). "
          "The API should return unique tool names — this may indicate a bug."
        )

      self._tools_by_key[tool.id] = tool
      self._tools_by_key[tool.name] = tool

  @classmethod
  async def from_capabilities(
    cls,
    session: McpSessionProtocol,
    capabilities: list[Capability],
  ) -> MetorialMcpToolManager:
    tools = []
    for i, cap in enumerate(capabilities):
      try:
        tool = MetorialMcpTool.from_capability(session, cap)
        tools.append(tool)
      except Exception as e:
        logger.error(f"Failed to create tool from capability {i}: {e}")
        continue
    return cls(session, tools)

  def get_tool(self, id_or_name: str) -> MetorialMcpTool | None:
    return self._tools_by_key.get(id_or_name)

  def get_tools(self) -> list[MetorialMcpTool]:
    # unique instances (id and name point to same object)
    seen = set()
    out: list[MetorialMcpTool] = []
    for tool in self._tools_by_key.values():
      if id(tool) not in seen:
        seen.add(id(tool))
        out.append(tool)
    return out

  async def call_tool(self, id_or_name: str, args: Any) -> Any:
    tool = self.get_tool(id_or_name)
    if tool is None:
      raise KeyError(f"Tool not found: {id_or_name}")

    logger.debug(f"MCP Tool Manager: Calling tool '{id_or_name}' with args: {args}")
    call_result = tool.call(args)
    logger.debug(
      f"MCP Tool Manager: tool.call() returned: {call_result} (type: {type(call_result)})"
    )

    result = await call_result
    logger.debug(f"MCP Tool Manager: Tool execution completed: {result}")

    return result
