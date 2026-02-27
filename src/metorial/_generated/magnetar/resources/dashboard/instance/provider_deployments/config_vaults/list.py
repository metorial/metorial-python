from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsConfigVaultsListOutputItems:
    object: str
    id: str
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider_deployment_id: Optional[str] = None
@dataclass
class DashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderDeploymentsConfigVaultsListOutput:
    items: List[DashboardInstanceProviderDeploymentsConfigVaultsListOutputItems]
    pagination: DashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination


class mapDashboardInstanceProviderDeploymentsConfigVaultsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsConfigVaultsListOutputItems:
        return DashboardInstanceProviderDeploymentsConfigVaultsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsConfigVaultsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination:
        return DashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderDeploymentsConfigVaultsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsConfigVaultsListOutput:
        return DashboardInstanceProviderDeploymentsConfigVaultsListOutput(
        items=[mapDashboardInstanceProviderDeploymentsConfigVaultsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderDeploymentsConfigVaultsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsConfigVaultsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderDeploymentsConfigVaultsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceProviderDeploymentsConfigVaultsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsConfigVaultsListQuery:
        return DashboardInstanceProviderDeploymentsConfigVaultsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsConfigVaultsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
