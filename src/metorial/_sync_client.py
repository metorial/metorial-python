"""
Metorial Sync Client
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from types import TracebackType
from typing import Any

from metorial._base import MetorialBase, _PulsarV1Namespace
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


class _SyncPulsarV1(_PulsarV1Namespace):
  """Extended Pulsar v1 namespace with sync client session methods."""

  def __init__(self, client: MetorialSync) -> None:
    super().__init__(client)
    self._client = client

  def session(
    self,
    server_deployments: str | list[str | dict[str, Any]],
  ) -> SyncSessionWrapper:
    """Create a Pulsar session for use with sync context manager."""
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

    return SyncSessionWrapper(self._client.create_mcp_session(init))


class MetorialSync(ClientCoreMixin, MetorialBase):
  """Synchronous Metorial client with enhanced error handling"""

  def session(
    self,
    providers: list[str | dict[str, Any]] | None = None,
  ) -> SyncSessionWrapper:
    """Create a Magnetar session for use with sync context manager.

    Args:
        providers: Provider deployment ID(s). Can be:
            - A list of provider deployment ID strings
            - A list of provider config dicts (with provider_deployment_id,
              session_template_id, provider_auth_config_id, etc.)

    Returns:
        Session wrapper for use with `with`

    Example:
        with metorial.session(providers=["provider-deployment-id"]) as session:
            tool_manager = session.get_tool_manager()
    """
    init: dict[str, Any] = {}
    if providers is not None:
      init["providers"] = providers
    else:
      init["providers"] = []
    return SyncSessionWrapper(self.create_magnetar_mcp_session(init))

  def wait_for_setup_session(
    self,
    sessions: Any | list[Any],
    poll_interval: float = 5.0,
    timeout: float = 600.0,
  ) -> list[Any]:
    """Wait for setup sessions to complete OAuth authentication (sync).

    Args:
        sessions: Single session or list of setup session objects
        poll_interval: Seconds between polls (minimum 2s)
        timeout: Maximum seconds to wait

    Returns:
        List of completed setup session statuses
    """
    return asyncio.run(
      self._wait_for_setup_session_async(sessions, poll_interval, timeout)
    )

  async def _wait_for_setup_session_async(
    self,
    sessions: Any | list[Any],
    poll_interval: float = 5.0,
    timeout: float = 600.0,
  ) -> list[Any]:
    import time

    if not isinstance(sessions, list):
      sessions = [sessions]

    if not sessions:
      return []

    poll_interval = max(poll_interval, 2.0)
    start_time = time.time()
    results: list[Any] = []

    while True:
      if time.time() - start_time > timeout:
        raise TimeoutError(
          f"Setup session authentication timeout after {timeout} seconds"
        )

      all_completed = True
      results = []

      deployments = self.provider_deployments
      if deployments is None:
        raise RuntimeError("Provider deployments not initialized")

      for session in sessions:
        session_id = session.id if hasattr(session, "id") else session["id"]
        status = deployments.setup_sessions.get(session_id)
        results.append(status)

        session_status: str | None
        if hasattr(status, "status"):
          session_status = status.status
        elif isinstance(status, dict):
          session_status = status.get("status")
        else:
          raise RuntimeError(f"Unexpected status type: {type(status)}")

        if session_status == "failed":
          raise RuntimeError(f"Setup session {session_id} failed")
        elif session_status != "completed":
          all_completed = False

      if all_completed:
        return results

      await asyncio.sleep(poll_interval)

  @property
  def v1(self) -> _SyncPulsarV1:
    """Access legacy Pulsar API (v1)."""
    return _SyncPulsarV1(self)

  def _normalize_magnetar_init(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
  ) -> dict[str, Any]:
    if isinstance(init, str):
      return {"providers": [init]}
    if isinstance(init, list):
      return {"providers": init}
    return init

  def create_magnetar_mcp_connection(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
  ) -> Any:
    """Synchronous wrapper for Magnetar create_mcp_connection with retry logic."""
    return asyncio.run(self._create_magnetar_mcp_connection_async(init))

  async def _create_magnetar_mcp_connection_async(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
  ) -> Any:
    normalized_init = self._normalize_magnetar_init(init)
    for attempt in range(self._config["maxRetries"]):
      try:
        session = self.create_magnetar_mcp_session(normalized_init)
        deployments = await session.get_server_deployments()
        return await session.get_client({"deploymentId": deployments[0]["id"]})
      except Exception as e:
        if attempt == self._config["maxRetries"] - 1:
          raise MetorialAPIError(
            f"Failed to create Magnetar MCP connection after {self._config['maxRetries']} attempts: {e}"
          ) from e
        await asyncio.sleep(2**attempt)

  def with_magnetar_session(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    """Synchronous wrapper for Magnetar with_session."""

    async def async_action_wrapper(session: MetorialSession) -> Any:
      if asyncio.iscoroutinefunction(action):
        return await action(session)
      else:
        return action(session)

    return asyncio.run(self._with_magnetar_session_async(init, async_action_wrapper))

  async def _with_magnetar_session_async(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    session = None
    try:
      normalized_init = self._normalize_magnetar_init(init)
      session = self.create_magnetar_mcp_session(normalized_init)
      return await action(session)
    except Exception as e:
      self.logger.error(f"Magnetar session action failed: {e}")
      raise
    finally:
      if session:
        try:
          await session.close()
        except Exception as e:
          self.logger.warning(f"Failed to close Magnetar session: {e}")

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
