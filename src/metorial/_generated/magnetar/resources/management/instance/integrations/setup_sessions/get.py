from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
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
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion
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
    config: Optional[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
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
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
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
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider
    integration_provider: ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsGetOutput:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    integration_instance: ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders(
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
        provider=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance:
        return ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsGetOutput:
        return ManagementInstanceIntegrationsSetupSessionsGetOutput(
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
        integration_instance=mapManagementInstanceIntegrationsSetupSessionsGetOutputIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

