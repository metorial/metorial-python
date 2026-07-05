from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IntegrationsInstancesUpdateOutputImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class IntegrationsInstancesUpdateOutputProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class IntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class IntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
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
class IntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: IntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion
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
    config: Optional[IntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsInstancesUpdateOutputProvidersConfig:
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
class IntegrationsInstancesUpdateOutputProvidersAuthConfig:
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
class IntegrationsInstancesUpdateOutputProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: IntegrationsInstancesUpdateOutputProvidersProvider
    integration_provider: IntegrationsInstancesUpdateOutputProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[IntegrationsInstancesUpdateOutputProvidersConfig] = None
    auth_config: Optional[IntegrationsInstancesUpdateOutputProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class IntegrationsInstancesUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[IntegrationsInstancesUpdateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[IntegrationsInstancesUpdateOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapIntegrationsInstancesUpdateOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputImplementation:
        return IntegrationsInstancesUpdateOutputImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersProvider:
        return IntegrationsInstancesUpdateOutputProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
        return IntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
        return IntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
        return IntegrationsInstancesUpdateOutputProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersConfig:
        return IntegrationsInstancesUpdateOutputProvidersConfig(
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
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProvidersAuthConfig:
        return IntegrationsInstancesUpdateOutputProvidersAuthConfig(
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
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutputProviders:
        return IntegrationsInstancesUpdateOutputProviders(
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
        provider=mapIntegrationsInstancesUpdateOutputProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapIntegrationsInstancesUpdateOutputProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapIntegrationsInstancesUpdateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapIntegrationsInstancesUpdateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateOutput:
        return IntegrationsInstancesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapIntegrationsInstancesUpdateOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapIntegrationsInstancesUpdateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class IntegrationsInstancesUpdateBodyProviders:
    provider_id: str
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    is_override_tool_filter: Optional[bool] = None
@dataclass
class IntegrationsInstancesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    providers: Optional[List[IntegrationsInstancesUpdateBodyProviders]] = None


class mapIntegrationsInstancesUpdateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateBodyProviders:
        return IntegrationsInstancesUpdateBodyProviders(
        provider_id=data.get('provider_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        tool_filters=data.get('tool_filters'),
        is_override_tool_filter=data.get('is_override_tool_filter')
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapIntegrationsInstancesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IntegrationsInstancesUpdateBody:
        return IntegrationsInstancesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        providers=[mapIntegrationsInstancesUpdateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[IntegrationsInstancesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

