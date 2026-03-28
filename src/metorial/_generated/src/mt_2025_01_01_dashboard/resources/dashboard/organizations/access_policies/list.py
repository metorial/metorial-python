from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItemsDocument:
    access: List[DashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItemsRoles:
    id: str
    name: str
    slug: str
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItemsProjects:
    id: str
    slug: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItemsInstances:
    id: str
    name: str
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputItems:
    object: str
    id: str
    organization_id: str
    type: str
    name: str
    slug: str
    document: DashboardOrganizationsAccessPoliciesListOutputItemsDocument
    roles: List[DashboardOrganizationsAccessPoliciesListOutputItemsRoles]
    projects: List[DashboardOrganizationsAccessPoliciesListOutputItemsProjects]
    instances: List[DashboardOrganizationsAccessPoliciesListOutputItemsInstances]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardOrganizationsAccessPoliciesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsAccessPoliciesListOutput:
    items: List[DashboardOrganizationsAccessPoliciesListOutputItems]
    pagination: DashboardOrganizationsAccessPoliciesListOutputPagination


class mapDashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess:
        return DashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItemsDocument:
        return DashboardOrganizationsAccessPoliciesListOutputItemsDocument(
        access=[mapDashboardOrganizationsAccessPoliciesListOutputItemsDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputItemsRoles:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItemsRoles:
        return DashboardOrganizationsAccessPoliciesListOutputItemsRoles(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItemsRoles, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputItemsProjects:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItemsProjects:
        return DashboardOrganizationsAccessPoliciesListOutputItemsProjects(
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItemsProjects, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputItemsInstances:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItemsInstances:
        return DashboardOrganizationsAccessPoliciesListOutputItemsInstances(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItemsInstances, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputItems:
        return DashboardOrganizationsAccessPoliciesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        document=mapDashboardOrganizationsAccessPoliciesListOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        roles=[mapDashboardOrganizationsAccessPoliciesListOutputItemsRoles.from_dict(item) for item in data.get('roles', []) if item],
        projects=[mapDashboardOrganizationsAccessPoliciesListOutputItemsProjects.from_dict(item) for item in data.get('projects', []) if item],
        instances=[mapDashboardOrganizationsAccessPoliciesListOutputItemsInstances.from_dict(item) for item in data.get('instances', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutputPagination:
        return DashboardOrganizationsAccessPoliciesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListOutput:
        return DashboardOrganizationsAccessPoliciesListOutput(
        items=[mapDashboardOrganizationsAccessPoliciesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsAccessPoliciesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessPoliciesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesListQuery:
        return DashboardOrganizationsAccessPoliciesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

