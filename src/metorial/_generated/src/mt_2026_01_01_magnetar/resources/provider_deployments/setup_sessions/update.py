from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthMethod:
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
    input_schema: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputDeployment:
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
class ProviderDeploymentsSetupSessionsUpdateOutputCredentials:
    object: str
    id: str
    type: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview:
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
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials:
    object: str
    id: str
    type: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment_preview: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment:
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
class ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment:
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
class ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault:
    object: str
    id: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutputConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    specification_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment] = None
    from_vault: Optional[ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault] = None
@dataclass
class ProviderDeploymentsSetupSessionsUpdateOutput:
    object: str
    id: str
    type: str
    status: str
    url: str
    provider_id: str
    auth_method: ProviderDeploymentsSetupSessionsUpdateOutputAuthMethod
    ui_mode: str
    created_at: datetime
    updated_at: datetime
    expires_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ProviderDeploymentsSetupSessionsUpdateOutputDeployment] = None
    credentials: Optional[ProviderDeploymentsSetupSessionsUpdateOutputCredentials] = None
    auth_config: Optional[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfig] = None
    config: Optional[ProviderDeploymentsSetupSessionsUpdateOutputConfig] = None
    redirect_url: Optional[str] = None


class mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthMethod:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputDeployment:
        return ProviderDeploymentsSetupSessionsUpdateOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputCredentials:
        return ProviderDeploymentsSetupSessionsUpdateOutputCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputAuthConfig:
        return ProviderDeploymentsSetupSessionsUpdateOutputAuthConfig(
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
        deployment_preview=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigDeploymentPreview.from_dict(data.get('deployment_preview')) if data.get('deployment_preview') else None,
        credentials=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment:
        return ProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment:
        return ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault:
        return ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapProviderDeploymentsSetupSessionsUpdateOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutputConfig:
        return ProviderDeploymentsSetupSessionsUpdateOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        specification_id=data.get('specification_id'),
        deployment=mapProviderDeploymentsSetupSessionsUpdateOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapProviderDeploymentsSetupSessionsUpdateOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateOutput:
        return ProviderDeploymentsSetupSessionsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        url=data.get('url'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        auth_method=mapProviderDeploymentsSetupSessionsUpdateOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapProviderDeploymentsSetupSessionsUpdateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapProviderDeploymentsSetupSessionsUpdateOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapProviderDeploymentsSetupSessionsUpdateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapProviderDeploymentsSetupSessionsUpdateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProviderDeploymentsSetupSessionsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsUpdateBody:
        return ProviderDeploymentsSetupSessionsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
