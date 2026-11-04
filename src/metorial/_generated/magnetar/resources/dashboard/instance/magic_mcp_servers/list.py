from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment:
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
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod:
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
    input_schema: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema] = None
    output_schema: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes]] = None
    adapters: Optional[List[str]] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials:
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
class DashboardInstanceMagicMcpServersListOutputItemsProvidersConfig:
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
class DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig:
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
class DashboardInstanceMagicMcpServersListOutputItemsProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: DashboardInstanceMagicMcpServersListOutputItemsProvidersProvider
    deployment: DashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod] = None
    auth_credentials: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials] = None
    config: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersConfig] = None
    auth_config: Optional[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember:
    id: str
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember] = None
    consumer: Optional[DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItemsAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[DashboardInstanceMagicMcpServersListOutputItemsAccessOwner] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputItems:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[DashboardInstanceMagicMcpServersListOutputItemsEndpoints]
    providers: List[DashboardInstanceMagicMcpServersListOutputItemsProviders]
    metadata: Dict[str, Any]
    access: DashboardInstanceMagicMcpServersListOutputItemsAccess
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceMagicMcpServersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMagicMcpServersListOutput:
    items: List[DashboardInstanceMagicMcpServersListOutputItems]
    pagination: DashboardInstanceMagicMcpServersListOutputPagination


class mapDashboardInstanceMagicMcpServersListOutputItemsEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsEndpoints:
        return DashboardInstanceMagicMcpServersListOutputItemsEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersProvider:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        adapters=data.get('adapters', []),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersConfig:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersConfig(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig:
        return DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig(
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
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsProviders:
        return DashboardInstanceMagicMcpServersListOutputItemsProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceMagicMcpServersListOutputItemsProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember:
        return DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer:
        return DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsAccessOwner:
        return DashboardInstanceMagicMcpServersListOutputItemsAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItemsAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItemsAccess:
        return DashboardInstanceMagicMcpServersListOutputItemsAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapDashboardInstanceMagicMcpServersListOutputItemsAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItemsAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputItems:
        return DashboardInstanceMagicMcpServersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapDashboardInstanceMagicMcpServersListOutputItemsEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapDashboardInstanceMagicMcpServersListOutputItemsProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        access=mapDashboardInstanceMagicMcpServersListOutputItemsAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutputPagination:
        return DashboardInstanceMagicMcpServersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMagicMcpServersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListOutput:
        return DashboardInstanceMagicMcpServersListOutput(
        items=[mapDashboardInstanceMagicMcpServersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMagicMcpServersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMagicMcpServersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    ownership: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    magic_mcp_group_id: Optional[Union[str, List[str]]] = None
    provider_template_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    owner: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    consumer_id: Optional[Union[str, List[str]]] = None
    consumer_profile_id: Optional[Union[str, List[str]]] = None
    search: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    preconfigured_only: Optional[bool] = None


class mapDashboardInstanceMagicMcpServersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersListQuery:
        return DashboardInstanceMagicMcpServersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        ownership=data.get('ownership'),
        status=data.get('status'),
        magic_mcp_group_id=data.get('magic_mcp_group_id'),
        provider_template_id=data.get('provider_template_id'),
        integration_instance_id=data.get('integration_instance_id'),
        owner=data.get('owner'),
        provider_id=data.get('provider_id'),
        consumer_id=data.get('consumer_id'),
        consumer_profile_id=data.get('consumer_profile_id'),
        search=data.get('search'),
        id=data.get('id'),
        preconfigured_only=data.get('preconfigured_only')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMagicMcpServersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

