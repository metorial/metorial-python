from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcpClient:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcpServer:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutputMcp:
    object: str
    version: Optional[str] = None
    connection_type: Optional[str] = None
    client: Optional[ManagementInstanceSessionsConnectionsGetOutputMcpClient] = None
    server: Optional[ManagementInstanceSessionsConnectionsGetOutputMcpServer] = None
@dataclass
class ManagementInstanceSessionsConnectionsGetOutput:
    object: str
    id: str
    mcp: ManagementInstanceSessionsConnectionsGetOutputMcp
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    connection_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    started_at: Optional[datetime] = None
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

class mapManagementInstanceSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSessionsConnectionsGetOutput:
        return ManagementInstanceSessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        mcp=mapManagementInstanceSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
