from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersToolsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersToolsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersToolsGetOutputTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ProvidersToolsGetOutput:
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
    input_schema: Optional[ProvidersToolsGetOutputInputSchema] = None
    output_schema: Optional[ProvidersToolsGetOutputOutputSchema] = None
    tags: Optional[ProvidersToolsGetOutputTags] = None


class mapProvidersToolsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsGetOutputInputSchema:
        return ProvidersToolsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersToolsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsGetOutputOutputSchema:
        return ProvidersToolsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersToolsGetOutputTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsGetOutputTags:
        return ProvidersToolsGetOutputTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsGetOutputTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersToolsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersToolsGetOutput:
        return ProvidersToolsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapProvidersToolsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersToolsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapProvidersToolsGetOutputTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersToolsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
