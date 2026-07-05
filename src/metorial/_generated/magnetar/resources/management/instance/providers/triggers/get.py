from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersTriggersGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersTriggersGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersTriggersGetOutput:
    object: str
    id: str
    key: str
    name: str
    invocation: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ManagementInstanceProvidersTriggersGetOutputInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersTriggersGetOutputOutputSchema] = None


class mapManagementInstanceProvidersTriggersGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersTriggersGetOutputInputSchema:
        return ManagementInstanceProvidersTriggersGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersTriggersGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersTriggersGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersTriggersGetOutputOutputSchema:
        return ManagementInstanceProvidersTriggersGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersTriggersGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersTriggersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersTriggersGetOutput:
        return ManagementInstanceProvidersTriggersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapManagementInstanceProvidersTriggersGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersTriggersGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersTriggersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

