from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOutpostsAccessSetOutputItems:
    object: str
    id: str
    outpost_id: str
    project_id: str
    instance_id: str
    organization_id: str
    services: List[str]
    created_at: datetime
@dataclass
class DashboardOrganizationsOutpostsAccessSetOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsOutpostsAccessSetOutput:
    items: List[DashboardOrganizationsOutpostsAccessSetOutputItems]
    pagination: DashboardOrganizationsOutpostsAccessSetOutputPagination


class mapDashboardOrganizationsOutpostsAccessSetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessSetOutputItems:
        return DashboardOrganizationsOutpostsAccessSetOutputItems(
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
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessSetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOutpostsAccessSetOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessSetOutputPagination:
        return DashboardOrganizationsOutpostsAccessSetOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessSetOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOutpostsAccessSetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessSetOutput:
        return DashboardOrganizationsOutpostsAccessSetOutput(
        items=[mapDashboardOrganizationsOutpostsAccessSetOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsOutpostsAccessSetOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessSetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOutpostsAccessSetBodyGrants:
    instance_id: str
    services: List[str]
@dataclass
class DashboardOrganizationsOutpostsAccessSetBody:
    grants: List[DashboardOrganizationsOutpostsAccessSetBodyGrants]


class mapDashboardOrganizationsOutpostsAccessSetBodyGrants:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessSetBodyGrants:
        return DashboardOrganizationsOutpostsAccessSetBodyGrants(
        instance_id=data.get('instance_id'),
        services=data.get('services', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessSetBodyGrants, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOutpostsAccessSetBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOutpostsAccessSetBody:
        return DashboardOrganizationsOutpostsAccessSetBody(
        grants=[mapDashboardOrganizationsOutpostsAccessSetBodyGrants.from_dict(item) for item in data.get('grants', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOutpostsAccessSetBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

