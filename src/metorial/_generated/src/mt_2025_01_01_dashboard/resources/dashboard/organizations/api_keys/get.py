from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: DashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject
@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardOrganizationsApiKeysGetOutputMachineAccessUser:
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
class DashboardOrganizationsApiKeysGetOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[DashboardOrganizationsApiKeysGetOutputMachineAccessActor] = None
    instance: Optional[DashboardOrganizationsApiKeysGetOutputMachineAccessInstance] = None
    organization: Optional[DashboardOrganizationsApiKeysGetOutputMachineAccessOrganization] = None
    user: Optional[DashboardOrganizationsApiKeysGetOutputMachineAccessUser] = None
@dataclass
class DashboardOrganizationsApiKeysGetOutputRevealInfo:
    until: datetime
    forever: bool
@dataclass
class DashboardOrganizationsApiKeysGetOutput:
    object: str
    id: str
    status: str
    secret_redacted: str
    secret_redacted_long: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: DashboardOrganizationsApiKeysGetOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    reveal_info: Optional[DashboardOrganizationsApiKeysGetOutputRevealInfo] = None


class mapDashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessActor:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardOrganizationsApiKeysGetOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessInstance:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapDashboardOrganizationsApiKeysGetOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessOrganization:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessOrganization(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccessUser:
        return DashboardOrganizationsApiKeysGetOutputMachineAccessUser(
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
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputMachineAccess:
        return DashboardOrganizationsApiKeysGetOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapDashboardOrganizationsApiKeysGetOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapDashboardOrganizationsApiKeysGetOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapDashboardOrganizationsApiKeysGetOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapDashboardOrganizationsApiKeysGetOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutputRevealInfo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutputRevealInfo:
        return DashboardOrganizationsApiKeysGetOutputRevealInfo(
        until=datetime.fromisoformat(data.get('until').replace('Z', '+00:00')) if data.get('until') else None,
        forever=data.get('forever')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutputRevealInfo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsApiKeysGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsApiKeysGetOutput:
        return DashboardOrganizationsApiKeysGetOutput(
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
        machine_access=mapDashboardOrganizationsApiKeysGetOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reveal_info=mapDashboardOrganizationsApiKeysGetOutputRevealInfo.from_dict(data.get('reveal_info')) if data.get('reveal_info') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsApiKeysGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

