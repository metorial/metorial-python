from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsListOutputItems:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsListOutput:
    items: List[ManagementInstancePortalsSurfaceProviderGroupsListOutputItems]
    pagination: ManagementInstancePortalsSurfaceProviderGroupsListOutputPagination


class mapManagementInstancePortalsSurfaceProviderGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsListOutputItems:
        return ManagementInstancePortalsSurfaceProviderGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsSurfaceProviderGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsListOutputPagination:
        return ManagementInstancePortalsSurfaceProviderGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsSurfaceProviderGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsListOutput:
        return ManagementInstancePortalsSurfaceProviderGroupsListOutput(
        items=[mapManagementInstancePortalsSurfaceProviderGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsSurfaceProviderGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsSurfaceProviderGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstancePortalsSurfaceProviderGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsSurfaceProviderGroupsListQuery:
        return ManagementInstancePortalsSurfaceProviderGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsSurfaceProviderGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

