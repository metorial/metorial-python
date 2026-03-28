from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksNotificationsListOutputItemsError:
    code: str
    message: str
@dataclass
class CallbacksNotificationsListOutputItemsEventRequestHeaders:
    key: str
    value: str
@dataclass
class CallbacksNotificationsListOutputItemsEventRequest:
    body: str
    headers: Optional[List[CallbacksNotificationsListOutputItemsEventRequestHeaders]] = None
@dataclass
class CallbacksNotificationsListOutputItemsEvent:
    object: str
    id: str
    type: str
    topics: List[str]
    status: str
    success_count: float
    failure_count: float
    created_at: datetime
    updated_at: datetime
    destination_count: Optional[float] = None
    request: Optional[CallbacksNotificationsListOutputItemsEventRequest] = None
@dataclass
class CallbacksNotificationsListOutputItemsDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class CallbacksNotificationsListOutputItemsDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class CallbacksNotificationsListOutputItemsDestination:
    object: str
    id: str
    name: str
    type: str
    retry: CallbacksNotificationsListOutputItemsDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[CallbacksNotificationsListOutputItemsDestinationWebhook] = None
@dataclass
class CallbacksNotificationsListOutputItems:
    object: str
    id: str
    status: str
    attempt_count: float
    event: CallbacksNotificationsListOutputItemsEvent
    destination: CallbacksNotificationsListOutputItemsDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[CallbacksNotificationsListOutputItemsError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
@dataclass
class CallbacksNotificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class CallbacksNotificationsListOutput:
    items: List[CallbacksNotificationsListOutputItems]
    pagination: CallbacksNotificationsListOutputPagination


class mapCallbacksNotificationsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsError:
        return CallbacksNotificationsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsEventRequestHeaders:
        return CallbacksNotificationsListOutputItemsEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsEventRequest:
        return CallbacksNotificationsListOutputItemsEventRequest(
        body=data.get('body'),
        headers=[mapCallbacksNotificationsListOutputItemsEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsEvent:
        return CallbacksNotificationsListOutputItemsEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapCallbacksNotificationsListOutputItemsEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsDestinationRetry:
        return CallbacksNotificationsListOutputItemsDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsDestinationWebhook:
        return CallbacksNotificationsListOutputItemsDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItemsDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItemsDestination:
        return CallbacksNotificationsListOutputItemsDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapCallbacksNotificationsListOutputItemsDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapCallbacksNotificationsListOutputItemsDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItemsDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputItems:
        return CallbacksNotificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapCallbacksNotificationsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapCallbacksNotificationsListOutputItemsEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapCallbacksNotificationsListOutputItemsDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutputPagination:
        return CallbacksNotificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListOutput:
        return CallbacksNotificationsListOutput(
        items=[mapCallbacksNotificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapCallbacksNotificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class CallbacksNotificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    destination_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapCallbacksNotificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsListQuery:
        return CallbacksNotificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        destination_id=data.get('destination_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

