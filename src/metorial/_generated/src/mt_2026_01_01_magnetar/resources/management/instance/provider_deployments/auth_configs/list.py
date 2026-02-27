from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview:
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
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials:
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
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema:
    type: str
    schema: Dict[str, Any]
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod:
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
    input_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema] = None
    output_schema: Optional[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema] = None
    scopes: Optional[List[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes]] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputItems:
    object: str
    id: str
    type: str
    source: str
    status: str
    is_default: bool
    provider_id: str
    auth_method: ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    deployment_preview: Optional[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview] = None
    credentials: Optional[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials] = None
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListOutput:
    items: List[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItems]
    pagination: ManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination


class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials(
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
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema(
        type=data.get('type'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description'),
        capabilities=data.get('capabilities'),
        input_schema=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodInputSchema.from_dict(data.get('input_schema')) if data.get('input_schema') else None,
        output_schema=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodOutputSchema.from_dict(data.get('output_schema')) if data.get('output_schema') else None,
        scopes=[mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethodScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputItems:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputItems(
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
        deployment_preview=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsDeploymentPreview.from_dict(data.get('deployment_preview')) if data.get('deployment_preview') else None,
        credentials=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsCredentials.from_dict(data.get('credentials')) if data.get('credentials') else None,
        auth_method=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItemsAuthMethod.from_dict(data.get('auth_method')) if data.get('auth_method') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsAuthConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsListOutput(
        items=[mapManagementInstanceProviderDeploymentsAuthConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderDeploymentsAuthConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    provider_deployment_id: Optional[Union[str, List[str]]] = None
    provider_auth_credentials_id: Optional[Union[str, List[str]]] = None
    provider_auth_method_id: Optional[Union[str, List[str]]] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsListQuery:
        return ManagementInstanceProviderDeploymentsAuthConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id'),
        provider_auth_method_id=data.get('provider_auth_method_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
