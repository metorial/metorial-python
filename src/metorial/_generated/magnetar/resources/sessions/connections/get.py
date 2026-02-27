from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsConnectionsGetOutputMcpClient:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class SessionsConnectionsGetOutputMcpServer:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class SessionsConnectionsGetOutputMcp:
    object: str
    version: Optional[str] = None
    connection_type: Optional[str] = None
    client: Optional[SessionsConnectionsGetOutputMcpClient] = None
    server: Optional[SessionsConnectionsGetOutputMcpServer] = None
@dataclass
class SessionsConnectionsGetOutput:
    object: str
    id: str
    mcp: SessionsConnectionsGetOutputMcp
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    connection_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class mapSessionsConnectionsGetOutputMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcpClient:
        return SessionsConnectionsGetOutputMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutputMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcpServer:
        return SessionsConnectionsGetOutputMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutputMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutputMcp:
        return SessionsConnectionsGetOutputMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapSessionsConnectionsGetOutputMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapSessionsConnectionsGetOutputMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutputMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsGetOutput:
        return SessionsConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        mcp=mapSessionsConnectionsGetOutputMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
