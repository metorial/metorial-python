from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderToolsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderToolsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderToolsGetOutputTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceProviderToolsGetOutput:
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
    input_schema: Optional[ManagementInstanceProviderToolsGetOutputInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderToolsGetOutputOutputSchema] = None
    tags: Optional[ManagementInstanceProviderToolsGetOutputTags] = None


class mapManagementInstanceProviderToolsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsGetOutputInputSchema:
        return ManagementInstanceProviderToolsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsGetOutputOutputSchema:
        return ManagementInstanceProviderToolsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsGetOutputTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsGetOutputTags:
        return ManagementInstanceProviderToolsGetOutputTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsGetOutputTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderToolsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderToolsGetOutput:
        return ManagementInstanceProviderToolsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceProviderToolsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderToolsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceProviderToolsGetOutputTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderToolsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

