from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsEventDestinationListenersListOutputItems:
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
class DashboardOrganizationsEventDestinationListenersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsEventDestinationListenersListOutput:
    items: List[DashboardOrganizationsEventDestinationListenersListOutputItems]
    pagination: DashboardOrganizationsEventDestinationListenersListOutputPagination


class mapDashboardOrganizationsEventDestinationListenersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationListenersListOutputItems:
        return DashboardOrganizationsEventDestinationListenersListOutputItems(
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
    def to_dict(value: Union[DashboardOrganizationsEventDestinationListenersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationListenersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationListenersListOutputPagination:
        return DashboardOrganizationsEventDestinationListenersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationListenersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsEventDestinationListenersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationListenersListOutput:
        return DashboardOrganizationsEventDestinationListenersListOutput(
        items=[mapDashboardOrganizationsEventDestinationListenersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsEventDestinationListenersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationListenersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsEventDestinationListenersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    event_destination_id: Optional[Union[str, List[str]]] = None
    instance_id: Optional[Union[str, List[str]]] = None
    callback_id: Optional[Union[str, List[str]]] = None
    chat_connection_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsEventDestinationListenersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsEventDestinationListenersListQuery:
        return DashboardOrganizationsEventDestinationListenersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        event_destination_id=data.get('event_destination_id'),
        instance_id=data.get('instance_id'),
        callback_id=data.get('callback_id'),
        chat_connection_id=data.get('chat_connection_id'),
        provider_id=data.get('provider_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsEventDestinationListenersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

