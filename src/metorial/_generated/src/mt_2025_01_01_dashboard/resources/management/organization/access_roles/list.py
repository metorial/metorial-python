from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessRolesListOutputItems:
    object: str
    id: str
    organization_id: str
    name: str
    slug: str
    is_admin: bool
    scopes: List[str]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementOrganizationAccessRolesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationAccessRolesListOutput:
    items: List[ManagementOrganizationAccessRolesListOutputItems]
    pagination: ManagementOrganizationAccessRolesListOutputPagination


class mapManagementOrganizationAccessRolesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesListOutputItems:
        return ManagementOrganizationAccessRolesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        is_admin=data.get('is_admin'),
        scopes=data.get('scopes', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessRolesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesListOutputPagination:
        return ManagementOrganizationAccessRolesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessRolesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesListOutput:
        return ManagementOrganizationAccessRolesListOutput(
        items=[mapManagementOrganizationAccessRolesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationAccessRolesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessRolesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationAccessRolesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesListQuery:
        return ManagementOrganizationAccessRolesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

