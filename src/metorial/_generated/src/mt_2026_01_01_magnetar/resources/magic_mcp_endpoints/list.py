from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpEndpointsListOutputItems:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpEndpointsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpEndpointsListOutput:
    items: List[MagicMcpEndpointsListOutputItems]
    pagination: MagicMcpEndpointsListOutputPagination


class mapMagicMcpEndpointsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsListOutputItems:
        return MagicMcpEndpointsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsListOutputPagination:
        return MagicMcpEndpointsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpEndpointsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsListOutput:
        return MagicMcpEndpointsListOutput(
        items=[mapMagicMcpEndpointsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpEndpointsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpEndpointsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapMagicMcpEndpointsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpEndpointsListQuery:
        return MagicMcpEndpointsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpEndpointsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

