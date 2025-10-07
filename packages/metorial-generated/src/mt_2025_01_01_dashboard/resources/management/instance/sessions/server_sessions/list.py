from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceSessionsServerSessionsListOutputItemsMcpClient] = None
    server: Optional[ManagementInstanceSessionsServerSessionsListOutputItemsMcpServer] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: ManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient:
    user_agent: str
    anonymized_ip_address: str
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItemsConnection:
    object: str
    id: str
    client: ManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputItems:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceSessionsServerSessionsListOutputItemsMcp
    usage: ManagementInstanceSessionsServerSessionsListOutputItemsUsage
    server: ManagementInstanceSessionsServerSessionsListOutputItemsServer
    session: ManagementInstanceSessionsServerSessionsListOutputItemsSession
    server_deployment: ManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment
    created_at: datetime
    connection: Optional[ManagementInstanceSessionsServerSessionsListOutputItemsConnection] = None
@dataclass
class ManagementInstanceSessionsServerSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsServerSessionsListOutput:
    items: List[ManagementInstanceSessionsServerSessionsListOutputItems]
    pagination: ManagementInstanceSessionsServerSessionsListOutputPagination


class mapManagementInstanceSessionsServerSessionsListOutputItemsMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsMcpClient:
        return ManagementInstanceSessionsServerSessionsListOutputItemsMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsMcpServer:
        return ManagementInstanceSessionsServerSessionsListOutputItemsMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsMcp:
        return ManagementInstanceSessionsServerSessionsListOutputItemsMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceSessionsServerSessionsListOutputItemsMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceSessionsServerSessionsListOutputItemsMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsUsage:
        return ManagementInstanceSessionsServerSessionsListOutputItemsUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsServer:
        return ManagementInstanceSessionsServerSessionsListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage:
        return ManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsSession:
        return ManagementInstanceSessionsServerSessionsListOutputItemsSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapManagementInstanceSessionsServerSessionsListOutputItemsSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
        return ManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment:
        return ManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient:
        return ManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient(
        user_agent=data.get('user_agent'),
        anonymized_ip_address=data.get('anonymized_ip_address')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItemsConnection:
        return ManagementInstanceSessionsServerSessionsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        client=mapManagementInstanceSessionsServerSessionsListOutputItemsConnectionClient.from_dict(data.get('client')) if data.get('client') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputItems:
        return ManagementInstanceSessionsServerSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceSessionsServerSessionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceSessionsServerSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapManagementInstanceSessionsServerSessionsListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapManagementInstanceSessionsServerSessionsListOutputItemsSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapManagementInstanceSessionsServerSessionsListOutputItemsServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        connection=mapManagementInstanceSessionsServerSessionsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutputPagination:
        return ManagementInstanceSessionsServerSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListOutput:
        return ManagementInstanceSessionsServerSessionsListOutput(
        items=[mapManagementInstanceSessionsServerSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsServerSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsServerSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceSessionsServerSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsListQuery:
        return ManagementInstanceSessionsServerSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

