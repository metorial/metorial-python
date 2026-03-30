from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment:
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
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials:
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
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment: Optional[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutput:
    object: str
    id: str
    note: str
    auth_config: ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig
    provider_id: str
    auth_method_id: str
    created_at: datetime
    ip: Optional[str] = None
    user_agent: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
    credentials_id: Optional[str] = None
    expires_at: Optional[datetime] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig(
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
        deployment=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        credentials=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfigAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        ip=data.get('ip'),
        user_agent=data.get('user_agent'),
        metadata=data.get('metadata'),
        auth_config=mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        auth_method_id=data.get('auth_method_id'),
        credentials_id=data.get('credentials_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

