from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
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
    resolved_by: Optional[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutput:
    items: List[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems]
    pagination: ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination


class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems(
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
        resolved_by=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutput:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutput(
        items=[mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    title: Optional[str] = None
    content: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
    item_id: str
    resolution_type: str
    resolution: Optional[ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsBulkResolveBody:
    items: List[ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems]


class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution(
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('fileId')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems(
        item_id=data.get('item_id'),
        resolution_type=data.get('resolution_type'),
        resolution=mapManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution.from_dict(data.get('resolution')) if data.get('resolution') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsBulkResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsBulkResolveBody:
        return ManagementInstanceSkillsMergeRequestsItemsBulkResolveBody(
        items=[mapManagementInstanceSkillsMergeRequestsItemsBulkResolveBodyItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsBulkResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

