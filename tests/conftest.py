"""
Shared test fixtures and configuration for metorial tests.

Includes sync/async client parametrization pattern.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from unittest.mock import AsyncMock, MagicMock

import pytest

if TYPE_CHECKING:
  from metorial import Metorial, MetorialSync


# --------------------------------------------------------------------------
# Pytest configuration
# --------------------------------------------------------------------------


def pytest_configure(config: pytest.Config) -> None:
  """Register custom markers."""
  config.addinivalue_line(
    "markers",
    "sync_and_async: mark test to run with both sync and async clients",
  )


# --------------------------------------------------------------------------
# Sync/Async client parametrization
# --------------------------------------------------------------------------


@pytest.fixture(params=["sync", "async"])
def client_type(request: pytest.FixtureRequest) -> Literal["sync", "async"]:
  """Parametrize tests to run with both sync and async clients."""
  return request.param


@pytest.fixture
def metorial_client(
  client_type: Literal["sync", "async"],
  mock_metorial_config: dict[str, str],
) -> Metorial | MetorialSync:
  """Create a Metorial client based on client_type fixture.

  This allows tests marked with @pytest.mark.sync_and_async to run
  automatically with both sync and async clients.
  """
  if client_type == "sync":
    from metorial import MetorialSync

    return MetorialSync(api_key=mock_metorial_config["apiKey"])
  else:
    from metorial import Metorial

    return Metorial(api_key=mock_metorial_config["apiKey"])


@pytest.fixture
def async_metorial_client(mock_metorial_config: dict[str, str]) -> Metorial:
  """Create an async-only Metorial client for async-specific tests."""
  from metorial import Metorial

  return Metorial(api_key=mock_metorial_config["apiKey"])


@pytest.fixture
def sync_metorial_client(mock_metorial_config: dict[str, str]) -> MetorialSync:
  """Create a sync-only Metorial client for sync-specific tests."""
  from metorial import MetorialSync

  return MetorialSync(api_key=mock_metorial_config["apiKey"])


# --------------------------------------------------------------------------
# Mock fixtures
# --------------------------------------------------------------------------


@pytest.fixture
def mock_tool_manager() -> MagicMock:
  """Mock tool manager for testing."""
  manager = MagicMock()
  manager.get_tools.return_value = []
  manager.call_tool = AsyncMock(return_value={"content": "result"})
  manager.get_tool.return_value = None
  return manager


@pytest.fixture
def mock_metorial_config() -> dict[str, str]:
  """Mock configuration for testing."""
  return {
    "apiKey": "test-api-key",
    "apiHost": "https://api.metorial.com",
    "mcpHost": "https://mcp.metorial.com",
  }


@pytest.fixture
def mock_mcp_tool() -> MagicMock:
  """Mock MCP tool object."""
  tool = MagicMock()
  tool.name = "test_tool"
  tool.description = "A test tool"
  tool.parameters = {"type": "object", "properties": {"param1": {"type": "string"}}}
  return tool


@pytest.fixture
def mock_mcp_session() -> MagicMock:
  """Mock MCP session for testing."""
  session = MagicMock()
  session.get_tool_manager = AsyncMock()
  session.close = AsyncMock()
  return session


@pytest.fixture
def mock_http_response() -> MagicMock:
  """Mock HTTP response for testing RawResponse."""
  response = MagicMock()
  response.status_code = 200
  response.headers = {
    "X-Request-ID": "req-test-123",
    "Content-Type": "application/json",
  }
  return response
