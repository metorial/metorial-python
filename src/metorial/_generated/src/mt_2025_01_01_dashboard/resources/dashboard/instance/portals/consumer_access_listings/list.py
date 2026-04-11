from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups:
    id: str
    name: str
    index: float
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerAccessListingsListOutputItems:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    groups: List[DashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
@dataclass
class DashboardInstancePortalsConsumerAccessListingsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsConsumerAccessListingsListOutput:
    items: List[DashboardInstancePortalsConsumerAccessListingsListOutputItems]
    pagination: DashboardInstancePortalsConsumerAccessListingsListOutputPagination


class mapDashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups:
        return DashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerAccessListingsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessListingsListOutputItems:
        return DashboardInstancePortalsConsumerAccessListingsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        access=data.get('access'),
        groups=[mapDashboardInstancePortalsConsumerAccessListingsListOutputItemsGroups.from_dict(item) for item in data.get('groups', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessListingsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerAccessListingsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessListingsListOutputPagination:
        return DashboardInstancePortalsConsumerAccessListingsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessListingsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsConsumerAccessListingsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessListingsListOutput:
        return DashboardInstancePortalsConsumerAccessListingsListOutput(
        items=[mapDashboardInstancePortalsConsumerAccessListingsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsConsumerAccessListingsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessListingsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsConsumerAccessListingsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    consumer_surface_provider_group_id: Optional[Union[str, List[str]]] = None
    provider_template_id: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None


class mapDashboardInstancePortalsConsumerAccessListingsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsConsumerAccessListingsListQuery:
        return DashboardInstancePortalsConsumerAccessListingsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        consumer_surface_provider_group_id=data.get('consumer_surface_provider_group_id'),
        provider_template_id=data.get('provider_template_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsConsumerAccessListingsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

