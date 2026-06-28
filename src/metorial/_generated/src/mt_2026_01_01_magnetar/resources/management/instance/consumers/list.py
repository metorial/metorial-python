from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersListOutputItems:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceConsumersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceConsumersListOutput:
    items: List[ManagementInstanceConsumersListOutputItems]
    pagination: ManagementInstanceConsumersListOutputPagination


class mapManagementInstanceConsumersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersListOutputItems:
        return ManagementInstanceConsumersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersListOutputPagination:
        return ManagementInstanceConsumersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceConsumersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersListOutput:
        return ManagementInstanceConsumersListOutput(
        items=[mapManagementInstanceConsumersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceConsumersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    email: Optional[Union[str, List[str]]] = None
    id: Optional[str] = None


class mapManagementInstanceConsumersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersListQuery:
        return ManagementInstanceConsumersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        email=data.get('email'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

