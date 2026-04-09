from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
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
    input_schema: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputDeployment:
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
class ProviderDeploymentsSetupSessionsCreateOutputCredentials:
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
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
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
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
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
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
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
class ProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
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
class ProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    object: str
    id: str
    status: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutputConfig:
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
    deployment: Optional[ProviderDeploymentsSetupSessionsCreateOutputConfigDeployment] = None
    from_vault: Optional[ProviderDeploymentsSetupSessionsCreateOutputConfigFromVault] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateOutput:
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
    auth_method: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthMethod] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsCreateOutputDeployment] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsCreateOutputCredentials] = None
    auth_config: Optional[ProviderDeploymentsSetupSessionsCreateOutputAuthConfig] = None
    config: Optional[ProviderDeploymentsSetupSessionsCreateOutputConfig] = None
    redirect_url: Optional[str] = None


class mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputDeployment:
        return ProviderDeploymentsSetupSessionsCreateOutputDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputCredentials:
        return ProviderDeploymentsSetupSessionsCreateOutputCredentials(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
        return ProviderDeploymentsSetupSessionsCreateOutputAuthConfig(
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
        deployment=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
        return ProviderDeploymentsSetupSessionsCreateOutputConfigDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
        return ProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment(
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
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
        return ProviderDeploymentsSetupSessionsCreateOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutputConfig:
        return ProviderDeploymentsSetupSessionsCreateOutputConfig(
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
        deployment=mapProviderDeploymentsSetupSessionsCreateOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapProviderDeploymentsSetupSessionsCreateOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateOutput:
        return ProviderDeploymentsSetupSessionsCreateOutput(
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
        auth_method=mapProviderDeploymentsSetupSessionsCreateOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapProviderDeploymentsSetupSessionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapProviderDeploymentsSetupSessionsCreateOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapProviderDeploymentsSetupSessionsCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapProviderDeploymentsSetupSessionsCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    group_id: str
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    collection_id: str
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    category_id: str
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    groups: Optional[List[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups]] = None
    collections: Optional[List[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections]] = None
    categories: Optional[List[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories]] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    enabled: Optional[bool] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    layout: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    provider_search: Optional[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch] = None
    tool_filters: Optional[ProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters] = None
    ui: Optional[ProviderDeploymentsSetupSessionsCreateBodyConfigurationUi] = None
@dataclass
class ProviderDeploymentsSetupSessionsCreateBody:
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_auth_method_id: Optional[str] = None
    provider_auth_credentials_id: Optional[str] = None
    identity_id: Optional[str] = None
    consumer_id: Optional[str] = None
    redirect_url: Optional[str] = None
    type: Optional[str] = None
    configuration: Optional[ProviderDeploymentsSetupSessionsCreateBodyConfiguration] = None


class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups(
        group_id=data.get('group_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections(
        collection_id=data.get('collection_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories(
        category_id=data.get('category_id')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch(
        groups=[mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups.from_dict(item) for item in data.get('groups', []) if item],
        collections=[mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections.from_dict(item) for item in data.get('collections', []) if item],
        categories=[mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories.from_dict(item) for item in data.get('categories', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
        return ProviderDeploymentsSetupSessionsCreateBodyConfigurationUi(
        layout=data.get('layout')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfigurationUi, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBodyConfiguration:
        return ProviderDeploymentsSetupSessionsCreateBodyConfiguration(
        provider_search=mapProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch.from_dict(data.get('provider_search')) if data.get('provider_search') else None,
        tool_filters=mapProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None,
        ui=mapProviderDeploymentsSetupSessionsCreateBodyConfigurationUi.from_dict(data.get('ui')) if data.get('ui') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBodyConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsCreateBody:
        return ProviderDeploymentsSetupSessionsCreateBody(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        identity_id=data.get('identity_id'),
        consumer_id=data.get('consumer_id'),
        redirect_url=data.get('redirect_url'),
        type=data.get('type'),
        configuration=mapProviderDeploymentsSetupSessionsCreateBodyConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

