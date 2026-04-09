from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerGroupsListOutputItems:
    object: str
    id: str
    status: str
    name: str
    is_default: bool
    sso_group_ids: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsConsumerGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsConsumerGroupsListOutput:
    items: List[PortalsConsumerGroupsListOutputItems]
    pagination: PortalsConsumerGroupsListOutputPagination


class mapPortalsConsumerGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsListOutputItems:
        return PortalsConsumerGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        is_default=data.get('is_default'),
        sso_group_ids=data.get('sso_group_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsListOutputPagination:
        return PortalsConsumerGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsListOutput:
        return PortalsConsumerGroupsListOutput(
        items=[mapPortalsConsumerGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsConsumerGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapPortalsConsumerGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerGroupsListQuery:
        return PortalsConsumerGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

