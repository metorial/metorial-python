from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpServersListOutputItemsEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpServersListOutputItems:
    object: str
    id: str
    status: str
    session_template_id: str
    endpoints: List[MagicMcpServersListOutputItemsEndpoints]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpServersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpServersListOutput:
    items: List[MagicMcpServersListOutputItems]
    pagination: MagicMcpServersListOutputPagination


class mapMagicMcpServersListOutputItemsEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputItemsEndpoints:
        return MagicMcpServersListOutputItemsEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersListOutputItemsEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputItems:
        return MagicMcpServersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        session_template_id=data.get('session_template_id'),
        endpoints=[mapMagicMcpServersListOutputItemsEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputPagination:
        return MagicMcpServersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutput:
        return MagicMcpServersListOutput(
        items=[mapMagicMcpServersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpServersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpServersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_group_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapMagicMcpServersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersListQuery:
        return MagicMcpServersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        magic_mcp_group_id=data.get('magic_mcp_group_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

