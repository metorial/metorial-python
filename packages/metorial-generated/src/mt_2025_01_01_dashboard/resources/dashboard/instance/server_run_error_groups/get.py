from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp
    usage: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer
    server_deployment: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment
    server_session: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutputDefaultError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorGroupsGetOutput:
    object: str
    id: str
    code: str
    message: str
    fingerprint: str
    count: float
    created_at: datetime
    first_seen_at: datetime
    last_seen_at: datetime
    default_error: Optional[DashboardInstanceServerRunErrorGroupsGetOutputDefaultError] = None


class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutputDefaultError:
        return DashboardInstanceServerRunErrorGroupsGetOutputDefaultError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutputDefaultError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorGroupsGetOutput:
        return DashboardInstanceServerRunErrorGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        fingerprint=data.get('fingerprint'),
        count=data.get('count'),
        default_error=mapDashboardInstanceServerRunErrorGroupsGetOutputDefaultError.from_dict(data.get('default_error')) if data.get('default_error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

