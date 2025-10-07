from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceSessionsConnectionsGetOutputMcpClient] = None
    server: Optional[DashboardInstanceSessionsConnectionsGetOutputMcpServer] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: DashboardInstanceSessionsConnectionsGetOutputSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceSessionsConnectionsGetOutputMcp
    usage: DashboardInstanceSessionsConnectionsGetOutputUsage
    server: DashboardInstanceSessionsConnectionsGetOutputServer
    session: DashboardInstanceSessionsConnectionsGetOutputSession
    server_deployment: DashboardInstanceSessionsConnectionsGetOutputServerDeployment
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None


class mapDashboardInstanceSessionsConnectionsGetOutputMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputMcpClient:
        return DashboardInstanceSessionsConnectionsGetOutputMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputMcpServer:
        return DashboardInstanceSessionsConnectionsGetOutputMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputMcp:
        return DashboardInstanceSessionsConnectionsGetOutputMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsConnectionsGetOutputMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsConnectionsGetOutputMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputUsage:
        return DashboardInstanceSessionsConnectionsGetOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputServer:
        return DashboardInstanceSessionsConnectionsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputSessionUsage:
        return DashboardInstanceSessionsConnectionsGetOutputSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputSession:
        return DashboardInstanceSessionsConnectionsGetOutputSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapDashboardInstanceSessionsConnectionsGetOutputSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer:
        return DashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutputServerDeployment:
        return DashboardInstanceSessionsConnectionsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsConnectionsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutput:
        return DashboardInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceSessionsConnectionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapDashboardInstanceSessionsConnectionsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapDashboardInstanceSessionsConnectionsGetOutputSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapDashboardInstanceSessionsConnectionsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

