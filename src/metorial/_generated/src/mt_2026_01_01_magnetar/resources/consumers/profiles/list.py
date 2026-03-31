from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersProfilesListOutputItemsGroupsGroup:
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
class ConsumersProfilesListOutputItemsGroups:
    object: str
    group: ConsumersProfilesListOutputItemsGroupsGroup
    assigned_via: str
@dataclass
class ConsumersProfilesListOutputItems:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[ConsumersProfilesListOutputItemsGroups]] = None
@dataclass
class ConsumersProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumersProfilesListOutput:
    items: List[ConsumersProfilesListOutputItems]
    pagination: ConsumersProfilesListOutputPagination


class mapConsumersProfilesListOutputItemsGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListOutputItemsGroupsGroup:
        return ConsumersProfilesListOutputItemsGroupsGroup(
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
    def to_dict(value: Union[ConsumersProfilesListOutputItemsGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersProfilesListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListOutputItemsGroups:
        return ConsumersProfilesListOutputItemsGroups(
        object=data.get('object'),
        group=mapConsumersProfilesListOutputItemsGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        assigned_via=data.get('assigned_via')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersProfilesListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersProfilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListOutputItems:
        return ConsumersProfilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapConsumersProfilesListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersProfilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListOutputPagination:
        return ConsumersProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListOutput:
        return ConsumersProfilesListOutput(
        items=[mapConsumersProfilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumersProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumersProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapConsumersProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersProfilesListQuery:
        return ConsumersProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

