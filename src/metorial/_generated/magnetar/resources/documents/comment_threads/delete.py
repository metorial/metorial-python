from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsDeleteOutputCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsDeleteOutputResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputCommentsAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsDeleteOutputComments:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DocumentsCommentThreadsDeleteOutputCommentsAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None
@dataclass
class DocumentsCommentThreadsDeleteOutput:
    object: str
    id: str
    document_id: str
    status: str
    anchor_status: str
    quote: str
    created_by_id: str
    created_by: DocumentsCommentThreadsDeleteOutputCreatedBy
    comments: List[DocumentsCommentThreadsDeleteOutputComments]
    created_at: datetime
    updated_at: datetime
    resolved_by_id: Optional[str] = None
    resolved_by: Optional[DocumentsCommentThreadsDeleteOutputResolvedBy] = None
    resolved_at: Optional[datetime] = None


class mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember:
        return DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams:
        return DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor:
        return DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCreatedByConsumer:
        return DocumentsCommentThreadsDeleteOutputCreatedByConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCreatedBy:
        return DocumentsCommentThreadsDeleteOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsDeleteOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsDeleteOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember:
        return DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams:
        return DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor:
        return DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputResolvedByConsumer:
        return DocumentsCommentThreadsDeleteOutputResolvedByConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputResolvedBy:
        return DocumentsCommentThreadsDeleteOutputResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsDeleteOutputResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsDeleteOutputResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember:
        return DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams:
        return DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor:
        return DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer:
        return DocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputCommentsAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputCommentsAuthor:
        return DocumentsCommentThreadsDeleteOutputCommentsAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsDeleteOutputCommentsAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsDeleteOutputCommentsAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputCommentsAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutputComments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutputComments:
        return DocumentsCommentThreadsDeleteOutputComments(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDocumentsCommentThreadsDeleteOutputCommentsAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutputComments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsDeleteOutput:
        return DocumentsCommentThreadsDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        quote=data.get('quote'),
        created_by_id=data.get('created_by_id'),
        created_by=mapDocumentsCommentThreadsDeleteOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        resolved_by_id=data.get('resolved_by_id'),
        resolved_by=mapDocumentsCommentThreadsDeleteOutputResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        comments=[mapDocumentsCommentThreadsDeleteOutputComments.from_dict(item) for item in data.get('comments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

