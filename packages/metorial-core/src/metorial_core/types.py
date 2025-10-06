"""
Type definitions for Metorial SDK to provide TypeScript-like experience.
"""

from typing import TypedDict, Union, List, Optional, Dict, Any


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


class RunResult(TypedDict):
  """Result from metorial.run() function."""

  text: str
  steps: int


class OAuthSession(TypedDict):
  """OAuth session information."""

  id: str
  url: str
  status: str


ServerDeployments = Union[List[str], List[ServerDeployment]]
MetorialClient = Any

__all__ = [
  "ServerDeployment",
  "MetorialRunParams",
  "RunResult",
  "OAuthSession",
  "ServerDeployments",
  "MetorialClient",
]
