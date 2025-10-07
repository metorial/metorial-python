from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient] = None
    server: Optional[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer] = None
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp
    usage: DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServerRunErrorsGetOutputServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceServerRunErrorsGetOutputServerRunServer
    server_deployment: DashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment
    server_session: DashboardInstanceServerRunErrorsGetOutputServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class DashboardInstanceServerRunErrorsGetOutput:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: DashboardInstanceServerRunErrorsGetOutputServerRun
    created_at: datetime


class mapDashboardInstanceServerRunErrorsGetOutputServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServer:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRunServerSession:
        return DashboardInstanceServerRunErrorsGetOutputServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutputServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutputServerRun:
        return DashboardInstanceServerRunErrorsGetOutputServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceServerRunErrorsGetOutputServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceServerRunErrorsGetOutputServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutputServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunErrorsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunErrorsGetOutput:
        return DashboardInstanceServerRunErrorsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapDashboardInstanceServerRunErrorsGetOutputServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunErrorsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

