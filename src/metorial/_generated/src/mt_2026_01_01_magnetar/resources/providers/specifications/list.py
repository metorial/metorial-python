from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersSpecificationsListOutputItemsToolsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsListOutputItemsToolsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsListOutputItemsToolsTags:
    destructive: Optional[bool] = None
    read_only: Optional[bool] = None
@dataclass
class ProvidersSpecificationsListOutputItemsTools:
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
    input_schema: Optional[ProvidersSpecificationsListOutputItemsToolsInputSchema] = None
    output_schema: Optional[ProvidersSpecificationsListOutputItemsToolsOutputSchema] = None
    tags: Optional[ProvidersSpecificationsListOutputItemsToolsTags] = None
@dataclass
class ProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProvidersSpecificationsListOutputItemsAuthMethods:
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
    input_schema: Optional[ProvidersSpecificationsListOutputItemsAuthMethodsInputSchema] = None
    output_schema: Optional[ProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema] = None
    scopes: Optional[List[ProvidersSpecificationsListOutputItemsAuthMethodsScopes]] = None
@dataclass
class ProvidersSpecificationsListOutputItems:
    object: str
    id: str
    key: str
    name: str
    config_schema: Dict[str, Any]
    config_visibility: str
    tools: List[ProvidersSpecificationsListOutputItemsTools]
    auth_methods: List[ProvidersSpecificationsListOutputItemsAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProvidersSpecificationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProvidersSpecificationsListOutput:
    items: List[ProvidersSpecificationsListOutputItems]
    pagination: ProvidersSpecificationsListOutputPagination


class mapProvidersSpecificationsListOutputItemsToolsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsToolsInputSchema:
        return ProvidersSpecificationsListOutputItemsToolsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsToolsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsToolsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsToolsOutputSchema:
        return ProvidersSpecificationsListOutputItemsToolsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsToolsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsToolsTags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsToolsTags:
        return ProvidersSpecificationsListOutputItemsToolsTags(
        destructive=data.get('destructive'),
        read_only=data.get('read_only')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsToolsTags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsTools:
        return ProvidersSpecificationsListOutputItemsTools(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        constraints=data.get('constraints', []),
        instructions=data.get('instructions', []),
        input_schema=mapProvidersSpecificationsListOutputItemsToolsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersSpecificationsListOutputItemsToolsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        tags=mapProvidersSpecificationsListOutputItemsToolsTags.from_dict(data.get('tags')) if data.get('tags') else None,
        specification_id=data.get('specification_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethodsInputSchema:
        return ProvidersSpecificationsListOutputItemsAuthMethodsInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethodsInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema:
        return ProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethodsScopes:
        return ProvidersSpecificationsListOutputItemsAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItemsAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItemsAuthMethods:
        return ProvidersSpecificationsListOutputItemsAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProvidersSpecificationsListOutputItemsAuthMethodsInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProvidersSpecificationsListOutputItemsAuthMethodsOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProvidersSpecificationsListOutputItemsAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItemsAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputItems:
        return ProvidersSpecificationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        config_visibility=data.get('config_visibility'),
        tools=[mapProvidersSpecificationsListOutputItemsTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapProvidersSpecificationsListOutputItemsAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutputPagination:
        return ProvidersSpecificationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersSpecificationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListOutput:
        return ProvidersSpecificationsListOutput(
        items=[mapProvidersSpecificationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProvidersSpecificationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersSpecificationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersSpecificationsListQuery:
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


class mapProvidersSpecificationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersSpecificationsListQuery:
        return ProvidersSpecificationsListQuery(
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
    def to_dict(value: Union[ProvidersSpecificationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
