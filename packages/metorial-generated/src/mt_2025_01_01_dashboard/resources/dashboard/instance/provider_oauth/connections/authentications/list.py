from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
    code: str
    message: Optional[str] = None
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
    id: str
    type: str
    metadata: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
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
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
    object: str
    id: str
    status: str
    events: List[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents]
    connection_id: str
    created_at: datetime
    error: Optional[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError] = None
    profile: Optional[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile] = None
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput:
    items: List[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems]
    pagination: DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination


class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents(
        id=data.get('id'),
        type=data.get('type'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile(
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
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        events=[mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents.from_dict(item) for item in data.get('events', []) if item],
        connection_id=data.get('connection_id'),
        profile=mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile.from_dict(data.get('profile')) if data.get('profile') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput(
        items=[mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceProviderOauthConnectionsAuthenticationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceProviderOauthConnectionsAuthenticationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery:
        return DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderOauthConnectionsAuthenticationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

