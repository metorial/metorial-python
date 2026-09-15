from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsCreateOutput:
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
    created_by: Optional[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None


class mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
        return DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy:
        return DashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateOutput:
        return DashboardInstanceSkillsMergeRequestsCreateOutput(
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
        created_by=mapDashboardInstanceSkillsMergeRequestsCreateOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsMergeRequestsCreateBody:
    source_skill_id: str
    title: str
    target_skill_id: Optional[str] = None
    description: Optional[str] = None


class mapDashboardInstanceSkillsMergeRequestsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsCreateBody:
        return DashboardInstanceSkillsMergeRequestsCreateBody(
        source_skill_id=data.get('source_skill_id'),
        target_skill_id=data.get('target_skill_id'),
        title=data.get('title'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

