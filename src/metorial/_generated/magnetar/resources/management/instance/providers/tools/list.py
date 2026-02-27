from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersToolsListOutputItems:
    object: str
    id: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    output_schema: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProvidersToolsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProvidersToolsListOutput:
    items: List[ManagementInstanceProvidersToolsListOutputItems]
    pagination: ManagementInstanceProvidersToolsListOutputPagination


class mapManagementInstanceProvidersToolsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersToolsListOutputItems:
        return ManagementInstanceProvidersToolsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        title=data.get('title'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersToolsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersToolsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersToolsListOutputPagination:
        return ManagementInstanceProvidersToolsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersToolsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersToolsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersToolsListOutput:
        return ManagementInstanceProvidersToolsListOutput(
        items=[mapManagementInstanceProvidersToolsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProvidersToolsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersToolsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProvidersToolsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_version_id: Optional[str] = None


class mapManagementInstanceProvidersToolsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersToolsListQuery:
        return ManagementInstanceProvidersToolsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersToolsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
