from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersListOutput:
    items: List[Dict[str, Any]]
    pagination: CustomProvidersListOutputPagination


class mapCustomProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersListOutputPagination:
        return CustomProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersListOutput:
        return CustomProvidersListOutput(
        items=data.get('items', []),
        pagination=mapCustomProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    created_at: Optional[CustomProvidersListQueryCreatedAt] = None
    updated_at: Optional[CustomProvidersListQueryUpdatedAt] = None


class mapCustomProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersListQuery:
        return CustomProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        type=data.get('type'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        search=data.get('search'),
        created_at=mapCustomProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCustomProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

