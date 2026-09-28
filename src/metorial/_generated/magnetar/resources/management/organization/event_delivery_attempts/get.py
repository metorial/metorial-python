from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutputError:
    code: str
    message: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutputRequest:
    url: str
    method: str
    headers: List[ManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders]
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders:
    key: str
    value: str
@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutputResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[ManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class ManagementOrganizationEventDeliveryAttemptsGetOutput:
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
    error: Optional[ManagementOrganizationEventDeliveryAttemptsGetOutputError] = None
    request: Optional[ManagementOrganizationEventDeliveryAttemptsGetOutputRequest] = None
    response: Optional[ManagementOrganizationEventDeliveryAttemptsGetOutputResponse] = None


class mapManagementOrganizationEventDeliveryAttemptsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutputError:
        return ManagementOrganizationEventDeliveryAttemptsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders:
        return ManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutputRequest:
        return ManagementOrganizationEventDeliveryAttemptsGetOutputRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapManagementOrganizationEventDeliveryAttemptsGetOutputRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders:
        return ManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsGetOutputResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutputResponse:
        return ManagementOrganizationEventDeliveryAttemptsGetOutputResponse(
        status_code=data.get('status_code'),
        headers=[mapManagementOrganizationEventDeliveryAttemptsGetOutputResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutputResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDeliveryAttemptsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDeliveryAttemptsGetOutput:
        return ManagementOrganizationEventDeliveryAttemptsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapManagementOrganizationEventDeliveryAttemptsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapManagementOrganizationEventDeliveryAttemptsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapManagementOrganizationEventDeliveryAttemptsGetOutputResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDeliveryAttemptsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

