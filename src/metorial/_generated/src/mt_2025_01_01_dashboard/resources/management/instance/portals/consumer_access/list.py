from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup:
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
class ManagementInstancePortalsConsumerAccessListOutputItems:
    object: str
    id: str
    access: Dict[str, Any]
    consumer_group: ManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstancePortalsConsumerAccessListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsConsumerAccessListOutput:
    items: List[ManagementInstancePortalsConsumerAccessListOutputItems]
    pagination: ManagementInstancePortalsConsumerAccessListOutputPagination


class mapManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup:
        return ManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup(
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
    def to_dict(value: Union[ManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerAccessListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerAccessListOutputItems:
        return ManagementInstancePortalsConsumerAccessListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        consumer_group=mapManagementInstancePortalsConsumerAccessListOutputItemsConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerAccessListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerAccessListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerAccessListOutputPagination:
        return ManagementInstancePortalsConsumerAccessListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerAccessListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerAccessListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerAccessListOutput:
        return ManagementInstancePortalsConsumerAccessListOutput(
        items=[mapManagementInstancePortalsConsumerAccessListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsConsumerAccessListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerAccessListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsConsumerAccessListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    id: Optional[str] = None
    consumer_group_id: Optional[Union[str, List[str]]] = None
    provider_template_id: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None


class mapManagementInstancePortalsConsumerAccessListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerAccessListQuery:
        return ManagementInstancePortalsConsumerAccessListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        id=data.get('id'),
        consumer_group_id=data.get('consumer_group_id'),
        provider_template_id=data.get('provider_template_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerAccessListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

