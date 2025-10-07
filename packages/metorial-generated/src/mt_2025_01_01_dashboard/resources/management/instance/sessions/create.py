from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsCreateOutputClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class ManagementInstanceSessionsCreateOutputServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class ManagementInstanceSessionsCreateOutputServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsCreateOutputServerDeploymentsServer
    connection_urls: ManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsCreateOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsCreateOutputClientInfo:
    name: str
    version: str
@dataclass
class ManagementInstanceSessionsCreateOutputClient:
    object: str
    info: ManagementInstanceSessionsCreateOutputClientInfo
@dataclass
class ManagementInstanceSessionsCreateOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: ManagementInstanceSessionsCreateOutputClientSecret
    server_deployments: List[ManagementInstanceSessionsCreateOutputServerDeployments]
    usage: ManagementInstanceSessionsCreateOutputUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    client: Optional[ManagementInstanceSessionsCreateOutputClient] = None


class mapManagementInstanceSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutput:
        return ManagementInstanceSessionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapManagementInstanceSessionsCreateOutputClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapManagementInstanceSessionsCreateOutputServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapManagementInstanceSessionsCreateOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        client=mapManagementInstanceSessionsCreateOutputClient.from_dict(data.get('client')) if data.get('client') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsCreateBody:
    server_deployments: List[Union[Dict[str, Any], str]]


class mapManagementInstanceSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateBody:
        return ManagementInstanceSessionsCreateBody(
        server_deployments=data.get('server_deployments', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

