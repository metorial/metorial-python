from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsConsumerGroupsListOutputItems:
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
class ManagementInstancePortalsConsumerGroupsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstancePortalsConsumerGroupsListOutput:
    items: List[ManagementInstancePortalsConsumerGroupsListOutputItems]
    pagination: ManagementInstancePortalsConsumerGroupsListOutputPagination


class mapManagementInstancePortalsConsumerGroupsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerGroupsListOutputItems:
        return ManagementInstancePortalsConsumerGroupsListOutputItems(
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
    def to_dict(value: Union[ManagementInstancePortalsConsumerGroupsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerGroupsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerGroupsListOutputPagination:
        return ManagementInstancePortalsConsumerGroupsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerGroupsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsConsumerGroupsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerGroupsListOutput:
        return ManagementInstancePortalsConsumerGroupsListOutput(
        items=[mapManagementInstancePortalsConsumerGroupsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstancePortalsConsumerGroupsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerGroupsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsConsumerGroupsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    id: Optional[str] = None


class mapManagementInstancePortalsConsumerGroupsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsConsumerGroupsListQuery:
        return ManagementInstancePortalsConsumerGroupsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        search=data.get('search'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsConsumerGroupsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

