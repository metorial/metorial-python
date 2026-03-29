from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessRolesCreateOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    is_admin: bool
    scopes: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsAccessRolesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesCreateOutput:
        return DashboardOrganizationsAccessRolesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        is_admin=data.get('is_admin'),
        scopes=data.get('scopes', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessRolesCreateBody:
    name: str
    description: Optional[str] = None
    scopes: Optional[List[str]] = None
    message: Optional[str] = None


class mapDashboardOrganizationsAccessRolesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessRolesCreateBody:
        return DashboardOrganizationsAccessRolesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        scopes=data.get('scopes', []),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessRolesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

