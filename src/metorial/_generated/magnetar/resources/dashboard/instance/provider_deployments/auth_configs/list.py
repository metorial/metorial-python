from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsListOutputItems:
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
class DashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsListOutput:
    items: List[DashboardInstanceProviderDeploymentsAuthConfigsListOutputItems]
    pagination: DashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination


class mapDashboardInstanceProviderDeploymentsAuthConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsListOutputItems:
        return DashboardInstanceProviderDeploymentsAuthConfigsListOutputItems(
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
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination:
        return DashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsAuthConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsListOutput:
        return DashboardInstanceProviderDeploymentsAuthConfigsListOutput(
        items=[mapDashboardInstanceProviderDeploymentsAuthConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderDeploymentsAuthConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderDeploymentsAuthConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    provider_auth_method_id: Optional[Union[str, List[str]]] = None
    provider_auth_credentials_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceProviderDeploymentsAuthConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsAuthConfigsListQuery:
        return DashboardInstanceProviderDeploymentsAuthConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        provider_auth_method_id=data.get('provider_auth_method_id'),
        provider_auth_credentials_id=data.get('provider_auth_credentials_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsAuthConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
