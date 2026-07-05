from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutputImplementation:
    type: str
    magic_mcp_server_id: str
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
    object: str
    id: str
    index: float
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
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
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
    object: str
    id: str
    provider_version: ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion
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
    config: Optional[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig:
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
class ManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig:
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
class ManagementInstanceIntegrationsInstancesUpdateOutputProviders:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    integration_instance_id: str
    is_override_tool_filter: bool
    provider: ManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider
    integration_provider: ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tool_filter: Optional[Dict[str, Any]] = None
    config: Optional[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig] = None
    auth_config: Optional[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    integration_id: str
    providers: List[ManagementInstanceIntegrationsInstancesUpdateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    implementation: Optional[ManagementInstanceIntegrationsInstancesUpdateOutputImplementation] = None
    archived_at: Optional[datetime] = None


class mapManagementInstanceIntegrationsInstancesUpdateOutputImplementation:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputImplementation:
        return ManagementInstanceIntegrationsInstancesUpdateOutputImplementation(
        type=data.get('type'),
        magic_mcp_server_id=data.get('magic_mcp_server_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputImplementation, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        index=data.get('index')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider(
        object=data.get('object'),
        id=data.get('id'),
        provider_version=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderProviderVersion.from_dict(data.get('provider_version')) if data.get('provider_version') else None,
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        deployment_id=data.get('deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        auth_credentials_id=data.get('auth_credentials_id'),
        config=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProviderConfig.from_dict(data.get('config')) if data.get('config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig(
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
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutputProviders:
        return ManagementInstanceIntegrationsInstancesUpdateOutputProviders(
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
        provider=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        integration_provider=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersIntegrationProvider.from_dict(data.get('integration_provider')) if data.get('integration_provider') else None,
        config=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapManagementInstanceIntegrationsInstancesUpdateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateOutput:
        return ManagementInstanceIntegrationsInstancesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        integration_id=data.get('integration_id'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        implementation=mapManagementInstanceIntegrationsInstancesUpdateOutputImplementation.from_dict(data.get('implementation')) if data.get('implementation') else None,
        providers=[mapManagementInstanceIntegrationsInstancesUpdateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationsInstancesUpdateBodyProviders:
    provider_id: str
    provider_config_id: Optional[str] = None
    provider_auth_config_id: Optional[str] = None
    tool_filters: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    is_override_tool_filter: Optional[bool] = None
@dataclass
class ManagementInstanceIntegrationsInstancesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    identity_actor_id: Optional[str] = None
    identity_id: Optional[str] = None
    providers: Optional[List[ManagementInstanceIntegrationsInstancesUpdateBodyProviders]] = None


class mapManagementInstanceIntegrationsInstancesUpdateBodyProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateBodyProviders:
        return ManagementInstanceIntegrationsInstancesUpdateBodyProviders(
        provider_id=data.get('provider_id'),
        provider_config_id=data.get('provider_config_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        tool_filters=data.get('tool_filters'),
        is_override_tool_filter=data.get('is_override_tool_filter')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateBodyProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationsInstancesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationsInstancesUpdateBody:
        return ManagementInstanceIntegrationsInstancesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        identity_actor_id=data.get('identity_actor_id'),
        identity_id=data.get('identity_id'),
        providers=[mapManagementInstanceIntegrationsInstancesUpdateBodyProviders.from_dict(item) for item in data.get('providers', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationsInstancesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

