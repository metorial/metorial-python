from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttemptsError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest:
    url: str
    method: str
    headers: List[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders]
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItemsAttempts:
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
    error: Optional[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsError] = None
    request: Optional[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest] = None
    response: Optional[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse] = None
@dataclass
class ManagementOrganizationEventDeliveriesListOutputItems:
    object: str
    id: str
    organization_id: str
    event_id: str
    event_type: str
    event_destination_id: str
    type: str
    status: str
    attempt_count: float
    retry: ManagementOrganizationEventDeliveriesListOutputItemsRetry
    attempts: List[ManagementOrganizationEventDeliveriesListOutputItemsAttempts]
    created_at: datetime
    updated_at: datetime
    instance_id: Optional[str] = None
    error: Optional[ManagementOrganizationEventDeliveriesListOutputItemsError] = None
    last_attempt_at: Optional[datetime] = None
    next_attempt_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationEventDeliveriesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationEventDeliveriesListOutput:
    items: List[ManagementOrganizationEventDeliveriesListOutputItems]
    pagination: ManagementOrganizationEventDeliveriesListOutputPagination


class mapManagementOrganizationEventDeliveriesListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsError:
        return ManagementOrganizationEventDeliveriesListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsRetry:
        return ManagementOrganizationEventDeliveriesListOutputItemsRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttemptsError:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttemptsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse(
        status_code=data.get('status_code'),
        headers=[mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItemsAttempts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItemsAttempts:
        return ManagementOrganizationEventDeliveriesListOutputItemsAttempts(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapManagementOrganizationEventDeliveriesListOutputItemsAttemptsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItemsAttempts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputItems:
        return ManagementOrganizationEventDeliveriesListOutputItems(
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
        error=mapManagementOrganizationEventDeliveriesListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        retry=mapManagementOrganizationEventDeliveriesListOutputItemsRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        attempts=[mapManagementOrganizationEventDeliveriesListOutputItemsAttempts.from_dict(item) for item in data.get('attempts', []) if item],
        last_attempt_at=datetime.fromisoformat(data.get('last_attempt_at').replace('Z', '+00:00')) if data.get('last_attempt_at') else None,
        next_attempt_at=datetime.fromisoformat(data.get('next_attempt_at').replace('Z', '+00:00')) if data.get('next_attempt_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutputPagination:
        return ManagementOrganizationEventDeliveriesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveriesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListOutput:
        return ManagementOrganizationEventDeliveriesListOutput(
        items=[mapManagementOrganizationEventDeliveriesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationEventDeliveriesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationEventDeliveriesListQuery:
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


class mapManagementOrganizationEventDeliveriesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveriesListQuery:
        return ManagementOrganizationEventDeliveriesListQuery(
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
    def to_dict(value: Union[ManagementOrganizationEventDeliveriesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

