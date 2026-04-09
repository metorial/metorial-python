from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
    object: str
    id: str
    name: str
    email: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerInvitesListOutputItems:
    object: str
    id: str
    status: str
    consumer_profile: DashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile
    invited_by: DashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy
    created_at: datetime
    updated_at: datetime
    portal_url: Optional[str] = None
    message: Optional[str] = None
    accepted_at: Optional[datetime] = None
@dataclass
class DashboardInstancePortalsConsumerInvitesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsConsumerInvitesListOutput:
    items: List[DashboardInstancePortalsConsumerInvitesListOutputItems]
    pagination: DashboardInstancePortalsConsumerInvitesListOutputPagination


class mapDashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
        return DashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
        return DashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListOutputItems:
        return DashboardInstancePortalsConsumerInvitesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        portal_url=data.get('portal_url'),
        consumer_profile=mapDashboardInstancePortalsConsumerInvitesListOutputItemsConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        invited_by=mapDashboardInstancePortalsConsumerInvitesListOutputItemsInvitedBy.from_dict(data.get('invited_by')) if data.get('invited_by') else None,
        message=data.get('message'),
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListOutputPagination:
        return DashboardInstancePortalsConsumerInvitesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerInvitesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListOutput:
        return DashboardInstancePortalsConsumerInvitesListOutput(
        items=[mapDashboardInstancePortalsConsumerInvitesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsConsumerInvitesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerInvitesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapDashboardInstancePortalsConsumerInvitesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerInvitesListQuery:
        return DashboardInstancePortalsConsumerInvitesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerInvitesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

