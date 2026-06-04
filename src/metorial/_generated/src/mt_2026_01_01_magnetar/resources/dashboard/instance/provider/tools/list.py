from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderToolsListOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderToolsListOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderToolsListOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceProviderToolsListOutputItems:
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
    input_schema: Optional[DashboardInstanceProviderToolsListOutputItemsInputSchema] = None
    output_schema: Optional[DashboardInstanceProviderToolsListOutputItemsOutputSchema] = None
    tags: Optional[DashboardInstanceProviderToolsListOutputItemsTags] = None
@dataclass
class DashboardInstanceProviderToolsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderToolsListOutput:
    items: List[DashboardInstanceProviderToolsListOutputItems]
    pagination: DashboardInstanceProviderToolsListOutputPagination


class mapDashboardInstanceProviderToolsListOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutputItemsInputSchema:
        return DashboardInstanceProviderToolsListOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderToolsListOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutputItemsOutputSchema:
        return DashboardInstanceProviderToolsListOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderToolsListOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutputItemsTags:
        return DashboardInstanceProviderToolsListOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderToolsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutputItems:
        return DashboardInstanceProviderToolsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceProviderToolsListOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProviderToolsListOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceProviderToolsListOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderToolsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutputPagination:
        return DashboardInstanceProviderToolsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderToolsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListOutput:
        return DashboardInstanceProviderToolsListOutput(
        items=[mapDashboardInstanceProviderToolsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderToolsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderToolsListQuery:
    provider_version_id: str
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceProviderToolsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderToolsListQuery:
        return DashboardInstanceProviderToolsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_version_id=data.get('provider_version_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderToolsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

