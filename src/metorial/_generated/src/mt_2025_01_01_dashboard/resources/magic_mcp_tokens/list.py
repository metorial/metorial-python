from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpTokensListOutputItemsGroups:
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
class MagicMcpTokensListOutputItems:
    object: str
    id: str
    status: str
    secret: str
    groups: List[MagicMcpTokensListOutputItemsGroups]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpTokensListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpTokensListOutput:
    items: List[MagicMcpTokensListOutputItems]
    pagination: MagicMcpTokensListOutputPagination


class mapMagicMcpTokensListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensListOutputItemsGroups:
        return MagicMcpTokensListOutputItemsGroups(
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
    def to_dict(value: Union[MagicMcpTokensListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensListOutputItems:
        return MagicMcpTokensListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret=data.get('secret'),
        name=data.get('name'),
        description=data.get('description'),
        groups=[mapMagicMcpTokensListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensListOutputPagination:
        return MagicMcpTokensListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpTokensListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensListOutput:
        return MagicMcpTokensListOutput(
        items=[mapMagicMcpTokensListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpTokensListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpTokensListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_group_id: Optional[Union[str, List[str]]] = None


class mapMagicMcpTokensListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpTokensListQuery:
        return MagicMcpTokensListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        magic_mcp_group_id=data.get('magic_mcp_group_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpTokensListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

