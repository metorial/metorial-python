from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp
    usage: ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorsListOutputItemsServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceServerRunErrorsListOutputItemsServerRunServer
    server_deployment: ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment
    server_session: ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceServerRunErrorsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: ManagementInstanceServerRunErrorsListOutputItemsServerRun
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceServerRunErrorsListOutput:
    items: List[ManagementInstanceServerRunErrorsListOutputItems]
    pagination: ManagementInstanceServerRunErrorsListOutputPagination


class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServer:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItemsServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItemsServerRun:
        return ManagementInstanceServerRunErrorsListOutputItemsServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceServerRunErrorsListOutputItemsServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItemsServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputItems:
        return ManagementInstanceServerRunErrorsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapManagementInstanceServerRunErrorsListOutputItemsServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutputPagination:
        return ManagementInstanceServerRunErrorsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListOutput:
        return ManagementInstanceServerRunErrorsListOutput(
        items=[mapManagementInstanceServerRunErrorsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceServerRunErrorsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServerRunErrorsListQuery:
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


class mapManagementInstanceServerRunErrorsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsListQuery:
        return ManagementInstanceServerRunErrorsListQuery(
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
    def to_dict(value: Union[ManagementInstanceServerRunErrorsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

