from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersDeployOutputEndpoints:
    id: str
    alias: str
    url: str
@dataclass
class ConsumerProvidersDeployOutputProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ConsumerProvidersDeployOutputProvidersDeployment:
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
class ConsumerProvidersDeployOutputProvidersAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersDeployOutputProvidersAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ConsumerProvidersDeployOutputProvidersAuthMethod:
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
    input_schema: Optional[ConsumerProvidersDeployOutputProvidersAuthMethodInputSchema] = None
    output_schema: Optional[ConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema] = None
    scopes: Optional[List[ConsumerProvidersDeployOutputProvidersAuthMethodScopes]] = None
    adapters: Optional[List[str]] = None
@dataclass
class ConsumerProvidersDeployOutputProvidersAuthCredentials:
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
class ConsumerProvidersDeployOutputProvidersConfig:
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
class ConsumerProvidersDeployOutputProvidersAuthConfig:
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
class ConsumerProvidersDeployOutputProviders:
    object: str
    id: str
    status: str
    magic_mcp_server_id: str
    provider_management_mode: str
    name: str
    provider: ConsumerProvidersDeployOutputProvidersProvider
    deployment: ConsumerProvidersDeployOutputProvidersDeployment
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method: Optional[ConsumerProvidersDeployOutputProvidersAuthMethod] = None
    auth_credentials: Optional[ConsumerProvidersDeployOutputProvidersAuthCredentials] = None
    config: Optional[ConsumerProvidersDeployOutputProvidersConfig] = None
    auth_config: Optional[ConsumerProvidersDeployOutputProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ConsumerProvidersDeployOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class ConsumerProvidersDeployOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class ConsumerProvidersDeployOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[ConsumerProvidersDeployOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[ConsumerProvidersDeployOutputAccessOwnerConsumer] = None
@dataclass
class ConsumerProvidersDeployOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[ConsumerProvidersDeployOutputAccessOwner] = None
@dataclass
class ConsumerProvidersDeployOutput:
    object: str
    id: str
    status: str
    source: str
    provider_management_mode: str
    endpoints: List[ConsumerProvidersDeployOutputEndpoints]
    providers: List[ConsumerProvidersDeployOutputProviders]
    metadata: Dict[str, Any]
    access: ConsumerProvidersDeployOutputAccess
    created_at: datetime
    updated_at: datetime
    provider_template_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class mapConsumerProvidersDeployOutputEndpoints:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputEndpoints:
        return ConsumerProvidersDeployOutputEndpoints(
        id=data.get('id'),
        alias=data.get('alias'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputEndpoints, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersProvider:
        return ConsumerProvidersDeployOutputProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersDeployment:
        return ConsumerProvidersDeployOutputProvidersDeployment(
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
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthMethodInputSchema:
        return ConsumerProvidersDeployOutputProvidersAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema:
        return ConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthMethodScopes:
        return ConsumerProvidersDeployOutputProvidersAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthMethod:
        return ConsumerProvidersDeployOutputProvidersAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapConsumerProvidersDeployOutputProvidersAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerProvidersDeployOutputProvidersAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapConsumerProvidersDeployOutputProvidersAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        adapters=data.get('adapters', []),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthCredentials:
        return ConsumerProvidersDeployOutputProvidersAuthCredentials(
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
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersConfig:
        return ConsumerProvidersDeployOutputProvidersConfig(
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
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProvidersAuthConfig:
        return ConsumerProvidersDeployOutputProvidersAuthConfig(
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
    def to_dict(value: Union[ConsumerProvidersDeployOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputProviders:
        return ConsumerProvidersDeployOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        magic_mcp_server_id=data.get('magic_mcp_server_id'),
        provider_management_mode=data.get('provider_management_mode'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider=mapConsumerProvidersDeployOutputProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        deployment=mapConsumerProvidersDeployOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        auth_method=mapConsumerProvidersDeployOutputProvidersAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        auth_credentials=mapConsumerProvidersDeployOutputProvidersAuthCredentials.from_dict(data.get('auth_credentials')) if data.get('auth_credentials') else None,
        config=mapConsumerProvidersDeployOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapConsumerProvidersDeployOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputAccessOwnerOrganizationMember:
        return ConsumerProvidersDeployOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputAccessOwnerConsumer:
        return ConsumerProvidersDeployOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputAccessOwner:
        return ConsumerProvidersDeployOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapConsumerProvidersDeployOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapConsumerProvidersDeployOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutputAccess:
        return ConsumerProvidersDeployOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapConsumerProvidersDeployOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersDeployOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployOutput:
        return ConsumerProvidersDeployOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        source=data.get('source'),
        provider_management_mode=data.get('provider_management_mode'),
        endpoints=[mapConsumerProvidersDeployOutputEndpoints.from_dict(item) for item in data.get('endpoints', []) if item],
        provider_template_id=data.get('provider_template_id'),
        providers=[mapConsumerProvidersDeployOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        access=mapConsumerProvidersDeployOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerProvidersDeployBody:
    integration_setup_session_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapConsumerProvidersDeployBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersDeployBody:
        return ConsumerProvidersDeployBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_setup_session_id=data.get('integration_setup_session_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersDeployBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

