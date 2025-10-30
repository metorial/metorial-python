"""
Utility functions for metorial-core with cross-version compatibility.
"""
import sys
from datetime import datetime
from typing import Union


def parse_iso_datetime(iso_string: str) -> datetime:
  """
  Parse ISO format datetime strings with Python 3.10+ compatibility.

  Python 3.10's datetime.fromisoformat() doesn't support 'Z' suffix for UTC timezone.
  This function provides backward compatibility by handling the 'Z' suffix across all versions.

  Args:
      iso_string: ISO format datetime string (e.g., '2025-10-04T00:37:50.512Z')

  Returns:
      datetime object

  Raises:
      ValueError: If the string format is invalid
  """
  if not isinstance(iso_string, str):
    raise TypeError(f"Expected string, got {type(iso_string)}")

  # Handle 'Z' suffix for UTC timezone
  if iso_string.endswith("Z"):
    # Python 3.11+ supports 'Z' directly, but Python 3.10 doesn't
    if sys.version_info >= (3, 11):
      return datetime.fromisoformat(iso_string)
    else:
      # Replace 'Z' with '+00:00' for Python 3.10 compatibility
      iso_string_normalized = iso_string[:-1] + "+00:00"
      return datetime.fromisoformat(iso_string_normalized)

  # For all other formats, use the standard parser
  return datetime.fromisoformat(iso_string)


def safe_parse_iso_datetime(iso_string: Union[str, None]) -> Union[datetime, None]:
  """
  Safely parse ISO format datetime strings, returning None on error.

  Args:
      iso_string: ISO format datetime string or None

  Returns:
      datetime object or None if parsing fails
  """
  if iso_string is None:
    return None

  try:
    return parse_iso_datetime(iso_string)
  except (ValueError, TypeError):
    return None
