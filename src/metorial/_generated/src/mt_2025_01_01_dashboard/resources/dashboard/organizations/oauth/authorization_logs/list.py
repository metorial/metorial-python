from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser:
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
class DashboardOrganizationsOauthAuthorizationLogsListOutputItems:
    object: str
    id: str
    status: str
    type: str
    organization_id: str
    scopes: List[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes]
    oauth_application: DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication
    created_at: datetime
    redirect_uri: Optional[str] = None
    client_ip: Optional[str] = None
    actor: Optional[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor] = None
    user: Optional[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser] = None
    accepted_at: Optional[datetime] = None
    denied_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListOutput:
    items: List[DashboardOrganizationsOauthAuthorizationLogsListOutputItems]
    pagination: DashboardOrganizationsOauthAuthorizationLogsListOutputPagination


class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser(
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
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputItems:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        redirect_uri=data.get('redirect_uri'),
        client_ip=data.get('client_ip'),
        scopes=[mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        oauth_application=mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        actor=mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        user=mapDashboardOrganizationsOauthAuthorizationLogsListOutputItemsUser.from_dict(data.get('user')) if data.get('user') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        accepted_at=datetime.fromisoformat(data.get('accepted_at').replace('Z', '+00:00')) if data.get('accepted_at') else None,
        denied_at=datetime.fromisoformat(data.get('denied_at').replace('Z', '+00:00')) if data.get('denied_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutputPagination:
        return DashboardOrganizationsOauthAuthorizationLogsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationLogsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListOutput:
        return DashboardOrganizationsOauthAuthorizationLogsListOutput(
        items=[mapDashboardOrganizationsOauthAuthorizationLogsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsOauthAuthorizationLogsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOauthAuthorizationLogsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    app_id: Optional[Union[str, List[str]]] = None
    user_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsOauthAuthorizationLogsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationLogsListQuery:
        return DashboardOrganizationsOauthAuthorizationLogsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        app_id=data.get('app_id'),
        user_id=data.get('user_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationLogsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

