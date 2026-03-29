from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationTeamsMembersDeleteOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationTeamsMembersDeleteOutputProjectsProject
@dataclass
class ManagementOrganizationTeamsMembersDeleteOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[ManagementOrganizationTeamsMembersDeleteOutputPolicies]
    projects: List[ManagementOrganizationTeamsMembersDeleteOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationTeamsMembersDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersDeleteOutputPolicies:
        return ManagementOrganizationTeamsMembersDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersDeleteOutputProjectsProject:
        return ManagementOrganizationTeamsMembersDeleteOutputProjectsProject(
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
    def to_dict(value: Union[ManagementOrganizationTeamsMembersDeleteOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersDeleteOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersDeleteOutputProjects:
        return ManagementOrganizationTeamsMembersDeleteOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationTeamsMembersDeleteOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersDeleteOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersDeleteOutput:
        return ManagementOrganizationTeamsMembersDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapManagementOrganizationTeamsMembersDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapManagementOrganizationTeamsMembersDeleteOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

