from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveOutput:
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
    resolved_by: Optional[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None


class mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveOutput:
        return ManagementInstanceSkillsMergeRequestsItemsResolveOutput(
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
        resolved_by=mapManagementInstanceSkillsMergeRequestsItemsResolveOutputResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution:
    title: Optional[str] = None
    content: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsMergeRequestsItemsResolveBody:
    resolution_type: str
    resolution: Optional[ManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution] = None


class mapManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution:
        return ManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution(
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('fileId')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsMergeRequestsItemsResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsMergeRequestsItemsResolveBody:
        return ManagementInstanceSkillsMergeRequestsItemsResolveBody(
        resolution_type=data.get('resolution_type'),
        resolution=mapManagementInstanceSkillsMergeRequestsItemsResolveBodyResolution.from_dict(data.get('resolution')) if data.get('resolution') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsMergeRequestsItemsResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

