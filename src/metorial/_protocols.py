"""Protocol definitions for type checking."""

from __future__ import annotations

from collections.abc import Awaitable, Coroutine
from typing import TYPE_CHECKING, Any, Protocol, runtime_checkable

if TYPE_CHECKING:
  from metorial.mcp.mcp_tool import MetorialMcpTool


class ToolLike(Protocol):
  """Protocol for tool-like objects that have name, description, and parameters."""

  @property
  def name(self) -> str: ...

  @property
  def description(self) -> str | None: ...

  def get_parameters_as(self, format: str) -> dict[str, Any]: ...


@runtime_checkable
class McpToolManagerProtocol(Protocol):
  """Protocol for MCP tool managers that provide tool access."""

  def get_tools(self) -> list[MetorialMcpTool]:
    """Get all available tools."""
    ...

  def get_tool(self, tool_id_or_name: str) -> MetorialMcpTool | None:
    """Get a specific tool by ID or name."""
    ...

  def call_tool(self, tool_name: str, args: dict[str, Any]) -> Coroutine[Any, Any, Any]:
    """Call a tool with the given arguments."""
    ...


@runtime_checkable
class ToolManagerProtocol(Protocol):
  """Protocol for wrapped tool managers with execute_tool and get_tools support."""

  def get_tools(self) -> list[ToolLike]:
    """Get all available tools."""
    ...

  async def execute_tool(self, tool_name: str, arguments: str | dict[str, Any]) -> Any:
    """Execute a tool with automatic argument parsing."""
    ...


@runtime_checkable
class SessionWithToolManagerProtocol(Protocol):
  """Protocol for sessions that provide tool manager access."""

  def get_tool_manager(self) -> Awaitable[ToolManagerProtocol]:
    """Get the tool manager for this session."""
    ...


@runtime_checkable
class MetorialSessionProtocol(Protocol):
  """Protocol for Metorial sessions with common operations."""

  def get_tools(self) -> list[Any]:
    """Get all available tools."""
    ...

  def get_tool(self, tool_id_or_name: str) -> Any | None:
    """Get a specific tool by ID or name."""
    ...

  def call_tool(self, tool_name: str, args: dict[str, Any]) -> Awaitable[Any]:
    """Call a tool with the given arguments."""
    ...

  def close(self) -> Awaitable[None]:
    """Close the session."""
    ...


@runtime_checkable
class FilteredToolManagerProtocol(Protocol):
  """Protocol for filtered tool managers."""

  def get_tools(self) -> list[Any]:
    """Get all available (filtered) tools."""
    ...

  def get_tool(self, tool_id_or_name: str) -> Any | None:
    """Get a specific tool by ID or name."""
    ...

  def call_tool(self, tool_name: str, args: dict[str, Any]) -> Awaitable[Any]:
    """Call a tool with the given arguments."""
    ...


class EmptyToolManager:
  """Empty tool manager for fallback mode when tools are unavailable."""

  def get_tools(self) -> list[Any]:
    """Return empty list of tools."""
    return []

  def get_tool(self, tool_id_or_name: str) -> None:
    """Always returns None - no tools available."""
    return None

  async def call_tool(self, tool_name: str, args: dict[str, Any]) -> Any:
    """Raise error - no tools available in fallback mode."""
    raise RuntimeError(f"No tools available (fallback mode). Cannot call '{tool_name}'")
