from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItemsError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest:
    url: str
    method: str
    headers: List[ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders]
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputItems:
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
    error: Optional[ManagementOrganizationEventDeliveryAttemptsListOutputItemsError] = None
    request: Optional[ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest] = None
    response: Optional[ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse] = None
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationEventDeliveryAttemptsListOutput:
    items: List[ManagementOrganizationEventDeliveryAttemptsListOutputItems]
    pagination: ManagementOrganizationEventDeliveryAttemptsListOutputPagination


class mapManagementOrganizationEventDeliveryAttemptsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItemsError:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapManagementOrganizationEventDeliveryAttemptsListOutputItemsRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse(
        status_code=data.get('status_code'),
        headers=[mapManagementOrganizationEventDeliveryAttemptsListOutputItemsResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputItems:
        return ManagementOrganizationEventDeliveryAttemptsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapManagementOrganizationEventDeliveryAttemptsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapManagementOrganizationEventDeliveryAttemptsListOutputItemsRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapManagementOrganizationEventDeliveryAttemptsListOutputItemsResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutputPagination:
        return ManagementOrganizationEventDeliveryAttemptsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListOutput:
        return ManagementOrganizationEventDeliveryAttemptsListOutput(
        items=[mapManagementOrganizationEventDeliveryAttemptsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationEventDeliveryAttemptsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationEventDeliveryAttemptsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    event_delivery_id: Optional[Union[str, List[str]]] = None
    event_id: Optional[Union[str, List[str]]] = None
    event_destination_id: Optional[Union[str, List[str]]] = None


class mapManagementOrganizationEventDeliveryAttemptsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsListQuery:
        return ManagementOrganizationEventDeliveryAttemptsListQuery(
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
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

