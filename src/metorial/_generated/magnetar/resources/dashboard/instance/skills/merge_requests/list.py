from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputItems:
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
    created_by: Optional[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsMergeRequestsListOutput:
    items: List[DashboardInstanceSkillsMergeRequestsListOutputItems]
    pagination: DashboardInstanceSkillsMergeRequestsListOutputPagination


class mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer:
        return DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy:
        return DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputItems:
        return DashboardInstanceSkillsMergeRequestsListOutputItems(
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
        created_by=mapDashboardInstanceSkillsMergeRequestsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutputPagination:
        return DashboardInstanceSkillsMergeRequestsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListOutput:
        return DashboardInstanceSkillsMergeRequestsListOutput(
        items=[mapDashboardInstanceSkillsMergeRequestsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsMergeRequestsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsMergeRequestsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsListQuery:
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
    created_at: Optional[DashboardInstanceSkillsMergeRequestsListQueryCreatedAt] = None


class mapDashboardInstanceSkillsMergeRequestsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsListQuery:
        return DashboardInstanceSkillsMergeRequestsListQuery(
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
        created_at=mapDashboardInstanceSkillsMergeRequestsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

