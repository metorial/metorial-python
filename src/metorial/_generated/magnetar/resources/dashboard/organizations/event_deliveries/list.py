from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItemsAttempts:
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
    error: Optional[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError] = None
    request: Optional[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest] = None
    response: Optional[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse] = None
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputItems:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: DashboardOrganizationsEventDeliveriesListOutputItemsRetry
    attempts: List[DashboardOrganizationsEventDeliveriesListOutputItemsAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[DashboardOrganizationsEventDeliveriesListOutputItemsError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsEventDeliveriesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsEventDeliveriesListOutput:
    items: List[DashboardOrganizationsEventDeliveriesListOutputItems]
    pagination: DashboardOrganizationsEventDeliveriesListOutputPagination


class mapDashboardOrganizationsEventDeliveriesListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsError:
        return DashboardOrganizationsEventDeliveriesListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsRetry:
        return DashboardOrganizationsEventDeliveriesListOutputItemsRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItemsAttempts:
        return DashboardOrganizationsEventDeliveriesListOutputItemsAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDeliveriesListOutputItemsAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputItems:
        return DashboardOrganizationsEventDeliveriesListOutputItems(
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
        error=mapDashboardOrganizationsEventDeliveriesListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapDashboardOrganizationsEventDeliveriesListOutputItemsRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapDashboardOrganizationsEventDeliveriesListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutputPagination:
        return DashboardOrganizationsEventDeliveriesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveriesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListOutput:
        return DashboardOrganizationsEventDeliveriesListOutput(
        items=[mapDashboardOrganizationsEventDeliveriesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsEventDeliveriesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsEventDeliveriesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    event_id: Optional[Union[str, List[str]]] = None
    event_type: Optional[Union[str, List[str]]] = None
    event_destination_id: Optional[Union[str, List[str]]] = None
    instance_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsEventDeliveriesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveriesListQuery:
        return DashboardOrganizationsEventDeliveriesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        event_id=data.get('event_id'),
        event_type=data.get('event_type'),
        event_destination_id=data.get('event_destination_id'),
        instance_id=data.get('instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveriesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

