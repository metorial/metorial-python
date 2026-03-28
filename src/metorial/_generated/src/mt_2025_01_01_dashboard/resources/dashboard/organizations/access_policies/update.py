from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutputDocument:
    access: List[DashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutputInstances:
    id: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: DashboardOrganizationsAccessPoliciesUpdateOutputDocument
    roles: List[DashboardOrganizationsAccessPoliciesUpdateOutputRoles]
    projects: List[DashboardOrganizationsAccessPoliciesUpdateOutputProjects]
    instances: List[DashboardOrganizationsAccessPoliciesUpdateOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess:
        return DashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutputDocument:
        return DashboardOrganizationsAccessPoliciesUpdateOutputDocument(
        access=[mapDashboardOrganizationsAccessPoliciesUpdateOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutputRoles:
        return DashboardOrganizationsAccessPoliciesUpdateOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutputProjects:
        return DashboardOrganizationsAccessPoliciesUpdateOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutputInstances:
        return DashboardOrganizationsAccessPoliciesUpdateOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateOutput:
        return DashboardOrganizationsAccessPoliciesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesUpdateOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapDashboardOrganizationsAccessPoliciesUpdateOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapDashboardOrganizationsAccessPoliciesUpdateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapDashboardOrganizationsAccessPoliciesUpdateOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateBodyDocument:
    access: List[DashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    document: Optional[DashboardOrganizationsAccessPoliciesUpdateBodyDocument] = None
    message: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess:
        return DashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateBodyDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateBodyDocument:
        return DashboardOrganizationsAccessPoliciesUpdateBodyDocument(
        access=[mapDashboardOrganizationsAccessPoliciesUpdateBodyDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateBodyDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesUpdateBody:
        return DashboardOrganizationsAccessPoliciesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesUpdateBodyDocument.from_dict(data.get('document')) if data.get('document') else None,
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

