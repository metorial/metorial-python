from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsToolsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsTools:
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
    input_schema: Optional[ManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema] = None
    tags: Optional[ManagementInstanceProvidersSpecificationsListOutputItemsToolsTags] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
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
    input_schema: Optional[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema] = None
    output_schema: Optional[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes]] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputItems:
    object: str
    id: str
    key: str
    name: str
    config_schema: Dict[str, Any]
    config_visibility: str
    tools: List[ManagementInstanceProvidersSpecificationsListOutputItemsTools]
    auth_methods: List[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersSpecificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProvidersSpecificationsListOutput:
    items: List[ManagementInstanceProvidersSpecificationsListOutputItems]
    pagination: ManagementInstanceProvidersSpecificationsListOutputPagination


class mapManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema:
        return ManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema:
        return ManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsToolsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsToolsTags:
        return ManagementInstanceProvidersSpecificationsListOutputItemsToolsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsToolsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsTools:
        return ManagementInstanceProvidersSpecificationsListOutputItemsTools(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapManagementInstanceProvidersSpecificationsListOutputItemsToolsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersSpecificationsListOutputItemsToolsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapManagementInstanceProvidersSpecificationsListOutputItemsToolsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods:
        return ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputItems:
        return ManagementInstanceProvidersSpecificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        config_visibility=data.get('config_visibility'),
        tools=[mapManagementInstanceProvidersSpecificationsListOutputItemsTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapManagementInstanceProvidersSpecificationsListOutputItemsAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutputPagination:
        return ManagementInstanceProvidersSpecificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersSpecificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListOutput:
        return ManagementInstanceProvidersSpecificationsListOutput(
        items=[mapManagementInstanceProvidersSpecificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProvidersSpecificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProvidersSpecificationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_version_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceProvidersSpecificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersSpecificationsListQuery:
        return ManagementInstanceProvidersSpecificationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersSpecificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
