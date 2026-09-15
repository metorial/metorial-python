from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
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
    created_by: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
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
    resolved_by: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    has_conflict: bool
    base_content: Optional[str] = None
    source_content: Optional[str] = None
    target_content: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutputItems:
    item: ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem
    base: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase] = None
    source: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource] = None
    target: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget] = None
    document_merge: Optional[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsPlanGetOutput:
    object: str
    merge_request: ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest
    items: List[ManagementInstanceSkillsMergeRequestsPlanGetOutputItems]


class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest(
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
        created_by=mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem(
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
        resolved_by=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge(
        base_content=data.get('base_content'),
        source_content=data.get('source_content'),
        target_content=data.get('target_content'),
        has_conflict=data.get('has_conflict')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutputItems:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutputItems(
        item=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsItem.from_dict(data.get('item')) if data.get('item') else None,
        base=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsBase.from_dict(data.get('base')) if data.get('base') else None,
        source=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsSource.from_dict(data.get('source')) if data.get('source') else None,
        target=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        document_merge=mapManagementInstanceSkillsMergeRequestsPlanGetOutputItemsDocumentMerge.from_dict(data.get('document_merge')) if data.get('document_merge') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsPlanGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsPlanGetOutput:
        return ManagementInstanceSkillsMergeRequestsPlanGetOutput(
        object=data.get('object'),
        merge_request=mapManagementInstanceSkillsMergeRequestsPlanGetOutputMergeRequest.from_dict(data.get('merge_request')) if data.get('merge_request') else None,
        items=[mapManagementInstanceSkillsMergeRequestsPlanGetOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsPlanGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

