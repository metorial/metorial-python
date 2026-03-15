from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputToolsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputTools:
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
    input_schema: Optional[DashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema] = None
    output_schema: Optional[DashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema] = None
    tags: Optional[DashboardInstanceProvidersSpecificationsGetOutputToolsTags] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
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
    input_schema: Optional[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema] = None
    output_schema: Optional[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema] = None
    scopes: Optional[List[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes]] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutput:
    object: str
    id: str
    key: str
    name: str
    config_schema: Dict[str, Any]
    config_visibility: str
    tools: List[DashboardInstanceProvidersSpecificationsGetOutputTools]
    auth_methods: List[DashboardInstanceProvidersSpecificationsGetOutputAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema:
        return DashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema:
        return DashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputToolsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputToolsTags:
        return DashboardInstanceProvidersSpecificationsGetOutputToolsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputToolsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputTools:
        return DashboardInstanceProvidersSpecificationsGetOutputTools(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapDashboardInstanceProvidersSpecificationsGetOutputToolsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProvidersSpecificationsGetOutputToolsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapDashboardInstanceProvidersSpecificationsGetOutputToolsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutput:
        return DashboardInstanceProvidersSpecificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        config_visibility=data.get('config_visibility'),
        tools=[mapDashboardInstanceProvidersSpecificationsGetOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

