from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersSpecificationsGetOutputToolsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsGetOutputToolsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsGetOutputToolsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ProvidersSpecificationsGetOutputTools:
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
    input_schema: Optional[ProvidersSpecificationsGetOutputToolsInputSchema] = None
    output_schema: Optional[ProvidersSpecificationsGetOutputToolsOutputSchema] = None
    tags: Optional[ProvidersSpecificationsGetOutputToolsTags] = None
@dataclass
class ProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsGetOutputAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProvidersSpecificationsGetOutputAuthMethods:
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
    input_schema: Optional[ProvidersSpecificationsGetOutputAuthMethodsInputSchema] = None
    output_schema: Optional[ProvidersSpecificationsGetOutputAuthMethodsOutputSchema] = None
    scopes: Optional[List[ProvidersSpecificationsGetOutputAuthMethodsScopes]] = None
@dataclass
class ProvidersSpecificationsGetOutput:
    object: str
    id: str
    key: str
    name: str
    config_schema: Dict[str, Any]
    config_visibility: str
    tools: List[ProvidersSpecificationsGetOutputTools]
    auth_methods: List[ProvidersSpecificationsGetOutputAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapProvidersSpecificationsGetOutputToolsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputToolsInputSchema:
        return ProvidersSpecificationsGetOutputToolsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputToolsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputToolsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputToolsOutputSchema:
        return ProvidersSpecificationsGetOutputToolsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputToolsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputToolsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputToolsTags:
        return ProvidersSpecificationsGetOutputToolsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputToolsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputTools:
        return ProvidersSpecificationsGetOutputTools(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapProvidersSpecificationsGetOutputToolsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersSpecificationsGetOutputToolsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapProvidersSpecificationsGetOutputToolsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputAuthMethodsInputSchema:
        return ProvidersSpecificationsGetOutputAuthMethodsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputAuthMethodsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
        return ProvidersSpecificationsGetOutputAuthMethodsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputAuthMethodsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputAuthMethodsScopes:
        return ProvidersSpecificationsGetOutputAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutputAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutputAuthMethods:
        return ProvidersSpecificationsGetOutputAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProvidersSpecificationsGetOutputAuthMethodsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersSpecificationsGetOutputAuthMethodsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProvidersSpecificationsGetOutputAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutputAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsGetOutput:
        return ProvidersSpecificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        config_visibility=data.get('config_visibility'),
        tools=[mapProvidersSpecificationsGetOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapProvidersSpecificationsGetOutputAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
