from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsConsumerAccessListOutputItemsConsumerGroup:
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
class PortalsConsumerAccessListOutputItems:
    object: str
    id: str
    access: Dict[str, Any]
    consumer_group: PortalsConsumerAccessListOutputItemsConsumerGroup
    created_at: datetime
    updated_at: datetime
@dataclass
class PortalsConsumerAccessListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class PortalsConsumerAccessListOutput:
    items: List[PortalsConsumerAccessListOutputItems]
    pagination: PortalsConsumerAccessListOutputPagination


class mapPortalsConsumerAccessListOutputItemsConsumerGroup:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerAccessListOutputItemsConsumerGroup:
        return PortalsConsumerAccessListOutputItemsConsumerGroup(
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
    def to_dict(value: Union[PortalsConsumerAccessListOutputItemsConsumerGroup, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerAccessListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerAccessListOutputItems:
        return PortalsConsumerAccessListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        consumer_group=mapPortalsConsumerAccessListOutputItemsConsumerGroup.from_dict(data.get('consumer_group')) if data.get('consumer_group') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerAccessListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerAccessListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerAccessListOutputPagination:
        return PortalsConsumerAccessListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerAccessListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapPortalsConsumerAccessListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerAccessListOutput:
        return PortalsConsumerAccessListOutput(
        items=[mapPortalsConsumerAccessListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapPortalsConsumerAccessListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerAccessListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class PortalsConsumerAccessListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    consumer_group_id: Optional[Union[str, List[str]]] = None
    provider_template_id: Optional[Union[str, List[str]]] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None
    type: Optional[Union[str, List[str]]] = None


class mapPortalsConsumerAccessListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsConsumerAccessListQuery:
        return PortalsConsumerAccessListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        consumer_group_id=data.get('consumer_group_id'),
        provider_template_id=data.get('provider_template_id'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        type=data.get('type')
        )

    @staticmethod
    def to_dict(value: Union[PortalsConsumerAccessListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

