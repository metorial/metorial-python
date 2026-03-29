from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersAuthMethodsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersAuthMethodsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersAuthMethodsGetOutputScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProvidersAuthMethodsGetOutput:
    object: str
    id: str
    type: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ProvidersAuthMethodsGetOutputInputSchema] = None
    output_schema: Optional[ProvidersAuthMethodsGetOutputOutputSchema] = None
    scopes: Optional[List[ProvidersAuthMethodsGetOutputScopes]] = None


class mapProvidersAuthMethodsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsGetOutputInputSchema:
        return ProvidersAuthMethodsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsGetOutputOutputSchema:
        return ProvidersAuthMethodsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsGetOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsGetOutputScopes:
        return ProvidersAuthMethodsGetOutputScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsGetOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersAuthMethodsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersAuthMethodsGetOutput:
        return ProvidersAuthMethodsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProvidersAuthMethodsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersAuthMethodsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProvidersAuthMethodsGetOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersAuthMethodsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

