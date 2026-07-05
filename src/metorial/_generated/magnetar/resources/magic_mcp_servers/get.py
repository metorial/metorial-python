from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MagicMcpServersGetOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class MagicMcpServersGetOutputProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MagicMcpServersGetOutputProvidersDeployment:
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
class MagicMcpServersGetOutputProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpServersGetOutputProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class MagicMcpServersGetOutputProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class MagicMcpServersGetOutputProvidersAuthMethod:
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
    input_schema: Optional[MagicMcpServersGetOutputProvidersAuthMethodInputSchema] = None
    output_schema: Optional[MagicMcpServersGetOutputProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[MagicMcpServersGetOutputProvidersAuthMethodScopes]] = None
@dataclass
class MagicMcpServersGetOutputProvidersAuthCredentials:
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
class MagicMcpServersGetOutputProvidersConfig:
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
class MagicMcpServersGetOutputProvidersAuthConfig:
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
class MagicMcpServersGetOutputProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: MagicMcpServersGetOutputProvidersProvider
    deployment: MagicMcpServersGetOutputProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[MagicMcpServersGetOutputProvidersAuthMethod] = None
    auth_credentials: Optional[MagicMcpServersGetOutputProvidersAuthCredentials] = None
    config: Optional[MagicMcpServersGetOutputProvidersConfig] = None
    auth_config: Optional[MagicMcpServersGetOutputProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class MagicMcpServersGetOutput:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[MagicMcpServersGetOutputEndpoints]
    providers: List[MagicMcpServersGetOutputProviders]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class mapMagicMcpServersGetOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputEndpoints:
        return MagicMcpServersGetOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersProvider:
        return MagicMcpServersGetOutputProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersDeployment:
        return MagicMcpServersGetOutputProvidersDeployment(
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
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthMethodInputSchema:
        return MagicMcpServersGetOutputProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthMethodOutputSchema:
        return MagicMcpServersGetOutputProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthMethodScopes:
        return MagicMcpServersGetOutputProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthMethod:
        return MagicMcpServersGetOutputProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapMagicMcpServersGetOutputProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapMagicMcpServersGetOutputProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapMagicMcpServersGetOutputProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthCredentials:
        return MagicMcpServersGetOutputProvidersAuthCredentials(
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
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersConfig:
        return MagicMcpServersGetOutputProvidersConfig(
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
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProvidersAuthConfig:
        return MagicMcpServersGetOutputProvidersAuthConfig(
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
    def to_dict(value: Union[MagicMcpServersGetOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputProviders:
        return MagicMcpServersGetOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapMagicMcpServersGetOutputProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapMagicMcpServersGetOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapMagicMcpServersGetOutputProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapMagicMcpServersGetOutputProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapMagicMcpServersGetOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapMagicMcpServersGetOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMagicMcpServersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutput:
        return MagicMcpServersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapMagicMcpServersGetOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapMagicMcpServersGetOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MagicMcpServersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

