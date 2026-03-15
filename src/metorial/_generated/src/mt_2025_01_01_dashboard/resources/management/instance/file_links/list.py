from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceFileLinksListOutputItems:
    object: str
    id: str
    file_id: str
    url: str
    created_at: datetime
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceFileLinksListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceFileLinksListOutput:
    items: List[ManagementInstanceFileLinksListOutputItems]
    pagination: ManagementInstanceFileLinksListOutputPagination


class mapManagementInstanceFileLinksListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFileLinksListOutputItems:
        return ManagementInstanceFileLinksListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        file_id=data.get('file_id'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFileLinksListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFileLinksListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFileLinksListOutputPagination:
        return ManagementInstanceFileLinksListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFileLinksListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceFileLinksListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFileLinksListOutput:
        return ManagementInstanceFileLinksListOutput(
        items=[mapManagementInstanceFileLinksListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceFileLinksListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFileLinksListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceFileLinksListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    file_id: Optional[str] = None


class mapManagementInstanceFileLinksListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceFileLinksListQuery:
        return ManagementInstanceFileLinksListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        file_id=data.get('file_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceFileLinksListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

