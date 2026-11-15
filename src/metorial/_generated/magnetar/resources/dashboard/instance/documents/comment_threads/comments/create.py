from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None


class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer(
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
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDashboardInstanceDocumentsCommentThreadsCommentsCreateOutputAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceDocumentsCommentThreadsCommentsCreateBody:
    body: str


class mapDashboardInstanceDocumentsCommentThreadsCommentsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsCommentsCreateBody:
        return DashboardInstanceDocumentsCommentThreadsCommentsCreateBody(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsCommentsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

