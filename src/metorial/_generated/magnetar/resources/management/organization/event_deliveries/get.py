from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDeliveriesGetOutputError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttemptsError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttemptsRequest:
    url: str
    method: str
    headers: List[ManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[ManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesGetOutputAttempts:
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
    error: Optional[ManagementOrganizationEventDeliveriesGetOutputAttemptsError] = None
    request: Optional[ManagementOrganizationEventDeliveriesGetOutputAttemptsRequest] = None
    response: Optional[ManagementOrganizationEventDeliveriesGetOutputAttemptsResponse] = None
@dataclass
class ManagementOrganizationEventDeliveriesGetOutput:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: ManagementOrganizationEventDeliveriesGetOutputRetry
    attempts: List[ManagementOrganizationEventDeliveriesGetOutputAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[ManagementOrganizationEventDeliveriesGetOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapManagementOrganizationEventDeliveriesGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputError:
        return ManagementOrganizationEventDeliveriesGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputRetry:
        return ManagementOrganizationEventDeliveriesGetOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttemptsError:
        return ManagementOrganizationEventDeliveriesGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders:
        return ManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttemptsRequest:
        return ManagementOrganizationEventDeliveriesGetOutputAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapManagementOrganizationEventDeliveriesGetOutputAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders:
        return ManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttemptsResponse:
        return ManagementOrganizationEventDeliveriesGetOutputAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapManagementOrganizationEventDeliveriesGetOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutputAttempts:
        return ManagementOrganizationEventDeliveriesGetOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapManagementOrganizationEventDeliveriesGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapManagementOrganizationEventDeliveriesGetOutputAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapManagementOrganizationEventDeliveriesGetOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesGetOutput:
        return ManagementOrganizationEventDeliveriesGetOutput(
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
        error=mapManagementOrganizationEventDeliveriesGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapManagementOrganizationEventDeliveriesGetOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapManagementOrganizationEventDeliveriesGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

