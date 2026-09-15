from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput:
    object: str
    id: str
    actor: DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor
    body: str
    created_at: datetime
    updated_at: datetime
    skill_merge_request_item_id: Optional[str] = None
    path: Optional[str] = None
    in_reply_to_comment_id: Optional[str] = None
    deleted_at: Optional[datetime] = None


class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_merge_request_item_id=data.get('skill_merge_request_item_id'),
        actor=mapDashboardInstanceSkillsMergeRequestsCommentsUpdateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        body=data.get('body'),
        path=data.get('path'),
        in_reply_to_comment_id=data.get('in_reply_to_comment_id'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsMergeRequestsCommentsUpdateBody:
    body: str


class mapDashboardInstanceSkillsMergeRequestsCommentsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCommentsUpdateBody:
        return DashboardInstanceSkillsMergeRequestsCommentsUpdateBody(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCommentsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

