from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes:
    identifier: str
    name: str
    description: str
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets:
    object: str
    id: str
    preview: str
    created_at: datetime
    secret: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication:
    object: str
    id: str
    status: str
    type: str
    access_level: str
    allow_token_exchange_without_client_secret: bool
    name: str
    scopes: List[DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes]
    image_url: str
    redirect_uris: List[str]
    client_id: str
    client_secrets: List[DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    website_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    terms_of_service_url: Optional[str] = None
    organization_id: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser:
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
class DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor] = None
    instance: Optional[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance] = None
    organization: Optional[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization] = None
    user: Optional[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser] = None
@dataclass
class DashboardOrganizationsOauthInstallationsRevokeOutput:
    object: str
    id: str
    status: str
    scopes: List[DashboardOrganizationsOauthInstallationsRevokeOutputScopes]
    organization_id: str
    oauth_application: DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication
    created_at: datetime
    updated_at: datetime
    server_side_machine_access: Optional[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess] = None
    last_used_at: Optional[datetime] = None
    revoked_at: Optional[datetime] = None


class mapDashboardOrganizationsOauthInstallationsRevokeOutputScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputScopes:
        return DashboardOrganizationsOauthInstallationsRevokeOutputScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes:
        return DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes(
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets:
        return DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets(
        object=data.get('object'),
        id=data.get('id'),
        preview=data.get('preview'),
        secret=data.get('secret'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication:
        return DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        access_level=data.get('access_level'),
        allow_token_exchange_without_client_secret=data.get('allow_token_exchange_without_client_secret'),
        name=data.get('name'),
        description=data.get('description'),
        scopes=[mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationScopes.from_dict(item) for item in data.get('scopes', []) if item],
        image_url=data.get('image_url'),
        website_url=data.get('website_url'),
        privacy_policy_url=data.get('privacy_policy_url'),
        terms_of_service_url=data.get('terms_of_service_url'),
        redirect_uris=data.get('redirect_uris', []),
        client_id=data.get('client_id'),
        client_secrets=[mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplicationClientSecrets.from_dict(item) for item in data.get('client_secrets', []) if item],
        organization_id=data.get('organization_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject(
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
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization(
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
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser(
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
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess:
        return DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsOauthInstallationsRevokeOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsOauthInstallationsRevokeOutput:
        return DashboardOrganizationsOauthInstallationsRevokeOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        scopes=[mapDashboardOrganizationsOauthInstallationsRevokeOutputScopes.from_dict(item) for item in data.get('scopes', []) if item],
        organization_id=data.get('organization_id'),
        oauth_application=mapDashboardOrganizationsOauthInstallationsRevokeOutputOauthApplication.from_dict(data.get('oauth_application')) if data.get('oauth_application') else None,
        server_side_machine_access=mapDashboardOrganizationsOauthInstallationsRevokeOutputServerSideMachineAccess.from_dict(data.get('server_side_machine_access')) if data.get('server_side_machine_access') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsOauthInstallationsRevokeOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

