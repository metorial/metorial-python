from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputMergeRequest:
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
    created_by: Optional[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy] = None
    merge_started_at: Optional[datetime] = None
    merged_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    rolled_back_at: Optional[datetime] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsItem:
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
    resolved_by: Optional[SkillsMergeRequestsPlanGetOutputItemsItemResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsBase:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsSource:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsTarget:
    kind: str
    path: str
    file_id: Optional[str] = None
    document_id: Optional[str] = None
    document_title: Optional[str] = None
    document_version_id: Optional[str] = None
    content: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    has_conflict: bool
    base_content: Optional[str] = None
    source_content: Optional[str] = None
    target_content: Optional[str] = None
@dataclass
class SkillsMergeRequestsPlanGetOutputItems:
    item: SkillsMergeRequestsPlanGetOutputItemsItem
    base: Optional[SkillsMergeRequestsPlanGetOutputItemsBase] = None
    source: Optional[SkillsMergeRequestsPlanGetOutputItemsSource] = None
    target: Optional[SkillsMergeRequestsPlanGetOutputItemsTarget] = None
    document_merge: Optional[SkillsMergeRequestsPlanGetOutputItemsDocumentMerge] = None
@dataclass
class SkillsMergeRequestsPlanGetOutput:
    object: str
    merge_request: SkillsMergeRequestsPlanGetOutputMergeRequest
    items: List[SkillsMergeRequestsPlanGetOutputItems]


class mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember:
        return SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams:
        return SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor:
        return SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer:
        return SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy:
        return SkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputMergeRequest:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputMergeRequest:
        return SkillsMergeRequestsPlanGetOutputMergeRequest(
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
        created_by=mapSkillsMergeRequestsPlanGetOutputMergeRequestCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
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
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputMergeRequest, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember:
        return SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams:
        return SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor:
        return SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer:
        return SkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItemResolvedBy:
        return SkillsMergeRequestsPlanGetOutputItemsItemResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItemResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsItem:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsItem:
        return SkillsMergeRequestsPlanGetOutputItemsItem(
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
        resolved_by=mapSkillsMergeRequestsPlanGetOutputItemsItemResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsItem, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsBase:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsBase:
        return SkillsMergeRequestsPlanGetOutputItemsBase(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsBase, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsSource:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsSource:
        return SkillsMergeRequestsPlanGetOutputItemsSource(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsSource, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsTarget:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsTarget:
        return SkillsMergeRequestsPlanGetOutputItemsTarget(
        kind=data.get('kind'),
        path=data.get('path'),
        file_id=data.get('file_id'),
        document_id=data.get('document_id'),
        document_title=data.get('document_title'),
        document_version_id=data.get('document_version_id'),
        content=data.get('content')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsTarget, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItemsDocumentMerge:
        return SkillsMergeRequestsPlanGetOutputItemsDocumentMerge(
        base_content=data.get('base_content'),
        source_content=data.get('source_content'),
        target_content=data.get('target_content'),
        has_conflict=data.get('has_conflict')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItemsDocumentMerge, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutputItems:
        return SkillsMergeRequestsPlanGetOutputItems(
        item=mapSkillsMergeRequestsPlanGetOutputItemsItem.from_dict(data.get('item')) if data.get('item') else None,
        base=mapSkillsMergeRequestsPlanGetOutputItemsBase.from_dict(data.get('base')) if data.get('base') else None,
        source=mapSkillsMergeRequestsPlanGetOutputItemsSource.from_dict(data.get('source')) if data.get('source') else None,
        target=mapSkillsMergeRequestsPlanGetOutputItemsTarget.from_dict(data.get('target')) if data.get('target') else None,
        document_merge=mapSkillsMergeRequestsPlanGetOutputItemsDocumentMerge.from_dict(data.get('document_merge')) if data.get('document_merge') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsPlanGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsPlanGetOutput:
        return SkillsMergeRequestsPlanGetOutput(
        object=data.get('object'),
        merge_request=mapSkillsMergeRequestsPlanGetOutputMergeRequest.from_dict(data.get('merge_request')) if data.get('merge_request') else None,
        items=[mapSkillsMergeRequestsPlanGetOutputItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsPlanGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

