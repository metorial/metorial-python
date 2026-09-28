from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationEventsListOutputItems:
    object: str
    id: str
    organization_id: str
    source: str
    event_type: str
    created_at: datetime
    instance_id: Optional[str] = None
    callback_id: Optional[str] = None
    callback_event_id: Optional[str] = None
    callback_trigger_key: Optional[str] = None
    chat_event_id: Optional[str] = None
    chat_connection_id: Optional[str] = None
    provider_id: Optional[str] = None
@dataclass
class ManagementOrganizationEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationEventsListOutput:
    items: List[ManagementOrganizationEventsListOutputItems]
    pagination: ManagementOrganizationEventsListOutputPagination


class mapManagementOrganizationEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventsListOutputItems:
        return ManagementOrganizationEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        source=data.get('source'),
        event_type=data.get('event_type'),
        callback_id=data.get('callback_id'),
        callback_event_id=data.get('callback_event_id'),
        callback_trigger_key=data.get('callback_trigger_key'),
        chat_event_id=data.get('chat_event_id'),
        chat_connection_id=data.get('chat_connection_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventsListOutputPagination:
        return ManagementOrganizationEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventsListOutput:
        return ManagementOrganizationEventsListOutput(
        items=[mapManagementOrganizationEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationEventsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementOrganizationEventsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    instance_id: Optional[str] = None
    event_type: Optional[Union[str, List[str]]] = None
    source: Optional[Union[str, List[str]]] = None
    callback_id: Optional[Union[str, List[str]]] = None
    callback_trigger_key: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementOrganizationEventsListQueryCreatedAt] = None


class mapManagementOrganizationEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationEventsListQuery:
        return ManagementOrganizationEventsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        instance_id=data.get('instance_id'),
        event_type=data.get('event_type'),
        source=data.get('source'),
        callback_id=data.get('callback_id'),
        callback_trigger_key=data.get('callback_trigger_key'),
        chat_connection_id=data.get('chat_connection_id'),
        provider_id=data.get('provider_id'),
        created_at=mapManagementOrganizationEventsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

