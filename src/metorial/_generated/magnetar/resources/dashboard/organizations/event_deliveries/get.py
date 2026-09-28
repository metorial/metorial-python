from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttemptsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutputAttempts:
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
    error: Optional[DashboardOrganizationsEventDeliveriesGetOutputAttemptsError] = None
    request: Optional[DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest] = None
    response: Optional[DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse] = None
@dataclass
class DashboardOrganizationsEventDeliveriesGetOutput:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: DashboardOrganizationsEventDeliveriesGetOutputRetry
    attempts: List[DashboardOrganizationsEventDeliveriesGetOutputAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[DashboardOrganizationsEventDeliveriesGetOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapDashboardOrganizationsEventDeliveriesGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputError:
        return DashboardOrganizationsEventDeliveriesGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputRetry:
        return DashboardOrganizationsEventDeliveriesGetOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttemptsError:
        return DashboardOrganizationsEventDeliveriesGetOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders:
        return DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest:
        return DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders:
        return DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse:
        return DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutputAttempts:
        return DashboardOrganizationsEventDeliveriesGetOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDeliveriesGetOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesGetOutput:
        return DashboardOrganizationsEventDeliveriesGetOutput(
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
        error=mapDashboardOrganizationsEventDeliveriesGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapDashboardOrganizationsEventDeliveriesGetOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapDashboardOrganizationsEventDeliveriesGetOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

