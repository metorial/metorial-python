from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationOauthAppsListOutputItemsScopes:
    identifier: str
    name: str
    description: str
@dataclass
class ManagementOrganizationOauthAppsListOutputItemsClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationOauthAppsListOutputItems:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[ManagementOrganizationOauthAppsListOutputItemsScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[ManagementOrganizationOauthAppsListOutputItemsClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class ManagementOrganizationOauthAppsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationOauthAppsListOutput:
    items: List[ManagementOrganizationOauthAppsListOutputItems]
    pagination: ManagementOrganizationOauthAppsListOutputPagination


class mapManagementOrganizationOauthAppsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListOutputItemsScopes:
        return ManagementOrganizationOauthAppsListOutputItemsScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOauthAppsListOutputItemsClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListOutputItemsClientSecrets:
        return ManagementOrganizationOauthAppsListOutputItemsClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListOutputItemsClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOauthAppsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListOutputItems:
        return ManagementOrganizationOauthAppsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapManagementOrganizationOauthAppsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapManagementOrganizationOauthAppsListOutputItemsClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOauthAppsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListOutputPagination:
        return ManagementOrganizationOauthAppsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationOauthAppsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListOutput:
        return ManagementOrganizationOauthAppsListOutput(
        items=[mapManagementOrganizationOauthAppsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationOauthAppsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationOauthAppsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None


class mapManagementOrganizationOauthAppsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationOauthAppsListQuery:
        return ManagementOrganizationOauthAppsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationOauthAppsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

