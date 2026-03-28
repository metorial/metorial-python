from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess:
    target: str
    scopes: Optional[List[str]] = None
    roles: Optional[List[str]] = None
@dataclass
class ManagementOrganizationAccessPoliciesVersionsOutputItemsDocument:
    access: List[ManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess]
@dataclass
class ManagementOrganizationAccessPoliciesVersionsOutputItems:
    object: str
    id: str
    access_policy_id: str
    index: float
    document: ManagementOrganizationAccessPoliciesVersionsOutputItemsDocument
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementOrganizationAccessPoliciesVersionsOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationAccessPoliciesVersionsOutput:
    items: List[ManagementOrganizationAccessPoliciesVersionsOutputItems]
    pagination: ManagementOrganizationAccessPoliciesVersionsOutputPagination


class mapManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess:
        return ManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess(
        target=data.get('target'),
        scopes=data.get('scopes', []),
        roles=data.get('roles', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesVersionsOutputItemsDocument:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsOutputItemsDocument:
        return ManagementOrganizationAccessPoliciesVersionsOutputItemsDocument(
        access=[mapManagementOrganizationAccessPoliciesVersionsOutputItemsDocumentAccess.from_dict(item) for item in data.get('access', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsOutputItemsDocument, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesVersionsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsOutputItems:
        return ManagementOrganizationAccessPoliciesVersionsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access_policy_id=data.get('access_policy_id'),
        index=data.get('index'),
        message=data.get('message'),
        document=mapManagementOrganizationAccessPoliciesVersionsOutputItemsDocument.from_dict(data.get('document')) if data.get('document') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesVersionsOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsOutputPagination:
        return ManagementOrganizationAccessPoliciesVersionsOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessPoliciesVersionsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsOutput:
        return ManagementOrganizationAccessPoliciesVersionsOutput(
        items=[mapManagementOrganizationAccessPoliciesVersionsOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationAccessPoliciesVersionsOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessPoliciesVersionsQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationAccessPoliciesVersionsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessPoliciesVersionsQuery:
        return ManagementOrganizationAccessPoliciesVersionsQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessPoliciesVersionsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

