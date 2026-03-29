from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbacksNotificationsGetOutputError:
    code: str
    message: str
@dataclass
class CallbacksNotificationsGetOutputEventRequestHeaders:
    key: str
    value: str
@dataclass
class CallbacksNotificationsGetOutputEventRequest:
    body: str
    headers: Optional[List[CallbacksNotificationsGetOutputEventRequestHeaders]] = None
@dataclass
class CallbacksNotificationsGetOutputEvent:
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
    request: Optional[CallbacksNotificationsGetOutputEventRequest] = None
@dataclass
class CallbacksNotificationsGetOutputDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class CallbacksNotificationsGetOutputDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class CallbacksNotificationsGetOutputDestination:
    object: str
    id: str
    name: str
    type: str
    retry: CallbacksNotificationsGetOutputDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[CallbacksNotificationsGetOutputDestinationWebhook] = None
@dataclass
class CallbacksNotificationsGetOutput:
    object: str
    id: str
    status: str
    attempt_count: float
    event: CallbacksNotificationsGetOutputEvent
    destination: CallbacksNotificationsGetOutputDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[CallbacksNotificationsGetOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None


class mapCallbacksNotificationsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputError:
        return CallbacksNotificationsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputEventRequestHeaders:
        return CallbacksNotificationsGetOutputEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputEventRequest:
        return CallbacksNotificationsGetOutputEventRequest(
        body=data.get('body'),
        headers=[mapCallbacksNotificationsGetOutputEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputEvent:
        return CallbacksNotificationsGetOutputEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapCallbacksNotificationsGetOutputEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputDestinationRetry:
        return CallbacksNotificationsGetOutputDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputDestinationWebhook:
        return CallbacksNotificationsGetOutputDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutputDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutputDestination:
        return CallbacksNotificationsGetOutputDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapCallbacksNotificationsGetOutputDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapCallbacksNotificationsGetOutputDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutputDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbacksNotificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbacksNotificationsGetOutput:
        return CallbacksNotificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapCallbacksNotificationsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapCallbacksNotificationsGetOutputEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapCallbacksNotificationsGetOutputDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbacksNotificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

