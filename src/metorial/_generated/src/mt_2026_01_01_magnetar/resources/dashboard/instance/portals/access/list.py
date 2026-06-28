from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAccessListOutputItemsListing:
    id: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsAccessListOutputItemsConsumerGroup:
    object: str
    id: str
    status: str
    name: str
    is_default: bool
    sso_group_ids: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstancePortalsAccessListOutputItems:
    object: str
    id: str
    name: str
    access: Dict[str, Any]
    consumer_group: DashboardInstancePortalsAccessListOutputItemsConsumerGroup
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    readme: Optional[str] = None
    listing: Optional[DashboardInstancePortalsAccessListOutputItemsListing] = None
@dataclass
class DashboardInstancePortalsAccessListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsAccessListOutput:
    items: List[DashboardInstancePortalsAccessListOutputItems]
    pagination: DashboardInstancePortalsAccessListOutputPagination


class mapDashboardInstancePortalsAccessListOutputItemsListing:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListOutputItemsListing:
        return DashboardInstancePortalsAccessListOutputItemsListing(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListOutputItemsListing, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessListOutputItemsConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListOutputItemsConsumerGroup:
        return DashboardInstancePortalsAccessListOutputItemsConsumerGroup(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        is_default=data.get('is_default'),
        sso_group_ids=data.get('sso_group_ids', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListOutputItemsConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListOutputItems:
        return DashboardInstancePortalsAccessListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        readme=data.get('readme'),
        listing=mapDashboardInstancePortalsAccessListOutputItemsListing.from_dict(data.get('listing')) if data.get('listing') else None,
        access=data.get('access'),
        consumer_group=mapDashboardInstancePortalsAccessListOutputItemsConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListOutputPagination:
        return DashboardInstancePortalsAccessListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAccessListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListOutput:
        return DashboardInstancePortalsAccessListOutput(
        items=[mapDashboardInstancePortalsAccessListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsAccessListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAccessListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    consumer_group_id: Optional[Union[str, List[str]]] = None
    provider_template_id: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    skill_id: Optional[Union[str, List[str]]] = None
    skill_template_id: Optional[Union[str, List[str]]] = None
    skill_group_id: Optional[Union[str, List[str]]] = None
    skill_marketplace_id: Optional[Union[str, List[str]]] = None
    consumer_access_listing_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None


class mapDashboardInstancePortalsAccessListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAccessListQuery:
        return DashboardInstancePortalsAccessListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        consumer_group_id=data.get('consumer_group_id'),
        provider_template_id=data.get('provider_template_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        skill_id=data.get('skill_id'),
        skill_template_id=data.get('skill_template_id'),
        skill_group_id=data.get('skill_group_id'),
        skill_marketplace_id=data.get('skill_marketplace_id'),
        consumer_access_listing_id=data.get('consumer_access_listing_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAccessListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

