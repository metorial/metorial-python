from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsCreateOutputClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class DashboardInstanceSessionsCreateOutputServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsCreateOutputServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class DashboardInstanceSessionsCreateOutputServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsCreateOutputServerDeploymentsServer
    connection_urls: DashboardInstanceSessionsCreateOutputServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsCreateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsCreateOutputClientInfo:
    name: str
    version: str
@dataclass
class DashboardInstanceSessionsCreateOutputClient:
    object: str
    info: DashboardInstanceSessionsCreateOutputClientInfo
@dataclass
class DashboardInstanceSessionsCreateOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: DashboardInstanceSessionsCreateOutputClientSecret
    server_deployments: List[DashboardInstanceSessionsCreateOutputServerDeployments]
    usage: DashboardInstanceSessionsCreateOutputUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    client: Optional[DashboardInstanceSessionsCreateOutputClient] = None


class mapDashboardInstanceSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateOutput:
        return DashboardInstanceSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapDashboardInstanceSessionsCreateOutputClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapDashboardInstanceSessionsCreateOutputServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapDashboardInstanceSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        client=mapDashboardInstanceSessionsCreateOutputClient.from_dict(data.get('client')) if data.get('client') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsCreateBody:
    server_deployments: List[Union[Dict[str, Any], str]]


class mapDashboardInstanceSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsCreateBody:
        return DashboardInstanceSessionsCreateBody(
        server_deployments=data.get('server_deployments', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

