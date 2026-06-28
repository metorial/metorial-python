from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class ManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
    object: str
    id: str
    name: str
    email: Optional[str] = None
@dataclass
class ManagementInstancePortalsConsumerInvitesListOutputItems:
    object: str
    id: str
    status: str
    consumer_profile: ManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile
    invited_by: ManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy
    created_at: datetime
    updated_at: datetime
    portal_url: Optional[str] = None
    message: Optional[str] = None
    accepted_at: Optional[datetime] = None
@dataclass
class ManagementInstancePortalsConsumerInvitesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsConsumerInvitesListOutput:
    items: List[ManagementInstancePortalsConsumerInvitesListOutputItems]
    pagination: ManagementInstancePortalsConsumerInvitesListOutputPagination


class mapManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile:
        return ManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy:
        return ManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerInvitesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListOutputItems:
        return ManagementInstancePortalsConsumerInvitesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        portal_url=data.get('portal_url'),
        consumer_profile=mapManagementInstancePortalsConsumerInvitesListOutputItemsConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        invited_by=mapManagementInstancePortalsConsumerInvitesListOutputItemsInvitedBy.from_dict(data.get('invited_by')) if data.get('invited_by') else None,
        message=data.get('message'),
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerInvitesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListOutputPagination:
        return ManagementInstancePortalsConsumerInvitesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerInvitesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListOutput:
        return ManagementInstancePortalsConsumerInvitesListOutput(
        items=[mapManagementInstancePortalsConsumerInvitesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsConsumerInvitesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsConsumerInvitesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    email: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstancePortalsConsumerInvitesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerInvitesListQuery:
        return ManagementInstancePortalsConsumerInvitesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        email=data.get('email'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerInvitesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

