"""
Tests for ToolManager functionality.
"""

from unittest.mock import AsyncMock

import pytest

from metorial._tool_manager import ToolManager


class TestToolManagerGetTools:
  """Tests for ToolManager.get_tools"""

  def test_get_tools_returns_list(self, mock_tool_manager):
    """get_tools should return a list."""
    mock_tool_manager.get_tools.return_value = []
    manager = ToolManager(mock_tool_manager)

    result = manager.get_tools()

    assert isinstance(result, list)
    mock_tool_manager.get_tools.assert_called_once()

  def test_get_tools_delegates_to_mcp_manager(self, mock_tool_manager, mock_mcp_tool):
    """get_tools should delegate to MCP manager."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    result = manager.get_tools()

    assert len(result) == 1
    assert result[0].name == "test_tool"


class TestToolManagerGetToolsForOpenAI:
  """Tests for ToolManager.get_tools_for_openai"""

  def test_get_tools_for_openai_returns_list(self, mock_tool_manager, mock_mcp_tool):
    """get_tools_for_openai should return OpenAI-formatted tools."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    result = manager.get_tools_for_openai()

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["type"] == "function"
    assert result[0]["function"]["name"] == "test_tool"

  def test_get_tools_for_openai_caching(self, mock_tool_manager, mock_mcp_tool):
    """get_tools_for_openai should cache results."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    # First call
    result1 = manager.get_tools_for_openai()
    # Second call should use cache
    result2 = manager.get_tools_for_openai()

    assert result1 == result2
    # Should only call get_tools once due to caching
    assert mock_tool_manager.get_tools.call_count == 1

  def test_get_tools_for_openai_force_refresh(self, mock_tool_manager, mock_mcp_tool):
    """force_refresh should bypass cache."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    # First call
    manager.get_tools_for_openai()
    # Force refresh
    manager.get_tools_for_openai(force_refresh=True)

    # Should call get_tools twice
    assert mock_tool_manager.get_tools.call_count == 2


class TestToolManagerCacheInvalidation:
  """Tests for cache invalidation"""

  def test_refresh_cache(self, mock_tool_manager, mock_mcp_tool):
    """refresh_cache should clear the cache."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    # Populate cache
    manager.get_tools_for_openai()
    assert mock_tool_manager.get_tools.call_count == 1

    # Refresh cache
    manager.refresh_cache()

    # Next call should fetch again
    manager.get_tools_for_openai()
    assert mock_tool_manager.get_tools.call_count == 2

  def test_get_cache_info(self, mock_tool_manager, mock_mcp_tool):
    """get_cache_info should return cache state."""
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    # Before caching
    info = manager.get_cache_info()
    assert info["cached"] is False

    # After caching
    manager.get_tools_for_openai()
    info = manager.get_cache_info()
    assert info["cached"] is True
    assert info["cache_age_seconds"] is not None


class TestToolManagerExecuteTool:
  """Tests for ToolManager.execute_tool"""

  @pytest.mark.asyncio
  async def test_execute_tool_success(self, mock_tool_manager):
    """execute_tool should execute tool and return result."""
    mock_tool_manager.call_tool = AsyncMock(return_value={"content": "test result"})
    manager = ToolManager(mock_tool_manager)

    result = await manager.execute_tool("test_tool", {"param1": "value1"})

    assert result["content"] == "test result"
    mock_tool_manager.call_tool.assert_called_once_with(
      "test_tool", {"param1": "value1"}
    )

  @pytest.mark.asyncio
  async def test_execute_tool_json_arguments(self, mock_tool_manager):
    """execute_tool should parse JSON string arguments."""
    mock_tool_manager.call_tool = AsyncMock(return_value={"content": "test result"})
    manager = ToolManager(mock_tool_manager)

    result = await manager.execute_tool("test_tool", '{"param1": "value1"}')

    assert result["content"] == "test result"
    mock_tool_manager.call_tool.assert_called_once_with(
      "test_tool", {"param1": "value1"}
    )

  @pytest.mark.asyncio
  async def test_execute_tool_invalid_json(self, mock_tool_manager):
    """execute_tool should raise ValueError for invalid JSON."""
    manager = ToolManager(mock_tool_manager)

    with pytest.raises(ValueError, match="Invalid JSON"):
      await manager.execute_tool("test_tool", "not valid json")

  @pytest.mark.asyncio
  async def test_execute_tool_not_found(self, mock_tool_manager, mock_mcp_tool):
    """execute_tool should raise ValueError when tool not found."""
    mock_tool_manager.call_tool = AsyncMock(side_effect=Exception("Tool not found"))
    mock_tool_manager.get_tools.return_value = [mock_mcp_tool]
    manager = ToolManager(mock_tool_manager)

    with pytest.raises(ValueError, match="not found"):
      await manager.execute_tool("nonexistent_tool", {})


class TestToolManagerGetTool:
  """Tests for ToolManager.get_tool"""

  def test_get_tool_delegates(self, mock_tool_manager, mock_mcp_tool):
    """get_tool should delegate to MCP manager."""
    mock_tool_manager.get_tool.return_value = mock_mcp_tool
    manager = ToolManager(mock_tool_manager)

    result = manager.get_tool("test_tool")

    assert result == mock_mcp_tool
    mock_tool_manager.get_tool.assert_called_once_with("test_tool")

  def test_get_tool_not_found(self, mock_tool_manager):
    """get_tool should return None for unknown tools."""
    mock_tool_manager.get_tool.return_value = None
    manager = ToolManager(mock_tool_manager)

    result = manager.get_tool("unknown_tool")

    assert result is None
