from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpGroupsListOutputItems:
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
class MagicMcpGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpGroupsListOutput:
    items: List[MagicMcpGroupsListOutputItems]
    pagination: MagicMcpGroupsListOutputPagination


class mapMagicMcpGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsListOutputItems:
        return MagicMcpGroupsListOutputItems(
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
    def to_dict(value: Union[MagicMcpGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsListOutputPagination:
        return MagicMcpGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsListOutput:
        return MagicMcpGroupsListOutput(
        items=[mapMagicMcpGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapMagicMcpGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpGroupsListQuery:
        return MagicMcpGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

