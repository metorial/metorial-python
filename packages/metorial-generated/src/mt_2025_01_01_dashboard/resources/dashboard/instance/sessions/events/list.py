from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp
    usage: DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceSessionsEventsListOutputItemsServerRunServer
    server_deployment: DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment
    server_session: DashboardInstanceSessionsEventsListOutputItemsServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp
    usage: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer
    server_deployment: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment
    server_session: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsServerRunError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun
    created_at: datetime
@dataclass
class DashboardInstanceSessionsEventsListOutputItemsLogLines:
    type: str
    line: str
@dataclass
class DashboardInstanceSessionsEventsListOutputItems:
    object: str
    id: str
    type: str
    session_id: str
    log_lines: List[DashboardInstanceSessionsEventsListOutputItemsLogLines]
    created_at: datetime
    server_run: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRun] = None
    server_run_error: Optional[DashboardInstanceSessionsEventsListOutputItemsServerRunError] = None
@dataclass
class DashboardInstanceSessionsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsEventsListOutput:
    items: List[DashboardInstanceSessionsEventsListOutputItems]
    pagination: DashboardInstanceSessionsEventsListOutputPagination


class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunServerSession:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRun:
        return DashboardInstanceSessionsEventsListOutputItemsServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceSessionsEventsListOutputItemsServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsServerRunError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsServerRunError:
        return DashboardInstanceSessionsEventsListOutputItemsServerRunError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapDashboardInstanceSessionsEventsListOutputItemsServerRunErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsServerRunError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItemsLogLines:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItemsLogLines:
        return DashboardInstanceSessionsEventsListOutputItemsLogLines(
        type=data.get('type'),
        line=data.get('line')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItemsLogLines, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputItems:
        return DashboardInstanceSessionsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        session_id=data.get('session_id'),
        server_run=mapDashboardInstanceSessionsEventsListOutputItemsServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        server_run_error=mapDashboardInstanceSessionsEventsListOutputItemsServerRunError.from_dict(data.get('server_run_error')) if data.get('server_run_error') else None,
        log_lines=[mapDashboardInstanceSessionsEventsListOutputItemsLogLines.from_dict(item) for item in data.get('log_lines', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutputPagination:
        return DashboardInstanceSessionsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListOutput:
        return DashboardInstanceSessionsEventsListOutput(
        items=[mapDashboardInstanceSessionsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_run_id: Optional[Union[str, List[str]]] = None
    server_session_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSessionsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsEventsListQuery:
        return DashboardInstanceSessionsEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_run_id=data.get('server_run_id'),
        server_session_id=data.get('server_session_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

