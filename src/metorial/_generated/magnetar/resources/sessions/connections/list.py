from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionsConnectionsListOutputItemsMcpClient:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class SessionsConnectionsListOutputItemsMcpServer:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class SessionsConnectionsListOutputItemsMcp:
    object: str
    version: Optional[str] = None
    connection_type: Optional[str] = None
    client: Optional[SessionsConnectionsListOutputItemsMcpClient] = None
    server: Optional[SessionsConnectionsListOutputItemsMcpServer] = None
@dataclass
class SessionsConnectionsListOutputItems:
    object: str
    id: str
    mcp: SessionsConnectionsListOutputItemsMcp
    session_id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    connection_state: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    session_provider_id: Optional[str] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
@dataclass
class SessionsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SessionsConnectionsListOutput:
    items: List[SessionsConnectionsListOutputItems]
    pagination: SessionsConnectionsListOutputPagination


class mapSessionsConnectionsListOutputItemsMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcpClient:
        return SessionsConnectionsListOutputItemsMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutputItemsMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsListOutputItemsMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcpServer:
        return SessionsConnectionsListOutputItemsMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutputItemsMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItemsMcp:
        return SessionsConnectionsListOutputItemsMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapSessionsConnectionsListOutputItemsMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapSessionsConnectionsListOutputItemsMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputItems:
        return SessionsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        mcp=mapSessionsConnectionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutputPagination:
        return SessionsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListOutput:
        return SessionsConnectionsListOutput(
        items=[mapSessionsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSessionsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionsConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[str] = None
    connection_state: Optional[str] = None
    session_provider_id: Optional[Union[str, List[str]]] = None


class mapSessionsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsConnectionsListQuery:
        return SessionsConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        session_provider_id=data.get('session_provider_id')
        )

    @staticmethod
    def to_dict(value: Union[SessionsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
