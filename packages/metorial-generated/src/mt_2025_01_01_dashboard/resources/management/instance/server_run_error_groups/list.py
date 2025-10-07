from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp
    usage: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer
    server_deployment: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment
    server_session: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputItems:
    object: str
    id: str
    code: str
    message: str
    fingerprint: str
    count: float
    created_at: datetime
    first_seen_at: datetime
    last_seen_at: datetime
    default_error: Optional[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceServerRunErrorGroupsListOutput:
    items: List[ManagementInstanceServerRunErrorGroupsListOutputItems]
    pagination: ManagementInstanceServerRunErrorGroupsListOutputPagination


class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError:
        return ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputItems:
        return ManagementInstanceServerRunErrorGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        fingerprint=data.get('fingerprint'),
        count=data.get('count'),
        default_error=mapManagementInstanceServerRunErrorGroupsListOutputItemsDefaultError.from_dict(data.get('default_error')) if data.get('default_error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutputPagination:
        return ManagementInstanceServerRunErrorGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListOutput:
        return ManagementInstanceServerRunErrorGroupsListOutput(
        items=[mapManagementInstanceServerRunErrorGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceServerRunErrorGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServerRunErrorGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceServerRunErrorGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsListQuery:
        return ManagementInstanceServerRunErrorGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_id=data.get('server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

