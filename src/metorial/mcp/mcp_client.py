from __future__ import annotations

import asyncio
import contextlib
import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import timedelta
from typing import TYPE_CHECKING, Any, TypedDict, TypeVar
from urllib.parse import urlencode, urljoin

from mcp import ClientSession
from mcp.client.sse import sse_client
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import (
  Implementation,
  LoggingLevel,
  PaginatedRequestParams,
  ServerCapabilities,
)
from pydantic import AnyUrl


# TypedDicts for method parameters (matching how they're actually called)
class CallToolParams(TypedDict, total=False):
  name: str
  arguments: dict[str, Any] | None


class CompleteParams(TypedDict, total=False):
  ref: Any
  argument: dict[str, str]


class GetPromptParams(TypedDict, total=False):
  name: str
  arguments: dict[str, str] | None


class ReadResourceParams(TypedDict, total=False):
  uri: str


class ListRequestParams(TypedDict, total=False):
  cursor: str | None


if TYPE_CHECKING:
  import anyio
else:
  try:
    import anyio
  except ImportError:  # pragma: no cover
    anyio = None

T = TypeVar("T")

logger = logging.getLogger("metorial.mcp.client")


def _log_info(message: str, **kwargs: Any) -> None:
  """Conditionally log info messages only if debug logging is enabled."""
  if logger.isEnabledFor(logging.DEBUG):
    logger.info(message, **kwargs)


@dataclass
class RequestOptions:
  timeout: float | None = None
  metadata: dict[str, Any] | None = None


class MetorialMcpClient:
  def __init__(
    self,
    *,
    session: ClientSession,
    transport_closer: Callable[[], Awaitable[None]],
    default_timeout: float | None = 60.0,
  ) -> None:
    self._session = session
    self._transport_closer = transport_closer
    self._closed = False
    self._default_timeout = default_timeout
    self._tasks: set[asyncio.Task[Any]] = set()  # Track background tasks
    logger.debug("MetorialMcpClient instantiated default_timeout=%s", default_timeout)

  async def __aenter__(self) -> MetorialMcpClient:
    """Async context manager entry"""
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: Any,
  ) -> None:
    """Async context manager exit with proper cleanup"""
    await self.close()

  @classmethod
  async def create(
    cls,
    session: Any,  # real Metorial session type
    *,
    host: str,
    deployment_id: str,
    client_name: str | None = None,
    client_version: str | None = None,
    use_sse: bool = True,
    use_http_stream: bool = False,
    connect_timeout: float = 30.0,
    read_timeout: float = 60.0,
    handshake_timeout: float = 3.0,
    extra_query: dict[str, str] | None = None,
    headers: dict[str, str] | None = None,
    log_raw_messages: bool = False,
    raw_message_logger: Callable[[str], None] | None = None,
  ) -> MetorialMcpClient:
    """Create and connect a client."""
    client_name = client_name or "metorial-py-client"
    client_version = client_version or "1.0.0"

    # Build URL
    path = f"/mcp/{session.id}/{deployment_id}/sse"
    q = {"key": session.clientSecret.secret}
    if extra_query:
      q.update(extra_query)
    query = urlencode(q)
    base = host if host.endswith("/") else host + "/"
    url = urljoin(base, path) + f"?{query}"

    _log_info(
      "Connecting to MCP endpoint",
      extra={
        "url": url,
        "deployment_id": deployment_id,
        "session_id": session.id,
      },
    )
    if headers:
      logger.debug("Custom headers set: %s", list(headers.keys()))

    # Pick transport and connect
    def _build_cm() -> Any:
      if use_http_stream:
        from datetime import timedelta

        timeout_delta = timedelta(seconds=connect_timeout)
        return streamablehttp_client(url=url, timeout=timeout_delta, headers=headers)
      if use_sse:
        return sse_client(url=url, timeout=connect_timeout, headers=headers)
      raise NotImplementedError("Only SSE or HTTP stream transports are supported.")

    cm = _build_cm()
    read, write = await cm.__aenter__()
    logger.debug("Transport entered (read/write acquired)")

    async def transport_closer() -> None:
      logger.debug("Closing transport")
      await cm.__aexit__(None, None, None)

    # Optionally wrap read/write to log raw traffic
    if log_raw_messages:
      read, write = wrap_streams_with_logging(
        read, write, raw_message_logger or (lambda m: logger.debug("RAW %s", m))
      )

    client_info = Implementation(name=client_name, version=client_version)

    session_cm = ClientSession(
      read,
      write,
      client_info=client_info,
      read_timeout_seconds=timedelta(seconds=read_timeout),
    )
    await session_cm.__aenter__()
    logger.debug("ClientSession entered; initializing")

    try:
      await asyncio.wait_for(session_cm.initialize(), timeout=handshake_timeout)
      _log_info("MCP session initialized")
    except Exception:
      logger.exception("Initialize failed, cleaning up")
      await session_cm.__aexit__(None, None, None)
      await transport_closer()
      raise

    return cls(
      session=session_cm,
      transport_closer=transport_closer,
      default_timeout=read_timeout,
    )

  @classmethod
  async def from_url(
    cls,
    url: str,
    *,
    client_name: str = "metorial-py-client",
    client_version: str = "1.0.0",
    connect_timeout: float = 30.0,
    read_timeout: float = 60.0,
    handshake_timeout: float = 15.0,
    headers: dict[str, str] | None = None,
    log_raw_messages: bool = False,
    raw_message_logger: Callable[[str], None] | None = None,
  ) -> MetorialMcpClient:
    """Directly connect using a full SSE/HTTP stream URL (debug helper)."""
    cm = sse_client(url=url, timeout=connect_timeout, headers=headers)
    read, write = await cm.__aenter__()

    async def transport_closer() -> None:
      await cm.__aexit__(None, None, None)

    if log_raw_messages:
      read, write = wrap_streams_with_logging(
        read, write, raw_message_logger or (lambda m: logger.debug("RAW %s", m))
      )

    client_info = Implementation(name=client_name, version=client_version)
    session_cm = ClientSession(
      read,
      write,
      client_info=client_info,
      read_timeout_seconds=timedelta(seconds=read_timeout),
    )
    await session_cm.__aenter__()
    try:
      await asyncio.wait_for(session_cm.initialize(), timeout=handshake_timeout)
    except Exception:
      await session_cm.__aexit__(None, None, None)
      await transport_closer()
      raise
    return cls(
      session=session_cm,
      transport_closer=transport_closer,
      default_timeout=read_timeout,
    )

  async def _with_timeout(
    self, coro: Awaitable[T], options: RequestOptions | None
  ) -> T:
    timeout = (
      options.timeout
      if options and options.timeout is not None
      else self._default_timeout
    )
    if timeout is None:
      return await coro
    return await asyncio.wait_for(coro, timeout)

  def _ensure_open(self) -> None:
    if self._closed:
      logger.error("Operation on closed client")
      raise RuntimeError("MetorialMcpClient is closed")

  def get_server_capabilities(self) -> ServerCapabilities:
    caps: ServerCapabilities | None = self._session.get_server_capabilities()
    logger.debug("get_server_capabilities -> %s", caps)
    if caps is None:
      raise RuntimeError("Server capabilities not available")
    return caps

  async def complete(
    self,
    params: CompleteParams,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("complete params=%s options=%s", params, options)
    return await self._with_timeout(
      self._session.complete(ref=params["ref"], argument=params["argument"]), options
    )

  async def set_logging_level(
    self, level: LoggingLevel, options: RequestOptions | None = None
  ) -> Any:
    self._ensure_open()
    logger.debug("set_logging_level level=%s options=%s", level, options)
    return await self._with_timeout(self._session.set_logging_level(level), options)

  async def get_prompt(
    self,
    params: GetPromptParams,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("get_prompt params=%s options=%s", params, options)
    return await self._with_timeout(
      self._session.get_prompt(name=params["name"], arguments=params.get("arguments")),
      options,
    )

  async def list_prompts(
    self,
    params: ListRequestParams | None = None,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_prompts params=%s options=%s", params, options)
    cursor = params.get("cursor") if params else None
    mcp_params = PaginatedRequestParams(cursor=cursor) if cursor else None
    return await self._with_timeout(
      self._session.list_prompts(params=mcp_params), options
    )

  async def list_resources(
    self,
    params: ListRequestParams | None = None,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_resources params=%s options=%s", params, options)
    cursor = params.get("cursor") if params else None
    mcp_params = PaginatedRequestParams(cursor=cursor) if cursor else None
    return await self._with_timeout(
      self._session.list_resources(params=mcp_params), options
    )

  async def list_resource_templates(
    self,
    params: ListRequestParams | None = None,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_resource_templates params=%s options=%s", params, options)
    cursor = params.get("cursor") if params else None
    mcp_params = PaginatedRequestParams(cursor=cursor) if cursor else None
    return await self._with_timeout(
      self._session.list_resource_templates(params=mcp_params), options
    )

  async def read_resource(
    self,
    params: ReadResourceParams,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("read_resource params=%s options=%s", params, options)
    uri = AnyUrl(params["uri"])
    return await self._with_timeout(self._session.read_resource(uri), options)

  async def call_tool(
    self,
    params: CallToolParams,
    result_validator: Callable[[Any], None] | None = None,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    name = params["name"]
    arguments = params.get("arguments")
    logger.debug("call_tool name=%s args=%s options=%s", name, arguments, options)

    result = await self._session.call_tool(name, arguments=arguments)
    logger.debug("call_tool result: %s", result)

    if result_validator is not None:
      try:
        result_validator(result)
      except Exception:
        logger.exception("Result validator failed")
        raise
    return result

  async def list_tools(
    self,
    params: ListRequestParams | None = None,
    options: RequestOptions | None = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_tools params=%s options=%s", params, options)
    cursor = params.get("cursor") if params else None
    mcp_params = PaginatedRequestParams(cursor=cursor) if cursor else None
    return await self._with_timeout(
      self._session.list_tools(params=mcp_params), options
    )

  async def send_roots_list_changed(self, options: RequestOptions | None = None) -> Any:
    self._ensure_open()
    logger.debug("send_roots_list_changed options=%s", options)
    return await self._with_timeout(self._session.send_roots_list_changed(), options)

  async def close(self) -> None:
    if self._closed:
      return

    # Mark as closed immediately to prevent multiple close attempts
    self._closed = True

    try:
      # Cancel and wait for background tasks first
      for task in list(self._tasks):
        if not task.done():
          task.cancel()

      if self._tasks:
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks.clear()

      # Close the session properly with aclose if available
      if hasattr(self._session, "aclose") and callable(self._session.aclose):
        with contextlib.suppress(asyncio.TimeoutError, Exception):
          await asyncio.wait_for(self._session.aclose(), timeout=2.0)
      elif hasattr(self._session, "close") and callable(self._session.close):
        with contextlib.suppress(asyncio.TimeoutError, Exception):
          await asyncio.wait_for(self._session.close(), timeout=2.0)

      # Close the transport gracefully
      if self._transport_closer is not None:
        with contextlib.suppress(asyncio.TimeoutError, Exception):
          await asyncio.wait_for(self._transport_closer(), timeout=1.0)

    except Exception:
      # All cleanup should be resilient and not raise
      pass

  def close_sync(self) -> None:
    try:
      loop = asyncio.get_running_loop()
    except RuntimeError:
      asyncio.run(self.close())
    else:
      loop.run_until_complete(self.close())


class _LoggingRecvStream:
  def __init__(self, inner: Any, logger_fn: Callable[[str], None]) -> None:
    self._inner = inner
    self._log = logger_fn

  async def receive(self) -> Any:
    msg = await self._inner.receive()
    self._log(f"<- {msg}")
    return msg

  # delegate everything else (aclose, __aenter__, __aexit__, etc.)
  def __getattr__(self, name: str) -> Any:
    return getattr(self._inner, name)


class _LoggingSendStream:
  def __init__(self, inner: Any, logger_fn: Callable[[str], None]) -> None:
    self._inner = inner
    self._log = logger_fn

  async def send(self, msg: Any) -> Any:
    self._log(f"-> {msg}")
    return await self._inner.send(msg)

  def __getattr__(self, name: str) -> Any:
    return getattr(self._inner, name)


def wrap_streams_with_logging(
  read_stream: Any, write_stream: Any, logger_fn: Callable[[str], None]
) -> tuple[_LoggingRecvStream, _LoggingSendStream]:
  return _LoggingRecvStream(read_stream, logger_fn), _LoggingSendStream(
    write_stream, logger_fn
  )
