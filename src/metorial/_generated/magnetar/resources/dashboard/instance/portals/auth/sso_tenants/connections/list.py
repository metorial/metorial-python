from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
    object: str
    id: str
    name: str
    provider_type: str
    created_at: datetime
    provider_name: Optional[str] = None
@dataclass
class DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput:
    items: List[DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems]
    pagination: DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination


class mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems:
        return DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        provider_type=data.get('provider_type'),
        provider_name=data.get('provider_name'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination:
        return DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput:
        return DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput(
        items=[mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsAuthSsoTenantsConnectionsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsConnectionsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAuthSsoTenantsConnectionsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstancePortalsAuthSsoTenantsConnectionsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsConnectionsListQuery:
        return DashboardInstancePortalsAuthSsoTenantsConnectionsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsConnectionsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

