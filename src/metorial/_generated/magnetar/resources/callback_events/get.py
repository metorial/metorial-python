from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class CallbackEventsGetOutputDetailsError:
    object: str
    code: str
    message: str
@dataclass
class CallbackEventsGetOutputDetailsWebhookRequestBody:
    encoding: str
    content: str
@dataclass
class CallbackEventsGetOutputDetailsWebhookRequest:
    object: str
    method: str
    url: str
    headers: Dict[str, str]
    body: Optional[CallbackEventsGetOutputDetailsWebhookRequestBody] = None
@dataclass
class CallbackEventsGetOutputDetailsWebhook:
    object: str
    status: str
    received_at: datetime
    request: Optional[CallbackEventsGetOutputDetailsWebhookRequest] = None
@dataclass
class CallbackEventsGetOutputDetails:
    object: str
    status: str
    payload: Optional[Dict[str, Any]] = None
    error: Optional[CallbackEventsGetOutputDetailsError] = None
    webhook: Optional[CallbackEventsGetOutputDetailsWebhook] = None
@dataclass
class CallbackEventsGetOutput:
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
    details: Optional[CallbackEventsGetOutputDetails] = None


class mapCallbackEventsGetOutputDetailsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutputDetailsError:
        return CallbackEventsGetOutputDetailsError(
        object=data.get('object'),
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutputDetailsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackEventsGetOutputDetailsWebhookRequestBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutputDetailsWebhookRequestBody:
        return CallbackEventsGetOutputDetailsWebhookRequestBody(
        encoding=data.get('encoding'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutputDetailsWebhookRequestBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackEventsGetOutputDetailsWebhookRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutputDetailsWebhookRequest:
        return CallbackEventsGetOutputDetailsWebhookRequest(
        object=data.get('object'),
        method=data.get('method'),
        url=data.get('url'),
        headers=data.get('headers'),
        body=mapCallbackEventsGetOutputDetailsWebhookRequestBody.from_dict(data.get('body')) if data.get('body') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutputDetailsWebhookRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackEventsGetOutputDetailsWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutputDetailsWebhook:
        return CallbackEventsGetOutputDetailsWebhook(
        object=data.get('object'),
        status=data.get('status'),
        request=mapCallbackEventsGetOutputDetailsWebhookRequest.from_dict(data.get('request')) if data.get('request') else None,
        received_at=datetime.fromisoformat(data.get('received_at').replace('Z', '+00:00')) if data.get('received_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutputDetailsWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackEventsGetOutputDetails:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutputDetails:
        return CallbackEventsGetOutputDetails(
        object=data.get('object'),
        status=data.get('status'),
        payload=data.get('payload'),
        error=mapCallbackEventsGetOutputDetailsError.from_dict(data.get('error')) if data.get('error') else None,
        webhook=mapCallbackEventsGetOutputDetailsWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutputDetails, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapCallbackEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> CallbackEventsGetOutput:
        return CallbackEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_trigger_key=data.get('provider_trigger_key'),
        mapped_type=data.get('mapped_type'),
        mapped_id=data.get('mapped_id'),
        callback_id=data.get('callback_id'),
        callback_instance_id=data.get('callback_instance_id'),
        details=mapCallbackEventsGetOutputDetails.from_dict(data.get('details')) if data.get('details') else None,
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[CallbackEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

