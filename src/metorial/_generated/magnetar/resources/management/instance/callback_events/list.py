from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbackEventsListOutputItems:
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
class ManagementInstanceCallbackEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCallbackEventsListOutput:
    items: List[ManagementInstanceCallbackEventsListOutputItems]
    pagination: ManagementInstanceCallbackEventsListOutputPagination


class mapManagementInstanceCallbackEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsListOutputItems:
        return ManagementInstanceCallbackEventsListOutputItems(
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
    def to_dict(value: Union[ManagementInstanceCallbackEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsListOutputPagination:
        return ManagementInstanceCallbackEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsListOutput:
        return ManagementInstanceCallbackEventsListOutput(
        items=[mapManagementInstanceCallbackEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCallbackEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbackEventsListQueryOccurredAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbackEventsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbackEventsListQuery:
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
    occurred_at: Optional[ManagementInstanceCallbackEventsListQueryOccurredAt] = None
    created_at: Optional[ManagementInstanceCallbackEventsListQueryCreatedAt] = None


class mapManagementInstanceCallbackEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsListQuery:
        return ManagementInstanceCallbackEventsListQuery(
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
        occurred_at=mapManagementInstanceCallbackEventsListQueryOccurredAt.from_dict(data.get('occurred_at')) if data.get('occurred_at') else None,
        created_at=mapManagementInstanceCallbackEventsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

