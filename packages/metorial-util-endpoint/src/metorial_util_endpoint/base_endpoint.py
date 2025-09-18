from __future__ import annotations

from .endpoint_manager import MetorialEndpointManager
from .request import MetorialRequest


class BaseMetorialEndpoint:
  """Base class for building custom API endpoints."""

  def __init__(self, manager: MetorialEndpointManager):
    self.manager = manager

  def _get(self, request: MetorialRequest):
    """Execute a GET request."""
    return self.manager._get(request)

  def _post(self, request: MetorialRequest):
    """Execute a POST request."""
    return self.manager._post(request)

  def _put(self, request: MetorialRequest):
    """Execute a PUT request."""
    return self.manager._put(request)

  def _patch(self, request: MetorialRequest):
    """Execute a PATCH request."""
    return self.manager._patch(request)

  def _delete(self, request: MetorialRequest):
    """Execute a DELETE request."""
    return self.manager._delete(request)
