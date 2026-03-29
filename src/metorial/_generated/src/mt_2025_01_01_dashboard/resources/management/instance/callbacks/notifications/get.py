from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputError:
    code: str
    message: str
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputEventRequest:
    body: str
    headers: Optional[List[ManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders]] = None
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputEvent:
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
    request: Optional[ManagementInstanceCallbacksNotificationsGetOutputEventRequest] = None
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutputDestination:
    object: str
    id: str
    name: str
    type: str
    retry: ManagementInstanceCallbacksNotificationsGetOutputDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[ManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook] = None
@dataclass
class ManagementInstanceCallbacksNotificationsGetOutput:
    object: str
    id: str
    status: str
    attempt_count: float
    event: ManagementInstanceCallbacksNotificationsGetOutputEvent
    destination: ManagementInstanceCallbacksNotificationsGetOutputDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[ManagementInstanceCallbacksNotificationsGetOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None


class mapManagementInstanceCallbacksNotificationsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputError:
        return ManagementInstanceCallbacksNotificationsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
        return ManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputEventRequest:
        return ManagementInstanceCallbacksNotificationsGetOutputEventRequest(
        body=data.get('body'),
        headers=[mapManagementInstanceCallbacksNotificationsGetOutputEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputEvent:
        return ManagementInstanceCallbacksNotificationsGetOutputEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapManagementInstanceCallbacksNotificationsGetOutputEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputDestinationRetry:
        return ManagementInstanceCallbacksNotificationsGetOutputDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook:
        return ManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutputDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutputDestination:
        return ManagementInstanceCallbacksNotificationsGetOutputDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapManagementInstanceCallbacksNotificationsGetOutputDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapManagementInstanceCallbacksNotificationsGetOutputDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutputDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbacksNotificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbacksNotificationsGetOutput:
        return ManagementInstanceCallbacksNotificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapManagementInstanceCallbacksNotificationsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapManagementInstanceCallbacksNotificationsGetOutputEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapManagementInstanceCallbacksNotificationsGetOutputDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbacksNotificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

