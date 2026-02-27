from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsMcpClient:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsMcpServer:
    object: str
    capabilities: Dict[str, Any]
    name: Optional[str] = None
    version: Optional[str] = None
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItemsMcp:
    object: str
    version: Optional[str] = None
    connection_type: Optional[str] = None
    client: Optional[DashboardInstanceSessionsConnectionsListOutputItemsMcpClient] = None
    server: Optional[DashboardInstanceSessionsConnectionsListOutputItemsMcpServer] = None
@dataclass
class DashboardInstanceSessionsConnectionsListOutputItems:
    object: str
    id: str
    mcp: DashboardInstanceSessionsConnectionsListOutputItemsMcp
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
class DashboardInstanceSessionsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSessionsConnectionsListOutput:
    items: List[DashboardInstanceSessionsConnectionsListOutputItems]
    pagination: DashboardInstanceSessionsConnectionsListOutputPagination


class mapDashboardInstanceSessionsConnectionsListOutputItemsMcpClient:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsMcpClient:
        return DashboardInstanceSessionsConnectionsListOutputItemsMcpClient(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsMcpClient, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItemsMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsMcpServer:
        return DashboardInstanceSessionsConnectionsListOutputItemsMcpServer(
        object=data.get('object'),
        name=data.get('name'),
        version=data.get('version'),
        capabilities=data.get('capabilities')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItemsMcp:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItemsMcp:
        return DashboardInstanceSessionsConnectionsListOutputItemsMcp(
        object=data.get('object'),
        version=data.get('version'),
        connection_type=data.get('connection_type'),
        client=mapDashboardInstanceSessionsConnectionsListOutputItemsMcpClient.from_dict(data.get('client')) if data.get('client') else None,
        server=mapDashboardInstanceSessionsConnectionsListOutputItemsMcpServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItemsMcp, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputItems:
        return DashboardInstanceSessionsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        connection_state=data.get('connection_state'),
        mcp=mapDashboardInstanceSessionsConnectionsListOutputItemsMcp.from_dict(data.get('mcp')) if data.get('mcp') else None,
        metadata=data.get('metadata'),
        session_id=data.get('session_id'),
        session_provider_id=data.get('session_provider_id'),
        started_at=datetime.fromisoformat(data.get('started_at')) if data.get('started_at') else None,
        ended_at=datetime.fromisoformat(data.get('ended_at')) if data.get('ended_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutputPagination:
        return DashboardInstanceSessionsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListOutput:
        return DashboardInstanceSessionsConnectionsListOutput(
        items=[mapDashboardInstanceSessionsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSessionsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSessionsConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[str] = None
    connection_state: Optional[str] = None
    session_provider_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceSessionsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionsConnectionsListQuery:
        return DashboardInstanceSessionsConnectionsListQuery(
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
    def to_dict(value: Union[DashboardInstanceSessionsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
