from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutputDocument:
    access: List[DashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutputInstances:
    id: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesCreateOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: DashboardOrganizationsAccessPoliciesCreateOutputDocument
    roles: List[DashboardOrganizationsAccessPoliciesCreateOutputRoles]
    projects: List[DashboardOrganizationsAccessPoliciesCreateOutputProjects]
    instances: List[DashboardOrganizationsAccessPoliciesCreateOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess:
        return DashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutputDocument:
        return DashboardOrganizationsAccessPoliciesCreateOutputDocument(
        access=[mapDashboardOrganizationsAccessPoliciesCreateOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutputRoles:
        return DashboardOrganizationsAccessPoliciesCreateOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutputProjects:
        return DashboardOrganizationsAccessPoliciesCreateOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutputInstances:
        return DashboardOrganizationsAccessPoliciesCreateOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateOutput:
        return DashboardOrganizationsAccessPoliciesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesCreateOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapDashboardOrganizationsAccessPoliciesCreateOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapDashboardOrganizationsAccessPoliciesCreateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapDashboardOrganizationsAccessPoliciesCreateOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesCreateBodyDocument:
    access: List[DashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesCreateBody:
    name: str
    document: DashboardOrganizationsAccessPoliciesCreateBodyDocument
    description: Optional[str] = None
    message: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess:
        return DashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateBodyDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateBodyDocument:
        return DashboardOrganizationsAccessPoliciesCreateBodyDocument(
        access=[mapDashboardOrganizationsAccessPoliciesCreateBodyDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateBodyDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesCreateBody:
        return DashboardOrganizationsAccessPoliciesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesCreateBodyDocument.from_dict(data.get('document')) if data.get('document') else None,
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

