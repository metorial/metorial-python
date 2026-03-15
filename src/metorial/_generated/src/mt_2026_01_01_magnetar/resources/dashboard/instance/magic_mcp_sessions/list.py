from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
    object: str
    id: str
    status: str
    session_template_id: str
    endpoints: List[DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpSessionsListOutputItems:
    object: str
    id: str
    subspace_session_id: str
    subspace_session_template_id: str
    magic_mcp_server: DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceMagicMcpSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMagicMcpSessionsListOutput:
    items: List[DashboardInstanceMagicMcpSessionsListOutputItems]
    pagination: DashboardInstanceMagicMcpSessionsListOutputPagination


class mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
        return DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
        return DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_template_id=data.get('session_template_id'),
        endpoints=[mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutputItems:
        return DashboardInstanceMagicMcpSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        subspace_session_id=data.get('subspace_session_id'),
        subspace_session_template_id=data.get('subspace_session_template_id'),
        magic_mcp_server=mapDashboardInstanceMagicMcpSessionsListOutputItemsMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutputPagination:
        return DashboardInstanceMagicMcpSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListOutput:
        return DashboardInstanceMagicMcpSessionsListOutput(
        items=[mapDashboardInstanceMagicMcpSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMagicMcpSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceMagicMcpSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpSessionsListQuery:
        return DashboardInstanceMagicMcpSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

