from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts:
    connections: float
@dataclass
class DashboardInstancePortalsAuthSsoTenantsListOutputItems:
    object: str
    id: str
    name: str
    status: str
    client_id: str
    counts: DashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstancePortalsAuthSsoTenantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstancePortalsAuthSsoTenantsListOutput:
    items: List[DashboardInstancePortalsAuthSsoTenantsListOutputItems]
    pagination: DashboardInstancePortalsAuthSsoTenantsListOutputPagination


class mapDashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts:
        return DashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts(
        connections=data.get('connections')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsListOutputItems:
        return DashboardInstancePortalsAuthSsoTenantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        status=data.get('status'),
        client_id=data.get('client_id'),
        counts=mapDashboardInstancePortalsAuthSsoTenantsListOutputItemsCounts.from_dict(data.get('counts')) if data.get('counts') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsListOutputPagination:
        return DashboardInstancePortalsAuthSsoTenantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsListOutput:
        return DashboardInstancePortalsAuthSsoTenantsListOutput(
        items=[mapDashboardInstancePortalsAuthSsoTenantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstancePortalsAuthSsoTenantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAuthSsoTenantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstancePortalsAuthSsoTenantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsListQuery:
        return DashboardInstancePortalsAuthSsoTenantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

