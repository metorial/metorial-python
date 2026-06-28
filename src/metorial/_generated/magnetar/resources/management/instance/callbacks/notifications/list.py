from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsError:
    code: str
    message: str
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsEventRequest:
    body: str
    headers: Optional[List[ManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders]] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsEvent:
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
    request: Optional[ManagementInstanceCallbacksNotificationsListOutputItemsEventRequest] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsDestination:
    object: str
    id: str
    name: str
    type: str
    retry: ManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[ManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError:
    code: str
    message: str
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse:
    status_code: float
    body: Optional[str] = None
    headers: Optional[List[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders]] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
    object: str
    id: str
    status: str
    attempt_number: float
    duration_ms: float
    created_at: datetime
    started_at: datetime
    completed_at: datetime
    error: Optional[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError] = None
    response: Optional[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputItems:
    object: str
    id: str
    status: str
    attempt_count: float
    event: ManagementInstanceCallbacksNotificationsListOutputItemsEvent
    destination: ManagementInstanceCallbacksNotificationsListOutputItemsDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[ManagementInstanceCallbacksNotificationsListOutputItemsError] = None
    attempts: Optional[List[ManagementInstanceCallbacksNotificationsListOutputItemsAttempts]] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
@dataclass
class ManagementInstanceCallbacksNotificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceCallbacksNotificationsListOutput:
    items: List[ManagementInstanceCallbacksNotificationsListOutputItems]
    pagination: ManagementInstanceCallbacksNotificationsListOutputPagination


class mapManagementInstanceCallbacksNotificationsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsError:
        return ManagementInstanceCallbacksNotificationsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
        return ManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsEventRequest:
        return ManagementInstanceCallbacksNotificationsListOutputItemsEventRequest(
        body=data.get('body'),
        headers=[mapManagementInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsEvent:
        return ManagementInstanceCallbacksNotificationsListOutputItemsEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapManagementInstanceCallbacksNotificationsListOutputItemsEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
        return ManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
        return ManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsDestination:
        return ManagementInstanceCallbacksNotificationsListOutputItemsDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapManagementInstanceCallbacksNotificationsListOutputItemsDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapManagementInstanceCallbacksNotificationsListOutputItemsDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError:
        return ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders:
        return ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse:
        return ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse(
        status_code=data.get('status_code'),
        body=data.get('body'),
        headers=[mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItemsAttempts:
        return ManagementInstanceCallbacksNotificationsListOutputItemsAttempts(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        error=mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        response=mapManagementInstanceCallbacksNotificationsListOutputItemsAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputItems:
        return ManagementInstanceCallbacksNotificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapManagementInstanceCallbacksNotificationsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapManagementInstanceCallbacksNotificationsListOutputItemsEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapManagementInstanceCallbacksNotificationsListOutputItemsDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        attempts=[mapManagementInstanceCallbacksNotificationsListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutputPagination:
        return ManagementInstanceCallbacksNotificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListOutput:
        return ManagementInstanceCallbacksNotificationsListOutput(
        items=[mapManagementInstanceCallbacksNotificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceCallbacksNotificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCallbacksNotificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    destination_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementInstanceCallbacksNotificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsListQuery:
        return ManagementInstanceCallbacksNotificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        destination_id=data.get('destination_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

