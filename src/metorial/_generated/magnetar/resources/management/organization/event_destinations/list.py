from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventDestinationsListOutputItemsWebhook:
    url: str
    method: str
    signing_secret: Optional[str] = None
@dataclass
class ManagementOrganizationEventDestinationsListOutputItemsRetry:
    strategy: str
    max_attempts: float
    base_delay_seconds: float
    max_delay_seconds: float
@dataclass
class ManagementOrganizationEventDestinationsListOutputItemsListeners:
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
class ManagementOrganizationEventDestinationsListOutputItems:
    object: str
    id: str
    organization_id: str
    name: str
    status: str
    type: str
    retry: ManagementOrganizationEventDestinationsListOutputItemsRetry
    listeners: List[ManagementOrganizationEventDestinationsListOutputItemsListeners]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    webhook: Optional[ManagementOrganizationEventDestinationsListOutputItemsWebhook] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationEventDestinationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationEventDestinationsListOutput:
    items: List[ManagementOrganizationEventDestinationsListOutputItems]
    pagination: ManagementOrganizationEventDestinationsListOutputPagination


class mapManagementOrganizationEventDestinationsListOutputItemsWebhook:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutputItemsWebhook:
        return ManagementOrganizationEventDestinationsListOutputItemsWebhook(
        url=data.get('url'),
        method=data.get('method'),
        signing_secret=data.get('signing_secret')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutputItemsWebhook, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsListOutputItemsRetry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutputItemsRetry:
        return ManagementOrganizationEventDestinationsListOutputItemsRetry(
        strategy=data.get('strategy'),
        max_attempts=data.get('max_attempts'),
        base_delay_seconds=data.get('base_delay_seconds'),
        max_delay_seconds=data.get('max_delay_seconds')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutputItemsRetry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsListOutputItemsListeners:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutputItemsListeners:
        return ManagementOrganizationEventDestinationsListOutputItemsListeners(
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
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutputItemsListeners, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutputItems:
        return ManagementOrganizationEventDestinationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        description=data.get('description'),
        status=data.get('status'),
        type=data.get('type'),
        webhook=mapManagementOrganizationEventDestinationsListOutputItemsWebhook.from_dict(data.get('webhook')) if data.get('webhook') else None,
        retry=mapManagementOrganizationEventDestinationsListOutputItemsRetry.from_dict(data.get('retry')) if data.get('retry') else None,
        listeners=[mapManagementOrganizationEventDestinationsListOutputItemsListeners.from_dict(item) for item in data.get('listeners', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutputPagination:
        return ManagementOrganizationEventDestinationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventDestinationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListOutput:
        return ManagementOrganizationEventDestinationsListOutput(
        items=[mapManagementOrganizationEventDestinationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationEventDestinationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationEventDestinationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    callback_id: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None


class mapManagementOrganizationEventDestinationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventDestinationsListQuery:
        return ManagementOrganizationEventDestinationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        callback_id=data.get('callback_id'),
        chat_connection_id=data.get('chat_connection_id'),
        search=data.get('search')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventDestinationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

