from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDestinationsCreateOutputWebhook:
    url: str
    method: str
    signing_secret: Optional[str] = None
@dataclass
class ManagementOrganizationEventDestinationsCreateOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class ManagementOrganizationEventDestinationsCreateOutputListeners:
    object: str
    id: str
    instance_id: str
    event_destination_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    event_types: Optional[List[str]] = None
    callback_id: Optional[str] = None
    triggers: Optional[List[str]] = None
    chat_connection_id: Optional[str] = None
    provider_id: Optional[str] = None
@dataclass
class ManagementOrganizationEventDestinationsCreateOutput:
    object: str
    id: str
    organization_id: str
    name: str
    status: str
    type: str
    retry: ManagementOrganizationEventDestinationsCreateOutputRetry
    listeners: List[ManagementOrganizationEventDestinationsCreateOutputListeners]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    webhook: Optional[ManagementOrganizationEventDestinationsCreateOutputWebhook] = None
    archived_at: Optional[datetime] = None


class mapManagementOrganizationEventDestinationsCreateOutputWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateOutputWebhook:
        return ManagementOrganizationEventDestinationsCreateOutputWebhook(
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateOutputWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsCreateOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateOutputRetry:
        return ManagementOrganizationEventDestinationsCreateOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsCreateOutputListeners:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateOutputListeners:
        return ManagementOrganizationEventDestinationsCreateOutputListeners(
        object=data.get('object'),
        id=data.get('id'),
        instance_id=data.get('instance_id'),
        event_destination_id=data.get('event_destination_id'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        callback_id=data.get('callback_id'),
        triggers=data.get('triggers', []),
        chat_connection_id=data.get('chat_connection_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateOutputListeners, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateOutput:
        return ManagementOrganizationEventDestinationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        type=data.get('type'),
        webhook=mapManagementOrganizationEventDestinationsCreateOutputWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        retry=mapManagementOrganizationEventDestinationsCreateOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        listeners=[mapManagementOrganizationEventDestinationsCreateOutputListeners.from_dict(item) for item in data.get('listeners', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationEventDestinationsCreateBodyWebhook:
    url: str
@dataclass
class ManagementOrganizationEventDestinationsCreateBodyRetry:
    strategy: Optional[str] = None
    max_attempts: Optional[float] = None
    base_delay_seconds: Optional[float] = None
    max_delay_seconds: Optional[float] = None
@dataclass
class ManagementOrganizationEventDestinationsCreateBody:
    name: str
    type: str
    webhook: ManagementOrganizationEventDestinationsCreateBodyWebhook
    description: Optional[str] = None
    retry: Optional[ManagementOrganizationEventDestinationsCreateBodyRetry] = None


class mapManagementOrganizationEventDestinationsCreateBodyWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateBodyWebhook:
        return ManagementOrganizationEventDestinationsCreateBodyWebhook(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateBodyWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsCreateBodyRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateBodyRetry:
        return ManagementOrganizationEventDestinationsCreateBodyRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateBodyRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsCreateBody:
        return ManagementOrganizationEventDestinationsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        webhook=mapManagementOrganizationEventDestinationsCreateBodyWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        retry=mapManagementOrganizationEventDestinationsCreateBodyRetry.from_dict(data.get('retry')) if data.get('retry') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

