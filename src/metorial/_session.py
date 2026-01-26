"""
Metorial session manager with error handling and fallback mechanisms.
"""

from __future__ import annotations

import asyncio
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial.mcp import MetorialMcpSession
else:
  MetorialMcpSession = Any

from metorial._tool_adapters import ToolStatistics
from metorial._tool_manager import ToolManager as ToolManagerWrapper
from metorial.exceptions import AuthenticationError, NotFoundError, OAuthRequiredError

logger = logging.getLogger(__name__)


class MetorialSession:
  """Metorial session with automatic error handling and fallbacks.

  This class implements the async context manager protocol for proper
  resource management:

      async with session as s:
          tools = await s.get_tool_manager()
          # ... use session
      # Session is automatically closed
  """

  def __init__(self, mcp_session: MetorialMcpSession):
    """Initialize with an MCP session."""
    self._mcp_session = mcp_session
    self._tool_manager: ToolManagerWrapper | None = None
    self._fallback_mode = False
    self._closed = False

  async def __aenter__(self) -> MetorialSession:
    """Async context manager entry."""
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: TracebackType | None,
  ) -> None:
    """Async context manager exit - ensures cleanup."""
    await self.close()

  async def get_tool_manager(
    self, timeout: float = 30.0, enable_fallback: bool = False
  ) -> ToolManagerWrapper:
    """Get tool manager with timeout.

    Args:
        timeout: Maximum time to wait for tool manager initialization
        enable_fallback: If True, return empty tool manager on failure instead of raising

    Returns:
        ToolManager instance for accessing and executing tools

    Raises:
        RuntimeError: If tool manager cannot be initialized and enable_fallback is False
    """
    if self._tool_manager is not None:
      return self._tool_manager

    try:
      self._tool_manager = ToolManagerWrapper(
        await asyncio.wait_for(self._mcp_session.get_tool_manager(), timeout=timeout)
      )
      self._fallback_mode = False
      return self._tool_manager

    except asyncio.TimeoutError as e:
      logger.debug("⏰ Timeout getting tool manager")
      if enable_fallback:
        return self._create_fallback_tool_manager()
      raise RuntimeError(
        f"Tool manager initialization timed out after {timeout}s"
      ) from e

    except (AuthenticationError, NotFoundError, OAuthRequiredError):
      # Re-raise critical errors without wrapping
      logger.debug("❌ Critical error getting tool manager")
      raise

    except Exception as e:
      logger.debug(f"❌ Error getting tool manager: {e}")
      if enable_fallback:
        return self._create_fallback_tool_manager()
      raise RuntimeError(f"Failed to get tool manager: {e}") from e

  def _create_fallback_tool_manager(self) -> ToolManagerWrapper:
    """Create a fallback empty tool manager."""
    self._fallback_mode = True
    logger.warning(
      "Tool manager unavailable - creating fallback with NO tools. "
      "Tool calls will fail. Check MCP session connectivity."
    )
    from metorial._protocols import EmptyToolManager

    return ToolManagerWrapper(EmptyToolManager())

  async def execute_tools(self, tool_calls: list[Any]) -> list[dict[str, Any]]:
    """Execute tools with automatic fallback handling."""
    if self._tool_manager is None:
      # Try to get tool manager first
      tool_manager = await self.get_tool_manager()
      if tool_manager is None:
        raise RuntimeError("No tool manager available and fallback disabled")

    # Execute tools using the available tool manager
    if self._tool_manager is None:
      raise RuntimeError("No tool manager available")
    return await self._tool_manager.execute_tools(tool_calls)

  async def call_tools(self, tool_calls: list[Any]) -> list[dict[str, Any]]:
    """Alias for execute_tools for backward compatibility."""
    return await self.execute_tools(tool_calls)

  def is_fallback_mode(self) -> bool:
    """Check if the session is running in fallback mode."""
    return self._fallback_mode

  def get_tool_statistics(self) -> ToolStatistics | None:
    """Get tool statistics if available."""
    if self._tool_manager is not None:
      return self._tool_manager.get_tool_statistics()
    return None

  # Delegate other methods to the MCP session
  def __getattr__(self, name: str) -> Any:
    """Delegate unknown attributes to the MCP session."""
    return getattr(self._mcp_session, name)

  @property
  def is_closed(self) -> bool:
    """Check if the session has been closed."""
    return self._closed

  async def close(self) -> None:
    """Close the session and clean up resources gracefully.

    This method is idempotent - calling it multiple times is safe.
    """
    if self._closed:
      return

    self._closed = True

    if self._tool_manager is not None:
      self._tool_manager.refresh_cache()

    if hasattr(self._mcp_session, "close"):
      try:
        # Close with timeout to prevent hanging
        close_result = self._mcp_session.close()
        if asyncio.iscoroutine(close_result):
          await asyncio.wait_for(close_result, timeout=3.0)
        # If it's not a coroutine, it might be a dictionary or other value, just ignore it
      except asyncio.TimeoutError:
        # Timeout is acceptable during cleanup
        logger.debug("MCP session close timeout - continuing")
      except Exception as e:
        # Log the error but don't raise it to avoid breaking the session cleanup
        logger.debug(f"Warning: Error closing MCP session: {e}")


class SessionFactory:
  """Factory for creating sessions."""

  @staticmethod
  def create_session(mcp_session: MetorialMcpSession) -> MetorialSession:
    """Create a session from an MCP session."""
    return MetorialSession(mcp_session)
