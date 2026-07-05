from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesListToolsOutputItemsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionTemplatesListToolsOutputItemsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class SessionTemplatesListToolsOutputItemsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class SessionTemplatesListToolsOutputItems:
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
    input_schema: Optional[SessionTemplatesListToolsOutputItemsInputSchema] = None
    output_schema: Optional[SessionTemplatesListToolsOutputItemsOutputSchema] = None
    tags: Optional[SessionTemplatesListToolsOutputItemsTags] = None
@dataclass
class SessionTemplatesListToolsOutput:
    object: str
    items: List[SessionTemplatesListToolsOutputItems]


class mapSessionTemplatesListToolsOutputItemsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListToolsOutputItemsInputSchema:
        return SessionTemplatesListToolsOutputItemsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListToolsOutputItemsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListToolsOutputItemsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListToolsOutputItemsOutputSchema:
        return SessionTemplatesListToolsOutputItemsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListToolsOutputItemsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListToolsOutputItemsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListToolsOutputItemsTags:
        return SessionTemplatesListToolsOutputItemsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListToolsOutputItemsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListToolsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListToolsOutputItems:
        return SessionTemplatesListToolsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapSessionTemplatesListToolsOutputItemsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapSessionTemplatesListToolsOutputItemsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapSessionTemplatesListToolsOutputItemsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListToolsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesListToolsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesListToolsOutput:
        return SessionTemplatesListToolsOutput(
        object=data.get('object'),
        items=[mapSessionTemplatesListToolsOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesListToolsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

