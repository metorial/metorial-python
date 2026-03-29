from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationTeamsListOutputItemsPolicies:
    object: str
    id: str
    type: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationTeamsListOutputItemsProjectsProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationTeamsListOutputItemsProjects:
    id: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationTeamsListOutputItemsProjectsProject
@dataclass
class ManagementOrganizationTeamsListOutputItems:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    policies: List[ManagementOrganizationTeamsListOutputItemsPolicies]
    projects: List[ManagementOrganizationTeamsListOutputItemsProjects]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementOrganizationTeamsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationTeamsListOutput:
    items: List[ManagementOrganizationTeamsListOutputItems]
    pagination: ManagementOrganizationTeamsListOutputPagination


class mapManagementOrganizationTeamsListOutputItemsPolicies:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutputItemsPolicies:
        return ManagementOrganizationTeamsListOutputItemsPolicies(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListOutputItemsPolicies, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsListOutputItemsProjectsProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutputItemsProjectsProject:
        return ManagementOrganizationTeamsListOutputItemsProjectsProject(
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
    def to_dict(value: Union[ManagementOrganizationTeamsListOutputItemsProjectsProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsListOutputItemsProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutputItemsProjects:
        return ManagementOrganizationTeamsListOutputItemsProjects(
        id=data.get('id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationTeamsListOutputItemsProjectsProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListOutputItemsProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutputItems:
        return ManagementOrganizationTeamsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        policies=[mapManagementOrganizationTeamsListOutputItemsPolicies.from_dict(item) for item in data.get('policies', []) if item],
        projects=[mapManagementOrganizationTeamsListOutputItemsProjects.from_dict(item) for item in data.get('projects', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutputPagination:
        return ManagementOrganizationTeamsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationTeamsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListOutput:
        return ManagementOrganizationTeamsListOutput(
        items=[mapManagementOrganizationTeamsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationTeamsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationTeamsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationTeamsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationTeamsListQuery:
        return ManagementOrganizationTeamsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationTeamsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

