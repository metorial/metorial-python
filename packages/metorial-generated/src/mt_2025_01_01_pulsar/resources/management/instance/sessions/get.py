from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsGetOutputClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class ManagementInstanceSessionsGetOutputServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class ManagementInstanceSessionsGetOutputServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsGetOutputServerDeploymentsServer
    connection_urls: ManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsGetOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsGetOutput:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: ManagementInstanceSessionsGetOutputClientSecret
    server_deployments: List[ManagementInstanceSessionsGetOutputServerDeployments]
    usage: ManagementInstanceSessionsGetOutputUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


class mapManagementInstanceSessionsGetOutputClientSecret:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutputClientSecret:
        return ManagementInstanceSessionsGetOutputClientSecret(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        secret=data.get('secret'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutputClientSecret, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsGetOutputServerDeploymentsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutputServerDeploymentsServer:
        return ManagementInstanceSessionsGetOutputServerDeploymentsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutputServerDeploymentsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls:
        return ManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls(
        sse=data.get('sse'),
        streamable_http=data.get('streamable_http'),
        websocket=data.get('websocket')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsGetOutputServerDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutputServerDeployments:
        return ManagementInstanceSessionsGetOutputServerDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        oauth_session_id=data.get('oauth_session_id'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsGetOutputServerDeploymentsServer.from_dict(data.get('server')) if data.get('server') else None,
        connection_urls=mapManagementInstanceSessionsGetOutputServerDeploymentsConnectionUrls.from_dict(data.get('connection_urls')) if data.get('connection_urls') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutputServerDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutputUsage:
        return ManagementInstanceSessionsGetOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsGetOutput:
        return ManagementInstanceSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapManagementInstanceSessionsGetOutputClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapManagementInstanceSessionsGetOutputServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapManagementInstanceSessionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

