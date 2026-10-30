from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
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
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
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
    input_schema: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema] = None
    output_schema: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes]] = None
    adapters: Optional[List[str]] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
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
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
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
class MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
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
class MagicMcpSessionsListOutputItemsMagicMcpServerProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: MagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider
    deployment: MagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod] = None
    auth_credentials: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials] = None
    config: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig] = None
    auth_config: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember:
    id: str
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember] = None
    consumer: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServerAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints]
    providers: List[MagicMcpSessionsListOutputItemsMagicMcpServerProviders]
    metadata: Dict[str, Any]
    access: MagicMcpSessionsListOutputItemsMagicMcpServerAccess
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember:
    id: str
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember] = None
    consumer: Optional[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpEndpointAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner] = None
@dataclass
class MagicMcpSessionsListOutputItemsMagicMcpEndpoint:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    enable_skill_editing: bool
    access: MagicMcpSessionsListOutputItemsMagicMcpEndpointAccess
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class MagicMcpSessionsListOutputItems:
    object: str
    id: str
    consumer_integration_ids: List[str]
    session_id: str
    created_at: datetime
    updated_at: datetime
    magic_mcp_server: Optional[MagicMcpSessionsListOutputItemsMagicMcpServer] = None
    magic_mcp_endpoint: Optional[MagicMcpSessionsListOutputItemsMagicMcpEndpoint] = None
    consumer_profile_id: Optional[str] = None
    expires_at: Optional[datetime] = None
@dataclass
class MagicMcpSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MagicMcpSessionsListOutput:
    items: List[MagicMcpSessionsListOutputItems]
    pagination: MagicMcpSessionsListOutputPagination


class mapMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
        return MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment(
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
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        adapters=data.get('adapters', []),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials(
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
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig(
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
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig(
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
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerProviders:
        return MagicMcpSessionsListOutputItemsMagicMcpServerProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember:
        return MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer:
        return MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner:
        return MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServerAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServerAccess:
        return MagicMcpSessionsListOutputItemsMagicMcpServerAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapMagicMcpSessionsListOutputItemsMagicMcpServerAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServerAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpServer:
        return MagicMcpSessionsListOutputItemsMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapMagicMcpSessionsListOutputItemsMagicMcpServerProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        access=mapMagicMcpSessionsListOutputItemsMagicMcpServerAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember:
        return MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer:
        return MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner:
        return MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpEndpointAccess:
        return MagicMcpSessionsListOutputItemsMagicMcpEndpointAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpEndpointAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItemsMagicMcpEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItemsMagicMcpEndpoint:
        return MagicMcpSessionsListOutputItemsMagicMcpEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        enable_skill_editing=data.get('enable_skill_editing'),
        access=mapMagicMcpSessionsListOutputItemsMagicMcpEndpointAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItemsMagicMcpEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputItems:
        return MagicMcpSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        magic_mcp_server=mapMagicMcpSessionsListOutputItemsMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        magic_mcp_endpoint=mapMagicMcpSessionsListOutputItemsMagicMcpEndpoint.from_dict(data.get('magic_mcp_endpoint')) if data.get('magic_mcp_endpoint') else None,
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_integration_ids=data.get('consumer_integration_ids', []),
        session_id=data.get('session_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutputPagination:
        return MagicMcpSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListOutput:
        return MagicMcpSessionsListOutput(
        items=[mapMagicMcpSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMagicMcpSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MagicMcpSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapMagicMcpSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpSessionsListQuery:
        return MagicMcpSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

