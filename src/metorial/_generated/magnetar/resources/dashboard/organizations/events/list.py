from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventsListOutputItems:
    object: str
    id: str
    organization_id: str
    source: str
    event_type: str
    created_at: datetime
    instance_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
    callback_id: Optional[str] = None
    callback_trigger_key: Optional[str] = None
    chat_event_id: Optional[str] = None
    chat_integration_id: Optional[str] = None
@dataclass
class DashboardOrganizationsEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsEventsListOutput:
    items: List[DashboardOrganizationsEventsListOutputItems]
    pagination: DashboardOrganizationsEventsListOutputPagination


class mapDashboardOrganizationsEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventsListOutputItems:
        return DashboardOrganizationsEventsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        source=data.get('source'),
        event_type=data.get('event_type'),
        payload=data.get('payload'),
        callback_id=data.get('callback_id'),
        callback_trigger_key=data.get('callback_trigger_key'),
        chat_event_id=data.get('chat_event_id'),
        chat_integration_id=data.get('chat_integration_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventsListOutputPagination:
        return DashboardOrganizationsEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventsListOutput:
        return DashboardOrganizationsEventsListOutput(
        items=[mapDashboardOrganizationsEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsEventsListQuery:
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
    chat_integration_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsEventsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventsListQuery:
        return DashboardOrganizationsEventsListQuery(
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
        chat_integration_id=data.get('chat_integration_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

