from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbackEventsListOutputItems:
    object: str
    id: str
    status: str
    source: str
    provider_trigger_key: str
    callback_id: str
    callback_instance_id: str
    occurred_at: datetime
    created_at: datetime
    mapped_type: Optional[str] = None
    mapped_id: Optional[str] = None
@dataclass
class DashboardInstanceCallbackEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCallbackEventsListOutput:
    items: List[DashboardInstanceCallbackEventsListOutputItems]
    pagination: DashboardInstanceCallbackEventsListOutputPagination


class mapDashboardInstanceCallbackEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsListOutputItems:
        return DashboardInstanceCallbackEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_trigger_key=data.get('provider_trigger_key'),
        mapped_type=data.get('mapped_type'),
        mapped_id=data.get('mapped_id'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsListOutputPagination:
        return DashboardInstanceCallbackEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsListOutput:
        return DashboardInstanceCallbackEventsListOutput(
        items=[mapDashboardInstanceCallbackEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCallbackEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCallbackEventsListQueryOccurredAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceCallbackEventsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceCallbackEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    callback_id: Optional[Union[str, List[str]]] = None
    callback_instance_id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_trigger_key: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    source: Optional[Union[str, List[str]]] = None
    occurred_at: Optional[DashboardInstanceCallbackEventsListQueryOccurredAt] = None
    created_at: Optional[DashboardInstanceCallbackEventsListQueryCreatedAt] = None


class mapDashboardInstanceCallbackEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsListQuery:
        return DashboardInstanceCallbackEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        integration_id=data.get('integration_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider_id=data.get('provider_id'),
        provider_trigger_key=data.get('provider_trigger_key'),
        status=data.get('status'),
        source=data.get('source'),
        occurred_at=mapDashboardInstanceCallbackEventsListQueryOccurredAt.from_dict(data.get('occurred_at')) if data.get('occurred_at') else None,
        created_at=mapDashboardInstanceCallbackEventsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

