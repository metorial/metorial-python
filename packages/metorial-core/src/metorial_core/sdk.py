# sdk.py
from dataclasses import dataclass
from typing import TypedDict, Dict, Any

from .sdk_builder import MetorialSDKBuilder
from metorial_util_endpoint import MetorialEndpointManager

from mt_2025_01_01_pulsar.endpoints.instance import MetorialInstanceEndpoint
from mt_2025_01_01_pulsar.endpoints.secrets import MetorialSecretsEndpoint

from mt_2025_01_01_pulsar.endpoints.servers import MetorialServersEndpoint
from mt_2025_01_01_pulsar.endpoints.servers_variants import MetorialServersVariantsEndpoint
from mt_2025_01_01_pulsar.endpoints.servers_versions import MetorialServersVersionsEndpoint
from mt_2025_01_01_pulsar.endpoints.servers_deployments import MetorialServersDeploymentsEndpoint
from mt_2025_01_01_pulsar.endpoints.servers_implementations import MetorialServersImplementationsEndpoint
from mt_2025_01_01_pulsar.endpoints.servers_capabilities import MetorialServersCapabilitiesEndpoint

from mt_2025_01_01_pulsar.endpoints.server_runs import MetorialServerRunsEndpoint
from mt_2025_01_01_pulsar.endpoints.server_run_errors import MetorialServerRunErrorsEndpoint

from mt_2025_01_01_pulsar.endpoints.sessions import MetorialSessionsEndpoint
from mt_2025_01_01_pulsar.endpoints.sessions_messages import MetorialSessionsMessagesEndpoint


# ---------- typing for config ----------
class SDKConfig(TypedDict):
    apiKey: str
    apiVersion: str
    apiHost: str
# ---------------------------------------


class _DelegatingGroup:
    """Base: forwards any missing attr to _root endpoint."""
    __slots__ = ("_root",)

    def __init__(self, root):
        # remember the real endpoint
        self._root = root

        # bind every public method that root actually provides, so
        # editors see completion & it won’t crash if one is missing
        for name in dir(root):
            if name.startswith("_"):
                continue
            attr = getattr(root, name)
            if callable(attr):
                # only bind if we haven't already set it on the subclass
                # (avoids stomping on explicit sub‐resource attrs)
                if not hasattr(self, name):
                    setattr(self, name, attr)

    def __getattr__(self, name):
        # fall back to real endpoint for anything else
        return getattr(self._root, name)
    
    
class SessionsGroup(_DelegatingGroup):
    __slots__ = ("messages")

    def __init__(self, root, messages):
        super().__init__(root)
        self.messages = messages

class RunsGroup(_DelegatingGroup):
    __slots__ = ("errors",)

    def __init__(self, root, errors):
        super().__init__(root)
        self.errors = errors

class ServersGroup(_DelegatingGroup):
    __slots__ = ("variants", "versions", "deployments", "implementations", "capabilities", "runs")

    def __init__(self, root, variants, versions, deployments, implementations, capabilities, runs):
        super().__init__(root)
        self.variants = variants
        self.versions = versions
        self.deployments = deployments
        self.implementations = implementations
        self.capabilities = capabilities
        self.runs = runs


@dataclass(frozen=True)
class SDK:
    _config: SDKConfig
    instance: MetorialInstanceEndpoint
    secrets: MetorialSecretsEndpoint
    servers: MetorialServersEndpoint
    sessions: MetorialSessionsEndpoint
# -----------------------------------------------


def get_config(soft: Dict[str, Any]) -> Dict[str, Any]:
    return {**soft, "apiVersion": soft.get("apiVersion", "2025-01-01-pulsar")}

def get_headers(config: Dict[str, Any]) -> Dict[str, str]:
    return {"Authorization": f"Bearer {config['apiKey']}"}

def get_api_host(config: Dict[str, Any]) -> str:
    return config.get("apiHost", "https://api.metorial.com")


def get_endpoints(manager: MetorialEndpointManager) -> Dict[str, Any]:
    endpoints: Dict[str, Any] = {
        "instance": MetorialInstanceEndpoint(manager),
        "secrets": MetorialSecretsEndpoint(manager),
    }

    servers = MetorialServersEndpoint(manager)
    setattr(servers, "variants", MetorialServersVariantsEndpoint(manager))
    setattr(servers, "versions", MetorialServersVersionsEndpoint(manager))
    setattr(servers, "deployments", MetorialServersDeploymentsEndpoint(manager))
    setattr(servers, "implementations", MetorialServersImplementationsEndpoint(manager))
    setattr(servers, "capabilities", MetorialServersCapabilitiesEndpoint(manager))

    runs = MetorialServerRunsEndpoint(manager)
    setattr(runs, "errors", MetorialServerRunErrorsEndpoint(manager))
    setattr(servers, "runs", runs)

    sessions = MetorialSessionsEndpoint(manager)

    setattr(sessions, "messages", MetorialSessionsMessagesEndpoint(manager))


    endpoints["servers"] = servers
    endpoints["sessions"] = sessions
    return endpoints


# --- builder ---
_create = (
    MetorialSDKBuilder
    .create("myapi", "2025-01-01-pulsar")
    .set_get_api_host(get_api_host)
    .set_get_headers(get_headers)
    .build(get_config)
)

def _to_typed_sdk(raw: Dict[str, Any]) -> SDK:
    _cfg = raw["_config"]

    servers_root = raw["servers"]
    sessions_root = raw["sessions"]

    servers_group = ServersGroup(
        servers_root,
        servers_root.variants,
        servers_root.versions,
        servers_root.deployments,
        servers_root.implementations,
        servers_root.capabilities,
        RunsGroup(servers_root.runs, servers_root.runs.errors),
    )

    sessions_group = SessionsGroup(
        sessions_root,
        sessions_root.messages,
    )

    return SDK(
        _config=SDKConfig(
            apiKey=_cfg["apiKey"],
            apiVersion=_cfg["apiVersion"],
            apiHost=_cfg["apiHost"],
        ),
        instance=raw["instance"],
        secrets=raw["secrets"],
        servers=servers_group,
        sessions=sessions_group,
    )

def create_metorial_sdk(config: Dict[str, Any]) -> SDK:
    raw = _create(get_endpoints)(config)
    return _to_typed_sdk(raw)
