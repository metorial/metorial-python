from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview:
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
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials:
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
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod:
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
    input_schema: Optional[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema] = None
    output_schema: Optional[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes]] = None
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment_preview: Optional[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview] = None
    credentials: Optional[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials] = None


class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput:
        return DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput(
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
        deployment_preview=mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputDeploymentPreview.from_dict(data.get('deployment_preview')) if data.get('deployment_preview') else None,
        credentials=mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapDashboardInstanceProviderDeploymentsAuthConfigsDeleteOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
