from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook:
    url: str
    method: str
    signing_secret: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners:
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
class DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput:
    object: str
    id: str
    organization_id: str
    name: str
    status: str
    type: str
    retry: DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry
    listeners: List[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    webhook: Optional[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook] = None
    archived_at: Optional[datetime] = None


class mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook:
        return DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook(
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry:
        return DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners:
        return DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners(
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
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput:
        return DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        type=data.get('type'),
        webhook=mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        retry=mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        listeners=[mapDashboardOrganizationsEventDestinationsRotateWebhookSecretOutputListeners.from_dict(item) for item in data.get('listeners', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsRotateWebhookSecretOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

