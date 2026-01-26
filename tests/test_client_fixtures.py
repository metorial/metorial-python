"""
Tests for client fixture functionality and sync/async parametrization.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
  from metorial import Metorial, MetorialSync


# =============================================================================
# Client Type Parametrization Tests
# =============================================================================


class TestClientTypeFixture:
  """Tests for client_type parametrized fixture."""

  def test_client_type_is_sync_or_async(self, client_type: str) -> None:
    """client_type should be either 'sync' or 'async'."""
    assert client_type in ("sync", "async")


# =============================================================================
# Metorial Client Fixture Tests
# =============================================================================


class TestMetorialClientFixture:
  """Tests for metorial_client parametrized fixture."""

  def test_creates_sync_client(self, mock_metorial_config: dict[str, str]) -> None:
    """Should create sync client when client_type is 'sync'."""
    from metorial import MetorialSync

    client = MetorialSync(api_key=mock_metorial_config["apiKey"])
    assert isinstance(client, MetorialSync)

  def test_creates_async_client(self, mock_metorial_config: dict[str, str]) -> None:
    """Should create async client when client_type is 'async'."""
    from metorial import Metorial

    client = Metorial(api_key=mock_metorial_config["apiKey"])
    assert isinstance(client, Metorial)

  def test_client_has_api_key(self, metorial_client: Metorial | MetorialSync) -> None:
    """Client should have API key configured."""
    assert metorial_client._config_data["apiKey"] == "test-api-key"


# =============================================================================
# Async Metorial Client Fixture Tests
# =============================================================================


class TestAsyncMetorialClientFixture:
  """Tests for async_metorial_client fixture."""

  def test_creates_async_client(self, async_metorial_client: Metorial) -> None:
    """Should create an async Metorial client."""
    from metorial import Metorial

    assert isinstance(async_metorial_client, Metorial)

  def test_async_client_has_config(self, async_metorial_client: Metorial) -> None:
    """Async client should have proper configuration."""
    assert async_metorial_client._config_data["apiKey"] == "test-api-key"
    assert "apiHost" in async_metorial_client._config_data

  def test_async_client_has_provider_session(
    self, async_metorial_client: Metorial
  ) -> None:
    """Async client should have provider_session method."""
    assert hasattr(async_metorial_client, "provider_session")
    assert callable(async_metorial_client.provider_session)


# =============================================================================
# Sync Metorial Client Fixture Tests
# =============================================================================


class TestSyncMetorialClientFixture:
  """Tests for sync_metorial_client fixture."""

  def test_creates_sync_client(self, sync_metorial_client: MetorialSync) -> None:
    """Should create a sync MetorialSync client."""
    from metorial import MetorialSync

    assert isinstance(sync_metorial_client, MetorialSync)

  def test_sync_client_has_config(self, sync_metorial_client: MetorialSync) -> None:
    """Sync client should have proper configuration."""
    assert sync_metorial_client._config_data["apiKey"] == "test-api-key"
    assert "apiHost" in sync_metorial_client._config_data

  def test_sync_client_has_session_method(
    self, sync_metorial_client: MetorialSync
  ) -> None:
    """Sync client should have session method."""
    assert hasattr(sync_metorial_client, "session")
    assert callable(sync_metorial_client.session)


# =============================================================================
# Mock Configuration Fixture Tests
# =============================================================================


class TestMockMetorialConfigFixture:
  """Tests for mock_metorial_config fixture."""

  def test_has_required_keys(self, mock_metorial_config: dict[str, str]) -> None:
    """Config should have all required keys."""
    assert "apiKey" in mock_metorial_config
    assert "apiHost" in mock_metorial_config
    assert "mcpHost" in mock_metorial_config

  def test_has_valid_values(self, mock_metorial_config: dict[str, str]) -> None:
    """Config should have valid values."""
    assert mock_metorial_config["apiKey"] == "test-api-key"
    assert mock_metorial_config["apiHost"].startswith("https://")
    assert mock_metorial_config["mcpHost"].startswith("https://")


# =============================================================================
# Mock Tool Manager Fixture Tests
# =============================================================================


class TestMockToolManagerFixture:
  """Tests for mock_tool_manager fixture."""

  def test_has_get_tools_method(self, mock_tool_manager) -> None:
    """Should have get_tools method."""
    assert hasattr(mock_tool_manager, "get_tools")
    assert mock_tool_manager.get_tools() == []

  def test_has_call_tool_method(self, mock_tool_manager) -> None:
    """Should have call_tool method."""
    assert hasattr(mock_tool_manager, "call_tool")

  def test_has_get_tool_method(self, mock_tool_manager) -> None:
    """Should have get_tool method."""
    assert hasattr(mock_tool_manager, "get_tool")
    assert mock_tool_manager.get_tool() is None


# =============================================================================
# Mock MCP Tool Fixture Tests
# =============================================================================


class TestMockMcpToolFixture:
  """Tests for mock_mcp_tool fixture."""

  def test_has_name(self, mock_mcp_tool) -> None:
    """Should have name attribute."""
    assert mock_mcp_tool.name == "test_tool"

  def test_has_description(self, mock_mcp_tool) -> None:
    """Should have description attribute."""
    assert mock_mcp_tool.description == "A test tool"

  def test_has_parameters(self, mock_mcp_tool) -> None:
    """Should have parameters attribute."""
    assert "type" in mock_mcp_tool.parameters
    assert "properties" in mock_mcp_tool.parameters


# =============================================================================
# Mock MCP Session Fixture Tests
# =============================================================================


class TestMockMcpSessionFixture:
  """Tests for mock_mcp_session fixture."""

  def test_has_get_tool_manager_method(self, mock_mcp_session) -> None:
    """Should have get_tool_manager method."""
    assert hasattr(mock_mcp_session, "get_tool_manager")

  def test_has_close_method(self, mock_mcp_session) -> None:
    """Should have close method."""
    assert hasattr(mock_mcp_session, "close")


# =============================================================================
# Mock HTTP Response Fixture Tests
# =============================================================================


class TestMockHttpResponseFixture:
  """Tests for mock_http_response fixture."""

  def test_has_status_code(self, mock_http_response) -> None:
    """Should have status_code attribute."""
    assert mock_http_response.status_code == 200

  def test_has_headers(self, mock_http_response) -> None:
    """Should have headers dict."""
    assert "X-Request-ID" in mock_http_response.headers
    assert "Content-Type" in mock_http_response.headers

  def test_has_request_id_header(self, mock_http_response) -> None:
    """Should have X-Request-ID header."""
    assert mock_http_response.headers["X-Request-ID"] == "req-test-123"


# =============================================================================
# Client Context Manager Tests
# =============================================================================


class TestClientContextManagers:
  """Tests for client context manager behavior."""

  def test_sync_client_context_manager(
    self, sync_metorial_client: MetorialSync
  ) -> None:
    """Sync client should support context manager."""
    with sync_metorial_client as client:
      assert client is sync_metorial_client

  @pytest.mark.asyncio
  async def test_async_client_context_manager(
    self, async_metorial_client: Metorial
  ) -> None:
    """Async client should support async context manager."""
    async with async_metorial_client as client:
      assert client is async_metorial_client


# =============================================================================
# Client Configuration Tests
# =============================================================================


class TestClientConfiguration:
  """Tests for client configuration handling."""

  def test_client_default_timeout(
    self, metorial_client: Metorial | MetorialSync
  ) -> None:
    """Client should have default timeout configured."""
    assert metorial_client._config_data["timeout"] == 30.0

  def test_client_default_max_retries(
    self, metorial_client: Metorial | MetorialSync
  ) -> None:
    """Client should have default max retries configured."""
    assert metorial_client._config_data["maxRetries"] == 3

  def test_client_has_http_client(
    self, metorial_client: Metorial | MetorialSync
  ) -> None:
    """Client should have HTTP client initialized."""
    assert hasattr(metorial_client, "_http_client")
