from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceSessionsServerSessionsGetOutputMcpClient] = None
    server: Optional[ManagementInstanceSessionsServerSessionsGetOutputMcpServer] = None
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: ManagementInstanceSessionsServerSessionsGetOutputSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputConnectionClient:
    user_agent: str
    anonymized_ip_address: str
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutputConnection:
    object: str
    id: str
    client: ManagementInstanceSessionsServerSessionsGetOutputConnectionClient
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSessionsServerSessionsGetOutput:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceSessionsServerSessionsGetOutputMcp
    usage: ManagementInstanceSessionsServerSessionsGetOutputUsage
    server: ManagementInstanceSessionsServerSessionsGetOutputServer
    session: ManagementInstanceSessionsServerSessionsGetOutputSession
    server_deployment: ManagementInstanceSessionsServerSessionsGetOutputServerDeployment
    created_at: datetime
    connection: Optional[ManagementInstanceSessionsServerSessionsGetOutputConnection] = None


class mapManagementInstanceSessionsServerSessionsGetOutputMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputMcpClient:
        return ManagementInstanceSessionsServerSessionsGetOutputMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputMcpServer:
        return ManagementInstanceSessionsServerSessionsGetOutputMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputMcp:
        return ManagementInstanceSessionsServerSessionsGetOutputMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceSessionsServerSessionsGetOutputMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceSessionsServerSessionsGetOutputMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputUsage:
        return ManagementInstanceSessionsServerSessionsGetOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputServer:
        return ManagementInstanceSessionsServerSessionsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputSessionUsage:
        return ManagementInstanceSessionsServerSessionsGetOutputSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputSession:
        return ManagementInstanceSessionsServerSessionsGetOutputSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapManagementInstanceSessionsServerSessionsGetOutputSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
        return ManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputServerDeployment:
        return ManagementInstanceSessionsServerSessionsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsServerSessionsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputConnectionClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputConnectionClient:
        return ManagementInstanceSessionsServerSessionsGetOutputConnectionClient(
        user_agent=data.get('user_agent'),
        anonymized_ip_address=data.get('anonymized_ip_address')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputConnectionClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutputConnection:
        return ManagementInstanceSessionsServerSessionsGetOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        client=mapManagementInstanceSessionsServerSessionsGetOutputConnectionClient.from_dict(data.get('client')) if data.get('client') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsServerSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsServerSessionsGetOutput:
        return ManagementInstanceSessionsServerSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceSessionsServerSessionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceSessionsServerSessionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapManagementInstanceSessionsServerSessionsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapManagementInstanceSessionsServerSessionsGetOutputSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapManagementInstanceSessionsServerSessionsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        connection=mapManagementInstanceSessionsServerSessionsGetOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsServerSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

