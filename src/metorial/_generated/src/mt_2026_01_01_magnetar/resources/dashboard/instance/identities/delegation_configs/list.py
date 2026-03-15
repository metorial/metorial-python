from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIdentitiesDelegationConfigsListOutputItems:
    object: str
    id: str
    status: str
    is_default: bool
    sub_delegation_behavior: str
    sub_delegation_depth: float
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceIdentitiesDelegationConfigsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceIdentitiesDelegationConfigsListOutput:
    items: List[DashboardInstanceIdentitiesDelegationConfigsListOutputItems]
    pagination: DashboardInstanceIdentitiesDelegationConfigsListOutputPagination


class mapDashboardInstanceIdentitiesDelegationConfigsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationConfigsListOutputItems:
        return DashboardInstanceIdentitiesDelegationConfigsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        sub_delegation_behavior=data.get('sub_delegation_behavior'),
        sub_delegation_depth=data.get('sub_delegation_depth'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationConfigsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationConfigsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationConfigsListOutputPagination:
        return DashboardInstanceIdentitiesDelegationConfigsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationConfigsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIdentitiesDelegationConfigsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationConfigsListOutput:
        return DashboardInstanceIdentitiesDelegationConfigsListOutput(
        items=[mapDashboardInstanceIdentitiesDelegationConfigsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceIdentitiesDelegationConfigsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationConfigsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceIdentitiesDelegationConfigsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceIdentitiesDelegationConfigsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIdentitiesDelegationConfigsListQuery:
        return DashboardInstanceIdentitiesDelegationConfigsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIdentitiesDelegationConfigsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

