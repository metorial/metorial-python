"""
Magnetar MCP session class.

Uses providers instead of server_deployments, connectionUrl instead of clientSecret,
and MetorialMcpClient.from_url() for direct URL connection.
"""

from __future__ import annotations

import asyncio
import contextlib
import logging
from typing import TYPE_CHECKING, Any, Protocol, TypedDict

from .mcp_client import MetorialMcpClient
from .mcp_tool import Capability, ResourceTemplate, Tool

if TYPE_CHECKING:
  from .mcp_tool_manager import MetorialMcpToolManager

logger = logging.getLogger(__name__)


def _should_log_debug() -> bool:
  return logger.isEnabledFor(logging.DEBUG)


def _log_info(message: str) -> None:
  if _should_log_debug():
    logger.info(message)


class _ClientInfo(TypedDict, total=False):
  name: str
  version: str


class MagnetarMcpSessionInit(TypedDict, total=False):
  providers: list[dict[str, Any] | str]
  client: _ClientInfo
  metadata: dict[str, Any]
  session_template: str


class _SDKConfig(TypedDict, total=False):
  apiHost: str
  mcpHost: str
  apiKey: str


class _MagnetarSessionsAPI(Protocol):
  def create(self, **kwargs: Any) -> Any: ...


class _MagnetarSessionTemplatesProvidersAPI(Protocol):
  def list(self, session_template_id: str, **kwargs: Any) -> Any: ...


class _MagnetarSessionTemplatesAPI(Protocol):
  @property
  def providers(self) -> _MagnetarSessionTemplatesProvidersAPI: ...


class MagnetarCoreSDK(Protocol):
  @property
  def _config(self) -> _SDKConfig: ...

  @property
  def magnetar_sessions(self) -> _MagnetarSessionsAPI | None: ...

  @property
  def session_templates(self) -> _MagnetarSessionTemplatesAPI | None: ...


class MetorialMagnetarMcpSession:
  """Magnetar MCP session class. Uses providers and connectionUrl."""

  def __init__(
    self,
    sdk: MagnetarCoreSDK,
    init: MagnetarMcpSessionInit,
  ) -> None:
    self._sdk = sdk
    self._init = init
    self._session: dict[str, Any] | None = None
    self._client_promises: dict[str, asyncio.Task[MetorialMcpClient]] = {}

    # Extract client info
    client_info = init.get("client", {})
    self.client_info = {
      "name": client_info.get("name", "metorial-python"),
      "version": client_info.get("version", "1.0.0"),
    }

  @property
  def _mcp_host(self) -> str:
    """Derive Magnetar MCP host from config."""
    config = self._sdk._config
    mcp_host = config.get("mcpHost")
    if mcp_host:
      return mcp_host
    api_host = config.get("apiHost", "https://api.metorial.com")
    return api_host.replace("://api.", "://connect.")

  def get_session(self) -> dict[str, Any]:
    if self._session is not None:
      return self._session

    providers_input = self._init.get("providers", [])
    session_template = self._init.get("session_template")

    # If session_template is set, resolve providers from it
    if session_template and not providers_input:
      try:
        st_api = self._sdk.session_templates
        if st_api is not None:
          template_providers = st_api.providers.list(
            session_template_id=session_template
          )
          items = (
            template_providers.items
            if hasattr(template_providers, "items")
            else template_providers
          )
          providers_input = [
            {
              "provider_deployment": item.provider_deployment_id
              if hasattr(item, "provider_deployment_id")
              else item["provider_deployment_id"],
              "session_template_id": session_template,
            }
            for item in items
          ]
      except Exception as e:
        logger.warning(f"Failed to resolve session template providers: {e}")

    # Normalize providers for API payload
    providers_list: list[dict[str, Any]] = []
    for prov in providers_input:
      if isinstance(prov, dict):
        providers_list.append(prov)
      else:
        # String ID - wrap as provider_deployment
        providers_list.append({"provider_deployment": prov})

    api_payload: dict[str, Any] = {
      "providers": providers_list,
    }
    if "metadata" in self._init:
      api_payload["metadata"] = self._init["metadata"]

    _log_info(f"Creating Magnetar session with API payload: {api_payload}")
    try:
      sessions_api = self._sdk.magnetar_sessions
      if sessions_api is None:
        raise RuntimeError("SDK Magnetar sessions API is not initialized")

      # Try to use the endpoint manager directly for the raw JSON response,
      # because the generated mapper incorrectly maps 'provider_deployments'
      # instead of 'providers' from the API response.
      raw_response: dict[str, Any] | None = None
      try:
        from metorial._endpoint import MetorialRequest

        root = getattr(sessions_api, "_root", None)
        base = getattr(root, "_base", None) if root is not None else None
        manager = getattr(base, "manager", None) if base is not None else None
        if manager is None:
          raise AttributeError("Cannot access endpoint manager")
        request = MetorialRequest(path=["sessions"], body=api_payload)
        raw_response = manager._request("POST", request)
        logger.debug(
          f"Session raw response keys: {list(raw_response.keys()) if isinstance(raw_response, dict) else type(raw_response)}"
        )
      except (AttributeError, ImportError):
        # Fall back to typed API (e.g., in tests with fake APIs)
        pass

      if raw_response is not None:
        session_id = raw_response["id"]
        connection_url = raw_response.get("connection_url")

        # The API returns 'providers' with nested 'deployment' objects
        raw_providers = raw_response.get("providers", [])
        provider_deployments = []
        for prov in raw_providers:
          deployment = prov.get("deployment") if isinstance(prov, dict) else None
          if deployment and isinstance(deployment, dict) and deployment.get("id"):
            provider_deployments.append(
              {
                "id": deployment["id"],
                "provider_deployment_id": deployment["id"],
              }
            )
      else:
        # Fallback: use the typed API (may have empty provider_deployments
        # due to mapper bug, but works for tests/mocks)
        session_response = sessions_api.create(**api_payload)
        if isinstance(session_response, dict):
          session_id = session_response["id"]
          connection_url = session_response.get("connection_url")
          raw_deps = session_response.get("provider_deployments", [])
        else:
          session_id = session_response.id
          connection_url = session_response.connection_url
          raw_deps = session_response.provider_deployments or []

        provider_deployments = []
        for dep in raw_deps:
          dep_id = dep["id"] if isinstance(dep, dict) else dep.id
          dep_pdid = (
            dep.get("provider_deployment_id")
            if isinstance(dep, dict)
            else getattr(dep, "provider_deployment_id", None)
          )
          provider_deployments.append(
            {
              "id": dep_id,
              "provider_deployment_id": dep_pdid or dep_id,
            }
          )

      self._session = {
        "id": session_id,
        "connection_url": connection_url,
        "provider_deployments": provider_deployments,
      }
      _log_info(f"Magnetar session created: {self._session.get('id', 'unknown')}")
    except Exception as e:
      logger.error(f"Failed to create Magnetar session: {e}")
      raise

    return self._session

  def get_server_deployments(self) -> list[dict[str, Any]]:
    """Get provider deployments (aliased for compatibility with session interface)."""
    ses = self.get_session()
    result = ses.get("provider_deployments", [])
    return result if isinstance(result, list) else []

  async def get_capabilities(self) -> list[Capability]:
    """Get capabilities via direct MCP tool discovery (no capabilities API in Magnetar)."""
    return await self._get_tools_via_direct_mcp()

  async def get_tool_manager(self) -> MetorialMcpToolManager:
    from .mcp_tool_manager import MetorialMcpToolManager

    _log_info("Getting capabilities for Magnetar tool manager...")

    from metorial.exceptions import (
      AuthenticationError,
      NotFoundError,
      OAuthRequiredError,
    )

    critical_error: Exception | None = None

    try:
      caps = await self.get_capabilities()
      _log_info(f"Got {len(caps)} capabilities from direct MCP")

      if caps:
        return await MetorialMcpToolManager.from_capabilities(self, caps)
      else:
        logger.debug("Direct MCP returned empty capabilities")

    except (AuthenticationError, NotFoundError, OAuthRequiredError):
      raise
    except Exception as e:
      critical_error = e
      logger.warning(f"Warning: Direct MCP discovery failed: {e}")

    if critical_error is not None:
      raise critical_error

    logger.warning("Warning: No capabilities found, returning empty tool manager")
    return await MetorialMcpToolManager.from_capabilities(self, [])

  async def _get_tools_via_direct_mcp(self) -> list[Capability]:
    """Get capabilities via direct MCP connection using connectionUrl."""
    _log_info("Starting Magnetar direct MCP tool discovery...")

    def _normalize_tool(raw_tool: object) -> Tool | None:
      if isinstance(raw_tool, dict):
        name_value = raw_tool.get("name")
        description_value = raw_tool.get("description")
        input_schema_value = raw_tool.get("inputSchema")
      else:
        name_value = getattr(raw_tool, "name", None)
        description_value = getattr(raw_tool, "description", None)
        input_schema_value = getattr(raw_tool, "inputSchema", None)

      if not isinstance(name_value, str) or not name_value:
        return None

      normalized_tool: Tool = {"name": name_value}
      if isinstance(description_value, str):
        normalized_tool["description"] = description_value
      if isinstance(input_schema_value, dict):
        normalized_tool["inputSchema"] = input_schema_value
      return normalized_tool

    def _normalize_resource_template(raw_template: object) -> ResourceTemplate | None:
      if isinstance(raw_template, dict):
        name_value = raw_template.get("name")
        description_value = raw_template.get("description")
        uri_template_value = raw_template.get("uriTemplate")
      else:
        name_value = getattr(raw_template, "name", None)
        description_value = getattr(raw_template, "description", None)
        uri_template_value = getattr(raw_template, "uriTemplate", None)

      if not isinstance(name_value, str) or not name_value:
        return None
      if not isinstance(uri_template_value, str) or not uri_template_value:
        return None

      normalized_template: ResourceTemplate = {
        "name": name_value,
        "uriTemplate": uri_template_value,
      }
      if isinstance(description_value, str):
        normalized_template["description"] = description_value
      return normalized_template

    capabilities: list[Capability] = []
    deployments = self.get_server_deployments()

    for deployment in deployments:
      deployment_id = deployment["id"]
      tools: list[Tool] = []
      resource_templates: list[ResourceTemplate] = []

      # Get client via connectionUrl
      try:
        _log_info(f"Connecting to MCP for deployment: {deployment_id}")
        client = await self.get_client({"deploymentId": deployment_id})
      except Exception as e:
        logger.warning(f"Warning: Failed to get client for {deployment_id}: {e}")
        continue

      # Get tools
      try:
        tools_response = await client.list_tools()
        raw_tools: object
        if hasattr(tools_response, "tools"):
          raw_tools = tools_response.tools
        elif isinstance(tools_response, dict):
          raw_tools = tools_response.get("tools", [])
        else:
          raw_tools = []

        if isinstance(raw_tools, list):
          for raw_tool in raw_tools:
            normalized_tool = _normalize_tool(raw_tool)
            if normalized_tool is not None:
              tools.append(normalized_tool)

        _log_info(f"Direct MCP found {len(tools)} tools for {deployment_id}")
      except Exception as e:
        logger.warning(f"Warning: Failed to get tools for {deployment_id}: {e}")

      # Get resource templates
      try:
        templates_response = await client.list_resource_templates()
        raw_templates: object
        if hasattr(templates_response, "resourceTemplates"):
          raw_templates = templates_response.resourceTemplates or []
        elif hasattr(templates_response, "resource_templates"):
          raw_templates = templates_response.resource_templates or []
        elif isinstance(templates_response, dict):
          raw_templates = templates_response.get(
            "resourceTemplates"
          ) or templates_response.get("resource_templates", [])
        else:
          raw_templates = []

        if isinstance(raw_templates, list):
          for raw_template in raw_templates:
            normalized_template = _normalize_resource_template(raw_template)
            if normalized_template is not None:
              resource_templates.append(normalized_template)
      except Exception as e:
        logger.debug(
          f"Warning: Failed to get resource templates for {deployment_id}: {e}"
        )

      # Build capabilities
      for tool in tools:
        capabilities.append(
          {
            "type": "tool",
            "tool": tool,
            "serverDeployment": {"id": deployment_id},
          }
        )

      for template in resource_templates:
        capabilities.append(
          {
            "type": "resource-template",
            "resourceTemplate": template,
            "serverDeployment": {"id": deployment_id},
          }
        )

    _log_info(
      f"Magnetar MCP discovery completed: {len(capabilities)} total capabilities"
    )
    return capabilities

  async def get_client(self, opts: dict[str, str]) -> MetorialMcpClient:
    dep_id = opts["deploymentId"]

    if dep_id not in self._client_promises:

      async def _create_client() -> MetorialMcpClient:
        try:
          ses = self.get_session()
          connection_url = ses.get("connection_url")

          if not connection_url:
            # Construct URL from mcp_host + session ID
            session_id = ses.get("id")
            if session_id:
              connection_url = f"{self._mcp_host}/mcp/{session_id}"
            else:
              raise RuntimeError(
                "No connection_url in Magnetar session response. "
                "Ensure the session was created successfully."
              )

          # Add Bearer auth header
          api_key = self._sdk._config.get("apiKey", "")
          headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}

          # Use from_url for Magnetar - Streamable HTTP transport (v2)
          client = await MetorialMcpClient.from_url(
            connection_url,
            client_name=self.client_info["name"],
            client_version=self.client_info["version"],
            handshake_timeout=30.0,
            headers=headers,
            use_http_stream=True,
          )
          return client
        except Exception as e:
          if dep_id in self._client_promises:
            del self._client_promises[dep_id]
          raise e

      self._client_promises[dep_id] = asyncio.create_task(_create_client())

    try:
      return await self._client_promises[dep_id]
    except Exception as e:
      if dep_id in self._client_promises:
        task = self._client_promises[dep_id]
        if not task.done():
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
            await task
        del self._client_promises[dep_id]
      raise e

  async def close(self) -> None:
    close_tasks = []
    for client_promise in list(self._client_promises.values()):
      if client_promise.done() and not client_promise.cancelled():
        try:
          client = client_promise.result()
          close_tasks.append(client.close())
        except Exception:
          continue

    if close_tasks:
      try:
        await asyncio.wait_for(
          asyncio.gather(*close_tasks, return_exceptions=True), timeout=5.0
        )
      except asyncio.TimeoutError:
        logger.debug("Magnetar MCP session close timeout - continuing cleanup")
      except Exception as e:
        logger.debug(f"Magnetar MCP session close warning: {e}")

    self._client_promises.clear()
