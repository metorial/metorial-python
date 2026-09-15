from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
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
    resolved_by: Optional[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput:
    items: List[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems]
    pagination: DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination


class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems(
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
        resolved_by=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItemsResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput(
        items=[mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    title: Optional[str] = None
    content: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
    item_id: str
    resolution_type: str
    resolution: Optional[DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution] = None
@dataclass
class DashboardInstanceSkillsMergeRequestsItemsBulkResolveBody:
    items: List[DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems]


class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution(
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('fileId')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems(
        item_id=data.get('item_id'),
        resolution_type=data.get('resolution_type'),
        resolution=mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItemsResolution.from_dict(data.get('resolution')) if data.get('resolution') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsMergeRequestsItemsBulkResolveBody:
        return DashboardInstanceSkillsMergeRequestsItemsBulkResolveBody(
        items=[mapDashboardInstanceSkillsMergeRequestsItemsBulkResolveBodyItems.from_dict(item) for item in data.get('items', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsMergeRequestsItemsBulkResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

