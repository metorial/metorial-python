from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpTokensListOutputItemsServer:
    object: str
    id: str
    status: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensListOutputItemsEndpoint:
    object: str
    id: str
    status: str
    slug: str
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensListOutputItemsGroups:
    object: str
    id: str
    status: str
    slug: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpTokensListOutputItems:
    object: str
    id: str
    status: str
    secret: str
    groups: List[DashboardInstanceMagicMcpTokensListOutputItemsGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    server: Optional[DashboardInstanceMagicMcpTokensListOutputItemsServer] = None
    endpoint: Optional[DashboardInstanceMagicMcpTokensListOutputItemsEndpoint] = None
@dataclass
class DashboardInstanceMagicMcpTokensListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMagicMcpTokensListOutput:
    items: List[DashboardInstanceMagicMcpTokensListOutputItems]
    pagination: DashboardInstanceMagicMcpTokensListOutputPagination


class mapDashboardInstanceMagicMcpTokensListOutputItemsServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutputItemsServer:
        return DashboardInstanceMagicMcpTokensListOutputItemsServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutputItemsServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensListOutputItemsEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutputItemsEndpoint:
        return DashboardInstanceMagicMcpTokensListOutputItemsEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutputItemsEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutputItemsGroups:
        return DashboardInstanceMagicMcpTokensListOutputItemsGroups(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutputItems:
        return DashboardInstanceMagicMcpTokensListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        server=mapDashboardInstanceMagicMcpTokensListOutputItemsServer.from_dict(data.get('server')) if data.get('server') else None,
        endpoint=mapDashboardInstanceMagicMcpTokensListOutputItemsEndpoint.from_dict(data.get('endpoint')) if data.get('endpoint') else None,
        groups=[mapDashboardInstanceMagicMcpTokensListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutputPagination:
        return DashboardInstanceMagicMcpTokensListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpTokensListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListOutput:
        return DashboardInstanceMagicMcpTokensListOutput(
        items=[mapDashboardInstanceMagicMcpTokensListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMagicMcpTokensListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpTokensListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_group_id: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    magic_mcp_endpoint_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceMagicMcpTokensListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpTokensListQuery:
        return DashboardInstanceMagicMcpTokensListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        magic_mcp_group_id=data.get('magic_mcp_group_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        magic_mcp_endpoint_id=data.get('magic_mcp_endpoint_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpTokensListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

