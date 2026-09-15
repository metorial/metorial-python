from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDestinationsCreateOutputWebhook:
    url: str
    method: str
    signing_secret: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDestinationsCreateOutputListeners:
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
    chat_integration_id: Optional[str] = None
@dataclass
class DashboardOrganizationsEventDestinationsCreateOutput:
    object: str
    id: str
    organization_id: str
    name: str
    status: str
    type: str
    listeners: List[DashboardOrganizationsEventDestinationsCreateOutputListeners]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    webhook: Optional[DashboardOrganizationsEventDestinationsCreateOutputWebhook] = None
    archived_at: Optional[datetime] = None


class mapDashboardOrganizationsEventDestinationsCreateOutputWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsCreateOutputWebhook:
        return DashboardOrganizationsEventDestinationsCreateOutputWebhook(
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsCreateOutputWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsCreateOutputListeners:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsCreateOutputListeners:
        return DashboardOrganizationsEventDestinationsCreateOutputListeners(
        object=data.get('object'),
        id=data.get('id'),
        instance_id=data.get('instance_id'),
        event_destination_id=data.get('event_destination_id'),
        type=data.get('type'),
        event_types=data.get('event_types', []),
        callback_id=data.get('callback_id'),
        triggers=data.get('triggers', []),
        chat_integration_id=data.get('chat_integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsCreateOutputListeners, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsCreateOutput:
        return DashboardOrganizationsEventDestinationsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        type=data.get('type'),
        webhook=mapDashboardOrganizationsEventDestinationsCreateOutputWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        listeners=[mapDashboardOrganizationsEventDestinationsCreateOutputListeners.from_dict(item) for item in data.get('listeners', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsEventDestinationsCreateBodyWebhook:
    url: str
@dataclass
class DashboardOrganizationsEventDestinationsCreateBody:
    name: str
    type: str
    webhook: DashboardOrganizationsEventDestinationsCreateBodyWebhook
    description: Optional[str] = None


class mapDashboardOrganizationsEventDestinationsCreateBodyWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsCreateBodyWebhook:
        return DashboardOrganizationsEventDestinationsCreateBodyWebhook(
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsCreateBodyWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationsCreateBody:
        return DashboardOrganizationsEventDestinationsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        webhook=mapDashboardOrganizationsEventDestinationsCreateBodyWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

