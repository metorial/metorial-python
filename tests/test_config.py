"""
Tests for configuration handling.
"""

import pytest

from metorial._base import MetorialBase


class TestConfigFromEnv:
  """Tests for configuration from environment"""

  def test_load_config_from_env(self):
    """Configuration should load API key from parameter."""
    base = MetorialBase(api_key="test-key")

    assert base._config_data["apiKey"] == "test-key"
    assert base._config_data["apiHost"] == "https://api.metorial.com"
    assert base._config_data["mcpHost"] == "https://mcp.metorial.com"

  def test_config_with_dict(self):
    """Configuration should accept dict format."""
    config = {
      "apiKey": "dict-api-key",
      "apiHost": "https://custom-api.example.com",
      "mcpHost": "https://custom-mcp.example.com",
    }
    base = MetorialBase(api_key=config)

    assert base._config_data["apiKey"] == "dict-api-key"
    assert base._config_data["apiHost"] == "https://custom-api.example.com"
    assert base._config_data["mcpHost"] == "https://custom-mcp.example.com"


class TestConfigValidation:
  """Tests for configuration validation"""

  def test_validate_config_missing_key(self):
    """Missing API key should raise ValueError."""
    with pytest.raises(ValueError, match="api_key is required"):
      MetorialBase(api_key=None)

  def test_validate_config_empty_key(self):
    """Empty API key should raise ValueError."""
    with pytest.raises(ValueError, match="api_key is required"):
      MetorialBase(api_key="")

  def test_config_with_updates(self):
    """Additional kwargs should be stored in config."""
    base = MetorialBase(api_key="test-key", custom_param="custom_value")

    assert base._config_data["custom_param"] == "custom_value"


class TestConfigHostDerivation:
  """Tests for automatic host derivation"""

  def test_derive_mcp_from_api_host(self):
    """MCP host should be derived from custom API host."""
    base = MetorialBase(api_key="test-key", api_host="https://api.custom.example.com")

    assert base._config_data["mcpHost"] == "https://mcp.custom.example.com"

  def test_derive_api_from_mcp_host(self):
    """API host should be derived from custom MCP host."""
    base = MetorialBase(api_key="test-key", mcp_host="https://mcp.custom.example.com")

    assert base._config_data["apiHost"] == "https://api.custom.example.com"

  def test_explicit_hosts_not_overwritten(self):
    """Explicitly provided hosts should not be overwritten."""
    base = MetorialBase(
      api_key="test-key",
      api_host="https://api.explicit.com",
      mcp_host="https://mcp.explicit.com",
    )

    assert base._config_data["apiHost"] == "https://api.explicit.com"
    assert base._config_data["mcpHost"] == "https://mcp.explicit.com"


class TestConfigTimeout:
  """Tests for timeout configuration"""

  def test_default_timeout(self):
    """Default timeout should be 30 seconds."""
    base = MetorialBase(api_key="test-key")

    assert base._config_data["timeout"] == 30.0

  def test_custom_timeout(self):
    """Custom timeout should be respected."""
    base = MetorialBase(api_key="test-key", timeout=60.0)

    assert base._config_data["timeout"] == 60.0

  def test_max_retries_default(self):
    """Default max retries should be 3."""
    base = MetorialBase(api_key="test-key")

    assert base._config_data["maxRetries"] == 3

  def test_custom_max_retries(self):
    """Custom max retries should be respected."""
    base = MetorialBase(api_key="test-key", max_retries=5)

    assert base._config_data["maxRetries"] == 5
