from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersReconnectOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ConsumerProvidersReconnectOutputProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ConsumerProvidersReconnectOutputProvidersDeployment:
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
class ConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersReconnectOutputProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ConsumerProvidersReconnectOutputProvidersAuthMethod:
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
    input_schema: Optional[ConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema] = None
    output_schema: Optional[ConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[ConsumerProvidersReconnectOutputProvidersAuthMethodScopes]] = None
    adapters: Optional[List[str]] = None
@dataclass
class ConsumerProvidersReconnectOutputProvidersAuthCredentials:
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
class ConsumerProvidersReconnectOutputProvidersConfig:
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
class ConsumerProvidersReconnectOutputProvidersAuthConfig:
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
class ConsumerProvidersReconnectOutputProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: ConsumerProvidersReconnectOutputProvidersProvider
    deployment: ConsumerProvidersReconnectOutputProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[ConsumerProvidersReconnectOutputProvidersAuthMethod] = None
    auth_credentials: Optional[ConsumerProvidersReconnectOutputProvidersAuthCredentials] = None
    config: Optional[ConsumerProvidersReconnectOutputProvidersConfig] = None
    auth_config: Optional[ConsumerProvidersReconnectOutputProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ConsumerProvidersReconnectOutputOwnerActor:
    id: str
    type: str
    consumer_id: Optional[str] = None
@dataclass
class ConsumerProvidersReconnectOutput:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[ConsumerProvidersReconnectOutputEndpoints]
    providers: List[ConsumerProvidersReconnectOutputProviders]
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    owner_actor: Optional[ConsumerProvidersReconnectOutputOwnerActor] = None


class mapConsumerProvidersReconnectOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputEndpoints:
        return ConsumerProvidersReconnectOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersProvider:
        return ConsumerProvidersReconnectOutputProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersDeployment:
        return ConsumerProvidersReconnectOutputProvidersDeployment(
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
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema:
        return ConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema:
        return ConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthMethodScopes:
        return ConsumerProvidersReconnectOutputProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthMethod:
        return ConsumerProvidersReconnectOutputProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapConsumerProvidersReconnectOutputProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerProvidersReconnectOutputProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapConsumerProvidersReconnectOutputProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        adapters=data.get('adapters', []),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthCredentials:
        return ConsumerProvidersReconnectOutputProvidersAuthCredentials(
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
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersConfig:
        return ConsumerProvidersReconnectOutputProvidersConfig(
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
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProvidersAuthConfig:
        return ConsumerProvidersReconnectOutputProvidersAuthConfig(
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
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputProviders:
        return ConsumerProvidersReconnectOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapConsumerProvidersReconnectOutputProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapConsumerProvidersReconnectOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapConsumerProvidersReconnectOutputProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapConsumerProvidersReconnectOutputProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapConsumerProvidersReconnectOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapConsumerProvidersReconnectOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutputOwnerActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutputOwnerActor:
        return ConsumerProvidersReconnectOutputOwnerActor(
        id=data.get('id'),
        type=data.get('type'),
        consumer_id=data.get('consumer_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutputOwnerActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersReconnectOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectOutput:
        return ConsumerProvidersReconnectOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapConsumerProvidersReconnectOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapConsumerProvidersReconnectOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        owner_actor=mapConsumerProvidersReconnectOutputOwnerActor.from_dict(data.get('owner_actor')) if data.get('owner_actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersReconnectBody:
    magic_mcp_server_id: str
    integration_setup_session_id: str


class mapConsumerProvidersReconnectBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersReconnectBody:
        return ConsumerProvidersReconnectBody(
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        integration_setup_session_id=data.get('integration_setup_session_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersReconnectBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

