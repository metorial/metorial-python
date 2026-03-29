from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup:
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
class DashboardInstancePortalsConsumerProfilesListOutputItemsGroups:
    object: str
    group: DashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup
    assigned_via: str
@dataclass
class DashboardInstancePortalsConsumerProfilesListOutputItems:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    consumer_id: str
    created_at: datetime
    updated_at: datetime
    groups: Optional[List[DashboardInstancePortalsConsumerProfilesListOutputItemsGroups]] = None
@dataclass
class DashboardInstancePortalsConsumerProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsConsumerProfilesListOutput:
    items: List[DashboardInstancePortalsConsumerProfilesListOutputItems]
    pagination: DashboardInstancePortalsConsumerProfilesListOutputPagination


class mapDashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup:
        return DashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup(
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
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerProfilesListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutputItemsGroups:
        return DashboardInstancePortalsConsumerProfilesListOutputItemsGroups(
        object=data.get('object'),
        group=mapDashboardInstancePortalsConsumerProfilesListOutputItemsGroupsGroup.from_dict(data.get('group')) if data.get('group') else None,
        assigned_via=data.get('assigned_via')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerProfilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutputItems:
        return DashboardInstancePortalsConsumerProfilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        groups=[mapDashboardInstancePortalsConsumerProfilesListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        consumer_id=data.get('consumer_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutputPagination:
        return DashboardInstancePortalsConsumerProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListOutput:
        return DashboardInstancePortalsConsumerProfilesListOutput(
        items=[mapDashboardInstancePortalsConsumerProfilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsConsumerProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstancePortalsConsumerProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerProfilesListQuery:
        return DashboardInstancePortalsConsumerProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

