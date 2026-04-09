from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpServersToolsOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceMagicMcpServersToolsOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceMagicMcpServersToolsOutputItems:
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
    input_schema: Optional[DashboardInstanceMagicMcpServersToolsOutputItemsInputSchema] = None
    output_schema: Optional[DashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema] = None
    tags: Optional[DashboardInstanceMagicMcpServersToolsOutputItemsTags] = None
@dataclass
class DashboardInstanceMagicMcpServersToolsOutput:
    object: str
    items: List[DashboardInstanceMagicMcpServersToolsOutputItems]


class mapDashboardInstanceMagicMcpServersToolsOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersToolsOutputItemsInputSchema:
        return DashboardInstanceMagicMcpServersToolsOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersToolsOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema:
        return DashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersToolsOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersToolsOutputItemsTags:
        return DashboardInstanceMagicMcpServersToolsOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersToolsOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersToolsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersToolsOutputItems:
        return DashboardInstanceMagicMcpServersToolsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceMagicMcpServersToolsOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceMagicMcpServersToolsOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceMagicMcpServersToolsOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersToolsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersToolsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersToolsOutput:
        return DashboardInstanceMagicMcpServersToolsOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceMagicMcpServersToolsOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersToolsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

