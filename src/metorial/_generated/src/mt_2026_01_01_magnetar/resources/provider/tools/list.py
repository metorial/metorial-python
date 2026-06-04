from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderToolsListOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderToolsListOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderToolsListOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ProviderToolsListOutputItems:
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
    input_schema: Optional[ProviderToolsListOutputItemsInputSchema] = None
    output_schema: Optional[ProviderToolsListOutputItemsOutputSchema] = None
    tags: Optional[ProviderToolsListOutputItemsTags] = None
@dataclass
class ProviderToolsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderToolsListOutput:
    items: List[ProviderToolsListOutputItems]
    pagination: ProviderToolsListOutputPagination


class mapProviderToolsListOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutputItemsInputSchema:
        return ProviderToolsListOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsListOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutputItemsOutputSchema:
        return ProviderToolsListOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsListOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutputItemsTags:
        return ProviderToolsListOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutputItems:
        return ProviderToolsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapProviderToolsListOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderToolsListOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapProviderToolsListOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutputPagination:
        return ProviderToolsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListOutput:
        return ProviderToolsListOutput(
        items=[mapProviderToolsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderToolsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderToolsListQuery:
    provider_version_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProviderToolsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsListQuery:
        return ProviderToolsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

