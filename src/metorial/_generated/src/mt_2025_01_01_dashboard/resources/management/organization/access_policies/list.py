from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesListOutputItemsDocument:
    access: List[ManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesListOutputItemsRoles:
    id: str
    name: str
    slug: str
@dataclass
class ManagementOrganizationAccessPoliciesListOutputItemsProjects:
    id: str
    slug: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesListOutputItemsInstances:
    id: str
    name: str
@dataclass
class ManagementOrganizationAccessPoliciesListOutputItems:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: ManagementOrganizationAccessPoliciesListOutputItemsDocument
    roles: List[ManagementOrganizationAccessPoliciesListOutputItemsRoles]
    projects: List[ManagementOrganizationAccessPoliciesListOutputItemsProjects]
    instances: List[ManagementOrganizationAccessPoliciesListOutputItemsInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementOrganizationAccessPoliciesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationAccessPoliciesListOutput:
    items: List[ManagementOrganizationAccessPoliciesListOutputItems]
    pagination: ManagementOrganizationAccessPoliciesListOutputPagination


class mapManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess:
        return ManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItemsDocument:
        return ManagementOrganizationAccessPoliciesListOutputItemsDocument(
        access=[mapManagementOrganizationAccessPoliciesListOutputItemsDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputItemsRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItemsRoles:
        return ManagementOrganizationAccessPoliciesListOutputItemsRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItemsRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputItemsProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItemsProjects:
        return ManagementOrganizationAccessPoliciesListOutputItemsProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItemsProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputItemsInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItemsInstances:
        return ManagementOrganizationAccessPoliciesListOutputItemsInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItemsInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputItems:
        return ManagementOrganizationAccessPoliciesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapManagementOrganizationAccessPoliciesListOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapManagementOrganizationAccessPoliciesListOutputItemsRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapManagementOrganizationAccessPoliciesListOutputItemsProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapManagementOrganizationAccessPoliciesListOutputItemsInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutputPagination:
        return ManagementOrganizationAccessPoliciesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListOutput:
        return ManagementOrganizationAccessPoliciesListOutput(
        items=[mapManagementOrganizationAccessPoliciesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationAccessPoliciesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessPoliciesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationAccessPoliciesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesListQuery:
        return ManagementOrganizationAccessPoliciesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

