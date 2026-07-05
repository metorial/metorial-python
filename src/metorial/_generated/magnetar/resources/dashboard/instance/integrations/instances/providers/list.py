from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
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
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
    object: str
    id: str
    provider_version: DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion
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
    config: Optional[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig:
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
class DashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig:
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
class DashboardInstanceIntegrationsInstancesProvidersListOutputItems:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: DashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider
    integration_provider: DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig] = None
    auth_config: Optional[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListOutput:
    items: List[DashboardInstanceIntegrationsInstancesProvidersListOutputItems]
    pagination: DashboardInstanceIntegrationsInstancesProvidersListOutputPagination


class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig(
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
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputItems:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputItems(
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
        provider=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceIntegrationsInstancesProvidersListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutputPagination:
        return DashboardInstanceIntegrationsInstancesProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationsInstancesProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListOutput:
        return DashboardInstanceIntegrationsInstancesProvidersListOutput(
        items=[mapDashboardInstanceIntegrationsInstancesProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIntegrationsInstancesProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceIntegrationsInstancesProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    integration_instance_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    integration_provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    session_template_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceIntegrationsInstancesProvidersListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceIntegrationsInstancesProvidersListQueryUpdatedAt] = None


class mapDashboardInstanceIntegrationsInstancesProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationsInstancesProvidersListQuery:
        return DashboardInstanceIntegrationsInstancesProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        integration_id=data.get('integration_id'),
        integration_instance_id=data.get('integration_instance_id'),
        provider_id=data.get('provider_id'),
        integration_provider_id=data.get('integration_provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        session_template_id=data.get('session_template_id'),
        created_at=mapDashboardInstanceIntegrationsInstancesProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceIntegrationsInstancesProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationsInstancesProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

