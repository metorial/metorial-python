from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsAuthConfigsGetOutputDeploymentPreview:
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
class ProviderDeploymentsAuthConfigsGetOutputCredentials:
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
class ProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ProviderDeploymentsAuthConfigsGetOutputAuthMethod:
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
    input_schema: Optional[ProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema] = None
    output_schema: Optional[ProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes]] = None
@dataclass
class ProviderDeploymentsAuthConfigsGetOutput:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: ProviderDeploymentsAuthConfigsGetOutputAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment_preview: Optional[ProviderDeploymentsAuthConfigsGetOutputDeploymentPreview] = None
    credentials: Optional[ProviderDeploymentsAuthConfigsGetOutputCredentials] = None


class mapProviderDeploymentsAuthConfigsGetOutputDeploymentPreview:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputDeploymentPreview:
        return ProviderDeploymentsAuthConfigsGetOutputDeploymentPreview(
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
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputDeploymentPreview, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputCredentials:
        return ProviderDeploymentsAuthConfigsGetOutputCredentials(
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
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema:
        return ProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema:
        return ProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes:
        return ProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutputAuthMethod:
        return ProviderDeploymentsAuthConfigsGetOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapProviderDeploymentsAuthConfigsGetOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapProviderDeploymentsAuthConfigsGetOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapProviderDeploymentsAuthConfigsGetOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsAuthConfigsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsAuthConfigsGetOutput:
        return ProviderDeploymentsAuthConfigsGetOutput(
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
        deployment_preview=mapProviderDeploymentsAuthConfigsGetOutputDeploymentPreview.from_dict(data.get('deployment_preview')) if data.get('deployment_preview') else None,
        credentials=mapProviderDeploymentsAuthConfigsGetOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapProviderDeploymentsAuthConfigsGetOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsAuthConfigsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

