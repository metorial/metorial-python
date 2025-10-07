from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp
    usage: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer
    server_deployment: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment
    server_session: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    fingerprint: str
    count: float
    created_at: datetime
    first_seen_at: datetime
    last_seen_at: datetime
    default_error: Optional[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceServerRunErrorGroupsListOutput:
    items: List[DashboardInstanceServerRunErrorGroupsListOutputItems]
    pagination: DashboardInstanceServerRunErrorGroupsListOutputPagination


class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError:
        return DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputItems:
        return DashboardInstanceServerRunErrorGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        fingerprint=data.get('fingerprint'),
        count=data.get('count'),
        default_error=mapDashboardInstanceServerRunErrorGroupsListOutputItemsDefaultError.from_dict(data.get('default_error')) if data.get('default_error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutputPagination:
        return DashboardInstanceServerRunErrorGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListOutput:
        return DashboardInstanceServerRunErrorGroupsListOutput(
        items=[mapDashboardInstanceServerRunErrorGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceServerRunErrorGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceServerRunErrorGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceServerRunErrorGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsListQuery:
        return DashboardInstanceServerRunErrorGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_id=data.get('server_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

