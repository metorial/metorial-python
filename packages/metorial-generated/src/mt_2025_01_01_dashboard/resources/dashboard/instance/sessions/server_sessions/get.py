from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputMcpClient:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputMcpServer:
    object: str
    name: str
    version: str
    capabilities: Dict[str, Any]
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputMcp:
    object: str
    version: str
    connection_type: str
    client: Optional[DashboardInstanceSessionsServerSessionsGetOutputMcpClient] = None
    server: Optional[DashboardInstanceSessionsServerSessionsGetOutputMcpServer] = None
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputSessionUsage:
    total_productive_message_count: float
    total_productive_client_message_count: float
    total_productive_server_message_count: float
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputSession:
    object: str
    id: str
    status: str
    connection_status: str
    usage: DashboardInstanceSessionsServerSessionsGetOutputSessionUsage
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputConnectionClient:
    user_agent: str
    anonymized_ip_address: str
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutputConnection:
    object: str
    id: str
    client: DashboardInstanceSessionsServerSessionsGetOutputConnectionClient
    created_at: datetime
    started_at: datetime
    ended_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSessionsServerSessionsGetOutput:
    object: str
    id: str
    status: str
    mcp: DashboardInstanceSessionsServerSessionsGetOutputMcp
    usage: DashboardInstanceSessionsServerSessionsGetOutputUsage
    server: DashboardInstanceSessionsServerSessionsGetOutputServer
    session: DashboardInstanceSessionsServerSessionsGetOutputSession
    server_deployment: DashboardInstanceSessionsServerSessionsGetOutputServerDeployment
    created_at: datetime
    connection: Optional[DashboardInstanceSessionsServerSessionsGetOutputConnection] = None


class mapDashboardInstanceSessionsServerSessionsGetOutputMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputMcpClient:
        return DashboardInstanceSessionsServerSessionsGetOutputMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputMcpServer:
        return DashboardInstanceSessionsServerSessionsGetOutputMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputMcp:
        return DashboardInstanceSessionsServerSessionsGetOutputMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsServerSessionsGetOutputMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsServerSessionsGetOutputMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputUsage:
        return DashboardInstanceSessionsServerSessionsGetOutputUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputServer:
        return DashboardInstanceSessionsServerSessionsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputSessionUsage:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputSessionUsage:
        return DashboardInstanceSessionsServerSessionsGetOutputSessionUsage(
        total_productive_message_count=data.get('total_productive_message_count'),
        total_productive_client_message_count=data.get('total_productive_client_message_count'),
        total_productive_server_message_count=data.get('total_productive_server_message_count')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputSessionUsage, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputSession:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputSession:
        return DashboardInstanceSessionsServerSessionsGetOutputSession(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_status=data.get('connection_status'),
        usage=mapDashboardInstanceSessionsServerSessionsGetOutputSessionUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputSession, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer:
        return DashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputServerDeployment:
        return DashboardInstanceSessionsServerSessionsGetOutputServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceSessionsServerSessionsGetOutputServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputConnectionClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputConnectionClient:
        return DashboardInstanceSessionsServerSessionsGetOutputConnectionClient(
        user_agent=data.get('user_agent'),
        anonymized_ip_address=data.get('anonymized_ip_address')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputConnectionClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutputConnection:
        return DashboardInstanceSessionsServerSessionsGetOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        client=mapDashboardInstanceSessionsServerSessionsGetOutputConnectionClient.from_dict(data.get('client')) if data.get('client') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsServerSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsServerSessionsGetOutput:
        return DashboardInstanceSessionsServerSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        mcp=mapDashboardInstanceSessionsServerSessionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        usage=mapDashboardInstanceSessionsServerSessionsGetOutputUsage.from_dict(data.get('usage')) if data.get('usage') else None,
        server=mapDashboardInstanceSessionsServerSessionsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        session=mapDashboardInstanceSessionsServerSessionsGetOutputSession.from_dict(data.get('session')) if data.get('session') else None,
        server_deployment=mapDashboardInstanceSessionsServerSessionsGetOutputServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        connection=mapDashboardInstanceSessionsServerSessionsGetOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsServerSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

