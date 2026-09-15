from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember] = None
@dataclass
class SkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsItemsResolveOutputResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor] = None
    consumer: Optional[SkillsMergeRequestsItemsResolveOutputResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsMergeRequestsItemsResolveOutput:
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
    resolved_by: Optional[SkillsMergeRequestsItemsResolveOutputResolvedBy] = None
    resolved_at: Optional[datetime] = None
    applied_at: Optional[datetime] = None


class mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember:
        return SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams:
        return SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor:
        return SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutputResolvedByConsumer:
        return SkillsMergeRequestsItemsResolveOutputResolvedByConsumer(
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
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutputResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveOutputResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutputResolvedBy:
        return SkillsMergeRequestsItemsResolveOutputResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsMergeRequestsItemsResolveOutputResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsMergeRequestsItemsResolveOutputResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutputResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveOutput:
        return SkillsMergeRequestsItemsResolveOutput(
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
        resolved_by=mapSkillsMergeRequestsItemsResolveOutputResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        applied_at=datetime.fromisoformat(data.get('applied_at').replace('Z', '+00:00')) if data.get('applied_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsMergeRequestsItemsResolveBodyResolution:
    title: Optional[str] = None
    content: Optional[str] = None
    file_id: Optional[str] = None
@dataclass
class SkillsMergeRequestsItemsResolveBody:
    resolution_type: str
    resolution: Optional[SkillsMergeRequestsItemsResolveBodyResolution] = None


class mapSkillsMergeRequestsItemsResolveBodyResolution:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveBodyResolution:
        return SkillsMergeRequestsItemsResolveBodyResolution(
        title=data.get('title'),
        content=data.get('content'),
        file_id=data.get('fileId')
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveBodyResolution, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsMergeRequestsItemsResolveBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsMergeRequestsItemsResolveBody:
        return SkillsMergeRequestsItemsResolveBody(
        resolution_type=data.get('resolution_type'),
        resolution=mapSkillsMergeRequestsItemsResolveBodyResolution.from_dict(data.get('resolution')) if data.get('resolution') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsMergeRequestsItemsResolveBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

