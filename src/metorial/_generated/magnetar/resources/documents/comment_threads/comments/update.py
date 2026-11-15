from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsCommentsUpdateOutputAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsCommentsUpdateOutput:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DocumentsCommentThreadsCommentsUpdateOutputAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None


class mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember:
        return DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams:
        return DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor:
        return DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer:
        return DocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsUpdateOutputAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutputAuthor:
        return DocumentsCommentThreadsCommentsUpdateOutputAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsCommentsUpdateOutputAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsCommentsUpdateOutputAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutputAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateOutput:
        return DocumentsCommentThreadsCommentsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDocumentsCommentThreadsCommentsUpdateOutputAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DocumentsCommentThreadsCommentsUpdateBody:
    body: str


class mapDocumentsCommentThreadsCommentsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsUpdateBody:
        return DocumentsCommentThreadsCommentsUpdateBody(
        body=data.get('body')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

