from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class StoresParticipantsGetOutputActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class StoresParticipantsGetOutputActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresParticipantsGetOutputActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[StoresParticipantsGetOutputActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[StoresParticipantsGetOutputActorOrganizationActorMember] = None
@dataclass
class StoresParticipantsGetOutputActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class StoresParticipantsGetOutputActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[StoresParticipantsGetOutputActorOrganizationActor] = None
    consumer: Optional[StoresParticipantsGetOutputActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class StoresParticipantsGetOutputSurfacesActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class StoresParticipantsGetOutputSurfacesActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class StoresParticipantsGetOutputSurfacesActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[StoresParticipantsGetOutputSurfacesActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[StoresParticipantsGetOutputSurfacesActorOrganizationActorMember] = None
@dataclass
class StoresParticipantsGetOutputSurfacesActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class StoresParticipantsGetOutputSurfacesActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[StoresParticipantsGetOutputSurfacesActorOrganizationActor] = None
    consumer: Optional[StoresParticipantsGetOutputSurfacesActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class StoresParticipantsGetOutputSurfaces:
    id: str
    roles: List[str]
    actor: StoresParticipantsGetOutputSurfacesActor
    created_at: datetime
    last_active_at: Optional[datetime] = None
@dataclass
class StoresParticipantsGetOutput:
    object: str
    id: str
    store_id: str
    permissions: List[str]
    roles: List[str]
    actor: StoresParticipantsGetOutputActor
    created_at: datetime
    updated_at: datetime
    surfaces: Optional[List[StoresParticipantsGetOutputSurfaces]] = None
    last_active_at: Optional[datetime] = None


class mapStoresParticipantsGetOutputActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputActorOrganizationActorMember:
        return StoresParticipantsGetOutputActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputActorOrganizationActorTeams:
        return StoresParticipantsGetOutputActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputActorOrganizationActor:
        return StoresParticipantsGetOutputActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapStoresParticipantsGetOutputActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapStoresParticipantsGetOutputActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputActorConsumer:
        return StoresParticipantsGetOutputActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputActor:
        return StoresParticipantsGetOutputActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapStoresParticipantsGetOutputActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapStoresParticipantsGetOutputActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfacesActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfacesActorOrganizationActorMember:
        return StoresParticipantsGetOutputSurfacesActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfacesActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfacesActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfacesActorOrganizationActorTeams:
        return StoresParticipantsGetOutputSurfacesActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfacesActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfacesActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfacesActorOrganizationActor:
        return StoresParticipantsGetOutputSurfacesActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapStoresParticipantsGetOutputSurfacesActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapStoresParticipantsGetOutputSurfacesActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfacesActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfacesActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfacesActorConsumer:
        return StoresParticipantsGetOutputSurfacesActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfacesActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfacesActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfacesActor:
        return StoresParticipantsGetOutputSurfacesActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapStoresParticipantsGetOutputSurfacesActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapStoresParticipantsGetOutputSurfacesActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfacesActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutputSurfaces:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutputSurfaces:
        return StoresParticipantsGetOutputSurfaces(
        id=data.get('id'),
        roles=data.get('roles', []),
        actor=mapStoresParticipantsGetOutputSurfacesActor.from_dict(data.get('actor')) if data.get('actor') else None,
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutputSurfaces, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapStoresParticipantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> StoresParticipantsGetOutput:
        return StoresParticipantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        store_id=data.get('store_id'),
        permissions=data.get('permissions', []),
        roles=data.get('roles', []),
        actor=mapStoresParticipantsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        surfaces=[mapStoresParticipantsGetOutputSurfaces.from_dict(item) for item in data.get('surfaces', []) if item],
        last_active_at=datetime.fromisoformat(data.get('last_active_at').replace('Z', '+00:00')) if data.get('last_active_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[StoresParticipantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

