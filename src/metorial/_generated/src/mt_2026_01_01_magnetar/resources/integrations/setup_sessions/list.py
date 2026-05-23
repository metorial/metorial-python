from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
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
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion
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
    config: Optional[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
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
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
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
class IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider
    integration_provider: IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig] = None
    auth_config: Optional[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsListOutputItemsIntegrationInstance:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsListOutputItems:
    object: str
    id: str
    status: str
    url: str
    integration_id: str
    integration_instance: IntegrationsSetupSessionsListOutputItemsIntegrationInstance
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    redirect_url: Optional[str] = None
@dataclass
class IntegrationsSetupSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IntegrationsSetupSessionsListOutput:
    items: List[IntegrationsSetupSessionsListOutputItems]
    pagination: IntegrationsSetupSessionsListOutputPagination


class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig(
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
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders(
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
        provider=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItemsIntegrationInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItemsIntegrationInstance:
        return IntegrationsSetupSessionsListOutputItemsIntegrationInstance(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapIntegrationsSetupSessionsListOutputItemsIntegrationInstanceProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItemsIntegrationInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputItems:
        return IntegrationsSetupSessionsListOutputItems(
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
        integration_instance=mapIntegrationsSetupSessionsListOutputItemsIntegrationInstance.from_dict(data.get('integration_instance')) if data.get('integration_instance') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutputPagination:
        return IntegrationsSetupSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsSetupSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListOutput:
        return IntegrationsSetupSessionsListOutput(
        items=[mapIntegrationsSetupSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIntegrationsSetupSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsSetupSessionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsSetupSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[IntegrationsSetupSessionsListQueryCreatedAt] = None
    updated_at: Optional[IntegrationsSetupSessionsListQueryUpdatedAt] = None


class mapIntegrationsSetupSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsSetupSessionsListQuery:
        return IntegrationsSetupSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        created_at=mapIntegrationsSetupSessionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapIntegrationsSetupSessionsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsSetupSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

