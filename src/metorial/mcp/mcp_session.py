from __future__ import annotations

import asyncio
import contextlib
import logging
import types
from typing import TYPE_CHECKING, Any, Protocol, TypedDict

from metorial.exceptions import AuthenticationError, NotFoundError, OAuthRequiredError

from .mcp_client import MetorialMcpClient
from .mcp_tool import Capability

if TYPE_CHECKING:
  from .mcp_tool_manager import MetorialMcpToolManager

logger = logging.getLogger(__name__)


def _should_log_debug() -> bool:
  """Check if debug logging should be enabled by examining logger level."""
  return logger.isEnabledFor(logging.DEBUG)


def _log_info(message: str) -> None:
  """Conditionally log info messages only if debug logging is enabled."""
  if _should_log_debug():
    logger.info(message)


class _ServerDeploymentRequired(TypedDict):
  id: str


class _ServerDeployment(_ServerDeploymentRequired, total=False):
  """Server deployment config with optional OAuth session."""

  oauthSessionId: str
  serverDeploymentId: str  # Alternative key for id


class _ClientInfo(TypedDict, total=False):
  name: str
  version: str


# Use a flexible type for session init since deployments can be strings or dicts
ServerDeploymentInput = _ServerDeployment | str


class MetorialMcpSessionInit(TypedDict, total=False):
  serverDeployments: list[ServerDeploymentInput]
  client: _ClientInfo
  metadata: dict[str, Any]


class _SDKConfig(TypedDict, total=False):
  apiHost: str
  mcpHost: str
  apiKey: str


class _SessionsAPI(Protocol):
  """Protocol for sessions API - only requires create method."""

  def create(self, **kwargs: Any) -> Any:
    """Create a session. Returns object with id, server_deployments, client_secret."""
    ...


class _CapabilitiesAPI(Protocol):
  """Protocol for capabilities API - only requires list method."""

  def list(self, **kwargs: Any) -> Any:
    """List capabilities for given server deployment IDs."""
    ...


class _ServersAPI(Protocol):
  """Protocol for servers API - only requires capabilities sub-API."""

  @property
  def capabilities(self) -> _CapabilitiesAPI: ...


class MetorialCoreSDK(Protocol):
  """Protocol for the SDK interface used by MCP sessions.

  Defines the minimal interface needed for MCP session operations.
  Sessions and servers may be None during initialization but are
  expected to be set before MCP session operations are called.
  """

  @property
  def _config(self) -> _SDKConfig: ...

  @property
  def sessions(self) -> _SessionsAPI | None: ...

  @property
  def servers(self) -> _ServersAPI | None: ...


class _SessionResponse(TypedDict):
  id: str
  serverDeployments: list[dict[str, Any]]
  client_secret: dict[str, str]


class _MCPServer(TypedDict, total=False):
  id: str
  serverDeployment: dict[str, Any]
  server_deployment: dict[str, Any]  # snake_case variant


class _ToolCapability(TypedDict, total=False):
  mcpServerId: str
  mcp_server_id: str  # snake_case variant
  name: str
  description: str
  inputSchema: dict[str, Any]
  input_schema: dict[str, Any]  # snake_case variant


class _ResourceTemplateCapability(TypedDict, total=False):
  mcpServerId: str
  mcp_server_id: str  # snake_case variant
  name: str
  description: str
  uriTemplate: str
  uri_template: str  # snake_case variant


class _CapabilitiesResponse(TypedDict, total=False):
  """Response from capabilities API - supports both camelCase and snake_case."""

  mcpServers: list[_MCPServer]
  mcp_servers: list[_MCPServer]  # snake_case variant
  tools: list[_ToolCapability]
  resourceTemplates: list[_ResourceTemplateCapability]
  resource_templates: list[_ResourceTemplateCapability]  # snake_case variant


class MetorialMcpSession:
  """Internal MCP session class. Use Metorial client instead of creating directly."""

  def __init__(
    self,
    sdk: MetorialCoreSDK,
    init: MetorialMcpSessionInit,
  ) -> None:
    self._sdk = sdk
    self._init = init
    self._session: dict[str, Any] | None = None
    self._session_promise: asyncio.Task[dict[str, Any]] | None = None
    self._client_promises: dict[str, asyncio.Task[MetorialMcpClient]] = {}

    # Extract server deployment IDs from init
    server_deployments = init.get("serverDeployments", [])
    self.server_deployment_ids = [
      dep["id"] if isinstance(dep, dict) else dep for dep in server_deployments
    ]

    # Extract client info
    client_info = init.get("client", {})
    self.client_info = {
      "name": client_info.get("name", "metorial-python"),
      "version": client_info.get("version", "1.0.0"),
    }

    # Warn about duplicate deployment IDs
    if len(self.server_deployment_ids) != len(set(self.server_deployment_ids)):
      duplicates = [
        id
        for id in set(self.server_deployment_ids)
        if self.server_deployment_ids.count(id) > 1
      ]
      logger.warning(f"Warning: Duplicate server deployment IDs found: {duplicates}")

  def get_session(self) -> dict[str, Any]:
    if self._session is None:
      server_deployments: list[dict[str, Any]] = []
      for dep in self._init.get("serverDeployments", []):
        if isinstance(dep, dict):
          server_deployment_id = (
            dep.get("server_deployment_id")
            or dep.get("serverDeploymentId")
            or dep.get("id")
          )
          deployment_obj = {"serverDeploymentId": server_deployment_id}
          # Handle oauth_session_id (snake_case) or oauthSessionId (camelCase)
          oauth_session_id = dep.get("oauth_session_id") or dep.get("oauthSessionId")
          if oauth_session_id:
            deployment_obj["oauthSessionId"] = oauth_session_id
          server_deployments.append(deployment_obj)
        else:
          server_deployments.append({"serverDeploymentId": dep})

      api_payload = {
        "serverDeployments": server_deployments,
        "client": self._init.get(
          "client", {"name": "metorial-python", "version": "1.0.0"}
        ),
      }
      if "metadata" in self._init:
        api_payload["metadata"] = self._init["metadata"]

      _log_info(f"Creating session with API payload: {api_payload}")
      try:
        api_compatible_deployments: list[dict[str, Any]] = []
        for dep_item in server_deployments:
          transformed_dep: dict[str, Any] = {}
          if "serverDeploymentId" in dep_item:
            transformed_dep["server_deployment_id"] = dep_item["serverDeploymentId"]
          if "oauthSessionId" in dep_item:
            transformed_dep["oauth_session_id"] = dep_item["oauthSessionId"]
          for key, value in dep_item.items():
            if key not in ["serverDeploymentId", "oauthSessionId"]:
              transformed_dep[key] = value
          api_compatible_deployments.append(transformed_dep)

        sessions_api = self._sdk.sessions
        if sessions_api is None:
          raise RuntimeError("SDK sessions API is not initialized")
        session_response = sessions_api.create(
          server_deployments=api_compatible_deployments
        )
        logger.debug(f"Session response type: {type(session_response)}")
        logger.debug(f"Session response: {session_response}")

        try:
          # Try to access as object first
          session_id = session_response.id
          server_deployments = session_response.server_deployments
          client_secret = session_response.client_secret
          logger.debug("Successfully accessed response as object")
        except AttributeError as e:
          logger.debug(f"Failed to access as object: {e}")
          # If that fails, access as dict
          session_id = session_response["id"]
          server_deployments = session_response.get("server_deployments", [])
          client_secret = session_response.get("client_secret")
          logger.debug("Successfully accessed response as dict")

        self._session = {
          "id": session_id,
          "server_deployments": (
            [
              {"id": dep.id if hasattr(dep, "id") else dep["id"]}
              for dep in server_deployments
            ]
            if server_deployments
            else []
          ),
          "client_secret": (
            {
              "secret": client_secret.secret
              if hasattr(client_secret, "secret")
              else client_secret["secret"]
            }
            if client_secret
            else {}
          ),
        }
        _log_info(f"Session created: {self._session.get('id', 'unknown')}")
      except Exception as e:
        logger.error(f"Failed to create session: {e}")
        logger.error(f"Request payload was: {api_payload}")
        raise
    assert self._session is not None
    return self._session

  def get_server_deployments(self) -> list[dict[str, Any]]:
    """Get server deployments using cached session"""
    ses = self.get_session()
    result = ses.get("server_deployments") or ses.get("serverDeployments") or []
    if isinstance(result, list):
      return result
    return []

  async def get_capabilities(self) -> list[Capability]:
    _log_info("Getting server deployments...")
    deployments = self.get_server_deployments()
    _log_info(f"Got {len(deployments)} deployments: {[d['id'] for d in deployments]}")

    _log_info("Fetching capabilities from SDK...")
    try:
      servers_api = self._sdk.servers
      if servers_api is None:
        raise RuntimeError("SDK servers API is not initialized")
      capabilities_response: Any = servers_api.capabilities.list(
        server_deployment_id=[dep["id"] for dep in deployments]
      )

      # Handle both dict-like and object-like responses
      mcp_servers: list[Any] = getattr(capabilities_response, "mcp_servers", None) or (
        capabilities_response.get("mcp_servers", [])
        if hasattr(capabilities_response, "get")
        else []
      )
      tools: list[Any] = getattr(capabilities_response, "tools", None) or (
        capabilities_response.get("tools", [])
        if hasattr(capabilities_response, "get")
        else []
      )
      resource_templates: list[Any] = getattr(
        capabilities_response, "resource_templates", None
      ) or (
        capabilities_response.get("resource_templates", [])
        if hasattr(capabilities_response, "get")
        else []
      )

      _log_info(
        f"Got capabilities response: {len(tools)} tools, {len(mcp_servers)} servers"
      )
    except Exception as e:
      logger.error(f"Failed to get capabilities from SDK: {e}")
      raise

    servers_map = {
      server.id if hasattr(server, "id") else server["id"]: server
      for server in mcp_servers
    }

    # Group capabilities by deployment ID
    capabilities_by_deployment_id: dict[str, Any] = {}

    # Process tool capabilities
    for capability in tools:
      server = servers_map.get(
        capability.mcp_server_id
        if hasattr(capability, "mcp_server_id")
        else capability["mcp_server_id"]
      )
      if not server or not (
        server.server_deployment
        if hasattr(server, "server_deployment")
        else (server.get("server_deployment") if hasattr(server, "get") else None)
      ):
        continue

      server_deployment = (
        server.server_deployment
        if hasattr(server, "server_deployment")
        else (
          server.get("server_deployment")
          if hasattr(server, "get")
          else server["server_deployment"]
        )
      )
      deployment_id = (
        server_deployment.id
        if hasattr(server_deployment, "id")
        else server_deployment["id"]
      )
      if deployment_id not in capabilities_by_deployment_id:
        capabilities_by_deployment_id[deployment_id] = []

      capabilities_by_deployment_id[deployment_id].append(
        {
          "type": "tool",
          "tool": {
            "name": capability.name
            if hasattr(capability, "name")
            else capability["name"],
            "description": capability.description
            if hasattr(capability, "description")
            else (
              capability.get("description")
              if hasattr(capability, "get")
              else capability["description"]
            ),
            "inputSchema": capability.input_schema
            if hasattr(capability, "input_schema")
            else (
              capability.get("input_schema")
              if hasattr(capability, "get")
              else capability["input_schema"]
            ),
          },
          "serverDeployment": {"id": deployment_id},
        }
      )

    # Process resource template capabilities
    for capability in resource_templates:
      server = servers_map.get(
        capability.mcp_server_id
        if hasattr(capability, "mcp_server_id")
        else capability["mcp_server_id"]
      )
      if not server or not (
        server.server_deployment
        if hasattr(server, "server_deployment")
        else (server.get("server_deployment") if hasattr(server, "get") else None)
      ):
        continue

      server_deployment = (
        server.server_deployment
        if hasattr(server, "server_deployment")
        else (
          server.get("server_deployment")
          if hasattr(server, "get")
          else server["server_deployment"]
        )
      )
      deployment_id = (
        server_deployment.id
        if hasattr(server_deployment, "id")
        else server_deployment["id"]
      )
      if deployment_id not in capabilities_by_deployment_id:
        capabilities_by_deployment_id[deployment_id] = []

      capabilities_by_deployment_id[deployment_id].append(
        {
          "type": "resource-template",
          "resourceTemplate": {
            "name": capability.name
            if hasattr(capability, "name")
            else capability["name"],
            "description": capability.description
            if hasattr(capability, "description")
            else (
              capability.get("description")
              if hasattr(capability, "get")
              else capability["description"]
            ),
            "uriTemplate": capability.uri_template
            if hasattr(capability, "uri_template")
            else (
              capability.get("uri_template")
              if hasattr(capability, "get")
              else capability["uri_template"]
            ),
          },
          "serverDeployment": {"id": deployment_id},
        }
      )

    # Get capabilities for each deployment
    deployment_capabilities = []
    for deployment in deployments:
      deployment_id = deployment["id"]
      caps = capabilities_by_deployment_id.get(deployment_id, [])

      # If no auto-discovered capabilities, try manual discovery
      if not caps:
        try:
          client = await self.get_client({"deploymentId": deployment_id})
          tools_response: Any = await client.list_tools()

          # Handle both dict-like and object-like responses
          tools_list = (
            tools_response.get("tools", [])
            if hasattr(tools_response, "get")
            else getattr(tools_response, "tools", [])
          )
          caps.extend(
            [
              {
                "type": "tool",
                "tool": {
                  "name": tool["name"],
                  "description": tool.get("description"),
                  "inputSchema": tool.get("inputSchema"),
                },
                "serverDeployment": deployment,
              }
              for tool in tools_list
            ]
          )
        except Exception:
          # Server might not support tool listing
          pass

        try:
          templates_response: Any = await client.list_resource_templates()

          # Handle both dict-like and object-like responses
          templates_list = (
            templates_response.get("resourceTemplates", [])
            if hasattr(templates_response, "get")
            else getattr(templates_response, "resourceTemplates", [])
          )
          caps.extend(
            [
              {
                "type": "resource-template",
                "resourceTemplate": {
                  "name": template["name"],
                  "description": template.get("description"),
                  "uriTemplate": template.get("uriTemplate"),
                },
                "serverDeployment": deployment,
              }
              for template in templates_list
            ]
          )
        except Exception:
          # Server might not support resource templates
          pass

      deployment_capabilities.extend(caps)

    # If no capabilities found for specific deployments, log warning but don't return all capabilities
    if not deployment_capabilities:
      logger.debug(
        f"Warning: No capabilities found for requested deployments: {[d['id'] for d in deployments]}"
      )
      _log_info(
        f"Available deployment IDs with capabilities: {list(capabilities_by_deployment_id.keys())}"
      )

    return deployment_capabilities

  async def get_tool_manager(self) -> MetorialMcpToolManager:
    from .mcp_tool_manager import MetorialMcpToolManager

    _log_info("Getting capabilities for tool manager...")

    # Track the last critical error to re-raise if all methods fail
    critical_error: Exception | None = None

    try:
      caps = await self.get_capabilities()
      _log_info(f"Got {len(caps)} capabilities from API")

      if caps:
        return await MetorialMcpToolManager.from_capabilities(self, caps)
      else:
        logger.debug("Capabilities API returned empty, trying direct MCP...")

    except Exception as api_error:
      # Check if this is a critical error that should not be swallowed
      if self._is_critical_error(api_error):
        critical_error = api_error
        logger.error(f"Critical error from capabilities API: {api_error}")
      else:
        logger.warning(f"Warning: Capabilities API failed: {api_error}")
        # Add traceback for debugging
        import traceback

        logger.debug(f"Capabilities API error details: {traceback.format_exc()}")

    # Fallback to direct MCP if capabilities API fails or returns empty
    try:
      logger.debug("Trying direct MCP tool discovery as fallback...")
      caps = await self._get_tools_via_direct_mcp()
      _log_info(f"Direct MCP discovery found {len(caps)} capabilities")

      if caps:
        return await MetorialMcpToolManager.from_capabilities(self, caps)

    except Exception as direct_error:
      # Check if this is a critical error
      if self._is_critical_error(direct_error):
        critical_error = direct_error
        logger.error(f"Critical error from direct MCP: {direct_error}")
      else:
        logger.warning(f"Warning: Direct MCP discovery also failed: {direct_error}")
        # Add traceback for debugging
        import traceback

        logger.debug(f"Direct MCP error details: {traceback.format_exc()}")

    # If we have a critical error, re-raise it with a helpful message
    if critical_error is not None:
      self._raise_critical_error(critical_error)

    # If both methods failed or returned empty, return an empty tool manager
    logger.warning(
      "Warning: Both capabilities API and direct MCP failed, returning empty tool manager"
    )
    return await MetorialMcpToolManager.from_capabilities(self, [])

  def _is_critical_error(self, error: Exception) -> bool:
    """Check if an error is critical and should not be swallowed."""
    # Check for our typed exceptions
    if isinstance(error, AuthenticationError | NotFoundError | OAuthRequiredError):
      return True

    # Check error message for common critical error indicators
    error_str = str(error).lower()
    if "401" in error_str or "invalid api key" in error_str:
      return True

    if "404" in error_str and "not found" in error_str:
      return True

    # Check for OAuth required error patterns
    if "oauth" in error_str and ("required" in error_str or "session" in error_str):
      return True

    return "authentication required" in error_str

  def _raise_critical_error(self, error: Exception) -> None:
    """Re-raise a critical error with a helpful message."""
    error_str = str(error).lower()

    # Check for OAuth required error first (before auth error, as it's more specific)
    if isinstance(error, OAuthRequiredError):
      raise error

    if (
      "oauth" in error_str and ("required" in error_str or "session" in error_str)
    ) or "authentication required" in error_str:
      raise OAuthRequiredError(
        "This server deployment requires OAuth authentication. "
        "Create an OAuth session and include it in your server_deployments:\n\n"
        "    oauth = metorial.oauth.sessions.create(server_deployment_id='your-deployment')\n"
        "    print(f'Authorize at: {oauth.url}')\n"
        "    await metorial.oauth.wait_for_completion([oauth])\n\n"
        "    async with metorial.provider_session(\n"
        "        provider='openai',\n"
        "        server_deployments=[\n"
        "            {'server_deployment_id': 'your-deployment', 'oauth_session_id': oauth.id}\n"
        "        ],\n"
        "    ) as session:\n"
        "        ...",
        status_code=401,
      ) from error

    if (
      isinstance(error, AuthenticationError)
      or "401" in error_str
      or "invalid api key" in error_str
    ):
      raise AuthenticationError(
        "Invalid API key. Please check your METORIAL_API_KEY or the api_key parameter.",
        status_code=401,
      ) from error

    if isinstance(error, NotFoundError) or (
      "404" in error_str and "not found" in error_str
    ):
      raise NotFoundError(
        f"Server deployment not found. Please verify your deployment ID exists and is accessible. Original error: {error}",
        status_code=404,
      ) from error

    # Re-raise unknown critical errors as-is
    raise error

  async def _get_tools_via_direct_mcp(self) -> list[Capability]:
    """Get tools by connecting directly to MCP server, bypassing capabilities API."""
    _log_info("Starting direct MCP tool discovery...")

    capabilities: list[Capability] = []

    for deployment_id in self.server_deployment_ids:
      client = None
      tools = []

      # Step 1: Get client
      try:
        _log_info(f"Connecting directly to MCP for deployment: {deployment_id}")
        client = await self.get_client({"deploymentId": deployment_id})
      except Exception as e:
        logger.warning(f"Warning: Failed to get client for {deployment_id}: {e}")
        continue

      # Step 2: Get tools (this is the critical part)
      try:
        tools_response = await client.list_tools()

        if hasattr(tools_response, "tools"):
          tools = tools_response.tools
        elif isinstance(tools_response, dict):
          tools = tools_response.get("tools", [])
        else:
          tools = []

        _log_info(f"Direct MCP found {len(tools)} tools for {deployment_id}")

      except Exception as e:
        logger.warning(f"Warning: Failed to get tools for {deployment_id}: {e}")
        # Don't continue, still try to get templates

      # Step 3: Get resource templates (less critical)
      try:
        templates_response = await client.list_resource_templates()

        if hasattr(templates_response, "resourceTemplates"):
          pass  # templates = templates_response.resourceTemplates (unused)
        elif isinstance(templates_response, dict):
          pass  # templates = templates_response.get("resourceTemplates", []) (unused)
      except Exception as e:
        logger.debug(
          f"Warning: Failed to get resource templates for {deployment_id}: {e}"
        )
        # This is OK, we can proceed without templates

      # Step 4: Process tools into capabilities
      for tool in tools:
        try:
          capability: Capability = {
            "type": "tool",
            "tool": tool,
            "serverDeployment": {"id": deployment_id},
          }
          capabilities.append(capability)
        except Exception as e:
          logger.warning(f"Warning: Failed to process tool {tool}: {e}")
          continue

    _log_info(f"Direct MCP discovery completed: {len(capabilities)} total capabilities")
    return capabilities

  async def get_client(self, opts: dict[str, str]) -> MetorialMcpClient:
    dep_id = opts["deploymentId"]

    if dep_id not in self._client_promises:

      async def _create_client() -> MetorialMcpClient:
        try:
          ses = self.get_session()  # Use persistent cached session

          client = await MetorialMcpClient.create(
            types.SimpleNamespace(
              id=ses["id"],
              clientSecret=types.SimpleNamespace(secret=ses["client_secret"]["secret"]),
            ),
            host=self._mcp_host,
            deployment_id=dep_id,
            client_name=self.client_info["name"],
            client_version=self.client_info["version"],
            handshake_timeout=30.0,
            use_http_stream=False,
            log_raw_messages=False,
          )
          return client
        except Exception as e:
          # Clean up the task from the cache on error
          if dep_id in self._client_promises:
            del self._client_promises[dep_id]
          raise e

      self._client_promises[dep_id] = asyncio.create_task(_create_client())

    try:
      return await self._client_promises[dep_id]
    except Exception as e:
      # Clean up failed task
      if dep_id in self._client_promises:
        task = self._client_promises[dep_id]
        if not task.done():
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
            await task
        del self._client_promises[dep_id]
      raise e

  @property
  def _mcp_host(self) -> str:
    """Get MCP host from SDK config, with fallback logic."""
    config = self._sdk._config
    if hasattr(self._sdk, "_config") and config.get("mcpHost"):
      mcp_host = config["mcpHost"]
      return str(mcp_host) if mcp_host else "https://mcp.metorial.com"

    api_host_value = config.get("apiHost", "https://api.metorial.com")
    api_host = str(api_host_value) if api_host_value else "https://api.metorial.com"

    if api_host.startswith("https://api.metorial"):
      return api_host.replace("https://api.metorial", "https://mcp.metorial")

    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(api_host)
    parsed_dict = parsed._asdict()
    parsed_dict["port"] = 3311
    parsed = type(parsed)(**parsed_dict)
    return str(urlunparse(parsed))

  async def close(self) -> None:
    # Close all client promises gracefully
    close_tasks = []
    for client_promise in list(self._client_promises.values()):
      if client_promise.done() and not client_promise.cancelled():
        try:
          client = client_promise.result()
          close_tasks.append(client.close())
        except Exception:
          # Skip clients that failed to create
          continue

    if close_tasks:
      # Close all clients with timeout and exception handling
      try:
        await asyncio.wait_for(
          asyncio.gather(*close_tasks, return_exceptions=True), timeout=5.0
        )
      except asyncio.TimeoutError:
        logger.debug("MCP session close timeout - continuing cleanup")
      except Exception as e:
        logger.debug(f"MCP session close warning: {e}")

    # Clear the client promises
    self._client_promises.clear()
