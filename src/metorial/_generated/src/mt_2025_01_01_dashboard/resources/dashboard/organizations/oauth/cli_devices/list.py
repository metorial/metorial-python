from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthCliDevicesListOutputItemsUser:
    object: str
    id: str
    status: str
    type: str
    email: str
    name: str
    first_name: str
    last_name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthCliDevicesListOutputItems:
    object: str
    id: str
    ip: str
    organization_id: str
    oauth_authorization_id: str
    created_at: datetime
    updated_at: datetime
    user: DashboardOrganizationsOauthCliDevicesListOutputItemsUser
@dataclass
class DashboardOrganizationsOauthCliDevicesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsOauthCliDevicesListOutput:
    items: List[DashboardOrganizationsOauthCliDevicesListOutputItems]
    pagination: DashboardOrganizationsOauthCliDevicesListOutputPagination


class mapDashboardOrganizationsOauthCliDevicesListOutputItemsUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthCliDevicesListOutputItemsUser:
        return DashboardOrganizationsOauthCliDevicesListOutputItemsUser(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        email=data.get('email'),
        name=data.get('name'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthCliDevicesListOutputItemsUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthCliDevicesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthCliDevicesListOutputItems:
        return DashboardOrganizationsOauthCliDevicesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        organization_id=data.get('organization_id'),
        oauth_authorization_id=data.get('oauth_authorization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        user=mapDashboardOrganizationsOauthCliDevicesListOutputItemsUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthCliDevicesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthCliDevicesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthCliDevicesListOutputPagination:
        return DashboardOrganizationsOauthCliDevicesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthCliDevicesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthCliDevicesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthCliDevicesListOutput:
        return DashboardOrganizationsOauthCliDevicesListOutput(
        items=[mapDashboardOrganizationsOauthCliDevicesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsOauthCliDevicesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthCliDevicesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOauthCliDevicesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardOrganizationsOauthCliDevicesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthCliDevicesListQuery:
        return DashboardOrganizationsOauthCliDevicesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthCliDevicesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

