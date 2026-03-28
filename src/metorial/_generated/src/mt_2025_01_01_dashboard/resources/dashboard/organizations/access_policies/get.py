from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesGetOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesGetOutputDocument:
    access: List[DashboardOrganizationsAccessPoliciesGetOutputDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesGetOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsAccessPoliciesGetOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesGetOutputInstances:
    id: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesGetOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: DashboardOrganizationsAccessPoliciesGetOutputDocument
    roles: List[DashboardOrganizationsAccessPoliciesGetOutputRoles]
    projects: List[DashboardOrganizationsAccessPoliciesGetOutputProjects]
    instances: List[DashboardOrganizationsAccessPoliciesGetOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesGetOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutputDocumentAccess:
        return DashboardOrganizationsAccessPoliciesGetOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesGetOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutputDocument:
        return DashboardOrganizationsAccessPoliciesGetOutputDocument(
        access=[mapDashboardOrganizationsAccessPoliciesGetOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesGetOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutputRoles:
        return DashboardOrganizationsAccessPoliciesGetOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesGetOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutputProjects:
        return DashboardOrganizationsAccessPoliciesGetOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesGetOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutputInstances:
        return DashboardOrganizationsAccessPoliciesGetOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesGetOutput:
        return DashboardOrganizationsAccessPoliciesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesGetOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapDashboardOrganizationsAccessPoliciesGetOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapDashboardOrganizationsAccessPoliciesGetOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapDashboardOrganizationsAccessPoliciesGetOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

