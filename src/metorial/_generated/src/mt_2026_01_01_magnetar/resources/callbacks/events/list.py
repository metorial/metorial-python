from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksEventsListOutputItemsError:
    code: Optional[str] = None
    message: Optional[str] = None
@dataclass
class CallbacksEventsListOutputItems:
    object: str
    id: str
    type: str
    source_id: str
    trigger_key: str
    status: str
    delivery_status: str
    callback_id: str
    created_at: datetime
    input: Optional[Dict[str, Any]] = None
    output: Optional[Dict[str, Any]] = None
    error: Optional[CallbacksEventsListOutputItemsError] = None
    callback_instance_id: Optional[str] = None
@dataclass
class CallbacksEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksEventsListOutput:
    items: List[CallbacksEventsListOutputItems]
    pagination: CallbacksEventsListOutputPagination


class mapCallbacksEventsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutputItemsError:
        return CallbacksEventsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksEventsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutputItems:
        return CallbacksEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source_id=data.get('source_id'),
        trigger_key=data.get('trigger_key'),
        input=data.get('input'),
        output=data.get('output'),
        status=data.get('status'),
        error=mapCallbacksEventsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        delivery_status=data.get('delivery_status'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutputPagination:
        return CallbacksEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksEventsListOutput:
        return CallbacksEventsListOutput(
        items=[mapCallbacksEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None
    source_id: Optional[Union[str, List[str]]] = None


class mapCallbacksEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksEventsListQuery:
        return CallbacksEventsListQuery(
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
    def to_dict(value: Union[CallbacksEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

