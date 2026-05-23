from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class StoresListOutputItems:
    object: str
    id: str
    name: str
    access: str
    item_count: float
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class StoresListOutput:
    items: List[StoresListOutputItems]
    pagination: StoresListOutputPagination


class mapStoresListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresListOutputItems:
        return StoresListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        access=data.get('access'),
        item_count=data.get('item_count'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresListOutputPagination:
        return StoresListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[StoresListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresListOutput:
        return StoresListOutput(
        items=[mapStoresListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapStoresListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class StoresListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class StoresListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class StoresListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    created_at: Optional[StoresListQueryCreatedAt] = None
    updated_at: Optional[StoresListQueryUpdatedAt] = None


class mapStoresListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresListQuery:
        return StoresListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        created_at=mapStoresListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapStoresListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

