from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttemptsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutputAttempts:
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
    error: Optional[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsError] = None
    request: Optional[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest] = None
    response: Optional[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse] = None
@dataclass
class DashboardOrganizationsEventDeliveriesRetryOutput:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: DashboardOrganizationsEventDeliveriesRetryOutputRetry
    attempts: List[DashboardOrganizationsEventDeliveriesRetryOutputAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[DashboardOrganizationsEventDeliveriesRetryOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapDashboardOrganizationsEventDeliveriesRetryOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputError:
        return DashboardOrganizationsEventDeliveriesRetryOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputRetry:
        return DashboardOrganizationsEventDeliveriesRetryOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttemptsError:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutputAttempts:
        return DashboardOrganizationsEventDeliveriesRetryOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDeliveriesRetryOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesRetryOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesRetryOutput:
        return DashboardOrganizationsEventDeliveriesRetryOutput(
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
        error=mapDashboardOrganizationsEventDeliveriesRetryOutputError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapDashboardOrganizationsEventDeliveriesRetryOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapDashboardOrganizationsEventDeliveriesRetryOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesRetryOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

