"""
Tests for tool adapter functionality.
"""

from unittest.mock import MagicMock

from metorial._tool_adapters import (
  ToolFormatAdapter,
  ToolSanitizer,
)


class TestSanitizeFunctionName:
  """Tests for ToolFormatAdapter.sanitize_function_name"""

  def test_sanitize_function_name_valid(self):
    """Valid names should pass through unchanged."""
    assert ToolFormatAdapter.sanitize_function_name("my_tool") == "my_tool"
    assert ToolFormatAdapter.sanitize_function_name("myTool") == "myTool"
    assert ToolFormatAdapter.sanitize_function_name("tool123") == "tool123"
    assert ToolFormatAdapter.sanitize_function_name("my-tool") == "my_tool"

  def test_sanitize_function_name_special_chars(self):
    """Special characters should be replaced or removed."""
    assert ToolFormatAdapter.sanitize_function_name("tool.name") == "tool_name"
    assert ToolFormatAdapter.sanitize_function_name("tool&name") == "tool_and_name"
    assert ToolFormatAdapter.sanitize_function_name("tool+name") == "tool_plus_name"
    assert ToolFormatAdapter.sanitize_function_name("tool#name") == "tool_hash_name"
    assert ToolFormatAdapter.sanitize_function_name("tool@name") == "tool_at_name"

  def test_sanitize_function_name_spaces(self):
    """Spaces should become underscores."""
    assert ToolFormatAdapter.sanitize_function_name("my tool") == "my_tool"
    assert ToolFormatAdapter.sanitize_function_name("my  tool") == "my_tool"
    assert ToolFormatAdapter.sanitize_function_name(" my tool ") == "my_tool"

  def test_sanitize_function_name_empty(self):
    """Empty names should return default."""
    assert ToolFormatAdapter.sanitize_function_name("") == "unknown_tool"

  def test_sanitize_function_name_numeric_prefix(self):
    """Names starting with numbers should get prefix."""
    assert ToolFormatAdapter.sanitize_function_name("123tool") == "tool_123tool"


class TestOpenAIFunctionPattern:
  """Tests for the OpenAI function name pattern regex."""

  def test_openai_function_pattern_valid(self):
    """Valid function names should match the pattern."""
    pattern = ToolFormatAdapter.OPENAI_FUNCTION_PATTERN
    assert pattern.match("my_tool")
    assert pattern.match("myTool")
    assert pattern.match("tool123")
    assert pattern.match("my-tool")
    assert pattern.match("TOOL")
    assert pattern.match("a")

  def test_openai_function_pattern_invalid(self):
    """Invalid function names should not match the pattern."""
    pattern = ToolFormatAdapter.OPENAI_FUNCTION_PATTERN
    assert not pattern.match("my tool")  # space
    assert not pattern.match("tool.name")  # dot
    assert not pattern.match("tool@name")  # at symbol
    assert not pattern.match("tool!name")  # exclamation
    assert not pattern.match("")  # empty


class TestToOpenAIFormat:
  """Tests for ToolFormatAdapter.to_openai_format"""

  def test_to_openai_format_valid_tool(self, mock_mcp_tool):
    """Valid tools should convert correctly."""
    result = ToolFormatAdapter.to_openai_format(mock_mcp_tool)

    assert result is not None
    assert result["type"] == "function"
    assert result["function"]["name"] == "test_tool"
    assert result["function"]["description"] == "A test tool"
    assert "properties" in result["function"]["parameters"]

  def test_to_openai_format_sanitizes_name(self):
    """Tool names should be sanitized."""
    tool = MagicMock()
    tool.name = "my tool name"
    tool.description = "Test"
    tool.parameters = {}

    result = ToolFormatAdapter.to_openai_format(tool)

    assert result is not None
    assert result["function"]["name"] == "my_tool_name"

  def test_to_openai_format_missing_name(self):
    """Tools without names should return None."""
    tool = MagicMock()
    tool.name = None
    tool.description = "Test"
    tool.parameters = {}

    result = ToolFormatAdapter.to_openai_format(tool)

    assert result is None


class TestToolValidation:
  """Tests for ToolFormatAdapter.validate_tool"""

  def test_validate_tool_valid(self, mock_mcp_tool):
    """Valid tools should pass validation."""
    result = ToolFormatAdapter.validate_tool(mock_mcp_tool)

    assert result.is_valid
    assert len(result.errors) == 0
    assert result.sanitized_name == "test_tool"

  def test_validate_tool_missing_name(self):
    """Tools without names should fail validation."""
    tool = MagicMock()
    tool.name = None
    tool.description = "Test"
    tool.parameters = {}

    result = ToolFormatAdapter.validate_tool(tool)

    assert not result.is_valid
    assert any("name" in err.lower() for err in result.errors)

  def test_validate_tool_name_warning(self):
    """Tools with sanitized names should have warnings."""
    tool = MagicMock()
    tool.name = "my tool"
    tool.description = "Test"
    tool.parameters = {}

    result = ToolFormatAdapter.validate_tool(tool)

    assert result.is_valid
    assert result.sanitized_name == "my_tool"
    assert any("sanitized" in warn.lower() for warn in result.warnings)


class TestToolSanitizer:
  """Tests for ToolSanitizer class"""

  def test_sanitize_tools_filters_invalid(self):
    """Invalid tools should be filtered out."""
    valid_tool = MagicMock()
    valid_tool.name = "valid_tool"
    valid_tool.description = "Valid"
    valid_tool.parameters = {}

    invalid_tool = MagicMock()
    invalid_tool.name = None
    invalid_tool.description = "Invalid"
    invalid_tool.parameters = {}

    result = ToolSanitizer.sanitize_tools(
      [valid_tool, invalid_tool], log_warnings=False
    )

    assert len(result) == 1
    assert result[0]["function"]["name"] == "valid_tool"

  def test_get_tool_statistics(self, mock_mcp_tool):
    """Tool statistics should be calculated correctly."""
    invalid_tool = MagicMock()
    invalid_tool.name = None
    invalid_tool.description = "Invalid"
    invalid_tool.parameters = {}

    stats = ToolSanitizer.get_tool_statistics([mock_mcp_tool, invalid_tool])

    assert stats["total_tools"] == 2
    assert stats["valid_tools"] == 1
    assert stats["invalid_tools"] == 1
