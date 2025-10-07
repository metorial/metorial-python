from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServerRunsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServerRunsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServerRunsGetOutputServerSessionMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunsGetOutputServerSessionMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceServerRunsGetOutputServerSessionMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceServerRunsGetOutputServerSessionMcpClient] = None
    server: Optional[ManagementInstanceServerRunsGetOutputServerSessionMcpServer] = None
@dataclass
class ManagementInstanceServerRunsGetOutputServerSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceServerRunsGetOutputServerSession:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceServerRunsGetOutputServerSessionMcp
    usage: ManagementInstanceServerRunsGetOutputServerSessionUsage
    session_id: str
    created_at: datetime
@dataclass
class ManagementInstanceServerRunsGetOutput:
    object: str
    id: str
    type: str
    status: str
    server_version_id: str
    server: ManagementInstanceServerRunsGetOutputServer
    server_deployment: ManagementInstanceServerRunsGetOutputServerDeployment
    server_session: ManagementInstanceServerRunsGetOutputServerSession
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None


class mapManagementInstanceServerRunsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServer:
        return ManagementInstanceServerRunsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerDeploymentServer:
        return ManagementInstanceServerRunsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerDeployment:
        return ManagementInstanceServerRunsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServerRunsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerSessionMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerSessionMcpClient:
        return ManagementInstanceServerRunsGetOutputServerSessionMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerSessionMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerSessionMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerSessionMcpServer:
        return ManagementInstanceServerRunsGetOutputServerSessionMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerSessionMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerSessionMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerSessionMcp:
        return ManagementInstanceServerRunsGetOutputServerSessionMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceServerRunsGetOutputServerSessionMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceServerRunsGetOutputServerSessionMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerSessionMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerSessionUsage:
        return ManagementInstanceServerRunsGetOutputServerSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutputServerSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutputServerSession:
        return ManagementInstanceServerRunsGetOutputServerSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceServerRunsGetOutputServerSessionMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceServerRunsGetOutputServerSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        session_id=data.get('session_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutputServerSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServerRunsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServerRunsGetOutput:
        return ManagementInstanceServerRunsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        server_version_id=data.get('server_version_id'),
        server=mapManagementInstanceServerRunsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        server_deployment=mapManagementInstanceServerRunsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        server_session=mapManagementInstanceServerRunsGetOutputServerSession.from_dict(data.get('server_session')) if data.get('server_session') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        stopped_at=datetime.fromisoformat(data.get('stopped_at')) if data.get('stopped_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServerRunsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

