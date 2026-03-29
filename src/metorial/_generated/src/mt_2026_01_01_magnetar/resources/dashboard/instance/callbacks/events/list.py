from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksEventsListOutputItems:
    object: str
    id: str
    type: str
    source_id: str
    trigger_key: str
    input: Dict[str, Any]
    output: Dict[str, Any]
    delivery_status: str
    callback_id: str
    created_at: datetime
    callback_instance_id: Optional[str] = None
@dataclass
class DashboardInstanceCallbacksEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCallbacksEventsListOutput:
    items: List[DashboardInstanceCallbacksEventsListOutputItems]
    pagination: DashboardInstanceCallbacksEventsListOutputPagination


class mapDashboardInstanceCallbacksEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListOutputItems:
        return DashboardInstanceCallbacksEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source_id=data.get('source_id'),
        trigger_key=data.get('trigger_key'),
        input=data.get('input'),
        output=data.get('output'),
        delivery_status=data.get('delivery_status'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListOutputPagination:
        return DashboardInstanceCallbacksEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListOutput:
        return DashboardInstanceCallbacksEventsListOutput(
        items=[mapDashboardInstanceCallbacksEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCallbacksEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCallbacksEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    source_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCallbacksEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsListQuery:
        return DashboardInstanceCallbacksEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        type=data.get('type'),
        source_id=data.get('source_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

