from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpServersToolsOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpServersToolsOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceMagicMcpServersToolsOutputItems:
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
    input_schema: Optional[ManagementInstanceMagicMcpServersToolsOutputItemsInputSchema] = None
    output_schema: Optional[ManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema] = None
    tags: Optional[ManagementInstanceMagicMcpServersToolsOutputItemsTags] = None
@dataclass
class ManagementInstanceMagicMcpServersToolsOutput:
    object: str
    items: List[ManagementInstanceMagicMcpServersToolsOutputItems]


class mapManagementInstanceMagicMcpServersToolsOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersToolsOutputItemsInputSchema:
        return ManagementInstanceMagicMcpServersToolsOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersToolsOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema:
        return ManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersToolsOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersToolsOutputItemsTags:
        return ManagementInstanceMagicMcpServersToolsOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersToolsOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersToolsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersToolsOutputItems:
        return ManagementInstanceMagicMcpServersToolsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceMagicMcpServersToolsOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceMagicMcpServersToolsOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceMagicMcpServersToolsOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersToolsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersToolsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersToolsOutput:
        return ManagementInstanceMagicMcpServersToolsOutput(
        object=data.get('object'),
        items=[mapManagementInstanceMagicMcpServersToolsOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersToolsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

