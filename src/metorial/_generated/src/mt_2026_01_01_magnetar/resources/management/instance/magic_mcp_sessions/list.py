from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
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
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
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
    input_schema: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes]] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
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
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
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
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
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
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider
    deployment: ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod] = None
    auth_credentials: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials] = None
    config: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig] = None
    auth_config: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints]
    providers: List[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint:
    object: str
    id: str
    status: str
    slug: str
    url: str
    servers: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputItems:
    object: str
    id: str
    consumer_integration_ids: List[str]
    session_id: str
    created_at: datetime
    updated_at: datetime
    magic_mcp_server: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer] = None
    magic_mcp_endpoint: Optional[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint] = None
    consumer_profile_id: Optional[str] = None
    expires_at: Optional[datetime] = None
@dataclass
class ManagementInstanceMagicMcpSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceMagicMcpSessionsListOutput:
    items: List[ManagementInstanceMagicMcpSessionsListOutputItems]
    pagination: ManagementInstanceMagicMcpSessionsListOutputPagination


class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServerProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint:
        return ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        url=data.get('url'),
        servers=data.get('servers', []),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputItems:
        return ManagementInstanceMagicMcpSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        magic_mcp_server=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpServer.from_dict(data.get('magic_mcp_server')) if data.get('magic_mcp_server') else None,
        magic_mcp_endpoint=mapManagementInstanceMagicMcpSessionsListOutputItemsMagicMcpEndpoint.from_dict(data.get('magic_mcp_endpoint')) if data.get('magic_mcp_endpoint') else None,
        consumer_profile_id=data.get('consumer_profile_id'),
        consumer_integration_ids=data.get('consumer_integration_ids', []),
        session_id=data.get('session_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutputPagination:
        return ManagementInstanceMagicMcpSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMagicMcpSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListOutput:
        return ManagementInstanceMagicMcpSessionsListOutput(
        items=[mapManagementInstanceMagicMcpSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceMagicMcpSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMagicMcpSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    magic_mcp_server_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceMagicMcpSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpSessionsListQuery:
        return ManagementInstanceMagicMcpSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMagicMcpSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

