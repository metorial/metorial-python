from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile:
    object: str
    id: str
    name: str
    email: str
@dataclass
class DashboardInstancePortalsAccessRequestsListOutputItems:
    object: str
    id: str
    status: str
    consumer_profile: DashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile
    target: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    message: Optional[str] = None
    resolution_message: Optional[str] = None
    reviewed_at: Optional[datetime] = None
@dataclass
class DashboardInstancePortalsAccessRequestsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsAccessRequestsListOutput:
    items: List[DashboardInstancePortalsAccessRequestsListOutputItems]
    pagination: DashboardInstancePortalsAccessRequestsListOutputPagination


class mapDashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile:
        return DashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessRequestsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessRequestsListOutputItems:
        return DashboardInstancePortalsAccessRequestsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        message=data.get('message'),
        resolution_message=data.get('resolution_message'),
        consumer_profile=mapDashboardInstancePortalsAccessRequestsListOutputItemsConsumerProfile.from_dict(data.get('consumer_profile')) if data.get('consumer_profile') else None,
        target=data.get('target'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reviewed_at=datetime.fromisoformat(data.get('reviewed_at').replace('Z', '+00:00')) if data.get('reviewed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessRequestsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessRequestsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessRequestsListOutputPagination:
        return DashboardInstancePortalsAccessRequestsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessRequestsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessRequestsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessRequestsListOutput:
        return DashboardInstancePortalsAccessRequestsListOutput(
        items=[mapDashboardInstancePortalsAccessRequestsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsAccessRequestsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessRequestsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAccessRequestsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    consumer_profile_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstancePortalsAccessRequestsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessRequestsListQuery:
        return DashboardInstancePortalsAccessRequestsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        consumer_profile_id=data.get('consumer_profile_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessRequestsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

