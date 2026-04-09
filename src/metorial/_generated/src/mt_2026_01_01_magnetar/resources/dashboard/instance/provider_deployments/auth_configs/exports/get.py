from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment:
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
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials:
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
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod:
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
    input_schema: Optional[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    tool_filter: Dict[str, Any]
    auth_method: DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment] = None
    credentials: Optional[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials] = None
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput:
    object: str
    id: str
    note: str
    auth_config: DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig
    provider_id: str
    auth_method_id: str
    created_at: datetime
    ip: Optional[str] = None
    user_agent: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
    credentials_id: Optional[str] = None
    value: Optional[Dict[str, Any]] = None
    expires_at: Optional[datetime] = None


class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig(
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
        deployment=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput:
        return DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        ip=data.get('ip'),
        user_agent=data.get('user_agent'),
        metadata=data.get('metadata'),
        auth_config=mapDashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        credentials_id=data.get('credentials_id'),
        value=data.get('value'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsExportsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

