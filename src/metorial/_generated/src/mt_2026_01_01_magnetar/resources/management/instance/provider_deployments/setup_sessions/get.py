from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials:
    object: str
    id: str
    type: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials:
    object: str
    id: str
    type: str
    is_default: bool
    is_managed: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault:
    object: str
    id: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig:
    object: str
    id: str
    is_default: bool
    tool_filter: Dict[str, Any]
    provider_id: str
    specification_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment] = None
    from_vault: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsGetOutput:
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
    auth_method: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials] = None
    auth_config: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig] = None
    config: Optional[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig(
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
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        specification_id=data.get('specification_id'),
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsGetOutput:
        return ManagementInstanceProviderDeploymentsSetupSessionsGetOutput(
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
        auth_method=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapManagementInstanceProviderDeploymentsSetupSessionsGetOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

