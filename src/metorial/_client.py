import asyncio
import contextlib
from collections.abc import Awaitable, Callable
from contextlib import AbstractContextManager
from types import TracebackType
from typing import TYPE_CHECKING, Any, Literal, cast

from metorial._base import MetorialBase
from metorial._client_core import ClientCoreMixin
from metorial._session import MetorialSession
from metorial.exceptions import MetorialAPIError
from metorial.mcp.mcp_session import MetorialCoreSDK

if TYPE_CHECKING:
  from metorial._protocols import ToolManagerProtocol

# Provider type literals
ProviderType = Literal[
  "anthropic", "openai", "google", "mistral", "deepseek", "xai", "togetherai"
]


class ProviderSession:
  """Async context manager for provider-specific sessions.

  Provides a Pythonic interface with attribute access to tools and call_tools.

  Example:
      async with metorial.provider_session(
          provider="anthropic",
          server_deployments=[deployment_id]
      ) as session:
          tools = session.tools
          result = await session.call_tools(tool_calls)
  """

  def __init__(
    self,
    metorial: "Metorial",
    provider: ProviderType,
    server_deployments: list[str | dict[str, Any]],
  ) -> None:
    self._metorial = metorial
    self._provider = provider
    self._server_deployments = server_deployments
    self._session: MetorialSession | None = None
    self._tool_manager: ToolManagerProtocol | None = None
    self._tools: list[dict[str, Any]] = []
    self._call_tools_fn: Callable[..., Awaitable[Any]] | None = None
    self._closed = False

  def _check_closed(self) -> None:
    """Raise an error if the session has been closed."""
    if self._closed:
      raise RuntimeError(
        "Cannot use session after it has been closed. "
        "Use 'async with metorial.provider_session(...) as session:' "
        "and keep operations inside the context manager."
      )

  @property
  def tools(self) -> list[dict[str, Any]]:
    """Get tools formatted for the provider."""
    self._check_closed()
    return self._tools

  @property
  def tool_manager(self) -> "ToolManagerProtocol | None":
    """Get the underlying tool manager."""
    self._check_closed()
    return self._tool_manager

  async def call_tools(self, tool_calls: list[Any]) -> Any:
    """Execute tool calls and return provider-formatted results."""
    self._check_closed()
    if self._call_tools_fn is None:
      raise RuntimeError("Session not initialized. Use 'async with' context manager.")
    return await self._call_tools_fn(tool_calls)

  async def call_tool(self, tool_name: str, kwargs: dict[str, Any]) -> Any:
    """Execute a single tool by name.

    Args:
        tool_name: Name of the tool to execute
        kwargs: Arguments to pass to the tool

    Returns:
        Tool result with 'content' key containing the result
    """
    self._check_closed()
    if self._tool_manager is None:
      raise RuntimeError("Session not initialized. Use 'async with' context manager.")
    # Filter out None values
    filtered_kwargs = {k: v for k, v in kwargs.items() if v is not None}
    return await self._tool_manager.execute_tool(tool_name, filtered_kwargs)

  def get_tools(self) -> list[dict[str, Any]]:
    """Get tools formatted for the provider.

    This is an alias for the `tools` property for API compatibility.
    """
    self._check_closed()
    return self._tools

  async def __aenter__(self) -> "ProviderSession":
    """Initialize the session and load tools."""
    # Normalize server deployments (accept both snake_case and camelCase)
    normalized: list[dict[str, Any]] = []
    for dep in self._server_deployments:
      if isinstance(dep, str):
        normalized.append({"id": dep})
      elif isinstance(dep, dict):
        # Accept snake_case (Pythonic) or camelCase (JS compat)
        dep_id = (
          dep.get("id")
          or dep.get("server_deployment_id")
          or dep.get("serverDeploymentId")
        )
        norm_dep: dict[str, Any] = {"id": dep_id}

        # Handle oauth_session_id (snake_case) or oauthSessionId (camelCase)
        oauth_session_id = dep.get("oauth_session_id") or dep.get("oauthSessionId")
        if oauth_session_id:
          norm_dep["oauthSessionId"] = oauth_session_id

        normalized.append(norm_dep)

    # Create session
    self._session = self._metorial.create_mcp_session({"serverDeployments": normalized})

    # Get tool manager
    self._tool_manager = await self._session.get_tool_manager()

    # Build provider-specific tools and call_tools function
    if self._provider == "anthropic":
      from metorial.providers.anthropic import (
        build_anthropic_tools,
        call_anthropic_tools,
      )

      self._tools = build_anthropic_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_anthropic_tools(self._tool_manager, tc)

    elif self._provider == "openai":
      from metorial.providers.openai import build_openai_tools, call_openai_tools

      self._tools = build_openai_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_openai_tools(self._tool_manager, tc)

    elif self._provider == "google":
      from metorial.providers.google import build_google_tools, call_google_tools

      self._tools = build_google_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_google_tools(self._tool_manager, tc)

    elif self._provider == "mistral":
      from metorial.providers.mistral import build_mistral_tools, call_mistral_tools

      self._tools = build_mistral_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_mistral_tools(self._tool_manager, tc)

    elif self._provider == "deepseek":
      from metorial.providers.deepseek import build_deepseek_tools, call_deepseek_tools

      self._tools = build_deepseek_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_deepseek_tools(self._tool_manager, tc)

    elif self._provider == "xai":
      from metorial.providers.xai import build_xai_tools, call_xai_tools

      self._tools = build_xai_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_xai_tools(self._tool_manager, tc)

    elif self._provider == "togetherai":
      from metorial.providers.togetherai import (
        build_togetherai_tools,
        call_togetherai_tools,
      )

      self._tools = build_togetherai_tools(self._tool_manager)
      self._call_tools_fn = lambda tc: call_togetherai_tools(self._tool_manager, tc)

    else:
      raise ValueError(f"Unknown provider: {self._provider}")

    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: TracebackType | None,
  ) -> None:
    """Clean up the session."""
    self._closed = True
    if self._session is not None:
      with contextlib.suppress(Exception):
        await self._session.close()
    # Also close the metorial client
    with contextlib.suppress(Exception):
      await self._metorial.close()


class Metorial(ClientCoreMixin, MetorialBase):
  def session(
    self,
    server_deployments: str | list[str | dict[str, Any]],
  ) -> MetorialSession:
    """Create a session for use with async context manager.

    Args:
        server_deployments: Server deployment ID(s). Can be:
            - A single deployment ID string
            - A list of deployment ID strings
            - A list of deployment config dicts (for OAuth, etc)

    Returns:
        MetorialSession for use with `async with`

    Example:
        async with metorial.session("deployment-id") as session:
            tool_manager = await session.get_tool_manager()
            tools = tool_manager.get_tools_for_openai()
    """
    init: dict[str, Any]
    if isinstance(server_deployments, str):
      init = {"serverDeployments": [server_deployments]}
    elif isinstance(server_deployments, list):
      # Check if it's a list of strings or list of dicts
      if server_deployments and isinstance(server_deployments[0], str):
        init = {"serverDeployments": server_deployments}
      else:
        # List of dicts - normalize the keys
        normalized = []
        for d in server_deployments:
          if isinstance(d, dict):
            dep: dict[str, Any] = {"id": d.get("id") or d.get("serverDeploymentId")}
            for k, v in d.items():
              if k not in ("id", "serverDeploymentId"):
                dep[k] = v
            normalized.append(dep)
        init = {"serverDeployments": normalized}

    return self.create_mcp_session(init)

  def provider_session(
    self,
    provider: ProviderType,
    server_deployments: list[str | dict[str, Any]],
  ) -> ProviderSession:
    """Create a provider-specific session for use with async context manager.

    This is the recommended Pythonic way to use Metorial with LLM providers.

    Args:
        provider: The LLM provider type ("anthropic", "openai", "google", etc.)
        server_deployments: Server deployment ID(s). Can be:
            - A list of deployment ID strings
            - A list of deployment config dicts (for OAuth, etc)

    Returns:
        ProviderSession for use with `async with`

    Example:
        async with metorial.provider_session(
            provider="anthropic",
            server_deployments=[
                "deployment-id",
                {"serverDeploymentId": "oauth-deployment", "oauthSessionId": "session-id"},
            ]
        ) as session:
            tools = session.tools
            response = await anthropic.messages.create(tools=tools, ...)
            result = await session.call_tools(tool_calls)
    """
    return ProviderSession(self, provider, server_deployments)

  async def create_mcp_connection(self, init: dict[str, Any]) -> Any:
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

  async def with_session(
    self,
    init: dict[str, Any] | str | list[str],
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    if isinstance(init, str):
      init = {"serverDeployments": [init]}
    elif isinstance(init, list):
      init = {"serverDeployments": init}

    session = self.create_mcp_session(init)
    try:
      return await action(session)
    except Exception as e:
      self.logger.error(f"Session action failed: {e}")
      raise

  async def with_provider_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: dict[str, Any] | str | list[str],
    action: Callable[[dict[str, Any]], Any],
  ) -> Any:
    if isinstance(init, str):
      init = {"serverDeployments": [init]}
    elif isinstance(init, list):
      init = {"serverDeployments": init}

    # Check if streaming mode is enabled
    streaming = init.get("streaming", False) if isinstance(init, dict) else False

    if streaming:
      return await self._with_streaming_session(provider, init, action)

    async def session_action(session: MetorialSession) -> Any:
      try:
        provider_data = await provider(session)

        simplified_session = {
          "tools": provider_data.get("tools"),
          "callTools": provider_data.get("callTools")
          or (lambda tool_calls: session.execute_tools(tool_calls)),
          "getToolManager": lambda: session.get_tool_manager(),
          "session": session,
          "closeSession": session.close
          if hasattr(session, "close")
          else lambda: session._mcp_session.close(),
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

        return await action(simplified_session)

      except Exception as e:
        self.logger.error(f"Error in provider session: {e}")
        raise

    # Automatically apply safe cleanup for provider sessions
    cleanup_context: AbstractContextManager[None]
    try:
      from metorial._safe_cleanup import (
        drain_pending_tasks,
      )
      from metorial._safe_cleanup import (
        quiet_asyncio_shutdown as _quiet_shutdown,
      )

      cleanup_context = _quiet_shutdown()
    except ImportError:
      from contextlib import nullcontext  # noqa: I001

      cleanup_context = nullcontext()

      async def drain_pending_tasks(timeout: float = 0.5) -> None:  # noqa: ARG001
        pass

    with cleanup_context:
      try:
        return await self.with_session(init, session_action)
      finally:
        # Ensure cleanup happens automatically
        await asyncio.create_task(self.close())
        await drain_pending_tasks(timeout=0.2)

  async def _with_streaming_session(
    self,
    provider: Callable[[MetorialSession], Any],
    init: dict[str, Any],
    action: Callable[[dict[str, Any]], Any],
  ) -> Any:
    """
    Streaming session that requires manual closeSession() call.
    Used when streaming: True is set in the init config.
    """
    session = self.create_mcp_session(init)
    session_closed = False

    async def close_session() -> None:
      nonlocal session_closed
      if not session_closed:
        session_closed = True
        self.logger.debug("[Metorial] Closing streaming session")
        if hasattr(session, "close"):
          await session.close()
        else:
          await session._mcp_session.close()
        await self.close()

    try:
      provider_data = await provider(session)

      simplified_session = {
        "tools": provider_data.get("tools"),
        "callTools": provider_data.get("callTools")
        or (lambda tool_calls: session.execute_tools(tool_calls)),
        "getToolManager": lambda: session.get_tool_manager(),
        "session": session,
        "closeSession": close_session,
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

      result = await action(simplified_session)

      # Safety timeout: close session after 30 seconds if user forgot
      async def safety_close() -> None:
        await asyncio.sleep(30)
        if not session_closed:
          self.logger.warning(
            "[Metorial] Streaming session not closed by user, closing automatically"
          )
          await close_session()

      asyncio.create_task(safety_close())

      return result

    except Exception as e:
      self.logger.error(f"Error in streaming session: {e}")
      if not session_closed:
        await close_session()
      raise

  async def with_oauth_session(
    self,
    oauth_session_id: str,
    deployment_id: str,
    action: Callable[[MetorialSession], Any],
  ) -> Any:
    import httpx

    try:
      self.logger.debug(
        f"Creating MCP session with OAuth authentication: {oauth_session_id}"
      )

      async with httpx.AsyncClient() as client:
        response = await client.post(
          f"{self._config['apiHost']}/sessions",
          headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._config['apiKey']}",
          },
          json={
            "server_deployments": [
              {
                "server_deployment_id": deployment_id,
                "oauth_session_id": oauth_session_id,
                "config": {},
              }
            ],
            "client": {"name": "metorial-python", "version": "1.0.0"},
          },
        )

        if response.status_code not in [200, 201]:
          self.logger.error(
            f"Failed to create session: {response.status_code} - {response.text}"
          )
          raise MetorialAPIError(
            f"Failed to create MCP session with OAuth: {response.status_code}"
          )

        session_data = response.json()
        self.logger.debug(f"✅ Created MCP session: {session_data.get('id')}")

      from metorial._session import SessionFactory
      from metorial.mcp import MetorialMcpSession

      mcp_init = {
        "serverDeployments": [deployment_id],
        "client": {"name": "metorial-python", "version": "1.0.0"},
      }

      from metorial.mcp import MetorialMcpSessionInit

      # Cast self to MetorialCoreSDK - the SDK is fully initialized at this point
      mcp_session = MetorialMcpSession(
        sdk=cast(MetorialCoreSDK, self), init=cast(MetorialMcpSessionInit, mcp_init)
      )
      mcp_session._session = session_data

      session = SessionFactory.create_session(mcp_session)

      return await action(session)

    except Exception as e:
      self.logger.error(f"OAuth session action failed: {e}")
      raise
    finally:
      if "session" in locals():
        try:
          await session.close()
        except Exception as e:
          self.logger.warning(f"Failed to close OAuth session: {e}")

  async def __aenter__(self) -> "Metorial":
    return self

  async def __aexit__(
    self,
    exc_type: type[BaseException] | None,
    exc_val: BaseException | None,
    exc_tb: Any,
  ) -> None:
    await self.close()
