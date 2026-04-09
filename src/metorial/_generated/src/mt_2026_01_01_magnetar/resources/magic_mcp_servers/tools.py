from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpServersToolsOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpServersToolsOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpServersToolsOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class MagicMcpServersToolsOutputItems:
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
    input_schema: Optional[MagicMcpServersToolsOutputItemsInputSchema] = None
    output_schema: Optional[MagicMcpServersToolsOutputItemsOutputSchema] = None
    tags: Optional[MagicMcpServersToolsOutputItemsTags] = None
@dataclass
class MagicMcpServersToolsOutput:
    object: str
    items: List[MagicMcpServersToolsOutputItems]


class mapMagicMcpServersToolsOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersToolsOutputItemsInputSchema:
        return MagicMcpServersToolsOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersToolsOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersToolsOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersToolsOutputItemsOutputSchema:
        return MagicMcpServersToolsOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersToolsOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersToolsOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersToolsOutputItemsTags:
        return MagicMcpServersToolsOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersToolsOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersToolsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersToolsOutputItems:
        return MagicMcpServersToolsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapMagicMcpServersToolsOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapMagicMcpServersToolsOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapMagicMcpServersToolsOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersToolsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersToolsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersToolsOutput:
        return MagicMcpServersToolsOutput(
        object=data.get('object'),
        items=[mapMagicMcpServersToolsOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersToolsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

