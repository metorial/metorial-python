from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp
    usage: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer
    server_deployment: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment
    server_session: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutputDefaultError:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorGroupsGetOutput:
    object: str
    id: str
    code: str
    message: str
    fingerprint: str
    count: float
    created_at: datetime
    first_seen_at: datetime
    last_seen_at: datetime
    default_error: Optional[ManagementInstanceServerRunErrorGroupsGetOutputDefaultError] = None


class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutputDefaultError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutputDefaultError:
        return ManagementInstanceServerRunErrorGroupsGetOutputDefaultError(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultErrorServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutputDefaultError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorGroupsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorGroupsGetOutput:
        return ManagementInstanceServerRunErrorGroupsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        fingerprint=data.get('fingerprint'),
        count=data.get('count'),
        default_error=mapManagementInstanceServerRunErrorGroupsGetOutputDefaultError.from_dict(data.get('default_error')) if data.get('default_error') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        first_seen_at=datetime.fromisoformat(data.get('first_seen_at')) if data.get('first_seen_at') else None,
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at')) if data.get('last_seen_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorGroupsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

