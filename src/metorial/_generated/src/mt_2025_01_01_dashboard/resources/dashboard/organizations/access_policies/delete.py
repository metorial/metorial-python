from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutputDocument:
    access: List[DashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutputInstances:
    id: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesDeleteOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: DashboardOrganizationsAccessPoliciesDeleteOutputDocument
    roles: List[DashboardOrganizationsAccessPoliciesDeleteOutputRoles]
    projects: List[DashboardOrganizationsAccessPoliciesDeleteOutputProjects]
    instances: List[DashboardOrganizationsAccessPoliciesDeleteOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess:
        return DashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesDeleteOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutputDocument:
        return DashboardOrganizationsAccessPoliciesDeleteOutputDocument(
        access=[mapDashboardOrganizationsAccessPoliciesDeleteOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesDeleteOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutputRoles:
        return DashboardOrganizationsAccessPoliciesDeleteOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesDeleteOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutputProjects:
        return DashboardOrganizationsAccessPoliciesDeleteOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesDeleteOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutputInstances:
        return DashboardOrganizationsAccessPoliciesDeleteOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesDeleteOutput:
        return DashboardOrganizationsAccessPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesDeleteOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapDashboardOrganizationsAccessPoliciesDeleteOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapDashboardOrganizationsAccessPoliciesDeleteOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapDashboardOrganizationsAccessPoliciesDeleteOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

