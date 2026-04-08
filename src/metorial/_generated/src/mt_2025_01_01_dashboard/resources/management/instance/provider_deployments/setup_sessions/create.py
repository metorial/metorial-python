from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
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
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    object: str
    id: str
    status: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
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
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment] = None
    from_vault: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
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
    auth_method: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials] = None
    auth_config: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig] = None
    config: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig(
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
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig(
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
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput(
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
        auth_method=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapManagementInstanceProviderDeploymentsSetupSessionsCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    group_id: str
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    collection_id: str
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    category_id: str
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    groups: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups]] = None
    collections: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections]] = None
    categories: Optional[List[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories]] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    enabled: Optional[bool] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    layout: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    provider_search: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch] = None
    tool_filters: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters] = None
    ui: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
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
    configuration: Optional[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups(
        group_id=data.get('group_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections(
        collection_id=data.get('collection_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories(
        category_id=data.get('category_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch(
        groups=[mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups.from_dict(item) for item in data.get('groups', []) if item],
        collections=[mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections.from_dict(item) for item in data.get('collections', []) if item],
        categories=[mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories.from_dict(item) for item in data.get('categories', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi(
        layout=data.get('layout')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration(
        provider_search=mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch.from_dict(data.get('provider_search')) if data.get('provider_search') else None,
        tool_filters=mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None,
        ui=mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi.from_dict(data.get('ui')) if data.get('ui') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsCreateBody:
        return ManagementInstanceProviderDeploymentsSetupSessionsCreateBody(
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
        configuration=mapManagementInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

