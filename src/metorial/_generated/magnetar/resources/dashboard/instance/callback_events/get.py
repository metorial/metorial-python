from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCallbackEventsGetOutputDetailsError:
    object: str
    code: str
    message: str
@dataclass
class DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
    encoding: str
    content: str
@dataclass
class DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest:
    object: str
    method: str
    url: str
    headers: Dict[str, str]
    body: Optional[DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody] = None
@dataclass
class DashboardInstanceCallbackEventsGetOutputDetailsWebhook:
    object: str
    id: str
    status: str
    received_at: datetime
    request: Optional[DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest] = None
@dataclass
class DashboardInstanceCallbackEventsGetOutputDetails:
    object: str
    status: str
    payload: Optional[Dict[str, Any]] = None
    error: Optional[DashboardInstanceCallbackEventsGetOutputDetailsError] = None
    webhook: Optional[DashboardInstanceCallbackEventsGetOutputDetailsWebhook] = None
@dataclass
class DashboardInstanceCallbackEventsGetOutput:
    object: str
    id: str
    status: str
    source: str
    provider_trigger_key: str
    callback_id: str
    callback_instance_id: str
    occurred_at: datetime
    created_at: datetime
    mapped_type: Optional[str] = None
    mapped_id: Optional[str] = None
    details: Optional[DashboardInstanceCallbackEventsGetOutputDetails] = None


class mapDashboardInstanceCallbackEventsGetOutputDetailsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutputDetailsError:
        return DashboardInstanceCallbackEventsGetOutputDetailsError(
        object=data.get('object'),
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutputDetailsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
        return DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody(
        encoding=data.get('encoding'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest:
        return DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest(
        object=data.get('object'),
        method=data.get('method'),
        url=data.get('url'),
        headers=data.get('headers'),
        body=mapDashboardInstanceCallbackEventsGetOutputDetailsWebhookRequestBody.from_dict(data.get('body')) if data.get('body') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsGetOutputDetailsWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutputDetailsWebhook:
        return DashboardInstanceCallbackEventsGetOutputDetailsWebhook(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        request=mapDashboardInstanceCallbackEventsGetOutputDetailsWebhookRequest.from_dict(data.get('request')) if data.get('request') else None,
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutputDetailsWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsGetOutputDetails:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutputDetails:
        return DashboardInstanceCallbackEventsGetOutputDetails(
        object=data.get('object'),
        status=data.get('status'),
        payload=data.get('payload'),
        error=mapDashboardInstanceCallbackEventsGetOutputDetailsError.from_dict(data.get('error')) if data.get('error') else None,
        webhook=mapDashboardInstanceCallbackEventsGetOutputDetailsWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutputDetails, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCallbackEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbackEventsGetOutput:
        return DashboardInstanceCallbackEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_trigger_key=data.get('provider_trigger_key'),
        mapped_type=data.get('mapped_type'),
        mapped_id=data.get('mapped_id'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        details=mapDashboardInstanceCallbackEventsGetOutputDetails.from_dict(data.get('details')) if data.get('details') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCallbackEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

