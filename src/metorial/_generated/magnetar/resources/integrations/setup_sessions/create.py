from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
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
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion
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
    config: Optional[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
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
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
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
class IntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider
    integration_provider: IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsCreateOutputIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[IntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsCreateOutput:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    integration_instance: IntegrationsSetupSessionsCreateOutputIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None


class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders(
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
        provider=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutputIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutputIntegrationInstance:
        return IntegrationsSetupSessionsCreateOutputIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapIntegrationsSetupSessionsCreateOutputIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutputIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateOutput:
        return IntegrationsSetupSessionsCreateOutput(
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
        integration_instance=mapIntegrationsSetupSessionsCreateOutputIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    group_id: str
@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    collection_id: str
@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    category_id: str
@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
    groups: Optional[List[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups]] = None
    collections: Optional[List[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections]] = None
    categories: Optional[List[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories]] = None
@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
    enabled: Optional[bool] = None
@dataclass
class IntegrationsSetupSessionsCreateBodyConfigurationUi:
    layout: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsCreateBodyConfiguration:
    provider_search: Optional[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearch] = None
    tool_filters: Optional[IntegrationsSetupSessionsCreateBodyConfigurationToolFilters] = None
    ui: Optional[IntegrationsSetupSessionsCreateBodyConfigurationUi] = None
@dataclass
class IntegrationsSetupSessionsCreateBody:
    integration_id: str
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    expires_at: Optional[datetime] = None
    redirect_url: Optional[str] = None
    configuration: Optional[IntegrationsSetupSessionsCreateBodyConfiguration] = None


class mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
        return IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups(
        group_id=data.get('group_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
        return IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections(
        collection_id=data.get('collection_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
        return IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories(
        category_id=data.get('category_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationProviderSearch:
        return IntegrationsSetupSessionsCreateBodyConfigurationProviderSearch(
        groups=[mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchGroups.from_dict(item) for item in data.get('groups', []) if item],
        collections=[mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCollections.from_dict(item) for item in data.get('collections', []) if item],
        categories=[mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearchCategories.from_dict(item) for item in data.get('categories', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationProviderSearch, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationToolFilters:
        return IntegrationsSetupSessionsCreateBodyConfigurationToolFilters(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfigurationUi:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfigurationUi:
        return IntegrationsSetupSessionsCreateBodyConfigurationUi(
        layout=data.get('layout')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfigurationUi, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBodyConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBodyConfiguration:
        return IntegrationsSetupSessionsCreateBodyConfiguration(
        provider_search=mapIntegrationsSetupSessionsCreateBodyConfigurationProviderSearch.from_dict(data.get('provider_search')) if data.get('provider_search') else None,
        tool_filters=mapIntegrationsSetupSessionsCreateBodyConfigurationToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None,
        ui=mapIntegrationsSetupSessionsCreateBodyConfigurationUi.from_dict(data.get('ui')) if data.get('ui') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBodyConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsCreateBody:
        return IntegrationsSetupSessionsCreateBody(
        integration_id=data.get('integration_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        redirect_url=data.get('redirect_url'),
        configuration=mapIntegrationsSetupSessionsCreateBodyConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

