from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsParticipantsGetOutputActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsParticipantsGetOutputActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsParticipantsGetOutputActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsParticipantsGetOutputActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsParticipantsGetOutputActorOrganizationActorMember] = None
@dataclass
class SkillsParticipantsGetOutputActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsParticipantsGetOutputActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsParticipantsGetOutputActorOrganizationActor] = None
    consumer: Optional[SkillsParticipantsGetOutputActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsParticipantsGetOutput:
    object: str
    id: str
    skill_id: str
    roles: List[str]
    actor: SkillsParticipantsGetOutputActor
    created_at: datetime
    updated_at: datetime


class mapSkillsParticipantsGetOutputActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutputActorOrganizationActorMember:
        return SkillsParticipantsGetOutputActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsParticipantsGetOutputActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsParticipantsGetOutputActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutputActorOrganizationActorTeams:
        return SkillsParticipantsGetOutputActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsParticipantsGetOutputActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsParticipantsGetOutputActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutputActorOrganizationActor:
        return SkillsParticipantsGetOutputActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsParticipantsGetOutputActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsParticipantsGetOutputActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsParticipantsGetOutputActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsParticipantsGetOutputActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutputActorConsumer:
        return SkillsParticipantsGetOutputActorConsumer(
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
    def to_dict(value: Union[SkillsParticipantsGetOutputActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsParticipantsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutputActor:
        return SkillsParticipantsGetOutputActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsParticipantsGetOutputActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsParticipantsGetOutputActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsParticipantsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsParticipantsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsParticipantsGetOutput:
        return SkillsParticipantsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        roles=data.get('roles', []),
        actor=mapSkillsParticipantsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsParticipantsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

