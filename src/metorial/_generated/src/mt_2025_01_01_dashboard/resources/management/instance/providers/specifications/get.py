from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputToolsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputTools:
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
    input_schema: Optional[ManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema] = None
    tags: Optional[ManagementInstanceProvidersSpecificationsGetOutputToolsTags] = None
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutputAuthMethods:
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
    input_schema: Optional[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes]] = None
@dataclass
class ManagementInstanceProvidersSpecificationsGetOutput:
    object: str
    id: str
    key: str
    name: str
    config_schema: Dict[str, Any]
    config_visibility: str
    tools: List[ManagementInstanceProvidersSpecificationsGetOutputTools]
    auth_methods: List[ManagementInstanceProvidersSpecificationsGetOutputAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema:
        return ManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
        return ManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputToolsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputToolsTags:
        return ManagementInstanceProvidersSpecificationsGetOutputToolsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputToolsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputTools:
        return ManagementInstanceProvidersSpecificationsGetOutputTools(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceProvidersSpecificationsGetOutputToolsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersSpecificationsGetOutputToolsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceProvidersSpecificationsGetOutputToolsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
        return ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
        return ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
        return ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutputAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutputAuthMethods:
        return ManagementInstanceProvidersSpecificationsGetOutputAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProvidersSpecificationsGetOutputAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutputAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsGetOutput:
        return ManagementInstanceProvidersSpecificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        config_visibility=data.get('config_visibility'),
        tools=[mapManagementInstanceProvidersSpecificationsGetOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapManagementInstanceProvidersSpecificationsGetOutputAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
