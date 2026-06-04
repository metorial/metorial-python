from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderToolsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderToolsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderToolsGetOutputTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ProviderToolsGetOutput:
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
    input_schema: Optional[ProviderToolsGetOutputInputSchema] = None
    output_schema: Optional[ProviderToolsGetOutputOutputSchema] = None
    tags: Optional[ProviderToolsGetOutputTags] = None


class mapProviderToolsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsGetOutputInputSchema:
        return ProviderToolsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsGetOutputOutputSchema:
        return ProviderToolsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsGetOutputTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsGetOutputTags:
        return ProviderToolsGetOutputTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsGetOutputTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderToolsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderToolsGetOutput:
        return ProviderToolsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapProviderToolsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderToolsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapProviderToolsGetOutputTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderToolsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

