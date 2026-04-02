from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementOrganizationApiKeysGetOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject
@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysGetOutputMachineAccessUser:
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
class ManagementOrganizationApiKeysGetOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[ManagementOrganizationApiKeysGetOutputMachineAccessActor] = None
    instance: Optional[ManagementOrganizationApiKeysGetOutputMachineAccessInstance] = None
    organization: Optional[ManagementOrganizationApiKeysGetOutputMachineAccessOrganization] = None
    user: Optional[ManagementOrganizationApiKeysGetOutputMachineAccessUser] = None
@dataclass
class ManagementOrganizationApiKeysGetOutput:
    object: str
    id: str
    status: str
    secret_redacted: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: ManagementOrganizationApiKeysGetOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class mapManagementOrganizationApiKeysGetOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessActorTeams:
        return ManagementOrganizationApiKeysGetOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessActor:
        return ManagementOrganizationApiKeysGetOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementOrganizationApiKeysGetOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject:
        return ManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessInstance:
        return ManagementOrganizationApiKeysGetOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationApiKeysGetOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessOrganization:
        return ManagementOrganizationApiKeysGetOutputMachineAccessOrganization(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccessUser:
        return ManagementOrganizationApiKeysGetOutputMachineAccessUser(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutputMachineAccess:
        return ManagementOrganizationApiKeysGetOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapManagementOrganizationApiKeysGetOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapManagementOrganizationApiKeysGetOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapManagementOrganizationApiKeysGetOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapManagementOrganizationApiKeysGetOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysGetOutput:
        return ManagementOrganizationApiKeysGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_redacted=data.get('secret_redacted'),
        secret=data.get('secret'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        ip_filters=data.get('ip_filters', []),
        machine_access=mapManagementOrganizationApiKeysGetOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

