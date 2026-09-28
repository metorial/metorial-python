from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDestinationsPingOutputError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttemptsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttemptsRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDestinationsPingOutputAttempts:
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
    error: Optional[DashboardOrganizationsEventDestinationsPingOutputAttemptsError] = None
    request: Optional[DashboardOrganizationsEventDestinationsPingOutputAttemptsRequest] = None
    response: Optional[DashboardOrganizationsEventDestinationsPingOutputAttemptsResponse] = None
@dataclass
class DashboardOrganizationsEventDestinationsPingOutput:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: DashboardOrganizationsEventDestinationsPingOutputRetry
    attempts: List[DashboardOrganizationsEventDestinationsPingOutputAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[DashboardOrganizationsEventDestinationsPingOutputError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class mapDashboardOrganizationsEventDestinationsPingOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputError:
        return DashboardOrganizationsEventDestinationsPingOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputRetry:
        return DashboardOrganizationsEventDestinationsPingOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttemptsError:
        return DashboardOrganizationsEventDestinationsPingOutputAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders:
        return DashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttemptsRequest:
        return DashboardOrganizationsEventDestinationsPingOutputAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDestinationsPingOutputAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders:
        return DashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttemptsResponse:
        return DashboardOrganizationsEventDestinationsPingOutputAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDestinationsPingOutputAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutputAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutputAttempts:
        return DashboardOrganizationsEventDestinationsPingOutputAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDestinationsPingOutputAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDestinationsPingOutputAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDestinationsPingOutputAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutputAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsPingOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsPingOutput:
        return DashboardOrganizationsEventDestinationsPingOutput(
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
        error=mapDashboardOrganizationsEventDestinationsPingOutputError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapDashboardOrganizationsEventDestinationsPingOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapDashboardOrganizationsEventDestinationsPingOutputAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsPingOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

