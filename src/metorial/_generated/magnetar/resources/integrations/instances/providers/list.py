from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstancesProvidersListOutputItemsProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class IntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class IntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
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
class IntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
    object: str
    id: str
    provider_version: IntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion
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
    config: Optional[IntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsInstancesProvidersListOutputItemsConfig:
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
class IntegrationsInstancesProvidersListOutputItemsAuthConfig:
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
class IntegrationsInstancesProvidersListOutputItems:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: IntegrationsInstancesProvidersListOutputItemsProvider
    integration_provider: IntegrationsInstancesProvidersListOutputItemsIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[IntegrationsInstancesProvidersListOutputItemsConfig] = None
    auth_config: Optional[IntegrationsInstancesProvidersListOutputItemsAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsInstancesProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class IntegrationsInstancesProvidersListOutput:
    items: List[IntegrationsInstancesProvidersListOutputItems]
    pagination: IntegrationsInstancesProvidersListOutputPagination


class mapIntegrationsInstancesProvidersListOutputItemsProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsProvider:
        return IntegrationsInstancesProvidersListOutputItemsProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion:
        return IntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig:
        return IntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig(
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
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsIntegrationProvider:
        return IntegrationsInstancesProvidersListOutputItemsIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapIntegrationsInstancesProvidersListOutputItemsIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsInstancesProvidersListOutputItemsIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsConfig:
        return IntegrationsInstancesProvidersListOutputItemsConfig(
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
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItemsAuthConfig:
        return IntegrationsInstancesProvidersListOutputItemsAuthConfig(
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
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputItems:
        return IntegrationsInstancesProvidersListOutputItems(
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
        provider=mapIntegrationsInstancesProvidersListOutputItemsProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapIntegrationsInstancesProvidersListOutputItemsIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapIntegrationsInstancesProvidersListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstancesProvidersListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutputPagination:
        return IntegrationsInstancesProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListOutput:
        return IntegrationsInstancesProvidersListOutput(
        items=[mapIntegrationsInstancesProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapIntegrationsInstancesProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstancesProvidersListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsInstancesProvidersListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class IntegrationsInstancesProvidersListQuery:
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
    created_at: Optional[IntegrationsInstancesProvidersListQueryCreatedAt] = None
    updated_at: Optional[IntegrationsInstancesProvidersListQueryUpdatedAt] = None


class mapIntegrationsInstancesProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesProvidersListQuery:
        return IntegrationsInstancesProvidersListQuery(
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
        created_at=mapIntegrationsInstancesProvidersListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapIntegrationsInstancesProvidersListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

