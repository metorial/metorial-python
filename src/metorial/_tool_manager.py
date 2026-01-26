"""
Tool manager that provides OpenAI-compatible tool access.
"""

from __future__ import annotations

import json
import logging
import time
from typing import TYPE_CHECKING, Any, TypedDict

from metorial._tool_adapters import (
  OpenAITool,
  ToolResult,
  ToolSanitizer,
  ToolStatistics,
)

if TYPE_CHECKING:
  from metorial._protocols import McpToolManagerProtocol


class CacheInfo(TypedDict):
  """Information about the current cache state."""

  cached: bool
  cache_age_seconds: float | None
  cache_ttl_seconds: int
  cache_valid: bool


logger = logging.getLogger(__name__)


class ToolManager:
  """Tool manager with OpenAI compatibility and automatic sanitization."""

  def __init__(self, mcp_tool_manager: McpToolManagerProtocol) -> None:
    """Initialize with an MCP tool manager."""
    self._mcp_manager: McpToolManagerProtocol = mcp_tool_manager
    self._openai_tools_cache: list[OpenAITool] | None = None
    self._cache_timestamp = 0.0
    self._cache_ttl = 60  # Cache TTL in seconds

  def get_tools(self) -> list[Any]:
    """Get raw Metorial tools."""
    result = self._mcp_manager.get_tools()
    return result

  def get_tools_for_openai(self, force_refresh: bool = False) -> list[OpenAITool]:
    """Get tools in OpenAI-compatible format with automatic sanitization."""
    current_time = time.monotonic()

    # Check cache
    if (
      not force_refresh
      and self._openai_tools_cache is not None
      and current_time - self._cache_timestamp < self._cache_ttl
    ):
      return self._openai_tools_cache

    # Cache invalidation warning
    if self._openai_tools_cache is not None:
      cache_age = current_time - self._cache_timestamp
      if force_refresh:
        logger.debug("🔄 Cache force refresh requested")
      else:
        logger.warning(
          f"⚠️ Cache invalidated (age: {cache_age:.1f}s > TTL: {self._cache_ttl}s)"
        )

    # Get raw tools and convert them
    raw_tools = self._mcp_manager.get_tools()
    openai_tools = ToolSanitizer.sanitize_tools(raw_tools)

    # Cache the result
    self._openai_tools_cache = openai_tools
    self._cache_timestamp = current_time

    logger.debug(f"📦 Cached {len(openai_tools)} OpenAI-compatible tools")

    return openai_tools

  async def execute_tool(
    self, tool_name: str, arguments: str | dict[str, Any]
  ) -> ToolResult:
    """Execute a tool with automatic argument parsing and error handling.

    Args:
        tool_name: Name of the tool to execute
        arguments: Tool arguments as JSON string or dict

    Returns:
        ToolResult with 'content' key containing the result

    Raises:
        ValueError: If tool not found or invalid arguments
        RuntimeError: If tool execution fails
    """

    # Parse arguments if they're a JSON string
    if isinstance(arguments, str):
      try:
        args = json.loads(arguments)
      except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON arguments: {e}") from e
    else:
      args = arguments

    try:
      logger.debug(f"🔧 Calling tool '{tool_name}' with args: {args}")
      result = await self._mcp_manager.call_tool(tool_name, args)
      logger.debug(f"🔧 Tool execution completed: {result}")

      # Ensure result is in ToolResult format
      if isinstance(result, dict) and "content" in result:
        return ToolResult(content=result["content"])
      return ToolResult(content=result)

    except Exception as e:
      if "not found" in str(e).lower():
        available_tools = [tool.name for tool in self._mcp_manager.get_tools()]
        raise ValueError(
          f"Tool '{tool_name}' not found. Available tools: {available_tools}"
        ) from e
      else:
        raise RuntimeError(f"Tool execution failed: {e}") from e

  async def execute_tools(self, tool_calls: list[Any]) -> list[dict[str, Any]]:
    """Execute multiple tools and return formatted responses."""
    responses: list[dict[str, Any]] = []

    for tool_call in tool_calls:
      try:
        tool_name = tool_call.function.name
        tool_args = tool_call.function.arguments
        tool_call_id = getattr(tool_call, "id", f"call_{len(responses)}")

        result = await self.execute_tool(tool_name, tool_args)

        response = {
          "role": "tool",
          "tool_call_id": tool_call_id,
          "content": str(result),
        }

        responses.append(response)

      except Exception as e:
        error_response = {
          "role": "tool",
          "tool_call_id": getattr(tool_call, "id", f"call_{len(responses)}"),
          "content": f"Tool execution failed: {str(e)}",
        }
        responses.append(error_response)

    return responses

  def get_tool_statistics(self) -> ToolStatistics:
    """Get statistics about the available tools."""
    raw_tools = self._mcp_manager.get_tools()
    return ToolSanitizer.get_tool_statistics(raw_tools)

  def get_tool(self, tool_id_or_name: str) -> Any | None:
    """Get a specific tool by ID or name."""
    return self._mcp_manager.get_tool(tool_id_or_name)

  def refresh_cache(self) -> None:
    """Force refresh of the OpenAI tools cache."""
    if self._openai_tools_cache is not None:
      logger.warning("⚠️ Manually refreshing OpenAI tools cache")
      self._openai_tools_cache = None
      self._cache_timestamp = 0

  def get_cache_info(self) -> CacheInfo:
    """Get information about the current cache state."""
    current_time = time.monotonic()
    cache_age = (
      current_time - self._cache_timestamp if self._cache_timestamp > 0 else None
    )

    return CacheInfo(
      cached=self._openai_tools_cache is not None,
      cache_age_seconds=cache_age,
      cache_ttl_seconds=self._cache_ttl,
      cache_valid=cache_age is not None and cache_age < self._cache_ttl,
    )
