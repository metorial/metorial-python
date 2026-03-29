from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser:
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
class DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor] = None
    instance: Optional[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance] = None
    organization: Optional[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization] = None
    user: Optional[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser] = None
@dataclass
class DashboardOrganizationsOauthAuthorizationsGetOutput:
    object: str
    id: str
    status: str
    type: str
    scopes: List[DashboardOrganizationsOauthAuthorizationsGetOutputScopes]
    organization_id: str
    oauth_application_id: str
    oauth_installation_id: str
    oauth_application: DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication
    machine_access: DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
    organization_member_id: Optional[str] = None
    requesting_ip: Optional[str] = None
    accepting_ip: Optional[str] = None
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapDashboardOrganizationsOauthAuthorizationsGetOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputScopes:
        return DashboardOrganizationsOauthAuthorizationsGetOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes:
        return DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets:
        return DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication:
        return DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject(
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
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization(
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
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser(
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
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess:
        return DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthAuthorizationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthAuthorizationsGetOutput:
        return DashboardOrganizationsOauthAuthorizationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        scopes=[mapDashboardOrganizationsOauthAuthorizationsGetOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        organization_id=data.get('organization_id'),
        oauth_application_id=data.get('oauth_application_id'),
        oauth_installation_id=data.get('oauth_installation_id'),
        user_id=data.get('user_id'),
        organization_member_id=data.get('organization_member_id'),
        oauth_application=mapDashboardOrganizationsOauthAuthorizationsGetOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        machine_access=mapDashboardOrganizationsOauthAuthorizationsGetOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        requesting_ip=data.get('requesting_ip'),
        accepting_ip=data.get('accepting_ip'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthAuthorizationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

