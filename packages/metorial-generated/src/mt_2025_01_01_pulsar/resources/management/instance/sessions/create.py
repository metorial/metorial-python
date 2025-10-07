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


class mapManagementInstanceSessionsCreateOutputClientSecret:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputClientSecret:
        return ManagementInstanceSessionsCreateOutputClientSecret(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        secret=data.get('secret'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputClientSecret, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputServerDeploymentsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputServerDeploymentsServer:
        return ManagementInstanceSessionsCreateOutputServerDeploymentsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputServerDeploymentsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls:
        return ManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls(
        sse=data.get('sse'),
        streamable_http=data.get('streamable_http'),
        websocket=data.get('websocket')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputServerDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputServerDeployments:
        return ManagementInstanceSessionsCreateOutputServerDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        oauth_session_id=data.get('oauth_session_id'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsCreateOutputServerDeploymentsServer.from_dict(data.get('server')) if data.get('server') else None,
        connection_urls=mapManagementInstanceSessionsCreateOutputServerDeploymentsConnectionUrls.from_dict(data.get('connection_urls')) if data.get('connection_urls') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputServerDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsCreateOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsCreateOutputUsage:
        return ManagementInstanceSessionsCreateOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsCreateOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

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
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
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

