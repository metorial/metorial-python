"""
Shared client core functionality for async and sync clients.

This module contains common logic shared between Metorial and MetorialSync clients
to avoid code duplication.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from metorial._session import MetorialSession


class ClientCoreMixin:
  """Mixin class containing shared client logic."""

  def _normalize_server_deployments(
    self, server_deployments: list[str] | list[dict[str, str]]
  ) -> list[dict[str, str]]:
    """Normalize server deployments to handle both string and object formats.

    Args:
        server_deployments: List of deployment IDs (strings) or
            deployment configs (dicts)

    Returns:
        List of normalized deployment configs with serverDeploymentId key

    Raises:
        ValueError: If deployment format is invalid
    """
    normalized: list[dict[str, str]] = []

    for deployment in server_deployments:
      if isinstance(deployment, str):
        # Simple string format -> convert to object
        normalized.append({"serverDeploymentId": deployment})
      elif isinstance(deployment, dict):
        # Already object format -> validate and use as-is
        if "serverDeploymentId" in deployment:
          normalized.append(deployment)
        elif "id" in deployment:
          converted: dict[str, str] = {"serverDeploymentId": deployment["id"]}
          if "oauthSessionId" in deployment:
            converted["oauthSessionId"] = deployment["oauthSessionId"]
          normalized.append(converted)
        else:
          raise ValueError(f"Invalid deployment object format: {deployment}")
      else:
        raise ValueError(
          f"Invalid deployment type: {type(deployment)} - must be string or dict"
        )

    return normalized

  def _normalize_init(self, init: dict[str, Any] | str | list[str]) -> dict[str, Any]:
    """Normalize session init to a consistent dict format.

    Args:
        init: Can be a dict, a single deployment ID string,
            or list of deployment IDs

    Returns:
        Normalized dict with serverDeployments key
    """
    if isinstance(init, str):
      return {"serverDeployments": [init]}
    elif isinstance(init, list):
      return {"serverDeployments": init}
    return init

  def _build_session_deployments(
    self, normalized_deployments: list[dict[str, str]]
  ) -> list[dict[str, str]]:
    """Build session deployment configs from normalized deployments.

    Args:
        normalized_deployments: List of normalized deployment configs

    Returns:
        List of deployment configs formatted for session creation
    """
    session_deployments: list[dict[str, str]] = []
    for deployment in normalized_deployments:
      deployment_config: dict[str, str] = {"id": deployment["serverDeploymentId"]}
      if "oauthSessionId" in deployment:
        deployment_config["oauthSessionId"] = deployment["oauthSessionId"]
      session_deployments.append(deployment_config)
    return session_deployments

  def _build_simplified_session(
    self,
    session: MetorialSession,
    provider_data: dict[str, Any],
    close_session_fn: Any,
  ) -> dict[str, Any]:
    """Build a simplified session dict for provider session callbacks.

    Args:
        session: The MetorialSession instance
        provider_data: Data from the provider callback
        close_session_fn: Function to close the session

    Returns:
        Simplified session dict with tools and utility functions
    """
    return {
      "tools": provider_data.get("tools"),
      "callTools": provider_data.get("callTools")
      or (lambda tool_calls: session.execute_tools(tool_calls)),
      "getToolManager": lambda: session.get_tool_manager(),
      "session": session,
      "closeSession": close_session_fn,
      "getSession": session.get_session
      if hasattr(session, "get_session")
      else lambda: session._mcp_session.get_session(),
      "getCapabilities": session.get_capabilities
      if hasattr(session, "get_capabilities")
      else lambda: session._mcp_session.get_capabilities(),
      "getClient": session.get_client
      if hasattr(session, "get_client")
      else lambda opts: session._mcp_session.get_client(opts),
      "getServerDeployments": session.get_server_deployments
      if hasattr(session, "get_server_deployments")
      else lambda: session._mcp_session.get_server_deployments(),
      **provider_data,
    }


__all__ = ["ClientCoreMixin"]
