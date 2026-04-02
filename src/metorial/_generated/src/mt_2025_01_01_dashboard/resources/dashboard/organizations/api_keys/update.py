from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputMachineAccessUser:
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
class DashboardOrganizationsApiKeysUpdateOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[DashboardOrganizationsApiKeysUpdateOutputMachineAccessActor] = None
    instance: Optional[DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance] = None
    organization: Optional[DashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization] = None
    user: Optional[DashboardOrganizationsApiKeysUpdateOutputMachineAccessUser] = None
@dataclass
class DashboardOrganizationsApiKeysUpdateOutputRevealInfo:
    until: datetime
    forever: bool
@dataclass
class DashboardOrganizationsApiKeysUpdateOutput:
    object: str
    id: str
    status: str
    secret_redacted: str
    secret_redacted_long: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: DashboardOrganizationsApiKeysUpdateOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    reveal_info: Optional[DashboardOrganizationsApiKeysUpdateOutputRevealInfo] = None


class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessActor:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccessUser:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccessUser(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputMachineAccess:
        return DashboardOrganizationsApiKeysUpdateOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutputRevealInfo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutputRevealInfo:
        return DashboardOrganizationsApiKeysUpdateOutputRevealInfo(
        until=datetime.fromisoformat(data.get('until').replace('Z', '+00:00')) if data.get('until') else None,
        forever=data.get('forever')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutputRevealInfo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateOutput:
        return DashboardOrganizationsApiKeysUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_redacted=data.get('secret_redacted'),
        secret_redacted_long=data.get('secret_redacted_long'),
        secret=data.get('secret'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        ip_filters=data.get('ip_filters', []),
        machine_access=mapDashboardOrganizationsApiKeysUpdateOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reveal_info=mapDashboardOrganizationsApiKeysUpdateOutputRevealInfo.from_dict(data.get('reveal_info')) if data.get('reveal_info') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardOrganizationsApiKeysUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    expires_at: Optional[datetime] = None
    ip_filters: Optional[List[str]] = None


class mapDashboardOrganizationsApiKeysUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysUpdateBody:
        return DashboardOrganizationsApiKeysUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        ip_filters=data.get('ip_filters', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

