from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutputDocument:
    access: List[ManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutputRoles:
    id: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutputProjects:
    id: str
    slug: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutputInstances:
    id: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesDeleteOutput:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: ManagementOrganizationAccessPoliciesDeleteOutputDocument
    roles: List[ManagementOrganizationAccessPoliciesDeleteOutputRoles]
    projects: List[ManagementOrganizationAccessPoliciesDeleteOutputProjects]
    instances: List[ManagementOrganizationAccessPoliciesDeleteOutputInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None


class mapManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess:
        return ManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesDeleteOutputDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutputDocument:
        return ManagementOrganizationAccessPoliciesDeleteOutputDocument(
        access=[mapManagementOrganizationAccessPoliciesDeleteOutputDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutputDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesDeleteOutputRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutputRoles:
        return ManagementOrganizationAccessPoliciesDeleteOutputRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutputRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesDeleteOutputProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutputProjects:
        return ManagementOrganizationAccessPoliciesDeleteOutputProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutputProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesDeleteOutputInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutputInstances:
        return ManagementOrganizationAccessPoliciesDeleteOutputInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutputInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesDeleteOutput:
        return ManagementOrganizationAccessPoliciesDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesDeleteOutputDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapManagementOrganizationAccessPoliciesDeleteOutputRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapManagementOrganizationAccessPoliciesDeleteOutputProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapManagementOrganizationAccessPoliciesDeleteOutputInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

