from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationTeamsMembersCreateOutputPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationTeamsMembersCreateOutputProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationTeamsMembersCreateOutputProjectsProject
@dataclass
class ManagementOrganizationTeamsMembersCreateOutput:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[ManagementOrganizationTeamsMembersCreateOutputPolicies]
    projects: List[ManagementOrganizationTeamsMembersCreateOutputProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationTeamsMembersCreateOutputPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateOutputPolicies:
        return ManagementOrganizationTeamsMembersCreateOutputPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersCreateOutputPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersCreateOutputProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateOutputProjectsProject:
        return ManagementOrganizationTeamsMembersCreateOutputProjectsProject(
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
    def to_dict(value: Union[ManagementOrganizationTeamsMembersCreateOutputProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersCreateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateOutputProjects:
        return ManagementOrganizationTeamsMembersCreateOutputProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationTeamsMembersCreateOutputProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersCreateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsMembersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateOutput:
        return ManagementOrganizationTeamsMembersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapManagementOrganizationTeamsMembersCreateOutputPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapManagementOrganizationTeamsMembersCreateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationTeamsMembersCreateBody:
    actor_id: str


class mapManagementOrganizationTeamsMembersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsMembersCreateBody:
        return ManagementOrganizationTeamsMembersCreateBody(
        actor_id=data.get('actor_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsMembersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

