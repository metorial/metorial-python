from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputCreatedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputCreatedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsUpdateOutputCreatedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputResolvedByConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputResolvedBy:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsUpdateOutputResolvedByConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputCommentsAuthor:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor] = None
    consumer: Optional[DocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class DocumentsCommentThreadsUpdateOutputComments:
    object: str
    id: str
    thread_id: str
    body: str
    author_id: str
    author: DocumentsCommentThreadsUpdateOutputCommentsAuthor
    created_at: datetime
    updated_at: datetime
    edited_at: Optional[datetime] = None
@dataclass
class DocumentsCommentThreadsUpdateOutput:
    object: str
    id: str
    document_id: str
    status: str
    anchor_status: str
    quote: str
    created_by_id: str
    created_by: DocumentsCommentThreadsUpdateOutputCreatedBy
    comments: List[DocumentsCommentThreadsUpdateOutputComments]
    created_at: datetime
    updated_at: datetime
    resolved_by_id: Optional[str] = None
    resolved_by: Optional[DocumentsCommentThreadsUpdateOutputResolvedBy] = None
    resolved_at: Optional[datetime] = None


class mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember:
        return DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams:
        return DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor:
        return DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCreatedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCreatedByConsumer:
        return DocumentsCommentThreadsUpdateOutputCreatedByConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCreatedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCreatedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCreatedBy:
        return DocumentsCommentThreadsUpdateOutputCreatedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsUpdateOutputCreatedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsUpdateOutputCreatedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCreatedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember:
        return DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams:
        return DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor:
        return DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputResolvedByConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputResolvedByConsumer:
        return DocumentsCommentThreadsUpdateOutputResolvedByConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputResolvedByConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputResolvedBy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputResolvedBy:
        return DocumentsCommentThreadsUpdateOutputResolvedBy(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsUpdateOutputResolvedByOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsUpdateOutputResolvedByConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputResolvedBy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember:
        return DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams:
        return DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor:
        return DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer:
        return DocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer(
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
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputCommentsAuthor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputCommentsAuthor:
        return DocumentsCommentThreadsUpdateOutputCommentsAuthor(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDocumentsCommentThreadsUpdateOutputCommentsAuthorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDocumentsCommentThreadsUpdateOutputCommentsAuthorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputCommentsAuthor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutputComments:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutputComments:
        return DocumentsCommentThreadsUpdateOutputComments(
        object=data.get('object'),
        id=data.get('id'),
        thread_id=data.get('thread_id'),
        body=data.get('body'),
        author_id=data.get('author_id'),
        author=mapDocumentsCommentThreadsUpdateOutputCommentsAuthor.from_dict(data.get('author')) if data.get('author') else None,
        edited_at=datetime.fromisoformat(data.get('edited_at').replace('Z', '+00:00')) if data.get('edited_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutputComments, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDocumentsCommentThreadsUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateOutput:
        return DocumentsCommentThreadsUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        document_id=data.get('document_id'),
        status=data.get('status'),
        anchor_status=data.get('anchor_status'),
        quote=data.get('quote'),
        created_by_id=data.get('created_by_id'),
        created_by=mapDocumentsCommentThreadsUpdateOutputCreatedBy.from_dict(data.get('created_by')) if data.get('created_by') else None,
        resolved_by_id=data.get('resolved_by_id'),
        resolved_by=mapDocumentsCommentThreadsUpdateOutputResolvedBy.from_dict(data.get('resolved_by')) if data.get('resolved_by') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        comments=[mapDocumentsCommentThreadsUpdateOutputComments.from_dict(item) for item in data.get('comments', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DocumentsCommentThreadsUpdateBody:
    status: Optional[str] = None


class mapDocumentsCommentThreadsUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsCommentThreadsUpdateBody:
        return DocumentsCommentThreadsUpdateBody(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsCommentThreadsUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

