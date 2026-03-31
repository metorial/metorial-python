from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConsumersProfilesListOutputItemsGroupsGroup:
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
class DashboardInstanceConsumersProfilesListOutputItemsGroups:
    object: str
    group: DashboardInstanceConsumersProfilesListOutputItemsGroupsGroup
    assigned_via: str
@dataclass
class DashboardInstanceConsumersProfilesListOutputItems:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[DashboardInstanceConsumersProfilesListOutputItemsGroups]] = None
@dataclass
class DashboardInstanceConsumersProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceConsumersProfilesListOutput:
    items: List[DashboardInstanceConsumersProfilesListOutputItems]
    pagination: DashboardInstanceConsumersProfilesListOutputPagination


class mapDashboardInstanceConsumersProfilesListOutputItemsGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutputItemsGroupsGroup:
        return DashboardInstanceConsumersProfilesListOutputItemsGroupsGroup(
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
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutputItemsGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumersProfilesListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutputItemsGroups:
        return DashboardInstanceConsumersProfilesListOutputItemsGroups(
        object=data.get('object'),
        group=mapDashboardInstanceConsumersProfilesListOutputItemsGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        assigned_via=data.get('assigned_via')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumersProfilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutputItems:
        return DashboardInstanceConsumersProfilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapDashboardInstanceConsumersProfilesListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumersProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutputPagination:
        return DashboardInstanceConsumersProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumersProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListOutput:
        return DashboardInstanceConsumersProfilesListOutput(
        items=[mapDashboardInstanceConsumersProfilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceConsumersProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConsumersProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceConsumersProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersProfilesListQuery:
        return DashboardInstanceConsumersProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

