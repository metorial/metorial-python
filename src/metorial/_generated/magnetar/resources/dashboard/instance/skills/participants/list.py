from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsParticipantsListOutputItemsActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsParticipantsListOutputItemsActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsParticipantsListOutputItemsActorConsumer] = None
@dataclass
class DashboardInstanceSkillsParticipantsListOutputItems:
    object: str
    id: str
    skill_id: str
    roles: List[str]
    actor: DashboardInstanceSkillsParticipantsListOutputItemsActor
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsParticipantsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsParticipantsListOutput:
    items: List[DashboardInstanceSkillsParticipantsListOutputItems]
    pagination: DashboardInstanceSkillsParticipantsListOutputPagination


class mapDashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams:
        return DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor:
        return DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutputItemsActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputItemsActorConsumer:
        return DashboardInstanceSkillsParticipantsListOutputItemsActorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputItemsActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputItemsActor:
        return DashboardInstanceSkillsParticipantsListOutputItemsActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsParticipantsListOutputItemsActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsParticipantsListOutputItemsActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputItems:
        return DashboardInstanceSkillsParticipantsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        skill_id=data.get('skill_id'),
        roles=data.get('roles', []),
        actor=mapDashboardInstanceSkillsParticipantsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutputPagination:
        return DashboardInstanceSkillsParticipantsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsParticipantsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListOutput:
        return DashboardInstanceSkillsParticipantsListOutput(
        items=[mapDashboardInstanceSkillsParticipantsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsParticipantsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsParticipantsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceSkillsParticipantsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsParticipantsListQuery:
        return DashboardInstanceSkillsParticipantsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsParticipantsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

