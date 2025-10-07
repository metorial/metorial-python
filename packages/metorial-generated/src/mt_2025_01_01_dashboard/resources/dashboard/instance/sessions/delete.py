from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsDeleteOutputClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class DashboardInstanceSessionsDeleteOutputServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class DashboardInstanceSessionsDeleteOutputServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsDeleteOutputServerDeploymentsServer
    connection_urls: DashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsDeleteOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsDeleteOutputClientInfo:
    name: str
    version: str
@dataclass
class DashboardInstanceSessionsDeleteOutputClient:
    object: str
    info: DashboardInstanceSessionsDeleteOutputClientInfo
@dataclass
class DashboardInstanceSessionsDeleteOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: DashboardInstanceSessionsDeleteOutputClientSecret
    server_deployments: List[DashboardInstanceSessionsDeleteOutputServerDeployments]
    usage: DashboardInstanceSessionsDeleteOutputUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    client: Optional[DashboardInstanceSessionsDeleteOutputClient] = None


class mapDashboardInstanceSessionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutput:
        return DashboardInstanceSessionsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapDashboardInstanceSessionsDeleteOutputClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapDashboardInstanceSessionsDeleteOutputServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapDashboardInstanceSessionsDeleteOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        client=mapDashboardInstanceSessionsDeleteOutputClient.from_dict(data.get('client')) if data.get('client') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

