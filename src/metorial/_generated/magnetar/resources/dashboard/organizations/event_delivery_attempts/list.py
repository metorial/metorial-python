from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItemsError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputItems:
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
    error: Optional[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsError] = None
    request: Optional[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest] = None
    response: Optional[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse] = None
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListOutput:
    items: List[DashboardOrganizationsEventDeliveryAttemptsListOutputItems]
    pagination: DashboardOrganizationsEventDeliveryAttemptsListOutputPagination


class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItemsError:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputItems:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDeliveryAttemptsListOutputItemsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutputPagination:
        return DashboardOrganizationsEventDeliveryAttemptsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListOutput:
        return DashboardOrganizationsEventDeliveryAttemptsListOutput(
        items=[mapDashboardOrganizationsEventDeliveryAttemptsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsEventDeliveryAttemptsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsEventDeliveryAttemptsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    event_delivery_id: Optional[Union[str, List[str]]] = None
    event_id: Optional[Union[str, List[str]]] = None
    event_destination_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsEventDeliveryAttemptsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsListQuery:
        return DashboardOrganizationsEventDeliveryAttemptsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

