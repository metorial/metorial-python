from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutputComment:
    object: str
    id: str
    actor: ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor
    body: str
    created_at: datetime
    updated_at: datetime
    skill_merge_request_item_id: Optional[str] = None
    path: Optional[str] = None
    in_reply_to_comment_id: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsEventsGetOutput:
    object: str
    id: str
    type: str
    created_at: datetime
    actor: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputActor] = None
    comment: Optional[ManagementInstanceSkillsMergeRequestsEventsGetOutputComment] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None


class mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputActor:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsEventsGetOutputActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutputComment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutputComment:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutputComment(
        object=data.get('object'),
        id=data.get('id'),
        skill_merge_request_item_id=data.get('skill_merge_request_item_id'),
        actor=mapManagementInstanceSkillsMergeRequestsEventsGetOutputCommentActor.from_dict(data.get('actor')) if data.get('actor') else None,
        body=data.get('body'),
        path=data.get('path'),
        in_reply_to_comment_id=data.get('in_reply_to_comment_id'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutputComment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsEventsGetOutput:
        return ManagementInstanceSkillsMergeRequestsEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor=mapManagementInstanceSkillsMergeRequestsEventsGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        comment=mapManagementInstanceSkillsMergeRequestsEventsGetOutputComment.from_dict(data.get('comment')) if data.get('comment') else None,
        error_code=data.get('error_code'),
        error_message=data.get('error_message'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

