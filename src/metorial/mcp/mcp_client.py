from __future__ import annotations

import asyncio
import contextlib
import logging
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, TypedDict, TypeVar

import mcp.types as mcp_types
from mcp import ClientSession
from mcp.types import (
  Implementation,
  LoggingLevel,
  PaginatedRequestParams,
  ServerCapabilities,
)
from pydantic import AnyUrl

from .transport import MetorialMcpTransport


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


T = TypeVar("T")

logger = logging.getLogger("metorial.mcp.client")


class MetorialClientSession(ClientSession):
  """ClientSession variant that preserves raw MCP tool results."""

  async def _validate_tool_result(
    self, name: str, result: mcp_types.CallToolResult
  ) -> None:
    logger.debug("Skipping MCP outputSchema validation for tool result: %s", name)
    return None


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
    use_http_stream: bool = False,
    log_raw_messages: bool = False,
    raw_message_logger: Any | None = None,
  ) -> MetorialMcpClient:
    """Directly connect using a full Streamable HTTP URL."""
    if not use_http_stream:
      raise NotImplementedError(
        "Pulsar/SSE transport is no longer supported. Use Streamable HTTP."
      )
    if log_raw_messages:
      logger.debug("Raw message logging is not supported on the owned transport.")
    if raw_message_logger is not None:
      logger.debug("Custom raw message logger is ignored on the owned transport.")

    transport = MetorialMcpTransport(
      url=url,
      headers=headers,
      connect_timeout=connect_timeout,
      read_timeout=read_timeout,
    )
    read, write = await transport.open()

    client_info = Implementation(name=client_name, version=client_version)
    session_cm = MetorialClientSession(
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
      await transport.close()
      raise

    return cls(
      session=session_cm,
      transport_closer=transport.close,
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
