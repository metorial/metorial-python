from __future__ import annotations

from typing import Any, Dict, Optional, Union


class MetorialRequest:
  """Request configuration object for Metorial API calls."""

  def __init__(
    self,
    path: Union[str, list[str]],
    host: Optional[str] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
  ):
    self.path = path
    self.host = host
    self.query = query
    self.body = body
