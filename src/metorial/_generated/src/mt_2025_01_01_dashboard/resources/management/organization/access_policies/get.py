from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesGetOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesGetOutputDocument:
    access: List[ManagementOrganizationAccessPoliciesGetOutputDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesGetOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationAccessPoliciesGetOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesGetOutputInstances:
    id: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesGetOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: ManagementOrganizationAccessPoliciesGetOutputDocument
    roles: List[ManagementOrganizationAccessPoliciesGetOutputRoles]
    projects: List[ManagementOrganizationAccessPoliciesGetOutputProjects]
    instances: List[ManagementOrganizationAccessPoliciesGetOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationAccessPoliciesGetOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutputDocumentAccess:
        return ManagementOrganizationAccessPoliciesGetOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesGetOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutputDocument:
        return ManagementOrganizationAccessPoliciesGetOutputDocument(
        access=[mapManagementOrganizationAccessPoliciesGetOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesGetOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutputRoles:
        return ManagementOrganizationAccessPoliciesGetOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesGetOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutputProjects:
        return ManagementOrganizationAccessPoliciesGetOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesGetOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutputInstances:
        return ManagementOrganizationAccessPoliciesGetOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesGetOutput:
        return ManagementOrganizationAccessPoliciesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesGetOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapManagementOrganizationAccessPoliciesGetOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapManagementOrganizationAccessPoliciesGetOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapManagementOrganizationAccessPoliciesGetOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

