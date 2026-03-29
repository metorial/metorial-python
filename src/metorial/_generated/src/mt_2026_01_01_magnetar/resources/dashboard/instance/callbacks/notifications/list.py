from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsError:
    code: str
    message: str
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsEventRequest:
    body: str
    headers: Optional[List[DashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders]] = None
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsEvent:
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
    request: Optional[DashboardInstanceCallbacksNotificationsListOutputItemsEventRequest] = None
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItemsDestination:
    object: str
    id: str
    name: str
    type: str
    retry: DashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[DashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook] = None
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputItems:
    object: str
    id: str
    status: str
    attempt_count: float
    event: DashboardInstanceCallbacksNotificationsListOutputItemsEvent
    destination: DashboardInstanceCallbacksNotificationsListOutputItemsDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[DashboardInstanceCallbacksNotificationsListOutputItemsError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
@dataclass
class DashboardInstanceCallbacksNotificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceCallbacksNotificationsListOutput:
    items: List[DashboardInstanceCallbacksNotificationsListOutputItems]
    pagination: DashboardInstanceCallbacksNotificationsListOutputPagination


class mapDashboardInstanceCallbacksNotificationsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsError:
        return DashboardInstanceCallbacksNotificationsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders:
        return DashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsEventRequest:
        return DashboardInstanceCallbacksNotificationsListOutputItemsEventRequest(
        body=data.get('body'),
        headers=[mapDashboardInstanceCallbacksNotificationsListOutputItemsEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsEvent:
        return DashboardInstanceCallbacksNotificationsListOutputItemsEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapDashboardInstanceCallbacksNotificationsListOutputItemsEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry:
        return DashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook:
        return DashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItemsDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItemsDestination:
        return DashboardInstanceCallbacksNotificationsListOutputItemsDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapDashboardInstanceCallbacksNotificationsListOutputItemsDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapDashboardInstanceCallbacksNotificationsListOutputItemsDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItemsDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputItems:
        return DashboardInstanceCallbacksNotificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapDashboardInstanceCallbacksNotificationsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapDashboardInstanceCallbacksNotificationsListOutputItemsEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapDashboardInstanceCallbacksNotificationsListOutputItemsDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutputPagination:
        return DashboardInstanceCallbacksNotificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListOutput:
        return DashboardInstanceCallbacksNotificationsListOutput(
        items=[mapDashboardInstanceCallbacksNotificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceCallbacksNotificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCallbacksNotificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    destination_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceCallbacksNotificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsListQuery:
        return DashboardInstanceCallbacksNotificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        destination_id=data.get('destination_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

