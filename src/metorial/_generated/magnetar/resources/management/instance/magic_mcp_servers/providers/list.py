from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod:
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
    input_schema: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes]] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials:
    object: str
    id: str
    type: str
    status: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    scopes: Optional[List[str]] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputItems:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: ManagementInstanceMagicMcpServersProvidersListOutputItemsProvider
    deployment: ManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod] = None
    auth_credentials: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials] = None
    config: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsConfig] = None
    auth_config: Optional[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceMagicMcpServersProvidersListOutput:
    items: List[ManagementInstanceMagicMcpServersProvidersListOutputItems]
    pagination: ManagementInstanceMagicMcpServersProvidersListOutputPagination


class mapManagementInstanceMagicMcpServersProvidersListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsProvider:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        is_managed=data.get('is_managed'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        scopes=data.get('scopes', []),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsConfig:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig:
        return ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputItems:
        return ManagementInstanceMagicMcpServersProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapManagementInstanceMagicMcpServersProvidersListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapManagementInstanceMagicMcpServersProvidersListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapManagementInstanceMagicMcpServersProvidersListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceMagicMcpServersProvidersListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutputPagination:
        return ManagementInstanceMagicMcpServersProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpServersProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListOutput:
        return ManagementInstanceMagicMcpServersProvidersListOutput(
        items=[mapManagementInstanceMagicMcpServersProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceMagicMcpServersProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpServersProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceMagicMcpServersProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    integration_instance_provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceMagicMcpServersProvidersListQueryCreatedAt] = None
    updated_at: Optional[ManagementInstanceMagicMcpServersProvidersListQueryUpdatedAt] = None


class mapManagementInstanceMagicMcpServersProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersProvidersListQuery:
        return ManagementInstanceMagicMcpServersProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        integration_provider_id=data.get('integration_provider_id'),
        integration_instance_provider_id=data.get('integration_instance_provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        created_at=mapManagementInstanceMagicMcpServersProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapManagementInstanceMagicMcpServersProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpServersProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

