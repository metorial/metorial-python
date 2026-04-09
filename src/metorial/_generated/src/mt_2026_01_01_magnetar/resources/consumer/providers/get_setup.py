from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerProvidersGetSetupOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersGetSetupOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersGetSetupOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ConsumerProvidersGetSetupOutputAuthMethod:
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
    input_schema: Optional[ConsumerProvidersGetSetupOutputAuthMethodInputSchema] = None
    output_schema: Optional[ConsumerProvidersGetSetupOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ConsumerProvidersGetSetupOutputAuthMethodScopes]] = None
@dataclass
class ConsumerProvidersGetSetupOutputDeployment:
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
class ConsumerProvidersGetSetupOutputCredentials:
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
class ConsumerProvidersGetSetupOutputAuthConfigDeployment:
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
class ConsumerProvidersGetSetupOutputAuthConfigCredentials:
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
class ConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ConsumerProvidersGetSetupOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ConsumerProvidersGetSetupOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: ConsumerProvidersGetSetupOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ConsumerProvidersGetSetupOutputAuthConfigDeployment] = None
    credentials: Optional[ConsumerProvidersGetSetupOutputAuthConfigCredentials] = None
@dataclass
class ConsumerProvidersGetSetupOutputConfigDeployment:
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
class ConsumerProvidersGetSetupOutputConfigFromVaultDeployment:
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
class ConsumerProvidersGetSetupOutputConfigFromVault:
    object: str
    id: str
    status: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ConsumerProvidersGetSetupOutputConfigFromVaultDeployment] = None
@dataclass
class ConsumerProvidersGetSetupOutputConfig:
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
    deployment: Optional[ConsumerProvidersGetSetupOutputConfigDeployment] = None
    from_vault: Optional[ConsumerProvidersGetSetupOutputConfigFromVault] = None
@dataclass
class ConsumerProvidersGetSetupOutput:
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
    auth_method: Optional[ConsumerProvidersGetSetupOutputAuthMethod] = None
    deployment: Optional[ConsumerProvidersGetSetupOutputDeployment] = None
    credentials: Optional[ConsumerProvidersGetSetupOutputCredentials] = None
    auth_config: Optional[ConsumerProvidersGetSetupOutputAuthConfig] = None
    config: Optional[ConsumerProvidersGetSetupOutputConfig] = None
    redirect_url: Optional[str] = None


class mapConsumerProvidersGetSetupOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthMethodInputSchema:
        return ConsumerProvidersGetSetupOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthMethodOutputSchema:
        return ConsumerProvidersGetSetupOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthMethodScopes:
        return ConsumerProvidersGetSetupOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthMethod:
        return ConsumerProvidersGetSetupOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapConsumerProvidersGetSetupOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerProvidersGetSetupOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapConsumerProvidersGetSetupOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputDeployment:
        return ConsumerProvidersGetSetupOutputDeployment(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputCredentials:
        return ConsumerProvidersGetSetupOutputCredentials(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigDeployment:
        return ConsumerProvidersGetSetupOutputAuthConfigDeployment(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigCredentials:
        return ConsumerProvidersGetSetupOutputAuthConfigCredentials(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema:
        return ConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema:
        return ConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes:
        return ConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfigAuthMethod:
        return ConsumerProvidersGetSetupOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapConsumerProvidersGetSetupOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputAuthConfig:
        return ConsumerProvidersGetSetupOutputAuthConfig(
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
        deployment=mapConsumerProvidersGetSetupOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapConsumerProvidersGetSetupOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapConsumerProvidersGetSetupOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputConfigDeployment:
        return ConsumerProvidersGetSetupOutputConfigDeployment(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputConfigFromVaultDeployment:
        return ConsumerProvidersGetSetupOutputConfigFromVaultDeployment(
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
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputConfigFromVault:
        return ConsumerProvidersGetSetupOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapConsumerProvidersGetSetupOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutputConfig:
        return ConsumerProvidersGetSetupOutputConfig(
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
        deployment=mapConsumerProvidersGetSetupOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapConsumerProvidersGetSetupOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerProvidersGetSetupOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerProvidersGetSetupOutput:
        return ConsumerProvidersGetSetupOutput(
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
        auth_method=mapConsumerProvidersGetSetupOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapConsumerProvidersGetSetupOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapConsumerProvidersGetSetupOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapConsumerProvidersGetSetupOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapConsumerProvidersGetSetupOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerProvidersGetSetupOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

