from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutputError:
    code: str
    message: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutputRequest:
    url: str
    method: str
    headers: List[DashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders]
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders:
    key: str
    value: str
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutputResponse:
    status_code: float
    is_body_truncated: bool
    headers: Optional[List[DashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders]] = None
    body: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDeliveryAttemptsGetOutput:
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
    error: Optional[DashboardOrganizationsEventDeliveryAttemptsGetOutputError] = None
    request: Optional[DashboardOrganizationsEventDeliveryAttemptsGetOutputRequest] = None
    response: Optional[DashboardOrganizationsEventDeliveryAttemptsGetOutputResponse] = None


class mapDashboardOrganizationsEventDeliveryAttemptsGetOutputError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutputError:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutputError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutputError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsGetOutputRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutputRequest:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutputRequest(
        url=data.get('url'),
        method=data.get('method'),
        headers=[mapDashboardOrganizationsEventDeliveryAttemptsGetOutputRequestHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutputRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders(
        key=data.get('key'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsGetOutputResponse:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutputResponse:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutputResponse(
        status_code=data.get('status_code'),
        headers=[mapDashboardOrganizationsEventDeliveryAttemptsGetOutputResponseHeaders.from_dict(item) for item in data.get('headers', []) if item],
        body=data.get('body'),
        is_body_truncated=data.get('is_body_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutputResponse, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDeliveryAttemptsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDeliveryAttemptsGetOutput:
        return DashboardOrganizationsEventDeliveryAttemptsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        event_delivery_id=data.get('event_delivery_id'),
        event_id=data.get('event_id'),
        event_destination_id=data.get('event_destination_id'),
        status=data.get('status'),
        attempt_number=data.get('attempt_number'),
        duration_ms=data.get('duration_ms'),
        is_retryable=data.get('is_retryable'),
        error=mapDashboardOrganizationsEventDeliveryAttemptsGetOutputError.from_dict(data.get('error')) if data.get('error') else None,
        request=mapDashboardOrganizationsEventDeliveryAttemptsGetOutputRequest.from_dict(data.get('request')) if data.get('request') else None,
        response=mapDashboardOrganizationsEventDeliveryAttemptsGetOutputResponse.from_dict(data.get('response')) if data.get('response') else None,
        started_at=datetime.fromisoformat(data.get('started_at').replace('Z', '+00:00')) if data.get('started_at') else None,
        completed_at=datetime.fromisoformat(data.get('completed_at').replace('Z', '+00:00')) if data.get('completed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDeliveryAttemptsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

