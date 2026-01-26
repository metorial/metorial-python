"""
Metorial Sync Client
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from types import TracebackType
from typing import Any

from metorial._base import MetorialBase
from metorial._client_core import ClientCoreMixin
from metorial._session import MetorialSession
from metorial.exceptions import MetorialAPIError


class SyncSessionWrapper:
  """Wrapper to provide sync context manager for MetorialSession."""

  def __init__(self, session: MetorialSession):
    self._session = session

  def __enter__(self) -> MetorialSession:
    return self._session

  def __exit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: TracebackType | None,
  ) -> None:
    asyncio.run(self._session.close())

  def __getattr__(self, name: str) -> Any:
    return getattr(self._session, name)


class MetorialSync(ClientCoreMixin, MetorialBase):
  """Synchronous Metorial client with enhanced error handling"""

  def session(
    self,
    server_deployments: str | list[str | dict[str, Any]],
  ) -> SyncSessionWrapper:
    """Create a session for use with sync context manager.

    Args:
        server_deployments: Server deployment ID(s). Can be:
            - A single deployment ID string
            - A list of deployment ID strings
            - A list of deployment config dicts (for OAuth, etc)

    Returns:
        Session wrapper for use with `with`

    Example:
        with metorial.session("deployment-id") as session:
            tool_manager = session.get_tool_manager()
            tools = tool_manager.get_tools_for_openai()
    """
    init: dict[str, Any]
    if isinstance(server_deployments, str):
      init = {"serverDeployments": [server_deployments]}
    elif isinstance(server_deployments, list):
      if server_deployments and isinstance(server_deployments[0], str):
        init = {"serverDeployments": server_deployments}
      else:
        normalized = []
        for d in server_deployments:
          if isinstance(d, dict):
            dep: dict[str, Any] = {"id": d.get("id") or d.get("serverDeploymentId")}
            for k, v in d.items():
              if k not in ("id", "serverDeploymentId"):
                dep[k] = v
            normalized.append(dep)
        init = {"serverDeployments": normalized}

    return SyncSessionWrapper(self.create_mcp_session(init))

  def create_mcp_connection(self, init: dict[str, Any]) -> Any:
    """Synchronous wrapper for create_mcp_connection with retry logic"""
    return asyncio.run(self._create_mcp_connection_async(init))

  async def _create_mcp_connection_async(self, init: dict[str, Any]) -> Any:
    for attempt in range(self._config["maxRetries"]):
      try:
        session = self.create_mcp_session(init)
        deployments = await session.get_server_deployments()
        return await session.get_client({"deploymentId": deployments[0]["id"]})
      except Exception as e:
        if attempt == self._config["maxRetries"] - 1:
          raise MetorialAPIError(
            f"Failed to create MCP connection after {self._config['maxRetries']} attempts: {e}"
          ) from e
        await asyncio.sleep(2**attempt)

  def with_session(
    self,
    init: dict[str, Any] | str | list[str],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    """Synchronous wrapper for with_session"""

    async def async_action_wrapper(session: MetorialSession) -> Any:
      if asyncio.iscoroutinefunction(action):
        return await action(session)
      else:
        return action(session)

    return asyncio.run(self._with_session_async(init, async_action_wrapper))

  async def _with_session_async(
    self,
    init: dict[str, Any] | str | list[str],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    session = None
    try:
      # Convert string or list of strings to proper init format
      normalized_init = self._normalize_init(init)
      session = self.create_mcp_session(normalized_init)
      return await action(session)
    except Exception as e:
      self.logger.error(f"Session action failed: {e}")
      raise
    finally:
      if session:
        try:
          await session.close()
        except Exception as e:
          self.logger.warning(f"Failed to close session: {e}")

  def with_provider_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: dict[str, Any] | str | list[str],
    action: Callable[[dict[str, Any]], Any],
  ) -> Any:
    """Synchronous wrapper for with_provider_session"""
    return asyncio.run(self._with_provider_session_async(provider, init, action))

  async def _with_provider_session_async(
    self,
    provider: Callable[[MetorialSession], Any],
    init: dict[str, Any] | str | list[str],
    action: Callable[[dict[str, Any]], Any],
  ) -> Any:
    normalized_init = self._normalize_init(init)

    async def session_action(session: MetorialSession) -> Any:
      try:
        provider_data = await provider(session)

        simplified_session = {
          "tools": provider_data.get("tools"),
          "callTools": lambda tool_calls: session.execute_tools(tool_calls),
          "getToolManager": lambda: session.get_tool_manager(),
          **provider_data,
        }

        return action(simplified_session)

      except Exception as e:
        self.logger.error(f"Error in provider session: {e}")
        raise

    return await self._with_session_async(normalized_init, session_action)

  def __enter__(self) -> MetorialSync:
    return self

  def __exit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: TracebackType | None,
  ) -> None:
    asyncio.run(self.close())
