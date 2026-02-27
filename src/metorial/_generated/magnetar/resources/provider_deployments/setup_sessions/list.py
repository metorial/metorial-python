from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
    object: str
    id: str
    type: str
    provider_id: str
    provider_auth_method_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputItems:
    object: str
    id: str
    type: str
    status: str
    provider_id: str
    provider_auth_method_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None
    expires_at: Optional[datetime] = None
    auth_config: Optional[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig] = None
@dataclass
class ProviderDeploymentsSetupSessionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsSetupSessionsListOutput:
    items: List[ProviderDeploymentsSetupSessionsListOutputItems]
    pagination: ProviderDeploymentsSetupSessionsListOutputPagination


class mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig:
        return ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItemsAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputItems:
        return ProviderDeploymentsSetupSessionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        redirect_url=data.get('redirect_url'),
        url=data.get('url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at')) if data.get('expires_at') else None,
        auth_config=mapProviderDeploymentsSetupSessionsListOutputItemsAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutputPagination:
        return ProviderDeploymentsSetupSessionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListOutput:
        return ProviderDeploymentsSetupSessionsListOutput(
        items=[mapProviderDeploymentsSetupSessionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsSetupSessionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_auth_method_id: Optional[Union[str, List[str]]] = None
    status: Optional[str] = None


class mapProviderDeploymentsSetupSessionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsListQuery:
        return ProviderDeploymentsSetupSessionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
