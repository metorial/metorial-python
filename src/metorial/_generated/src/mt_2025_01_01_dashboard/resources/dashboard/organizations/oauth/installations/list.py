from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser:
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
class DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor] = None
    instance: Optional[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance] = None
    organization: Optional[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization] = None
    user: Optional[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser] = None
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputItems:
    object: str
    id: str
    status: str
    scopes: List[DashboardOrganizationsOauthInstallationsListOutputItemsScopes]
    organization_id: str
    oauth_application: DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication
    created_at: datetime
    updated_at: datetime
    server_side_machine_access: Optional[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess] = None
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthInstallationsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsOauthInstallationsListOutput:
    items: List[DashboardOrganizationsOauthInstallationsListOutputItems]
    pagination: DashboardOrganizationsOauthInstallationsListOutputPagination


class mapDashboardOrganizationsOauthInstallationsListOutputItemsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsScopes:
        return DashboardOrganizationsOauthInstallationsListOutputItemsScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes:
        return DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets:
        return DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication:
        return DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        slug=data.get('slug'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser(
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
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess:
        return DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputItems:
        return DashboardOrganizationsOauthInstallationsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        scopes=[mapDashboardOrganizationsOauthInstallationsListOutputItemsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        organization_id=data.get('organization_id'),
        oauth_application=mapDashboardOrganizationsOauthInstallationsListOutputItemsOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        server_side_machine_access=mapDashboardOrganizationsOauthInstallationsListOutputItemsServerSideMachineAccess.from_dict(data.get('server_side_machine_access')) if data.get('server_side_machine_access') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutputPagination:
        return DashboardOrganizationsOauthInstallationsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListOutput:
        return DashboardOrganizationsOauthInstallationsListOutput(
        items=[mapDashboardOrganizationsOauthInstallationsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsOauthInstallationsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsOauthInstallationsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    app_id: Optional[Union[str, List[str]]] = None


class mapDashboardOrganizationsOauthInstallationsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsListQuery:
        return DashboardOrganizationsOauthInstallationsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        status=data.get('status'),
        app_id=data.get('app_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

