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


class mapDashboardInstanceSessionsDeleteOutputClientSecret:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutputClientSecret:
        return DashboardInstanceSessionsDeleteOutputClientSecret(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        secret=data.get('secret'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutputClientSecret, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsDeleteOutputServerDeploymentsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutputServerDeploymentsServer:
        return DashboardInstanceSessionsDeleteOutputServerDeploymentsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutputServerDeploymentsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
        return DashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls(
        sse=data.get('sse'),
        streamable_http=data.get('streamable_http'),
        websocket=data.get('websocket')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsDeleteOutputServerDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutputServerDeployments:
        return DashboardInstanceSessionsDeleteOutputServerDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        oauth_session_id=data.get('oauth_session_id'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsDeleteOutputServerDeploymentsServer.from_dict(data.get('server')) if data.get('server') else None,
        connection_urls=mapDashboardInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls.from_dict(data.get('connection_urls')) if data.get('connection_urls') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutputServerDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsDeleteOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsDeleteOutputUsage:
        return DashboardInstanceSessionsDeleteOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

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
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

