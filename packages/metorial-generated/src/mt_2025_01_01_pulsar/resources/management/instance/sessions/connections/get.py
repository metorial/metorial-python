from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[ManagementInstanceSessionsConnectionsGetOutputMcpClient] = None
    server: Optional[ManagementInstanceSessionsConnectionsGetOutputMcpServer] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: ManagementInstanceSessionsConnectionsGetOutputSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    status: str
    mcp: ManagementInstanceSessionsConnectionsGetOutputMcp
    usage: ManagementInstanceSessionsConnectionsGetOutputUsage
    server: ManagementInstanceSessionsConnectionsGetOutputServer
    session: ManagementInstanceSessionsConnectionsGetOutputSession
    server_deployment: ManagementInstanceSessionsConnectionsGetOutputServerDeployment
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None


class mapManagementInstanceSessionsConnectionsGetOutputMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputMcpClient:
        return ManagementInstanceSessionsConnectionsGetOutputMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputMcpServer:
        return ManagementInstanceSessionsConnectionsGetOutputMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputMcp:
        return ManagementInstanceSessionsConnectionsGetOutputMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapManagementInstanceSessionsConnectionsGetOutputMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapManagementInstanceSessionsConnectionsGetOutputMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputUsage:
        return ManagementInstanceSessionsConnectionsGetOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputServer:
        return ManagementInstanceSessionsConnectionsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputSessionUsage:
        return ManagementInstanceSessionsConnectionsGetOutputSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputSession:
        return ManagementInstanceSessionsConnectionsGetOutputSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapManagementInstanceSessionsConnectionsGetOutputSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer:
        return ManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutputServerDeployment:
        return ManagementInstanceSessionsConnectionsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceSessionsConnectionsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutput:
        return ManagementInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapManagementInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapManagementInstanceSessionsConnectionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapManagementInstanceSessionsConnectionsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapManagementInstanceSessionsConnectionsGetOutputSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapManagementInstanceSessionsConnectionsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

