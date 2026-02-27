from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcpClient:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcpServer:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutputMcp:
    object: str
    version: Optional[str] = None
    connection_type: Optional[str] = None
    client: Optional[DashboardInstanceSessionsConnectionsGetOutputMcpClient] = None
    server: Optional[DashboardInstanceSessionsConnectionsGetOutputMcpServer] = None
@dataclass
class DashboardInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    mcp: DashboardInstanceSessionsConnectionsGetOutputMcp
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    connection_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    started_at: Optional[datetime] = None
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

class mapDashboardInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsGetOutput:
        return DashboardInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        mcp=mapDashboardInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
