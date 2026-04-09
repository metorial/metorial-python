from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthMethod:
    object: str
    id: str
    type: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsDeployment:
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
class ProviderDeploymentsSetupSessionsListOutputItemsCredentials:
    object: str
    id: str
    type: str
    status: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment:
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
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials:
    object: str
    id: str
    type: str
    status: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod:
    object: str
    id: str
    type: str
    key: str
    name: str
    capabilities: Dict[str, Any]
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment:
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
class ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment:
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
class ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault:
    object: str
    id: str
    status: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsConfig:
    object: str
    id: str
    status: str
    is_default: bool
    tool_filter: Dict[str, Any]
    provider_id: str
    specification_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment] = None
    from_vault: Optional[ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItems:
    object: str
    id: str
    type: str
    status: str
    url: str
    ui_mode: str
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    configuration: Optional[Dict[str, Any]] = None
    provider_id: Optional[str] = None
    identity_id: Optional[str] = None
    identity_credential_id: Optional[str] = None
    auth_method: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethod] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsListOutputItemsDeployment] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsListOutputItemsCredentials] = None
    auth_config: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig] = None
    config: Optional[ProviderDeploymentsSetupSessionsListOutputItemsConfig] = None
    redirect_url: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsSetupSessionsListOutput:
    items: List[ProviderDeploymentsSetupSessionsListOutputItems]
    pagination: ProviderDeploymentsSetupSessionsListOutputPagination


class mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthMethod:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsDeployment:
        return ProviderDeploymentsSetupSessionsListOutputItemsDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsCredentials:
        return ProviderDeploymentsSetupSessionsListOutputItemsCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        is_managed=data.get('is_managed'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        is_managed=data.get('is_managed'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source=data.get('source'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        provider_id=data.get('provider_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        deployment=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment:
        return ProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment:
        return ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault:
        return ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapProviderDeploymentsSetupSessionsListOutputItemsConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItemsConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsConfig:
        return ProviderDeploymentsSetupSessionsListOutputItemsConfig(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        specification_id=data.get('specification_id'),
        deployment=mapProviderDeploymentsSetupSessionsListOutputItemsConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapProviderDeploymentsSetupSessionsListOutputItemsConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItems:
        return ProviderDeploymentsSetupSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        url=data.get('url'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=data.get('configuration'),
        provider_id=data.get('provider_id'),
        identity_id=data.get('identity_id'),
        identity_credential_id=data.get('identity_credential_id'),
        auth_method=mapProviderDeploymentsSetupSessionsListOutputItemsAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapProviderDeploymentsSetupSessionsListOutputItemsDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapProviderDeploymentsSetupSessionsListOutputItemsCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapProviderDeploymentsSetupSessionsListOutputItemsConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputPagination:
        return ProviderDeploymentsSetupSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutput:
        return ProviderDeploymentsSetupSessionsListOutput(
        items=[mapProviderDeploymentsSetupSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsSetupSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderDeploymentsSetupSessionsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ProviderDeploymentsSetupSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_auth_method_id: Optional[Union[str, List[str]]] = None
    provider_auth_config_id: Optional[Union[str, List[str]]] = None
    provider_auth_credentials_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    created_at: Optional[ProviderDeploymentsSetupSessionsListQueryCreatedAt] = None
    updated_at: Optional[ProviderDeploymentsSetupSessionsListQueryUpdatedAt] = None


class mapProviderDeploymentsSetupSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListQuery:
        return ProviderDeploymentsSetupSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        status=data.get('status'),
        created_at=mapProviderDeploymentsSetupSessionsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapProviderDeploymentsSetupSessionsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

