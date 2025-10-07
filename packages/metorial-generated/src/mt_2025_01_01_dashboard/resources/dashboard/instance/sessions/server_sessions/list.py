from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceSessionsServerSessionsListOutputItemsMcpClient] = None
    server: Optional[DashboardInstanceSessionsServerSessionsListOutputItemsMcpServer] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: DashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient:
    user_agent: str
    anonymized_ip_address: str
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItemsConnection:
    object: str
    id: str
    client: DashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputItems:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceSessionsServerSessionsListOutputItemsMcp
    usage: DashboardInstanceSessionsServerSessionsListOutputItemsUsage
    server: DashboardInstanceSessionsServerSessionsListOutputItemsServer
    session: DashboardInstanceSessionsServerSessionsListOutputItemsSession
    server_deployment: DashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment
    created_at: datetime
    connection: Optional[DashboardInstanceSessionsServerSessionsListOutputItemsConnection] = None
@dataclass
class DashboardInstanceSessionsServerSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsServerSessionsListOutput:
    items: List[DashboardInstanceSessionsServerSessionsListOutputItems]
    pagination: DashboardInstanceSessionsServerSessionsListOutputPagination


class mapDashboardInstanceSessionsServerSessionsListOutputItemsMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsMcpClient:
        return DashboardInstanceSessionsServerSessionsListOutputItemsMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsMcpServer:
        return DashboardInstanceSessionsServerSessionsListOutputItemsMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsMcp:
        return DashboardInstanceSessionsServerSessionsListOutputItemsMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsServerSessionsListOutputItemsMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsServerSessionsListOutputItemsMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsUsage:
        return DashboardInstanceSessionsServerSessionsListOutputItemsUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsServer:
        return DashboardInstanceSessionsServerSessionsListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage:
        return DashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsSession:
        return DashboardInstanceSessionsServerSessionsListOutputItemsSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapDashboardInstanceSessionsServerSessionsListOutputItemsSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer:
        return DashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment:
        return DashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsServerSessionsListOutputItemsServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient:
        return DashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient(
        user_agent=data.get('user_agent'),
        anonymized_ip_address=data.get('anonymized_ip_address')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItemsConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItemsConnection:
        return DashboardInstanceSessionsServerSessionsListOutputItemsConnection(
        object=data.get('object'),
        id=data.get('id'),
        client=mapDashboardInstanceSessionsServerSessionsListOutputItemsConnectionClient.from_dict(data.get('client')) if data.get('client') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItemsConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputItems:
        return DashboardInstanceSessionsServerSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceSessionsServerSessionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceSessionsServerSessionsListOutputItemsUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapDashboardInstanceSessionsServerSessionsListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapDashboardInstanceSessionsServerSessionsListOutputItemsSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapDashboardInstanceSessionsServerSessionsListOutputItemsServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        connection=mapDashboardInstanceSessionsServerSessionsListOutputItemsConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutputPagination:
        return DashboardInstanceSessionsServerSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListOutput:
        return DashboardInstanceSessionsServerSessionsListOutput(
        items=[mapDashboardInstanceSessionsServerSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsServerSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsServerSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSessionsServerSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsListQuery:
        return DashboardInstanceSessionsServerSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

