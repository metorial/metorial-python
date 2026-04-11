from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsSurfaceProviderGroupsListOutputItems:
    object: str
    id: str
    name: str
    index: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class PortalsSurfaceProviderGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsSurfaceProviderGroupsListOutput:
    items: List[PortalsSurfaceProviderGroupsListOutputItems]
    pagination: PortalsSurfaceProviderGroupsListOutputPagination


class mapPortalsSurfaceProviderGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsSurfaceProviderGroupsListOutputItems:
        return PortalsSurfaceProviderGroupsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsSurfaceProviderGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsSurfaceProviderGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsSurfaceProviderGroupsListOutputPagination:
        return PortalsSurfaceProviderGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsSurfaceProviderGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsSurfaceProviderGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsSurfaceProviderGroupsListOutput:
        return PortalsSurfaceProviderGroupsListOutput(
        items=[mapPortalsSurfaceProviderGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsSurfaceProviderGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsSurfaceProviderGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsSurfaceProviderGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapPortalsSurfaceProviderGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsSurfaceProviderGroupsListQuery:
        return PortalsSurfaceProviderGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[PortalsSurfaceProviderGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

