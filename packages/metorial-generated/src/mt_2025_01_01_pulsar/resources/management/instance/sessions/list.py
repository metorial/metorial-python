from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsListOutputItemsClientSecret:
    object: str
    type: str
    id: str
    secret: str
    expires_at: datetime
@dataclass
class ManagementInstanceSessionsListOutputItemsServerDeploymentsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls:
    sse: str
    streamable_http: str
    websocket: str
@dataclass
class ManagementInstanceSessionsListOutputItemsServerDeployments:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsListOutputItemsServerDeploymentsServer
    connection_urls: ManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls
    name: Optional[str] = None
    oauth_session_id: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsListOutputItemsUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsListOutputItems:
    object: str
    id: str
    status: str
    connection_status: str
    client_secret: ManagementInstanceSessionsListOutputItemsClientSecret
    server_deployments: List[ManagementInstanceSessionsListOutputItemsServerDeployments]
    usage: ManagementInstanceSessionsListOutputItemsUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsListOutput:
    items: List[ManagementInstanceSessionsListOutputItems]
    pagination: ManagementInstanceSessionsListOutputPagination


class mapManagementInstanceSessionsListOutputItemsClientSecret:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsClientSecret:
        return ManagementInstanceSessionsListOutputItemsClientSecret(
        object=data.get('object'),
        type=data.get('type'),
        id=data.get('id'),
        secret=data.get('secret'),
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsClientSecret, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItemsServerDeploymentsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsServerDeploymentsServer:
        return ManagementInstanceSessionsListOutputItemsServerDeploymentsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsServerDeploymentsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls:
        return ManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls(
        sse=data.get('sse'),
        streamable_http=data.get('streamable_http'),
        websocket=data.get('websocket')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItemsServerDeployments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsServerDeployments:
        return ManagementInstanceSessionsListOutputItemsServerDeployments(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        oauth_session_id=data.get('oauth_session_id'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsListOutputItemsServerDeploymentsServer.from_dict(data.get('server')) if data.get('server') else None,
        connection_urls=mapManagementInstanceSessionsListOutputItemsServerDeploymentsConnectionUrls.from_dict(data.get('connection_urls')) if data.get('connection_urls') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsServerDeployments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItemsUsage:
        return ManagementInstanceSessionsListOutputItemsUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputItems:
        return ManagementInstanceSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        client_secret=mapManagementInstanceSessionsListOutputItemsClientSecret.from_dict(data.get('client_secret')) if data.get('client_secret') else None,
        server_deployments=[mapManagementInstanceSessionsListOutputItemsServerDeployments.from_dict(item) for item in data.get('server_deployments', []) if item],
        usage=mapManagementInstanceSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutputPagination:
        return ManagementInstanceSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListOutput:
        return ManagementInstanceSessionsListOutput(
        items=[mapManagementInstanceSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    server_id: Optional[Union[str, List[str]]] = None
    server_variant_id: Optional[Union[str, List[str]]] = None
    server_implementation_id: Optional[Union[str, List[str]]] = None
    server_deployment_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsListQuery:
        return ManagementInstanceSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        server_implementation_id=data.get('server_implementation_id'),
        server_deployment_id=data.get('server_deployment_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

