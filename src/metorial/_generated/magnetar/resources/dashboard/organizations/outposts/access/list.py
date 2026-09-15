from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOutpostsAccessListOutputItems:
    object: str
    id: str
    outpost_id: str
    project_id: str
    instance_id: str
    organization_id: str
    services: List[str]
    created_at: datetime
@dataclass
class DashboardOrganizationsOutpostsAccessListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsOutpostsAccessListOutput:
    items: List[DashboardOrganizationsOutpostsAccessListOutputItems]
    pagination: DashboardOrganizationsOutpostsAccessListOutputPagination


class mapDashboardOrganizationsOutpostsAccessListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessListOutputItems:
        return DashboardOrganizationsOutpostsAccessListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        outpost_id=data.get('outpost_id'),
        project_id=data.get('project_id'),
        instance_id=data.get('instance_id'),
        organization_id=data.get('organization_id'),
        services=data.get('services', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOutpostsAccessListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessListOutputPagination:
        return DashboardOrganizationsOutpostsAccessListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOutpostsAccessListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessListOutput:
        return DashboardOrganizationsOutpostsAccessListOutput(
        items=[mapDashboardOrganizationsOutpostsAccessListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsOutpostsAccessListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOutpostsAccessListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    organization_id: Optional[str] = None
    instance_id: Optional[str] = None


class mapDashboardOrganizationsOutpostsAccessListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessListQuery:
        return DashboardOrganizationsOutpostsAccessListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

