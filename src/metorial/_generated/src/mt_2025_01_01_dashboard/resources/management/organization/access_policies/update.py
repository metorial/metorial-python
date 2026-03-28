from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutputDocument:
    access: List[ManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutputInstances:
    id: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesUpdateOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: ManagementOrganizationAccessPoliciesUpdateOutputDocument
    roles: List[ManagementOrganizationAccessPoliciesUpdateOutputRoles]
    projects: List[ManagementOrganizationAccessPoliciesUpdateOutputProjects]
    instances: List[ManagementOrganizationAccessPoliciesUpdateOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess:
        return ManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutputDocument:
        return ManagementOrganizationAccessPoliciesUpdateOutputDocument(
        access=[mapManagementOrganizationAccessPoliciesUpdateOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutputRoles:
        return ManagementOrganizationAccessPoliciesUpdateOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutputProjects:
        return ManagementOrganizationAccessPoliciesUpdateOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutputInstances:
        return ManagementOrganizationAccessPoliciesUpdateOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateOutput:
        return ManagementOrganizationAccessPoliciesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesUpdateOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapManagementOrganizationAccessPoliciesUpdateOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapManagementOrganizationAccessPoliciesUpdateOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapManagementOrganizationAccessPoliciesUpdateOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesUpdateBodyDocument:
    access: List[ManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    document: Optional[ManagementOrganizationAccessPoliciesUpdateBodyDocument] = None
    message: Optional[str] = None


class mapManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess:
        return ManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateBodyDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateBodyDocument:
        return ManagementOrganizationAccessPoliciesUpdateBodyDocument(
        access=[mapManagementOrganizationAccessPoliciesUpdateBodyDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateBodyDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesUpdateBody:
        return ManagementOrganizationAccessPoliciesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesUpdateBodyDocument.from_dict(data.get('document')) if data.get('document') else None,
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

