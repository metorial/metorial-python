from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsListOutputItemsCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsListOutputItems:
    object: str
    id: str
    status: str
    direction: str
    base_strategy: str
    title: str
    source_skill_id: str
    target_skill_id: str
    base_target_skill_version_id: str
    requested_source_skill_version_id: str
    requested_target_skill_version_id: str
    item_count: float
    comment_count: float
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    merge_error: Optional[str] = None
    merge_error_code: Optional[str] = None
    pre_merge_target_skill_version_id: Optional[str] = None
    merged_target_skill_version_id: Optional[str] = None
    rollback_target_skill_version_id: Optional[str] = None
    created_by: Optional[SkillsMergeRequestsListOutputItemsCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None
@dataclass
class SkillsMergeRequestsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsMergeRequestsListOutput:
    items: List[SkillsMergeRequestsListOutputItems]
    pagination: SkillsMergeRequestsListOutputPagination


class mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
        return SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
        return SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
        return SkillsMergeRequestsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItemsCreatedByConsumer:
        return SkillsMergeRequestsListOutputItemsCreatedByConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItemsCreatedBy:
        return SkillsMergeRequestsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputItems:
        return SkillsMergeRequestsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        direction=data.get('direction'),
        base_strategy=data.get('base_strategy'),
        title=data.get('title'),
        description=data.get('description'),
        merge_error=data.get('merge_error'),
        merge_error_code=data.get('merge_error_code'),
        source_skill_id=data.get('source_skill_id'),
        target_skill_id=data.get('target_skill_id'),
        base_target_skill_version_id=data.get('base_target_skill_version_id'),
        requested_source_skill_version_id=data.get('requested_source_skill_version_id'),
        requested_target_skill_version_id=data.get('requested_target_skill_version_id'),
        pre_merge_target_skill_version_id=data.get('pre_merge_target_skill_version_id'),
        merged_target_skill_version_id=data.get('merged_target_skill_version_id'),
        rollback_target_skill_version_id=data.get('rollback_target_skill_version_id'),
        created_by=mapSkillsMergeRequestsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        item_count=data.get('item_count'),
        comment_count=data.get('comment_count'),
        merge_started_at=datetime.fromisoformat(data.get('merge_started_at').replace('Z', '+00:00')) if data.get('merge_started_at') else None,
        merged_at=datetime.fromisoformat(data.get('merged_at').replace('Z', '+00:00')) if data.get('merged_at') else None,
        closed_at=datetime.fromisoformat(data.get('closed_at').replace('Z', '+00:00')) if data.get('closed_at') else None,
        rolled_back_at=datetime.fromisoformat(data.get('rolled_back_at').replace('Z', '+00:00')) if data.get('rolled_back_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutputPagination:
        return SkillsMergeRequestsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListOutput:
        return SkillsMergeRequestsListOutput(
        items=[mapSkillsMergeRequestsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsMergeRequestsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMergeRequestsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class SkillsMergeRequestsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    source_skill_id: Optional[Union[str, List[str]]] = None
    target_skill_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    created_by_actor_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[SkillsMergeRequestsListQueryCreatedAt] = None


class mapSkillsMergeRequestsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsListQuery:
        return SkillsMergeRequestsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        source_skill_id=data.get('source_skill_id'),
        target_skill_id=data.get('target_skill_id'),
        status=data.get('status'),
        created_by_actor_id=data.get('created_by_actor_id'),
        created_at=mapSkillsMergeRequestsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

