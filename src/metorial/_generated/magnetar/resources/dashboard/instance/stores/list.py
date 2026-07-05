from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceStoresListOutputItems:
    object: str
    id: str
    name: str
    access: str
    item_count: float
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceStoresListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceStoresListOutput:
    items: List[DashboardInstanceStoresListOutputItems]
    pagination: DashboardInstanceStoresListOutputPagination


class mapDashboardInstanceStoresListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresListOutputItems:
        return DashboardInstanceStoresListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        access=data.get('access'),
        item_count=data.get('item_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresListOutputPagination:
        return DashboardInstanceStoresListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceStoresListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresListOutput:
        return DashboardInstanceStoresListOutput(
        items=[mapDashboardInstanceStoresListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceStoresListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceStoresListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceStoresListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceStoresListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceStoresListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceStoresListQueryUpdatedAt] = None


class mapDashboardInstanceStoresListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresListQuery:
        return DashboardInstanceStoresListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapDashboardInstanceStoresListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceStoresListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

