from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember:
    id: str
@dataclass
class IntegrationsSetupSessionsGetOutputAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsGetOutputAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[IntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember] = None
    consumer: Optional[IntegrationsSetupSessionsGetOutputAccessOwnerConsumer] = None
@dataclass
class IntegrationsSetupSessionsGetOutputAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[IntegrationsSetupSessionsGetOutputAccessOwner] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember:
    id: str
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer:
    id: str
    profile_id: str
    portal_id: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner:
    type: str
    name: Optional[str] = None
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_member: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember] = None
    consumer: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceAccess:
    type: str
    visibility: str
    source: Optional[str] = None
    owner: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
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
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion
    status: str
    name: str
    provider_id: str
    deployment_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    auth_method_id: Optional[str] = None
    auth_credentials_id: Optional[str] = None
    config: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
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
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
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
class IntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider
    integration_provider: IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig] = None
    callback_instance_id: Optional[str] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsGetOutputIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    access: IntegrationsSetupSessionsGetOutputIntegrationInstanceAccess
    providers: List[IntegrationsSetupSessionsGetOutputIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[IntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsGetOutput:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    access: IntegrationsSetupSessionsGetOutputAccess
    integration_instance: IntegrationsSetupSessionsGetOutputIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None


class mapIntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember:
        return IntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputAccessOwnerConsumer:
        return IntegrationsSetupSessionsGetOutputAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputAccessOwner:
        return IntegrationsSetupSessionsGetOutputAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapIntegrationsSetupSessionsGetOutputAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapIntegrationsSetupSessionsGetOutputAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputAccess:
        return IntegrationsSetupSessionsGetOutputAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapIntegrationsSetupSessionsGetOutputAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember(
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer(
        id=data.get('id'),
        profile_id=data.get('profile_id'),
        portal_id=data.get('portal_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_member=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerOrganizationMember.from_dict(data.get('organization_member')) if data.get('organization_member') else None,
        consumer=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwnerConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceAccess:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceAccess(
        source=data.get('source'),
        type=data.get('type'),
        visibility=data.get('visibility'),
        owner=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccessOwner.from_dict(data.get('owner')) if data.get('owner') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
        return IntegrationsSetupSessionsGetOutputIntegrationInstanceProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        tool_filter=data.get('tool_filter'),
        is_override_tool_filter=data.get('is_override_tool_filter'),
        provider=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        callback_instance_id=data.get('callback_instance_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutputIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutputIntegrationInstance:
        return IntegrationsSetupSessionsGetOutputIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        access=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceAccess.from_dict(data.get('access')) if data.get('access') else None,
        implementation=mapIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutputIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsGetOutput:
        return IntegrationsSetupSessionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        url=data.get('url'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=data.get('configuration'),
        redirect_url=data.get('redirect_url'),
        integration_id=data.get('integration_id'),
        access=mapIntegrationsSetupSessionsGetOutputAccess.from_dict(data.get('access')) if data.get('access') else None,
        integration_instance=mapIntegrationsSetupSessionsGetOutputIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

