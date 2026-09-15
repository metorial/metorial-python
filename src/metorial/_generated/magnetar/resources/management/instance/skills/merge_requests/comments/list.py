from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputItems:
    object: str
    id: str
    actor: ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor
    body: str
    created_at: datetime
    updated_at: datetime
    skill_merge_request_item_id: Optional[str] = None
    path: Optional[str] = None
    in_reply_to_comment_id: Optional[str] = None
    deleted_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListOutput:
    items: List[ManagementInstanceSkillsMergeRequestsCommentsListOutputItems]
    pagination: ManagementInstanceSkillsMergeRequestsCommentsListOutputPagination


class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputItems:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        skill_merge_request_item_id=data.get('skill_merge_request_item_id'),
        actor=mapManagementInstanceSkillsMergeRequestsCommentsListOutputItemsActor.from_dict(data.get('actor')) if data.get('actor') else None,
        body=data.get('body'),
        path=data.get('path'),
        in_reply_to_comment_id=data.get('in_reply_to_comment_id'),
        deleted_at=datetime.fromisoformat(data.get('deleted_at').replace('Z', '+00:00')) if data.get('deleted_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutputPagination:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCommentsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListOutput:
        return ManagementInstanceSkillsMergeRequestsCommentsListOutput(
        items=[mapManagementInstanceSkillsMergeRequestsCommentsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsMergeRequestsCommentsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsMergeRequestsCommentsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    item_id: Optional[str] = None


class mapManagementInstanceSkillsMergeRequestsCommentsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCommentsListQuery:
        return ManagementInstanceSkillsMergeRequestsCommentsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        item_id=data.get('item_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCommentsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

