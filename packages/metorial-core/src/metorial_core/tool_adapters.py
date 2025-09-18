"""
Tool format adapters for converting between Metorial and OpenAI formats.
"""

import re
import logging
from typing import Dict, Any, List, Optional, TypedDict
from dataclasses import dataclass

logger = logging.getLogger(__name__)


class OpenAITool(TypedDict):
  """OpenAI tool format structure."""

  type: str
  function: Dict[str, Any]


class MetorialTool(TypedDict):
  """Metorial tool format structure."""

  name: str
  description: str
  parameters: Dict[str, Any]


class ToolStatistics(TypedDict):
  """Statistics about tool validation."""

  total_tools: int
  valid_tools: int
  invalid_tools: int
  warning_count: int
  warnings: List[str]


@dataclass
class ToolValidationResult:
  """Result of tool validation."""

  is_valid: bool
  errors: List[str]
  warnings: List[str]
  sanitized_name: Optional[str] = None


class ToolFormatAdapter:
  """Handles conversion between Metorial and OpenAI tool formats."""

  # OpenAI function name pattern: alphanumeric, underscore, hyphen only
  OPENAI_FUNCTION_PATTERN = re.compile(r"^[a-zA-Z0 - 9_-]+$")

  # Common replacements for invalid characters
  NAME_REPLACEMENTS = {
    " ": "_",  # Space to underscore
    ".": "_",  # Dot to underscore
    "-": "_",  # Hyphen to underscore (keep as is)
    "(": "",  # Remove parentheses
    ")": "",
    "[": "",
    "]": "",
    "{": "",
    "}": "",
    "<": "",
    ">": "",
    "&": "and",  # & to 'and'
    "+": "plus",  # + to 'plus'
    "#": "hash",  # # to 'hash'
    "@": "at",  # @ to 'at'
    "!": "",  # Remove exclamation
    "?": "",  # Remove question
    ",": "",  # Remove comma
    ";": "",  # Remove semicolon
    ":": "",  # Remove colon
    '"': "",  # Remove quotes
    "'": "",  # Remove quotes
    "`": "",  # Remove backtick
    "~": "",  # Remove tilde
    "^": "",  # Remove caret
    "|": "",  # Remove pipe
    "\\": "",  # Remove backslash
    "/": "_",  # Forward slash to underscore
  }

  @classmethod
  def sanitize_function_name(cls, name: str) -> str:
    """Sanitizes a function name to match OpenAI requirements."""

    if not name:
      return "unknown_tool"

    # Apply replacements
    sanitized = name
    for old_char, new_char in cls.NAME_REPLACEMENTS.items():
      sanitized = sanitized.replace(old_char, new_char)

    # Remove multiple consecutive underscores
    sanitized = re.sub(r"_+", "_", sanitized)

    # Remove leading/trailing underscores
    sanitized = sanitized.strip("_")

    # Ensure it starts with a letter or underscore
    if sanitized and not sanitized[0].isalpha() and sanitized[0] != "_":
      sanitized = f"tool_{sanitized}"

    # Ensure it's not empty
    if not sanitized:
      sanitized = "unknown_tool"

    # Truncate if too long (OpenAI has limits)
    if len(sanitized) > 64:
      sanitized = sanitized[:64]

    return sanitized

  @classmethod
  def validate_tool(cls, tool: Any) -> ToolValidationResult:
    """Validates a tool object for OpenAI compatibility."""
    errors = []
    warnings: list[str] = []

    # Check if tool has required structure
    if not hasattr(tool, "__dict__"):
      errors.append("Tool must be an object with attributes")
      return ToolValidationResult(False, errors, warnings)

    # Extract tool information
    tool_name = getattr(tool, "name", None)
    tool_description = getattr(tool, "description", None)
    tool_parameters = getattr(tool, "parameters", None)

    # Validate name
    if not tool_name:
      errors.append("Tool must have a name")
    elif not isinstance(tool_name, str):
      errors.append("Tool name must be a string")
    else:
      sanitized_name = cls.sanitize_function_name(tool_name)
      if sanitized_name != tool_name:
        warnings.append(f"Tool name '{tool_name}' was sanitized to '{sanitized_name}'")

    if not cls.OPENAI_FUNCTION_PATTERN.match(sanitized_name):
      errors.append(
        f"Sanitized tool name '{sanitized_name}' still doesn't match OpenAI pattern"
      )
    else:
      tool_name = sanitized_name

    # Validate description
    if not tool_description:
      warnings.append("Tool should have a description for better AI understanding")

    # Validate parameters
    if tool_parameters is None:
      warnings.append("Tool should have parameters defined")

    is_valid = len(errors) == 0

    return ToolValidationResult(
      is_valid=is_valid,
      errors=errors,
      warnings=warnings,
      sanitized_name=tool_name,
    )

  @classmethod
  def to_openai_format(cls, metorial_tool: Any) -> Optional[OpenAITool]:
    """Converts a Metorial tool to OpenAI format with automatic sanitization."""

    # Validate the tool
    validation = cls.validate_tool(metorial_tool)

    if not validation.is_valid:
      # Log validation errors for debugging
      print(f"⚠️ Tool validation failed: {validation.errors}")
      return None

    # Log warnings
    for warning in validation.warnings:
      print(f"⚠️ Tool validation warning: {warning}")

    # Convert to OpenAI format
    openai_tool = OpenAITool(
      type="function",
      function={
        "name": validation.sanitized_name,
        "description": getattr(
          metorial_tool, "description", "No description available"
        ),
        "parameters": getattr(metorial_tool, "parameters", {}),
      },
    )

    return openai_tool

  @classmethod
  def from_openai_format(cls, openai_tool: Dict[str, Any]) -> MetorialTool:
    """Converts an OpenAI tool format back to Metorial format."""
    if openai_tool.get("type") != "function":
      raise ValueError("OpenAI tool must be of type 'function'")

    function = openai_tool.get("function", {})

    return MetorialTool(
      name=function.get("name", ""),
      description=function.get("description", ""),
      parameters=function.get("parameters", {}),
    )


class ToolSanitizer:
  """Handles bulk tool sanitization and filtering."""

  @classmethod
  def sanitize_tools(
    cls, tools: List[Any], filter_invalid: bool = True, log_warnings: bool = True
  ) -> List[OpenAITool]:
    """Sanitizes a list of tools, optionally filtering out invalid ones."""
    openai_tools = []
    invalid_count = 0
    sanitized_names: dict[str, str] = {}  # Track original -> sanitized name mappings
    name_conflicts = []  # Track sanitization conflicts

    for tool in tools:
      try:
        openai_tool = ToolFormatAdapter.to_openai_format(tool)
        if openai_tool:
          original_name = getattr(tool, "name", "unknown")
          sanitized_name = openai_tool["function"]["name"]

          # Check for sanitization conflicts
          if sanitized_name in sanitized_names:
            if sanitized_names[sanitized_name] != original_name:
              conflict_msg = f"Tool name conflict: '{original_name}' and '{sanitized_names[sanitized_name]}' both sanitize to '{sanitized_name}'"
              name_conflicts.append(conflict_msg)
              if log_warnings:
                logger.warning(f"⚠️ {conflict_msg}")
          else:
            sanitized_names[sanitized_name] = original_name

          # Log name changes
          if original_name != sanitized_name and log_warnings:
            logger.warning(
              f"⚠️ Tool name sanitized: '{original_name}' → '{sanitized_name}'"
            )

          openai_tools.append(openai_tool)
        else:
          invalid_count += 1
      except Exception as e:
        if log_warnings:
          logger.warning(
            f"⚠️ Error processing tool {getattr(tool, 'name', 'unknown')}: {e}"
          )
        invalid_count += 1

    if log_warnings and invalid_count > 0:
      logger.warning(
        f"⚠️ Filtered out {invalid_count} invalid tools, kept {len(openai_tools)} valid tools"
      )

    if log_warnings and name_conflicts:
      logger.warning(
        f"⚠️ Found {len(name_conflicts)} tool name sanitization conflicts. This may cause tool call failures."
      )

    return openai_tools

  @classmethod
  def get_tool_statistics(cls, tools: List[Any]) -> ToolStatistics:
    """Provides statistics about tool validation."""
    total_tools = len(tools)
    valid_tools = 0
    invalid_tools = 0
    warnings = []

    for tool in tools:
      validation = ToolFormatAdapter.validate_tool(tool)
      if validation.is_valid:
        valid_tools += 1
      else:
        invalid_tools += 1

      warnings.extend(validation.warnings)

    return ToolStatistics(
      total_tools=total_tools,
      valid_tools=valid_tools,
      invalid_tools=invalid_tools,
      warning_count=len(warnings),
      warnings=warnings,
    )
