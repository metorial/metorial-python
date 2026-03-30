from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
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
    input_schema: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema] = None
    output_schema: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes]] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
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
    input_schema: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment] = None
    credentials: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
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
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    object: str
    id: str
    name: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
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
    deployment: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment] = None
    from_vault: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput:
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
    auth_method: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod] = None
    deployment: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment] = None
    credentials: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials] = None
    auth_config: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig] = None
    config: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig] = None
    redirect_url: Optional[str] = None


class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig(
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
        deployment=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        deployment=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVaultDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        specification_id=data.get('specification_id'),
        deployment=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        from_vault=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfigFromVault.from_dict(data.get('from_vault')) if data.get('from_vault') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput(
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
        auth_method=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        deployment=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_config=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        config=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        ui_mode=data.get('ui_mode'),
        redirect_url=data.get('redirect_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    group_id: str
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    collection_id: str
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    category_id: str
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    groups: Optional[List[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups]] = None
    collections: Optional[List[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections]] = None
    categories: Optional[List[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories]] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    enabled: Optional[bool] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    layout: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    provider_search: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch] = None
    tool_filters: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters] = None
    ui: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi] = None
@dataclass
class DashboardInstanceProviderDeploymentsSetupSessionsCreateBody:
    provider_id: Optional[str] = None
    provider_deployment_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_auth_method_id: Optional[str] = None
    provider_auth_credentials_id: Optional[str] = None
    redirect_url: Optional[str] = None
    configuration: Optional[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration] = None


class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups(
        group_id=data.get('group_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections(
        collection_id=data.get('collection_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories(
        category_id=data.get('category_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch(
        groups=[mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchGroups.from_dict(item) for item in data.get('groups', []) if item],
        collections=[mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCollections.from_dict(item) for item in data.get('collections', []) if item],
        categories=[mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearchCategories.from_dict(item) for item in data.get('categories', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters(
        enabled=data.get('enabled')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi(
        layout=data.get('layout')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration(
        provider_search=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationProviderSearch.from_dict(data.get('provider_search')) if data.get('provider_search') else None,
        tool_filters=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationToolFilters.from_dict(data.get('tool_filters')) if data.get('tool_filters') else None,
        ui=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfigurationUi.from_dict(data.get('ui')) if data.get('ui') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsSetupSessionsCreateBody:
        return DashboardInstanceProviderDeploymentsSetupSessionsCreateBody(
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        redirect_url=data.get('redirect_url'),
        configuration=mapDashboardInstanceProviderDeploymentsSetupSessionsCreateBodyConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsSetupSessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

