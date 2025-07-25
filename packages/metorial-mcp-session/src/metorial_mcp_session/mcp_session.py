from __future__ import annotations
import asyncio, types, json, requests
from typing import Any, Dict, List, Optional, TypedDict

from .mcp_client import MetorialMcpClient
from .mcp_tool import Capability

# -------- REST helpers --------
def build_session_body(server_deployment_ids: List[str], *,
                       client_name="metorial-python",
                       client_version="0.1.0",
                       metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    body = {
        "server_deployment_ids": server_deployment_ids,
        "client": {"name": client_name, "version": client_version},
    }
    if metadata:
        body["metadata"] = metadata
    return body


def create_session(*, api_key: str, api_host: str,
                   server_deployment_ids: List[str],
                   client_name="metorial-python",
                   client_version="0.1.0",
                   metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    body = build_session_body(server_deployment_ids,
                              client_name=client_name,
                              client_version=client_version,
                              metadata=metadata)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    url = f"{api_host.rstrip('/')}/sessions"
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    if resp.status_code >= 400:
        raise RuntimeError(f"Session create failed: {resp.status_code} {resp.text}")
    return resp.json()


# -------- Types (optional niceties) --------
class _ServerDeployment(TypedDict):
    id: str

class MetorialMcpSessionInit(TypedDict, total=False):
    serverDeployments: List[_ServerDeployment]
    client: Dict[str, str]
    metadata: Dict[str, Any]


# -------- Main class --------
class MetorialMcpSession:
    def __init__(
        self,
        *,
        api_key: str,
        api_host: str,
        mcp_host: str,
        server_deployment_ids: List[str],
        client_name: str = "metorial-python",
        client_version: str = "0.1.0",
    ) -> None:
        self.api_key = api_key
        self.api_host = api_host.rstrip("/")
        self.mcp_host = mcp_host.rstrip("/")
        self.server_deployment_ids = server_deployment_ids
        self.client_info = {"name": client_name, "version": client_version}

        self._session: Optional[Dict[str, Any]] = None
        self._client_tasks: Dict[str, asyncio.Task[MetorialMcpClient]] = {}

    # --- public ---
    async def get_session(self) -> Dict[str, Any]:
        if self._session is None:
            self._session = create_session(
                api_key=self.api_key,
                api_host=self.api_host,
                server_deployment_ids=self.server_deployment_ids,
                client_name=self.client_info["name"],
                client_version=self.client_info["version"],
            )
        return self._session

    async def get_server_deployments(self) -> List[Dict[str, Any]]:
        ses = await self.get_session()
        return ses.get("server_deployments") or ses.get("serverDeployments") or []

    async def get_capabilities(self) -> List[Capability]:
        # Only manual discovery through MCP
        deployments = await self.get_server_deployments()
        return await self._manual_discover(deployments)

    async def get_tool_manager(self):
        from .mcp_tool_manager import MetorialMcpToolManager
        caps = await self.get_capabilities()
        return await MetorialMcpToolManager.from_capabilities(self, caps)

    async def get_client(self, opts: Dict[str, str]) -> MetorialMcpClient:
        dep_id = opts["deploymentId"]
        if dep_id not in self._client_tasks:

            async def _create() -> MetorialMcpClient:
                ses = await self.get_session()
                return await MetorialMcpClient.create(
                    types.SimpleNamespace(
                        id=ses["id"],
                        clientSecret=types.SimpleNamespace(secret=ses["client_secret"]["secret"]),
                    ),
                    host=self.mcp_host,
                    deployment_id=dep_id,
                    client_name=self.client_info["name"],
                    client_version=self.client_info["version"],
                    handshake_timeout=30.0,
                    use_http_stream=False,
                    log_raw_messages=False,
                )

            self._client_tasks[dep_id] = asyncio.create_task(_create())

        return await self._client_tasks[dep_id]

    async def close(self) -> None:
        await asyncio.gather(
            *[
                t.result().close()
                for t in self._client_tasks.values()
                if t.done() and not t.cancelled()
            ],
            return_exceptions=True,
        )

    # --- internals ---
    async def _manual_discover(self, deployments: List[Dict[str, Any]]) -> List[Capability]:
        caps: List[Capability] = []
        for dep in deployments:
            client = await self.get_client({"deploymentId": dep["id"]})

            # tools
            try:
                tools = await client.list_tools()
                for t in tools.tools:
                    caps.append({
                        "type": "tool",
                        "tool": {
                            "name": t.name,
                            "description": t.description,
                            "inputSchema": t.inputSchema,
                        },
                        "serverDeployment": dep,
                    })
            except Exception:
                pass

            # resource templates
            try:
                rts = await client.list_resource_templates()
                for rt in rts.resourceTemplates:
                    caps.append({
                        "type": "resource-template",
                        "resourceTemplate": {
                            "name": rt.name,
                            "description": rt.description,
                            "uriTemplate": rt.uriTemplate,
                        },
                        "serverDeployment": dep,
                    })
            except Exception:
                pass
        return caps
