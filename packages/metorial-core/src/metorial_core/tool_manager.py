"""
Tool manager that provides OpenAI-compatible tool access.
"""

import json
import asyncio
import logging
from typing import Dict, Any, List, Optional, Union, TypedDict
from .tool_adapters import ToolSanitizer, ToolStatistics, OpenAITool


class CacheInfo(TypedDict):
  """Information about the current cache state."""

  cached: bool
  cache_age_seconds: Optional[float]
  cache_ttl_seconds: int
  cache_valid: bool


logger = logging.getLogger(__name__)


class ToolManager:
  """Tool manager with OpenAI compatibility and automatic sanitization."""

  def __init__(self, mcp_tool_manager):
    """Initialize with an MCP tool manager."""
    self._mcp_manager = mcp_tool_manager
    self._openai_tools_cache: Optional[List[OpenAITool]] = None
    self._cache_timestamp = 0.0
    self._cache_ttl = 60  # Cache TTL in seconds

  def get_tools(self) -> List[Any]:
    """Get raw Metorial tools."""
    result = self._mcp_manager.get_tools()
    return result  # type: ignore[no-any-return]

  def get_tools_for_openai(self, force_refresh: bool = False) -> List[OpenAITool]:
    """Get tools in OpenAI-compatible format with automatic sanitization."""
    current_time = asyncio.get_event_loop().time()

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
    self, tool_name: str, arguments: Union[str, Dict[str, Any]]
  ) -> Any:
    """Execute a tool with automatic argument parsing and error handling."""

    try:
      # Parse arguments if they're a JSON string
      if isinstance(arguments, str):
        try:
          args = json.loads(arguments)
        except json.JSONDecodeError as e:
          raise ValueError(f"Invalid JSON arguments: {e}")
      else:
        args = arguments

      logger.debug(f"🔧 Calling tool '{tool_name}' with args: {args}")
      call_result = self._mcp_manager.call_tool(tool_name, args)
      logger.debug(f"🔧 Tool call returned: {call_result} (type: {type(call_result)})")
      if asyncio.iscoroutine(call_result):
        result = await call_result
        logger.debug(f"🔧 Tool execution completed: {result}")
      else:
        logger.debug(
          f"🔧 Tool call returned non-awaitable result, using directly: {call_result}"
        )
        result = call_result
      return result

    except Exception as e:
      if "not found" in str(e).lower():
        available_tools = [tool.name for tool in self._mcp_manager.get_tools()]
        raise ValueError(
          f"Tool '{tool_name}' not found. Available tools: {available_tools}"
        )
      else:
        raise RuntimeError(f"Tool execution failed: {e}")

  async def execute_tools(self, tool_calls: List[Any]) -> List[Dict[str, Any]]:
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

  def get_tool(self, tool_id_or_name: str) -> Optional[Any]:
    """Get a specific tool by ID or name."""
    return self._mcp_manager.get_tool(tool_id_or_name)

  def refresh_cache(self):
    """Force refresh of the OpenAI tools cache."""
    if self._openai_tools_cache is not None:
      logger.warning("⚠️ Manually refreshing OpenAI tools cache")
      self._openai_tools_cache = None
      self._cache_timestamp = 0

  def get_cache_info(self) -> CacheInfo:
    """Get information about the current cache state."""
    current_time = asyncio.get_event_loop().time()
    cache_age = (
      current_time - self._cache_timestamp if self._cache_timestamp > 0 else None
    )

    return CacheInfo(
      cached=self._openai_tools_cache is not None,
      cache_age_seconds=cache_age,
      cache_ttl_seconds=self._cache_ttl,
      cache_valid=cache_age is not None and cache_age < self._cache_ttl,
    )
