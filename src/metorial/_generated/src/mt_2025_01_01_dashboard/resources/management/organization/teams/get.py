from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationTeamsGetOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationTeamsGetOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationTeamsGetOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationTeamsGetOutputProjectsProject
@dataclass
class ManagementOrganizationTeamsGetOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[ManagementOrganizationTeamsGetOutputPolicies]
    projects: List[ManagementOrganizationTeamsGetOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationTeamsGetOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsGetOutputPolicies:
        return ManagementOrganizationTeamsGetOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsGetOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsGetOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsGetOutputProjectsProject:
        return ManagementOrganizationTeamsGetOutputProjectsProject(
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
    def to_dict(value: Union[ManagementOrganizationTeamsGetOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsGetOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsGetOutputProjects:
        return ManagementOrganizationTeamsGetOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationTeamsGetOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsGetOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsGetOutput:
        return ManagementOrganizationTeamsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapManagementOrganizationTeamsGetOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapManagementOrganizationTeamsGetOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

