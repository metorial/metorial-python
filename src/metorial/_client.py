import asyncio
import contextlib
from collections.abc import Awaitable, Callable
from types import TracebackType
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from metorial._base import MetorialBase
from metorial._session import MetorialSession
from metorial.connectors import (
  ConnectedSession,
  MetorialAdapter,
  metorial_anthropic,
  metorial_deepseek,
  metorial_google,
  metorial_mistral,
  metorial_openai,
  metorial_togetherai,
  metorial_xai,
)
from metorial.exceptions import MetorialAPIError

if TYPE_CHECKING:
  from metorial._protocols import ToolManagerProtocol

ProviderType = Literal[
  "anthropic", "openai", "google", "mistral", "deepseek", "xai", "togetherai"
]
ConnectResult = TypeVar("ConnectResult")


class ProviderSession:
  """Async context manager for Magnetar provider-specific sessions."""

  def __init__(
    self,
    metorial: "Metorial",
    provider: ProviderType,
    providers: list[str | dict[str, Any]] | None = None,
  ) -> None:
    self._metorial = metorial
    self._provider = provider
    self._providers = providers or []
    self._connected_session: ConnectedSession[Any] | None = None
    self._tool_manager: ToolManagerProtocol | None = None
    self._tools: list[dict[str, Any]] = []
    self._call_tools_fn: Callable[..., Awaitable[Any]] | None = None
    self._closed = False

  def _check_closed(self) -> None:
    if self._closed:
      raise RuntimeError(
        "Cannot use session after it has been closed. "
        "Use 'async with metorial.provider_session(...) as session:' "
        "and keep operations inside the context manager."
      )

  @property
  def tools(self) -> list[dict[str, Any]]:
    self._check_closed()
    return self._tools

  @property
  def tool_manager(self) -> "ToolManagerProtocol | None":
    self._check_closed()
    return self._tool_manager

  async def call_tools(self, tool_calls: list[Any]) -> Any:
    self._check_closed()
    if self._call_tools_fn is None:
      raise RuntimeError("Session not initialized. Use 'async with' context manager.")
    return await self._call_tools_fn(tool_calls)

  async def call_tool(self, tool_name: str, kwargs: dict[str, Any]) -> Any:
    self._check_closed()
    if self._tool_manager is None:
      raise RuntimeError("Session not initialized. Use 'async with' context manager.")
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    return await self._tool_manager.execute_tool(tool_name, filtered_kwargs)

  def get_tools(self) -> list[dict[str, Any]]:
    self._check_closed()
    return self._tools

  async def __aenter__(self) -> "ProviderSession":
    self._connected_session = await self._metorial.connect(
      adapter=self._metorial._resolve_provider_adapter(self._provider),
      providers=self._providers,
    )
    self._tool_manager = await self._connected_session.get_tool_manager()
    self._tools = cast(list[dict[str, Any]], self._connected_session.tools())
    self._call_tools_fn = self._connected_session.call_tools

    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: TracebackType | None,
  ) -> None:
    self._closed = True
    if self._connected_session is not None:
      with contextlib.suppress(Exception):
        await self._connected_session.close()


class Metorial(MetorialBase):
  def _resolve_connect_adapter(
    self,
    adapter: MetorialAdapter[ConnectResult]
    | Callable[[], MetorialAdapter[ConnectResult]],
  ) -> MetorialAdapter[ConnectResult]:
    if hasattr(adapter, "__resolve"):
      return cast(MetorialAdapter[ConnectResult], adapter)
    return adapter()

  def _resolve_provider_adapter(
    self, provider: ProviderType
  ) -> MetorialAdapter[ConnectedSession[Any]]:
    provider_adapters: dict[
      ProviderType, Callable[[], MetorialAdapter[ConnectedSession[Any]]]
    ] = {
      "openai": metorial_openai,
      "anthropic": metorial_anthropic,
      "google": metorial_google,
      "mistral": metorial_mistral,
      "deepseek": metorial_deepseek,
      "xai": metorial_xai,
      "togetherai": metorial_togetherai,
    }
    return provider_adapters[provider]()

  async def _resolve_magnetar_adapter_result(
    self,
    *,
    adapter: MetorialAdapter[ConnectResult]
    | Callable[[], MetorialAdapter[ConnectResult]],
    providers: list[str | dict[str, Any]] | None = None,
    client: dict[str, str] | None = None,
  ) -> tuple[MetorialSession, ConnectResult]:
    resolved_adapter = self._resolve_connect_adapter(adapter)
    init: dict[str, Any] = {"providers": providers or []}
    if client is not None:
      init["client"] = client
    session = self.create_magnetar_mcp_session(init)
    resolve = getattr(resolved_adapter, "__resolve")
    result = await resolve(session)
    return session, result

  def _normalize_magnetar_init(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
  ) -> dict[str, Any]:
    if isinstance(init, str):
      return {"providers": [init]}
    if isinstance(init, list):
      return {"providers": init}
    return init

  def session(
    self,
    providers: list[str | dict[str, Any]] | None = None,
  ) -> MetorialSession:
    return self.create_magnetar_mcp_session({"providers": providers or []})

  def provider_session(
    self,
    provider: ProviderType,
    providers: list[str | dict[str, Any]] | None = None,
  ) -> ProviderSession:
    return ProviderSession(self, provider, providers=providers)

  async def connect(
    self,
    *,
    adapter: MetorialAdapter[ConnectResult]
    | Callable[[], MetorialAdapter[ConnectResult]],
    providers: list[str | dict[str, Any]] | None = None,
    client: dict[str, str] | None = None,
  ) -> ConnectResult:
    _, result = await self._resolve_magnetar_adapter_result(
      adapter=adapter,
      providers=providers,
      client=client,
    )
    return result

  async def wait_for_setup_session(
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

        session_status: object | None
        if hasattr(status, "status"):
          session_status = status.status
        elif isinstance(status, dict):
          session_status = status.get("status")
        else:
          raise RuntimeError(f"Unexpected status type: {type(status)}")

        if session_status == "failed":
          raise RuntimeError(f"Setup session {session_id} failed")
        if session_status != "completed":
          all_completed = False

      if all_completed:
        return results

      await asyncio.sleep(poll_interval)

  async def create_magnetar_mcp_connection(
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
            f"Failed to create MCP connection after {self._config['maxRetries']} attempts: {e}"
          ) from e
        await asyncio.sleep(2**attempt)

  async def with_magnetar_session(
    self,
    init: dict[str, Any] | str | list[str | dict[str, Any]],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    try:
      normalized_init = self._normalize_magnetar_init(init)
      session = self.create_magnetar_mcp_session(normalized_init)
      return await action(session)
    except Exception as e:
      self.logger.error(f"Session action failed: {e}")
      raise

  async def __aenter__(self) -> "Metorial":
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: Any,
  ) -> None:
    await self.close()
