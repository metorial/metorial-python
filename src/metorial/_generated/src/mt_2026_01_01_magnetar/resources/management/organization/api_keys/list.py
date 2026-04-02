from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject:
    object: str
    id: str
    status: str
    slug: str
    name: str
    organization_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessInstance:
    object: str
    id: str
    slug: str
    name: str
    organization_id: str
    type: str
    created_at: datetime
    updated_at: datetime
    project: ManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject
@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization:
    object: str
    id: str
    type: str
    slug: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementOrganizationApiKeysListOutputItemsMachineAccessUser:
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
class ManagementOrganizationApiKeysListOutputItemsMachineAccess:
    object: str
    id: str
    status: str
    type: str
    name: str
    last_used_at: datetime
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    actor: Optional[ManagementOrganizationApiKeysListOutputItemsMachineAccessActor] = None
    instance: Optional[ManagementOrganizationApiKeysListOutputItemsMachineAccessInstance] = None
    organization: Optional[ManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization] = None
    user: Optional[ManagementOrganizationApiKeysListOutputItemsMachineAccessUser] = None
@dataclass
class ManagementOrganizationApiKeysListOutputItems:
    object: str
    id: str
    status: str
    secret_redacted: str
    type: str
    name: str
    ip_filters: List[str]
    machine_access: ManagementOrganizationApiKeysListOutputItemsMachineAccess
    created_at: datetime
    updated_at: datetime
    secret: Optional[str] = None
    description: Optional[str] = None
    deleted_at: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
@dataclass
class ManagementOrganizationApiKeysListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationApiKeysListOutput:
    items: List[ManagementOrganizationApiKeysListOutputItems]
    pagination: ManagementOrganizationApiKeysListOutputPagination


class mapManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccessActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessActor:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementOrganizationApiKeysListOutputItemsMachineAccessActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccessInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessInstance:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessInstance(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        organization_id=data.get('organization_id'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        project=mapManagementOrganizationApiKeysListOutputItemsMachineAccessInstanceProject.from_dict(data.get('project')) if data.get('project') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccessUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccessUser:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccessUser(
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
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccessUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItemsMachineAccess:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItemsMachineAccess:
        return ManagementOrganizationApiKeysListOutputItemsMachineAccess(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type'),
        name=data.get('name'),
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        actor=mapManagementOrganizationApiKeysListOutputItemsMachineAccessActor.from_dict(data.get('actor')) if data.get('actor') else None,
        instance=mapManagementOrganizationApiKeysListOutputItemsMachineAccessInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        organization=mapManagementOrganizationApiKeysListOutputItemsMachineAccessOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        user=mapManagementOrganizationApiKeysListOutputItemsMachineAccessUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItemsMachineAccess, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputItems:
        return ManagementOrganizationApiKeysListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        secret_redacted=data.get('secret_redacted'),
        secret=data.get('secret'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        ip_filters=data.get('ip_filters', []),
        machine_access=mapManagementOrganizationApiKeysListOutputItemsMachineAccess.from_dict(data.get('machine_access')) if data.get('machine_access') else None,
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutputPagination:
        return ManagementOrganizationApiKeysListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationApiKeysListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListOutput:
        return ManagementOrganizationApiKeysListOutput(
        items=[mapManagementOrganizationApiKeysListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationApiKeysListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementOrganizationApiKeysListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    type: Optional[str] = None
    instance_id: Optional[str] = None


class mapManagementOrganizationApiKeysListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationApiKeysListQuery:
        return ManagementOrganizationApiKeysListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        type=data.get('type'),
        instance_id=data.get('instance_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationApiKeysListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

