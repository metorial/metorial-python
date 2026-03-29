from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationAccessRolesVersionsOutputItems:
    object: str
    id: str
    access_role_id: str
    index: float
    scopes: List[str]
    scopes_added: List[str]
    scopes_removed: List[str]
    created_at: datetime
    message: Optional[str] = None
@dataclass
class ManagementOrganizationAccessRolesVersionsOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationAccessRolesVersionsOutput:
    items: List[ManagementOrganizationAccessRolesVersionsOutputItems]
    pagination: ManagementOrganizationAccessRolesVersionsOutputPagination


class mapManagementOrganizationAccessRolesVersionsOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesVersionsOutputItems:
        return ManagementOrganizationAccessRolesVersionsOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        access_role_id=data.get('access_role_id'),
        index=data.get('index'),
        scopes=data.get('scopes', []),
        scopes_added=data.get('scopes_added', []),
        scopes_removed=data.get('scopes_removed', []),
        message=data.get('message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesVersionsOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessRolesVersionsOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesVersionsOutputPagination:
        return ManagementOrganizationAccessRolesVersionsOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesVersionsOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationAccessRolesVersionsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesVersionsOutput:
        return ManagementOrganizationAccessRolesVersionsOutput(
        items=[mapManagementOrganizationAccessRolesVersionsOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationAccessRolesVersionsOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesVersionsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationAccessRolesVersionsQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementOrganizationAccessRolesVersionsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationAccessRolesVersionsQuery:
        return ManagementOrganizationAccessRolesVersionsQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationAccessRolesVersionsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

