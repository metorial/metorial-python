from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
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
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion
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
    config: Optional[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
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
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
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
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider
    integration_provider: ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateOutput:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    integration_instance: ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders(
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
        provider=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateOutput:
        return ManagementInstanceIntegrationsSetupSessionsCreateOutput(
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
        integration_instance=mapManagementInstanceIntegrationsSetupSessionsCreateOutputIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    group_id: str
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    collection_id: str
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    category_id: str
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
    groups: Optional[List[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups]] = None
    collections: Optional[List[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections]] = None
    categories: Optional[List[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories]] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
    enabled: Optional[bool] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi:
    layout: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration:
    provider_search: Optional[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch] = None
    tool_filters: Optional[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters] = None
    ui: Optional[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi] = None
@dataclass
class ManagementInstanceIntegrationsSetupSessionsCreateBody:
    integration_id: str
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    expires_at: Optional[datetime] = None
    redirect_url: Optional[str] = None
    configuration: Optional[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration] = None


class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups(
        group_id=data.get('group_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections(
        collection_id=data.get('collection_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories(
        category_id=data.get('category_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch(
        groups=[mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups.from_dict(item) for item in data.get('groups', []) if item],
        collections=[mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections.from_dict(item) for item in data.get('collections', []) if item],
        categories=[mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories.from_dict(item) for item in data.get('categories', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi(
        layout=data.get('layout')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration:
        return ManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration(
        provider_search=mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch.from_dict(data.get('provider_search')) if data.get('provider_search') else None,
        tool_filters=mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None,
        ui=mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfigurationUi.from_dict(data.get('ui')) if data.get('ui') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsSetupSessionsCreateBody:
        return ManagementInstanceIntegrationsSetupSessionsCreateBody(
        integration_id=data.get('integration_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        redirect_url=data.get('redirect_url'),
        configuration=mapManagementInstanceIntegrationsSetupSessionsCreateBodyConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

