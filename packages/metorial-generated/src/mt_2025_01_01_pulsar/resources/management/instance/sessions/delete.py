from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsDeleteOutputClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class ManagementInstanceSessionsDeleteOutputServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class ManagementInstanceSessionsDeleteOutputServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsDeleteOutputServerDeploymentsServer
    connection_urls: ManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsDeleteOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsDeleteOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: ManagementInstanceSessionsDeleteOutputClientSecret
    server_deployments: List[ManagementInstanceSessionsDeleteOutputServerDeployments]
    usage: ManagementInstanceSessionsDeleteOutputUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


class mapManagementInstanceSessionsDeleteOutputClientSecret:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutputClientSecret:
        return ManagementInstanceSessionsDeleteOutputClientSecret(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        secret=data.get('secret'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutputClientSecret, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsDeleteOutputServerDeploymentsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutputServerDeploymentsServer:
        return ManagementInstanceSessionsDeleteOutputServerDeploymentsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutputServerDeploymentsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls:
        return ManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls(
        sse=data.get('sse'),
        streamable_http=data.get('streamable_http'),
        websocket=data.get('websocket')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsDeleteOutputServerDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutputServerDeployments:
        return ManagementInstanceSessionsDeleteOutputServerDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        oauth_session_id=data.get('oauth_session_id'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsDeleteOutputServerDeploymentsServer.from_dict(data.get('server')) if data.get('server') else None,
        connection_urls=mapManagementInstanceSessionsDeleteOutputServerDeploymentsConnectionUrls.from_dict(data.get('connection_urls')) if data.get('connection_urls') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutputServerDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsDeleteOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutputUsage:
        return ManagementInstanceSessionsDeleteOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsDeleteOutput:
        return ManagementInstanceSessionsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapManagementInstanceSessionsDeleteOutputClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapManagementInstanceSessionsDeleteOutputServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapManagementInstanceSessionsDeleteOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

