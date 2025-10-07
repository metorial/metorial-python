from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient] = None
    server: Optional[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer] = None
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRunServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp
    usage: ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServerRunErrorsGetOutputServerRun:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceServerRunErrorsGetOutputServerRunServer
    server_deployment: ManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment
    server_session: ManagementInstanceServerRunErrorsGetOutputServerRunServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
@dataclass
class ManagementInstanceServerRunErrorsGetOutput:
    object: str
    id: str
    code: str
    message: str
    metadata: Dict[str, Any]
    server_run: ManagementInstanceServerRunErrorsGetOutputServerRun
    created_at: datetime


class mapManagementInstanceServerRunErrorsGetOutputServerRunServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServer:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServerRunErrorsGetOutputServerRunServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRunServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRunServerSession:
        return ManagementInstanceServerRunErrorsGetOutputServerRunServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceServerRunErrorsGetOutputServerRunServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRunServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutputServerRun:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutputServerRun:
        return ManagementInstanceServerRunErrorsGetOutputServerRun(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceServerRunErrorsGetOutputServerRunServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceServerRunErrorsGetOutputServerRunServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceServerRunErrorsGetOutputServerRunServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutputServerRun, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunErrorsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunErrorsGetOutput:
        return ManagementInstanceServerRunErrorsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        code=data.get('code'),
        message=data.get('message'),
        metadata=data.get('metadata'),
        server_run=mapManagementInstanceServerRunErrorsGetOutputServerRun.from_dict(data.get('server_run')) if data.get('server_run') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunErrorsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

