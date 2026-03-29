from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessRolesVersionsOutputItems:
    object: str
    id: str
    access_role_id: str
    index: float
    scopes: List[str]
    scopes_added: List[str]
    scopes_removed: List[str]
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardOrganizationsAccessRolesVersionsOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsAccessRolesVersionsOutput:
    items: List[DashboardOrganizationsAccessRolesVersionsOutputItems]
    pagination: DashboardOrganizationsAccessRolesVersionsOutputPagination


class mapDashboardOrganizationsAccessRolesVersionsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesVersionsOutputItems:
        return DashboardOrganizationsAccessRolesVersionsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access_role_id=data.get('access_role_id'),
        index=data.get('index'),
        scopes=data.get('scopes', []),
        scopes_added=data.get('scopes_added', []),
        scopes_removed=data.get('scopes_removed', []),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesVersionsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessRolesVersionsOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesVersionsOutputPagination:
        return DashboardOrganizationsAccessRolesVersionsOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesVersionsOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessRolesVersionsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesVersionsOutput:
        return DashboardOrganizationsAccessRolesVersionsOutput(
        items=[mapDashboardOrganizationsAccessRolesVersionsOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsAccessRolesVersionsOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesVersionsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessRolesVersionsQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardOrganizationsAccessRolesVersionsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesVersionsQuery:
        return DashboardOrganizationsAccessRolesVersionsQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesVersionsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

