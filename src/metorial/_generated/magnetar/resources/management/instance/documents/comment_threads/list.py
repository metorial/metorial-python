from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor] = None
    consumer: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItemsComments:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputItems:
    object: str
    id: str
    document_id: str
    status: str
    anchor_status: str
    quote: str
    created_by_id: str
    created_by: ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy
    comments: List[ManagementInstanceDocumentsCommentThreadsListOutputItemsComments]
    created_at: datetime
    updated_at: datetime
    resolved_by_id: Optional[str] = None
    resolved_by: Optional[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy] = None
    resolved_at: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceDocumentsCommentThreadsListOutput:
    items: List[ManagementInstanceDocumentsCommentThreadsListOutputItems]
    pagination: ManagementInstanceDocumentsCommentThreadsListOutputPagination


class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer(
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
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer(
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
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItemsComments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItemsComments:
        return ManagementInstanceDocumentsCommentThreadsListOutputItemsComments(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCommentsAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItemsComments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputItems:
        return ManagementInstanceDocumentsCommentThreadsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        quote=data.get('quote'),
        created_by_id=data.get('created_by_id'),
        created_by=mapManagementInstanceDocumentsCommentThreadsListOutputItemsCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        resolved_by_id=data.get('resolved_by_id'),
        resolved_by=mapManagementInstanceDocumentsCommentThreadsListOutputItemsResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        comments=[mapManagementInstanceDocumentsCommentThreadsListOutputItemsComments.from_dict(item) for item in data.get('comments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutputPagination:
        return ManagementInstanceDocumentsCommentThreadsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceDocumentsCommentThreadsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListOutput:
        return ManagementInstanceDocumentsCommentThreadsListOutput(
        items=[mapManagementInstanceDocumentsCommentThreadsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceDocumentsCommentThreadsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceDocumentsCommentThreadsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceDocumentsCommentThreadsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    anchor_status: Optional[Union[str, List[str]]] = None
    created_at: Optional[ManagementInstanceDocumentsCommentThreadsListQueryCreatedAt] = None


class mapManagementInstanceDocumentsCommentThreadsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsCommentThreadsListQuery:
        return ManagementInstanceDocumentsCommentThreadsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        created_at=mapManagementInstanceDocumentsCommentThreadsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsCommentThreadsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

