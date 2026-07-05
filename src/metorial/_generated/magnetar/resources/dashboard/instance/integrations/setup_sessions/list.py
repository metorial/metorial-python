from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
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
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion
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
    config: Optional[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
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
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
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
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider
    integration_provider: DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputItems:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    integration_instance: DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListOutput:
    items: List[DashboardInstanceIntegrationsSetupSessionsListOutputItems]
    pagination: DashboardInstanceIntegrationsSetupSessionsListOutputPagination


class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders(
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
        provider=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputItems:
        return DashboardInstanceIntegrationsSetupSessionsListOutputItems(
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
        integration_instance=mapDashboardInstanceIntegrationsSetupSessionsListOutputItemsIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutputPagination:
        return DashboardInstanceIntegrationsSetupSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsSetupSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListOutput:
        return DashboardInstanceIntegrationsSetupSessionsListOutput(
        items=[mapDashboardInstanceIntegrationsSetupSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIntegrationsSetupSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationsSetupSessionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsSetupSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceIntegrationsSetupSessionsListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceIntegrationsSetupSessionsListQueryUpdatedAt] = None


class mapDashboardInstanceIntegrationsSetupSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsSetupSessionsListQuery:
        return DashboardInstanceIntegrationsSetupSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        created_at=mapDashboardInstanceIntegrationsSetupSessionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceIntegrationsSetupSessionsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsSetupSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

