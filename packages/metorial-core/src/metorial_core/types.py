"""
Type definitions for Metorial SDK to provide TypeScript-like experience.
"""

from typing import TypedDict, Union, List, Optional, Dict, Any


class DictAttributeAccess(dict):
  """Base class that supports both dictionary and attribute access."""

  def __getattr__(self, name: str) -> Any:
    """Allow attribute access to dictionary keys."""
    try:
      return self[name]
    except KeyError:
      raise AttributeError(
        f"'{self.__class__.__name__}' object has no attribute '{name}'"
      )

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
      )


class ServerDeployment(TypedDict, total=False):
  """Server deployment configuration with optional OAuth session."""

  serverDeploymentId: str
  oauthSessionId: Optional[str]


class MetorialRunParams(TypedDict, total=False):
  """Parameters for metorial.run() function."""

  message: str
  server_deployments: Union[List[str], List[ServerDeployment]]
  client: Any
  model: str
  max_steps: int
  tools: Optional[List[str]]
  temperature: Optional[float]
  max_tokens: Optional[int]


class RunResult(DictAttributeAccess):
  """Result from metorial.run() function with hybrid dict/attribute access.

  Supports both:
  - Dictionary access: result["text"], result["steps"]
  - Attribute access: result.text, result.steps
  """

  def __init__(self, text: str, steps: int):
    super().__init__(text=text, steps=steps)
    # Explicit attributes for better IDE support
    self.text: str = text
    self.steps: int = steps


class OAuthSession(TypedDict):
  """OAuth session information."""

  id: str
  url: str
  status: str


ServerDeployments = Union[List[str], List[ServerDeployment]]
MetorialClient = Any

__all__ = [
  "DictAttributeAccess",
  "ServerDeployment",
  "MetorialRunParams",
  "RunResult",
  "OAuthSession",
  "ServerDeployments",
  "MetorialClient",
]
