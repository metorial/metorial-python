from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsCreateOutput:
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
    created_by: Optional[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None


class mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer:
        return ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy:
        return ManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateOutput:
        return ManagementInstanceSkillsMergeRequestsCreateOutput(
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
        created_by=mapManagementInstanceSkillsMergeRequestsCreateOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsMergeRequestsCreateBody:
    source_skill_id: str
    title: str
    target_skill_id: Optional[str] = None
    description: Optional[str] = None


class mapManagementInstanceSkillsMergeRequestsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsCreateBody:
        return ManagementInstanceSkillsMergeRequestsCreateBody(
        source_skill_id=data.get('source_skill_id'),
        target_skill_id=data.get('target_skill_id'),
        title=data.get('title'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

