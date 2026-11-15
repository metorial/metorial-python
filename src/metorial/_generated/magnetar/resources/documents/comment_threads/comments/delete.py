from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsCommentsDeleteOutputAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsCommentsDeleteOutput:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DocumentsCommentThreadsCommentsDeleteOutputAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None


class mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember:
        return DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams:
        return DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor:
        return DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer:
        return DocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsDeleteOutputAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutputAuthor:
        return DocumentsCommentThreadsCommentsDeleteOutputAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsCommentsDeleteOutputAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsCommentsDeleteOutputAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutputAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsCommentsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsCommentsDeleteOutput:
        return DocumentsCommentThreadsCommentsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDocumentsCommentThreadsCommentsDeleteOutputAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsCommentsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

