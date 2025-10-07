from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderOauthConnectionsProfilesListOutputItems:
    object: str
    id: str
    status: str
    sub: str
    connection_id: str
    created_at: datetime
    last_used_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    email: Optional[str] = None
@dataclass
class DashboardInstanceProviderOauthConnectionsProfilesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderOauthConnectionsProfilesListOutput:
    items: List[DashboardInstanceProviderOauthConnectionsProfilesListOutputItems]
    pagination: DashboardInstanceProviderOauthConnectionsProfilesListOutputPagination


class mapDashboardInstanceProviderOauthConnectionsProfilesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsProfilesListOutputItems:
        return DashboardInstanceProviderOauthConnectionsProfilesListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        sub=data.get('sub'),
        name=data.get('name'),
        email=data.get('email'),
        connection_id=data.get('connection_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at')) if data.get('last_used_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsProfilesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsProfilesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsProfilesListOutputPagination:
        return DashboardInstanceProviderOauthConnectionsProfilesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsProfilesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsProfilesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsProfilesListOutput:
        return DashboardInstanceProviderOauthConnectionsProfilesListOutput(
        items=[mapDashboardInstanceProviderOauthConnectionsProfilesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderOauthConnectionsProfilesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsProfilesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderOauthConnectionsProfilesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceProviderOauthConnectionsProfilesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsProfilesListQuery:
        return DashboardInstanceProviderOauthConnectionsProfilesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsProfilesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

