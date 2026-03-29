from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersTriggersGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersTriggersGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersTriggersGetOutput:
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
    input_schema: Optional[ProvidersTriggersGetOutputInputSchema] = None
    output_schema: Optional[ProvidersTriggersGetOutputOutputSchema] = None


class mapProvidersTriggersGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersGetOutputInputSchema:
        return ProvidersTriggersGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersGetOutputOutputSchema:
        return ProvidersTriggersGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersTriggersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersTriggersGetOutput:
        return ProvidersTriggersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=mapProvidersTriggersGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersTriggersGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        invocation=data.get('invocation'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersTriggersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

