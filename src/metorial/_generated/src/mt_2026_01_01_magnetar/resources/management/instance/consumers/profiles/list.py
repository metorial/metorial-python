from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersProfilesListOutputItemsGroupsGroup:
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
class ManagementInstanceConsumersProfilesListOutputItemsGroups:
    object: str
    group: ManagementInstanceConsumersProfilesListOutputItemsGroupsGroup
    assigned_via: str
@dataclass
class ManagementInstanceConsumersProfilesListOutputItems:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[ManagementInstanceConsumersProfilesListOutputItemsGroups]] = None
@dataclass
class ManagementInstanceConsumersProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConsumersProfilesListOutput:
    items: List[ManagementInstanceConsumersProfilesListOutputItems]
    pagination: ManagementInstanceConsumersProfilesListOutputPagination


class mapManagementInstanceConsumersProfilesListOutputItemsGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutputItemsGroupsGroup:
        return ManagementInstanceConsumersProfilesListOutputItemsGroupsGroup(
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
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutputItemsGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutputItemsGroups:
        return ManagementInstanceConsumersProfilesListOutputItemsGroups(
        object=data.get('object'),
        group=mapManagementInstanceConsumersProfilesListOutputItemsGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        assigned_via=data.get('assigned_via')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutputItems:
        return ManagementInstanceConsumersProfilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapManagementInstanceConsumersProfilesListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutputPagination:
        return ManagementInstanceConsumersProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListOutput:
        return ManagementInstanceConsumersProfilesListOutput(
        items=[mapManagementInstanceConsumersProfilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceConsumersProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumersProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceConsumersProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersProfilesListQuery:
        return ManagementInstanceConsumersProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

