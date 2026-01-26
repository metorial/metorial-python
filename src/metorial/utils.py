"""
Metorial SDK Utilities
"""

from datetime import datetime


def parse_iso_datetime(value: str | None) -> datetime | None:
  """Parse an ISO 8601 datetime string to a datetime object.

  Args:
    value: ISO 8601 datetime string (e.g., '2024-01-01T00:00:00Z')

  Returns:
    datetime object or None if value is None or invalid
  """
  if value is None:
    return None
  try:
    # Handle Z suffix
    if value.endswith("Z"):
      value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)
  except (ValueError, TypeError):
    return None


__all__ = ["parse_iso_datetime"]
