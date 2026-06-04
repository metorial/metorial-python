from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderToolsListOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderToolsListOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderToolsListOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceProviderToolsListOutputItems:
    object: str
    id: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    constraints: List[str]
    instructions: List[str]
    specification_id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ManagementInstanceProviderToolsListOutputItemsInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderToolsListOutputItemsOutputSchema] = None
    tags: Optional[ManagementInstanceProviderToolsListOutputItemsTags] = None
@dataclass
class ManagementInstanceProviderToolsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderToolsListOutput:
    items: List[ManagementInstanceProviderToolsListOutputItems]
    pagination: ManagementInstanceProviderToolsListOutputPagination


class mapManagementInstanceProviderToolsListOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutputItemsInputSchema:
        return ManagementInstanceProviderToolsListOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsListOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutputItemsOutputSchema:
        return ManagementInstanceProviderToolsListOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsListOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutputItemsTags:
        return ManagementInstanceProviderToolsListOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutputItems:
        return ManagementInstanceProviderToolsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceProviderToolsListOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderToolsListOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceProviderToolsListOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutputPagination:
        return ManagementInstanceProviderToolsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListOutput:
        return ManagementInstanceProviderToolsListOutput(
        items=[mapManagementInstanceProviderToolsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderToolsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderToolsListQuery:
    provider_version_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceProviderToolsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsListQuery:
        return ManagementInstanceProviderToolsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

