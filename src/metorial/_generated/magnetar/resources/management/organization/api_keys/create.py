from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    magic_mcp_session_duration_minutes: float
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject
    sandbox_id: Optional[str] = None
@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysCreateOutputMachineAccessUser:
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
class ManagementOrganizationApiKeysCreateOutputMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[ManagementOrganizationApiKeysCreateOutputMachineAccessActor] = None
    instance: Optional[ManagementOrganizationApiKeysCreateOutputMachineAccessInstance] = None
    organization: Optional[ManagementOrganizationApiKeysCreateOutputMachineAccessOrganization] = None
    user: Optional[ManagementOrganizationApiKeysCreateOutputMachineAccessUser] = None
@dataclass
class ManagementOrganizationApiKeysCreateOutput:
    object: str
    id: str
    status: str
    secret_redacted: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: ManagementOrganizationApiKeysCreateOutputMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None


class mapManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessActor:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementOrganizationApiKeysCreateOutputMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        magic_mcp_session_duration_minutes=data.get('magic_mcp_session_duration_minutes'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessInstance:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        sandbox_id=data.get('sandbox_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationApiKeysCreateOutputMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessOrganization:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessOrganization(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccessUser:
        return ManagementOrganizationApiKeysCreateOutputMachineAccessUser(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutputMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutputMachineAccess:
        return ManagementOrganizationApiKeysCreateOutputMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapManagementOrganizationApiKeysCreateOutputMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapManagementOrganizationApiKeysCreateOutputMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapManagementOrganizationApiKeysCreateOutputMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapManagementOrganizationApiKeysCreateOutputMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutputMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateOutput:
        return ManagementOrganizationApiKeysCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_redacted=data.get('secret_redacted'),
        secret=data.get('secret'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        ip_filters=data.get('ip_filters', []),
        machine_access=mapManagementOrganizationApiKeysCreateOutputMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationApiKeysCreateBody:
    name: str
    type: Optional[str] = None
    instance_id: Optional[str] = None
    description: Optional[str] = None
    expires_at: Optional[datetime] = None
    ip_filters: Optional[List[str]] = None


class mapManagementOrganizationApiKeysCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysCreateBody:
        return ManagementOrganizationApiKeysCreateBody(
        type=data.get('type'),
        instance_id=data.get('instance_id'),
        name=data.get('name'),
        description=data.get('description'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        ip_filters=data.get('ip_filters', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

