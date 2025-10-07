from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp
    usage: DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorsListOutputItemsServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceServerRunErrorsListOutputItemsServerRunServer
    server_deployment: DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment
    server_session: DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceServerRunErrorsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: DashboardInstanceServerRunErrorsListOutputItemsServerRun
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceServerRunErrorsListOutput:
    items: List[DashboardInstanceServerRunErrorsListOutputItems]
    pagination: DashboardInstanceServerRunErrorsListOutputPagination


class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServer:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItemsServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItemsServerRun:
        return DashboardInstanceServerRunErrorsListOutputItemsServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceServerRunErrorsListOutputItemsServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItemsServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputItems:
        return DashboardInstanceServerRunErrorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapDashboardInstanceServerRunErrorsListOutputItemsServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutputPagination:
        return DashboardInstanceServerRunErrorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListOutput:
        return DashboardInstanceServerRunErrorsListOutput(
        items=[mapDashboardInstanceServerRunErrorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceServerRunErrorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceServerRunErrorsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_session_id: Optional[Union[str, List[str]]] = None
    server_implementation_id: Optional[Union[str, List[str]]] = None
    server_deployment_id: Optional[Union[str, List[str]]] = None
    server_run_id: Optional[Union[str, List[str]]] = None
    server_run_error_group_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceServerRunErrorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsListQuery:
        return DashboardInstanceServerRunErrorsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_session_id=data.get('server_session_id'),
        server_implementation_id=data.get('server_implementation_id'),
        server_deployment_id=data.get('server_deployment_id'),
        server_run_id=data.get('server_run_id'),
        server_run_error_group_id=data.get('server_run_error_group_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

