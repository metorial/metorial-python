from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsListOutputItems:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsListOutput:
    items: List[DashboardInstancePortalsSurfaceProviderGroupsListOutputItems]
    pagination: DashboardInstancePortalsSurfaceProviderGroupsListOutputPagination


class mapDashboardInstancePortalsSurfaceProviderGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsListOutputItems:
        return DashboardInstancePortalsSurfaceProviderGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsSurfaceProviderGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsListOutputPagination:
        return DashboardInstancePortalsSurfaceProviderGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsSurfaceProviderGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsListOutput:
        return DashboardInstancePortalsSurfaceProviderGroupsListOutput(
        items=[mapDashboardInstancePortalsSurfaceProviderGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsSurfaceProviderGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsSurfaceProviderGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstancePortalsSurfaceProviderGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsSurfaceProviderGroupsListQuery:
        return DashboardInstancePortalsSurfaceProviderGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsSurfaceProviderGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

