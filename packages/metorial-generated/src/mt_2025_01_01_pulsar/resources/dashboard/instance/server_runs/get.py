from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServerRunsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServerRunsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServerRunsGetOutputServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunsGetOutputServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceServerRunsGetOutputServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceServerRunsGetOutputServerSessionMcpClient] = None
    server: Optional[DashboardInstanceServerRunsGetOutputServerSessionMcpServer] = None
@dataclass
class DashboardInstanceServerRunsGetOutputServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceServerRunsGetOutputServerSession:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceServerRunsGetOutputServerSessionMcp
    usage: DashboardInstanceServerRunsGetOutputServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class DashboardInstanceServerRunsGetOutput:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: DashboardInstanceServerRunsGetOutputServer
    server_deployment: DashboardInstanceServerRunsGetOutputServerDeployment
    server_session: DashboardInstanceServerRunsGetOutputServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None


class mapDashboardInstanceServerRunsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServer:
        return DashboardInstanceServerRunsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerDeploymentServer:
        return DashboardInstanceServerRunsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerDeployment:
        return DashboardInstanceServerRunsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServerRunsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerSessionMcpClient:
        return DashboardInstanceServerRunsGetOutputServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerSessionMcpServer:
        return DashboardInstanceServerRunsGetOutputServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerSessionMcp:
        return DashboardInstanceServerRunsGetOutputServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceServerRunsGetOutputServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceServerRunsGetOutputServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerSessionUsage:
        return DashboardInstanceServerRunsGetOutputServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutputServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutputServerSession:
        return DashboardInstanceServerRunsGetOutputServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceServerRunsGetOutputServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceServerRunsGetOutputServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutputServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServerRunsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServerRunsGetOutput:
        return DashboardInstanceServerRunsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapDashboardInstanceServerRunsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapDashboardInstanceServerRunsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapDashboardInstanceServerRunsGetOutputServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServerRunsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

