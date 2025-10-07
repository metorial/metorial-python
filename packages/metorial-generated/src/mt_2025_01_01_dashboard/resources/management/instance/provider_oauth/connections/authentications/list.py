from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
    code: str
    message: Optional[str] = None
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
    id: str
    type: str
    metadata: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
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
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
    object: str
    id: str
    status: str
    events: List[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents]
    connection_id: str
    created_at: datetime
    error: Optional[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError] = None
    profile: Optional[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile] = None
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListOutput:
    items: List[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems]
    pagination: ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination


class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError(
        code=data.get('code'),
        message=data.get('message')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents(
        id=data.get('id'),
        type=data.get('type'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile(
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
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        error=mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsError.from_dict(data.get('error')) if data.get('error') else None,
        events=[mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsEvents.from_dict(item) for item in data.get('events', []) if item],
        connection_id=data.get('connection_id'),
        profile=mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItemsProfile.from_dict(data.get('profile')) if data.get('profile') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListOutput:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListOutput(
        items=[mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderOauthConnectionsAuthenticationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderOauthConnectionsAuthenticationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceProviderOauthConnectionsAuthenticationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderOauthConnectionsAuthenticationsListQuery:
        return ManagementInstanceProviderOauthConnectionsAuthenticationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderOauthConnectionsAuthenticationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

