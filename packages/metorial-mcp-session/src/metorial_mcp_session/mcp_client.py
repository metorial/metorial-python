from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from datetime import timedelta
from typing import Any, Awaitable, Callable, Dict, Optional, Tuple, TypeVar, List
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
from ._silence_sse_noise import *
from mcp.client.sse import sse_client
from mcp.client.streamable_http import streamablehttp_client

import truststore; truststore.inject_into_ssl()
from contextlib import suppress

import requests
import json

def create_session(
    *,
    api_key: str,
    api_host: str,
    server_deployment_ids: List[str],
    client_name: str = "metorial-python",
    client_version: str = "0.1.0",
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "server_deployment_ids": server_deployment_ids,
        "client": {"name": client_name, "version": client_version},
    }
    if metadata:
        body["metadata"] = metadata

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = f"{api_host.rstrip('/')}/sessions"
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    if resp.status_code >= 400:
        raise RuntimeError(f"Session create failed: {resp.status_code} {resp.text}")
    return resp.json()

try:
    import anyio
except ImportError:  # pragma: no cover
    anyio = None

T = TypeVar("T")

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
logger = logging.getLogger("metorial.mcp.client")


@dataclass
class RequestOptions:
    timeout: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None


class MetorialMcpClient:
    """Python analogue of the Node MetorialMcpClient."""

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

    # ------------------------------------------------------------------
    # Factories
    # ------------------------------------------------------------------

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
        """Create and connect a client.

        Parameters of note:
          - handshake_timeout: seconds to wait for `initialize()`.
          - log_raw_messages/raw_message_logger: wrap read/write to trace JSON-RPC payloads.
          - use_http_stream: set True to try the HTTP streaming transport instead of SSE.
        """
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

        logger.info(
            "Connecting to MCP endpoint",
            extra={"url": url, "deployment_id": deployment_id, "session_id": session.id},
        )
        if headers:
            logger.debug("Custom headers set: %s", list(headers.keys()))

        # Pick transport
        if use_http_stream:
            cm = streamablehttp_client(url=url, timeout=connect_timeout, headers=headers)
        elif use_sse:
            cm = sse_client(url=url, timeout=connect_timeout, headers=headers)
        else:  # pragma: no cover
            raise NotImplementedError("Only SSE or HTTP stream transports are supported.")

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
            logger.info("MCP session initialized")
        except Exception:
            logger.exception("Initialize failed, cleaning up")
            await session_cm.__aexit__(None, None, None)
            await transport_closer()
            raise

        return cls(session=session_cm, transport_closer=transport_closer, default_timeout=read_timeout)

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
        session_cm = ClientSession(read, write, client_info=client_info, read_timeout_seconds=timedelta(seconds=read_timeout))
        await session_cm.__aenter__()
        try:
            await asyncio.wait_for(session_cm.initialize(), timeout=handshake_timeout)
        except Exception:
            await session_cm.__aexit__(None, None, None)
            await transport_closer()
            raise
        return cls(session=session_cm, transport_closer=transport_closer, default_timeout=read_timeout)

    # ------------------------------------------------------------------
    # Context manager
    # ------------------------------------------------------------------

    async def __aenter__(self) -> "MetorialMcpClient":
        logger.debug("__aenter__")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        logger.debug("__aexit__")
        await self.close()

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    async def _with_timeout(self, coro: Awaitable[T], options: Optional[RequestOptions]) -> T:
        timeout = options.timeout if options and options.timeout is not None else self._default_timeout
        if timeout is None:
            return await coro
        return await asyncio.wait_for(coro, timeout)


    def _ensure_open(self) -> None:
        if self._closed:
            logger.error("Operation on closed client")
            raise RuntimeError("MetorialMcpClient is closed")

    # ------------------------------------------------------------------
    # RPC wrappers
    # ------------------------------------------------------------------

    async def register_capabilities(self, caps: ClientCapabilities) -> Any:
        self._ensure_open()
        logger.debug("register_capabilities caps=%s", caps)
        return await self._session.register_capabilities(caps)

    def get_server_capabilities(self) -> Any:
        caps = self._session.get_server_capabilities()
        logger.debug("get_server_capabilities -> %s", caps)
        if caps is None:
            raise RuntimeError("Server capabilities not available")
        return caps

    def get_server_version(self) -> Any:
        version = self._session.get_server_version()
        logger.debug("get_server_version -> %s", version)
        if version is None:
            raise RuntimeError("Server version not available")
        return version

    def get_instructions(self) -> Any:
        instr = self._session.get_instructions()
        logger.debug("get_instructions -> %s", instr)
        return instr

    async def complete(self, params: CompleteRequest["params"], options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("complete params=%s options=%s", params, options)
        return await self._with_timeout(self._session.complete(**params), options)

    async def set_logging_level(self, level: LoggingLevel, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("set_logging_level level=%s options=%s", level, options)
        return await self._with_timeout(self._session.set_logging_level(level), options)

    async def get_prompt(self, params: GetPromptRequest["params"], options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("get_prompt params=%s options=%s", params, options)
        return await self._with_timeout(self._session.get_prompt(**params), options)

    async def list_prompts(self, params: Optional[ListPromptsRequest["params"]] = None, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("list_prompts params=%s options=%s", params, options)
        return await self._with_timeout(self._session.list_prompts(**(params or {})), options)

    async def list_resources(self, params: Optional[ListResourcesRequest["params"]] = None, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("list_resources params=%s options=%s", params, options)
        return await self._with_timeout(self._session.list_resources(**(params or {})), options)

    async def list_resource_templates(self, params: Optional[ListResourceTemplatesRequest["params"]] = None, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("list_resource_templates params=%s options=%s", params, options)
        return await self._with_timeout(self._session.list_resource_templates(**(params or {})), options)

    async def read_resource(self, params: ReadResourceRequest["params"], options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("read_resource params=%s options=%s", params, options)
        return await self._with_timeout(self._session.read_resource(**params), options)

    async def call_tool(
        self,
        params: CallToolRequest["params"],
        result_validator: Optional[Callable[[Any], None]] = None,
        options: Optional[RequestOptions] = None,
    ) -> Any:
        self._ensure_open()
        logger.debug("call_tool name=%s args=%s options=%s", params.get("name"), params.get("arguments"), options)
        result = await self._with_timeout(
            self._session.call_tool(params["name"], arguments=params.get("arguments")), options
        )
        if result_validator is not None:
            try:
                result_validator(result)
            except Exception:
                logger.exception("Result validator failed")
                raise
        return result

    async def list_tools(self, params: Optional[ListToolsRequest["params"]] = None, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("list_tools params=%s options=%s", params, options)
        return await self._with_timeout(self._session.list_tools(**(params or {})), options)

    async def send_roots_list_changed(self, options: Optional[RequestOptions] = None) -> Any:
        self._ensure_open()
        logger.debug("send_roots_list_changed options=%s", options)
        return await self._with_timeout(self._session.send_roots_list_changed(), options)

    # ------------------------------------------------------------------
    # Teardown
    # ------------------------------------------------------------------

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        with suppress(Exception):
            await self._session.__aexit__(None, None, None)
        with suppress(Exception):
            await self._transport_closer()


    def close_sync(self) -> None:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            asyncio.run(self.close())
        else:
            loop.run_until_complete(self.close())


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

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
    return _LoggingRecvStream(read_stream, logger_fn), _LoggingSendStream(write_stream, logger_fn)