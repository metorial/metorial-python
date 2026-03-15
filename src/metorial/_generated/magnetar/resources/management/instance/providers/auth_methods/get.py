from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersAuthMethodsGetOutputInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersAuthMethodsGetOutputOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersAuthMethodsGetOutputScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersAuthMethodsGetOutput:
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
    input_schema: Optional[ManagementInstanceProvidersAuthMethodsGetOutputInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersAuthMethodsGetOutputOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProvidersAuthMethodsGetOutputScopes]] = None


class mapManagementInstanceProvidersAuthMethodsGetOutputInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthMethodsGetOutputInputSchema:
        return ManagementInstanceProvidersAuthMethodsGetOutputInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthMethodsGetOutputInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersAuthMethodsGetOutputOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthMethodsGetOutputOutputSchema:
        return ManagementInstanceProvidersAuthMethodsGetOutputOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthMethodsGetOutputOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersAuthMethodsGetOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthMethodsGetOutputScopes:
        return ManagementInstanceProvidersAuthMethodsGetOutputScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthMethodsGetOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersAuthMethodsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersAuthMethodsGetOutput:
        return ManagementInstanceProvidersAuthMethodsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProvidersAuthMethodsGetOutputInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersAuthMethodsGetOutputOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProvidersAuthMethodsGetOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersAuthMethodsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

