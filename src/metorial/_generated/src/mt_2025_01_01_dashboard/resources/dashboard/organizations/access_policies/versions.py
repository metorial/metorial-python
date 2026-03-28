from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument:
    access: List[DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess]
@dataclass
class DashboardOrganizationsAccessPoliciesVersionsOutputItems:
    object: str
    id: str
    access_policy_id: str
    index: float
    document: DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument
    created_at: datetime
    message: Optional[str] = None
@dataclass
class DashboardOrganizationsAccessPoliciesVersionsOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsAccessPoliciesVersionsOutput:
    items: List[DashboardOrganizationsAccessPoliciesVersionsOutputItems]
    pagination: DashboardOrganizationsAccessPoliciesVersionsOutputPagination


class mapDashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess:
        return DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument:
        return DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument(
        access=[mapDashboardOrganizationsAccessPoliciesVersionsOutputItemsDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesVersionsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsOutputItems:
        return DashboardOrganizationsAccessPoliciesVersionsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access_policy_id=data.get('access_policy_id'),
        index=data.get('index'),
        message=data.get('message'),
        document=mapDashboardOrganizationsAccessPoliciesVersionsOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesVersionsOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsOutputPagination:
        return DashboardOrganizationsAccessPoliciesVersionsOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsAccessPoliciesVersionsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsOutput:
        return DashboardOrganizationsAccessPoliciesVersionsOutput(
        items=[mapDashboardOrganizationsAccessPoliciesVersionsOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsAccessPoliciesVersionsOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsAccessPoliciesVersionsQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardOrganizationsAccessPoliciesVersionsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsAccessPoliciesVersionsQuery:
        return DashboardOrganizationsAccessPoliciesVersionsQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsAccessPoliciesVersionsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

