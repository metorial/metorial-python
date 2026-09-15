from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputItems:
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
    resolved_by: Optional[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class SkillsMergeRequestsItemsBulkResolveOutput:
    items: List[SkillsMergeRequestsItemsBulkResolveOutputItems]
    pagination: SkillsMergeRequestsItemsBulkResolveOutputPagination


class mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
        return SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
        return SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
        return SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
        return SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
        return SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputItems:
        return SkillsMergeRequestsItemsBulkResolveOutputItems(
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
        resolved_by=mapSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutputPagination:
        return SkillsMergeRequestsItemsBulkResolveOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveOutput:
        return SkillsMergeRequestsItemsBulkResolveOutput(
        items=[mapSkillsMergeRequestsItemsBulkResolveOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapSkillsMergeRequestsItemsBulkResolveOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    title: Optional[str] = None
    content: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveBodyItems:
    item_id: str
    resolution_type: str
    resolution: Optional[SkillsMergeRequestsItemsBulkResolveBodyItemsResolution] = None
@dataclass
class SkillsMergeRequestsItemsBulkResolveBody:
    items: List[SkillsMergeRequestsItemsBulkResolveBodyItems]


class mapSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
        return SkillsMergeRequestsItemsBulkResolveBodyItemsResolution(
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('fileId')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveBodyItemsResolution, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveBodyItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveBodyItems:
        return SkillsMergeRequestsItemsBulkResolveBodyItems(
        item_id=data.get('item_id'),
        resolution_type=data.get('resolution_type'),
        resolution=mapSkillsMergeRequestsItemsBulkResolveBodyItemsResolution.from_dict(data.get('resolution')) if data.get('resolution') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveBodyItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsBulkResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsBulkResolveBody:
        return SkillsMergeRequestsItemsBulkResolveBody(
        items=[mapSkillsMergeRequestsItemsBulkResolveBodyItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsBulkResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

