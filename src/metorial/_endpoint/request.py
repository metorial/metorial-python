from __future__ import annotations

from typing import Any


class MetorialRequest:
  """Request configuration object for Metorial API calls."""

  def __init__(
    self,
    path: str | list[str],
    host: str | None = None,
    query: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
  ):
    self.path = path
    self.host = host
    self.query = query
    self.body = body
