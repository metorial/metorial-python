from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp
    usage: ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceSessionsEventsListOutputItemsServerRunServer
    server_deployment: ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment
    server_session: ManagementInstanceSessionsEventsListOutputItemsServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp
    usage: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer
    server_deployment: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment
    server_session: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsServerRunError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun
    created_at: datetime
@dataclass
class ManagementInstanceSessionsEventsListOutputItemsLogLines:
    type: str
    line: str
@dataclass
class ManagementInstanceSessionsEventsListOutputItems:
    object: str
    id: str
    type: str
    session_id: str
    log_lines: List[ManagementInstanceSessionsEventsListOutputItemsLogLines]
    created_at: datetime
    server_run: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRun] = None
    server_run_error: Optional[ManagementInstanceSessionsEventsListOutputItemsServerRunError] = None
@dataclass
class ManagementInstanceSessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSessionsEventsListOutput:
    items: List[ManagementInstanceSessionsEventsListOutputItems]
    pagination: ManagementInstanceSessionsEventsListOutputPagination


class mapManagementInstanceSessionsEventsListOutputItemsServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunServerSession:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRun:
        return ManagementInstanceSessionsEventsListOutputItemsServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceSessionsEventsListOutputItemsServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsServerRunError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsServerRunError:
        return ManagementInstanceSessionsEventsListOutputItemsServerRunError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapManagementInstanceSessionsEventsListOutputItemsServerRunErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsServerRunError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItemsLogLines:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItemsLogLines:
        return ManagementInstanceSessionsEventsListOutputItemsLogLines(
        type=data.get('type'),
        line=data.get('line')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItemsLogLines, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputItems:
        return ManagementInstanceSessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        server_run=mapManagementInstanceSessionsEventsListOutputItemsServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        server_run_error=mapManagementInstanceSessionsEventsListOutputItemsServerRunError.from_dict(data.get('server_run_error')) if data.get('server_run_error') else None,
        log_lines=[mapManagementInstanceSessionsEventsListOutputItemsLogLines.from_dict(item) for item in data.get('log_lines', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutputPagination:
        return ManagementInstanceSessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListOutput:
        return ManagementInstanceSessionsEventsListOutput(
        items=[mapManagementInstanceSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSessionsEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_run_id: Optional[Union[str, List[str]]] = None
    server_session_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsEventsListQuery:
        return ManagementInstanceSessionsEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_run_id=data.get('server_run_id'),
        server_session_id=data.get('server_session_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

