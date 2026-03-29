from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsTeamsGetOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsTeamsGetOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsTeamsGetOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsTeamsGetOutputProjectsProject
@dataclass
class DashboardOrganizationsTeamsGetOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[DashboardOrganizationsTeamsGetOutputPolicies]
    projects: List[DashboardOrganizationsTeamsGetOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsTeamsGetOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsGetOutputPolicies:
        return DashboardOrganizationsTeamsGetOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsGetOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsGetOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsGetOutputProjectsProject:
        return DashboardOrganizationsTeamsGetOutputProjectsProject(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsGetOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsGetOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsGetOutputProjects:
        return DashboardOrganizationsTeamsGetOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsTeamsGetOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsGetOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsGetOutput:
        return DashboardOrganizationsTeamsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapDashboardOrganizationsTeamsGetOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapDashboardOrganizationsTeamsGetOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

