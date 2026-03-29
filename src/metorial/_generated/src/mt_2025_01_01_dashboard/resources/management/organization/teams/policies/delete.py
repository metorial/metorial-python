from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationTeamsPoliciesDeleteOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationTeamsPoliciesDeleteOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject
@dataclass
class ManagementOrganizationTeamsPoliciesDeleteOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[ManagementOrganizationTeamsPoliciesDeleteOutputPolicies]
    projects: List[ManagementOrganizationTeamsPoliciesDeleteOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationTeamsPoliciesDeleteOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsPoliciesDeleteOutputPolicies:
        return ManagementOrganizationTeamsPoliciesDeleteOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsPoliciesDeleteOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject:
        return ManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject(
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
    def to_dict(value: Union[ManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsPoliciesDeleteOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsPoliciesDeleteOutputProjects:
        return ManagementOrganizationTeamsPoliciesDeleteOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationTeamsPoliciesDeleteOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsPoliciesDeleteOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsPoliciesDeleteOutput:
        return ManagementOrganizationTeamsPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapManagementOrganizationTeamsPoliciesDeleteOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapManagementOrganizationTeamsPoliciesDeleteOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

