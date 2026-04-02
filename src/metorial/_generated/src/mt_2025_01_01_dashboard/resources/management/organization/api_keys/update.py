from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject
@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysUpdateOutputMachineAccessUser:
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
class ManagementOrganizationApiKeysUpdateOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[ManagementOrganizationApiKeysUpdateOutputMachineAccessActor] = None
    instance: Optional[ManagementOrganizationApiKeysUpdateOutputMachineAccessInstance] = None
    organization: Optional[ManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization] = None
    user: Optional[ManagementOrganizationApiKeysUpdateOutputMachineAccessUser] = None
@dataclass
class ManagementOrganizationApiKeysUpdateOutputRevealInfo:
    until: datetime
    forever: bool
@dataclass
class ManagementOrganizationApiKeysUpdateOutput:
    object: str
    id: str
    status: str
    secret_redacted: str
    secret_redacted_long: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: ManagementOrganizationApiKeysUpdateOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    reveal_info: Optional[ManagementOrganizationApiKeysUpdateOutputRevealInfo] = None


class mapManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessActor:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementOrganizationApiKeysUpdateOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessInstance:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationApiKeysUpdateOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccessUser:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccessUser(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputMachineAccess:
        return ManagementOrganizationApiKeysUpdateOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapManagementOrganizationApiKeysUpdateOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapManagementOrganizationApiKeysUpdateOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapManagementOrganizationApiKeysUpdateOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapManagementOrganizationApiKeysUpdateOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutputRevealInfo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutputRevealInfo:
        return ManagementOrganizationApiKeysUpdateOutputRevealInfo(
        until=datetime.fromisoformat(data.get('until').replace('Z', '+00:00')) if data.get('until') else None,
        forever=data.get('forever')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutputRevealInfo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateOutput:
        return ManagementOrganizationApiKeysUpdateOutput(
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
        machine_access=mapManagementOrganizationApiKeysUpdateOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        reveal_info=mapManagementOrganizationApiKeysUpdateOutputRevealInfo.from_dict(data.get('reveal_info')) if data.get('reveal_info') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationApiKeysUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    expires_at: Optional[datetime] = None
    ip_filters: Optional[List[str]] = None


class mapManagementOrganizationApiKeysUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysUpdateBody:
        return ManagementOrganizationApiKeysUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        ip_filters=data.get('ip_filters', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

