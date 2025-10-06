from __future__ import annotations
import asyncio
import types
import logging
from typing import Any, Dict, List, Optional, TypedDict, Protocol

from .mcp_client import MetorialMcpClient
from .mcp_tool import Capability

logger = logging.getLogger(__name__)

def _should_log_debug():
  """Check if debug logging should be enabled by examining logger level."""
  return logger.isEnabledFor(logging.DEBUG)

def _log_info(message):
  """Conditionally log info messages only if debug logging is enabled."""
  if _should_log_debug():
    logger.info(message)


class _ServerDeployment(TypedDict):
  id: str


class _ClientInfo(TypedDict, total=False):
  name: str
  version: str


class MetorialMcpSessionInit(TypedDict, total=False):
  serverDeployments: List[_ServerDeployment]
  client: _ClientInfo
  metadata: Dict[str, Any]


class _SDKConfig(TypedDict, total=False):
  apiHost: str
  mcpHost: str
  apiKey: str


class _SessionsAPI(Protocol):
  async def create(self, init: MetorialMcpSessionInit) -> Dict[str, Any]:
    ...


class _CapabilitiesAPI(Protocol):
  async def list(self, params: Dict[str, Any]) -> Dict[str, Any]:
    ...


class _ServersAPI(Protocol):
  capabilities: _CapabilitiesAPI


class MetorialCoreSDK(Protocol):
  _config: _SDKConfig
  sessions: _SessionsAPI
  servers: _ServersAPI


class _SessionResponse(TypedDict):
  id: str
  serverDeployments: List[Dict[str, Any]]
  client_secret: Dict[str, str]


class _MCPServer(TypedDict):
  id: str
  serverDeployment: Dict[str, Any]


class _ToolCapability(TypedDict):
  mcpServerId: str
  name: str
  description: str
  inputSchema: Dict[str, Any]


class _ResourceTemplateCapability(TypedDict):
  mcpServerId: str
  name: str
  description: str
  uriTemplate: str


class _CapabilitiesResponse(TypedDict):
  mcpServers: List[_MCPServer]
  tools: List[_ToolCapability]
  resourceTemplates: List[_ResourceTemplateCapability]


class MetorialMcpSession:
  """Internal MCP session class. Use Metorial client instead of creating directly."""

  def __init__(
    self,
    sdk: MetorialCoreSDK,
    init: MetorialMcpSessionInit,
  ) -> None:
    self._sdk = sdk
    self._init = init
    self._session: Optional[Dict[str, Any]] = None
    self._client_tasks: Dict[str, asyncio.Task[MetorialMcpClient]] = {}

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
      logger.warning(f"⚠️ Duplicate server deployment IDs found: {duplicates}")

  def get_session(self) -> _SessionResponse:
    if self._session is None:
      # Use TypeScript-compatible format: {serverDeployments: [{serverDeploymentId, oauthSessionId?}]}
      server_deployments = []
      for dep in self._init.get("serverDeployments", []):
        if isinstance(dep, dict):
          server_deployment_id = dep.get("serverDeploymentId") or dep.get("id")
          deployment_obj = {"serverDeploymentId": server_deployment_id}
          if "oauthSessionId" in dep:
            deployment_obj["oauthSessionId"] = dep["oauthSessionId"]
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

      _log_info(f"🔄 Creating session with API payload: {api_payload}")
      try:
        api_compatible_deployments = []
        for dep in server_deployments:
          if isinstance(dep, dict):
            transformed_dep = {}
            if "serverDeploymentId" in dep:
              transformed_dep["server_deployment_id"] = dep["serverDeploymentId"]
            if "oauthSessionId" in dep:
              transformed_dep["oauth_session_id"] = dep["oauthSessionId"]
            for key, value in dep.items():
              if key not in ["serverDeploymentId", "oauthSessionId"]:
                transformed_dep[key] = value
            api_compatible_deployments.append(transformed_dep)
          else:
            # String format stays as-is
            api_compatible_deployments.append(dep)

        session_response = self._sdk.sessions.create(
          server_deployments=api_compatible_deployments
        )
        logger.debug(f"Session response type: {type(session_response)}")
        logger.debug(f"Session response: {session_response}")

        try:
          # Try to access as object first
          session_id = session_response.id
          server_deployments = session_response.server_deployments
          client_secret = session_response.client_secret
          logger.debug("✅ Successfully accessed response as object")
        except AttributeError as e:
          logger.debug(f"❌ Failed to access as object: {e}")
          # If that fails, access as dict
          session_id = session_response["id"]
          server_deployments = session_response.get("server_deployments", [])
          client_secret = session_response.get("client_secret")
          logger.debug("✅ Successfully accessed response as dict")

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
        _log_info(f"✅ Session created: {self._session.get('id', 'unknown')}")
      except Exception as e:
        logger.error(f"❌ Failed to create session: {e}")
        logger.error(f"📊 Request payload was: {api_payload}")
        raise
    return self._session  # type: ignore[return-value]

  def get_server_deployments(self) -> List[Dict[str, Any]]:
    ses = self.get_session()
    return ses.get("server_deployments") or ses.get("serverDeployments") or []  # type: ignore[return-value]

  async def get_capabilities(self) -> List[Capability]:
    _log_info("📋 Getting server deployments...")
    deployments = self.get_server_deployments()
    _log_info(
      f"✅ Got {len(deployments)} deployments: {[d['id'] for d in deployments]}"
    )

    _log_info("🔍 Fetching capabilities from SDK...")
    try:
      capabilities: _CapabilitiesResponse = self._sdk.servers.capabilities.list(  # type: ignore[assignment]
        server_deployment_id=[dep["id"] for dep in deployments]
      )

      # Handle both dict-like and object-like responses
      mcp_servers = (
        capabilities.mcp_servers
        if hasattr(capabilities, "mcp_servers")
        else capabilities.get("mcp_servers", [])
        if hasattr(capabilities, "get")
        else capabilities["mcp_servers"]
      )
      tools = (
        capabilities.tools
        if hasattr(capabilities, "tools")
        else capabilities.get("tools", [])
        if hasattr(capabilities, "get")
        else capabilities.get("tools", [])
      )
      resource_templates = (
        capabilities.resource_templates
        if hasattr(capabilities, "resource_templates")
        else capabilities.get("resource_templates", [])
        if hasattr(capabilities, "get")
        else capabilities.get("resource_templates", [])
      )

      _log_info(
        f"✅ Got capabilities response: {len(tools)} tools, {len(mcp_servers)} servers"
      )
    except Exception as e:
      logger.error(f"❌ Failed to get capabilities from SDK: {e}")
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
          tools = await client.list_tools()

          caps.extend(
            [
              {
                "type": "tool",
                "tool": {
                  "name": tool["name"],
                  "description": tool["description"],
                  "inputSchema": tool["inputSchema"],
                },
                "serverDeployment": deployment,
              }
              for tool in tools.get("tools", [])
            ]
          )
        except Exception:
          # Server might not support tool listing
          pass

        try:
          resource_templates = await client.list_resource_templates()
          caps.extend(
            [
              {
                "type": "resource-template",
                "resourceTemplate": {
                  "name": template["name"],
                  "description": template["description"],
                  "uriTemplate": template["uriTemplate"],
                },
                "serverDeployment": deployment,
              }
              for template in resource_templates.get("resourceTemplates", [])
            ]
          )
        except Exception:
          # Server might not support resource templates
          pass

      deployment_capabilities.extend(caps)

    # If no capabilities found for specific deployments, log warning but don't return all capabilities
    if not deployment_capabilities:
      logger.debug(
        f"⚠️ No capabilities found for requested deployments: {[d['id'] for d in deployments]}"
      )
      _log_info(
        f"📊 Available deployment IDs with capabilities: {list(capabilities_by_deployment_id.keys())}"
      )

    return deployment_capabilities

  async def get_tool_manager(self):
    from .mcp_tool_manager import MetorialMcpToolManager

    _log_info("🔧 Getting capabilities for tool manager...")
    try:
      caps = await self.get_capabilities()
      _log_info(f"✅ Got {len(caps)} capabilities")

      # If capabilities API returns empty tools, try direct MCP tool discovery
      if not caps:
        logger.debug(
          "❌ Capabilities API returned empty, trying direct MCP tool discovery..."
        )
        caps = await self._get_tools_via_direct_mcp()
        _log_info(f"Direct MCP discovery found {len(caps)} capabilities")

      return await MetorialMcpToolManager.from_capabilities(self, caps)
    except Exception as e:
      logger.error(f"❌ Failed to get tool manager: {e}")
      # Try direct MCP as fallback
      try:
        logger.warning("🔄 Falling back to direct MCP tool discovery...")
        caps = await self._get_tools_via_direct_mcp()
        _log_info(f"🎯 Fallback MCP discovery found {len(caps)} capabilities")
        return await MetorialMcpToolManager.from_capabilities(self, caps)
      except Exception as fallback_error:
        logger.error(f"❌ Fallback MCP discovery also failed: {fallback_error}")
        raise e  # Raise the original error

  async def _get_tools_via_direct_mcp(self) -> List[Capability]:
    """Get tools by connecting directly to MCP server, bypassing capabilities API."""
    _log_info("🔧 Starting direct MCP tool discovery...")

    capabilities = []

    for deployment_id in self.server_deployment_ids:
      try:
        _log_info(f"🔗 Connecting directly to MCP for deployment: {deployment_id}")

        client = await self.get_client({"deploymentId": deployment_id})

        tools_response = await client.list_tools()

        if hasattr(tools_response, "tools"):
          tools = tools_response.tools
        elif isinstance(tools_response, dict):
          tools = tools_response.get("tools", [])
        else:
          tools = []

        templates_response = await client.list_resource_templates()

        if hasattr(templates_response, "resourceTemplates"):
          templates = templates_response.resourceTemplates
        elif isinstance(templates_response, dict):
          templates = templates_response.get("resourceTemplates", [])
        else:
          templates = []

        _log_info(
          f"🎯 Direct MCP found {len(tools)} tools and {len(templates)} templates for {deployment_id}"
        )

        for tool in tools:
          capabilities.append(
            {"type": "tool", "tool": tool, "serverDeployment": {"id": deployment_id}}
          )

        # TODO: Implement resource template support

      except Exception as e:
        logger.warning(f"⚠️ Direct MCP discovery failed for {deployment_id}: {e}")
        continue

    _log_info(
      f"🎯 Direct MCP discovery completed: {len(capabilities)} total capabilities"
    )
    return capabilities

  async def get_client(self, opts: Dict[str, str]) -> MetorialMcpClient:
    dep_id = opts["deploymentId"]
    if dep_id not in self._client_tasks:

      async def _create() -> MetorialMcpClient:
        ses = self.get_session()
        return await MetorialMcpClient.create(
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

      self._client_tasks[dep_id] = asyncio.create_task(_create())

    return await self._client_tasks[dep_id]

  @property
  def _mcp_host(self) -> str:
    """Get MCP host from SDK config, with fallback logic."""
    if hasattr(self._sdk, "_config") and self._sdk._config.get("mcpHost"):
      return self._sdk._config["mcpHost"]

    api_host = self._sdk._config.get("apiHost", "https://api.metorial.com")

    if api_host.startswith("https://api.metorial"):
      return api_host.replace("https://api.metorial", "https://mcp.metorial")

    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(api_host)
    parsed = parsed._replace(port=3311)  # type: ignore[call-arg]
    return urlunparse(parsed)

  async def close(self) -> None:
    await asyncio.gather(
      *[
        t.result().close()
        for t in self._client_tasks.values()
        if t.done() and not t.cancelled()
      ],
      return_exceptions=True,
    )
