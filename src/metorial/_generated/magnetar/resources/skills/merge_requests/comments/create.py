from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsCommentsCreateOutputActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsCommentsCreateOutputActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsCommentsCreateOutputActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsCommentsCreateOutputActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsCommentsCreateOutput:
    object: str
    id: str
    actor: SkillsMergeRequestsCommentsCreateOutputActor
    body: str
    created_at: datetime
    updated_at: datetime
    skill_merge_request_item_id: Optional[str] = None
    path: Optional[str] = None
    in_reply_to_comment_id: Optional[str] = None
    deleted_at: Optional[datetime] = None


class mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember:
        return SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams:
        return SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutputActorOrganizationActor:
        return SkillsMergeRequestsCommentsCreateOutputActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutputActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsCommentsCreateOutputActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutputActorConsumer:
        return SkillsMergeRequestsCommentsCreateOutputActorConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutputActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsCommentsCreateOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutputActor:
        return SkillsMergeRequestsCommentsCreateOutputActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsCommentsCreateOutputActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsCommentsCreateOutputActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsCommentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateOutput:
        return SkillsMergeRequestsCommentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        skill_merge_request_item_id=data.get('skill_merge_request_item_id'),
        actor=mapSkillsMergeRequestsCommentsCreateOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        body=data.get('body'),
        path=data.get('path'),
        in_reply_to_comment_id=data.get('in_reply_to_comment_id'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMergeRequestsCommentsCreateBody:
    body: str
    item_id: Optional[str] = None
    in_reply_to_comment_id: Optional[str] = None
    path: Optional[str] = None


class mapSkillsMergeRequestsCommentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsCommentsCreateBody:
        return SkillsMergeRequestsCommentsCreateBody(
        item_id=data.get('item_id'),
        in_reply_to_comment_id=data.get('in_reply_to_comment_id'),
        body=data.get('body'),
        path=data.get('path')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsCommentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

