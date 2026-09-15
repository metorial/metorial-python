from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
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
    created_by: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
    object: str
    id: str
    skill_merge_request_id: str
    path: str
    kind: str
    change_type: str
    status: str
    created_at: datetime
    updated_at: datetime
    resolution_type: Optional[str] = None
    conflict_reason: Optional[str] = None
    resolution: Optional[Dict[str, Any]] = None
    resolved_by: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    has_conflict: bool
    base_content: Optional[str] = None
    source_content: Optional[str] = None
    target_content: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutputItems:
    item: DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem
    base: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase] = None
    source: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource] = None
    target: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget] = None
    document_merge: Optional[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsPlanGetOutput:
    object: str
    merge_request: DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest
    items: List[DashboardInstanceSkillsMergeRequestsPlanGetOutputItems]


class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest(
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
        created_by=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem(
        object=data.get('object'),
        id=data.get('id'),
        skill_merge_request_id=data.get('skill_merge_request_id'),
        path=data.get('path'),
        kind=data.get('kind'),
        change_type=data.get('change_type'),
        status=data.get('status'),
        resolution_type=data.get('resolution_type'),
        conflict_reason=data.get('conflict_reason'),
        resolution=data.get('resolution'),
        resolved_by=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge(
        base_content=data.get('base_content'),
        source_content=data.get('source_content'),
        target_content=data.get('target_content'),
        has_conflict=data.get('has_conflict')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutputItems:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutputItems(
        item=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsItem.from_dict(data.get('item')) if data.get('item') else None,
        base=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsBase.from_dict(data.get('base')) if data.get('base') else None,
        source=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsSource.from_dict(data.get('source')) if data.get('source') else None,
        target=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        document_merge=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge.from_dict(data.get('document_merge')) if data.get('document_merge') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsPlanGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsPlanGetOutput:
        return DashboardInstanceSkillsMergeRequestsPlanGetOutput(
        object=data.get('object'),
        merge_request=mapDashboardInstanceSkillsMergeRequestsPlanGetOutputMergeRequest.from_dict(data.get('merge_request')) if data.get('merge_request') else None,
        items=[mapDashboardInstanceSkillsMergeRequestsPlanGetOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsPlanGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

