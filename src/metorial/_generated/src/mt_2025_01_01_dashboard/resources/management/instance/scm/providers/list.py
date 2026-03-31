from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmProvidersListOutputItems:
    object: str
    id: str
    type: str
    name: str
    is_default: bool
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    api_url: Optional[str] = None
    web_url: Optional[str] = None
@dataclass
class ManagementInstanceScmProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceScmProvidersListOutput:
    items: List[ManagementInstanceScmProvidersListOutputItems]
    pagination: ManagementInstanceScmProvidersListOutputPagination


class mapManagementInstanceScmProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmProvidersListOutputItems:
        return ManagementInstanceScmProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        api_url=data.get('api_url'),
        web_url=data.get('web_url'),
        is_default=data.get('is_default'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmProvidersListOutputPagination:
        return ManagementInstanceScmProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmProvidersListOutput:
        return ManagementInstanceScmProvidersListOutput(
        items=[mapManagementInstanceScmProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceScmProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceScmProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmProvidersListQuery:
        return ManagementInstanceScmProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

