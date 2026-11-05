from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumerOauthAuthorizationsListOutputItemsScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ConsumerOauthAuthorizationsListOutputItemsOauthApplication:
    id: str
    name: str
    image_url: str
    description: Optional[str] = None
    website_url: Optional[str] = None
@dataclass
class ConsumerOauthAuthorizationsListOutputItems:
    object: str
    id: str
    status: str
    scopes: List[ConsumerOauthAuthorizationsListOutputItemsScopes]
    oauth_application: ConsumerOauthAuthorizationsListOutputItemsOauthApplication
    created_at: datetime
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class ConsumerOauthAuthorizationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ConsumerOauthAuthorizationsListOutput:
    items: List[ConsumerOauthAuthorizationsListOutputItems]
    pagination: ConsumerOauthAuthorizationsListOutputPagination


class mapConsumerOauthAuthorizationsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListOutputItemsScopes:
        return ConsumerOauthAuthorizationsListOutputItemsScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsListOutputItemsOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListOutputItemsOauthApplication:
        return ConsumerOauthAuthorizationsListOutputItemsOauthApplication(
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        website_url=data.get('website_url')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListOutputItemsOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListOutputItems:
        return ConsumerOauthAuthorizationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        scopes=[mapConsumerOauthAuthorizationsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        oauth_application=mapConsumerOauthAuthorizationsListOutputItemsOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListOutputPagination:
        return ConsumerOauthAuthorizationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumerOauthAuthorizationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListOutput:
        return ConsumerOauthAuthorizationsListOutput(
        items=[mapConsumerOauthAuthorizationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapConsumerOauthAuthorizationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumerOauthAuthorizationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapConsumerOauthAuthorizationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumerOauthAuthorizationsListQuery:
        return ConsumerOauthAuthorizationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ConsumerOauthAuthorizationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

