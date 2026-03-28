from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesCreateOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesCreateOutputDocument:
    access: List[ManagementOrganizationAccessPoliciesCreateOutputDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesCreateOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationAccessPoliciesCreateOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesCreateOutputInstances:
    id: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesCreateOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: ManagementOrganizationAccessPoliciesCreateOutputDocument
    roles: List[ManagementOrganizationAccessPoliciesCreateOutputRoles]
    projects: List[ManagementOrganizationAccessPoliciesCreateOutputProjects]
    instances: List[ManagementOrganizationAccessPoliciesCreateOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationAccessPoliciesCreateOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutputDocumentAccess:
        return ManagementOrganizationAccessPoliciesCreateOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutputDocument:
        return ManagementOrganizationAccessPoliciesCreateOutputDocument(
        access=[mapManagementOrganizationAccessPoliciesCreateOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutputRoles:
        return ManagementOrganizationAccessPoliciesCreateOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutputProjects:
        return ManagementOrganizationAccessPoliciesCreateOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutputInstances:
        return ManagementOrganizationAccessPoliciesCreateOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateOutput:
        return ManagementOrganizationAccessPoliciesCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesCreateOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapManagementOrganizationAccessPoliciesCreateOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapManagementOrganizationAccessPoliciesCreateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapManagementOrganizationAccessPoliciesCreateOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessPoliciesCreateBodyDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesCreateBodyDocument:
    access: List[ManagementOrganizationAccessPoliciesCreateBodyDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesCreateBody:
    name: str
    document: ManagementOrganizationAccessPoliciesCreateBodyDocument
    description: Optional[str] = None
    message: Optional[str] = None


class mapManagementOrganizationAccessPoliciesCreateBodyDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateBodyDocumentAccess:
        return ManagementOrganizationAccessPoliciesCreateBodyDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateBodyDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateBodyDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateBodyDocument:
        return ManagementOrganizationAccessPoliciesCreateBodyDocument(
        access=[mapManagementOrganizationAccessPoliciesCreateBodyDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateBodyDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesCreateBody:
        return ManagementOrganizationAccessPoliciesCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesCreateBodyDocument.from_dict(data.get('document')) if data.get('document') else None,
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

