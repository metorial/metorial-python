from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview:
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
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials:
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
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutput:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment_preview: Optional[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutput(
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
        deployment_preview=mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputDeploymentPreview.from_dict(data.get('deployment_preview')) if data.get('deployment_preview') else None,
        credentials=mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapManagementInstanceProviderDeploymentsAuthConfigsUpdateOutputAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsUpdateBody:
        return ManagementInstanceProviderDeploymentsAuthConfigsUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
