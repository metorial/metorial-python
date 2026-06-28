from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputError:
    code: str
    message: str
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputEventRequest:
    body: str
    headers: Optional[List[DashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders]] = None
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputEvent:
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
    request: Optional[DashboardInstanceCallbacksNotificationsGetOutputEventRequest] = None
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputDestinationRetry:
    type: str
    max_attempts: float
    delay_seconds: float
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook:
    id: str
    url: str
    method: str
    created_at: datetime
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputDestination:
    object: str
    id: str
    name: str
    type: str
    retry: DashboardInstanceCallbacksNotificationsGetOutputDestinationRetry
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    event_types: Optional[List[str]] = None
    webhook: Optional[DashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook] = None
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputAttemptsError:
    code: str
    message: str
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse:
    status_code: float
    body: Optional[str] = None
    headers: Optional[List[DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders]] = None
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutputAttempts:
    object: str
    id: str
    status: str
    attempt_number: float
    duration_ms: float
    created_at: datetime
    started_at: datetime
    completed_at: datetime
    error: Optional[DashboardInstanceCallbacksNotificationsGetOutputAttemptsError] = None
    response: Optional[DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse] = None
@dataclass
class DashboardInstanceCallbacksNotificationsGetOutput:
    object: str
    id: str
    status: str
    attempt_count: float
    event: DashboardInstanceCallbacksNotificationsGetOutputEvent
    destination: DashboardInstanceCallbacksNotificationsGetOutputDestination
    created_at: datetime
    updated_at: datetime
    error: Optional[DashboardInstanceCallbacksNotificationsGetOutputError] = None
    attempts: Optional[List[DashboardInstanceCallbacksNotificationsGetOutputAttempts]] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None


class mapDashboardInstanceCallbacksNotificationsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputError:
        return DashboardInstanceCallbacksNotificationsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders:
        return DashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputEventRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputEventRequest:
        return DashboardInstanceCallbacksNotificationsGetOutputEventRequest(
        body=data.get('body'),
        headers=[mapDashboardInstanceCallbacksNotificationsGetOutputEventRequestHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputEventRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputEvent:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputEvent:
        return DashboardInstanceCallbacksNotificationsGetOutputEvent(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        topics=data.get('topics', []),
        status=data.get('status'),
        destination_count=data.get('destination_count'),
        success_count=data.get('success_count'),
        failure_count=data.get('failure_count'),
        request=mapDashboardInstanceCallbacksNotificationsGetOutputEventRequest.from_dict(data.get('request')) if data.get('request') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputEvent, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputDestinationRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputDestinationRetry:
        return DashboardInstanceCallbacksNotificationsGetOutputDestinationRetry(
        type=data.get('type'),
        max_attempts=data.get('maxAttempts'),
        delay_seconds=data.get('delaySeconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputDestinationRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook:
        return DashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook(
        id=data.get('id'),
        url=data.get('url'),
        method=data.get('method'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputDestination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputDestination:
        return DashboardInstanceCallbacksNotificationsGetOutputDestination(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        retry=mapDashboardInstanceCallbacksNotificationsGetOutputDestinationRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        webhook=mapDashboardInstanceCallbacksNotificationsGetOutputDestinationWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputDestination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputAttemptsError:
        return DashboardInstanceCallbacksNotificationsGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders:
        return DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse:
        return DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse(
        status_code=data.get('status_code'),
        body=data.get('body'),
        headers=[mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutputAttempts:
        return DashboardInstanceCallbacksNotificationsGetOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        error=mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        response=mapDashboardInstanceCallbacksNotificationsGetOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbacksNotificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksNotificationsGetOutput:
        return DashboardInstanceCallbacksNotificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapDashboardInstanceCallbacksNotificationsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        attempt_count=data.get('attempt_count'),
        event=mapDashboardInstanceCallbacksNotificationsGetOutputEvent.from_dict(data.get('event')) if data.get('event') else None,
        destination=mapDashboardInstanceCallbacksNotificationsGetOutputDestination.from_dict(data.get('destination')) if data.get('destination') else None,
        attempts=[mapDashboardInstanceCallbacksNotificationsGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbacksNotificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

