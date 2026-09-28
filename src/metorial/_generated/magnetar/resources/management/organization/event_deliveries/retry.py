from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttemptsError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest:
    url: str
    method: str
    headers: List[ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutputAttempts:
    object: str
    id: str
    event_delivery_id: str
    event_id: str
    event_destination_id: str
    status: str
    attempt_number: float
    duration_ms: float
    is_retryable: bool
    started_at: datetime
    completed_at: datetime
    created_at: datetime
    error: Optional[ManagementOrganizationEventDeliveriesRetryOutputAttemptsError] = None
    request: Optional[ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest] = None
    response: Optional[ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse] = None
@dataclass
class ManagementOrganizationEventDeliveriesRetryOutput:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: ManagementOrganizationEventDeliveriesRetryOutputRetry
    attempts: List[ManagementOrganizationEventDeliveriesRetryOutputAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[ManagementOrganizationEventDeliveriesRetryOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapManagementOrganizationEventDeliveriesRetryOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputError:
        return ManagementOrganizationEventDeliveriesRetryOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputRetry:
        return ManagementOrganizationEventDeliveriesRetryOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttemptsError:
        return ManagementOrganizationEventDeliveriesRetryOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders:
        return ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest:
        return ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapManagementOrganizationEventDeliveriesRetryOutputAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders:
        return ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse:
        return ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapManagementOrganizationEventDeliveriesRetryOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutputAttempts:
        return ManagementOrganizationEventDeliveriesRetryOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapManagementOrganizationEventDeliveriesRetryOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapManagementOrganizationEventDeliveriesRetryOutputAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapManagementOrganizationEventDeliveriesRetryOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesRetryOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesRetryOutput:
        return ManagementOrganizationEventDeliveriesRetryOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        event_id=data.get('event_id'),
        event_type=data.get('event_type'),
        event_destination_id=data.get('event_destination_id'),
        type=data.get('type'),
        status=data.get('status'),
        attempt_count=data.get('attempt_count'),
        error=mapManagementOrganizationEventDeliveriesRetryOutputError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapManagementOrganizationEventDeliveriesRetryOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapManagementOrganizationEventDeliveriesRetryOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesRetryOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

