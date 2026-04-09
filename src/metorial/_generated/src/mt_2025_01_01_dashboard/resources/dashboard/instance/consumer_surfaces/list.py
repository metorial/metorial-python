from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConsumerSurfacesListOutputItemsAuth:
    object: str
    session_expiry_time_in_seconds: float
    email_whitelist: List[str]
@dataclass
class DashboardInstanceConsumerSurfacesListOutputItems:
    object: str
    id: str
    status: str
    name: str
    auth: DashboardInstanceConsumerSurfacesListOutputItemsAuth
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceConsumerSurfacesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceConsumerSurfacesListOutput:
    items: List[DashboardInstanceConsumerSurfacesListOutputItems]
    pagination: DashboardInstanceConsumerSurfacesListOutputPagination


class mapDashboardInstanceConsumerSurfacesListOutputItemsAuth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesListOutputItemsAuth:
        return DashboardInstanceConsumerSurfacesListOutputItemsAuth(
        object=data.get('object'),
        session_expiry_time_in_seconds=data.get('session_expiry_time_in_seconds'),
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesListOutputItemsAuth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumerSurfacesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesListOutputItems:
        return DashboardInstanceConsumerSurfacesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        auth=mapDashboardInstanceConsumerSurfacesListOutputItemsAuth.from_dict(data.get('auth')) if data.get('auth') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumerSurfacesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesListOutputPagination:
        return DashboardInstanceConsumerSurfacesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceConsumerSurfacesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesListOutput:
        return DashboardInstanceConsumerSurfacesListOutput(
        items=[mapDashboardInstanceConsumerSurfacesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceConsumerSurfacesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConsumerSurfacesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceConsumerSurfacesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumerSurfacesListQuery:
        return DashboardInstanceConsumerSurfacesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumerSurfacesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

