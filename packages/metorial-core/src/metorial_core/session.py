"""
Metorial session manager with error handling and fallback mechanisms.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
  from metorial_mcp_session import MetorialMcpSession
else:
  MetorialMcpSession = Any

from .tool_manager import ToolManager as ToolManagerWrapper
from .tool_adapters import ToolStatistics

logger = logging.getLogger(__name__)


class MetorialSession:
  """Metorial session with automatic error handling and fallbacks."""

  def __init__(self, mcp_session: MetorialMcpSession):
    """Initialize with an MCP session."""
    self._mcp_session = mcp_session
    self._tool_manager: Optional[ToolManagerWrapper] = None
    self._fallback_mode = False

  async def get_tool_manager(
    self, timeout: float = 30.0, enable_fallback: bool = True
  ) -> Optional[ToolManagerWrapper]:
    """Get tool manager with timeout and automatic fallback."""
    if self._tool_manager is not None:
      return self._tool_manager

    try:
      self._tool_manager = ToolManagerWrapper(
        await asyncio.wait_for(self._mcp_session.get_tool_manager(), timeout=timeout)
      )
      self._fallback_mode = False
      return self._tool_manager

    except asyncio.TimeoutError:
      logger.debug("⏰ Timeout getting tool manager, using fallback")
      if enable_fallback:
        return self._create_fallback_tool_manager()
      else:
        raise RuntimeError("Tool manager timeout and fallback disabled")

    except Exception as e:
      logger.debug(f"❌ Error getting tool manager: {e}")
      if enable_fallback:
        return self._create_fallback_tool_manager()
      else:
        raise

  def _create_fallback_tool_manager(self) -> Optional[ToolManagerWrapper]:
    """Create a fallback tool manager when real tools are unavailable."""
    logger.debug("🔄 No fallback tool manager available")
    self._fallback_mode = True
    return None

  async def execute_tools(self, tool_calls: List[Any]) -> List[Dict[str, Any]]:
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

  async def call_tools(self, tool_calls: List[Any]) -> List[Dict[str, Any]]:
    """Alias for execute_tools for backward compatibility."""
    return await self.execute_tools(tool_calls)

  def is_fallback_mode(self) -> bool:
    """Check if the session is running in fallback mode."""
    return self._fallback_mode

  def get_tool_statistics(self) -> Optional[ToolStatistics]:
    """Get tool statistics if available."""
    if self._tool_manager is not None:
      return self._tool_manager.get_tool_statistics()
    return None

  # Delegate other methods to the MCP session
  def __getattr__(self, name):
    """Delegate unknown attributes to the MCP session."""
    return getattr(self._mcp_session, name)

  async def close(self):
    """Close the session and clean up resources gracefully."""
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
  def create_session(mcp_session) -> MetorialSession:
    """Create a session from an MCP session."""
    return MetorialSession(mcp_session)
