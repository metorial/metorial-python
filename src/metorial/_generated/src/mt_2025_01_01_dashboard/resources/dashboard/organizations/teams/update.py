from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsTeamsUpdateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsTeamsUpdateOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsTeamsUpdateOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsTeamsUpdateOutputProjectsProject
@dataclass
class DashboardOrganizationsTeamsUpdateOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[DashboardOrganizationsTeamsUpdateOutputPolicies]
    projects: List[DashboardOrganizationsTeamsUpdateOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsTeamsUpdateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateOutputPolicies:
        return DashboardOrganizationsTeamsUpdateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsUpdateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsUpdateOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateOutputProjectsProject:
        return DashboardOrganizationsTeamsUpdateOutputProjectsProject(
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
    def to_dict(value: Union[DashboardOrganizationsTeamsUpdateOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsUpdateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateOutputProjects:
        return DashboardOrganizationsTeamsUpdateOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsTeamsUpdateOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsUpdateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsTeamsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateOutput:
        return DashboardOrganizationsTeamsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapDashboardOrganizationsTeamsUpdateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapDashboardOrganizationsTeamsUpdateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsTeamsUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None


class mapDashboardOrganizationsTeamsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsTeamsUpdateBody:
        return DashboardOrganizationsTeamsUpdateBody(
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsTeamsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

