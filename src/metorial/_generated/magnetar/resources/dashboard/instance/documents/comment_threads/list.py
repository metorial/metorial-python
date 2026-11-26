from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor] = None
    consumer: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItemsComments:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputItems:
    object: str
    id: str
    document_id: str
    status: str
    anchor_status: str
    quote: str
    created_by_id: str
    created_by: DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy
    comments: List[DashboardInstanceDocumentsCommentThreadsListOutputItemsComments]
    created_at: datetime
    updated_at: datetime
    resolved_by_id: Optional[str] = None
    resolved_by: Optional[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy] = None
    resolved_at: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListOutput:
    object: str
    items: List[DashboardInstanceDocumentsCommentThreadsListOutputItems]
    pagination: DashboardInstanceDocumentsCommentThreadsListOutputPagination


class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer(
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
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer(
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
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItemsComments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItemsComments:
        return DashboardInstanceDocumentsCommentThreadsListOutputItemsComments(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItemsComments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputItems:
        return DashboardInstanceDocumentsCommentThreadsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        quote=data.get('quote'),
        created_by_id=data.get('created_by_id'),
        created_by=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        resolved_by_id=data.get('resolved_by_id'),
        resolved_by=mapDashboardInstanceDocumentsCommentThreadsListOutputItemsResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        comments=[mapDashboardInstanceDocumentsCommentThreadsListOutputItemsComments.from_dict(item) for item in data.get('comments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutputPagination:
        return DashboardInstanceDocumentsCommentThreadsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceDocumentsCommentThreadsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListOutput:
        return DashboardInstanceDocumentsCommentThreadsListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceDocumentsCommentThreadsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceDocumentsCommentThreadsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceDocumentsCommentThreadsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceDocumentsCommentThreadsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    anchor_status: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceDocumentsCommentThreadsListQueryCreatedAt] = None


class mapDashboardInstanceDocumentsCommentThreadsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceDocumentsCommentThreadsListQuery:
        return DashboardInstanceDocumentsCommentThreadsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        created_at=mapDashboardInstanceDocumentsCommentThreadsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceDocumentsCommentThreadsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

