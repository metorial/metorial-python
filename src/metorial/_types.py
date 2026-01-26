"""
Type definitions for Metorial SDK to provide TypeScript-like experience.
"""

from typing import TYPE_CHECKING, Any, TypedDict


class DictAttributeAccess(dict[str, Any]):
  """Base class that supports both dictionary and attribute access."""

  def __getattr__(self, name: str) -> Any:
    """Allow attribute access to dictionary keys."""
    try:
      return self[name]
    except KeyError:
      raise AttributeError(
        f"'{self.__class__.__name__}' object has no attribute '{name}'"
      ) from None

  def __setattr__(self, name: str, value: Any) -> None:
    """Allow setting attributes as dictionary keys."""
    self[name] = value

  def __delattr__(self, name: str) -> None:
    """Allow deleting attributes as dictionary keys."""
    try:
      del self[name]
    except KeyError:
      raise AttributeError(
        f"'{self.__class__.__name__}' object has no attribute '{name}'"
      ) from None


class ServerDeployment(TypedDict, total=False):
  """Server deployment configuration with optional OAuth session.

  Accepts both snake_case (preferred) and camelCase keys:
  - server_deployment_id / serverDeploymentId / id
  - oauth_session_id / oauthSessionId
  """

  server_deployment_id: str
  oauth_session_id: str | None


class OAuthSession(TypedDict):
  """OAuth session information."""

  id: str
  url: str
  status: str


ServerDeployments = list[str] | list[ServerDeployment]

if TYPE_CHECKING:
  from metorial._client import Metorial

  MetorialClient = Metorial
else:
  MetorialClient = Any

__all__ = [
  "DictAttributeAccess",
  "ServerDeployment",
  "OAuthSession",
  "ServerDeployments",
  "MetorialClient",
]
