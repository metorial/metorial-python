from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCallbackEventsGetOutputDetailsError:
    object: str
    code: str
    message: str
@dataclass
class ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
    encoding: str
    content: str
@dataclass
class ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest:
    object: str
    method: str
    url: str
    headers: Dict[str, str]
    body: Optional[ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody] = None
@dataclass
class ManagementInstanceCallbackEventsGetOutputDetailsWebhook:
    object: str
    status: str
    received_at: datetime
    request: Optional[ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest] = None
@dataclass
class ManagementInstanceCallbackEventsGetOutputDetails:
    object: str
    status: str
    payload: Optional[Dict[str, Any]] = None
    error: Optional[ManagementInstanceCallbackEventsGetOutputDetailsError] = None
    webhook: Optional[ManagementInstanceCallbackEventsGetOutputDetailsWebhook] = None
@dataclass
class ManagementInstanceCallbackEventsGetOutput:
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
    details: Optional[ManagementInstanceCallbackEventsGetOutputDetails] = None


class mapManagementInstanceCallbackEventsGetOutputDetailsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutputDetailsError:
        return ManagementInstanceCallbackEventsGetOutputDetailsError(
        object=data.get('object'),
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutputDetailsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody:
        return ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody(
        encoding=data.get('encoding'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest:
        return ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest(
        object=data.get('object'),
        method=data.get('method'),
        url=data.get('url'),
        headers=data.get('headers'),
        body=mapManagementInstanceCallbackEventsGetOutputDetailsWebhookRequestBody.from_dict(data.get('body')) if data.get('body') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsGetOutputDetailsWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutputDetailsWebhook:
        return ManagementInstanceCallbackEventsGetOutputDetailsWebhook(
        object=data.get('object'),
        status=data.get('status'),
        request=mapManagementInstanceCallbackEventsGetOutputDetailsWebhookRequest.from_dict(data.get('request')) if data.get('request') else None,
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutputDetailsWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsGetOutputDetails:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutputDetails:
        return ManagementInstanceCallbackEventsGetOutputDetails(
        object=data.get('object'),
        status=data.get('status'),
        payload=data.get('payload'),
        error=mapManagementInstanceCallbackEventsGetOutputDetailsError.from_dict(data.get('error')) if data.get('error') else None,
        webhook=mapManagementInstanceCallbackEventsGetOutputDetailsWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutputDetails, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCallbackEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCallbackEventsGetOutput:
        return ManagementInstanceCallbackEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_trigger_key=data.get('provider_trigger_key'),
        mapped_type=data.get('mapped_type'),
        mapped_id=data.get('mapped_id'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        details=mapManagementInstanceCallbackEventsGetOutputDetails.from_dict(data.get('details')) if data.get('details') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCallbackEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

