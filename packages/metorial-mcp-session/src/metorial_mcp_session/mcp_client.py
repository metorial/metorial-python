from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, Awaitable, Callable, Dict, Optional, TypeVar, List
from urllib.parse import urlencode, urljoin

from mcp import ClientSession
from mcp.types import (
  CallToolRequest,
  ClientCapabilities,
  CompleteRequest,
  GetPromptRequest,
  ListPromptsRequest,
  ListResourceTemplatesRequest,
  ListResourcesRequest,
  ListToolsRequest,
  LoggingLevel,
  ReadResourceRequest,
  Implementation,
)
from . import _silence_sse_noise  # Import for side effects (patching)  # noqa: F401
from mcp.client.sse import sse_client
from mcp.client.streamable_http import streamablehttp_client
from contextlib import suppress


try:
  import anyio
except ImportError:  # pragma: no cover
  anyio = None  # type: ignore[assignment]

T = TypeVar("T")

logger = logging.getLogger("metorial.mcp.client")

def _log_info(message, **kwargs):
  """Conditionally log info messages only if debug logging is enabled."""
  if logger.isEnabledFor(logging.DEBUG):
    logger.info(message, **kwargs)


@dataclass
class RequestOptions:
  timeout: Optional[float] = None
  metadata: Optional[Dict[str, Any]] = None


class MetorialMcpClient:
  def __init__(
    self,
    *,
    session: ClientSession,
    transport_closer: Callable[[], Awaitable[None]],
    default_timeout: Optional[float] = 60.0,
  ) -> None:
    self._session = session
    self._transport_closer = transport_closer
    self._closed = False
    self._default_timeout = default_timeout
    logger.debug("MetorialMcpClient instantiated default_timeout=%s", default_timeout)

  @classmethod
  async def create(
    cls,
    session: Any,  # real Metorial session type
    *,
    host: str,
    deployment_id: str,
    client_name: Optional[str] = None,
    client_version: Optional[str] = None,
    use_sse: bool = True,
    use_http_stream: bool = False,
    connect_timeout: float = 30.0,
    read_timeout: float = 60.0,
    handshake_timeout: float = 3.0,
    extra_query: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
    log_raw_messages: bool = False,
    raw_message_logger: Optional[Callable[[str], None]] = None,
  ) -> "MetorialMcpClient":
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
    def _build_cm():
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
    headers: Optional[Dict[str, str]] = None,
    log_raw_messages: bool = False,
    raw_message_logger: Optional[Callable[[str], None]] = None,
  ) -> "MetorialMcpClient":
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

  async def __aenter__(self) -> "MetorialMcpClient":
    logger.debug("__aenter__")
    return self

  async def __aexit__(self, exc_type, exc, tb) -> None:
    logger.debug("__aexit__")
    await self.close()

  async def _with_timeout(
    self, coro: Awaitable[T], options: Optional[RequestOptions]
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

  async def register_capabilities(self, caps: ClientCapabilities) -> Any:
    self._ensure_open()
    logger.debug("register_capabilities caps=%s", caps)
    return await self._session.register_capabilities(caps)  # type: ignore[attr-defined]

  def get_server_capabilities(self) -> Any:
    caps = self._session.get_server_capabilities()  # type: ignore[attr-defined]
    logger.debug("get_server_capabilities -> %s", caps)
    if caps is None:
      raise RuntimeError("Server capabilities not available")
    return caps

  def get_server_version(self) -> Any:
    version = self._session.get_server_version()  # type: ignore[attr-defined]
    logger.debug("get_server_version -> %s", version)
    if version is None:
      raise RuntimeError("Server version not available")
    return version

  def get_instructions(self) -> Any:
    instr = self._session.get_instructions()  # type: ignore[attr-defined]
    logger.debug("get_instructions -> %s", instr)
    return instr

  async def complete(
    self,
    params: CompleteRequest,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("complete params=%s options=%s", params, options)
    return await self._with_timeout(self._session.complete(**params), options)  # type: ignore[arg-type]

  async def set_logging_level(
    self, level: LoggingLevel, options: Optional[RequestOptions] = None
  ) -> Any:
    self._ensure_open()
    logger.debug("set_logging_level level=%s options=%s", level, options)
    return await self._with_timeout(self._session.set_logging_level(level), options)

  async def get_prompt(
    self,
    params: GetPromptRequest,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("get_prompt params=%s options=%s", params, options)
    return await self._with_timeout(self._session.get_prompt(**params), options)  # type: ignore[arg-type]

  async def list_prompts(
    self,
    params: Optional[ListPromptsRequest] = None,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_prompts params=%s options=%s", params, options)
    return await self._with_timeout(
      self._session.list_prompts(**(params or {})), options
    )

  async def list_resources(
    self,
    params: Optional[ListResourcesRequest] = None,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_resources params=%s options=%s", params, options)
    return await self._with_timeout(
      self._session.list_resources(**(params or {})), options
    )

  async def list_resource_templates(
    self,
    params: Optional[ListResourceTemplatesRequest] = None,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_resource_templates params=%s options=%s", params, options)
    return await self._with_timeout(
      self._session.list_resource_templates(**(params or {})), options
    )

  async def read_resource(
    self,
    params: ReadResourceRequest,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("read_resource params=%s options=%s", params, options)
    return await self._with_timeout(self._session.read_resource(**params), options)  # type: ignore[arg-type]

  async def call_tool(
    self,
    params: CallToolRequest,
    result_validator: Optional[Callable[[Any], None]] = None,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug(
      "call_tool name=%s args=%s options=%s",
      params.get("name"),  # type: ignore[attr-defined]
      params.get("arguments"),  # type: ignore[attr-defined]
      options,
    )

    call_result = self._session.call_tool(
      params["name"], arguments=params.get("arguments")  # type: ignore[index,attr-defined]
    )  # noqa: F821
    logger.debug(
      "_session.call_tool returned: %s (type: %s)", call_result, type(call_result)
    )

    # The MCP library's call_tool method returns a coroutine, so we need to await it
    if asyncio.iscoroutine(call_result):
      result = await call_result
      logger.debug("Awaited call_result: %s", result)
    else:
      result = call_result  # type: ignore[unreachable]
      logger.debug("Using call_result directly: %s", result)
    if result_validator is not None:
      try:
        result_validator(result)
      except Exception:
        logger.exception("Result validator failed")
        raise
    return result

  async def list_tools(
    self,
    params: Optional[ListToolsRequest] = None,
    options: Optional[RequestOptions] = None,
  ) -> Any:
    self._ensure_open()
    logger.debug("list_tools params=%s options=%s", params, options)
    return await self._with_timeout(self._session.list_tools(**(params or {})), options)

  async def send_roots_list_changed(
    self, options: Optional[RequestOptions] = None
  ) -> Any:
    self._ensure_open()
    logger.debug("send_roots_list_changed options=%s", options)
    return await self._with_timeout(self._session.send_roots_list_changed(), options)

  async def close(self) -> None:
    if self._closed:
      return
    self._closed = True
    with suppress(Exception):
      aexit_result = self._session.__aexit__(None, None, None)
      if asyncio.iscoroutine(aexit_result):
        await aexit_result
      # If it's not a coroutine, it might be a dictionary or other value, just ignore it
    with suppress(Exception):
      transport_result = self._transport_closer()
      if asyncio.iscoroutine(transport_result):
        await transport_result
      # If it's not a coroutine, it might be a dictionary or other value, just ignore it

  def close_sync(self) -> None:
    try:
      loop = asyncio.get_running_loop()
    except RuntimeError:
      asyncio.run(self.close())
    else:
      loop.run_until_complete(self.close())


class _LoggingRecvStream:
  def __init__(self, inner: Any, logger_fn):
    self._inner = inner
    self._log = logger_fn

  async def receive(self):
    msg = await self._inner.receive()
    self._log(f"<- {msg}")
    return msg

  # delegate everything else (aclose, __aenter__, __aexit__, etc.)
  def __getattr__(self, name):
    return getattr(self._inner, name)


class _LoggingSendStream:
  def __init__(self, inner: Any, logger_fn):
    self._inner = inner
    self._log = logger_fn

  async def send(self, msg):
    self._log(f"-> {msg}")
    return await self._inner.send(msg)

  def __getattr__(self, name):
    return getattr(self._inner, name)


def wrap_streams_with_logging(read_stream, write_stream, logger_fn):
  return _LoggingRecvStream(read_stream, logger_fn), _LoggingSendStream(
    write_stream, logger_fn
  )
