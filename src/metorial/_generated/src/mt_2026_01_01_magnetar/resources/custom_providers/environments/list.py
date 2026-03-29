from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CustomProvidersEnvironmentsListOutputItems:
    object: str
    id: str
    custom_provider_id: str
    instance_id: str
    created_at: datetime
    updated_at: datetime
    provider_id: Optional[str] = None
    current_provider_version_id: Optional[str] = None
@dataclass
class CustomProvidersEnvironmentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CustomProvidersEnvironmentsListOutput:
    items: List[CustomProvidersEnvironmentsListOutputItems]
    pagination: CustomProvidersEnvironmentsListOutputPagination


class mapCustomProvidersEnvironmentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersEnvironmentsListOutputItems:
        return CustomProvidersEnvironmentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        custom_provider_id=data.get('custom_provider_id'),
        provider_id=data.get('provider_id'),
        current_provider_version_id=data.get('current_provider_version_id'),
        instance_id=data.get('instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersEnvironmentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersEnvironmentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersEnvironmentsListOutputPagination:
        return CustomProvidersEnvironmentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersEnvironmentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCustomProvidersEnvironmentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersEnvironmentsListOutput:
        return CustomProvidersEnvironmentsListOutput(
        items=[mapCustomProvidersEnvironmentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCustomProvidersEnvironmentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersEnvironmentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CustomProvidersEnvironmentsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersEnvironmentsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class CustomProvidersEnvironmentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    custom_provider_version_id: Optional[Union[str, List[str]]] = None
    custom_provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[CustomProvidersEnvironmentsListQueryCreatedAt] = None
    updated_at: Optional[CustomProvidersEnvironmentsListQueryUpdatedAt] = None


class mapCustomProvidersEnvironmentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CustomProvidersEnvironmentsListQuery:
        return CustomProvidersEnvironmentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        custom_provider_version_id=data.get('custom_provider_version_id'),
        custom_provider_id=data.get('custom_provider_id'),
        created_at=mapCustomProvidersEnvironmentsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapCustomProvidersEnvironmentsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CustomProvidersEnvironmentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

